"""Round-286 R4 Loop-14 materials/spreads/strategic-resources price-validation pack.

This module converts ``docs/round/round_286.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: a lithium squeeze headline can move battery-material stocks for
a day, but it is still only event premium unless customer call-off, ASP,
inventory valuation and margin prove the price move became FCF.
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


ROUND286_SOURCE_ROUND_PATH = "docs/round/round_286.md"
ROUND286_ANALYST_ROUND_ID = "round_214"
ROUND286_LARGE_SECTOR = "MATERIALS_SPREADS_STRATEGIC_RESOURCES"
ROUND286_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round286_r4_loop14_materials_spreads_strategic_resources_price_validation"
ROUND286_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop14_round286.jsonl"
ROUND286_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round286_r4_loop14_materials_spreads_strategic_resources_price_validation_audit.json"

ROUND286_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "PETROCHEMICAL_SPREAD_COLLAPSE_4C": E2RArchetype.PETROCHEMICAL_SPREAD_COLLAPSE_4C.value,
    "PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN": E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN.value,
    "STEEL_ANTI_DUMPING_EVENT_PREMIUM": E2RArchetype.STEEL_ANTI_DUMPING_EVENT_PREMIUM.value,
    "STRATEGIC_METAL_CONTROL_PREMIUM_4B": E2RArchetype.STRATEGIC_METAL_CONTROL_PREMIUM_4B.value,
    "LITHIUM_RESOURCE_INTEGRATION_STAGE2": E2RArchetype.LITHIUM_RESOURCE_INTEGRATION_STAGE2.value,
    "LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM": E2RArchetype.LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM.value,
    "BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C": E2RArchetype.BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C.value,
    "RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C": E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C.value,
    "CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2": E2RArchetype.CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2.value,
}

ROUND286_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "spread_margin_realization_confirmed",
    "capacity_cut_actual_execution_confirmed",
    "plant_shutdown_discipline_confirmed",
    "commodity_price_sensitivity_measured",
    "customer_calloff_visibility_confirmed",
    "contract_value_durability_confirmed",
    "resource_offtake_utilization_confirmed",
    "export_license_continuity_confirmed",
    "governance_dilution_control_confirmed",
    "inventory_valuation_risk_controlled",
    "price_path_after_evidence",
)

ROUND286_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "commodity_rebound_headline_only",
    "tariff_relief_only",
    "control_premium_only",
    "capacity_restructuring_policy_only",
    "mine_stake_without_processing_margin",
    "CATL_license_suspension_sentiment",
    "nonbinding_supply_agreement",
    "signed_contract_without_calloff",
    "rare_earth_truce_without_actual_exports",
)

ROUND286_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "control_premium_20pct_plus",
    "CATL_lithium_license_headline_8pct_plus",
    "anti_dumping_tariff_5pct_plus",
    "restructuring_policy_support_before_spread",
    "strategic_mineral_or_rare_earth_headline_before_license",
    "mine_stake_acquisition_before_processing_utilization",
)

ROUND286_HARD_4C_GATES: tuple[str, ...] = (
    "signed_contract_value_collapse",
    "customer_calloff_failure",
    "petrochemical_spread_collapse_with_deep_operating_loss",
    "rare_earth_export_license_denial_or_shipment_failure",
    "tariff_reversal_or_export_tariff_shock",
    "forced_plant_shutdown_without_balance_sheet_relief",
    "commodity_price_collapse_breaking_mine_or_offtake_economics",
    "governance_dilution_accounting_risk_after_control_premium",
)

ROUND286_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "reported_event_price_anchor",
    "operating_loss_anchor",
    "contract_value_anchor",
    "tariff_rate_anchor",
    "ownership_stake_anchor",
    "production_capacity_anchor",
    "export_control_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round286ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round286ShadowWeightRow:
    archetype: E2RArchetype
    spread_margin_realization: int
    restructuring_execution: int
    customer_calloff_visibility: int
    resource_offtake_utilization: int
    export_license_continuity: int
    governance_dilution_control: int
    commodity_price_sensitivity: int
    inventory_valuation_control: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "spread_margin_realization": _signed(self.spread_margin_realization),
            "restructuring_execution": _signed(self.restructuring_execution),
            "customer_calloff_visibility": _signed(self.customer_calloff_visibility),
            "resource_offtake_utilization": _signed(self.resource_offtake_utilization),
            "export_license_continuity": _signed(self.export_license_continuity),
            "governance_dilution_control": _signed(self.governance_dilution_control),
            "commodity_price_sensitivity": _signed(self.commodity_price_sensitivity),
            "inventory_valuation_control": _signed(self.inventory_valuation_control),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round286DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round286CaseCandidate:
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
    hard_4c_watch_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage1_price_anchor: float | None
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


ROUND286_SCORE_ADJUSTMENTS: tuple[Round286ScoreAdjustment, ...] = (
    Round286ScoreAdjustment("spread_margin_realization", 5, "raise", "소재/화학은 가격보다 제품 스프레드와 현금마진이 먼저다."),
    Round286ScoreAdjustment("capacity_cut_actual_execution", 5, "raise", "구조조정은 발표가 아니라 실제 shutdown과 공급규율이 필요하다."),
    Round286ScoreAdjustment("customer_calloff_visibility", 5, "raise", "장기 소재 계약은 실제 고객 call-off가 있어야 매출이 된다."),
    Round286ScoreAdjustment("contract_value_durability", 5, "raise", "초기 계약금액이 줄어들면 Stage 4C가 될 수 있다."),
    Round286ScoreAdjustment("resource_offtake_utilization", 5, "raise", "광산 지분은 offtake와 가공설비 utilization으로 닫혀야 한다."),
    Round286ScoreAdjustment("export_license_continuity", 5, "raise", "희토류/전략자원은 실제 수출허가와 선적 지속성이 핵심이다."),
    Round286ScoreAdjustment("governance_dilution_control", 5, "raise", "지배권 프리미엄은 희석·거버넌스 통과 전에는 operating Green이 아니다."),
    Round286ScoreAdjustment("inventory_valuation_risk_controlled", 4, "raise", "리튬·양극재는 재고평가손실과 판가연동을 같이 봐야 한다."),
    Round286ScoreAdjustment("commodity_rebound_headline_only", -5, "lower", "상품가격 반등 headline만으로 Green을 만들지 않는다."),
    Round286ScoreAdjustment("tariff_relief_only", -5, "lower", "반덤핑 관세는 수요와 스프레드가 없으면 event premium이다."),
    Round286ScoreAdjustment("control_premium_only", -5, "lower", "지배권 프리미엄은 FCF 증거가 아니다."),
    Round286ScoreAdjustment("capacity_restructuring_policy_only", -5, "lower", "정책 지원만 있고 스프레드 회복이 없으면 Stage 2다."),
    Round286ScoreAdjustment("mine_stake_without_processing_margin", -5, "lower", "광산 지분만 있고 가공마진이 없으면 Green 금지다."),
    Round286ScoreAdjustment("CATL_license_suspension_sentiment", -5, "lower", "CATL 허가 중단 감성 랠리는 마진 확인 전 event premium이다."),
    Round286ScoreAdjustment("nonbinding_supply_agreement", -5, "lower", "non-binding lithium agreement는 계약/마진으로 보지 않는다."),
    Round286ScoreAdjustment("signed_contract_without_calloff", -5, "lower", "서명 계약만 있고 실제 발주가 없으면 Stage 4C 리스크다."),
    Round286ScoreAdjustment("rare_earth_truce_without_actual_exports", -5, "lower", "희토류 휴전 headline은 실제 수출량 회복 전 Green이 아니다."),
)


ROUND286_SHADOW_WEIGHT_ROWS: tuple[Round286ShadowWeightRow, ...] = (
    Round286ShadowWeightRow(E2RArchetype.PETROCHEMICAL_SPREAD_COLLAPSE_4C, 5, 5, 0, 0, 0, 2, 5, 5, -5, 5, 5, "Petrochemical oversupply and deep losses are RedTeam until spread/cash margin recover."),
    Round286ShadowWeightRow(E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN, 5, 5, 0, 0, 0, 3, 4, 4, -4, 5, 4, "Daesan restructuring is Stage 2 until shutdown execution and spread recovery close."),
    Round286ShadowWeightRow(E2RArchetype.STEEL_ANTI_DUMPING_EVENT_PREMIUM, 5, 2, 0, 0, 0, 2, 4, 4, -5, 5, 4, "Anti-dumping relief is useful but needs demand and spread."),
    Round286ShadowWeightRow(E2RArchetype.STRATEGIC_METAL_CONTROL_PREMIUM_4B, 3, 1, 0, 0, 0, 5, 3, 3, -5, 5, 5, "Korea Zinc control premium is 4B-watch before operating evidence."),
    Round286ShadowWeightRow(E2RArchetype.LITHIUM_RESOURCE_INTEGRATION_STAGE2, 4, 2, 4, 5, 0, 2, 5, 5, -4, 4, 4, "Mine stake is Stage 2 until offtake, processing utilization and lithium price support confirm."),
    Round286ShadowWeightRow(E2RArchetype.LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM, 3, 0, 3, 2, 0, 1, 5, 5, -5, 5, 4, "Lithium squeeze rally needs ASP, inventory and margin before Green."),
    Round286ShadowWeightRow(E2RArchetype.BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C, 2, 0, 5, 2, 0, 2, 4, 5, 0, 4, 5, "Contract value collapse and call-off failure are hard 4C gates."),
    Round286ShadowWeightRow(E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C, 2, 0, 0, 2, 5, 1, 4, 3, -5, 5, 5, "Rare-earth export controls are supply-chain RedTeam until license and shipment continuity prove otherwise."),
    Round286ShadowWeightRow(E2RArchetype.CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2, 4, 2, 5, 4, 3, 2, 4, 5, -4, 4, 4, "Cathode rebalancing requires binding terms, ramp, customer call-off and margin."),
)


ROUND286_DEEP_SUB_ARCHETYPES: tuple[Round286DeepSubArchetype, ...] = (
    Round286DeepSubArchetype("petrochemical spread collapse", E2RArchetype.PETROCHEMICAL_SPREAD_COLLAPSE_4C, ("Lotte Chemical", "LG Chem", "NE Asia oversupply", "deep operating loss", "NCC spread collapse")),
    Round286DeepSubArchetype("Korea petrochemical restructuring", E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN, ("Daesan NCC shutdown", "2T KRW policy support", "1.2T KRW capital increase", "utility support")),
    Round286DeepSubArchetype("steel anti-dumping event premium", E2RArchetype.STEEL_ANTI_DUMPING_EVENT_PREMIUM, ("Hyundai Steel", "POSCO", "Chinese steel dumping", "anti-dumping tariff", "weak construction demand")),
    Round286DeepSubArchetype("strategic metal control premium", E2RArchetype.STRATEGIC_METAL_CONTROL_PREMIUM_4B, ("Korea Zinc", "Young Poong", "MBK", "tender offer", "buyback defence", "governance risk")),
    Round286DeepSubArchetype("lithium resource integration", E2RArchetype.LITHIUM_RESOURCE_INTEGRATION_STAGE2, ("POSCO", "Mineral Resources", "Wodgina", "Mt Marion", "lithium hydroxide JV")),
    Round286DeepSubArchetype("lithium squeeze event premium", E2RArchetype.LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM, ("POSCO Future M", "L&F", "Samsung SDI", "LGES", "CATL Yichun suspension")),
    Round286DeepSubArchetype("battery material contract hard 4C", E2RArchetype.BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C, ("L&F", "Tesla", "4680 cathode", "contract value collapse", "customer call-off failure")),
    Round286DeepSubArchetype("rare-earth export control", E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C, ("China export controls", "processed rare earths", "magnets", "exports down 50%", "license continuity")),
    Round286DeepSubArchetype("cathode supply-chain rebalancing", E2RArchetype.CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2, ("LG Chem", "Toyota Tsusho", "Huayou", "Exxon", "non-binding lithium")),
)


ROUND286_CASE_CANDIDATES: tuple[Round286CaseCandidate, ...] = (
    Round286CaseCandidate(
        case_id="r4_loop14_lotte_lgchem_petrochemical_spread_collapse",
        symbol="011170/051910",
        company_name="Lotte Chemical / LG Chem petrochemical spread collapse",
        primary_archetype=E2RArchetype.PETROCHEMICAL_SPREAD_COLLAPSE_4C,
        secondary_archetypes=(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, E2RArchetype.COMMODITY_SPREAD_CYCLE_NOT_STRUCTURAL),
        case_type="failed_rerating",
        round_case_type="failed_rerating + 4C-watch",
        stage1_date=date(2024, 12, 31),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 2, 7),
        stage3_decision="petrochemical_rebound_is_not_green_while_spread_loss_and_oversupply_continue",
        stage4b_status="4C-watch/petrochemical-spread-collapse-deep-loss",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=True,
        evidence_fields=("NE_Asia_oversupply", "NCC_spread_collapse", "Lotte_2024_operating_loss_895bn_krw", "LG_Chem_OP_decline"),
        red_flag_fields=("petrochemical_spread_collapse_with_deep_operating_loss", "China_demand_weak", "Middle_East_supply_pressure", "inventory_loss_risk"),
        price_data_source="reported operating-loss and spread-collapse anchors",
        reported_price_anchor="Lotte Chemical 2024 OP loss 895B KRW; LG Chem OP down about 63.75%",
        reported_return_anchor="Spread collapse and deep losses should block commodity-rebound Green.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"lotte_2024_op_loss_krw_bn": 895, "lotte_op_loss_widening_krw_bn": 157, "lg_chem_op_krw_bn": 916.8, "lg_chem_op_decline_pct": -63.75, "petro_q4_loss_krw_bn": 99},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="petrochemical_spread_collapse_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="spread_and_cash_margin_broke_before_green",
        price_validation_status="reported_loss_anchor_not_full_ohlc",
        notes="Petrochemical oversupply is a RedTeam gate until spread, utilization and cash margin recover.",
    ),
    Round286CaseCandidate(
        case_id="r4_loop14_lotte_hdhyundai_petrochemical_restructuring",
        symbol="011170/HD_Hyundai_Oilbank_readthrough",
        company_name="Lotte Chemical / HD Hyundai Oilbank Daesan restructuring",
        primary_archetype=E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_restructuring",
        stage1_date=date(2025, 8, 1),
        stage2_date=date(2026, 2, 24),
        stage3_date=None,
        stage4b_date=date(2025, 11, 26),
        stage4c_date=None,
        stage3_decision="policy_restructuring_is_stage2_until_shutdown_execution_spread_and_cash_margin_confirm",
        stage4b_status="4B-watch/restructuring-policy-support-before-spread",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Daesan_NCC_shutdown_plan", "2T_KRW_policy_support", "1_2T_KRW_capital_increase", "utility_support_115bn_krw"),
        red_flag_fields=("capacity_restructuring_policy_only", "spread_recovery_unconfirmed", "shutdown_execution_unconfirmed", "cash_margin_unconfirmed"),
        price_data_source="reported restructuring and policy-support anchors",
        reported_price_anchor="2T KRW policy support; 1.2T KRW capital increase; 3-year shutdown plan",
        reported_return_anchor="Restructuring policy is Stage 2; Green waits for executed cut and spread recovery.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"capacity_cut_low_mn_tpy": 2.7, "capacity_cut_high_mn_tpy": 3.7, "capacity_cut_equivalent_pct": 25, "lotte_daesan_shutdown_mn_tpy": 1.1, "hd_hyundai_oilbank_shutdown_mn_tpy": 0.85, "policy_support_krw_trn": 2.0, "capital_increase_krw_trn": 1.2, "lotte_contribution_krw_bn": 600, "hd_hyundai_contribution_krw_bn": 600, "shutdown_years": 3, "utility_support_krw_bn": 115, "r_and_d_support_krw_bn": 26},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_restructuring",
        rerating_result="policy_event_rerating",
        round_rerating_label="petrochemical_restructuring_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_support_not_spread_cash_margin_green",
        price_validation_status="reported_policy_anchor_not_full_ohlc",
        notes="Daesan restructuring is useful Stage 2 evidence, not Green before actual shutdown discipline and spread recovery.",
    ),
    Round286CaseCandidate(
        case_id="r4_loop14_hyundai_posco_steel_spread_antidumping",
        symbol="004020/005490",
        company_name="Hyundai Steel / POSCO steel anti-dumping relief",
        primary_archetype=E2RArchetype.STEEL_ANTI_DUMPING_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF, E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK),
        case_type="event_premium",
        round_case_type="event_premium_policy_relief",
        stage1_date=date(2024, 6, 21),
        stage2_date=date(2025, 2, 20),
        stage3_date=None,
        stage4b_date=date(2025, 2, 20),
        stage4c_date=date(2024, 6, 21),
        stage3_decision="anti_dumping_is_event_premium_until_physical_demand_spread_and_export_tariff_risk_clear",
        stage4b_status="4B-watch/anti-dumping-relief-before-demand; 4C-watch/export-tariff-risk",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=True,
        evidence_fields=("anti_dumping_tariff", "China_steel_import_pressure", "Hyundai_Steel_event_return_5_8pct", "rebar_weak_demand"),
        red_flag_fields=("tariff_relief_only", "weak_demand_persists", "net_profit_estimates_cut", "export_tariff_shock"),
        price_data_source="reported anti-dumping event-return and weak-demand anchors",
        reported_price_anchor="Hyundai Steel around +5.8%; event price 29,000 KRW; target 30,000 KRW",
        reported_return_anchor="Tariff relief can move price, but demand and steel spread decide FCF.",
        event_mfe_pct=5.8,
        event_mae_pct=-1.2,
        stage1_price_anchor=None,
        stage2_price_anchor=29000.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_price_krw": 29000, "target_price_krw": 30000, "hyundai_steel_antidumping_mfe_pct": 5.8, "same_context_mae_pct": -1.2, "anti_dumping_tariff_visible": True, "weak_demand_estimate_revision": True},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="event_premium_policy_relief",
        rerating_result="policy_event_rerating",
        round_rerating_label="steel_anti_dumping_event_premium",
        stage_failure_type="false_yellow",
        round_stage_failure_label="tariff_relief_not_demand_or_spread_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Steel anti-dumping relief is useful, but Green needs physical demand, ASP/spread and export risk control.",
    ),
    Round286CaseCandidate(
        case_id="r4_loop14_korea_zinc_strategic_metal_control_premium",
        symbol="010130/000670",
        company_name="Korea Zinc / Young Poong strategic metal control premium",
        primary_archetype=E2RArchetype.STRATEGIC_METAL_CONTROL_PREMIUM_4B,
        secondary_archetypes=(E2RArchetype.CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION, E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE),
        case_type="4b_watch",
        round_case_type="event_premium_4B_watch",
        stage1_date=date(2024, 9, 13),
        stage2_date=date(2024, 9, 13),
        stage3_date=None,
        stage4b_date=date(2024, 9, 13),
        stage4c_date=None,
        stage3_decision="control_premium_is_not_operating_green_without_smelter_margin_governance_and_dilution_control",
        stage4b_status="4B-watch/control-premium-before-operating-evidence",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("tender_offer_2T_KRW", "offer_price_660000_krw", "prior_close_556000_krw", "Korea_Zinc_event_plus_19_8pct"),
        red_flag_fields=("control_premium_only", "buyback_defence_funding_risk", "governance_dispute", "safety_accounting_quality_watch"),
        price_data_source="reported tender-offer and control-premium anchors",
        reported_price_anchor="Offer price 660,000 KRW vs prior close 556,000 KRW; Korea Zinc +19.8%; Young Poong +30%",
        reported_return_anchor="Control premium is 4B-watch until operating cashflow and governance quality confirm.",
        event_mfe_pct=19.8,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=660000.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=660000.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"tender_offer_krw_trn": 2.0, "tender_offer_usd_bn": 1.5, "offer_price_krw": 660000, "prior_close_krw": 556000, "korea_zinc_event_mfe_pct": 19.8, "young_poong_event_mfe_pct": 30, "buyback_defence_krw_trn": 2.663, "buyback_price_krw": 830000},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="strategic_metal_control_premium_4B_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="control_premium_not_FCF_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Korea Zinc is a control-premium price case; operating Green needs smelter margin, governance and dilution checks.",
    ),
    Round286CaseCandidate(
        case_id="r4_loop14_posco_minres_lithium_resource_integration",
        symbol="005490",
        company_name="POSCO / Mineral Resources lithium resource integration",
        primary_archetype=E2RArchetype.LITHIUM_RESOURCE_INTEGRATION_STAGE2,
        secondary_archetypes=(E2RArchetype.LITHIUM_RESOURCE_SECURITY, E2RArchetype.LITHIUM_BATTERY_RAW_MATERIAL),
        case_type="success_candidate",
        round_case_type="success_candidate_resource_integration",
        stage1_date=date(2025, 11, 11),
        stage2_date=date(2025, 11, 11),
        stage3_date=None,
        stage4b_date=date(2025, 11, 11),
        stage4c_date=None,
        stage3_decision="mine_stake_is_stage2_until_offtake_processing_utilization_lithium_price_and_customer_calloff_confirm",
        stage4b_status="4B-watch/mine-stake-before-processing-utilization",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Wodgina_Mt_Marion_assets", "30pct_interest_sale", "POSCO_effective_15pct", "lithium_hydroxide_JV_path"),
        red_flag_fields=("mine_stake_without_processing_margin", "low_lithium_price_context", "customer_calloff_unconfirmed", "hydroxide_utilization_unconfirmed"),
        price_data_source="reported deal-value and MinRes event anchors",
        reported_price_anchor="$765M deal; 30% interest; POSCO effective 15%; MinRes event +10.8%",
        reported_return_anchor="Resource security is Stage 2; Green waits for offtake, processing margin and customer call-off.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_usd_mn": 765, "mine_interest_sold_pct": 30, "posco_effective_interest_pct": 15, "minres_event_mfe_pct": 10.8, "assets": ["Wodgina", "Mt Marion"], "hydroxide_jv_path": True, "processing_utilization_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_price_data_unavailable",
        rerating_result="unknown",
        round_rerating_label="lithium_resource_integration_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="mine_stake_not_processing_margin_green",
        price_validation_status="counterparty_event_anchor_not_POSCO_full_ohlc",
        notes="POSCO lithium resource integration needs offtake and processing utilization before it becomes structural evidence.",
    ),
    Round286CaseCandidate(
        case_id="r4_loop14_posco_future_m_lnf_lithium_squeeze_rally",
        symbol="003670/066970/006400/373220",
        company_name="POSCO Future M / L&F / battery basket lithium squeeze",
        primary_archetype=E2RArchetype.LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.GRAPHITE_LITHIUM_POLICY_PRICE_EVENT, E2RArchetype.COMMODITY_PRICE_EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_lithium_squeeze",
        stage1_date=date(2025, 8, 11),
        stage2_date=date(2025, 8, 11),
        stage3_date=None,
        stage4b_date=date(2025, 8, 11),
        stage4c_date=None,
        stage3_decision="lithium_squeeze_rally_is_event_premium_until_ASP_inventory_and_margin_confirm",
        stage4b_status="4B-watch/lithium-license-headline-before-margin",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("CATL_Yichun_suspension", "lithium_price_squeeze", "LNF_plus_10pct", "POSCO_Future_M_plus_8_3pct"),
        red_flag_fields=("CATL_license_suspension_sentiment", "commodity_rebound_headline_only", "inventory_valuation_risk_ignored", "customer_volume_unconfirmed"),
        price_data_source="reported lithium squeeze event-return anchors",
        reported_price_anchor="Ganfeng +21%, Tianqi +18%, POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%",
        reported_return_anchor="Lithium squeeze is event premium unless it becomes ASP, inventory and margin.",
        event_mfe_pct=10.0,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ganfeng_event_mfe_pct": 21, "tianqi_event_mfe_pct": 18, "posco_future_m_event_mfe_pct": 8.3, "lnf_event_mfe_pct": 10, "samsung_sdi_event_mfe_pct": 3.2, "lges_event_mfe_pct": 2.8, "kospi_same_context_pct": -0.1, "lithium_price_prior_decline_pct": -90},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_lithium_squeeze",
        rerating_result="event_premium",
        round_rerating_label="lithium_price_squeeze_event_premium",
        stage_failure_type="false_yellow",
        round_stage_failure_label="lithium_headline_not_ASP_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Lithium squeeze rallies need customer volume, ASP, pass-through and inventory checks before Green.",
    ),
    Round286CaseCandidate(
        case_id="r4_loop14_lnf_tesla_4680_cathode_contract_collapse",
        symbol="066970",
        company_name="L&F Tesla 4680 cathode contract collapse",
        primary_archetype=E2RArchetype.BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C,
        secondary_archetypes=(E2RArchetype.EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE, E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK),
        case_type="4c_thesis_break",
        round_case_type="hard 4C",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2023, 1, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 29),
        stage3_decision="signed_cathode_contract_is_not_green_if_customer_calloff_and_contract_value_collapse",
        stage4b_status="hard-4C/contract-value-collapse-customer-calloff-failure",
        hard_4c_confirmed=True,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Tesla_4680_cathode_contract", "initial_contract_value_visible", "supply_period_visible", "revised_contract_value_collapse"),
        red_flag_fields=("signed_contract_value_collapse", "customer_calloff_failure", "EV_demand_slowdown", "4680_ramp_difficulty"),
        price_data_source="reported contract-value-collapse anchor",
        reported_price_anchor="Initial contract value 2.9B USD equivalent; revised to 7,386 KRW scale anchor",
        reported_return_anchor="Customer-name contract becomes hard 4C when value and call-off collapse.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"initial_contract_value_usd_bn": 2.9, "revised_contract_value_anchor": 7386, "contract_value_collapse_pct": -99.9997, "customer": "Tesla", "program": "4680_cathode"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="battery_material_contract_collapse_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="signed_contract_without_calloff_became_4C",
        price_validation_status="reported_contract_anchor_not_full_ohlc",
        notes="L&F is the R4 hard 4C reference: signed contract value is not durable evidence without call-off.",
    ),
    Round286CaseCandidate(
        case_id="r4_loop14_rare_earth_export_control_supply_chain",
        symbol="005930/000660/042660/strategic_materials_basket",
        company_name="Korea strategic-materials basket rare-earth export controls",
        primary_archetype=E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C,
        secondary_archetypes=(E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY),
        case_type="4b_watch",
        round_case_type="4C-watch",
        stage1_date=date(2025, 4, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 10, 22),
        stage3_decision="rare_earth_export_control_is_redteam_overlay_until_export_licenses_and_shipments_continue",
        stage4b_status="4C-watch/export-control-license-and-shipment-continuity",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=True,
        evidence_fields=("China_export_controls", "processed_rare_earth_share_over_90pct", "magnet_supply_chain", "exports_down_about_50pct"),
        red_flag_fields=("rare_earth_export_license_denial_or_shipment_failure", "rare_earth_truce_without_actual_exports", "customer_supply_chain_break", "defense_end_use_restriction"),
        price_data_source="reported export-control and shipment-decline anchors",
        reported_price_anchor="China share >90% in processed rare earths/magnets; exports down about 50%",
        reported_return_anchor="Rare-earth headline is not beneficiary evidence unless licenses and shipments continue.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"processed_rare_earth_share_pct": 90, "reported_export_decline_pct": -50, "affected_elements": ["samarium", "gadolinium", "terbium", "dysprosium", "lutetium", "scandium", "yttrium"], "license_continuity_confirmed": False, "actual_exports_recovered": False},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="rare_earth_export_control_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="export_control_is_supply_chain_risk_not_green",
        price_validation_status="export_control_anchor_not_stock_ohlc",
        notes="Rare-earth controls should feed RedTeam and supply-chain 4C-watch, not automatic beneficiary scoring.",
    ),
    Round286CaseCandidate(
        case_id="r4_loop14_lg_chem_cathode_supply_chain_rebalancing",
        symbol="051910",
        company_name="LG Chem cathode supply-chain rebalancing",
        primary_archetype=E2RArchetype.CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2,
        secondary_archetypes=(E2RArchetype.CATHODE_SUPPLY_CHAIN_DERISKING, E2RArchetype.LITHIUM_RESOURCE_SECURITY),
        case_type="success_candidate",
        round_case_type="success_candidate_nonbinding_watch",
        stage1_date=date(2024, 11, 20),
        stage2_date=date(2025, 9, 8),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="cathode_rebalancing_is_stage2_until_binding_lithium_terms_Tennessee_ramp_calloff_and_margin_confirm",
        stage4b_status="watch/nonbinding-supply-before-ramp-and-margin",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Toyota_Tsusho_stake_25pct", "Huayou_stake_reduced_from_49_to_24pct", "Exxon_nonbinding_lithium_100000_tonnes", "China_exposure_reduction"),
        red_flag_fields=("nonbinding_supply_agreement", "cathode_ramp_unconfirmed", "customer_calloff_unconfirmed", "final_financial_terms_unconfirmed"),
        price_data_source="reported stake-shift and non-binding lithium anchors",
        reported_price_anchor="Toyota Tsusho 25%; Huayou 49% to 24%; Exxon non-binding 100,000 tonnes lithium",
        reported_return_anchor="Supply-chain rebalancing is Stage 2 until binding terms, ramp and margin confirm.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"toyota_tsusho_stake_pct": 25, "huayou_initial_stake_pct": 49, "huayou_revised_stake_pct": 24, "huayou_stake_decline_pp": -25, "exxon_lithium_tonnes": 100000, "binding_contract": False, "final_financial_terms_visible": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_nonbinding_watch",
        rerating_result="unknown",
        round_rerating_label="cathode_supply_chain_rebalancing_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="nonbinding_supply_and_rebalancing_not_margin_green",
        price_validation_status="reported_supply_chain_anchor_not_full_ohlc",
        notes="LG Chem cathode rebalancing needs binding lithium terms, Tennessee ramp, customer call-off and margin.",
    ),
)


def round286_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND286_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND286_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round286 R4 Loop-14 materials/spreads/strategic-resources price-validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=candidate.evidence_fields if candidate.stage3_date else (),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("premium", "headline", "control", "squeeze", "policy", "watch", "stake"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("collapse", "failure", "loss", "4c", "export", "tariff", "shutdown", "calloff", "weak"))),
            must_have_fields=ROUND286_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"structural_success", "success_candidate"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND286_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "round286_hard_4c_confirmed_true",
                "do_not_use_round286_cases_as_candidate_generation_input",
                "do_not_treat_spread_policy_control_premium_lithium_or_rare_earth_headlines_as_green",
                *ROUND286_GREEN_REQUIRED_FIELDS,
                *ROUND286_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.event_mfe_pct is not None
                    or candidate.event_mae_pct is not None
                    or candidate.stage1_price_anchor is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.84 if "unavailable" not in candidate.price_validation_status else 0.72,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round286_case_rows() -> tuple[dict[str, str], ...]:
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
            "hard_4c_watch_confirmed": str(candidate.hard_4c_watch_confirmed).lower(),
            "price_data_source": candidate.price_data_source,
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
            "event_mfe_pct": _float_text(candidate.event_mfe_pct),
            "event_mae_pct": _float_text(candidate.event_mae_pct),
            "stage1_price_anchor": _float_text(candidate.stage1_price_anchor),
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
        for candidate in ROUND286_CASE_CANDIDATES
    )


def round286_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND286_SCORE_ADJUSTMENTS)


def round286_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND286_SHADOW_WEIGHT_ROWS)


def round286_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND286_DEEP_SUB_ARCHETYPES)


def round286_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round286_price_validation": "true"} for field in ROUND286_PRICE_VALIDATION_FIELDS)


def round286_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round286_label": label, "canonical_archetype": canonical} for label, canonical in ROUND286_REQUIRED_TARGET_ALIASES.items())


def round286_summary() -> dict[str, int | bool | str]:
    cases = ROUND286_CASE_CANDIDATES
    return {
        "source_round": ROUND286_SOURCE_ROUND_PATH,
        "round_id": ROUND286_ANALYST_ROUND_ID,
        "large_sector": ROUND286_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "event_premium_or_result_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "hard_4c_watch_case_count": sum(1 for case in cases if case.hard_4c_watch_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "unknown_alignment_count": sum(1 for case in cases if case.score_price_alignment == "unknown"),
        "aligned_count": sum(1 for case in cases if case.score_price_alignment == "aligned"),
        "target_archetype_count": len(ROUND286_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND286_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND286_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "hard_4c_watch_confirmed": any(case.hard_4c_watch_confirmed for case in cases),
    }


def round286_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND286_SOURCE_ROUND_PATH,
        "round_id": ROUND286_ANALYST_ROUND_ID,
        "large_sector": ROUND286_LARGE_SECTOR,
        "summary": round286_summary(),
        "target_aliases": dict(ROUND286_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND286_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND286_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND286_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND286_HARD_4C_GATES),
        "score_adjustments": list(round286_score_adjustment_rows()),
        "shadow_weights": list(round286_shadow_weight_rows()),
        "deep_sub_archetypes": list(round286_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND286_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round286_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_spread_policy_control_premium_lithium_or_rare_earth_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round286_summary_markdown() -> str:
    summary = round286_summary()
    lines = [
        "# Round 286 R4 Loop 14 Materials Spreads Strategic Resources Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- Stage 3 dated candidates: {summary['stage3_case_count']}",
        f"- stage4b_watch: {summary['stage4b_watch_count']}",
        f"- stage4c_watch: {summary['stage4c_watch_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- hard_4c_watch: {summary['hard_4c_watch_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND286_CASE_CANDIDATES:
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
            "- Petrochemical spread collapse and L&F contract collapse are thesis-break references, not Green inputs.",
            "- Steel anti-dumping, lithium squeeze and Korea Zinc control premium are event-premium or 4B-watch unless FCF evidence appears.",
            "- POSCO lithium integration, Daesan restructuring and LG Chem cathode rebalancing are Stage 2 candidates until utilization, binding terms, call-off and margin close.",
            "- Rare-earth export controls are RedTeam supply-chain overlays; actual license and shipment continuity must be verified.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round286_green_gate_review_markdown() -> str:
    lines = [
        "# Round 286 R4 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R4 Stage 3-Green is not `spread`, `tariff`, `control premium`, `lithium`, or `rare earth` as a label. It requires spread/margin realization, executed restructuring, customer call-off, offtake utilization, export-license continuity and FCF-quality evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND286_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND286_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND286_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `anti-dumping tariff` can lift steel shares, but without actual steel spread and demand it remains event premium.",
            "- `mine stake acquisition` is Stage 2 until offtake, processing utilization and customer call-off confirm.",
            "- `rare-earth export control` is a supply-chain RedTeam input; it is not automatic beneficiary evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round286_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 286 R4 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND286_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND286_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | hard 4C watch | interpretation |", "|---|---|---|---|---|---|"])
    for case in ROUND286_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.hard_4c_watch_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round286_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 286 R4 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, full MFE/MAE, spread recovery, call-off, offtake, export-license continuity, binding supply terms, or FCF evidence where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND286_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND286_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round286_r4_loop14_reports(
    output_directory: str | Path = ROUND286_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND286_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND286_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round286_case_records(), cases_path),
        "audit": _write_json(round286_audit_payload(), audit_path),
        "summary": output / "round286_r4_loop14_price_validation_summary.md",
        "case_matrix": output / "round286_r4_loop14_case_matrix.csv",
        "target_aliases": output / "round286_r4_loop14_target_aliases.csv",
        "score_adjustments": output / "round286_r4_loop14_score_adjustments.csv",
        "shadow_weights": output / "round286_r4_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round286_r4_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round286_r4_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round286_r4_loop14_green_gate_review.md",
        "price_validation_plan": output / "round286_r4_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round286_r4_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round286_summary_markdown(), encoding="utf-8")
    _write_csv(round286_case_rows(), paths["case_matrix"])
    _write_csv(round286_target_alias_rows(), paths["target_aliases"])
    _write_csv(round286_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round286_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round286_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round286_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round286_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round286_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round286_stage4b_4c_review_markdown(), encoding="utf-8")
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


__all__ = [
    "ROUND286_CASE_CANDIDATES",
    "ROUND286_GREEN_FORBIDDEN_PATTERNS",
    "ROUND286_GREEN_REQUIRED_FIELDS",
    "ROUND286_HARD_4C_GATES",
    "ROUND286_LARGE_SECTOR",
    "ROUND286_PRICE_VALIDATION_FIELDS",
    "ROUND286_REQUIRED_TARGET_ALIASES",
    "ROUND286_SHADOW_WEIGHT_ROWS",
    "ROUND286_STAGE4B_WATCH_TRIGGERS",
    "render_round286_green_gate_review_markdown",
    "render_round286_stage4b_4c_review_markdown",
    "round286_audit_payload",
    "round286_case_records",
    "round286_case_rows",
    "round286_deep_sub_archetype_rows",
    "round286_shadow_weight_rows",
    "round286_summary",
    "write_round286_r4_loop14_reports",
]
