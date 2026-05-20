"""Round-285 R3 Loop-14 battery/EV/green-energy price-validation pack.

This module converts ``docs/round/round_285.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: a 27GWh battery JV is useful Stage 2 evidence, but it is not
Stage 3-Green until actual customer call-off, factory utilization, subsidy
durability, gross margin and FCF are visible.
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


ROUND285_SOURCE_ROUND_PATH = "docs/round/round_285.md"
ROUND285_ANALYST_ROUND_ID = "round_213"
ROUND285_LARGE_SECTOR = "SECONDARY_BATTERY_EV_GREEN_ENERGY"
ROUND285_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round285_r3_loop14_secondary_battery_ev_green_energy_price_validation"
ROUND285_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop14_round285.jsonl"
ROUND285_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round285_r3_loop14_secondary_battery_ev_green_energy_price_validation_audit.json"

ROUND285_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C": E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C.value,
    "BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH": E2RArchetype.BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH.value,
    "SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2": E2RArchetype.SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2.value,
    "BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C": E2RArchetype.BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C.value,
    "SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C": E2RArchetype.SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C.value,
    "HYDROGEN_FUEL_CELL_CAPEX_STAGE2": E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX_STAGE2.value,
    "SILICON_ANODE_SCALEUP_STAGE2": E2RArchetype.SILICON_ANODE_SCALEUP_STAGE2.value,
    "BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE": E2RArchetype.BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE.value,
}

ROUND285_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "customer_calloff_visibility_confirmed",
    "contract_cancellation_risk_cleared",
    "plant_utilization_confirmed",
    "EV_model_mix_battery_content_confirmed",
    "subsidy_tariff_policy_stability_confirmed",
    "ESS_PO_value_and_margin_confirmed",
    "supply_chain_customs_clearance_confirmed",
    "localization_execution_confirmed",
    "raw_material_cost_pass_through_confirmed",
    "listed_value_bridge_for_unlisted_tech_confirmed",
    "price_path_after_evidence",
)

ROUND285_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "EV_growth_headline_only",
    "signed_contract_without_calloff",
    "capacity_capex_without_utilization",
    "IRA_or_policy_loan_only",
    "ESS_pivot_without_contract_value",
    "hybrid_shift_ignored",
    "unlisted_material_tech_readthrough",
    "solar_factory_without_customs_clearance",
    "hydrogen_capex_without_demand",
)

ROUND285_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "EV_battery_plant_or_JV_headline_before_utilization",
    "ESS_pivot_headline_before_disclosed_margin",
    "hydrogen_capex_before_customer_demand",
    "silicon_anode_funding_without_listed_EPS_bridge",
    "solar_policy_loan_before_customs_and_utilization",
    "automaker_customer_name_without_actual_calloff",
)

ROUND285_HARD_4C_GATES: tuple[str, ...] = (
    "major_customer_contract_cancellation",
    "automaker_EV_model_cancellation",
    "BEV_to_hybrid_shift_lowering_battery_content",
    "plant_utilization_delay",
    "subsidy_or_tax_credit_expiry_damaging_demand",
    "customs_detention_blocking_component_shipments",
    "JV_dissolution_or_capacity_transfer",
    "repeated_operating_losses_without_utilization_recovery",
    "raw_material_price_collapse_inventory_loss",
)

ROUND285_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "contract_value_anchor",
    "operating_loss_anchor",
    "factory_investment_anchor",
    "policy_subsidy_anchor",
    "customs_supply_chain_anchor",
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
class Round285ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round285ShadowWeightRow:
    archetype: E2RArchetype
    customer_calloff_visibility: int
    contract_cancellation_risk: int
    plant_utilization: int
    ev_model_mix_battery_content: int
    subsidy_tariff_policy_stability: int
    ess_po_value_margin: int
    supply_chain_customs_clearance: int
    localization_execution: int
    raw_material_cost_pass_through: int
    listed_value_bridge: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "customer_calloff_visibility": _signed(self.customer_calloff_visibility),
            "contract_cancellation_risk": _signed(self.contract_cancellation_risk),
            "plant_utilization": _signed(self.plant_utilization),
            "ev_model_mix_battery_content": _signed(self.ev_model_mix_battery_content),
            "subsidy_tariff_policy_stability": _signed(self.subsidy_tariff_policy_stability),
            "ess_po_value_margin": _signed(self.ess_po_value_margin),
            "supply_chain_customs_clearance": _signed(self.supply_chain_customs_clearance),
            "localization_execution": _signed(self.localization_execution),
            "raw_material_cost_pass_through": _signed(self.raw_material_cost_pass_through),
            "listed_value_bridge": _signed(self.listed_value_bridge),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round285DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round285CaseCandidate:
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


ROUND285_SCORE_ADJUSTMENTS: tuple[Round285ScoreAdjustment, ...] = (
    Round285ScoreAdjustment("customer_calloff_visibility", 5, "raise", "배터리 계약은 실제 call-off와 shipment가 보여야 강하다."),
    Round285ScoreAdjustment("contract_cancellation_risk", 5, "raise", "대형 고객 계약 취소는 expected revenue와 utilization을 직접 깬다."),
    Round285ScoreAdjustment("plant_utilization", 5, "raise", "공장·JV·capex는 utilization이 있어야 EPS/FCF로 연결된다."),
    Round285ScoreAdjustment("EV_model_mix_battery_content", 5, "raise", "BEV에서 hybrid/EREV로 바뀌면 차량당 battery content가 줄 수 있다."),
    Round285ScoreAdjustment("subsidy_tariff_policy_stability", 5, "raise", "IRA/AMPC/관세/보조금은 지속성과 실질 이익 품질을 확인해야 한다."),
    Round285ScoreAdjustment("ESS_PO_value_and_margin", 5, "raise", "ESS pivot은 PO value, installation, margin이 있어야 Stage 3로 간다."),
    Round285ScoreAdjustment("supply_chain_customs_clearance", 5, "raise", "태양광·배터리 현지화는 customs clearance가 막히면 utilization이 무너진다."),
    Round285ScoreAdjustment("localization_execution", 4, "raise", "현지화는 공장 착공보다 부품 흐름, 인력, 가동률이 중요하다."),
    Round285ScoreAdjustment("raw_material_cost_pass_through", 4, "raise", "소재주는 원재료 가격과 판가연동, 재고손실을 같이 봐야 한다."),
    Round285ScoreAdjustment("listed_value_bridge_for_unlisted_tech", 4, "raise", "비상장 소재 기술은 상장사 EPS/value bridge가 있어야 한다."),
    Round285ScoreAdjustment("EV_growth_headline_only", -5, "lower", "EV 장기성장 단어만으로 Stage 3를 만들지 않는다."),
    Round285ScoreAdjustment("signed_contract_without_calloff", -5, "lower", "계약 체결만 있고 실제 call-off가 없으면 제한한다."),
    Round285ScoreAdjustment("capacity_capex_without_utilization", -5, "lower", "capacity capex는 utilization 전에는 현금소모일 수 있다."),
    Round285ScoreAdjustment("IRA_or_policy_loan_only", -5, "lower", "정책자금이나 IRA headline은 이익 품질이 아니다."),
    Round285ScoreAdjustment("ESS_pivot_without_contract_value", -5, "lower", "ESS pivot은 계약가와 margin이 없으면 Stage 2에 머문다."),
    Round285ScoreAdjustment("hybrid_shift_ignored", -5, "lower", "hybrid 전환은 battery content 감소 리스크다."),
    Round285ScoreAdjustment("unlisted_material_tech_readthrough", -4, "lower", "비상장 기술 성과를 상장사 EPS로 바로 연결하지 않는다."),
    Round285ScoreAdjustment("solar_factory_without_customs_clearance", -5, "lower", "태양광 공장은 통관과 부품 흐름 없이는 Green이 아니다."),
    Round285ScoreAdjustment("hydrogen_capex_without_demand", -4, "lower", "수소 공장 착공은 고객 수요와 unit economics 전에는 Stage 2다."),
)


ROUND285_SHADOW_WEIGHT_ROWS: tuple[Round285ShadowWeightRow, ...] = (
    Round285ShadowWeightRow(E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C, 5, 5, 5, 5, 5, 2, 3, 4, 3, 2, 0, 4, 5, "LGES cancellation shows call-off and utilization are hard gates."),
    Round285ShadowWeightRow(E2RArchetype.BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH, 5, 4, 5, 5, 5, 2, 2, 5, 3, 2, -4, 4, 4, "Samsung SDI GM JV needs 2027 production, call-off, AMPC and margin."),
    Round285ShadowWeightRow(E2RArchetype.SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2, 5, 5, 5, 5, 5, 5, 2, 4, 3, 3, -4, 5, 4, "SK On restructuring/ESS pivot needs disclosed PO value and profitability."),
    Round285ShadowWeightRow(E2RArchetype.BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C, 5, 5, 4, 5, 5, 1, 3, 3, 5, 2, 0, 5, 4, "Ford hybrid pivot shows lower battery content can hit materials."),
    Round285ShadowWeightRow(E2RArchetype.SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C, 3, 3, 5, 0, 5, 0, 5, 5, 4, 2, -5, 5, 4, "Qcells needs customs clearance and factory utilization after policy loan."),
    Round285ShadowWeightRow(E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX_STAGE2, 3, 3, 5, 0, 5, 1, 2, 4, 3, 2, -5, 5, 3, "Hyundai hydrogen capex requires demand, utilization and unit economics."),
    Round285ShadowWeightRow(E2RArchetype.SILICON_ANODE_SCALEUP_STAGE2, 5, 4, 5, 4, 4, 2, 3, 4, 5, 5, -5, 5, 4, "Group14/SK needs customer contracts, yield, margin and listed value bridge."),
    Round285ShadowWeightRow(E2RArchetype.BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE, 5, 5, 5, 5, 5, 5, 3, 4, 4, 3, -5, 5, 4, "ESS pivot is not Green until PO value, shipment, installation and margin confirm."),
)


ROUND285_DEEP_SUB_ARCHETYPES: tuple[Round285DeepSubArchetype, ...] = (
    Round285DeepSubArchetype("EV battery contract hard break", E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C, ("LG Energy Solution", "Ford cancellation 9.6T KRW", "Freudenberg cancellation 3.9T KRW", "expected revenue loss 13.5T KRW")),
    Round285DeepSubArchetype("Battery JV demand watch", E2RArchetype.BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH, ("Samsung SDI", "GM JV $3.5B", "27GWh to 36GWh", "Q4 OP loss 257B KRW", "EV demand sluggish until H1 2026")),
    Round285DeepSubArchetype("SK On restructuring ESS pivot", E2RArchetype.SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2, ("SK Innovation", "SK E&S merger", "assets 100T KRW", "Ford JV dissolution", "Flatiron ESS 7.2GWh")),
    Round285DeepSubArchetype("Battery material supply-chain beta", E2RArchetype.BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C, ("EcoPro Materials", "SK IE Technology", "Ford hybrid pivot", "lower battery content", "material supplier beta")),
    Round285DeepSubArchetype("Solar U.S. manufacturing customs gate", E2RArchetype.SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C, ("Hanwha Qcells", "DOE loan $1.45B", "Georgia facility $2.5B", "customs detentions", "1,000 furloughs")),
    Round285DeepSubArchetype("Hydrogen fuel-cell capex", E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX_STAGE2, ("Hyundai Motor", "930B KRW Ulsan plant", "fuel cells", "electrolyzers", "utilization gate")),
    Round285DeepSubArchetype("Silicon anode scale-up", E2RArchetype.SILICON_ANODE_SCALEUP_STAGE2, ("SK Inc", "Group14", "$463M Series D", "Korea BAM factory", "listed value bridge")),
    Round285DeepSubArchetype("Battery ESS pivot cross-reference", E2RArchetype.BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE, ("LGES", "Samsung SDI", "SK On", "ESS line conversion", "PO value and margin gate")),
)


ROUND285_CASE_CANDIDATES: tuple[Round285CaseCandidate, ...] = (
    Round285CaseCandidate(
        case_id="r3_loop14_lges_ford_freudenberg_contract_cancellation_hard_4c",
        symbol="373220",
        company_name="LG Energy Solution Ford/Freudenberg cancellation",
        primary_archetype=E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C,
        secondary_archetypes=(E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK, E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C),
        case_type="4c_thesis_break",
        round_case_type="hard 4C",
        stage1_date=date(2024, 10, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 26),
        stage3_decision="contract_headline_is_not_green_when_customer_calloff_and_utilization_break",
        stage4b_status="hard-4C/customer-calloff-contract-cancellation",
        hard_4c_confirmed=True,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Ford_EV_battery_contract_2026_2027", "Ford_contract_cancelled_9_6trn_krw", "Freudenberg_contract_cancelled_3_9trn_krw", "combined_expected_revenue_loss_13_5trn_krw"),
        red_flag_fields=("major_customer_contract_cancellation", "expected_revenue_loss_over_half_2024_revenue", "European_plant_utilization_delay", "replacement_orders_hard_to_secure"),
        price_data_source="Reuters contract-cancellation and event-return anchors",
        reported_price_anchor="Ford cancellation intraday -7.6%; KOSPI -1.4%; combined expected revenue loss 13.5T KRW",
        reported_return_anchor="Major customer call-off broke expected revenue and utilization thesis.",
        event_mfe_pct=None,
        event_mae_pct=-7.6,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ford_contract_cancelled_krw_trn": 9.6, "ford_contract_cancelled_usd_bn": 6.5, "freudenberg_contract_cancelled_krw_trn": 3.9, "freudenberg_contract_cancelled_usd_bn": 2.7, "combined_cancelled_expected_revenue_krw_trn": 13.5, "lges_2024_revenue_krw_trn": 25.62, "cancelled_revenue_as_share_of_2024_revenue_pct": 52.7, "ford_cancellation_event_mae_pct": -7.6, "kospi_same_context_pct": -1.4, "relative_underperformance_pp": -6.2, "european_plant_utilization_delay_risk": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="EV_battery_contract_cancellation_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="customer_calloff_and_utilization_break",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="LGES is the hard 4C reference: contract value without customer call-off and utilization can disappear.",
    ),
    Round285CaseCandidate(
        case_id="r3_loop14_samsung_sdi_gm_jv_stage2_ev_demand_watch",
        symbol="006400",
        company_name="Samsung SDI GM JV EV-demand watch",
        primary_archetype=E2RArchetype.BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH,
        secondary_archetypes=(E2RArchetype.US_BATTERY_LOCALIZATION, E2RArchetype.EV_BATTERY_JV_RESTRUCTURING),
        case_type="success_candidate",
        round_case_type="success_candidate + 4C-watch",
        stage1_date=date(2024, 8, 27),
        stage2_date=date(2024, 8, 28),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 5),
        stage3_decision="GM_JV_capacity_is_stage2_but_calloff_utilization_AMPC_and_margin_are_green_gates",
        stage4b_status="4C-watch/EV-demand-slump-before-JV-utilization",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=True,
        evidence_fields=("GM_JV_investment_3_5bn_usd", "initial_capacity_27GWh", "potential_capacity_36GWh", "mass_production_target_2027", "event_return_plus_3_2pct"),
        red_flag_fields=("EV_demand_sluggish_until_H1_2026", "Q4_2024_operating_loss_257bn_krw", "JV_capacity_not_utilization", "AMPC_margin_unconfirmed"),
        price_data_source="Reuters GM JV and EV-demand anchors",
        reported_price_anchor="+3.2% vs KOSPI -0.3%; Q4 2024 OP loss 257B KRW",
        reported_return_anchor="JV capacity is Stage 2; actual call-off, utilization, AMPC and margin are required.",
        event_mfe_pct=3.2,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"gm_jv_investment_usd_bn": 3.5, "initial_capacity_gwh": 27, "potential_expansion_capacity_gwh": 36, "capacity_expansion_pct": 33.3, "mass_production_target": 2027, "stage2_event_mfe_pct": 3.2, "kospi_same_context_pct": -0.3, "relative_outperformance_pp": 3.5, "q4_2024_operating_loss_krw_bn": 257, "q4_2024_operating_loss_usd_mn": 176.54, "ev_demand_sluggish_until": "H1_2026"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="unknown",
        round_rerating_label="battery_JV_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="JV_capacity_not_utilization_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Samsung SDI/GM is Stage 2, but EV demand and operating losses block Green until utilization and margin appear.",
    ),
    Round285CaseCandidate(
        case_id="r3_loop14_sk_innovation_skon_restructuring_ess_pivot",
        symbol="096770",
        company_name="SK Innovation / SK On restructuring ESS pivot",
        primary_archetype=E2RArchetype.SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2,
        secondary_archetypes=(E2RArchetype.BATTERY_PARENT_CAPITAL_RECYCLING, E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_restructuring + 4C-watch",
        stage1_date=date(2024, 7, 1),
        stage2_date=date(2024, 8, 27),
        stage3_date=None,
        stage4b_date=date(2025, 9, 3),
        stage4c_date=date(2025, 12, 11),
        stage3_decision="restructuring_and_ESS_pivot_are_stage2_until_PO_value_margin_and_loss_reversal_confirm",
        stage4b_status="4B-watch/ESS-pivot-before-contract-value-and-margin; 4C-watch/Ford-JV-reset",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=True,
        evidence_fields=("SK_ES_merger_assets_100trn_krw", "SK_Innovation_event_plus_5pct", "SK_ES_2023_OP_1_3trn_krw", "Flatiron_ESS_7_2GWh_2026_2030", "Georgia_EV_line_conversion_for_ESS"),
        red_flag_fields=("SK_On_not_profitable_since_2021_spinoff", "Ford_JV_dissolution", "Q3_2025_OP_loss_124_8bn_krw", "ESS_contract_value_undisclosed"),
        price_data_source="Reuters merger, JV dissolution and ESS anchors",
        reported_price_anchor="+5% merger relief; later Ford JV split and Q3 2025 OP loss 124.8B KRW",
        reported_return_anchor="Restructuring and ESS pivot are Stage 2; profitability and disclosed ESS economics are required.",
        event_mfe_pct=5.0,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"sk_innovation_merger_event_mfe_pct": 5.0, "kospi_merger_context_pct": -0.5, "merged_company_assets_krw_trn": 100, "sk_es_2023_op_krw_trn": 1.3, "sk_es_2023_sales_krw_trn": 11.2, "sk_on_profit_history": "not_profitable_since_2021_spin_off", "blueoval_sk_original_investment_usd_bn": 11.4, "sk_on_q3_2025_op_loss_krw_bn": 124.8, "sk_on_q2_2025_op_loss_krw_bn": 66.4, "q3_loss_vs_q2_loss_increase_pct": 88.0, "flatiron_ess_supply_gwh": 7.2, "flatiron_ess_supply_period": "2026-2030", "ess_contract_value_disclosed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_restructuring_but_4C_watch",
        rerating_result="unknown",
        round_rerating_label="SK_On_ESS_pivot_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="EV_capacity_reset_not_ESS_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="SK On needs ESS value, delivery, margin and loss reversal before the pivot can become structural.",
    ),
    Round285CaseCandidate(
        case_id="r3_loop14_battery_material_supply_chain_ford_beta",
        symbol="450080/361610/096770/373220",
        company_name="EcoPro Materials / SK IE Technology / SK Innovation / LGES",
        primary_archetype=E2RArchetype.BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C,
        secondary_archetypes=(E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK, E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT),
        case_type="4b_watch",
        round_case_type="4C-watch",
        stage1_date=date(2025, 12, 16),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 16),
        stage3_decision="battery_material_beta_is_not_green_when_customer_model_mix_lowers_battery_content",
        stage4b_status="4C-watch/customer-model-mix-lower-battery-content",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=True,
        evidence_fields=("Ford_EV_related_charge_context", "battery_supply_chain_repricing", "hybrid_or_EREV_replacement_context"),
        red_flag_fields=("BEV_to_hybrid_shift_lowering_battery_content", "SK_Innovation_minus_3pct", "LGES_minus_6pct", "SK_IE_minus_5pct", "EcoPro_Materials_minus_5pct"),
        price_data_source="MarketWatch Ford EV pivot / Korea battery supply-chain anchor",
        reported_price_anchor="SKI -3%, LGES -6%, SK IE -5%, EcoPro Materials -5%",
        reported_return_anchor="Ford model mix can lower battery content and directly hit material suppliers.",
        event_mfe_pct=None,
        event_mae_pct=-5.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ford_charge_context_usd_bn": 20, "sk_innovation_event_mae_pct": -3, "lg_energy_solution_event_mae_pct": -6, "sk_ie_technology_event_mae_pct": -5, "ecopro_materials_event_mae_pct": -5, "battery_content_risk": "lower_battery_content_in_hybrid_or_EREV_replacement"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="battery_material_customer_mix_beta",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="EV_model_mix_lower_battery_content",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Battery-material suppliers need customer BEV volume and battery content, not only EV long-term growth.",
    ),
    Round285CaseCandidate(
        case_id="r3_loop14_hanwha_qcells_solar_policy_customs_gate",
        symbol="009830",
        company_name="Hanwha Solutions / Qcells solar policy customs gate",
        primary_archetype=E2RArchetype.SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C,
        secondary_archetypes=(E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION, E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH),
        case_type="success_candidate",
        round_case_type="success_candidate + 4C-watch",
        stage1_date=date(2024, 8, 8),
        stage2_date=date(2024, 8, 8),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 11, 8),
        stage3_decision="DOE_loan_and_US_factory_are_stage2_until_customs_component_flow_utilization_and_margin_confirm",
        stage4b_status="4C-watch/customs-component-flow-after-policy-loan",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=True,
        evidence_fields=("DOE_conditional_loan_guarantee_1_45bn_usd", "Cartersville_facility_2_5bn_usd", "panels_for_500000_households", "nearly_2000_jobs"),
        red_flag_fields=("customs_detention_under_forced_labor_import_law", "1000_workers_furloughed", "300_contract_workers_cut", "production_temporarily_curtailed"),
        price_data_source="Reuters DOE loan guarantee and Qcells furlough anchors",
        reported_price_anchor="$1.45B DOE loan guarantee; later 1,000 furloughs and 300 contractor cuts",
        reported_return_anchor="Policy loan is Stage 2; customs clearance and utilization are Green gates.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"doe_conditional_loan_guarantee_usd_bn": 1.45, "cartersville_facility_investment_usd_bn": 2.5, "households_powered_per_year_context": 500000, "jobs_when_operational": 2000, "furloughed_workers": 1000, "contract_workers_cut": 300, "customs_issue": "component_shipments_detained_under_forced_labor_import_law", "full_production_resumption_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="solar_US_manufacturing_policy_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_loan_not_factory_utilization_green",
        price_validation_status="direct_event_return_unavailable_after_deep_search",
        notes="Qcells needs customs clearance, component flow and factory utilization after policy support.",
    ),
    Round285CaseCandidate(
        case_id="r3_loop14_hyundai_hydrogen_fuel_cell_capex_stage2",
        symbol="005380",
        company_name="Hyundai Motor hydrogen fuel-cell capex",
        primary_archetype=E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX_STAGE2,
        secondary_archetypes=(E2RArchetype.HYDROGEN_FUELCELL_CAPEX_OPTIONALITY, E2RArchetype.HYDROGEN_FUEL_CELL_INFRA),
        case_type="success_candidate",
        round_case_type="success_candidate + capex gate",
        stage1_date=date(2025, 10, 30),
        stage2_date=date(2025, 10, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="hydrogen_capex_is_stage2_until_customer_demand_utilization_cost_per_kw_and_unit_margin_confirm",
        stage4b_status="watch/hydrogen-capex-before-demand",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Ulsan_hydrogen_fuel_cell_plant_930bn_krw", "site_area_43000_sqm", "completion_expected_2027", "fuel_cells_and_electrolyzers"),
        red_flag_fields=("customer_demand_unconfirmed", "unit_economics_unconfirmed", "utilization_unconfirmed", "subsidy_dependency_watch"),
        price_data_source="Reuters Hyundai hydrogen fuel-cell plant anchor",
        reported_price_anchor="930B KRW / $654M facility; completion expected 2027",
        reported_return_anchor="Hydrogen plant capex is Stage 2; demand, utilization and unit economics are required.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"facility_investment_krw_bn": 930, "facility_investment_usd_mn": 654, "site_area_sqm": 43000, "completion_expected": 2027, "products": ["fuel_cells", "electrolyzers"], "applications": ["passenger_cars", "commercial_trucks", "buses", "construction_equipment", "marine_vessels"], "former_site": "internal_combustion_transmission_plant", "customer_demand_confirmed": False, "unit_economics_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_capex_gate",
        rerating_result="unknown",
        round_rerating_label="hydrogen_fuel_cell_capex_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="hydrogen_capex_not_utilization_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Hydrogen capex is not customer demand; Green waits for utilization and unit economics.",
    ),
    Round285CaseCandidate(
        case_id="r3_loop14_sk_group14_silicon_anode_stage2",
        symbol="034730_readthrough",
        company_name="SK / Group14 silicon anode scale-up",
        primary_archetype=E2RArchetype.SILICON_ANODE_SCALEUP_STAGE2,
        secondary_archetypes=(E2RArchetype.SILICON_ANODE_OPTIONALITY, E2RArchetype.SPECULATIVE_BATTERY_TECH),
        case_type="success_candidate",
        round_case_type="success_candidate + insufficient evidence",
        stage1_date=date(2025, 8, 20),
        stage2_date=date(2025, 8, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="unlisted_material_scaleup_is_stage2_until_customer_contracts_yield_margin_and_listed_value_bridge_confirm",
        stage4b_status="watch/unlisted-silicon-anode-readthrough",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Group14_series_D_463mn_usd", "total_equity_raised_over_1bn_usd", "remaining_JV_stake_75pct_acquired", "Korea_BAM_factory_full_ownership", "SCC55_silicon_carbon_material"),
        red_flag_fields=("customer_contracts_unconfirmed", "yield_unconfirmed", "listed_SK_value_bridge_unconfirmed", "unlisted_material_tech_readthrough"),
        price_data_source="Reuters Group14 financing and JV-control anchor",
        reported_price_anchor="$463M Series D; total equity raised over $1B; Korea BAM factory full ownership",
        reported_return_anchor="Silicon-anode technology is Stage 2; listed SK Green needs contracts, yield, margin and value bridge.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"series_d_funding_usd_mn": 463, "total_equity_raised_usd_bn": 1.0, "remaining_jv_stake_acquired_pct": 75, "bam_factories_total": 3, "bam_factories_locations": ["Washington_1", "Washington_2", "South_Korea"], "material": "SCC55_silicon_carbon_composite", "graphite_replacement_potential": True, "customer_contracts_confirmed": False, "listed_sk_value_bridge_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_evidence",
        rerating_result="unknown",
        round_rerating_label="silicon_anode_scaleup_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="unlisted_material_scaleup_not_listed_EPS_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Unlisted battery-material scale-up cannot become listed-stock Green without an explicit value bridge.",
    ),
    Round285CaseCandidate(
        case_id="r3_loop14_korean_battery_ess_pivot_cross_reference",
        symbol="373220/006400/096770",
        company_name="LGES / Samsung SDI / SK On ESS pivot basket",
        primary_archetype=E2RArchetype.BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE,
        secondary_archetypes=(E2RArchetype.ESS_LFP_GRID_STORAGE, E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT),
        case_type="success_candidate",
        round_case_type="success_candidate + 4B-watch",
        stage1_date=date(2025, 7, 1),
        stage2_date=date(2025, 9, 3),
        stage3_date=None,
        stage4b_date=date(2025, 9, 3),
        stage4c_date=None,
        stage3_decision="ESS_pivot_is_stage2_until_PO_value_shipment_installation_margin_and_repeat_orders_confirm",
        stage4b_status="4B-watch/ESS-pivot-before-PO-value-installation-margin",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Flatiron_ESS_LFP_7_2GWh_2026_2030", "Georgia_EV_lines_conversion_planned", "LGES_Samsung_SDI_ESS_repurposing_context", "data_center_energy_storage_demand_context"),
        red_flag_fields=("contract_value_undisclosed", "actual_installation_margin_unconfirmed", "subsidy_phaseout_overhang", "slower_EV_demand"),
        price_data_source="Reuters SK On ESS and battery-sector pivot anchors",
        reported_price_anchor="Flatiron up to 7.2GWh 2026-2030; value undisclosed",
        reported_return_anchor="ESS pivot is Stage 2; PO value, installation, margin and repeat orders are required.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"flatiron_ess_supply_gwh": 7.2, "supply_period": "2026-2030", "lfp_ess_first_order": True, "ev_line_conversion_for_ess": "Georgia_EV_lines_some_conversion_planned", "contract_value_disclosed": False, "lges_samsung_sdi_ess_repurposing_context": True, "data_center_energy_storage_demand_context": True, "actual_installation_margin_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="ESS_pivot_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="ESS_pivot_not_PO_value_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="ESS is a possible next-cycle path, but Green needs PO value, shipment, installation, margin and repeat orders.",
    ),
)


def round285_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND285_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND285_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round285 R3 Loop-14 battery/EV/green-energy price-validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=candidate.evidence_fields if candidate.stage3_date else (),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("premium", "pivot", "headline", "capex", "funding", "watch", "ess"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("cancel", "loss", "sluggish", "customs", "furlough", "hybrid", "utilization", "delay", "dissolution", "4c"))),
            must_have_fields=ROUND285_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"structural_success", "success_candidate"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND285_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "round285_hard_4c_confirmed_true",
                "do_not_use_round285_cases_as_candidate_generation_input",
                "do_not_treat_EV_battery_IRA_ESS_solar_hydrogen_or_silicon_anode_keywords_as_green",
                *ROUND285_GREEN_REQUIRED_FIELDS,
                *ROUND285_GREEN_FORBIDDEN_PATTERNS,
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
                stage_dates_confidence=0.84 if candidate.price_validation_status != "price_data_unavailable_after_deep_search" else 0.72,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round285_case_rows() -> tuple[dict[str, str], ...]:
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
        for candidate in ROUND285_CASE_CANDIDATES
    )


def round285_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND285_SCORE_ADJUSTMENTS)


def round285_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND285_SHADOW_WEIGHT_ROWS)


def round285_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND285_DEEP_SUB_ARCHETYPES)


def round285_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round285_price_validation": "true"} for field in ROUND285_PRICE_VALIDATION_FIELDS)


def round285_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round285_label": label, "canonical_archetype": canonical} for label, canonical in ROUND285_REQUIRED_TARGET_ALIASES.items())


def round285_summary() -> dict[str, int | bool | str]:
    cases = ROUND285_CASE_CANDIDATES
    return {
        "source_round": ROUND285_SOURCE_ROUND_PATH,
        "round_id": ROUND285_ANALYST_ROUND_ID,
        "large_sector": ROUND285_LARGE_SECTOR,
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
        "target_archetype_count": len(ROUND285_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND285_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND285_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "hard_4c_watch_confirmed": any(case.hard_4c_watch_confirmed for case in cases),
    }


def round285_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND285_SOURCE_ROUND_PATH,
        "round_id": ROUND285_ANALYST_ROUND_ID,
        "large_sector": ROUND285_LARGE_SECTOR,
        "summary": round285_summary(),
        "target_aliases": dict(ROUND285_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND285_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND285_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND285_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND285_HARD_4C_GATES),
        "score_adjustments": list(round285_score_adjustment_rows()),
        "shadow_weights": list(round285_shadow_weight_rows()),
        "deep_sub_archetypes": list(round285_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND285_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round285_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_EV_battery_IRA_ESS_solar_hydrogen_or_silicon_anode_keywords_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round285_summary_markdown() -> str:
    summary = round285_summary()
    lines = [
        "# Round 285 R3 Loop 14 Secondary Battery EV Green Energy Price Validation",
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
    for case in ROUND285_CASE_CANDIDATES:
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
            "- LGES Ford/Freudenberg cancellation is the R3 hard 4C reference.",
            "- Samsung SDI/GM and SK On/ESS are Stage 2 examples, not Green, until call-off, utilization and margin close.",
            "- Battery-material suppliers need customer model mix and battery content checks; EV long-term growth is not enough.",
            "- Qcells, Hyundai hydrogen and SK/Group14 show policy/capex/funding evidence that remains below Green until utilization and unit economics confirm.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round285_green_gate_review_markdown() -> str:
    lines = [
        "# Round 285 R3 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R3 Stage 3-Green is not `battery`, `EV`, `IRA`, `solar`, `hydrogen`, `ESS`, or `silicon anode` as a label. It requires customer call-off, utilization, battery content, policy durability, customs clearance, PO value, margin and FCF.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND285_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND285_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND285_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `EV battery contract` becomes weaker if the automaker cancels the model or stops call-off.",
            "- `ESS pivot` is useful Stage 2 evidence, but Green waits for PO value, installation and margin.",
            "- `U.S. solar factory` still fails if components are stuck at customs and utilization drops.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round285_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 285 R3 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND285_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND285_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | hard 4C watch | interpretation |", "|---|---|---|---|---|---|"])
    for case in ROUND285_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.hard_4c_watch_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round285_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 285 R3 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, full MFE/MAE, call-off, utilization, AMPC quality, customs clearance, ESS value, hydrogen demand, silicon-anode contracts, or listed EPS bridge where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND285_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND285_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round285_r3_loop14_reports(
    output_directory: str | Path = ROUND285_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND285_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND285_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round285_case_records(), cases_path),
        "audit": _write_json(round285_audit_payload(), audit_path),
        "summary": output / "round285_r3_loop14_price_validation_summary.md",
        "case_matrix": output / "round285_r3_loop14_case_matrix.csv",
        "target_aliases": output / "round285_r3_loop14_target_aliases.csv",
        "score_adjustments": output / "round285_r3_loop14_score_adjustments.csv",
        "shadow_weights": output / "round285_r3_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round285_r3_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round285_r3_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round285_r3_loop14_green_gate_review.md",
        "price_validation_plan": output / "round285_r3_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round285_r3_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round285_summary_markdown(), encoding="utf-8")
    _write_csv(round285_case_rows(), paths["case_matrix"])
    _write_csv(round285_target_alias_rows(), paths["target_aliases"])
    _write_csv(round285_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round285_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round285_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round285_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round285_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round285_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round285_stage4b_4c_review_markdown(), encoding="utf-8")
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
    "ROUND285_CASE_CANDIDATES",
    "ROUND285_GREEN_FORBIDDEN_PATTERNS",
    "ROUND285_GREEN_REQUIRED_FIELDS",
    "ROUND285_HARD_4C_GATES",
    "ROUND285_LARGE_SECTOR",
    "ROUND285_PRICE_VALIDATION_FIELDS",
    "ROUND285_REQUIRED_TARGET_ALIASES",
    "ROUND285_SHADOW_WEIGHT_ROWS",
    "ROUND285_STAGE4B_WATCH_TRIGGERS",
    "render_round285_green_gate_review_markdown",
    "render_round285_stage4b_4c_review_markdown",
    "round285_audit_payload",
    "round285_case_records",
    "round285_case_rows",
    "round285_deep_sub_archetype_rows",
    "round285_shadow_weight_rows",
    "round285_summary",
    "write_round285_r3_loop14_reports",
]
