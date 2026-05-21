"""Round-306 R11 Loop-15 policy/geopolitics/disaster/event trigger pack.

This module turns ``docs/round/round_306.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a defense export headline becomes stronger only after it closes
into a signed contract, delivery, revenue, margin, and cash collection. A
political shock or energy chokepoint is the opposite: even if a relief bounce
appears, it is a 4C risk overlay until company-level EPS/FCF evidence is rebuilt.
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


ROUND306_SOURCE_ROUND_PATH = "docs/round/round_306.md"
ROUND306_ANALYST_ROUND_ID = "round_234"
ROUND306_LARGE_SECTOR = "POLICY_GEOPOLITICS_DISASTER_EVENT"
ROUND306_METHOD = "trigger_level_backtest_v1"
ROUND306_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round306_r11_loop15_policy_geopolitical_event_trigger_validation"
ROUND306_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop15_round234.jsonl"
ROUND306_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r11_loop15_round234.jsonl"
ROUND306_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round306_r11_loop15_policy_geopolitical_event_trigger_validation_audit.json"
ROUND306_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round234_r11_loop15_v1.csv"

ROUND306_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE": E2RArchetype.DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE.value,
    "GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW": E2RArchetype.GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW.value,
    "CHIP_EXPORT_CONTROL_4C_WATCH": E2RArchetype.CHIP_EXPORT_CONTROL_4C_WATCH.value,
    "SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH": E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH.value,
    "POLITICAL_SYSTEM_SHOCK_MARKET_4C": E2RArchetype.POLITICAL_SYSTEM_SHOCK_MARKET_4C.value,
    "HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF": E2RArchetype.HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF.value,
    "NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B": E2RArchetype.NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B.value,
    "NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE": E2RArchetype.NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE.value,
}

ROUND306_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "policy_or_geopolitical_headline_closes_into_signed_contract_or_delivery",
    "contract_value_or_delivery_revenue_is_meaningful_for_backlog_or_quarterly_revenue",
    "market_relative_event_return_exceeds_5pp_or_record_high_is_reported",
    "delivery_to_revenue_or_OP_estimate_revision_is_visible",
    "defense_local_production_tech_transfer_or_service_package_is_specific",
    "policy_relief_turns_into_supply_route_license_budget_or_procurement",
    "political_labor_export_control_disaster_events_are_separated_as_4C_overlays",
)

ROUND306_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "defense_contract_can_change_OP_or_EPS_path_but_margin_or_cash_collection_is_pending",
    "delivery_to_revenue_and_OP_revision_visible_but_multi_quarter_execution_pending",
    "naval_shipbuilding_policy_optionality_visible_but_formal_contract_or_tech_transfer_pending",
)

ROUND306_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "defense_contract_delivers_into_revenue_margin_and_cash_collection",
    "local_production_or_technology_transfer_terms_do_not_destroy_margin",
    "policy_relief_becomes_recurring_procurement_budget_license_or_formal_contract",
    "labor_export_control_political_and_energy_risks_are_cleared",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND306_GREEN_BLOCKERS: tuple[str, ...] = (
    "geopolitical_theme_only",
    "preferred_supplier_without_signed_contract",
    "defense_order_without_delivery_margin",
    "policy_relief_without_earnings",
    "energy_supply_relief_as_growth",
    "political_false_break_as_structural",
    "technology_transfer_headline_only",
    "full_adjusted_ohlc_missing_for_stage3_confirmation",
)

ROUND306_SCORE_UP_AXES: tuple[str, ...] = (
    "signed_defense_contract_value",
    "delivery_to_revenue_conversion",
    "defense_backlog_growth",
    "local_production_technology_transfer_terms",
    "trade_policy_license_risk",
    "labor_disruption_output_risk",
    "political_system_stability",
    "energy_chokepoint_exposure",
    "alternative_supply_route_relief",
    "disaster_direct_cost_and_recovery",
)

ROUND306_SCORE_DOWN_AXES: tuple[str, ...] = (
    "geopolitical_theme_only",
    "preferred_supplier_without_signed_contract",
    "defense_order_without_delivery_margin",
    "policy_relief_without_earnings",
    "energy_supply_relief_as_growth",
    "political_false_break_as_structural",
    "technology_transfer_headline_only",
)

ROUND306_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "defense_stocks_rerate_on_geopolitics_before_signed_contract",
    "naval_nuclear_sub_story_rises_before_formal_US_Navy_contract_or_tech_transfer_terms",
    "policy_relief_after_energy_shock_is_treated_as_growth",
    "political_shock_reverses_quickly_but_governance_risk_remains",
    "labor_strike_threat_rises_or_fades_without_actual_output_data",
)

ROUND306_HARD_4C_GATES: tuple[str, ...] = (
    "martial_law_or_political_system_shock",
    "export_license_revocation_affecting_production_upgrade",
    "labor_strike_threatening_core_national_export_output",
    "energy_chokepoint_closure_oil_shock_or_circuit_breaker",
    "defense_contract_cancellation_or_political_delay",
    "disaster_causing_direct_economic_damage_and_recovery_cost",
)


@dataclass(frozen=True)
class Round306ShadowWeightRow:
    archetype: E2RArchetype
    signed_defense_contract_value: int
    delivery_to_revenue_conversion: int
    defense_backlog_growth: int
    local_production_technology_transfer_terms: int
    trade_policy_license_risk: int
    labor_disruption_output_risk: int
    political_system_stability: int
    energy_chokepoint_exposure: int
    alternative_supply_route_relief: int
    disaster_direct_cost_recovery: int
    geopolitical_theme_only_penalty: int
    preferred_supplier_without_signed_contract_penalty: int
    defense_order_without_delivery_margin_penalty: int
    policy_relief_without_earnings_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "signed_defense_contract_value": _signed(self.signed_defense_contract_value),
            "delivery_to_revenue_conversion": _signed(self.delivery_to_revenue_conversion),
            "defense_backlog_growth": _signed(self.defense_backlog_growth),
            "local_production_technology_transfer_terms": _signed(self.local_production_technology_transfer_terms),
            "trade_policy_license_risk": _signed(self.trade_policy_license_risk),
            "labor_disruption_output_risk": _signed(self.labor_disruption_output_risk),
            "political_system_stability": _signed(self.political_system_stability),
            "energy_chokepoint_exposure": _signed(self.energy_chokepoint_exposure),
            "alternative_supply_route_relief": _signed(self.alternative_supply_route_relief),
            "disaster_direct_cost_recovery": _signed(self.disaster_direct_cost_recovery),
            "geopolitical_theme_only_penalty": _signed(self.geopolitical_theme_only_penalty),
            "preferred_supplier_without_signed_contract_penalty": _signed(self.preferred_supplier_without_signed_contract_penalty),
            "defense_order_without_delivery_margin_penalty": _signed(self.defense_order_without_delivery_margin_penalty),
            "policy_relief_without_earnings_penalty": _signed(self.policy_relief_without_earnings_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round306TriggerRecord:
    trigger_id: str
    case_id: str
    trigger_type: str
    trigger_date: str
    evidence_available: str
    event_return_pct: float | str | None
    trigger_outcome_label: str
    promote_to: str
    extra_metrics: Mapping[str, object]

    def as_dict(self) -> dict[str, object]:
        return {
            "trigger_id": self.trigger_id,
            "case_id": self.case_id,
            "trigger_type": self.trigger_type,
            "trigger_date": self.trigger_date,
            "evidence_available": self.evidence_available,
            "event_return_pct": self.event_return_pct,
            "trigger_outcome_label": self.trigger_outcome_label,
            "promote_to": self.promote_to,
            "extra_metrics": dict(self.extra_metrics),
        }

    def as_row(self) -> dict[str, str]:
        row = {key: _value_text(value) for key, value in self.as_dict().items() if key != "extra_metrics"}
        row["extra_metrics"] = json.dumps(self.extra_metrics, ensure_ascii=False, sort_keys=True)
        return row


@dataclass(frozen=True)
class Round306CaseCandidate:
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
            "do_not_use_round306_cases_as_candidate_generation_input",
            "do_not_treat_policy_geopolitics_or_disaster_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND306_LARGE_SECTOR,
            large_sector=ROUND306_LARGE_SECTOR,
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
            stage1_evidence=tuple(field for field in self.evidence_fields if "headline" in field or "awareness" in field),
            stage2_evidence=tuple(field for field in self.evidence_fields if "contract" in field or "delivery" in field or "relief" in field),
            stage3_evidence=tuple(field for field in self.evidence_fields if "margin" in field or "cash_collection" in field),
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4b" in field or "dilution" in field or "policy_premium" in field),
            stage4c_evidence=tuple(field for field in self.red_flag_fields if "4c" in field or "shock" in field or "strike" in field or "license" in field),
            must_have_fields=ROUND306_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern="reported_event_anchor_only",
            score_weight_hint={},
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(price_validation_status="price_data_unavailable_after_deep_search"),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.72,
            ),
        )

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "symbol": self.symbol,
            "company_name": self.company_name,
            "primary_archetype": self.primary_archetype.value,
            "secondary_archetypes": "|".join(archetype.value for archetype in self.secondary_archetypes),
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
            "evidence_fields": "|".join(self.evidence_fields),
            "red_flag_fields": "|".join(self.red_flag_fields),
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND306_CASE_CANDIDATES: tuple[Round306CaseCandidate, ...] = (
    Round306CaseCandidate(
        case_id="r11_loop15_hanwha_aerospace_romania_k9",
        symbol="012450",
        company_name="Hanwha Aerospace",
        primary_archetype=E2RArchetype.DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE,
        secondary_archetypes=(E2RArchetype.DEFENSE_BACKLOG_DILUTION_OVERLAY,),
        case_type="success_candidate",
        round_case_type="Stage2_promote_candidate",
        best_trigger="T1/T2",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage_candidate="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage1_date=date(2022, 2, 24),
        stage2_date=date(2024, 7, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("signed_contract_value", "defense_backlog_growth", "record_high_reported", "global_howitzer_export_share"),
        red_flag_fields=("delivery_schedule_execution_missing", "gross_margin_missing", "cash_collection_missing", "share_sale_dilution_absorption_missing"),
        event_mfe_pct=5.0,
        event_mae_pct=None,
        extra_price_metrics={
            "contract_value_usd_bn": 1.0,
            "k9_howitzers_count": 54,
            "k10_resupply_vehicles_count": 36,
            "delivery_end": "2029-07",
            "defense_backlog_end_2021_krw_trn": 5.1,
            "defense_backlog_mar_2024_krw_trn": 30,
            "global_howitzer_export_share_pct": 50,
        },
        score_price_alignment="aligned",
        round_alignment_label="excellent_stage2_actionable",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        notes="Signed Romania K9 contract, backlog expansion and +5% record-high reaction make this Stage2-Actionable; Green still needs delivery, margin and cash collection.",
    ),
    Round306CaseCandidate(
        case_id="r11_loop15_hyundai_rotem_poland_k2",
        symbol="064350",
        company_name="Hyundai Rotem",
        primary_archetype=E2RArchetype.GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW,
        secondary_archetypes=(E2RArchetype.DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE,),
        case_type="success_candidate",
        round_case_type="Stage2_promote_candidate",
        best_trigger="T1/T3",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage_candidate="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage1_date=date(2022, 8, 26),
        stage2_date=date(2024, 4, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("k2_shipments_to_poland", "delivery_to_revenue_conversion", "q1_op_estimate_beat", "market_relative_price_reaction"),
        red_flag_fields=("multi_quarter_delivery_missing", "gross_margin_missing", "cash_collection_missing", "local_production_execution_pending"),
        event_mfe_pct=9.3,
        event_mae_pct=None,
        extra_price_metrics={
            "t1_price_krw": 41300,
            "kospi_same_context_pct": -0.3,
            "market_relative_return_pp": 9.6,
            "q1_op_estimate_krw_bn": 59.1,
            "q1_op_estimate_yoy_pct": 85,
            "q1_op_consensus_krw_bn": 44.4,
            "k2_shipments_to_poland_count": 18,
            "k2_poland_revenue_contribution_krw_bn": 270,
            "second_contract_tanks_count": 180,
            "second_contract_value_usd_bn": 6.5,
            "polish_local_production_count": 61,
        },
        score_price_alignment="aligned",
        round_alignment_label="excellent_stage2_actionable_delivery_trigger",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        notes="Delivery-to-revenue and OP estimate beat are stronger than a defense headline alone; Yellow needs multi-quarter margin and cash proof.",
    ),
    Round306CaseCandidate(
        case_id="r11_loop15_samsung_skhynix_us_china_export_curbs",
        symbol="005930/000660/067310/042700",
        company_name="Samsung Electronics / SK Hynix / Hana Micron / Hanmi Semiconductor",
        primary_archetype=E2RArchetype.CHIP_EXPORT_CONTROL_4C_WATCH,
        secondary_archetypes=(E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH, E2RArchetype.SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH),
        case_type="4c_thesis_break",
        round_case_type="4C-watch",
        best_trigger="T1/T2",
        best_trigger_type="4C-watch_trade_policy",
        stage_candidate="4C-watch",
        stage1_date=date(2022, 10, 7),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        hard_4c_confirmed=False,
        evidence_fields=("export_authorization_revoked", "china_output_exposure_quantified", "license_policy_mapped"),
        red_flag_fields=("china_fab_upgrade_ceiling", "stranded_capex_risk", "license_denial_4c_watch"),
        event_mfe_pct=None,
        event_mae_pct=-4.4,
        extra_price_metrics={
            "samsung_event_return_pct": -2.3,
            "sk_hynix_event_return_pct": -4.4,
            "kospi_same_context_pct": -0.7,
            "samsung_market_relative_pp": -1.6,
            "skhynix_market_relative_pp": -3.7,
            "samsung_china_dram_output_share": ">33%",
            "skhynix_china_dram_nand_output_share_pct": "30-40",
            "policy_effective_delay_days": 120,
        },
        score_price_alignment="aligned",
        round_alignment_label="trade_policy_4C_watch",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="Export-license revocation is a technology-upgrade ceiling and must be kept as a RedTeam/4C overlay, not growth evidence.",
    ),
    Round306CaseCandidate(
        case_id="r11_loop15_samsung_labor_strike_risk",
        symbol="005930",
        company_name="Samsung Electronics",
        primary_archetype=E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH,
        secondary_archetypes=(E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C,),
        case_type="4c_thesis_break",
        round_case_type="4C-watch",
        best_trigger="T1/T2/T3",
        best_trigger_type="4C-watch_labor_policy",
        stage_candidate="4C-watch",
        stage1_date=date(2024, 7, 8),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 15),
        hard_4c_confirmed=False,
        evidence_fields=("potential_strike_workers", "national_export_share", "dram_nand_supply_risk", "government_mediation"),
        red_flag_fields=("labor_output_disruption", "customer_delivery_risk", "chip_production_loss_estimate", "strike_4c_watch"),
        event_mfe_pct=None,
        event_mae_pct=-9.3,
        extra_price_metrics={
            "potential_strike_workers": ">50000",
            "semiconductors_share_of_exports_april_pct": 37,
            "strike_duration_days": 18,
            "potential_dram_supply_reduction_pct": 4,
            "potential_nand_supply_reduction_pct": 3,
            "potential_chip_production_loss_usd_bn": 19.9,
            "operating_loss_estimate_usd_bn": 20.79,
        },
        score_price_alignment="aligned",
        round_alignment_label="labor_policy_4C_watch",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="Samsung strike risk is not a normal wage headline; it can threaten memory supply, export output and customer delivery reliability.",
    ),
    Round306CaseCandidate(
        case_id="r11_loop15_martial_law_political_shock",
        symbol="KOSPI/EWY/005930_readthrough/broad_Korea_basket",
        company_name="Korea broad market / political shock reference",
        primary_archetype=E2RArchetype.POLITICAL_SYSTEM_SHOCK_MARKET_4C,
        secondary_archetypes=(E2RArchetype.POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE,),
        case_type="4c_thesis_break",
        round_case_type="hard_4c_false_break_relief",
        best_trigger="T0/T1",
        best_trigger_type="hard_4C_political_shock_with_false_break_relief",
        stage_candidate="4C",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2024, 12, 4),
        stage4c_date=date(2024, 12, 3),
        hard_4c_confirmed=True,
        evidence_fields=("martial_law_declaration", "parliament_vote_to_lift", "ETF_initial_drawdown", "macro_spillover"),
        red_flag_fields=("political_system_shock", "won_15y_low_context", "retail_sales_decline", "political_false_break_not_structural"),
        event_mfe_pct=None,
        event_mae_pct=-7.0,
        extra_price_metrics={
            "korea_etf_initial_mae_pct": -7.0,
            "korea_etf_trimmed_loss_pct": -1.7,
            "parliament_vote_to_lift": True,
            "order_lifted_within_hours": True,
            "dec_retail_sales_mom_pct": -0.6,
            "car_home_appliance_sales_mom_pct": -4.1,
            "entertainment_spending_mom_pct": -0.6,
        },
        score_price_alignment="aligned",
        round_alignment_label="hard_4C_false_break_relief",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="Martial-law shock is a hard political 4C; fast reversal is false-break relief, not a structural positive.",
    ),
    Round306CaseCandidate(
        case_id="r11_loop15_hormuz_energy_security_market_shock",
        symbol="KOSPI/005930/000660/005380/refiners_chemicals_basket",
        company_name="Korea broad market / energy security basket",
        primary_archetype=E2RArchetype.HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C, E2RArchetype.HORMUZ_POLICY_RELIEF_RESPONSE),
        case_type="4c_thesis_break",
        round_case_type="hard_4c_with_policy_relief",
        best_trigger="T0/T2",
        best_trigger_type="hard_4C_geopolitical_energy_shock_with_policy_relief",
        stage_candidate="4C + Stage2 relief",
        stage1_date=None,
        stage2_date=date(2026, 4, 15),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 3, 3),
        hard_4c_confirmed=True,
        evidence_fields=("energy_chokepoint_shock", "kospi_circuit_breaker_context", "alternative_crude_route", "alternative_naphtha_route"),
        red_flag_fields=("oil_import_dependency", "lng_import_dependency", "energy_supply_relief_not_growth", "macro_hard_4c"),
        event_mfe_pct=None,
        event_mae_pct=-12.0,
        extra_price_metrics={
            "kospi_event_mae_pct_range": "-7_to_-12",
            "samsung_marketwatch_event_return_pct": -9.88,
            "skhynix_marketwatch_event_return_pct": -11.5,
            "won_event_move_pct": -1.34,
            "kospi_barrons_event_return_pct": -6,
            "alternative_route_crude_secured_mn_barrels": 273,
            "alternative_route_naphtha_secured_mn_tons": 2.1,
            "normal_crude_coverage_months": 3,
            "normal_naphtha_coverage_months": 1,
        },
        score_price_alignment="aligned",
        round_alignment_label="hard_4C_with_policy_relief",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="Hormuz is hard geopolitical 4C; alternative supply routes are downside relief, not company EPS growth.",
    ),
    Round306CaseCandidate(
        case_id="r11_loop15_hanwha_ocean_us_naval_shipbuilding",
        symbol="042660/012450",
        company_name="Hanwha Ocean / Hanwha Aerospace",
        primary_archetype=E2RArchetype.NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B,
        secondary_archetypes=(E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION, E2RArchetype.DEFENSE_BACKLOG_DILUTION_4B),
        case_type="4b_watch",
        round_case_type="Stage2_policy_optionality_with_4B_overlay",
        best_trigger="T1/T2/T3",
        best_trigger_type="Stage2_geopolitical_optionality_with_4B_overlay",
        stage_candidate="Stage2 + 4B-watch",
        stage1_date=date(2024, 12, 19),
        stage2_date=date(2025, 12, 23),
        stage3_date=None,
        stage4b_date=date(2025, 4, 28),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("us_naval_shipbuilding_context", "philly_shipyard_context", "trump_frigate_comment", "nuclear_submarine_technology_sharing_claim"),
        red_flag_fields=("formal_US_Navy_contract_missing", "technology_transfer_terms_missing", "share_sale_dilution", "policy_premium_4b_watch"),
        event_mfe_pct=6.0,
        event_mae_pct=None,
        extra_price_metrics={
            "hanwha_ocean_2025_ytd_return_pct": 139,
            "trump_frigate_comment_event_return_pct": 6,
            "share_sale_hanwha_aerospace_krw_trn": 3.6,
            "share_sale_hanwha_aerospace_usd_bn": 2.5,
            "hanwha_aerospace_share_sale_event_return_pct": -13,
        },
        score_price_alignment="false_positive_score",
        round_alignment_label="Stage2_policy_optionality_with_4B_overlay",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        notes="U.S. naval optionality can be Stage2, but +139% YTD and dilution require 4B overlay until formal contract, tech transfer and margin close.",
    ),
    Round306CaseCandidate(
        case_id="r11_loop15_2025_korea_wildfires_disaster_reference",
        symbol="disaster_recovery_basket/insurers/construction/utilities_readthrough",
        company_name="2025 South Korea wildfire disaster reference",
        primary_archetype=E2RArchetype.NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE,
        secondary_archetypes=(E2RArchetype.NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE,),
        case_type="4c_thesis_break",
        round_case_type="disaster_reference_price_unavailable",
        best_trigger="T0/T1",
        best_trigger_type="disaster_reference_price_unavailable",
        stage_candidate="N/A_reference",
        stage1_date=date(2025, 3, 21),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 30),
        hard_4c_confirmed=True,
        evidence_fields=("reported_deaths", "burned_area", "structures_destroyed", "special_disaster_response"),
        red_flag_fields=("direct_krx_price_anchor_missing", "listed_equity_trigger_missing", "disaster_reference_not_equity_stage3"),
        event_mfe_pct=None,
        event_mae_pct=None,
        extra_price_metrics={
            "reported_deaths_reuters": 26,
            "reported_burned_area_hectares_reuters": 48000,
            "reported_structures_destroyed_reuters": 4000,
            "reported_deaths_ap": 28,
            "reported_injuries_ap": 37,
            "reported_displaced_people_ap": 30000,
            "reported_burned_area_acres_ap": 118265,
        },
        score_price_alignment="unknown",
        round_alignment_label="disaster_reference_not_equity_stage3",
        rerating_result="no_rerating",
        stage_failure_type="should_have_been_red",
        notes="Wildfire damage is a disaster hard-gate/reference row; no reliable direct KRX beneficiary trigger was found.",
    ),
)

ROUND306_TRIGGER_RECORDS: tuple[Round306TriggerRecord, ...] = (
    Round306TriggerRecord(
        "r11l15_hanwha_k9_romania_T1",
        "r11_loop15_hanwha_aerospace_romania_k9",
        "Stage2-Actionable",
        "2024-07-09",
        "$1B Romania K9 contract, 54 K9 howitzers, 36 K10 resupply vehicles, backlog 5.1T to 30T won, shares +5% to record high",
        5.0,
        "excellent_stage2_actionable",
        "Stage3-Yellow_candidate",
        {"contract_value_usd_bn": 1.0, "global_howitzer_export_share_pct": 50},
    ),
    Round306TriggerRecord(
        "r11l15_hyundai_rotem_poland_T1",
        "r11_loop15_hyundai_rotem_poland_k2",
        "Stage2-Actionable",
        "2024-04-09",
        "18 K2 shipments to Poland, Q1 OP estimate +85% YoY, shares +9.3% while KOSPI -0.3%",
        9.3,
        "excellent_stage2_actionable_delivery_trigger",
        "Stage3-Yellow_candidate",
        {"market_relative_return_pp": 9.6, "q1_op_estimate_krw_bn": 59.1},
    ),
    Round306TriggerRecord(
        "r11l15_chip_export_curbs_T1",
        "r11_loop15_samsung_skhynix_us_china_export_curbs",
        "4C-watch",
        "2025-09-01",
        "U.S. revokes equipment export authorizations for Samsung/SK Hynix China fabs; Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%",
        "Samsung -2.3 / SK Hynix -4.4",
        "trade_policy_4C_watch",
        "4C-watch",
        {"samsung_market_relative_pp": -1.6, "skhynix_market_relative_pp": -3.7},
    ),
    Round306TriggerRecord(
        "r11l15_samsung_strike_T2",
        "r11_loop15_samsung_labor_strike_risk",
        "4C-watch",
        "2026-05-15",
        "Samsung union sticks to 18-day strike plan; shares slide 9.3%; delivery reliability and supply disruption risk",
        -9.3,
        "labor_policy_4C_watch",
        "4C-watch",
        {"potential_dram_supply_reduction_pct": 4, "potential_nand_supply_reduction_pct": 3},
    ),
    Round306TriggerRecord(
        "r11l15_martial_law_T0",
        "r11_loop15_martial_law_political_shock",
        "hard_4C",
        "2024-12-03",
        "Martial law declaration triggers Korea ETF initial -7% drop and broad Korean asset stress",
        -7.0,
        "hard_4c_political_shock",
        "4C",
        {"korea_etf_initial_mae_pct": -7.0},
    ),
    Round306TriggerRecord(
        "r11l15_martial_law_T1",
        "r11_loop15_martial_law_political_shock",
        "false_break_relief",
        "2024-12-04",
        "Parliament overturns martial law and order is lifted; ETF loss trimmed to about -1.7%",
        -1.7,
        "false_break_relief",
        "4C-watch_relief",
        {"parliament_vote_to_lift": True, "order_lifted_within_hours": True},
    ),
    Round306TriggerRecord(
        "r11l15_hormuz_T0",
        "r11_loop15_hormuz_energy_security_market_shock",
        "hard_4C",
        "2026-03-03/2026-03-09",
        "Hormuz/Middle East oil shock triggers KOSPI circuit-breaker selloff; Samsung/SK Hynix/Hyundai sharply down",
        "KOSPI -6_to_-12 / Samsung -7.8_to_-9.88 / SKH -9.5_to_-11.5 / Hyundai -8.3",
        "hard_4c_geopolitical_energy",
        "4C",
        {"kospi_event_mae_pct_range": "-7_to_-12"},
    ),
    Round306TriggerRecord(
        "r11l15_hormuz_T2",
        "r11_loop15_hormuz_energy_security_market_shock",
        "Stage2_relief",
        "2026-04-15",
        "Korea secures 273M barrels crude and 2.1M tons naphtha through routes outside Hormuz",
        "price_data_unavailable_after_deep_search",
        "policy_relief_not_growth",
        "Stage2_relief",
        {"alternative_route_crude_secured_mn_barrels": 273, "alternative_route_naphtha_secured_mn_tons": 2.1},
    ),
    Round306TriggerRecord(
        "r11l15_hanwha_ocean_T2",
        "r11_loop15_hanwha_ocean_us_naval_shipbuilding",
        "Stage2_policy_optionality",
        "2025-12-23",
        "Hanwha Ocean shares +6% after Trump comments on building U.S. frigates",
        6.0,
        "Stage2_policy_optionality_with_4B",
        "Stage2-Actionable",
        {"hanwha_ocean_2025_ytd_return_pct": 139},
    ),
    Round306TriggerRecord(
        "r11l15_wildfire_T1",
        "r11_loop15_2025_korea_wildfires_disaster_reference",
        "disaster_reference",
        "2025-03-30",
        "Korea's largest wildfire killed at least 26, burned 48k hectares and destroyed around 4k structures; no direct KRX price trigger found",
        "price_data_unavailable_after_deep_search",
        "disaster_reference_not_equity_stage3",
        "N/A_reference",
        {"reported_deaths_reuters": 26, "reported_burned_area_hectares_reuters": 48000},
    ),
)

ROUND306_SHADOW_WEIGHT_ROWS: tuple[Round306ShadowWeightRow, ...] = (
    Round306ShadowWeightRow(E2RArchetype.DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE, 5, 4, 5, 4, 1, 0, 1, 1, 0, 0, -5, -4, -4, -2, "signed contract+backlog+price reaction", "delivery/margin pending", "delivery+margin+cash collection", "Hanwha Aerospace Romania K9."),
    Round306ShadowWeightRow(E2RArchetype.GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW, 5, 5, 4, 5, 1, 0, 1, 1, 0, 0, -4, -3, -3, -2, "shipments+revenue+OP estimate", "local production/margin pending", "multi-quarter delivery+margin", "Hyundai Rotem Poland K2."),
    Round306ShadowWeightRow(E2RArchetype.CHIP_EXPORT_CONTROL_4C_WATCH, 0, 0, 0, 0, 5, 0, 2, 1, 1, 0, -1, -1, -1, -2, "license revocation", "relief annual license pending", "China fab upgrade stability", "Samsung/SK Hynix export curbs."),
    Round306ShadowWeightRow(E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH, 0, 0, 0, 0, 2, 5, 2, 1, 0, 0, -1, -1, -1, -2, "strike threat", "settlement/output loss pending", "production stability", "Samsung strike risk."),
    Round306ShadowWeightRow(E2RArchetype.POLITICAL_SYSTEM_SHOCK_MARKET_4C, 0, 0, 0, 0, 1, 1, 5, 2, 1, 1, -1, -1, -1, -4, "political shock", "order reversal/continuity pending", "stability restored", "Martial-law shock."),
    Round306ShadowWeightRow(E2RArchetype.HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF, 0, 0, 0, 0, 1, 0, 2, 5, 4, 1, -1, -1, -1, -5, "energy chokepoint shock", "alternative routes pending", "supply stabilized", "Hormuz energy crisis."),
    Round306ShadowWeightRow(E2RArchetype.NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B, 4, 3, 3, 5, 2, 0, 2, 2, 0, 0, -5, -4, -4, -2, "naval policy optionality", "formal contract/tech transfer pending", "Navy contract+shipyard margin", "Hanwha Ocean U.S. naval."),
    Round306ShadowWeightRow(E2RArchetype.NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE, 0, 0, 0, 0, 0, 0, 2, 1, 2, 5, -1, -1, -1, -3, "disaster and recovery", "listed equity trigger missing", "N/A", "Wildfire reference only."),
)


def round306_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND306_CASE_CANDIDATES]


def round306_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND306_CASE_CANDIDATES]


def round306_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND306_TRIGGER_RECORDS]


def round306_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND306_SHADOW_WEIGHT_ROWS]


def round306_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND306_REQUIRED_TARGET_ALIASES.items()]


def round306_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND306_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND306_SCORE_DOWN_AXES]
    )


def round306_summary() -> dict[str, object]:
    return {
        "source_round": ROUND306_SOURCE_ROUND_PATH,
        "round_id": ROUND306_ANALYST_ROUND_ID,
        "large_sector": ROUND306_LARGE_SECTOR,
        "method": ROUND306_METHOD,
        "case_candidate_count": len(ROUND306_CASE_CANDIDATES),
        "trigger_count": len(ROUND306_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND306_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 3,
        "stage3_yellow_candidate_count": 3,
        "stage3_green_confirmed_count": 0,
        "stage2_relief_count": 1,
        "stage4b_watch_count": 2,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 3,
        "disaster_reference_count": 1,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round306_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND306_SOURCE_ROUND_PATH,
        "round_id": ROUND306_ANALYST_ROUND_ID,
        "large_sector": ROUND306_LARGE_SECTOR,
        "method": ROUND306_METHOD,
        "summary": round306_summary(),
        "required_target_aliases": dict(ROUND306_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND306_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND306_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND306_STAGE3_GREEN_RULES,
        "green_blockers": ROUND306_GREEN_BLOCKERS,
        "score_up_axes": ROUND306_SCORE_UP_AXES,
        "score_down_axes": ROUND306_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND306_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND306_HARD_4C_GATES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round306_cases_as_candidate_generation_input",
            "do_not_treat_policy_geopolitics_or_disaster_headline_as_green",
            "do_not_treat_energy_or_political_relief_as_growth",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round306_summary_markdown() -> str:
    summary = round306_summary()
    lines = [
        "# R11 Loop 15 Policy / Geopolitics / Disaster Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: `Hyundai Rotem` was stronger than a defense headline because shipments, revenue contribution, OP estimate beat and +9.3% price reaction connected. `Hormuz` alternative crude routing is different: it is relief after a hard 4C shock, not growth.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Stage2-Actionable: Hanwha Aerospace Romania K9, Hyundai Rotem Poland K2, Hanwha Ocean U.S. naval optionality.",
            "- Stage3-Yellow candidates: defense cases where delivery, margin and cash collection still need confirmation.",
            "- Hard 4C / watch: chip export controls, semiconductor labor strike, martial-law shock, Hormuz energy shock and wildfire disaster reference.",
            "- Stage3-Green confirmed: `0`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round306_trigger_grid_markdown() -> str:
    lines = [
        "# Round 306 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round306_trigger_rows():
        lines.append(
            f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |"
        )
    return "\n".join(lines) + "\n"


def render_round306_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 306 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND306_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND306_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND306_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND306_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND306_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round306_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 306 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND306_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C / Watch Cases",
    ]
    for case in ROUND306_CASE_CANDIDATES:
        if case.stage4c_date or case.stage4b_date or "4C" in case.stage_candidate:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round306_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 306 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event return, market-relative return, policy amount and damage anchors are retained without inventing MFE/MAE.",
        "",
    ]
    for case in ROUND306_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def write_round306_r11_loop15_reports(
    output_directory: str | Path = ROUND306_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND306_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND306_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND306_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND306_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round306_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND306_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round306_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round306_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round306_r11_loop15_case_matrix.csv",
        "target_aliases": output_dir / "round306_r11_loop15_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round306_r11_loop15_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round306_r11_loop15_trigger_grid.md",
        "summary": output_dir / "round306_r11_loop15_trigger_validation_summary.md",
        "stage_rules": output_dir / "round306_r11_loop15_stage_rules.md",
        "stage4b_4c_review": output_dir / "round306_r11_loop15_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round306_r11_loop15_score_adjustments.csv",
        "shadow_weights": output_dir / "round306_r11_loop15_shadow_weights.csv",
        "price_validation_plan": output_dir / "round306_r11_loop15_price_validation_plan.md",
    }

    _write_csv(paths["case_matrix"], round306_case_rows())
    _write_csv(paths["target_aliases"], round306_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round306_trigger_rows())
    _write_csv(paths["score_adjustments"], round306_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round306_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round306_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round306_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round306_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round306_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round306_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def _write_csv(path: Path, rows: Iterable[Mapping[str, str]]) -> None:
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_jsonl(path: Path, rows: Iterable[Mapping[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _signed(value: int) -> str:
    return f"{value:+d}" if value else "+0"


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    return str(value)


def _bullet_lines(items: Iterable[str]) -> list[str]:
    return [f"- {item}" for item in items]
