"""Round-299 R4 Loop-15 materials/spread/strategic-resources validation pack.

This module converts ``docs/round/round_299.md`` into calibration-only case
records, trigger rows, and reports. It does not change production scoring,
staging, or candidate generation.

Easy example: a graphite tariff can be Stage2 evidence, but it is not Green
until non-China capacity, quality certification, customer awards, and margin
are visible.
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


ROUND299_SOURCE_ROUND_PATH = "docs/round/round_299.md"
ROUND299_ANALYST_ROUND_ID = "round_227"
ROUND299_LARGE_SECTOR = "MATERIALS_SPREAD_STRATEGIC_RESOURCES"
ROUND299_METHOD = "trigger_level_backtest_v1"
ROUND299_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round299_r4_loop15_materials_spread_strategic_trigger_validation"
ROUND299_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop15_round227.jsonl"
ROUND299_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r4_loop15_round227.jsonl"
ROUND299_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round299_r4_loop15_materials_spread_strategic_trigger_validation_audit.json"
ROUND299_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round227_r4_loop15_v1.csv"

ROUND299_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "GRAPHITE_TARIFF_STAGE2_ACTIONABLE": E2RArchetype.GRAPHITE_TARIFF_STAGE2_ACTIONABLE.value,
    "LITHIUM_PRICE_EVENT_PREMIUM": E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM.value,
    "UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2": E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2.value,
    "STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE": E2RArchetype.STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE.value,
    "STEEL_WEAK_DEMAND_FAILED_RERATING": E2RArchetype.STEEL_WEAK_DEMAND_FAILED_RERATING.value,
    "LOCALIZATION_CAPEX_FALSE_POSITIVE": E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE.value,
    "KOREA_ZINC_CONTROL_PREMIUM_4B": E2RArchetype.KOREA_ZINC_CONTROL_PREMIUM_4B.value,
    "CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B": E2RArchetype.CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B.value,
    "COPPER_TCRC_SPREAD_4C_WATCH": E2RArchetype.COPPER_TCRC_SPREAD_4C_WATCH.value,
    "CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C": E2RArchetype.CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C.value,
}

ROUND299_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "tariff_rate_antidumping_duty_or_import_share_is_numeric",
    "china_dependency_or_export_control_risk_is_reduced",
    "trigger_day_market_relative_return_5pp_plus",
    "spread_improvement_path_from_asp_raw_material_or_import_cost_is_explainable",
    "capacity_quality_customer_certification_or_offtake_is_partly_visible",
    "commodity_move_can_bridge_to_company_margin",
)

ROUND299_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "spread_or_strategic_resource_cashflow_path_is_numeric",
    "capacity_customer_qualification_offtake_funding_or_irr_gate_still_pending",
    "no_control_premium_localization_capex_or_export_control_hard_gate_dominates",
)

ROUND299_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "spread_improvement_is_visible_in_results",
    "asp_volume_utilization_margin_are_confirmed",
    "upstream_stake_links_to_downstream_cost_advantage",
    "strategic_resource_project_funding_and_offtake_are_confirmed",
    "operating_fcf_improves_not_just_control_premium",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND299_GREEN_BLOCKERS: tuple[str, ...] = (
    "commodity_price_event_only",
    "control_premium_as_operating_green",
    "localization_capex_without_funding",
    "upstream_stake_without_downstream_margin",
    "tariff_headline_without_asp_volume",
    "lithium_supply_shock_without_inventory_draw",
    "metal_price_without_spread",
    "strategic_resource_label_only",
)

ROUND299_SCORE_UP_AXES: tuple[str, ...] = (
    "tariff_rate_and_import_share",
    "china_dependency_reduction",
    "non_china_capacity_quality_certification",
    "spread_margin_visibility",
    "raw_material_price_durability",
    "tcrc_smelt_margin",
    "strategic_resource_offtake_contract",
    "funding_irr_capex_clarity",
    "control_premium_separation",
    "export_control_exposure",
)

ROUND299_SCORE_DOWN_AXES: tuple[str, ...] = (
    "commodity_price_event_only",
    "control_premium_as_operating_green",
    "localization_capex_without_funding",
    "upstream_stake_without_downstream_margin",
    "tariff_headline_without_asp_volume",
    "lithium_supply_shock_without_inventory_draw",
    "metal_price_without_spread",
    "strategic_resource_label_only",
)

ROUND299_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "control_premium_rally_20_to_30pct",
    "commodity_spot_event_rally_without_margin_evidence",
    "strategic_resource_capex_rally_without_funding_or_offtake",
    "localization_capex_headline_without_irr",
    "tender_buyback_or_share_issuance_dominates_operating_thesis",
)

ROUND299_HARD_4C_GATES: tuple[str, ...] = (
    "tcrc_collapse_breaks_smelter_margin",
    "commodity_price_rally_does_not_convert_to_company_spread",
    "china_export_control_blocks_strategic_material_sourcing",
    "capex_funding_gap_dilution_or_injunction",
    "control_premium_disappears_and_operating_valuation_returns",
    "lithium_price_reversal_inventory_write_down_or_asp_pass_through_failure",
)


@dataclass(frozen=True)
class Round299ShadowWeightRow:
    archetype: E2RArchetype
    tariff_rate_and_import_share: int
    china_dependency_reduction: int
    non_china_capacity_quality_certification: int
    spread_margin_visibility: int
    raw_material_price_durability: int
    tcrc_smelt_margin: int
    strategic_resource_offtake_contract: int
    funding_irr_capex_clarity: int
    control_premium_separation: int
    export_control_exposure: int
    commodity_price_event_only_penalty: int
    control_premium_as_operating_green_penalty: int
    localization_capex_without_funding_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "tariff_rate_and_import_share": _signed(self.tariff_rate_and_import_share),
            "china_dependency_reduction": _signed(self.china_dependency_reduction),
            "non_china_capacity_quality_certification": _signed(self.non_china_capacity_quality_certification),
            "spread_margin_visibility": _signed(self.spread_margin_visibility),
            "raw_material_price_durability": _signed(self.raw_material_price_durability),
            "tcrc_smelt_margin": _signed(self.tcrc_smelt_margin),
            "strategic_resource_offtake_contract": _signed(self.strategic_resource_offtake_contract),
            "funding_irr_capex_clarity": _signed(self.funding_irr_capex_clarity),
            "control_premium_separation": _signed(self.control_premium_separation),
            "export_control_exposure": _signed(self.export_control_exposure),
            "commodity_price_event_only_penalty": _signed(self.commodity_price_event_only_penalty),
            "control_premium_as_operating_green_penalty": _signed(self.control_premium_as_operating_green_penalty),
            "localization_capex_without_funding_penalty": _signed(self.localization_capex_without_funding_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round299TriggerRecord:
    trigger_id: str
    case_id: str
    trigger_type: str
    trigger_date: date
    evidence_available: str
    entry_price_krw: float | None
    event_return_pct: float | str | None
    market_relative_return_pp: float | str | None
    trigger_outcome_label: str
    promote_to: str
    extra_metrics: Mapping[str, object]

    def as_dict(self) -> dict[str, object]:
        return {
            "trigger_id": self.trigger_id,
            "case_id": self.case_id,
            "trigger_type": self.trigger_type,
            "trigger_date": self.trigger_date.isoformat(),
            "evidence_available": self.evidence_available,
            "entry_price_krw": self.entry_price_krw,
            "event_return_pct": self.event_return_pct,
            "market_relative_return_pp": self.market_relative_return_pp,
            "trigger_outcome_label": self.trigger_outcome_label,
            "promote_to": self.promote_to,
            "extra_metrics": dict(self.extra_metrics),
        }

    def as_row(self) -> dict[str, str]:
        row = {key: _value_text(value) for key, value in self.as_dict().items() if key != "extra_metrics"}
        row["extra_metrics"] = json.dumps(self.extra_metrics, ensure_ascii=False, sort_keys=True)
        return row


@dataclass(frozen=True)
class Round299CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
    best_trigger: str
    best_trigger_type: str
    stage_candidate: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    hard_4c_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    event_mfe_pct: float | None
    event_mae_pct: float | None
    market_relative_return_pp: float | None
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    stage_failure_type: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type

    def to_case_record(self) -> E2RCaseRecord:
        guardrails = [
            "production_scoring_changed_false",
            "candidate_generation_input_false",
            "shadow_weight_only_true",
            "full_adjusted_ohlc_complete_false",
            "stage_candidate_not_downgraded_for_missing_full_ohlc",
            "do_not_use_round299_cases_as_candidate_generation_input",
            "do_not_treat_commodity_control_premium_or_capex_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND299_LARGE_SECTOR,
            large_sector=ROUND299_LARGE_SECTOR,
            primary_archetype=self.primary_archetype,
            secondary_archetypes=self.secondary_archetypes,
            expected_group=self.expected_group,
            case_type=self.case_type,
            stage1_date=self.stage1_date,
            stage2_date=self.stage2_date,
            stage3_date=self.stage3_date,
            stage4b_date=self.stage4b_date,
            stage4c_date=self.stage4c_date,
            evidence_summary=self.notes,
            stage1_evidence=self.evidence_fields if self.stage1_date else (),
            stage2_evidence=self.evidence_fields if self.stage2_date else (),
            stage3_evidence=self.evidence_fields if self.stage3_date else (),
            stage4b_evidence=self.red_flag_fields if self.stage4b_date else (),
            stage4c_evidence=self.red_flag_fields if self.stage4c_date else (),
            must_have_fields=ROUND299_STAGE2_ACTIONABLE_RULES + ROUND299_STAGE3_YELLOW_RULES + ROUND299_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.red_flag_fields else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern=self.round_alignment_label,
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                stage1_price=self.stage1_price_anchor,
                stage2_price=self.stage2_price_anchor,
                mfe_30d=self.event_mfe_pct if self.event_mfe_pct and self.event_mfe_pct > 0 else None,
                mae_30d=self.event_mae_pct if self.event_mae_pct and self.event_mae_pct < 0 else None,
                price_validation_status="reported_event_anchor_not_full_ohlc",
            ),
            data_quality=CaseDataQuality(False, True, False, 0.7),
        )

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "symbol": self.symbol,
            "company_name": self.company_name,
            "primary_archetype": self.primary_archetype.value,
            "secondary_archetypes": ";".join(item.value for item in self.secondary_archetypes),
            "case_type": self.case_type,
            "round_case_type": self.round_case_type,
            "best_trigger": self.best_trigger,
            "best_trigger_type": self.best_trigger_type,
            "stage_candidate": self.stage_candidate,
            "stage1_date": _date_text(self.stage1_date),
            "stage2_date": _date_text(self.stage2_date),
            "stage3_date": _date_text(self.stage3_date),
            "stage4b_date": _date_text(self.stage4b_date),
            "stage4c_date": _date_text(self.stage4c_date),
            "hard_4c_confirmed": str(self.hard_4c_confirmed).lower(),
            "evidence_fields": ";".join(self.evidence_fields),
            "red_flag_fields": ";".join(self.red_flag_fields),
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "market_relative_return_pp": _value_text(self.market_relative_return_pp),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "price_validation_status": "reported_event_anchor_not_full_ohlc",
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "notes": self.notes,
        }


ROUND299_SHADOW_WEIGHT_ROWS: tuple[Round299ShadowWeightRow, ...] = (
    Round299ShadowWeightRow(E2RArchetype.GRAPHITE_TARIFF_STAGE2_ACTIONABLE, 5, 5, 5, 3, 3, 0, 3, 2, 1, 5, -4, -2, -2, "tariff+China dependency+relative strength", "capacity/quality/customer gate pending", "customer award+margin+capacity", "POSCO Future M graphite tariff is Stage2-Actionable."),
    Round299ShadowWeightRow(E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM, 1, 2, 1, 3, 5, 0, 1, 1, 1, 2, -5, -1, -1, "lithium supply shock price move", "durable price/margin pending", "ASP pass-through+inventory draw", "CATL mine suspension remains event premium."),
    Round299ShadowWeightRow(E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2, 1, 4, 2, 3, 5, 0, 4, 3, 1, 3, -3, -1, -2, "upstream stake/offtake rights", "cost advantage pending", "downstream margin confirmed", "POSCO/MinRes is supply security Stage2."),
    Round299ShadowWeightRow(E2RArchetype.STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE, 5, 2, 1, 5, 3, 0, 0, 1, 0, 2, -3, -1, -1, "tariff+import share+relative strength", "ASP/utilization pending", "spread margin confirmed", "Hyundai/POSCO anti-dumping is Stage2-Actionable."),
    Round299ShadowWeightRow(E2RArchetype.STEEL_WEAK_DEMAND_FAILED_RERATING, 1, 1, 0, 5, 3, 0, 0, 1, 0, 1, -1, -1, -1, "price/profit estimate cut", "demand recovery pending", "ASP/volume/margin recovery", "Hyundai Steel weak demand is 4C-watch."),
    Round299ShadowWeightRow(E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE, 1, 2, 1, 3, 2, 0, 2, 5, 1, 2, -2, -1, -5, "capex headline", "IRR/funding/customer demand pending", "firm funding+IRR+offtake", "Hyundai Steel U.S. plant is false positive."),
    Round299ShadowWeightRow(E2RArchetype.KOREA_ZINC_CONTROL_PREMIUM_4B, 1, 2, 1, 3, 3, 3, 2, 3, 5, 4, -2, -5, -2, "tender/control premium", "operating cashflow missing", "margin/FCF confirmed", "Korea Zinc tender is 4B not Green."),
    Round299ShadowWeightRow(E2RArchetype.CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B, 2, 5, 3, 4, 4, 3, 5, 5, 5, 5, -2, -4, -4, "strategic resource capex+U.S. backing", "funding/governance/offtake pending", "commercial operation+offtake+FCF", "Korea Zinc refinery needs 4B overlay."),
    Round299ShadowWeightRow(E2RArchetype.COPPER_TCRC_SPREAD_4C_WATCH, 0, 1, 0, 5, 5, 5, 1, 1, 1, 3, -4, -1, -1, "copper price vs TC/RC spread", "smelter margin pending", "TC/RC normalization+margin", "Copper price rally can be bad for smelters if TC/RC collapses."),
    Round299ShadowWeightRow(E2RArchetype.CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C, 1, 5, 4, 3, 4, 1, 4, 2, 1, 5, -2, -1, -1, "export controls on strategic materials", "license/sourcing uncertainty", "alternative supply/customer certification", "Always overlay export-control exposure in R4."),
)


ROUND299_TRIGGER_RECORDS: tuple[Round299TriggerRecord, ...] = (
    Round299TriggerRecord("r4l15_poscofm_graphite_T1", "r4_loop15_posco_future_m_graphite_tariff", "Stage2-Actionable", date(2025, 7, 18), "U.S. 93.5% tariff on Chinese graphite/anode active materials, China graphite dominance, POSCO Future M +20%", None, 20, None, "Stage2_promote_candidate", "Stage3-Yellow_candidate", {"us_graphite_antidumping_tariff_pct": 93.5}),
    Round299TriggerRecord("r4l15_lithium_catl_T2", "r4_loop15_catl_yichun_lithium_event", "event_premium", date(2025, 8, 11), "CATL Yichun mine suspension; POSCO Future M +8.3%, L&F +10%, but CATL says no material impact", None, "POSCO Future M +8.3 / L&F +10 / SDI +3.2 / LGES +2.8", None, "event_premium_not_stage3", "4B-watch", {"cme_lithium_carbonate_august_rally_pct": 27}),
    Round299TriggerRecord("r4l15_posco_minres_T1", "r4_loop15_posco_minres_lithium_jv", "Stage2_supply_security", date(2025, 11, 11), "POSCO pays $765M for 30% MinRes lithium JV, 15% indirect Wodgina/Mt Marion exposure", None, "MinRes +10.8 / POSCO unavailable", None, "success_candidate_stage2", "Stage2", {"minres_deal_value_usd_mn": 765}),
    Round299TriggerRecord("r4l15_steel_antidumping_T1", "r4_loop15_hyundai_posco_steel_antidumping", "Stage2-Actionable", date(2025, 2, 20), "Korea imposes 27.91-38.02% tariff on Chinese steel plates; Chinese steel imports 49% of Korea steel imports", None, "Hyundai Steel +5.8 / POSCO +3.9 / KOSPI -0.7", "6.5/4.6", "Stage2_promote_candidate", "Stage2-Actionable", {"hyundai_market_relative_pp": 6.5, "posco_market_relative_pp": 4.6}),
    Round299TriggerRecord("r4l15_hyundai_steel_weak_T1", "r4_loop15_hyundai_steel_weak_demand", "4C-watch", date(2024, 6, 21), "Rebar price expected -10%, net profit estimate cut 73% to 215B won, target cut 14%", 29000, -1.2, None, "failed_rerating_4C_watch", "4C-watch", {"net_profit_estimate_cut_pct": -73}),
    Round299TriggerRecord("r4l15_hyundai_steel_capex_T1", "r4_loop15_hyundai_steel_us_localization_capex", "false_positive_score", date(2025, 4, 22), "U.S. plant funding unclear, 50% debt, stock lost 21.2% since announcement", None, -21.2, None, "false_positive_score", "4C-watch", {"debt_funding_share_pct": 50}),
    Round299TriggerRecord("r4l15_koreazinc_tender_T0", "r4_loop15_korea_zinc_control_premium", "4B-watch", date(2024, 9, 13), "MBK/Young Poong tender offer 660,000 won, 19% premium; Korea Zinc +24%", None, 24, None, "event_premium_4B_control_premium", "4B-watch", {"offer_price_krw": 660000}),
    Round299TriggerRecord("r4l15_koreazinc_refinery_T1", "r4_loop15_korea_zinc_us_critical_minerals_smelter", "Stage2_strategic_resource", date(2025, 12, 15), "U.S.-backed $7.4B critical minerals refinery, antimony/germanium/gallium etc, shares +27%", None, 27, None, "Stage2_with_4B_overlay", "Stage2", {"us_refinery_investment_usd_bn": 7.4}),
    Round299TriggerRecord("r4l15_koreazinc_refinery_T3", "r4_loop15_korea_zinc_us_critical_minerals_smelter", "4B-watch", date(2025, 12, 16), "MBK/Young Poong seek injunction to block share issuance; shares -13%", None, -13, None, "4B_governance_dilution_overlay", "4B-watch", {"share_issuance_objected": True}),
    Round299TriggerRecord("r4l15_copper_tcrc_T1", "r4_loop15_copper_tcrc_smelt_margin_watch", "4C-watch", date(2025, 10, 15), "Japan/Spain/South Korea warn copper TC/RCs unsustainable, some Chinese smelters process for free/loss", None, "price_data_unavailable_after_deep_search", None, "thesis_break_watch", "4C-watch", {"tcrc_market_condition": "unsustainable"}),
    Round299TriggerRecord("r4l15_china_export_controls_T2", "r4_loop15_china_strategic_mineral_export_controls", "4C-watch_reference", date(2025, 2, 4), "China controls tungsten, bismuth, indium, tellurium, molybdenum and proposes battery/lithium/gallium processing tech restrictions", None, "price_data_unavailable_after_deep_search", None, "strategic_materials_4C_reference", "4C-watch", {"hard_4c_confirmed_for_specific_krx_name": False}),
)


ROUND299_CASE_CANDIDATES: tuple[Round299CaseCandidate, ...] = (
    Round299CaseCandidate("r4_loop15_posco_future_m_graphite_tariff", "003670", "POSCO Future M", E2RArchetype.GRAPHITE_TARIFF_STAGE2_ACTIONABLE, (E2RArchetype.FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN, E2RArchetype.ANODE_GRAPHITE_SUPPLYCHAIN_KOREA), "success_candidate", "Stage2_promote_candidate", "T1/T2", "Stage2-Actionable_to_Stage3-Yellow_candidate", "Stage2-Actionable_to_Stage3-Yellow_candidate", date(2024, 4, 26), date(2025, 7, 18), None, date(2025, 7, 18), None, False, ("US_graphite_antidumping_tariff_93_5pct", "approx_total_tariff_160pct", "China_battery_grade_graphite_control_99pct", "POSCO_Future_M_plus_20pct"), ("non_china_capacity_missing", "quality_certification_missing", "customer_award_missing", "anode_margin_missing"), 20, None, None, None, None, {"us_graphite_antidumping_tariff_pct": 93.5, "approx_total_us_tariff_on_chinese_graphite_pct": 160, "posco_future_m_event_mfe_pct": 20, "syrah_resources_event_mfe_pct": 22, "nouveau_monde_event_mfe_pct": 26, "novonix_event_mfe_pct": 15, "china_battery_grade_graphite_control_pct": 99, "china_synthetic_graphite_control_pct": 69, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "missed_due_to_score", "Stage2_promote_candidate_with_quality_capacity_4B_watch", "policy_event_rerating", "stage2_watch_success", "Graphite tariff and China dependency reduction justify Stage2-Actionable, but quality/capacity/customer award gates remain."),
    Round299CaseCandidate("r4_loop15_catl_yichun_lithium_event", "003670/066970/006400/373220", "POSCO Future M / L&F / Samsung SDI / LGES", E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM, (E2RArchetype.EVENT_LITHIUM_PRICE_RALLY, E2RArchetype.LITHIUM_CYCLE_OVERLAY), "event_premium", "event_premium", "T2", "event_premium", "4B-watch", date(2025, 8, 11), None, None, date(2025, 8, 18), None, False, ("CATL_Yichun_mine_suspension", "POSCO_Future_M_plus_8_3pct", "LNF_plus_10pct", "CME_lithium_carbonate_plus_27pct"), ("CATL_no_material_impact", "license_renewal_possible", "durable_margin_missing"), 10, None, None, None, None, {"posco_future_m_event_mfe_pct": 8.3, "lnf_event_mfe_pct": 10.0, "samsung_sdi_event_mfe_pct": 3.2, "lges_event_mfe_pct": 2.8, "ganfeng_lithium_event_mfe_pct": 21, "tianqi_lithium_event_mfe_pct": 18, "cme_lithium_carbonate_august_rally_pct": 27, "lithium_price_decline_from_2022_peak_pct": -90, "license_renewal_possible": True, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "price_moved_without_evidence", "event_premium_not_stage3", "event_premium", "false_yellow", "Lithium supply-shock rally requires durable lithium price, inventory drawdown and material margin before Stage3."),
    Round299CaseCandidate("r4_loop15_posco_minres_lithium_jv", "005490/003670", "POSCO Holdings / POSCO Future M", E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2, (E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA, E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2), "success_candidate", "Stage2 supply-security", "T1/T2", "Stage2_supply_security", "Stage2_supply_security", date(2022, 1, 1), date(2025, 11, 11), None, None, None, False, ("MinRes_lithium_JV_30pct_stake", "deal_value_765M_USD", "Wodgina_indirect_15pct", "Mt_Marion_indirect_15pct"), ("spodumene_far_below_2022_peak", "downstream_margin_missing"), 10.8, None, None, None, None, {"minres_deal_value_usd_mn": 765, "minres_event_mfe_pct": 10.8, "posco_effective_interest_wodgina_pct": 15, "posco_effective_interest_mt_marion_pct": 15, "spodumene_mid_2025_low_usd_t": 610, "spodumene_august_2025_usd_t": 880, "spodumene_2022_peak_usd_t": 6000, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "aligned", "success_candidate_stage2", "unknown", "stage2_watch_success", "Upstream lithium stake improves supply security, but Stage3 requires cost advantage and downstream margin."),
    Round299CaseCandidate("r4_loop15_hyundai_posco_steel_antidumping", "004020/005490", "Hyundai Steel / POSCO Holdings", E2RArchetype.STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE, (E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF, E2RArchetype.STEEL_TARIFF_EXPORT_RISK), "success_candidate", "Stage2_promote_candidate", "T1/T2", "Stage2-Actionable", "Stage2-Actionable", date(2024, 1, 1), date(2025, 2, 20), None, date(2025, 2, 20), None, False, ("anti_dumping_tariff_27_91_to_38_02pct", "Chinese_steel_imports_10_4B_USD", "China_import_share_49pct", "Hyundai_plus_5_8pct", "POSCO_plus_3_9pct"), ("ASP_recovery_missing", "volume_recovery_missing", "utilization_missing", "raw_material_spread_missing"), 5.8, None, 6.5, None, None, {"anti_dumping_tariff_pct": "27.91-38.02", "chinese_steel_imports_2024_usd_bn": 10.4, "chinese_share_of_korea_steel_imports_pct": 49, "hyundai_steel_event_mfe_pct": 5.8, "posco_event_mfe_pct": 3.9, "kospi_same_context_pct": -0.7, "hyundai_market_relative_pp": 6.5, "posco_market_relative_pp": 4.6, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "missed_due_to_score", "Stage2_Actionable_spread_relief", "policy_event_rerating", "stage2_watch_success", "Anti-dumping tariff, import share and relative strength make this Stage2-Actionable; Green needs ASP/volume/margin."),
    Round299CaseCandidate("r4_loop15_hyundai_steel_weak_demand", "004020", "Hyundai Steel", E2RArchetype.STEEL_WEAK_DEMAND_FAILED_RERATING, (E2RArchetype.STEEL_METAL_SPREAD, E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK), "failed_rerating", "failed_rerating_4c_watch", "T1/T2", "4C-watch", "4C-watch", date(2024, 6, 21), None, None, None, date(2024, 6, 21), False, ("rebar_price_decline_expected_minus_10pct", "net_profit_estimate_cut_minus_73pct", "target_price_cut_minus_14pct"), ("construction_demand", "shipbuilding_plate_competition", "Japanese_Chinese_steel_competition"), None, -1.2, None, 29000, None, {"entry_price_anchor_krw": 29000, "event_mae_pct": -1.2, "rebar_price_decline_expected_pct": -10, "net_profit_estimate_after_cut_krw_bn": 215, "net_profit_estimate_cut_pct": -73, "target_price_krw": 30000, "target_price_cut_pct": -14, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "unknown", "thesis_break_watch", "thesis_break", "should_have_been_red", "Rebar price and net-profit estimate cuts are materials spread 4C-watch triggers."),
    Round299CaseCandidate("r4_loop15_hyundai_steel_us_localization_capex", "004020", "Hyundai Steel", E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE, (E2RArchetype.STEEL_TARIFF_EXPORT_RISK, E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY), "failed_rerating", "false_positive_score", "T1", "false_positive_score", "false_positive_score", date(2025, 3, 25), None, None, date(2025, 4, 22), date(2025, 4, 22), False, ("US_plant_investment_5_8B_USD", "Louisiana_capacity_2_7M_tonnes", "Hyundai_group_US_package_21B_USD"), ("funding_unclear", "IRR_unclear", "stock_decline_since_announcement_minus_21_2pct", "debt_funding_share_50pct"), 5.0, -21.2, None, None, None, {"initial_mfe_pct": 5.0, "close_event_return_pct": -4.4, "us_plant_investment_usd_bn": 5.8, "us_plant_capacity_mn_tonnes": 2.7, "hyundai_group_us_package_usd_bn": 21, "stock_decline_since_announcement_pct": -21.2, "debt_funding_share_pct": 50, "full_funding_plan_disclosed": False, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "false_positive_score", "false_positive_score", "no_rerating", "false_green", "Localization capex requires funding, IRR, customer demand and tariff saving clarity before Green."),
    Round299CaseCandidate("r4_loop15_korea_zinc_control_premium", "010130/000670", "Korea Zinc / Young Poong / MBK", E2RArchetype.KOREA_ZINC_CONTROL_PREMIUM_4B, (E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE, E2RArchetype.NONFERROUS_STRATEGIC_METALS), "4b_watch", "event_premium_4b_watch", "T0/T2", "4B_control_premium", "4B-watch", date(2024, 9, 13), None, None, date(2024, 9, 13), None, False, ("tender_offer_660000_KRW", "tender_premium_18_7pct", "Korea_Zinc_plus_24pct", "upper_limit_plus_29_9pct"), ("control_premium_only", "operating_cashflow_improvement_unconfirmed", "governance_fight", "debt_funded_buyback_watch"), 29.9, None, None, None, None, {"offer_price_krw": 660000, "prior_close_krw": 556000, "tender_premium_pct": 18.7, "korea_zinc_event_mfe_pct": 24, "korea_zinc_event_high_krw": 690000, "upper_limit_return_pct": 29.9, "record_high_krw": 1470000, "operating_cashflow_improvement_confirmed": False, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "price_moved_without_evidence", "event_premium_4B_watch", "event_premium", "false_green", "Control premium must be separated from smelter spread, zinc price and operating cashflow."),
    Round299CaseCandidate("r4_loop15_korea_zinc_us_critical_minerals_smelter", "010130", "Korea Zinc", E2RArchetype.CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B, (E2RArchetype.NONFERROUS_STRATEGIC_METALS, E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY), "success_candidate", "Stage2_with_4B_overlay", "T1/T3", "Stage2_strategic_resource_with_4B_overlay", "Stage2_strategic_resource_with_4B_overlay", date(2024, 11, 18), date(2025, 12, 15), None, date(2025, 12, 16), None, False, ("US_refinery_investment_7_4B_USD", "antimony_germanium_gallium_zinc_lead_copper_gold_silver", "commercial_operation_2027_2029", "event_return_plus_27pct"), ("share_issuance_objected", "injunction_event_minus_13pct", "funding_plan_not_finalized", "offtake_or_margin_unconfirmed"), 27, -13, None, None, None, {"national_core_technology_ruling": True, "us_refinery_investment_usd_bn": 7.4, "event_mfe_pct": 27, "injunction_event_mae_pct": -13, "mbk_youngpoong_combined_stake_pct": 44, "share_issuance_objected": True, "funding_plan_finalized": False, "offtake_or_margin_confirmed": False, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "evidence_good_but_price_failed", "Stage2_with_4B_overlay", "unknown", "stage2_watch_success", "Strategic-resource capex needs funding, governance, offtake and margin before Green."),
    Round299CaseCandidate("r4_loop15_copper_tcrc_smelt_margin_watch", "LS_MnM/Korea_Zinc/copper_smelter_readthrough", "Copper smelter read-through", E2RArchetype.COPPER_TCRC_SPREAD_4C_WATCH, (E2RArchetype.NONFERROUS_STRATEGIC_METALS, E2RArchetype.COMMODITY_SPREAD), "4c_thesis_break", "4c_watch", "T1", "4C-watch", "4C-watch", date(2025, 10, 15), None, None, None, date(2025, 10, 15), False, ("TC_RC_unsustainable", "Chinese_smelters_free_or_loss_processing", "copper_record_price_11200_USD_t", "Mercuria_withdrawal_40000t"), ("metal_price_without_spread", "smelter_margin_squeeze", "concentrate_shortage"), None, None, None, None, None, {"tcrc_market_condition": "unsustainable", "some_chinese_smelters_processing_fee_condition": "free_or_loss", "copper_record_price_oct_2025_usd_t": 11200, "copper_ytd_gain_2025_pct": 27, "copper_record_price_dec_2025_usd_t": 11540, "mercuria_withdrawal_tonnes": 40000, "cancelled_lme_warrants_tonnes": 56875, "cancelled_warrants_share_lme_stocks_pct": 35, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "unknown", "thesis_break_watch", "thesis_break", "should_have_been_red", "Copper price bullishness and smelter TC/RC economics must be scored separately."),
    Round299CaseCandidate("r4_loop15_china_strategic_mineral_export_controls", "003670/051910/010130/strategic_materials_basket", "Strategic materials export-control reference", E2RArchetype.CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C, (E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, E2RArchetype.CARBON_CREDIT_CBAM_COMPLIANCE), "4c_thesis_break", "4c_reference", "T1/T2", "4C_strategic_reference", "4C-watch_reference", date(2023, 7, 1), None, None, None, date(2025, 2, 4), False, ("graphite_export_permits", "rare_earth_magnet_technology_ban", "antimony_controls", "gallium_germanium_restrictions", "tungsten_bismuth_indium_tellurium_molybdenum_controls"), ("China_export_control_exposure", "alternative_supply_missing", "customer_certification_missing"), None, None, None, None, None, {"controlled_materials": ["graphite", "rare_earth_magnet_technology", "antimony", "gallium", "germanium", "tungsten", "bismuth", "indium", "tellurium", "molybdenum", "battery_processing_technology", "lithium_processing_technology"], "china_graphite_refining_share_context_pct": 90, "hard_4c_confirmed_for_specific_krx_name": False, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "unknown", "thesis_break_reference", "thesis_break", "unknown", "China export-control exposure must be explicit overlay for all strategic-materials Stage3 candidates."),
)


def round299_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(case.to_case_record() for case in ROUND299_CASE_CANDIDATES)


def round299_summary() -> dict[str, object]:
    return {
        "source_round": ROUND299_SOURCE_ROUND_PATH,
        "round_id": ROUND299_ANALYST_ROUND_ID,
        "large_sector": ROUND299_LARGE_SECTOR,
        "method": ROUND299_METHOD,
        "case_candidate_count": len(ROUND299_CASE_CANDIDATES),
        "trigger_count": len(ROUND299_TRIGGER_RECORDS),
        "stage2_actionable_candidate_count": 4,
        "stage3_yellow_candidate_count": 3,
        "stage3_green_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 4,
        "stage4c_watch_count": 5,
        "hard_4c_case_count": 0,
        "missed_structural_count": 0,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
    }


def round299_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(case.as_row() for case in ROUND299_CASE_CANDIDATES)


def round299_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND299_TRIGGER_RECORDS)


def round299_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"requested_alias": key, "canonical_archetype": value} for key, value in ROUND299_REQUIRED_TARGET_ALIASES.items())


def round299_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND299_SHADOW_WEIGHT_ROWS)


def round299_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    rows = []
    for axis in ROUND299_SCORE_UP_AXES:
        rows.append({"axis": axis, "points": "+5", "direction": "raise", "reason": "R4 trigger quality axis"})
    for axis in ROUND299_SCORE_DOWN_AXES:
        rows.append({"axis": axis, "points": "-5", "direction": "lower", "reason": "R4 false-positive or 4B/4C blocker"})
    return tuple(rows)


def round299_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND299_SOURCE_ROUND_PATH,
        "round_id": ROUND299_ANALYST_ROUND_ID,
        "large_sector": ROUND299_LARGE_SECTOR,
        "method": ROUND299_METHOD,
        "summary": round299_summary(),
        "target_archetypes": dict(ROUND299_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND299_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND299_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND299_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND299_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND299_SCORE_UP_AXES),
        "score_down_axes": list(ROUND299_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND299_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND299_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_apply_round299_shadow_weights_to_production_scoring_yet",
            "do_not_use_round299_cases_as_candidate_generation_input",
            "do_not_treat_commodity_price_or_control_premium_as_green",
            "do_not_ignore_tcrc_spread_funding_irr_or_export_control_overlays",
        ],
    }


def render_round299_summary_markdown() -> str:
    summary = round299_summary()
    lines = [
        "# Round 299 R4 Loop 15 Materials/Spread/Strategic Resources Trigger Validation",
        "",
        "이번 라운드는 소재 가격 headline이 아니라 tariff, spread, TC/RC, funding, control premium을 분리한다.",
        "",
        "쉬운 예: Korea Zinc가 tender battle로 급등해도, 그것은 아연 제련 margin이 좋아진 Green이 아니라 control-premium 4B다.",
        "",
        "## Summary",
        "",
    ]
    for key in (
        "round_id",
        "large_sector",
        "case_candidate_count",
        "trigger_count",
        "stage2_actionable_candidate_count",
        "stage3_yellow_candidate_count",
        "stage3_green_confirmed_count",
        "stage4b_watch_count",
        "stage4c_watch_count",
        "hard_4c_case_count",
        "production_scoring_changed",
        "candidate_generation_input",
        "full_adjusted_ohlc_complete",
        "shadow_weight_only",
    ):
        lines.append(f"- {key}: {summary[key]}")
    lines.extend(
        [
            "",
            "## Core Findings",
            "",
            "- POSCO Future M graphite tariff는 Stage2-Actionable / Yellow candidate지만, capacity/quality/customer gate가 남는다.",
            "- CATL lithium mine suspension은 event premium이다. durable price와 margin 전에는 Stage3가 아니다.",
            "- Hyundai Steel/POSCO anti-dumping은 tariff, import share, relative strength가 있어 Stage2-Actionable이다.",
            "- Hyundai Steel U.S. plant는 funding/IRR/customer demand가 닫히지 않은 localization capex false positive다.",
            "- Korea Zinc tender battle은 control premium 4B이고, U.S. critical-minerals refinery는 Stage2 + 4B governance/dilution overlay다.",
            "- Copper record price와 smelter TC/RC margin은 반대로 움직일 수 있으므로 따로 scoring해야 한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round299_trigger_grid_markdown() -> str:
    lines = [
        "# Round 299 Trigger Grid",
        "",
        "| trigger_id | case_id | date | type | outcome | promote_to | evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND299_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {trigger.trigger_date.isoformat()} | {trigger.trigger_type} | {trigger.trigger_outcome_label} | {trigger.promote_to} | {trigger.evidence_available} |"
        )
    return "\n".join(lines) + "\n"


def render_round299_stage_rules_markdown() -> str:
    lines = ["# Round 299 Stage Rules", "", "Do not apply these weights to production scoring yet.", "", "## Stage2-Actionable", ""]
    lines.extend(f"- {rule}" for rule in ROUND299_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow", ""])
    lines.extend(f"- {rule}" for rule in ROUND299_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Stage3-Green", ""])
    lines.extend(f"- {rule}" for rule in ROUND299_STAGE3_GREEN_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND299_GREEN_BLOCKERS)
    return "\n".join(lines) + "\n"


def render_round299_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 299 4B/4C Review",
        "",
        "이번 라운드에서 확정 Green과 hard 4C는 없다. 대신 strong 4B/4C-watch가 많다.",
        "",
        "## 4B Watch",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND299_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## 4C Gates", ""])
    lines.extend(f"- {item}" for item in ROUND299_HARD_4C_GATES)
    return "\n".join(lines) + "\n"


def render_round299_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round 299 Price Validation Plan",
            "",
            "- reported_event_anchor_not_full_ohlc 상태를 유지한다.",
            "- full adjusted OHLC가 없다는 이유로 Stage2/Yellow 후보를 강등하지 않는다.",
            "- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.",
            "- 다음 단계에서는 trigger date 기준 30/90/180일 MFE/MAE, below-entry, control-premium 소멸 여부를 채운다.",
            "",
        ]
    )


def write_round299_r4_loop15_reports(
    *,
    output_directory: str | Path = ROUND299_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND299_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND299_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND299_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND299_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round299_case_records(), cases_path),
        "triggers": write_round299_triggers(triggers_path),
        "audit": _write_json(round299_audit_payload(), audit_path),
        "weight_profile": _write_csv(round299_shadow_weight_rows(), weight_profile_path),
        "summary": output / "round299_r4_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round299_r4_loop15_case_matrix.csv",
        "trigger_grid": output / "round299_r4_loop15_trigger_grid.csv",
        "target_aliases": output / "round299_r4_loop15_target_aliases.csv",
        "score_adjustments": output / "round299_r4_loop15_score_adjustments.csv",
        "shadow_weights": output / "round299_r4_loop15_shadow_weights.csv",
        "stage_rules": output / "round299_r4_loop15_stage_rules.md",
        "trigger_grid_md": output / "round299_r4_loop15_trigger_grid.md",
        "price_validation_plan": output / "round299_r4_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round299_r4_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round299_summary_markdown(), encoding="utf-8")
    _write_csv(round299_case_rows(), paths["case_matrix"])
    _write_csv(round299_trigger_rows(), paths["trigger_grid"])
    _write_csv(round299_target_alias_rows(), paths["target_aliases"])
    _write_csv(round299_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round299_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round299_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round299_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round299_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round299_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round299_triggers(path: str | Path = ROUND299_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND299_TRIGGER_RECORDS]
    target.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return target


def _write_json(payload: Mapping[str, object], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[Mapping[str, object]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows_tuple = tuple(rows)
    with target.open("w", encoding="utf-8", newline="") as handle:
        if not rows_tuple:
            handle.write("")
            return target
        writer = csv.DictWriter(handle, fieldnames=list(rows_tuple[0].keys()))
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow({key: _value_text(value) for key, value in row.items()})
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def _signed(value: int) -> str:
    return f"{value:+d}"


__all__ = [
    "ROUND299_CASE_CANDIDATES",
    "ROUND299_GREEN_BLOCKERS",
    "ROUND299_HARD_4C_GATES",
    "ROUND299_LARGE_SECTOR",
    "ROUND299_REQUIRED_TARGET_ALIASES",
    "ROUND299_SCORE_DOWN_AXES",
    "ROUND299_SCORE_UP_AXES",
    "ROUND299_SHADOW_WEIGHT_ROWS",
    "ROUND299_STAGE2_ACTIONABLE_RULES",
    "ROUND299_STAGE3_GREEN_RULES",
    "ROUND299_STAGE3_YELLOW_RULES",
    "ROUND299_STAGE4B_WATCH_TRIGGERS",
    "ROUND299_TRIGGER_RECORDS",
    "render_round299_stage_rules_markdown",
    "render_round299_stage4b_4c_review_markdown",
    "render_round299_trigger_grid_markdown",
    "round299_audit_payload",
    "round299_case_records",
    "round299_case_rows",
    "round299_shadow_weight_rows",
    "round299_summary",
    "round299_trigger_rows",
    "write_round299_r4_loop15_reports",
]
