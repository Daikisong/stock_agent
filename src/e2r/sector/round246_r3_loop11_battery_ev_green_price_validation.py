"""Round-246 R3 Loop-11 battery/EV/green price-validation pack.

This module converts ``docs/round/round_246.md`` into structured,
calibration-only case-library records and reports. It does not change
production scoring or candidate generation.

Easy example: a 3-year LFP ESS contract is useful Stage 2 evidence. It is not
Stage 3-Green until delivery, utilization, OPM/gross margin, FCF, and
customs/labor/customer-demand risks are checked.
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


ROUND246_SOURCE_ROUND_PATH = "docs/round/round_246.md"
ROUND246_ROUND_ID = "round_174"
ROUND246_LARGE_SECTOR = Round10LargeSector.BATTERY_EV_GREEN.value
ROUND246_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round246_r3_loop11_battery_ev_green_price_validation"
ROUND246_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop11_round246.jsonl"
ROUND246_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round246_r3_loop11_battery_ev_green_price_validation_audit.json"

ROUND246_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "ESS_LFP_GRID_STORAGE": E2RArchetype.ESS_LFP_GRID_STORAGE.value,
    "EV_TO_ESS_CAPACITY_REDEPLOYMENT": E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT.value,
    "US_BATTERY_LOCALIZATION": E2RArchetype.US_BATTERY_LOCALIZATION.value,
    "EV_BATTERY_CONTRACT_QUALITY_BREAK": E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK.value,
    "BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK": E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK.value,
    "LITHIUM_RESOURCE_SECURITY": E2RArchetype.LITHIUM_RESOURCE_SECURITY.value,
    "LITHIUM_OFFTAKE_DLE_OPTIONALITY": E2RArchetype.LITHIUM_OFFTAKE_DLE_OPTIONALITY.value,
    "SOLAR_US_SUPPLY_CHAIN_LOCALIZATION": E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION.value,
    "SOLAR_CUSTOMS_UFLPA_4C_WATCH": E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH.value,
    "EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK": E2RArchetype.EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK.value,
}

ROUND246_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "binding_contract",
    "customer_gwh_supply_period_confirmed",
    "actual_delivery_or_revenue_recognition_started",
    "utilization_improvement",
    "opm_or_gross_margin_confirmed",
    "fcf_after_capex",
    "subsidy_excluded_profit_quality",
    "customer_ev_strategy_or_ess_demand_risk_passed",
    "supply_chain_customs_labor_execution_risk_passed",
    "price_path_after_evidence",
)

ROUND246_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ev_capacity_announcement_only",
    "ess_lfp_theme_only",
    "customer_name_only",
    "unofficial_customer_source_only",
    "factory_construction_only",
    "lithium_resource_headline_only",
    "solar_localization_headline_only",
    "subsidy_excluded_losses",
    "contract_value_without_utilization",
)

ROUND246_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "ess_lfp_contract_headline_rally",
    "ev_line_conversion_headline_multiple_expansion",
    "unofficial_customer_name_rally",
    "lithium_resource_security_price_first",
    "solar_localization_before_utilization",
    "battery_factory_construction_before_utilization",
    "ev_demand_slowdown_ignored",
)

ROUND246_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "contract_value_collapse",
    "customer_ev_model_cancellation",
    "customer_strategy_pullback",
    "gwh_calloff_failure",
    "utilization_delay",
    "factory_restart_uncertainty",
    "negative_fcf",
    "jv_termination_or_weak_demand_transfer",
    "subsidy_quality_profit_collapse",
    "supply_chain_customs_detention",
    "production_furlough",
    "immigration_skilled_worker_execution_failure",
)

ROUND246_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "contract_value_anchor",
    "gwh_or_capacity_anchor",
    "delivery_or_supply_period_anchor",
    "utilization_or_labor_execution_anchor",
    "lost_revenue_or_cancellation_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round246ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round246ShadowWeightRow:
    archetype: E2RArchetype
    binding_contract: int
    gwh_volume: int
    delivery_schedule: int
    ess_revenue_conversion: int
    line_retrofit_execution: int
    utilization: int
    opm_fcf: int
    customer_quality: int
    event_penalty: int
    execution_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "binding_contract": _signed(self.binding_contract),
            "gwh_volume": _signed(self.gwh_volume),
            "delivery_schedule": _signed(self.delivery_schedule),
            "ess_revenue_conversion": _signed(self.ess_revenue_conversion),
            "line_retrofit_execution": _signed(self.line_retrofit_execution),
            "utilization": _signed(self.utilization),
            "opm_fcf": _signed(self.opm_fcf),
            "customer_quality": _signed(self.customer_quality),
            "event_penalty": _signed(self.event_penalty),
            "execution_redteam": _signed(self.execution_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round246DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round246CaseCandidate:
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


ROUND246_SCORE_ADJUSTMENTS: tuple[Round246ScoreAdjustment, ...] = (
    Round246ScoreAdjustment("binding_contract", 5, "raise", "R3는 계약이 binding일수록 Stage 2 품질이 올라간다."),
    Round246ScoreAdjustment("GWh_volume", 5, "raise", "ESS/LFP는 GWh 물량이 없으면 visibility가 약하다."),
    Round246ScoreAdjustment("delivery_schedule", 5, "raise", "납기와 공급기간이 있어야 매출 전환 경로가 보인다."),
    Round246ScoreAdjustment("ESS_revenue_conversion", 5, "raise", "ESS 계약은 실제 매출 전환 전 Green이 아니다."),
    Round246ScoreAdjustment("line_retrofit_execution", 4, "raise", "EV 라인을 ESS로 전환하는 실행력이 중요하다."),
    Round246ScoreAdjustment("utilization_rate", 5, "raise", "공장·라인 보유보다 가동률 회복이 더 중요하다."),
    Round246ScoreAdjustment("OPM_visibility", 5, "raise", "OPM/gross margin 확인 전 Stage 3-Green 금지다."),
    Round246ScoreAdjustment("FCF_after_capex", 5, "raise", "CAPEX 뒤 FCF가 남아야 구조적이다."),
    Round246ScoreAdjustment("customer_quality", 4, "raise", "고객 품질과 수요 안정성은 Stage 2 증거다."),
    Round246ScoreAdjustment("resource_security_with_offtake", 4, "raise", "리튬 자원 확보는 offtake와 downstream margin이 붙을 때 강하다."),
    Round246ScoreAdjustment("EV_capacity_announcement_only", -5, "lower", "EV CAPA 발표만으로는 수익 가시성이 없다."),
    Round246ScoreAdjustment("ESS_theme_only", -4, "lower", "ESS/LFP 테마만으로는 매출·마진·FCF가 아니다."),
    Round246ScoreAdjustment("customer_name_without_calloff", -5, "lower", "고객명만 있고 call-off가 없으면 Green 금지다."),
    Round246ScoreAdjustment("contract_value_without_utilization", -4, "lower", "계약금액만 있고 가동률이 없으면 Stage 2에 머문다."),
    Round246ScoreAdjustment("unofficial_customer_source_only", -3, "lower", "비공식 고객 보도는 disclosure confidence를 낮춘다."),
    Round246ScoreAdjustment("lithium_price_rebound_only", -5, "lower", "리튬 가격 반등만으로는 구조적 EPS/FCF가 아니다."),
    Round246ScoreAdjustment("solar_localization_without_component_flow", -5, "lower", "태양광 현지화는 component flow와 utilization이 필요하다."),
    Round246ScoreAdjustment("factory_construction_without_labor_execution", -4, "lower", "공장 건설은 labor/visa execution 전 Green이 아니다."),
    Round246ScoreAdjustment("subsidy_dependent_profit", -5, "lower", "보조금 제외 이익 품질이 약하면 감점한다."),
    Round246ScoreAdjustment("EV_demand_shock", -5, "lower", "고객 EV 전략 후퇴는 R3 핵심 4C-watch다."),
    Round246ScoreAdjustment("contract_cancellation", -5, "lower", "계약 취소는 hard 4C다."),
)

ROUND246_SHADOW_WEIGHT_ROWS: tuple[Round246ShadowWeightRow, ...] = (
    Round246ShadowWeightRow(E2RArchetype.ESS_LFP_GRID_STORAGE, 5, 5, 5, 5, 4, 5, 5, 4, -2, 2, 4, 4, "Samsung SDI/LGES/SK On ESS contracts are Stage 2 until delivery/utilization/margin/FCF confirm."),
    Round246ShadowWeightRow(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, 4, 5, 5, 5, 5, 5, 5, 3, -3, 4, 4, 5, "EV line conversion is positive only if utilization and ESS margins confirm."),
    Round246ShadowWeightRow(E2RArchetype.US_BATTERY_LOCALIZATION, 4, 4, 4, 4, 5, 5, 5, 4, -3, 5, 4, 5, "U.S. localization must pass customs/visa/labor execution risks."),
    Round246ShadowWeightRow(E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 5, "LGES Ford/Freudenberg cancellations are hard 4C."),
    Round246ShadowWeightRow(E2RArchetype.LITHIUM_RESOURCE_SECURITY, 3, 3, 3, 2, 0, 3, 5, 3, -4, 2, 4, 4, "POSCO/MinRes is Stage 2; lithium cycle and downstream margin matter."),
    Round246ShadowWeightRow(E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION, 3, 3, 4, 3, 4, 5, 5, 4, -4, 5, 4, 5, "Qcells localization is blocked by customs/component flow risk."),
    Round246ShadowWeightRow(E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 5, "Ford EV retreat is 4C-watch for Korean battery/cathode supply chain."),
    Round246ShadowWeightRow(E2RArchetype.EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK, 0, 0, 0, 0, 3, 3, 3, 2, 0, 5, 4, 5, "Georgia raid shows U.S. plant execution risk beyond capex headline."),
)

ROUND246_DEEP_SUB_ARCHETYPES: tuple[Round246DeepSubArchetype, ...] = (
    Round246DeepSubArchetype("ESS transition", E2RArchetype.ESS_LFP_GRID_STORAGE, ("Samsung SDI America", "LGES Tesla", "SK On Flatiron", "LFP ESS", "grid storage")),
    Round246DeepSubArchetype("EV-to-ESS redeployment", E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, ("Georgia EV lines", "line retrofit", "ESS production", "utilization")),
    Round246DeepSubArchetype("U.S. battery localization", E2RArchetype.US_BATTERY_LOCALIZATION, ("U.S. factory", "Michigan LFP", "IRA localization", "customs labor risk")),
    Round246DeepSubArchetype("Contract quality break", E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK, ("LGES Ford cancellation", "Freudenberg cancellation", "lost expected revenue")),
    Round246DeepSubArchetype("Lithium resource security", E2RArchetype.LITHIUM_RESOURCE_SECURITY, ("POSCO", "MinRes", "Wodgina", "Mt Marion", "spodumene cycle")),
    Round246DeepSubArchetype("Solar localization 4C", E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH, ("Hanwha Qcells", "UFLPA", "customs detention", "furlough")),
    Round246DeepSubArchetype("EV demand shock", E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK, ("Ford EV retreat", "LGES -6%", "Samsung SDI -3.5%", "POSCO Future M -8.2%")),
    Round246DeepSubArchetype("Factory execution risk", E2RArchetype.EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK, ("Hyundai-LG Georgia", "immigration raid", "skilled-worker visa", "construction restart")),
)

ROUND246_CASE_CANDIDATES: tuple[Round246CaseCandidate, ...] = (
    Round246CaseCandidate(
        case_id="r3_loop11_samsung_sdi_lfp_ess_us_contract",
        symbol="006400",
        company_name="Samsung SDI America / Samsung SDI",
        primary_archetype=E2RArchetype.ESS_LFP_GRID_STORAGE,
        secondary_archetypes=(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, E2RArchetype.US_BATTERY_LOCALIZATION, E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH),
        case_type="success_candidate",
        round_case_type="success_candidate_ess_conversion_4b_watch",
        stage1_date=None,
        stage2_date=date(2025, 12, 9),
        stage3_date=None,
        stage4b_date=date(2025, 12, 9),
        stage4c_date=None,
        stage3_decision="strong_ess_stage2_but_customer_delivery_utilization_opm_fcf_required_before_green",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("binding_lfp_ess_contract", "contract_value_over_2t_krw", "delivery_start_2027", "contract_duration_3_years", "existing_us_line_retrofit", "event_mfe_6_1pct"),
        red_flag_fields=("customer_unnamed", "actual_delivery_unconfirmed", "utilization_unconfirmed", "ess_opm_fcf_unconfirmed"),
        price_data_source="Reuters contract/event-return anchor",
        reported_price_anchor="Samsung SDI +6.1%; KOSPI -0.1%",
        reported_return_anchor=">2T KRW / $1.36B LFP ESS contract, delivery begins 2027",
        mfe_1d=6.1,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"contract_value_krw_trn_min": 2.0, "contract_value_usd_bn": 1.36, "delivery_start_year": 2027, "contract_duration_years": 3, "kospi_same_context_pct": -0.1, "relative_outperformance_pp": 6.2, "battery_type": "prismatic LFP ESS", "production_method": "retrofitting existing U.S. plant lines"},
        score_price_alignment="aligned",
        round_alignment_label="Stage 2",
        rerating_result="unknown",
        round_rerating_label="ESS_LFP_contract_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Strong ESS Stage 2; customer, delivery, utilization, OPM and FCF must confirm before Green.",
    ),
    Round246CaseCandidate(
        case_id="r3_loop11_lges_tesla_lfp_ess_contract",
        symbol="373220",
        company_name="LG Energy Solution",
        primary_archetype=E2RArchetype.ESS_LFP_GRID_STORAGE,
        secondary_archetypes=(E2RArchetype.US_BATTERY_LOCALIZATION, E2RArchetype.BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE),
        case_type="success_candidate",
        round_case_type="success_candidate_customer_confidentiality_watch",
        stage1_date=None,
        stage2_date=date(2025, 7, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="strong_ess_localization_stage2_but_official_customer_delivery_utilization_margin_required",
        stage4b_status="4B-watch-if-Tesla-name-rally",
        hard_4c_confirmed=False,
        evidence_fields=("global_lfp_supply_contract_4_3bn_usd", "reported_customer_tesla_source", "contract_period_2027_08_to_2030_07", "extension_option_up_to_7_years", "volume_increase_option", "us_factory_lfp_production"),
        red_flag_fields=("official_customer_not_disclosed", "unofficial_customer_source_only", "delivery_unconfirmed", "utilization_unconfirmed", "ess_margin_unconfirmed"),
        price_data_source="Reuters source-based contract anchor",
        reported_price_anchor="Reuters did not provide stock reaction anchor",
        reported_return_anchor="$4.3B LFP supply contract; Tesla named by Reuters source; contract period 2027-08 to 2030-07",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"contract_value_usd_bn": 4.3, "official_customer_disclosure": "not_disclosed_by_LGES", "reported_customer": "Tesla according to Reuters source", "extension_option_years": 7, "volume_increase_option": True, "lfp_production_started_michigan": "2025-05"},
        score_price_alignment="unknown",
        round_alignment_label="Stage 2",
        rerating_result="unknown",
        round_rerating_label="US_LFP_ESS_localization_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_contract_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Strong ESS/localization Stage 2; official customer disclosure, delivery, utilization and margin required before Green.",
    ),
    Round246CaseCandidate(
        case_id="r3_loop11_skon_flatiron_lfp_ess",
        symbol="096770_parent_exposure",
        company_name="SK On / SK Innovation exposure",
        primary_archetype=E2RArchetype.ESS_LFP_GRID_STORAGE,
        secondary_archetypes=(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT,),
        case_type="success_candidate",
        round_case_type="success_candidate_ev_to_ess_redeployment",
        stage1_date=None,
        stage2_date=date(2025, 9, 3),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="first_skon_lfp_ess_order_is_stage2_until_contract_value_utilization_opm_fcf_confirm",
        stage4b_status="4B-watch-if-ESS-pivot-rally",
        hard_4c_confirmed=False,
        evidence_fields=("flatiron_lfp_ess_contract_up_to_7_2gwh", "supply_2026_2030", "first_sk_on_lfp_ess_order", "georgia_ev_lines_converted_to_ess"),
        red_flag_fields=("contract_value_not_disclosed", "utilization_unconfirmed", "ess_opm_fcf_unconfirmed", "ev_order_slowdown_risk"),
        price_data_source="Reuters ESS contract anchor",
        reported_price_anchor="Reuters did not provide stock reaction anchor",
        reported_return_anchor="Up to 7.2GWh, 2026-2030 supply, first SK On LFP ESS order",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"contract_volume_gwh": 7.2, "supply_period": "2026-2030", "battery_type": "LFP ESS", "first_sk_on_lfp_ess_order": True, "production_start": "2H_2026", "capacity_redeployment": "some Georgia EV battery lines converted to ESS", "contract_value": "not_disclosed"},
        score_price_alignment="unknown",
        round_alignment_label="Stage 2",
        rerating_result="unknown",
        round_rerating_label="SK_On_ESS_pivot_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="ESS pivot is Stage 2; contract value, utilization, OPM and FCF required before Green.",
    ),
    Round246CaseCandidate(
        case_id="r3_loop11_lges_ford_freudenberg_contract_hard_4c",
        symbol="373220",
        company_name="LG Energy Solution",
        primary_archetype=E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK,
        secondary_archetypes=(E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="hard_4c_contract_quality_break",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 17),
        stage3_decision="contract_headline_cannot_be_green_without_actual_calloff_utilization_and_customer_strategy_stability",
        stage4b_status="not_applicable_hard_4C",
        hard_4c_confirmed=True,
        evidence_fields=("ford_cancelled_contract_9_6t_krw", "freudenberg_cancelled_contract_3_9t_krw", "lost_expected_revenue_13_5t_krw", "lost_revenue_52_7pct_of_2024_revenue"),
        red_flag_fields=("contract_cancellation", "contract_value_collapse", "customer_ev_model_cancellation", "customer_strategy_pullback", "relative_underperformance_minus_6_2pp"),
        price_data_source="Reuters contract cancellation and event-return anchors",
        reported_price_anchor="LGES -7.6% intraday after Ford cancellation; KOSPI -1.4%",
        reported_return_anchor="Ford $6.5B cancellation and Freudenberg $2.7B cancellation; total 13.5T KRW expected revenue loss",
        mfe_1d=None,
        mae_1d=-7.6,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ford_cancelled_contract_krw_trn": 9.6, "ford_cancelled_contract_usd_bn": 6.5, "freudenberg_cancelled_contract_krw_trn": 3.9, "freudenberg_cancelled_contract_usd_bn": 2.7, "total_lost_expected_revenue_krw_trn": 13.5, "lges_2024_revenue_krw_trn": 25.62, "lost_revenue_vs_2024_revenue_pct": 52.7, "kospi_same_context_pct": -1.4, "relative_underperformance_pp": -6.2, "freudenberg_cancellation_date": "2025-12-26"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="contract break",
        rerating_result="thesis_break",
        round_rerating_label="battery_contract_quality_failure",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Ford/Freudenberg cancellations are hard 4C; contract headline cannot be Green without actual call-off and utilization.",
    ),
    Round246CaseCandidate(
        case_id="r3_loop11_posco_minres_lithium_resource_security",
        symbol="005490",
        company_name="POSCO Holdings / MinRes lithium JV",
        primary_archetype=E2RArchetype.LITHIUM_RESOURCE_SECURITY,
        secondary_archetypes=(E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA, E2RArchetype.LITHIUM_CYCLE_OVERLAY, E2RArchetype.EVENT_LITHIUM_PRICE_RALLY),
        case_type="success_candidate",
        round_case_type="success_candidate_cyclical_watch",
        stage1_date=None,
        stage2_date=date(2025, 11, 11),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="resource_security_is_stage2_until_downstream_margin_offtake_economics_and_fcf_confirm",
        stage4b_status="4B-watch-if-lithium-rebound-rally",
        hard_4c_confirmed=False,
        evidence_fields=("minres_lithium_jv_stake_765m_usd", "indirect_15pct_wodgina_mt_marion", "spodumene_concentrate_right", "minres_event_mfe_10_8pct"),
        red_flag_fields=("lithium_cycle", "spodumene_peak_to_low_drawdown", "downstream_margin_unconfirmed", "fcf_unconfirmed"),
        price_data_source="Reuters lithium transaction/commodity anchors",
        reported_price_anchor="MinRes +10.8%; POSCO OHLC unavailable",
        reported_return_anchor="$765M JV stake; spodumene 2022 peak >$6000/t, 2025 low ~$610/t, rebound to $880/t",
        mfe_1d=10.8,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"transaction_value_usd_mn": 765, "posco_indirect_stake_pct": 15, "assets": ["Wodgina", "Mt Marion"], "spodumene_peak_2022_usd_per_t": 6000, "spodumene_low_2025_usd_per_t": 610, "spodumene_drawdown_peak_to_low_pct": -89.8, "spodumene_rebound_610_to_880_pct": 44.3, "spodumene_880_vs_peak_pct": -85.3},
        score_price_alignment="unknown",
        round_alignment_label="resource Stage 2",
        rerating_result="unknown",
        round_rerating_label="lithium_resource_security_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="posco_stock_ohlc_unavailable_after_deep_search",
        notes="Resource security is Stage 2; downstream margin, offtake economics and FCF required before Green.",
    ),
    Round246CaseCandidate(
        case_id="r3_loop11_hanwha_qcells_customs_supply_chain_4c_watch",
        symbol="009830/000880_exposure",
        company_name="Hanwha Qcells / Hanwha Solutions exposure",
        primary_archetype=E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION,
        secondary_archetypes=(E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="success_candidate",
        round_case_type="success_candidate_plus_4c_watch",
        stage1_date=None,
        stage2_date=date(2024, 8, 8),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 11, 8),
        stage3_decision="solar_localization_capex_is_stage2_but_component_flow_utilization_margin_and_fcf_required",
        stage4b_status="4B-watch-if-solar-localization-rally",
        hard_4c_confirmed=False,
        evidence_fields=("doe_conditional_loan_guarantee_1_45bn_usd", "cartersville_facility_investment_2_3_to_2_5bn_usd", "panels_cells_ingots_wafers_scope", "nearly_2000_jobs_when_operational"),
        red_flag_fields=("supply_chain_customs_detention", "production_furlough", "component_flow_failure", "about_1000_furloughed_or_reduced_hours", "300_contract_workers_cut"),
        price_data_source="Reuters/AP solar localization and customs-disruption anchors",
        reported_price_anchor="Reuters/AP did not provide stock reaction anchor",
        reported_return_anchor="$1.45B conditional DOE guarantee; about 1,000 furloughs/reduced hours and 300 staffing-worker cuts",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"doe_conditional_loan_guarantee_usd_bn": 1.45, "cartersville_facility_investment_usd_bn_reuters": 2.5, "cartersville_facility_investment_usd_bn_ap": 2.3, "jobs_when_fully_operational": 2000, "furloughed_or_reduced_hours_workers": 1000, "contract_workers_cut": 300, "affected_direct_workers_total": 1300, "cause": "U.S. customs detentions under forced-labor import law / UFLPA context"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="supply-chain watch",
        rerating_result="unknown",
        round_rerating_label="solar_localization_watch_with_supply_chain_risk",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_with_4C_watch",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Solar localization is Stage 2; customs/component disruption and furloughs create 4C-watch.",
    ),
    Round246CaseCandidate(
        case_id="r3_loop11_ford_ev_retreat_supply_chain_shock",
        symbol="373220/006400/003670/361610/450080",
        company_name="LGES / Samsung SDI / POSCO Future M / SKIET / EcoPro Materials basket",
        primary_archetype=E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK,
        secondary_archetypes=(E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="failed_rerating",
        round_case_type="4c_watch_demand_shock",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 16),
        stage3_decision="ford_ev_retreat_is_supply_chain_4c_watch_until_utilization_and_customer_demand_recover",
        stage4b_status="not_applicable_4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("ford_ev_retreat", "lges_event_mae_minus_6pct", "samsung_sdi_event_mae_minus_3_5pct", "posco_future_m_event_mae_minus_8_2pct"),
        red_flag_fields=("customer_ev_model_cancellation", "customer_strategy_pullback", "ev_demand_shock", "battery_supply_chain_drawdown"),
        price_data_source="Reuters event-return anchor",
        reported_price_anchor="LGES -6%, Samsung SDI -3.5%, POSCO Future M -8.2%",
        reported_return_anchor="Ford EV retreat / model cuts",
        mfe_1d=None,
        mae_1d=-8.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"lges_event_mae_pct": -6.0, "samsung_sdi_event_mae_pct": -3.5, "posco_future_m_event_mae_pct": -8.2, "ford_context": "EV retreat / model cuts"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="demand shock",
        rerating_result="thesis_break",
        round_rerating_label="EV_supply_chain_demand_shock",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="should_have_been_yellow_or_red",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="Ford EV retreat shows demand shock across Korean battery/cathode supply chain.",
    ),
    Round246CaseCandidate(
        case_id="r3_loop11_hyundai_lg_georgia_battery_raid_execution_watch",
        symbol="005380/000270/373220",
        company_name="Hyundai-LG Georgia battery plant / HL-GA Battery",
        primary_archetype=E2RArchetype.EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK,
        secondary_archetypes=(E2RArchetype.US_BATTERY_LOCALIZATION, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="failed_rerating",
        round_case_type="4c_watch_factory_execution_risk",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="factory_construction_alone_is_not_green_without_line_start_utilization_local_labor_visa_stability_and_fcf",
        stage4b_status="not_applicable_4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("hyundai_georgia_ev_site_battery_plant", "hl_ga_battery_jv", "production_target_h1_2026"),
        red_flag_fields=("immigration_skilled_worker_execution_failure", "over_300_korean_workers_detained", "construction_shut_down_temporarily", "skilled_worker_visa_policy_risk"),
        price_data_source="AP immigration-raid and restart anchors",
        reported_price_anchor="AP did not provide stock reaction anchor",
        reported_return_anchor="More than 300 Korean workers detained; construction halted then resumed",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage4c_month": "2025-09", "detained_workers": "over_300_Korean_workers", "ap_update_detainees": 330, "ap_update_koreans": 316, "operator": "HL-GA Battery Co., Hyundai-LG joint venture", "disruption": "construction shut down after raid", "relief": "some workers returned and construction resumed", "production_target": "H1_2026"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="factory execution risk",
        rerating_result="unknown",
        round_rerating_label="US_battery_factory_execution_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch_not_hard_4C",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="U.S. localization requires visa/skilled-worker/labor execution; construction alone is not Green.",
    ),
)


def round246_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("delivery", "utilization", "opm", "fcf", "margin", "revenue", "gross")
    for candidate in ROUND246_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND246_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round246 R3 Loop-11 battery/EV/green price-validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "rally" in field.lower() or "event" in field.lower() or "price" in field.lower() or "headline" in field.lower()),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "cancellation" in field.lower()
                or "shock" in field.lower()
                or "pullback" in field.lower()
                or "detention" in field.lower()
                or "furlough" in field.lower()
                or "failure" in field.lower()
                or "delay" in field.lower()
                or "shut" in field.lower()
            ),
            must_have_fields=ROUND246_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "4c_thesis_break", "event_premium", "overheat", "4b_watch"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND246_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_ess_lfp_lithium_solar_localization_or_factory_construction_as_green_alone",
                *ROUND246_GREEN_REQUIRED_FIELDS,
                *ROUND246_GREEN_FORBIDDEN_PATTERNS,
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
                price_data_available=candidate.mfe_1d is not None or candidate.mae_1d is not None,
                stage_dates_confidence=0.9 if candidate.hard_4c_confirmed else 0.75,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round246_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND246_CASE_CANDIDATES:
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


def round246_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND246_SCORE_ADJUSTMENTS)


def round246_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND246_SHADOW_WEIGHT_ROWS)


def round246_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND246_DEEP_SUB_ARCHETYPES)


def round246_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round246_price_validation": "true"} for field in ROUND246_PRICE_VALIDATION_FIELDS)


def round246_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round246_label": label, "canonical_archetype": canonical} for label, canonical in ROUND246_REQUIRED_TARGET_ALIASES.items())


def round246_summary() -> dict[str, int | bool | str]:
    cases = ROUND246_CASE_CANDIDATES
    return {
        "source_round": ROUND246_SOURCE_ROUND_PATH,
        "round_id": ROUND246_ROUND_ID,
        "large_sector": ROUND246_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B-watch" in case.stage4b_status or case.stage4b_date is not None),
        "watch_4c_count": sum(1 for case in cases if "4C" in case.stage4b_status or case.stage4c_date is not None or case.hard_4c_confirmed),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND246_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND246_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND246_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round246_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND246_SOURCE_ROUND_PATH,
        "round_id": ROUND246_ROUND_ID,
        "large_sector": ROUND246_LARGE_SECTOR,
        "summary": round246_summary(),
        "target_aliases": dict(ROUND246_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND246_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND246_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND246_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND246_HARD_4C_GATES),
        "deep_sub_archetypes": round246_deep_sub_archetype_rows(),
        "shadow_weights": round246_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round246_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_ess_lfp_lithium_solar_localization_or_factory_construction_as_green",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round246_summary_markdown() -> str:
    summary = round246_summary()
    lines = [
        "# Round 246 R3 Loop 11 Battery / EV / Green Price Validation",
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
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- 4C-watch cases: {summary['watch_4c_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | stage2 | stage3 | 4B | 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND246_CASE_CANDIDATES:
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
            "- Samsung SDI, LGES/Tesla-source, and SK On/Flatiron ESS contracts are Stage 2 watch items, not Green before delivery, utilization, OPM and FCF.",
            "- LGES Ford/Freudenberg cancellations are hard 4C because expected revenue disappeared after customer strategy changed.",
            "- POSCO/MinRes lithium resource security is Stage 2, but lithium price cycle and downstream margin cap Green.",
            "- Qcells and Hyundai-LG Georgia show why U.S. localization must pass customs, labor and visa execution risk.",
            "- Ford EV retreat is a supply-chain demand shock that should block unsafe battery/cathode Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round246_green_gate_review_markdown() -> str:
    lines = [
        "# Round 246 R3 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R3 Stage 3-Green is not `ESS/LFP/lithium/solar localization is good`. It requires contracts to close into GWh, delivery, utilization, OPM, FCF, and cleared execution risks.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND246_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND246_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `Samsung SDI +6.1% on an ESS contract` is useful Stage 2 evidence, but not Green until delivery, utilization, OPM and FCF confirm.",
            "- `Tesla according to source` is helpful context, but unofficial customer evidence cannot create Green alone.",
            "- `DOE loan guarantee for a solar plant` is Stage 2 at best if component flow and labor execution are not stable.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round246_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 246 R3 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND246_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND246_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B catches ESS/LFP, lithium, and solar-localization rallies that price before delivery, utilization or margin.",
            "- hard 4C catches contract cancellation, customer EV strategy pullback, customs detention, production furlough and immigration/labor execution failure.",
            "- This loop confirms LGES Ford/Freudenberg cancellations as hard 4C. Qcells and Hyundai-LG Georgia are strong 4C-watch, not hard 4C yet.",
            "",
            "## Case Notes",
            "",
        ]
    )
    for case in ROUND246_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or "4C" in case.stage4b_status or case.stage4c_date or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round246_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 246 R3 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "- Month-only risk events, such as the Hyundai-LG Georgia raid, are stored as metadata rather than fabricated exact dates.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND246_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round246_r3_loop11_reports(
    output_directory: str | Path = ROUND246_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND246_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND246_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round246_case_records(), cases_path),
        "audit": _write_json(round246_audit_payload(), audit_path),
        "summary": output / "round246_r3_loop11_price_validation_summary.md",
        "case_matrix": output / "round246_r3_loop11_case_matrix.csv",
        "target_aliases": output / "round246_r3_loop11_target_aliases.csv",
        "score_adjustments": output / "round246_r3_loop11_score_adjustments.csv",
        "shadow_weights": output / "round246_r3_loop11_shadow_weights.csv",
        "deep_sub_archetypes": output / "round246_r3_loop11_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round246_r3_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round246_r3_loop11_green_gate_review.md",
        "price_validation_plan": output / "round246_r3_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round246_r3_loop11_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round246_summary_markdown(), encoding="utf-8")
    _write_csv(round246_case_rows(), paths["case_matrix"])
    _write_csv(round246_target_alias_rows(), paths["target_aliases"])
    _write_csv(round246_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round246_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round246_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round246_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round246_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round246_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round246_stage4b_4c_review_markdown(), encoding="utf-8")
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
