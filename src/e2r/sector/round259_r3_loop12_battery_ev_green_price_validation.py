"""Round-259 R3 Loop-12 battery/EV/green price-validation pack.

This module converts ``docs/round/round_259.md`` into calibration-only
case-library records and reports. It intentionally leaves production scoring,
candidate generation, and StageClassifier thresholds unchanged.

Easy example: LGES losing Ford/Freudenberg expected revenue is hard 4C. By
contrast, SK On's ESS pivot or Hyundai's hydrogen plant can be Stage 2 research
evidence, but not Stage 3-Green before call-off, utilization, OPM, FCF, and
execution risks clear.
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


ROUND259_SOURCE_ROUND_PATH = "docs/round/round_259.md"
ROUND259_ROUND_ID = "round_187"
ROUND259_LARGE_SECTOR = Round10LargeSector.BATTERY_EV_GREEN.value
ROUND259_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round259_r3_loop12_battery_ev_green_price_validation"
ROUND259_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop12_round259.jsonl"
ROUND259_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round259_r3_loop12_battery_ev_green_price_validation_audit.json"

ROUND259_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "EV_BATTERY_CONTRACT_QUALITY_BREAK": E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK.value,
    "EV_BATTERY_JV_RESTRUCTURING": E2RArchetype.EV_BATTERY_JV_RESTRUCTURING.value,
    "EV_TO_ESS_CAPACITY_REDEPLOYMENT": E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT.value,
    "US_BATTERY_LOCALIZATION_DILUTION": E2RArchetype.US_BATTERY_LOCALIZATION_DILUTION.value,
    "BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK": E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK.value,
    "SILICON_ANODE_OPTIONALITY": E2RArchetype.SILICON_ANODE_OPTIONALITY.value,
    "SOLAR_US_SUPPLY_CHAIN_LOCALIZATION": E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION.value,
    "SOLAR_CUSTOMS_UFLPA_4C_WATCH": E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH.value,
    "HYDROGEN_FUELCELL_CAPEX_OPTIONALITY": E2RArchetype.HYDROGEN_FUELCELL_CAPEX_OPTIONALITY.value,
    "US_FACTORY_EXECUTION_VISA_RISK": E2RArchetype.US_FACTORY_EXECUTION_VISA_RISK.value,
}

ROUND259_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "actual_calloff_or_take_or_pay_confirmed",
    "gwh_volume_and_supply_period_confirmed",
    "delivery_or_revenue_recognition_started",
    "utilization_improvement",
    "opm_or_gross_margin_confirmed",
    "fcf_after_capex_confirmed",
    "subsidy_excluded_unit_economics_confirmed",
    "customs_visa_labor_supply_chain_flow_risk_passed",
    "price_path_after_evidence",
)

ROUND259_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ev_jv_headline_only",
    "us_localization_capex_only",
    "ess_pivot_only",
    "hydrogen_plant_only",
    "silicon_anode_optionality_only",
    "solar_loan_guarantee_only",
    "share_issuance_for_capex_without_demand_quality",
    "contract_cancellation_present",
    "customs_detention_present",
    "factory_startup_delay_present",
)

ROUND259_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "ess_pivot_news_rally_before_contract_value",
    "ev_line_conversion_headline_valuation_expansion",
    "silicon_anode_hydrogen_solar_localization_theme_rally",
    "loan_guarantee_price_rise_before_revenue",
    "us_factory_opening_expectation_before_utilization",
    "capex_funding_or_share_issuance_valuation_holds",
)

ROUND259_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "contract_value_collapse",
    "customer_ev_model_cancellation",
    "jv_dissolution_or_customer_exit",
    "plant_idling",
    "utilization_failure",
    "large_layoff_or_restart_uncertainty",
    "customs_detention_causing_production_cut",
    "visa_raid_factory_startup_delay",
    "share_issuance_dilution_with_weak_demand",
    "opm_collapse",
    "fcf_deterioration",
)

ROUND259_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "contract_or_jv_value_anchor",
    "gwh_or_capacity_anchor",
    "lost_revenue_or_cancellation_anchor",
    "utilization_layoff_restart_anchor",
    "customs_visa_factory_execution_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round259ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round259ShadowWeightRow:
    archetype: E2RArchetype
    actual_calloff: int
    take_or_pay: int
    gwh_volume: int
    delivery_schedule: int
    utilization: int
    ess_revenue: int
    line_redeployment: int
    opm_visibility: int
    fcf_after_capex: int
    supply_chain_flow: int
    factory_execution: int
    event_penalty: int
    stage4b_watch_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "actual_calloff": _signed(self.actual_calloff),
            "take_or_pay": _signed(self.take_or_pay),
            "gwh_volume": _signed(self.gwh_volume),
            "delivery_schedule": _signed(self.delivery_schedule),
            "utilization": _signed(self.utilization),
            "ess_revenue": _signed(self.ess_revenue),
            "line_redeployment": _signed(self.line_redeployment),
            "opm_visibility": _signed(self.opm_visibility),
            "fcf_after_capex": _signed(self.fcf_after_capex),
            "supply_chain_flow": _signed(self.supply_chain_flow),
            "factory_execution": _signed(self.factory_execution),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round259DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round259CaseCandidate:
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


ROUND259_SCORE_ADJUSTMENTS: tuple[Round259ScoreAdjustment, ...] = (
    Round259ScoreAdjustment("actual_calloff", 5, "raise", "계약 headline은 actual call-off 또는 take-or-pay로 닫혀야 한다."),
    Round259ScoreAdjustment("take_or_pay_quality", 5, "raise", "take-or-pay 품질이 높을수록 매출 visibility가 높다."),
    Round259ScoreAdjustment("GWh_volume", 5, "raise", "R3 계약은 GWh 물량과 기간이 핵심이다."),
    Round259ScoreAdjustment("delivery_schedule", 5, "raise", "납기와 revenue recognition path가 있어야 Stage 2 품질이 올라간다."),
    Round259ScoreAdjustment("utilization_visibility", 5, "raise", "공장·라인보다 실제 가동률 회복이 중요하다."),
    Round259ScoreAdjustment("ESS_revenue_conversion", 5, "raise", "ESS pivot은 매출·마진 전환이 확인될 때 강해진다."),
    Round259ScoreAdjustment("line_redeployment_execution", 4, "raise", "EV 라인을 ESS로 전환하는 실행력이 필요하다."),
    Round259ScoreAdjustment("OPM_visibility", 5, "raise", "OPM/gross margin 확인 전 Green은 금지다."),
    Round259ScoreAdjustment("FCF_after_capex", 5, "raise", "CAPEX 뒤 FCF가 남아야 구조적이다."),
    Round259ScoreAdjustment("supply_chain_flow_reliability", 5, "raise", "Qcells처럼 component flow가 막히면 localization이 깨진다."),
    Round259ScoreAdjustment("factory_execution_readiness", 5, "raise", "Hyundai-LG Georgia처럼 visa/workforce execution이 필요하다."),
    Round259ScoreAdjustment("EV_JV_headline_only", -5, "lower", "EV JV headline만으로는 Green이 아니다."),
    Round259ScoreAdjustment("US_localization_capex_only", -5, "lower", "미국 현지화 CAPEX만으로는 수익성이 없다."),
    Round259ScoreAdjustment("share_issuance_for_capex", -5, "lower", "수요 품질 없는 증자는 dilution risk다."),
    Round259ScoreAdjustment("customer_exit_report", -5, "lower", "고객 이탈 보도는 4C-watch다."),
    Round259ScoreAdjustment("ESS_pivot_without_contract_value", -4, "lower", "ESS pivot은 계약금액·마진 전 Stage 2다."),
    Round259ScoreAdjustment("silicon_anode_optionality_only", -4, "lower", "silicon-anode optionality만으로 Green 금지다."),
    Round259ScoreAdjustment("hydrogen_capex_without_offtake", -5, "lower", "수소 CAPEX는 offtake 전 Green이 아니다."),
    Round259ScoreAdjustment("solar_loan_guarantee_without_component_flow", -5, "lower", "태양광 loan guarantee는 component flow가 필요하다."),
    Round259ScoreAdjustment("factory_startup_visa_risk", -5, "lower", "visa/factory startup risk는 RedTeam 감점이다."),
    Round259ScoreAdjustment("EV_demand_shock", -5, "lower", "고객 EV 수요 후퇴는 R3 핵심 4C-watch다."),
)


ROUND259_SHADOW_WEIGHT_ROWS: tuple[Round259ShadowWeightRow, ...] = (
    Round259ShadowWeightRow(E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK, 5, 5, 5, 5, 5, 0, 0, 5, 5, 3, 3, 0, 3, 5, "LGES/Ford/Freudenberg shows contract headline can become hard 4C without actual call-off."),
    Round259ShadowWeightRow(E2RArchetype.EV_BATTERY_JV_RESTRUCTURING, 4, 4, 5, 4, 5, 3, 4, 5, 5, 3, 5, -5, 4, 5, "SK On/Ford and Samsung/Stellantis JV risks require 4C-watch."),
    Round259ShadowWeightRow(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, 4, 4, 5, 5, 5, 5, 5, 5, 5, 3, 4, -3, 5, 4, "ESS pivot is Stage 2 until contract value/utilization/margin/FCF confirm."),
    Round259ShadowWeightRow(E2RArchetype.US_BATTERY_LOCALIZATION_DILUTION, 3, 3, 4, 4, 4, 2, 3, 4, 5, 4, 5, -5, 4, 5, "Samsung SDI share issuance shows capex localization can fail without demand/funding clarity."),
    Round259ShadowWeightRow(E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 3, 0, 3, 5, "Ford EV retreat hit cathode/separator/precursor names directly."),
    Round259ShadowWeightRow(E2RArchetype.SILICON_ANODE_OPTIONALITY, 3, 3, 3, 3, 4, 0, 0, 4, 5, 3, 3, -4, 4, 4, "Group14/SK is Stage 2 optionality until offtake and utilization confirm."),
    Round259ShadowWeightRow(E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION, 3, 3, 4, 4, 5, 0, 0, 5, 5, 5, 5, -4, 4, 5, "Qcells loan guarantee is Stage 2; customs/component flow can create 4C-watch."),
    Round259ShadowWeightRow(E2RArchetype.HYDROGEN_FUELCELL_CAPEX_OPTIONALITY, 2, 2, 2, 4, 5, 0, 0, 5, 5, 3, 4, -5, 4, 4, "Hyundai hydrogen plant is capex Stage 2 until offtake/utilization/margin confirm."),
    Round259ShadowWeightRow(E2RArchetype.US_FACTORY_EXECUTION_VISA_RISK, 0, 0, 0, 0, 5, 0, 0, 4, 5, 3, 5, 0, 3, 5, "Hyundai-LG Georgia raid proves U.S. factory execution risk must be a hard gate candidate."),
)

ROUND259_DEEP_SUB_ARCHETYPES: tuple[Round259DeepSubArchetype, ...] = (
    Round259DeepSubArchetype("EV battery contract quality", E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK, ("LG Energy Solution", "Ford", "Freudenberg", "lost expected revenue", "call-off failure")),
    Round259DeepSubArchetype("EV battery JV restructuring", E2RArchetype.EV_BATTERY_JV_RESTRUCTURING, ("SK On Ford JV dissolution", "Ultium Ohio restart uncertainty", "Samsung SDI Stellantis StarPlus exit", "share-sale dilution")),
    Round259DeepSubArchetype("ESS pivot", E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, ("SK On Flatiron LFP ESS", "Ultium Tennessee ESS conversion", "EV line redeployment")),
    Round259DeepSubArchetype("Battery supply-chain shock", E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK, ("POSCO Future M", "SK IE Technology", "EcoPro Materials", "cathode separator precursor demand shock")),
    Round259DeepSubArchetype("Alternative battery materials", E2RArchetype.SILICON_ANODE_OPTIONALITY, ("SK Group14", "silicon-carbon anode", "Korea BAM factory", "offtake optionality")),
    Round259DeepSubArchetype("Solar", E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH, ("Hanwha Qcells", "DOE loan guarantee", "UFLPA customs detention", "furlough")),
    Round259DeepSubArchetype("Hydrogen", E2RArchetype.HYDROGEN_FUELCELL_CAPEX_OPTIONALITY, ("Hyundai Motor Ulsan", "hydrogen fuel-cell plant", "fuel cells", "electrolyzers")),
    Round259DeepSubArchetype("Factory execution", E2RArchetype.US_FACTORY_EXECUTION_VISA_RISK, ("Hyundai-LG Georgia", "immigration raid", "visa rules", "construction delay", "restart")),
)


ROUND259_CASE_CANDIDATES: tuple[Round259CaseCandidate, ...] = (
    Round259CaseCandidate(
        case_id="r3_loop12_samsung_sdi_starplus_share_sale_4c_watch",
        symbol="006400",
        company_name="Samsung SDI",
        primary_archetype=E2RArchetype.US_BATTERY_LOCALIZATION_DILUTION,
        secondary_archetypes=(E2RArchetype.EV_BATTERY_JV_RESTRUCTURING, E2RArchetype.US_BATTERY_LOCALIZATION, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="failed_rerating",
        round_case_type="failed_rerating + dilution / JV 4C-watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 4, 9),
        stage3_date=None,
        stage4b_date=date(2025, 4, 9),
        stage4c_date=date(2026, 2, 10),
        stage3_decision="us_battery_localization_capex_is_not_green_when_share_issuance_dilution_and_customer_exit_risk_are_unresolved",
        stage4b_status="4B/4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_battery_localization_capex", "gm_jv_hungary_capacity_investment", "planned_share_issuance_2tn_krw", "share_sale_price_cut_14pct"),
        red_flag_fields=("share_issuance_for_capex", "offering_price_cut", "stock_down_29_5pct_ytd", "stellantis_starplus_exit_report_not_final", "stellantis_ev_writedown_above_26_5bn_usd"),
        price_data_source="Reuters share-sale / JV-exit report anchors",
        reported_price_anchor="Share-sale price cut from 169,200 KRW to 146,200 KRW; stock -29.5% YTD; event -1.0% vs KOSPI -0.5%",
        reported_return_anchor="2T KRW issuance for GM JV/Hungary/other battery investments; Stellantis StarPlus exit report not final",
        mfe_1d=None,
        mae_1d=-1.0,
        stage2_price_anchor=146200.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=146200.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"planned_share_issuance_krw_trn": 2.0, "new_shares": 11821000, "initial_offering_price_krw": 169200, "revised_offering_price_krw": 146200, "offering_price_cut_pct": -13.59, "reported_price_cut_pct": -14.0, "samsung_sdi_ytd_drawdown_context_pct": -29.5, "event_day_samsung_sdi_mae_pct": -1.0, "kospi_same_context_pct": -0.5, "relative_underperformance_pp": -0.5, "stellantis_writedown_context_usd_bn_min": 26.5, "starplus_exit_status": "reported_not_final"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="failed_rerating_4C_watch",
        rerating_result="unknown",
        round_rerating_label="US_battery_localization_dilution_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="policy_capex_and_jv_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="미국 현지화 CAPEX와 JV는 수요·희석·고객 이탈 리스크가 남으면 Green이 아니다.",
    ),
    Round259CaseCandidate(
        case_id="r3_loop12_lges_contract_quality_ultium_utilization_break",
        symbol="373220",
        company_name="LG Energy Solution",
        primary_archetype=E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK,
        secondary_archetypes=(E2RArchetype.EV_BATTERY_JV_RESTRUCTURING, E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="hard 4C + utilization break",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 17),
        stage3_decision="contract_headline_fails_when_ford_freudenberg_cancellations_and_ultium_restart_uncertainty_break_calloff_and_utilization",
        stage4b_status="not_applicable_hard_4C",
        hard_4c_confirmed=True,
        evidence_fields=("ford_cancelled_contract_9_6tn_krw", "freudenberg_cancelled_contract_3_9tn_krw", "total_lost_expected_revenue_13_5tn_krw", "ultium_ohio_restart_uncertain"),
        red_flag_fields=("contract_cancellation", "lost_revenue_52_7pct_of_2024_revenue", "lges_ford_event_mae_minus_7_6pct", "restart_uncertainty", "large_layoff"),
        price_data_source="Reuters cancellation / event-return / Ultium restart anchors",
        reported_price_anchor="LGES as much as -7.6% after Ford cancellation; KOSPI -1.4%",
        reported_return_anchor="Ford 9.6T KRW and Freudenberg 3.9T KRW cancelled; total lost expected revenue 13.5T KRW",
        mfe_1d=None,
        mae_1d=-7.6,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ford_cancelled_contract_krw_trn": 9.6, "ford_cancelled_contract_usd_bn": 6.5, "freudenberg_cancelled_contract_krw_trn": 3.9, "freudenberg_cancelled_contract_usd_bn": 2.7, "total_lost_expected_revenue_krw_trn": 13.5, "lges_2024_revenue_krw_trn": 25.62, "lost_revenue_vs_2024_revenue_pct": 52.7, "lges_ford_event_mae_pct": -7.6, "kospi_same_context_pct": -1.4, "relative_underperformance_pp": -6.2, "ultium_ohio_workers_laid_off_since_january": 850, "ultium_pre_idle_workforce": 1330, "indefinite_layoffs": 480, "full_restart_status": "uncertain"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="EV_battery_contract_and_utilization_break",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="계약 취소와 공장 restart uncertainty가 겹친 이번 라운드의 확정 hard 4C다.",
    ),
    Round259CaseCandidate(
        case_id="r3_loop12_skon_ford_jv_split_ess_pivot",
        symbol="096770_parent_exposure",
        company_name="SK On / SK Innovation",
        primary_archetype=E2RArchetype.EV_BATTERY_JV_RESTRUCTURING,
        secondary_archetypes=(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, E2RArchetype.ESS_LFP_GRID_STORAGE, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="success_candidate",
        round_case_type="4C-watch + success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 9, 3),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 11),
        stage3_decision="ford_jv_split_is_ev_thesis_damage_and_flatiron_ess_is_stage2_until_contract_value_utilization_opm_and_fcf_confirm",
        stage4b_status="4C-watch + ESS Stage2",
        hard_4c_confirmed=False,
        evidence_fields=("ford_sk_jv_termination", "original_jv_investment_11_4bn_usd", "flatiron_lfp_ess_up_to_7_2gwh", "supply_2026_2030", "georgia_ev_lines_to_ess"),
        red_flag_fields=("jv_dissolution", "q3_2025_op_loss_124_8bn_krw", "loss_worsening_88pct", "contract_value_not_disclosed", "ess_margin_unconfirmed"),
        price_data_source="Reuters JV termination / ESS contract anchors",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="$11.4B Ford/SK JV split; Flatiron ESS up to 7.2GWh, 2026-2030",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"original_ford_sk_jv_investment_usd_bn": 11.4, "asset_split": "Ford takes Kentucky plants; SK On takes Tennessee plant", "sk_on_q3_2025_op_loss_krw_bn": 124.8, "previous_quarter_op_loss_krw_bn": 66.4, "loss_worsening_pct": 88.0, "flatiron_ess_contract_volume_gwh": 7.2, "flatiron_supply_period": "2026-2030", "contract_value": "not_disclosed", "production_start": "2H_2026_target", "capacity_redeployment": "some Georgia EV lines to ESS"},
        score_price_alignment="unknown",
        round_alignment_label="4C_watch_plus_success_candidate",
        rerating_result="unknown",
        round_rerating_label="EV_JV_break_then_ESS_pivot_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_pivot_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Ford JV split은 EV 논리 훼손이고, Flatiron ESS는 계약금액·가동률·마진·FCF 전 Stage 2다.",
    ),
    Round259CaseCandidate(
        case_id="r3_loop12_battery_supply_chain_ford_demand_shock",
        symbol="003670/361610/450080/096770/373220/006400",
        company_name="POSCO Future M / SK IE Technology / EcoPro Materials / battery supply-chain basket",
        primary_archetype=E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK,
        secondary_archetypes=(E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="failed_rerating",
        round_case_type="4C-watch supply-chain demand shock",
        stage1_date=date(2025, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 16),
        stage3_decision="ford_ev_retreat_transmits_to_cathode_separator_precursor_names_and_blocks_battery_supply_chain_green",
        stage4b_status="not_applicable_4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("ford_ev_model_cuts", "lower_battery_content_hybrid_shift", "posco_future_m_minus_8_2pct", "sk_iet_minus_5pct", "ecopro_materials_minus_5pct"),
        red_flag_fields=("ev_demand_shock", "customer_ev_model_cancellation", "battery_supply_chain_drawdown", "cathode_separator_precursor_demand_risk"),
        price_data_source="Reuters / MarketWatch battery supply-chain shock anchors",
        reported_price_anchor="LGES -6.0%, Samsung SDI -3.5%, POSCO Future M -8.2%, SKIET -5.0%, EcoPro Materials -5.0%",
        reported_return_anchor="Ford EV model cuts / lower-battery-content hybrid shift",
        mfe_1d=None,
        mae_1d=-8.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"lges_event_mae_pct": -6.0, "samsung_sdi_event_mae_pct": -3.5, "posco_future_m_event_mae_pct": -8.2, "sk_innovation_event_mae_pct": -3.0, "sk_ie_technology_event_mae_pct": -5.0, "ecopro_materials_event_mae_pct": -5.0, "posco_future_m_relative_vs_lges_pp": -2.2, "ford_policy": "EV model cuts / lower-battery-content hybrid shift"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="battery_material_separator_precursor_demand_shock",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="셀 업체보다 소재·분리막·전구체가 고객 EV 전략 변화에 더 민감하게 빠질 수 있다.",
    ),
    Round259CaseCandidate(
        case_id="r3_loop12_sk_group14_silicon_anode_optional",
        symbol="034730_exposure",
        company_name="SK / Group14 Technologies",
        primary_archetype=E2RArchetype.SILICON_ANODE_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.SILICON_ANODE_COMMERCIALIZATION, E2RArchetype.STAGE2_EVIDENCE_NOT_GREEN),
        case_type="success_candidate",
        round_case_type="success_candidate silicon-anode optionality",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 8, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="silicon_anode_funding_and_factory_control_are_stage2_until_customer_offtake_utilization_margin_and_equity_value_confirm",
        stage4b_status="4B-watch-if-silicon-anode-theme-rallies",
        hard_4c_confirmed=False,
        evidence_fields=("group14_series_d_463mn_usd", "sk_lead_investor", "total_equity_raised_above_1bn_usd", "group14_acquires_remaining_75pct_jv", "korea_bam_factory_control"),
        red_flag_fields=("offtake_unconfirmed", "utilization_unconfirmed", "margin_unconfirmed", "equity_method_value_unconfirmed"),
        price_data_source="Reuters Group14 financing / JV control anchor",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="Group14 raised $463M led by SK and acquired remaining 75% of JV; Korea BAM factory control",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"series_d_funding_usd_mn": 463.0, "lead_investor": "SK", "total_equity_raised_usd_bn_min": 1.0, "jv_stake_acquired_by_group14_pct": 75.0, "korea_bam_factory": "fully controlled by Group14 after transaction", "material": "SCC55 silicon-carbon composite", "valuation": "higher than >$1B 2022 round; exact value not disclosed"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="silicon_anode_optional_materials_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="investment_optional_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="투자와 소재 optionality는 Stage 2다. 고객 offtake·가동률·마진·SK 지분가치 전 Green이 아니다.",
    ),
    Round259CaseCandidate(
        case_id="r3_loop12_hanwha_qcells_solar_uflpa_4c_watch",
        symbol="009830/000880_exposure",
        company_name="Hanwha Qcells / Hanwha Solutions exposure",
        primary_archetype=E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION,
        secondary_archetypes=(E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="success_candidate",
        round_case_type="success_candidate + customs 4C-watch",
        stage1_date=date(2024, 8, 8),
        stage2_date=date(2024, 8, 8),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 11, 8),
        stage3_decision="doe_loan_and_us_solar_localization_are_stage2_but_component_flow_utilization_margin_and_fcf_required",
        stage4b_status="4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("doe_conditional_loan_guarantee_1_45bn_usd", "cartersville_facility_investment_2_5bn_usd", "panels_cells_ingots_wafers_scope", "nearly_2000_jobs_when_operational"),
        red_flag_fields=("uflpa_customs_detention", "component_flow_failure", "about_1000_furloughed_or_reduced_hours", "300_contract_workers_cut", "production_curtailment"),
        price_data_source="Reuters Qcells DOE loan / customs disruption anchors",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="$1.45B conditional DOE guarantee and $2.5B plant; about 1,000 furloughs and 300 contract-worker cuts",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"doe_conditional_loan_guarantee_usd_bn": 1.45, "cartersville_facility_investment_usd_bn": 2.5, "facility_scope": "solar panels|cells|ingots|wafers", "jobs_when_fully_operational": 2000, "furloughed_or_reduced_hours_workers": 1000, "contract_workers_cut": 300, "affected_direct_workers_total": 1300, "cause": "U.S. customs detentions under forced-labor import law / UFLPA context"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="success_candidate_plus_4C_watch",
        rerating_result="unknown",
        round_rerating_label="solar_localization_with_supply_chain_break_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="localization_not_green_until_component_flow_margin_FCF",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="DOE loan과 현지화는 Stage 2다. component flow와 utilization이 막히면 4C-watch다.",
    ),
    Round259CaseCandidate(
        case_id="r3_loop12_hyundai_hydrogen_fuelcell_capex",
        symbol="005380",
        company_name="Hyundai Motor hydrogen fuel-cell plant",
        primary_archetype=E2RArchetype.HYDROGEN_FUELCELL_CAPEX_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX, E2RArchetype.GREEN_MOBILITY_INFRASTRUCTURE, E2RArchetype.STAGE2_EVIDENCE_NOT_GREEN),
        case_type="success_candidate",
        round_case_type="success_candidate / capex optionality",
        stage1_date=date(2025, 10, 30),
        stage2_date=date(2025, 10, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="hydrogen_fuelcell_capex_is_stage2_until_offtake_utilization_hydrogen_economics_margin_and_fcf_confirm",
        stage4b_status="4B-watch-if-hydrogen-theme-rallies",
        hard_4c_confirmed=False,
        evidence_fields=("ulsan_hydrogen_fuel_cell_facility", "investment_930bn_krw", "facility_area_43000_sqm", "completion_target_2027", "fuel_cells_and_electrolyzers"),
        red_flag_fields=("hydrogen_capex_without_offtake", "utilization_unconfirmed", "hydrogen_economics_unconfirmed", "margin_fcf_unconfirmed"),
        price_data_source="Reuters hydrogen fuel-cell plant anchor",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="930B KRW / $654M plant, 43,000m², completion 2027",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"investment_krw_bn": 930.0, "investment_usd_mn": 654.0, "facility_area_sqm": 43000, "completion_target_year": 2027, "products": "fuel cells|electrolyzers", "applications": "passenger cars|commercial trucks|buses|construction equipment|marine vessels"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="hydrogen_fuelcell_capex_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="capex_not_green_until_offtake_utilization_margin",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="수소 fuel-cell CAPEX는 Stage 2다. offtake·가동률·수소경제성·마진·FCF 전 Green이 아니다.",
    ),
    Round259CaseCandidate(
        case_id="r3_loop12_hyundai_lg_georgia_factory_visa_execution_watch",
        symbol="005380/373220",
        company_name="Hyundai-LG Georgia battery plant / HL-GA Battery",
        primary_archetype=E2RArchetype.US_FACTORY_EXECUTION_VISA_RISK,
        secondary_archetypes=(E2RArchetype.EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK, E2RArchetype.US_BATTERY_LOCALIZATION, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="failed_rerating",
        round_case_type="4C-watch factory execution / visa risk",
        stage1_date=date(2025, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="us_battery_factory_localization_needs_visa_skilled_worker_subcontractor_compliance_startup_and_utilization_before_green",
        stage4b_status="4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("hyundai_lg_georgia_battery_site", "hl_ga_battery_production_target_h1_2026", "some_workers_returned_and_construction_resumed"),
        red_flag_fields=("visa_raid", "detained_workers_about_475", "over_300_korean_workers_detained", "startup_delay_2_to_3_months", "skilled_worker_bottleneck"),
        price_data_source="Reuters / AP factory execution and visa-risk anchors",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="About 475 detained in Reuters context; over 300 Korean workers in AP context; 2-3 month startup delay; construction later resumed",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage4c_month": "2025-09", "detained_workers_reuters_context": 475, "detained_korean_workers_ap_context": 300, "startup_delay_months": "2-3", "project": "Hyundai-LG Georgia battery plant / HL-GA Battery", "relief": "some workers returned and construction resumed", "production_target": "H1_2026", "local_hiring": "ongoing"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="US_battery_factory_execution_visa_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch_not_hard_4C",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="공장과 자본만으로 부족하다. visa와 숙련 인력 execution이 막히면 startup이 지연된다.",
    ),
)


def round259_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("calloff", "take", "delivery", "utilization", "opm", "margin", "fcf", "revenue", "offtake")
    for candidate in ROUND259_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND259_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round259 R3 Loop-12 battery/EV/green price-validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "rally" in field.lower() or "valuation" in field.lower() or "price" in field.lower()),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "cancellation" in field.lower()
                or "exit" in field.lower()
                or "dissolution" in field.lower()
                or "shock" in field.lower()
                or "detention" in field.lower()
                or "delay" in field.lower()
                or "layoff" in field.lower()
                or "raid" in field.lower()
                or "dilution" in field.lower()
                or "furlough" in field.lower()
            ),
            must_have_fields=ROUND259_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "4c_thesis_break", "event_premium", "overheat", "4b_watch"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND259_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_ev_jv_ess_hydrogen_solar_silicon_or_localization_as_green_alone",
                *ROUND259_GREEN_REQUIRED_FIELDS,
                *ROUND259_GREEN_FORBIDDEN_PATTERNS,
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
                price_data_available=candidate.mfe_1d is not None
                or candidate.mae_1d is not None
                or candidate.stage2_price_anchor is not None,
                stage_dates_confidence=0.9 if candidate.hard_4c_confirmed else 0.75,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round259_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND259_CASE_CANDIDATES:
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


def round259_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND259_SCORE_ADJUSTMENTS)


def round259_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND259_SHADOW_WEIGHT_ROWS)


def round259_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND259_DEEP_SUB_ARCHETYPES)


def round259_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round259_price_validation": "true"} for field in ROUND259_PRICE_VALIDATION_FIELDS)


def round259_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round259_label": label, "canonical_archetype": canonical} for label, canonical in ROUND259_REQUIRED_TARGET_ALIASES.items())


def round259_summary() -> dict[str, int | bool | str]:
    cases = ROUND259_CASE_CANDIDATES
    return {
        "source_round": ROUND259_SOURCE_ROUND_PATH,
        "round_id": ROUND259_ROUND_ID,
        "large_sector": ROUND259_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "thesis_break_case_count": sum(1 for case in cases if case.case_type == "4c_thesis_break"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status or case.stage4b_date is not None),
        "watch_4c_or_hard_count": sum(1 for case in cases if "4C" in case.stage4b_status or case.stage4c_date is not None or case.hard_4c_confirmed),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "price_data_unavailable_count": sum(1 for case in cases if case.price_validation_status == "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND259_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND259_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND259_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round259_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND259_SOURCE_ROUND_PATH,
        "round_id": ROUND259_ROUND_ID,
        "large_sector": ROUND259_LARGE_SECTOR,
        "summary": round259_summary(),
        "target_aliases": dict(ROUND259_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND259_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND259_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND259_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND259_HARD_4C_GATES),
        "deep_sub_archetypes": round259_deep_sub_archetype_rows(),
        "shadow_weights": round259_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round259_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_ev_jv_ess_hydrogen_solar_silicon_or_localization_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "do_not_confirm_hard_4c_except_lges_contract_quality_break_in_this_round",
        ],
    }


def render_round259_summary_markdown() -> str:
    summary = round259_summary()
    lines = [
        "# Round 259 R3 Loop 12 Battery / EV / Green Price Validation",
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
        f"- thesis_break_cases: {summary['thesis_break_case_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- 4C-watch or hard cases: {summary['watch_4c_or_hard_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | stage2 | stage3 | 4B | 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND259_CASE_CANDIDATES:
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
            "- R3 Stage 3 is not `EV, ESS, hydrogen, solar, or localization is good`. It needs call-off, GWh, delivery, utilization, OPM, FCF, and cleared execution risks.",
            "- LGES Ford/Freudenberg is the confirmed hard 4C in this round because expected revenue and utilization visibility broke.",
            "- Samsung SDI, SK On/Ford, Qcells, and Hyundai-LG Georgia are 4C-watch cases, not forced hard 4C unless customer exit, license, restart, or revenue impairment is confirmed.",
            "- SK/Group14 and Hyundai hydrogen are Stage 2 optionality cases. They need offtake, utilization, margin, and FCF before Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round259_green_gate_review_markdown() -> str:
    lines = [
        "# Round 259 R3 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R3 Stage 3-Green requires the contract or plant story to close into actual call-off, GWh, delivery, utilization, OPM, FCF, and cleared customs/visa/labor risks.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND259_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND259_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `LGES Ford/Freudenberg cancellation` is hard 4C because expected revenue disappears.",
            "- `SK On Flatiron ESS 7.2GWh` is Stage 2 until contract value, utilization, OPM and FCF are known.",
            "- `Qcells DOE loan guarantee` is not Green if customs detention cuts production flow.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round259_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 259 R3 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND259_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND259_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B catches EV/ESS/hydrogen/solar stories that price before utilization, OPM, or FCF.",
            "- 4C-watch catches customer exits, JV stress, customs detention, visa raids, and factory startup delays before they are fully quantified.",
            "- This loop confirms LGES Ford/Freudenberg as hard 4C. Other risks remain 4C-watch unless the revenue, license, restart, or production impairment is confirmed.",
            "",
            "## Case Notes",
            "",
        ]
    )
    for case in ROUND259_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or "4C" in case.stage4b_status or case.stage4c_date or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round259_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 259 R3 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "- Month-only risk events, such as the Hyundai-LG Georgia raid, are stored as metadata rather than fabricated exact dates.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND259_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round259_r3_loop12_reports(
    output_directory: str | Path = ROUND259_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND259_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND259_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round259_case_records(), cases_path),
        "audit": _write_json(round259_audit_payload(), audit_path),
        "summary": output / "round259_r3_loop12_price_validation_summary.md",
        "case_matrix": output / "round259_r3_loop12_case_matrix.csv",
        "target_aliases": output / "round259_r3_loop12_target_aliases.csv",
        "score_adjustments": output / "round259_r3_loop12_score_adjustments.csv",
        "shadow_weights": output / "round259_r3_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round259_r3_loop12_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round259_r3_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round259_r3_loop12_green_gate_review.md",
        "price_validation_plan": output / "round259_r3_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round259_r3_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round259_summary_markdown(), encoding="utf-8")
    _write_csv(round259_case_rows(), paths["case_matrix"])
    _write_csv(round259_target_alias_rows(), paths["target_aliases"])
    _write_csv(round259_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round259_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round259_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round259_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round259_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round259_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round259_stage4b_4c_review_markdown(), encoding="utf-8")
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
