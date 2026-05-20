"""Round-233 R3 Loop-10 battery/EV/green price validation pack.

This pack converts ``docs/round/round_233.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: a 5GWh ESS contract is good Stage 2 evidence, but it is not
Stage 3-Green until actual call-off, utilization, OPM, FCF, and price-path
confirmation are visible. R3 is where false Green is especially dangerous.
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


ROUND233_SOURCE_ROUND_PATH = "docs/round/round_233.md"
ROUND233_LARGE_SECTOR = "BATTERY_EV_GREEN"
ROUND233_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round233_r3_loop10_battery_ev_green_price_validation"
ROUND233_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop10_round233.jsonl"
ROUND233_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round233_r3_loop10_battery_ev_green_price_validation_audit.json"

ROUND233_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "ESS_LFP_GRID_STORAGE": E2RArchetype.ESS_LFP_GRID_STORAGE.value,
    "EV_TO_ESS_CAPACITY_REDEPLOYMENT": E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT.value,
    "EV_BATTERY_JV_RESTRUCTURING": E2RArchetype.EV_BATTERY_JV_RESTRUCTURING.value,
    "EV_BATTERY_FACTORY_UTILIZATION_4C": E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT.value,
    "BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE": E2RArchetype.BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE.value,
    "CATHODE_SUPPLY_CHAIN_DERISKING": E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY.value,
    "BATTERY_MATERIALS_CYCLE_OVERLAY": E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT.value,
    "LITHIUM_CYCLE_EVENT_PREMIUM": E2RArchetype.EVENT_LITHIUM_PRICE_RALLY.value,
    "SOLAR_US_SUPPLY_CHAIN_LOCALIZATION": E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION.value,
    "SOLAR_CUSTOMS_UFLPA_4C_WATCH": E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH.value,
    "HYDROGEN_FUEL_CELL_CAPEX": E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
}

ROUND233_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "binding_contract",
    "actual_calloff",
    "gwh_or_tonnage_volume",
    "utilization_improvement",
    "opm_or_gross_margin_improvement",
    "fcf_after_capex",
    "subsidy_excluded_profit_quality",
    "customer_ev_strategy_risk_passed",
    "supply_chain_disruption_risk_passed",
    "price_path_after_evidence",
)

ROUND233_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "customer_name_only",
    "factory_groundbreaking_only",
    "jv_restructuring_only",
    "ess_lfp_theme_only",
    "capacity_conversion_only",
    "lithium_price_event_only",
    "ampc_or_subsidy_quality_loss",
    "ev_demand_slowdown_ignored",
)

ROUND233_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "ess_lfp_contract_headline_rally",
    "ev_line_conversion_headline_multiple_expansion",
    "lithium_price_event_materials_basket_rally",
    "hydrogen_capex_theme_rally",
    "us_localization_prices_before_utilization",
    "battery_factory_ownership_prices_before_utilization",
)

ROUND233_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "contract_value_collapse",
    "customer_ev_model_cancellation",
    "customer_strategy_pullback",
    "gwh_calloff_failure",
    "utilization_delay",
    "factory_restart_uncertainty",
    "negative_fcf",
    "debt_burden_or_emergency_restructuring",
    "jv_termination_or_weak_demand_transfer",
    "subsidy_quality_profit_collapse",
    "share_issuance_or_dilution_under_weak_demand",
    "supply_chain_customs_detention",
    "production_furlough",
)

ROUND233_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "gwh_or_capacity_anchor",
    "factory_or_capex_anchor",
    "utilization_or_layoff_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round233ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round233ShadowWeightRow:
    archetype: E2RArchetype
    actual_calloff: int
    gwh_volume: int
    ess_revenue_conversion: int
    utilization: int
    opm_fcf: int
    customer_quality: int
    supply_chain_derisking: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "actual_calloff": _signed(self.actual_calloff),
            "gwh_volume": _signed(self.gwh_volume),
            "ess_revenue_conversion": _signed(self.ess_revenue_conversion),
            "utilization": _signed(self.utilization),
            "opm_fcf": _signed(self.opm_fcf),
            "customer_quality": _signed(self.customer_quality),
            "supply_chain_derisking": _signed(self.supply_chain_derisking),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round233DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round233CaseCandidate:
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


ROUND233_SCORE_ADJUSTMENTS: tuple[Round233ScoreAdjustment, ...] = (
    Round233ScoreAdjustment("actual_calloff", 5, "raise", "계약은 실제 call-off가 확인될 때 강해진다."),
    Round233ScoreAdjustment("gwh_volume", 5, "raise", "ESS/배터리는 GWh volume이 핵심 visibility다."),
    Round233ScoreAdjustment("ess_revenue_conversion", 5, "raise", "ESS 전환은 매출 전환 전 Stage 2다."),
    Round233ScoreAdjustment("utilization_rate", 5, "raise", "공장 ownership보다 가동률이 중요하다."),
    Round233ScoreAdjustment("opm_visibility", 5, "raise", "OPM/gross margin 확인 전 Green 금지다."),
    Round233ScoreAdjustment("fcf_after_capex", 5, "raise", "CAPEX 이후 FCF가 남아야 구조적이다."),
    Round233ScoreAdjustment("customer_quality", 4, "raise", "Hanwha QCells, Flatiron, GM 등 고객 품질은 Stage 2 증거다."),
    Round233ScoreAdjustment("supply_chain_derisking", 4, "raise", "중국 노출 축소와 현지화는 visibility를 보강한다."),
    Round233ScoreAdjustment("localization_with_real_utilization", 4, "raise", "현지화는 utilization이 동반될 때만 강하다."),
    Round233ScoreAdjustment("ev_capacity_announcement_only", -5, "lower", "EV CAPA 발표만으로 Green 금지다."),
    Round233ScoreAdjustment("ess_theme_only", -4, "lower", "ESS 테마만으로는 매출/OPM/FCF가 아니다."),
    Round233ScoreAdjustment("jv_restructuring_relief_only", -4, "lower", "JV 재편은 수요 부진을 숨길 수 있다."),
    Round233ScoreAdjustment("factory_ownership_without_utilization", -4, "lower", "공장 소유보다 가동률이 중요하다."),
    Round233ScoreAdjustment("customer_name_without_calloff", -5, "lower", "고객명만 있고 call-off가 없으면 Green 금지다."),
    Round233ScoreAdjustment("lithium_price_event", -5, "lower", "리튬 가격 이벤트는 commodity event premium이다."),
    Round233ScoreAdjustment("subsidy_dependent_profit", -5, "lower", "보조금 제외 이익 품질이 약하면 감점한다."),
    Round233ScoreAdjustment("negative_fcf_or_debt_burden", -5, "lower", "CAPEX 뒤 FCF/부채 부담은 RedTeam이다."),
    Round233ScoreAdjustment("supply_chain_customs_disruption", -5, "lower", "UFLPA/customs disruption은 4C-watch다."),
    Round233ScoreAdjustment("ev_demand_shock", -5, "lower", "고객 EV 전략 후퇴는 R3의 핵심 4C-watch다."),
)


ROUND233_SHADOW_WEIGHT_ROWS: tuple[Round233ShadowWeightRow, ...] = (
    Round233ShadowWeightRow(E2RArchetype.ESS_LFP_GRID_STORAGE, 5, 5, 5, 5, 5, 4, 3, -2, 4, 4, "LGES/SK On ESS contracts are Stage 2; revenue/utilization/OPM/FCF required."),
    Round233ShadowWeightRow(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, 4, 5, 5, 5, 5, 3, 3, -3, 4, 5, "EV line conversion is positive only if utilization and ESS margins confirm."),
    Round233ShadowWeightRow(E2RArchetype.EV_BATTERY_JV_RESTRUCTURING, 4, 5, 3, 5, 5, 4, 3, -4, 4, 4, "Samsung SDI/GM JV is Stage 2; demand delay and utilization risk remain."),
    Round233ShadowWeightRow(E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY, 4, 4, 2, 5, 5, 4, 5, -2, 3, 4, "LG Chem/Toyota reduces China exposure but needs offtake and margin."),
    Round233ShadowWeightRow(E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION, 3, 3, 2, 5, 5, 4, 5, -3, 4, 5, "Qcells localization is Stage 2; customs/component disruption is 4C-watch."),
    Round233ShadowWeightRow(E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE, 3, 4, 2, 5, 5, 4, 3, -5, 4, 5, "Ford EV retreat shows EV demand shock for separator/precursor names."),
    Round233ShadowWeightRow(E2RArchetype.EVENT_LITHIUM_PRICE_RALLY, 1, 1, 0, 2, 3, 1, 2, -5, 5, 4, "Lithium price rally is event premium unless call-off/OPM/FCF confirm."),
    Round233ShadowWeightRow(E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX, 2, 2, 1, 5, 5, 3, 3, -4, 4, 4, "Hydrogen plant capex is Stage 2 until order/utilization/margin/FCF confirm."),
)


ROUND233_DEEP_SUB_ARCHETYPES: tuple[Round233DeepSubArchetype, ...] = (
    Round233DeepSubArchetype("ESS transition", E2RArchetype.ESS_LFP_GRID_STORAGE, ("LG Energy Solution", "SK On", "LFP ESS", "EV line conversion", "grid storage demand")),
    Round233DeepSubArchetype("EV-to-ESS redeployment", E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, ("NextStar", "Ohio Ultium", "Tennessee ESS cells", "factory restart uncertainty", "layoffs")),
    Round233DeepSubArchetype("EV battery JV", E2RArchetype.EV_BATTERY_JV_RESTRUCTURING, ("Samsung SDI", "GM Indiana", "27GWh", "36GWh", "EV demand delay")),
    Round233DeepSubArchetype("Cathode derisking", E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY, ("LG Chem", "Toyota Tsusho", "Huayou stake reduction", "China exposure reduction")),
    Round233DeepSubArchetype("Solar localization 4C", E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH, ("Hanwha Qcells", "UFLPA", "customs detention", "Georgia furloughs")),
    Round233DeepSubArchetype("EV demand shock", E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE, ("SKIET", "EcoPro Materials", "Ford EV retreat", "hybrid pivot")),
    Round233DeepSubArchetype("Lithium event premium", E2RArchetype.EVENT_LITHIUM_PRICE_RALLY, ("CATL Yichun", "lithium futures", "POSCO Future M", "L&F", "not structural")),
    Round233DeepSubArchetype("Hydrogen capex", E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX, ("Hyundai", "Ulsan hydrogen fuel-cell plant", "2027 completion", "utilization required")),
)


ROUND233_CASE_CANDIDATES: tuple[Round233CaseCandidate, ...] = (
    Round233CaseCandidate(
        case_id="r3_loop10_lges_ess_pivot_ev_utilization_watch",
        symbol="373220",
        company_name="LG Energy Solution",
        primary_archetype=E2RArchetype.ESS_LFP_GRID_STORAGE,
        secondary_archetypes=(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, E2RArchetype.EV_BATTERY_JV_RESTRUCTURING),
        case_type="success_candidate",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 2, 4),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 12),
        stage3_decision="ess_contract_and_nextstar_restructuring_are_stage2_but_revenue_utilization_opm_fcf_required",
        stage4b_status="4B-watch-if_ess_pivot_multiple_prepays_utilization",
        hard_4c_confirmed=False,
        evidence_fields=("hanwha_qcells_ess_contract_5gwh", "lfp_cells", "supply_2028_2030", "nextstar_49pct_stake_for_100_usd", "tennessee_ess_redeployment"),
        red_flag_fields=("ohio_ultium_restart_uncertain", "ohio_layoffs_850_workers", "ev_factory_utilization_risk", "ess_margin_unconfirmed"),
        price_data_source="Reuters ESS/JV/restart anchors",
        reported_price_anchor="No reliable OHLC anchor from Reuters for LGES case row",
        reported_return_anchor="5GWh ESS contract; NextStar 49% stake for $100; Ohio 850 layoffs",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"hanwha_qcells_ess_contract_gwh": 5.0, "supply_period": "2028-2030", "cell_chemistry": "LFP", "production_site": "Holland_Michigan", "nextstar_stake_acquired_pct": 49.0, "nextstar_purchase_price_usd": 100.0, "nextstar_investment_to_date_cad_bn_min": 5.0, "nextstar_investment_to_date_usd_bn": 3.65, "ohio_ultium_layoffs_since_january": 850.0, "ohio_prior_employee_context": 1330.0, "indefinite_layoff_context": 480.0, "ess_redeployment": "Tennessee plant workers recalled to produce ESS cells"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="unknown",
        round_rerating_label="ESS_pivot_watch_with_EV_utilization_risk",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="ESS pivot is Stage 2; EV plant restart uncertainty and utilization risk require 4C-watch.",
    ),
    Round233CaseCandidate(
        case_id="r3_loop10_skon_flatiron_lfp_ess_order",
        symbol="096770",
        company_name="SK Innovation / SK On",
        primary_archetype=E2RArchetype.ESS_LFP_GRID_STORAGE,
        secondary_archetypes=(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT,),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 9, 3),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="first_lfp_ess_order_is_stage2_until_contract_value_utilization_opm_and_fcf_confirm",
        stage4b_status="4B-watch-if_ess_pivot_headline_rallies_without_margin",
        hard_4c_confirmed=False,
        evidence_fields=("flatiron_ess_contract_up_to_7_2gwh", "supply_2026_2030", "first_sk_on_lfp_ess_order", "georgia_ev_lines_partly_converted"),
        red_flag_fields=("contract_value_not_disclosed", "utilization_unconfirmed", "loss_persistence_risk", "ev_order_slowdown_risk"),
        price_data_source="Reuters ESS contract anchor",
        reported_price_anchor="Reuters did not provide stock reaction anchor",
        reported_return_anchor="Flatiron ESS up to 7.2GWh, 2026-2030, first SK On LFP ESS order",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"flatiron_ess_contract_gwh": 7.2, "supply_period": "2026-2030", "chemistry": "LFP", "first_sk_on_lfp_ess_order": True, "production_start": "2H_2026", "capacity_redeployment": "some Georgia EV battery lines converted for ESS use", "contract_value": "not_disclosed"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="SK_On_ESS_pivot_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="First LFP ESS order is Stage 2; contract value, utilization, OPM and FCF required before Green.",
    ),
    Round233CaseCandidate(
        case_id="r3_loop10_samsung_sdi_gm_indiana_ev_jv",
        symbol="006400",
        company_name="Samsung SDI",
        primary_archetype=E2RArchetype.EV_BATTERY_JV_RESTRUCTURING,
        secondary_archetypes=(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT,),
        case_type="success_candidate",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 8, 28),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="gm_jv_localization_is_stage2_but_ev_demand_cut_2027_timing_utilization_margin_fcf_block_green",
        stage4b_status="4B-watch-if_us_localization_prices_before_utilization",
        hard_4c_confirmed=False,
        evidence_fields=("gm_samsung_sdi_indiana_jv", "investment_3_5bn_usd", "initial_capacity_27gwh", "potential_capacity_36gwh", "mass_production_2027"),
        red_flag_fields=("gm_ev_forecast_cut_16_7pct", "production_start_delayed_to_2027", "utilization_unconfirmed", "cell_margin_unconfirmed"),
        price_data_source="Reuters JV and event-return anchors",
        reported_price_anchor="Samsung SDI +3.2%; KOSPI -0.3%",
        reported_return_anchor="Relative +3.5pp; GM EV forecast upper end cut from 300k to 250k",
        mfe_1d=3.2,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"jv_investment_usd_bn": 3.5, "initial_capacity_gwh": 27.0, "potential_capacity_gwh": 36.0, "capacity_expansion_potential_pct": 33.3, "mass_production_target_year": 2027.0, "event_mfe_pct": 3.2, "kospi_same_context_pct": -0.3, "relative_outperformance_pp": 3.5, "gm_ev_forecast_upper_before_units": 300000.0, "gm_ev_forecast_upper_after_units": 250000.0, "forecast_cut_pct": -16.7},
        score_price_alignment="aligned",
        round_alignment_label="success_candidate_demand_watch",
        rerating_result="unknown",
        round_rerating_label="EV_battery_localization_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="JV localization is Stage 2; GM demand cut and 2027 production timing block Green until utilization/margin/FCF confirm.",
    ),
    Round233CaseCandidate(
        case_id="r3_loop10_lg_chem_toyota_cathode_derisking",
        symbol="051910",
        company_name="LG Chem",
        primary_archetype=E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY,
        secondary_archetypes=(E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,),
        case_type="success_candidate",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 9, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="ownership_derisking_is_stage2_until_cathode_volume_customer_offtake_opm_and_fcf_confirm",
        stage4b_status="4B-watch-if_china_derisking_narrative_prices_before_offtake",
        hard_4c_confirmed=False,
        evidence_fields=("toyota_tsusho_25pct_stake", "huayou_stake_reduced_49_to_24pct", "china_exposure_reduction", "cathode_localization"),
        red_flag_fields=("cathode_volume_unconfirmed", "customer_offtake_unconfirmed", "opm_fcf_unconfirmed", "lithium_nickel_price_reversal_risk"),
        price_data_source="Reuters ownership-structure anchor",
        reported_price_anchor="Reuters did not provide stock reaction anchor",
        reported_return_anchor="Toyota Tsusho 25%; Huayou stake 49% to 24%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
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
    Round233CaseCandidate(
        case_id="r3_loop10_hanwha_qcells_uflpa_supply_chain_watch",
        symbol="009830",
        company_name="Hanwha Solutions / Qcells",
        primary_archetype=E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION,
        secondary_archetypes=(E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH,),
        case_type="success_candidate",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2025, 1, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 11, 1),
        stage3_decision="us_solar_localization_is_stage2_but_customs_component_disruption_and_furloughs_create_4c_watch",
        stage4b_status="4B-watch-if_localization_prices_before_component_flow_utilization_margin",
        hard_4c_confirmed=False,
        evidence_fields=("qcells_us_supply_chain_investment", "cartersville_facility_2_3bn_usd", "georgia_full_solar_supply_chain", "ira_tariff_protection_expectation"),
        red_flag_fields=("uflpa_customs_component_detention", "reduced_pay_hours_1000_workers", "contract_workers_laid_off_300", "component_supply_risk"),
        price_data_source="AP supply-chain disruption anchor",
        reported_price_anchor="AP did not provide stock reaction anchor",
        reported_return_anchor="About 1,000 workers reduced pay/hours, 300 contract workers cut, $2.3B facility",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"qcells_georgia_employee_context": 3000.0, "furlough_or_reduced_pay_hours_workers": 1000.0, "contract_workers_laid_off": 300.0, "affected_direct_workers_total": 1300.0, "affected_share_employee_context_pct": 33.3, "cartersville_facility_investment_usd_bn": 2.3, "cause": "U.S. Customs component detentions under forced-labor import law"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="solar_localization_watch_with_supply_chain_risk",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_with_4C_watch",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Solar localization is Stage 2; UFLPA/customs disruption and furloughs create 4C-watch.",
    ),
    Round233CaseCandidate(
        case_id="r3_loop10_ev_supply_chain_ford_shock_skiet_ecopro",
        symbol="361610/450080",
        company_name="SK IE Technology / EcoPro Materials / battery supply-chain basket",
        primary_archetype=E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE,
        secondary_archetypes=(E2RArchetype.PRECURSOR_SUPPLY_CHAIN_SHOCK, E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT),
        case_type="4c_thesis_break",
        stage1_date=date(2023, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 1),
        stage3_decision="ford_ev_retreat_and_hybrid_pivot_create_battery_supply_chain_4c_watch_until_utilization_demand_recover",
        stage4b_status="4C-watch-not-hard-4C",
        hard_4c_confirmed=False,
        evidence_fields=("ford_20bn_charge", "ford_ev_strategy_pullback", "hybrid_pivot", "korean_battery_supply_chain_drawdown"),
        red_flag_fields=("ev_demand_shock", "customer_strategy_pullback", "skiet_mae_minus_5pct", "ecopro_materials_mae_minus_5pct"),
        price_data_source="MarketWatch event-return anchors",
        reported_price_anchor="SK Innovation -3%, LGES -6%, SKIET -5%, EcoPro Materials -5%",
        reported_return_anchor="Ford about $20B charge, battery supply-chain names down 3-6%",
        mfe_1d=None,
        mae_1d=-6.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"ford_charge_usd_bn": 20.0, "sk_innovation_event_mae_pct": -3.0, "lges_event_mae_pct": -6.0, "sk_ie_technology_event_mae_pct": -5.0, "ecopro_materials_event_mae_pct": -5.0, "quantumscape_premarket_mae_pct": -2.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="EV_supply_chain_demand_shock",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="should_have_been_red_or_watch",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="Ford EV retreat and hybrid pivot hit Korean battery supply chain; separator/precursor Green requires utilization and demand confirmation.",
    ),
    Round233CaseCandidate(
        case_id="r3_loop10_posco_future_m_lnf_lithium_event",
        symbol="003670/066970",
        company_name="POSCO Future M / L&F",
        primary_archetype=E2RArchetype.EVENT_LITHIUM_PRICE_RALLY,
        secondary_archetypes=(E2RArchetype.LITHIUM_CYCLE_OVERLAY, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        stage1_date=date(2025, 8, 11),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 8, 11),
        stage4c_date=None,
        stage3_decision="lithium_price_rally_is_commodity_event_premium_without_company_calloff_opm_fcf_and_inventory_quality",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("catl_yichun_mine_license_expiry", "lithium_carbonate_futures_plus_8pct", "posco_future_m_plus_8_3pct", "lnf_plus_10pct"),
        red_flag_fields=("lithium_price_event_only", "catl_resume_if_license_renewed", "price_decline_from_2022_peak_90pct", "inventory_valuation_reversal_risk"),
        price_data_source="Reuters / WSJ commodity and event-return anchors",
        reported_price_anchor="POSCO Future M +8.3%, L&F +10.0%, Samsung SDI +3.2%, LGES +2.8%",
        reported_return_anchor="Lithium carbonate futures +8%; lithium price down up to -90% from 2022 peak",
        mfe_1d=10.0,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"lithium_carbonate_futures_event_return_pct": 8.0, "posco_future_m_event_mfe_pct": 8.3, "lnf_event_mfe_pct": 10.0, "samsung_sdi_event_mfe_pct": 3.2, "lges_event_mfe_pct": 2.8, "lithium_price_decline_from_2022_peak_pct": -90.0, "catl_resume_if_license_renewed": True},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="cyclical_success_event_premium",
        rerating_result="event_premium",
        round_rerating_label="lithium_price_event_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="should_not_be_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Lithium event is not Stage 3 without company-level call-off, OPM, FCF and inventory quality.",
    ),
    Round233CaseCandidate(
        case_id="r3_loop10_hyundai_hydrogen_fuel_cell_capex",
        symbol="005380",
        company_name="Hyundai Motor hydrogen fuel-cell plant",
        primary_archetype=E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX,
        secondary_archetypes=(E2RArchetype.HYDROGEN_FUEL_CELL_INFRA_KOREA,),
        case_type="success_candidate",
        stage1_date=date(2025, 10, 30),
        stage2_date=date(2025, 10, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="hydrogen_fuel_cell_capex_is_stage2_until_utilization_order_book_margin_and_fcf_confirm",
        stage4b_status="4B-watch-if_hydrogen_theme_rallies_before_orders",
        hard_4c_confirmed=False,
        evidence_fields=("ulsan_hydrogen_fuel_cell_facility_930bn_krw", "facility_area_43000_sqm", "completion_2027", "fuel_cells_electrolyzers_target_applications"),
        red_flag_fields=("utilization_unconfirmed", "order_book_unconfirmed", "hydrogen_demand_delay_risk", "subsidy_infrastructure_delay_risk"),
        price_data_source="Reuters capex/facility evidence",
        reported_price_anchor="Reuters did not provide stock reaction anchor",
        reported_return_anchor="930B KRW plant, 43,000 sqm, 2027 completion",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"investment_krw_bn": 930.0, "investment_usd_mn": 654.0, "facility_area_sqm": 43000.0, "completion_target_year": 2027.0, "target_applications": ["passenger_cars", "commercial_trucks_and_buses", "construction_equipment", "marine_vessels", "electrolyzers"]},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="hydrogen_fuel_cell_capex_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Hydrogen capex is Stage 2; utilization, orders, margin and FCF required before Green.",
    ),
)


def round233_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("calloff", "gwh", "utilization", "opm", "fcf", "margin", "revenue")
    for candidate in ROUND233_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND233_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round233 R3 Loop-10 battery/EV/green price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "event" in field.lower() or "rally" in field.lower() or "price" in field.lower() or "theme" in field.lower()),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "shock" in field.lower() or "risk" in field.lower() or "layoff" in field.lower() or "detention" in field.lower() or "furlough" in field.lower() or "uncertain" in field.lower() or "failure" in field.lower()),
            must_have_fields=ROUND233_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND233_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_battery_ess_green_capex_lithium_or_jv_headline_as_green_alone",
                *ROUND233_GREEN_REQUIRED_FIELDS,
                *ROUND233_GREEN_FORBIDDEN_PATTERNS,
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


def round233_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND233_CASE_CANDIDATES:
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


def round233_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND233_SCORE_ADJUSTMENTS)


def round233_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND233_SHADOW_WEIGHT_ROWS)


def round233_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND233_DEEP_SUB_ARCHETYPES)


def round233_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round233_price_validation": "true"} for field in ROUND233_PRICE_VALIDATION_FIELDS)


def round233_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round233_label": label, "canonical_archetype": canonical} for label, canonical in ROUND233_REQUIRED_TARGET_ALIASES.items())


def round233_summary() -> dict[str, int | bool | str]:
    cases = ROUND233_CASE_CANDIDATES
    return {
        "source_round": ROUND233_SOURCE_ROUND_PATH,
        "large_sector": ROUND233_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "watch_4c_count": sum(1 for case in cases if case.stage4c_date is not None),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND233_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND233_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND233_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round233_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND233_SOURCE_ROUND_PATH,
        "large_sector": ROUND233_LARGE_SECTOR,
        "summary": round233_summary(),
        "target_aliases": dict(ROUND233_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND233_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND233_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND233_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND233_HARD_4C_GATES),
        "deep_sub_archetypes": round233_deep_sub_archetype_rows(),
        "shadow_weights": round233_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round233_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_battery_ess_green_capex_lithium_or_jv_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round233_summary_markdown() -> str:
    summary = round233_summary()
    lines = [
        "# Round 233 R3 Loop 10 Battery / EV / Green Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- 4C-watch cases: {summary['watch_4c_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | stage3 | 4B | 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND233_CASE_CANDIDATES:
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
            "- LGES and SK On ESS pivots are valid Stage 2 watch items, not Green before utilization, OPM and FCF.",
            "- Samsung SDI/GM and Hyundai hydrogen plant show why CAPEX/JV alone is not Stage 3.",
            "- LG Chem/Toyota cathode derisking is useful Stage 2 evidence, but offtake and margin still matter.",
            "- Qcells, SKIET and EcoPro Materials illustrate R3 4C-watch from customs disruption and EV demand shock.",
            "- POSCO Future M / L&F lithium rally is a commodity event premium, not structural rerating.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round233_green_gate_review_markdown() -> str:
    lines = [
        "# Round 233 R3 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R3 Stage 3-Green is not `battery/ESS/green beneficiary`. It requires actual call-off, volume, utilization, margin, FCF, and risk clearance.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND233_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND233_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `5GWh ESS contract` is Stage 2 until ESS revenue, utilization, OPM and FCF confirm.",
            "- `lithium futures +8%` can move materials stocks, but without company call-off and margin it stays event premium.",
            "- `factory groundbreaking` is not Green until orders, utilization and FCF are visible.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round233_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 233 R3 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND233_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND233_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B catches ESS/LFP, lithium, hydrogen, and localization rallies that price before utilization or margin.",
            "- 4C catches demand shock, factory restart uncertainty, customs detention, furloughs, weak-demand JV transfers, and subsidy-quality profit collapse.",
            "- This loop marks no hard 4C, but EV demand shock and supply-chain disruption are strong 4C-watch signals.",
            "",
            "## Case Notes",
            "",
        ]
    )
    for case in ROUND233_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round233_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 233 R3 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND233_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round233_r3_loop10_reports(
    output_directory: str | Path = ROUND233_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND233_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND233_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round233_case_records(), cases_path),
        "audit": _write_json(round233_audit_payload(), audit_path),
        "summary": output / "round233_r3_loop10_price_validation_summary.md",
        "case_matrix": output / "round233_r3_loop10_case_matrix.csv",
        "target_aliases": output / "round233_r3_loop10_target_aliases.csv",
        "score_adjustments": output / "round233_r3_loop10_score_adjustments.csv",
        "shadow_weights": output / "round233_r3_loop10_shadow_weights.csv",
        "deep_sub_archetypes": output / "round233_r3_loop10_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round233_r3_loop10_price_validation_fields.csv",
        "green_gate_review": output / "round233_r3_loop10_green_gate_review.md",
        "price_validation_plan": output / "round233_r3_loop10_price_validation_plan.md",
        "stage4b_4c_review": output / "round233_r3_loop10_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round233_summary_markdown(), encoding="utf-8")
    _write_csv(round233_case_rows(), paths["case_matrix"])
    _write_csv(round233_target_alias_rows(), paths["target_aliases"])
    _write_csv(round233_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round233_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round233_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round233_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round233_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round233_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round233_stage4b_4c_review_markdown(), encoding="utf-8")
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
