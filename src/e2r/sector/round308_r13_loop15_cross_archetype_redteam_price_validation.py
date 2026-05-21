"""Round-308 R13 Loop-15 cross-archetype RedTeam validation pack.

This module converts ``docs/round/round_308.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: Samyang's ASP, shipment, capacity, OP-estimate and price reaction
can justify Stage2-Actionable / Yellow-candidate review. Jensen Huang eating at
an unlisted restaurant cannot justify Stage3 for listed chicken peers because no
direct revenue bridge exists.
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


ROUND308_SOURCE_ROUND_PATH = "docs/round/round_308.md"
ROUND308_ANALYST_ROUND_ID = "round_236"
ROUND308_LARGE_SECTOR = "CROSS_ARCHETYPE_REDTEAM"
ROUND308_METHOD = "trigger_level_backtest_v1_redteam"
ROUND308_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round308_r13_loop15_cross_archetype_redteam_price_validation"
ROUND308_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r13_loop15_round236.jsonl"
ROUND308_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r13_loop15_round236.jsonl"
ROUND308_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round308_r13_loop15_cross_archetype_redteam_price_validation_audit.json"
ROUND308_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round236_r13_loop15_v1.csv"

ROUND308_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "EARLY_EVIDENCE_MISSED_STRUCTURAL": E2RArchetype.EARLY_EVIDENCE_MISSED_STRUCTURAL.value,
    "DELIVERY_TO_REVENUE_STAGE2_YELLOW": E2RArchetype.DELIVERY_TO_REVENUE_STAGE2_YELLOW.value,
    "STRATEGIC_CAPITAL_WITH_DILUTION_4B": E2RArchetype.STRATEGIC_CAPITAL_WITH_DILUTION_4B.value,
    "CONTROL_BATTLE_GOVERNANCE_4B_4C": E2RArchetype.CONTROL_BATTLE_GOVERNANCE_4B_4C.value,
    "EVIDENCE_GOOD_BUT_PRICE_FAILED": E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED.value,
    "PLATFORM_SECURITY_HARD_4C": E2RArchetype.PLATFORM_SECURITY_HARD_4C.value,
    "OPERATIONAL_SAFETY_HARD_4C": E2RArchetype.OPERATIONAL_SAFETY_HARD_4C.value,
    "PRICE_MOVED_WITHOUT_EVIDENCE": E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE.value,
    "POLICY_THEME_OVERHEAT_4B": E2RArchetype.POLICY_THEME_OVERHEAT_4B.value,
    "OHLC_BACKFILL_SEPARATION_REQUIRED": E2RArchetype.OHLC_BACKFILL_SEPARATION_REQUIRED.value,
}

ROUND308_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "OP_EPS_FCF_estimate_revision_exists",
    "two_or_more_of_shipment_delivery_ASP_capacity_contract_value_close_together",
    "event_return_at_least_5pct",
    "market_relative_return_at_least_5pp",
    "evidence_has_revenue_or_margin_bridge_not_only_narrative",
    "evidence_publicly_available_on_trigger_date",
    "no_hard_4c_overlay",
)

ROUND308_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "only_one_core_gate_remains_open",
    "delivery_or_shipment_to_revenue_bridge_is_explicit",
    "price_reaction_agrees_with_evidence_or_disagreement_is_explained",
)

ROUND308_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "full_OHLC_backfill_supports_entry",
    "actual_earnings_or_cashflow_confirms_the_bridge",
    "4B_overlay_is_cleared_or_contained",
    "hard_4c_gate_absent",
    "no_below_entry_break_in_key_validation_window",
)

ROUND308_GREEN_BLOCKERS: tuple[str, ...] = (
    "CB_dilution_or_conversion_risk_unresolved",
    "control_premium_without_operating_EPS_FCF_change",
    "evidence_good_but_price_failed",
    "platform_security_or_customer_data_breach",
    "fatal_operational_safety_incident",
    "celebrity_or_meme_event_without_direct_revenue",
    "policy_theme_without_license_contract_or_revenue",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND308_SCORE_UP_AXES: tuple[str, ...] = (
    "evidence_to_earnings_bridge",
    "market_relative_event_strength",
    "delivery_to_revenue_conversion",
    "actual_capacity_or_shipment",
    "platform_security_trust",
    "operational_safety_trust",
    "governance_dilution_quality",
    "price_evidence_disagreement",
)

ROUND308_SCORE_DOWN_AXES: tuple[str, ...] = (
    "headline_only_score",
    "policy_theme_without_revenue",
    "control_premium_as_rerating",
    "CB_capital_without_backlog",
    "celebrity_meme_event",
    "IPO_pop_without_durability",
    "platform_scale_without_security",
)

ROUND308_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "strategic_capital_or_CB_rally_before_backlog_and_dilution_clear",
    "control_premium_priced_as_operating_rerating",
    "IPO_or_AI_cloud_story_before_aftermarket_and_margin_validation",
    "celebrity_or_policy_price_spike_before_revenue_bridge",
    "full_OHLC_backfill_missing_after_large_event_anchor",
)

ROUND308_HARD_4C_GATES: tuple[str, ...] = (
    "customer_data_breach_or_platform_security_failure",
    "fatal_safety_accident_or_nationwide_safety_inspection",
    "regulator_intervention_after_governance_or_dilution_event",
    "accounting_or_disclosure_control_failure",
    "revenue_forecast_cut_from_trust_or_security_incident",
)

ROUND308_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_what_happened_and_stage_candidate",
    "trigger_calibration_row_stores_entry_anchor_and_reported_event_return",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
)


@dataclass(frozen=True)
class Round308ShadowWeightRow:
    archetype: E2RArchetype
    evidence_to_earnings_bridge: int
    market_relative_event_strength: int
    delivery_to_revenue_conversion: int
    actual_capacity_or_shipment: int
    platform_security_trust: int
    operational_safety_trust: int
    governance_dilution_quality: int
    price_evidence_disagreement: int
    headline_only_penalty: int
    control_premium_as_rerating_penalty: int
    cb_capital_without_backlog_penalty: int
    celebrity_meme_event_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "evidence_to_earnings_bridge": _signed(self.evidence_to_earnings_bridge),
            "market_relative_event_strength": _signed(self.market_relative_event_strength),
            "delivery_to_revenue_conversion": _signed(self.delivery_to_revenue_conversion),
            "actual_capacity_or_shipment": _signed(self.actual_capacity_or_shipment),
            "platform_security_trust": _signed(self.platform_security_trust),
            "operational_safety_trust": _signed(self.operational_safety_trust),
            "governance_dilution_quality": _signed(self.governance_dilution_quality),
            "price_evidence_disagreement": _signed(self.price_evidence_disagreement),
            "headline_only_penalty": _signed(self.headline_only_penalty),
            "control_premium_as_rerating_penalty": _signed(self.control_premium_as_rerating_penalty),
            "cb_capital_without_backlog_penalty": _signed(self.cb_capital_without_backlog_penalty),
            "celebrity_meme_event_penalty": _signed(self.celebrity_meme_event_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round308TriggerRecord:
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
class Round308CaseCandidate:
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
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
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
            "do_not_use_round308_cases_as_candidate_generation_input",
            "do_not_treat_headline_control_premium_cb_meme_security_or_safety_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND308_LARGE_SECTOR,
            large_sector=ROUND308_LARGE_SECTOR,
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
            stage1_evidence=self.evidence_fields,
            stage2_evidence=self.evidence_fields if self.stage2_date else (),
            stage3_evidence=(),
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4b" in field or "premium" in field or "dilution" in field),
            stage4c_evidence=tuple(field for field in (*self.red_flag_fields, *self.evidence_fields) if "4c" in field or "breach" in field or "fatal" in field or "regulator" in field),
            must_have_fields=ROUND308_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "4c_thesis_break", "failed_rerating"} else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern="reported_event_anchor_only",
            score_weight_hint={},
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                stage1_price=self.stage1_price_anchor,
                stage2_price=self.stage2_price_anchor,
                stage4b_price=self.stage4b_price_anchor,
                stage4c_price=self.stage4c_price_anchor,
                mfe_30d=self.event_mfe_pct,
                mae_30d=self.event_mae_pct,
                price_validation_status="price_data_unavailable_after_deep_search",
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.74 if not self.hard_4c_confirmed else 0.86,
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
            "stage1_price_anchor": _value_text(self.stage1_price_anchor),
            "stage2_price_anchor": _value_text(self.stage2_price_anchor),
            "stage4b_price_anchor": _value_text(self.stage4b_price_anchor),
            "stage4c_price_anchor": _value_text(self.stage4c_price_anchor),
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND308_CASE_CANDIDATES: tuple[Round308CaseCandidate, ...] = (
    Round308CaseCandidate(
        case_id="r13_loop15_redteam_samyang_buldak_missed_structural",
        symbol="003230",
        company_name="Samyang Foods",
        primary_archetype=E2RArchetype.EARLY_EVIDENCE_MISSED_STRUCTURAL,
        secondary_archetypes=(E2RArchetype.EXPORT_RECURRING_CONSUMER, E2RArchetype.STAGE2_STRONG_NOT_GREEN),
        case_type="success_candidate",
        round_case_type="missed_structural_stage2_actionable_yellow_candidate",
        best_trigger="r13_samyang_T1",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage_candidate="Stage2-Actionable / Stage3-Yellow candidate",
        stage1_date=date(2024, 6, 14),
        stage2_date=date(2024, 6, 14),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("op_estimate_81_2bn_krw", "op_estimate_yoy_84pct", "Buldak_ASP_increase", "US_Europe_shipment_increase", "production_capacity_expansion", "event_return_5_7pct"),
        red_flag_fields=("reported_earnings_confirmation_pending", "full_ohlc_backfill_missing"),
        event_mfe_pct=5.7,
        event_mae_pct=None,
        stage1_price_anchor=647000,
        stage2_price_anchor=647000,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"entry_price_anchor_krw": 647000, "event_return_pct": 5.7, "target_price_krw": 830000, "target_price_raise_pct": 26, "op_estimate_krw_bn": 81.2, "op_estimate_yoy_pct": 84},
        score_price_alignment="missed_due_to_score",
        round_alignment_label="missed_structural_if_old_stage2_gate_used",
        rerating_result="true_rerating",
        stage_failure_type="missed_structural",
        notes="ASP, shipment, capacity, OP-estimate revision and price reaction should promote plain Stage2 into Actionable / Yellow-candidate review.",
    ),
    Round308CaseCandidate(
        case_id="r13_loop15_redteam_hyundai_rotem_k2_delivery",
        symbol="064350",
        company_name="Hyundai Rotem",
        primary_archetype=E2RArchetype.DELIVERY_TO_REVENUE_STAGE2_YELLOW,
        secondary_archetypes=(E2RArchetype.GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW, E2RArchetype.DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE),
        case_type="success_candidate",
        round_case_type="delivery_to_revenue_stage2_actionable_yellow_candidate",
        best_trigger="r13_rotem_T1",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage_candidate="Stage2-Actionable / Stage3-Yellow candidate",
        stage1_date=date(2024, 4, 9),
        stage2_date=date(2024, 4, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("k2_shipments_to_poland_18", "revenue_contribution_270bn_krw", "q1_op_estimate_59_1bn_krw", "q1_op_estimate_yoy_85pct", "consensus_44_4bn_krw", "market_relative_9_6pp"),
        red_flag_fields=("multi_quarter_margin_cash_collection_pending", "full_ohlc_backfill_missing"),
        event_mfe_pct=9.3,
        event_mae_pct=None,
        stage1_price_anchor=41300,
        stage2_price_anchor=41300,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"entry_price_anchor_krw": 41300, "event_return_pct": 9.3, "kospi_same_context_pct": -0.3, "market_relative_return_pp": 9.6, "k2_shipments_to_poland_count": 18, "k2_revenue_contribution_krw_bn": 270, "q1_op_estimate_krw_bn": 59.1, "q1_op_estimate_yoy_pct": 85, "q1_op_consensus_krw_bn": 44.4},
        score_price_alignment="aligned",
        round_alignment_label="excellent_delivery_to_revenue_entry",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        notes="Delivery plus revenue contribution and OP estimate beat is stronger than a simple defense contract headline.",
    ),
    Round308CaseCandidate(
        case_id="r13_loop15_redteam_samsung_sds_kkr_cb",
        symbol="018260",
        company_name="Samsung SDS",
        primary_archetype=E2RArchetype.STRATEGIC_CAPITAL_WITH_DILUTION_4B,
        secondary_archetypes=(E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM, E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY),
        case_type="4b_watch",
        round_case_type="stage2_actionable_with_cb_dilution_4b_overlay",
        best_trigger="r13_sds_T1",
        best_trigger_type="Stage2-Actionable_plus_4B",
        stage_candidate="Stage2-Actionable + 4B-watch",
        stage1_date=date(2026, 4, 15),
        stage2_date=date(2026, 4, 15),
        stage3_date=None,
        stage4b_date=date(2026, 4, 15),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("kkr_strategic_capital", "convertible_bond_820mn_usd", "ma_advisory", "ai_offerings_expansion", "physical_ai", "stablecoin_ambition", "cash_6_4tn_krw"),
        red_flag_fields=("CB_dilution", "conversion_risk", "enterprise_AI_backlog_missing", "strategy_execution_risk", "4b_overlay_required"),
        event_mfe_pct=20.8,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"convertible_bond_value_usd_mn": 820, "event_mfe_pct": 20.8, "morning_return_pct": 19.4, "kospi_same_context_pct": 3.0, "market_relative_return_pp": 17.8, "cash_and_equivalents_krw_trn": 6.4},
        score_price_alignment="false_positive_score",
        round_alignment_label="Stage2_promote_candidate_with_4B_overlay",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        notes="Strategic capital is actionable, but CB dilution, conversion risk and backlog gaps block Green.",
    ),
    Round308CaseCandidate(
        case_id="r13_loop15_redteam_korea_zinc_control_battle",
        symbol="010130",
        company_name="Korea Zinc",
        primary_archetype=E2RArchetype.CONTROL_BATTLE_GOVERNANCE_4B_4C,
        secondary_archetypes=(E2RArchetype.CONTROL_PREMIUM_DILUTION_4B, E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE),
        case_type="4b_watch",
        round_case_type="control_premium_then_governance_dilution_4b_4c",
        best_trigger="r13_koreazinc_T1_T2",
        best_trigger_type="control_premium_then_governance_4B_4C",
        stage_candidate="4B-watch / 4C-watch",
        stage1_date=date(2024, 9, 13),
        stage2_date=date(2024, 9, 13),
        stage3_date=None,
        stage4b_date=date(2024, 9, 13),
        stage4c_date=date(2024, 11, 6),
        hard_4c_confirmed=False,
        evidence_fields=("tender_offer_660000_krw", "pre_offer_close_556000_krw", "korea_zinc_event_return_19_8pct", "young_poong_event_return_30pct", "tender_offer_value_2tn_krw"),
        red_flag_fields=("control_battle", "defensive_share_issuance", "dilution", "FSS_revision_order", "governance_uncertainty", "share_sale_event_minus_8pct"),
        event_mfe_pct=19.8,
        event_mae_pct=-8.0,
        stage1_price_anchor=556000,
        stage2_price_anchor=660000,
        stage4b_price_anchor=660000,
        stage4c_price_anchor=None,
        extra_price_metrics={"tender_offer_price_krw": 660000, "pre_offer_close_krw": 556000, "korea_zinc_event_return_pct": 19.8, "young_poong_event_return_pct": 30, "tender_offer_value_krw_trn": 2.0, "tender_offer_value_usd_bn": 1.5, "share_sale_plan_usd_bn": 1.8, "share_sale_event_mae_pct": -8, "fss_revision_order": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="control_premium_not_stage3_green",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        notes="Control premium is not operating EPS/FCF rerating; defensive issuance and regulator intervention create governance 4B/4C.",
    ),
    Round308CaseCandidate(
        case_id="r13_loop15_redteam_lg_cns_evidence_price_fail",
        symbol="LG_CNS",
        company_name="LG CNS",
        primary_archetype=E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED,
        secondary_archetypes=(E2RArchetype.AI_CLOUD_IPO_FALSE_POSITIVE, E2RArchetype.IPO_EVENT_PREMIUM),
        case_type="failed_rerating",
        round_case_type="evidence_good_but_price_failed",
        best_trigger="r13_lgcns_T1",
        best_trigger_type="evidence_good_but_price_failed",
        stage_candidate="Stage2 only / Green blocked",
        stage1_date=date(2025, 2, 5),
        stage2_date=date(2025, 2, 5),
        stage3_date=None,
        stage4b_date=date(2025, 2, 5),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("cloud_ai_sales_share_54pct", "ipo_raise_1_2tn_krw", "revenue_4_0tn_krw", "op_313bn_krw"),
        red_flag_fields=("debut_below_issue_price", "aftermarket_demand_failed", "price_evidence_disagreement"),
        event_mfe_pct=None,
        event_mae_pct=-3.55,
        stage1_price_anchor=61900,
        stage2_price_anchor=59700,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_issue_price_krw": 61900, "debut_open_price_krw": 60500, "debut_last_reported_price_krw": 59700, "debut_return_vs_issue_pct": -3.55, "ipo_raise_krw_trn": 1.2, "cloud_ai_sales_share_3q2024_pct": 54, "revenue_3q2024_krw_trn": 4.0, "op_3q2024_krw_bn": 313},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        stage_failure_type="false_yellow",
        notes="Good cloud/AI evidence cannot create Green when the IPO trades below issue price at the trigger.",
    ),
    Round308CaseCandidate(
        case_id="r13_loop15_redteam_platform_security_4c",
        symbol="017670/CPNG_reference",
        company_name="SK Telecom / Coupang",
        primary_archetype=E2RArchetype.PLATFORM_SECURITY_HARD_4C,
        secondary_archetypes=(E2RArchetype.DATA_TRUST_HARD_4C, E2RArchetype.ECOMMERCE_DATA_BREACH_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="platform_security_hard_4c",
        best_trigger="r13_security_T1",
        best_trigger_type="hard_4C_security",
        stage_candidate="4C",
        stage1_date=date(2025, 7, 4),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 7, 4),
        hard_4c_confirmed=True,
        evidence_fields=("skt_data_pieces_leaked_26_96mn", "skt_event_return_minus_5_6pct", "skt_security_investment_700bn_krw", "skt_revenue_forecast_cut_800bn_krw", "coupang_affected_accounts_33_7mn"),
        red_flag_fields=("customer_data_leak", "regulator_finding", "compensation_cost", "revenue_forecast_cut", "trust_damage", "hard_4c_security"),
        event_mfe_pct=None,
        event_mae_pct=-5.6,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"skt_data_pieces_leaked_mn": 26.96, "skt_event_return_pct": -5.6, "skt_security_investment_5y_krw_bn": 700, "skt_revenue_forecast_cut_2025_krw_bn": 800, "skt_august_subscription_discount_pct": 50, "coupang_affected_accounts_mn": 33.7, "coupang_premarket_event_return_pct": -4.4},
        score_price_alignment="aligned",
        round_alignment_label="hard_4c_success_platform_security",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="Platform scale without security turns customer base into damage multiplier; data breach is hard 4C.",
    ),
    Round308CaseCandidate(
        case_id="r13_loop15_redteam_jeju_air_safety_4c",
        symbol="089590",
        company_name="Jeju Air",
        primary_archetype=E2RArchetype.OPERATIONAL_SAFETY_HARD_4C,
        secondary_archetypes=(E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C, E2RArchetype.AIRLINE_SAFETY_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="operational_safety_hard_4c",
        best_trigger="r13_jejuair_T1",
        best_trigger_type="hard_4C_operational_safety",
        stage_candidate="4C",
        stage1_date=date(2024, 12, 30),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 30),
        hard_4c_confirmed=True,
        evidence_fields=("fatalities_179", "intraday_mae_minus_15_7pct", "intraday_low_6920_krw", "market_cap_loss_95_7bn_krw", "safety_inspection_ordered"),
        red_flag_fields=("fatal_safety_accident", "consumer_trust_collapse", "emergency_safety_inspection", "hard_4c_operational_safety"),
        event_mfe_pct=None,
        event_mae_pct=-15.7,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=6920,
        extra_price_metrics={"fatalities": 179, "intraday_mae_pct": -15.7, "intraday_low_krw": 6920, "reported_midday_return_pct": -8.5, "market_cap_loss_krw_bn": 95.7, "ak_holdings_intraday_mae_pct": -12, "safety_inspection_ordered": True},
        score_price_alignment="aligned",
        round_alignment_label="hard_4c_success_operational_safety",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="Fatal safety incident outranks airline demand, yield or reopening triggers.",
    ),
    Round308CaseCandidate(
        case_id="r13_loop15_redteam_jensen_chicken_meme",
        symbol="339770/066360/348340",
        company_name="Kyochon F&B / Cherrybro / Neuromeka",
        primary_archetype=E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE,
        secondary_archetypes=(E2RArchetype.FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE, E2RArchetype.FRIED_CHICKEN_MEME_EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="price_moved_without_evidence",
        best_trigger="r13_chicken_T1",
        best_trigger_type="price_moved_without_evidence",
        stage_candidate="N/A no valid Stage3",
        stage1_date=date(2025, 10, 31),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 10, 31),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("celebrity_dinner_context", "unlisted_kkanbu_chicken", "listed_peer_price_move", "nvidia_korea_ai_chip_deals_260000_units"),
        red_flag_fields=("direct_revenue_link_false", "equity_purchase_false", "same_store_sales_false", "franchise_fee_false", "celebrity_meme_event"),
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kkanbu_listed": False, "nvidia_korea_ai_chip_deals_units": 260000, "direct_revenue_link_confirmed": False, "equity_purchase_confirmed": False, "same_store_sales_confirmed": False, "franchise_fee_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_green",
        notes="Celebrity meme rally without direct revenue evidence is separated from Stage scoring.",
    ),
)


ROUND308_TRIGGER_RECORDS: tuple[Round308TriggerRecord, ...] = (
    Round308TriggerRecord("r13_samyang_T1", "r13_loop15_redteam_samyang_buldak_missed_structural", "Stage2-Actionable_to_Stage3-Yellow_candidate", "2024-06-14", "OP estimate KRW81.2B +84% YoY, Buldak ASP increase, U.S./Europe shipment growth, capacity expansion, shares +5.7%", 5.7, "missed_structural_if_old_gate_used", "Stage3-Yellow_candidate", {"entry_price_krw": 647000, "target_price_krw": 830000}),
    Round308TriggerRecord("r13_rotem_T1", "r13_loop15_redteam_hyundai_rotem_k2_delivery", "Stage2-Actionable_to_Stage3-Yellow_candidate", "2024-04-09", "18 K2 tanks shipped to Poland, KRW270B revenue contribution, Q1 OP estimate +85%, shares +9.3%, KOSPI -0.3%", 9.3, "excellent_delivery_to_revenue_entry", "Stage3-Yellow_candidate", {"entry_price_krw": 41300, "market_relative_return_pp": 9.6}),
    Round308TriggerRecord("r13_sds_T1", "r13_loop15_redteam_samsung_sds_kkr_cb", "Stage2-Actionable_plus_4B", "2026-04-15", "KKR buys $820M Samsung SDS CB, shares +20.8%, KKR to advise on M&A/capital allocation/AI offerings", 20.8, "Stage2_Actionable_with_required_4B_overlay", "Stage2-Actionable+4B", {"convertible_bond_value_usd_mn": 820, "market_relative_return_pp": 17.8}),
    Round308TriggerRecord("r13_koreazinc_T1", "r13_loop15_redteam_korea_zinc_control_battle", "control_premium_4B", "2024-09-13", "MBK/Young Poong tender offer at KRW660,000; Korea Zinc +19.8%, Young Poong +30%", 19.8, "control_premium_not_operating_rerating", "4B-watch", {"tender_offer_price_krw": 660000, "pre_offer_close_krw": 556000}),
    Round308TriggerRecord("r13_koreazinc_T2", "r13_loop15_redteam_korea_zinc_control_battle", "governance_dilution_4C_watch", "2024-11-06", "FSS revision order on Korea Zinc $1.8B share sale plan; shares fell as much as 8%", -8.0, "governance_dilution_4C_watch", "4C-watch", {"share_sale_plan_usd_bn": 1.8, "fss_revision_order": True}),
    Round308TriggerRecord("r13_lgcns_T1", "r13_loop15_redteam_lg_cns_evidence_price_fail", "evidence_good_but_price_failed", "2025-02-05", "Cloud/AI 54% sales, IPO raised 1.2T won, but debut traded at 59,700 below 61,900 issue price", -3.55, "evidence_good_but_price_failed", "Stage2_only", {"ipo_issue_price_krw": 61900, "debut_last_reported_price_krw": 59700}),
    Round308TriggerRecord("r13_security_T1", "r13_loop15_redteam_platform_security_4c", "hard_4C_security", "2025-07-04/2025-12-01", "SKT negligent data leak, -5.6%, 26.96M data pieces; Coupang 33.7M accounts, -4.4% premarket", "SKT -5.6 / Coupang -4.4", "hard_4C_success", "4C", {"skt_data_pieces_leaked_mn": 26.96, "coupang_affected_accounts_mn": 33.7}),
    Round308TriggerRecord("r13_jejuair_T1", "r13_loop15_redteam_jeju_air_safety_4c", "hard_4C_operational_safety", "2024-12-30", "Jeju Air crash killed 179; shares fell as much as 15.7% to KRW6,920; market cap loss 95.7B won", -15.7, "hard_4C_success", "4C", {"fatalities": 179, "intraday_low_krw": 6920}),
    Round308TriggerRecord("r13_chicken_T1", "r13_loop15_redteam_jensen_chicken_meme", "price_moved_without_evidence", "2025-10-31", "Jensen Huang dined at non-listed Kkanbu Chicken; listed chicken/robot names surged without direct revenue or equity purchase", "no_valid_stage3_entry", "price_moved_without_evidence", "N/A", {"direct_revenue_link_confirmed": False, "kkanbu_listed": False}),
)


ROUND308_SHADOW_WEIGHT_ROWS: tuple[Round308ShadowWeightRow, ...] = (
    Round308ShadowWeightRow(E2RArchetype.EARLY_EVIDENCE_MISSED_STRUCTURAL, 5, 4, 3, 5, 0, 0, 1, 2, -4, -1, -1, -2, "ASP+shipment+capacity+OP estimate", "reported earnings confirmation pending", "actual earnings+favorable OHLC", "Samyang template."),
    Round308ShadowWeightRow(E2RArchetype.DELIVERY_TO_REVENUE_STAGE2_YELLOW, 5, 5, 5, 2, 0, 0, 1, 1, -3, -1, -1, -1, "delivery+revenue+OP estimate", "multi-quarter margin pending", "cash collection+margin+OHLC", "Hyundai Rotem template."),
    Round308ShadowWeightRow(E2RArchetype.STRATEGIC_CAPITAL_WITH_DILUTION_4B, 3, 5, 1, 1, 1, 0, 5, 2, -3, -2, -5, -1, "strategic capital+price strength", "order backlog/dilution pending", "backlog+margin+conversion clarity", "Samsung SDS template."),
    Round308ShadowWeightRow(E2RArchetype.CONTROL_BATTLE_GOVERNANCE_4B_4C, 1, 4, 0, 0, 0, 0, 5, 5, -2, -5, -3, -1, "control premium", "governance/dilution/regulator risk", "clean governance+cashflow", "Korea Zinc template."),
    Round308ShadowWeightRow(E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED, 3, 0, 1, 2, 1, 0, 1, 5, -3, -1, -1, -1, "good evidence but weak price", "price confirmation missing", "price recovery+earnings proof", "LG CNS template."),
    Round308ShadowWeightRow(E2RArchetype.PLATFORM_SECURITY_HARD_4C, 0, 0, 0, 0, 5, 1, 3, 5, -1, -1, -1, -1, "data breach", "trust recovery pending", "security restored+revenue stabilized", "SKT/Coupang template."),
    Round308ShadowWeightRow(E2RArchetype.OPERATIONAL_SAFETY_HARD_4C, 0, 0, 0, 0, 1, 5, 2, 5, -1, -1, -1, -1, "fatal safety incident", "investigation/remediation pending", "safety trust recovered", "Jeju Air template."),
    Round308ShadowWeightRow(E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE, 0, 3, 0, 0, 0, 0, 0, 5, -5, -1, -1, -5, "price move without revenue evidence", "no evidence", "N/A", "Jensen fried-chicken template."),
    Round308ShadowWeightRow(E2RArchetype.POLICY_THEME_OVERHEAT_4B, 0, 2, 0, 0, 0, 0, 1, 4, -5, -1, -1, -1, "policy theme", "license/revenue missing", "license+revenue+contract", "Stablecoin/AI-textbook policy template."),
    Round308ShadowWeightRow(E2RArchetype.OHLC_BACKFILL_SEPARATION_REQUIRED, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, "stage row separate from OHLC row", "backfill pending", "full MFE/MAE calculated", "Production architecture rule."),
)


def round308_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND308_CASE_CANDIDATES]


def round308_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND308_CASE_CANDIDATES]


def round308_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND308_TRIGGER_RECORDS]


def round308_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND308_SHADOW_WEIGHT_ROWS]


def round308_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND308_REQUIRED_TARGET_ALIASES.items()]


def round308_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND308_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND308_SCORE_DOWN_AXES]
    )


def round308_summary() -> dict[str, object]:
    return {
        "source_round": ROUND308_SOURCE_ROUND_PATH,
        "round_id": ROUND308_ANALYST_ROUND_ID,
        "large_sector": ROUND308_LARGE_SECTOR,
        "method": ROUND308_METHOD,
        "case_candidate_count": len(ROUND308_CASE_CANDIDATES),
        "trigger_count": len(ROUND308_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND308_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 3,
        "stage3_yellow_candidate_count": 2,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 4,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 2,
        "evidence_good_but_price_failed_count": 1,
        "price_moved_without_evidence_count": 1,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round308_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND308_SOURCE_ROUND_PATH,
        "round_id": ROUND308_ANALYST_ROUND_ID,
        "large_sector": ROUND308_LARGE_SECTOR,
        "method": ROUND308_METHOD,
        "summary": round308_summary(),
        "required_target_aliases": dict(ROUND308_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND308_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND308_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND308_STAGE3_GREEN_RULES,
        "green_blockers": ROUND308_GREEN_BLOCKERS,
        "score_up_axes": ROUND308_SCORE_UP_AXES,
        "score_down_axes": ROUND308_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND308_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND308_HARD_4C_GATES,
        "row_separation_rules": ROUND308_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round308_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_headline_control_premium_cb_meme_security_or_safety_as_green",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round308_summary_markdown() -> str:
    summary = round308_summary()
    lines = [
        "# R13 Loop 15 Cross-Archetype RedTeam / Price Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: Samyang's ASP/shipment/capacity/OP-estimate bundle can lift Stage2 to Actionable review, while Jensen's fried-chicken event cannot because there is no direct revenue bridge.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Stage2 can be too conservative when estimate revision, shipment/delivery, capacity and price reaction arrive together.",
            "- CB, control premium, IPO, policy, celebrity and platform-scale headlines need 4B/4C overlays instead of Green promotion.",
            "- Hard 4C: platform security breach and fatal safety incident.",
            "- Stage3-Green confirmed: `0`.",
            "- Case rows, trigger rows and OHLC backfill rows must stay separate.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round308_trigger_grid_markdown() -> str:
    lines = [
        "# Round 308 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round308_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round308_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 308 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND308_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND308_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND308_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND308_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND308_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round308_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 308 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND308_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C Gates",
        *_bullet_lines(ROUND308_HARD_4C_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND308_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date or case.hard_4c_confirmed:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round308_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 308 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND308_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round308_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 308 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: Samyang can be a valid Stage2-Actionable case even if 30D/90D OHLC has not been backfilled yet.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND308_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round308_r13_loop15_reports(
    output_directory: str | Path = ROUND308_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND308_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND308_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND308_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND308_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round308_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND308_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round308_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round308_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round308_r13_loop15_case_matrix.csv",
        "target_aliases": output_dir / "round308_r13_loop15_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round308_r13_loop15_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round308_r13_loop15_trigger_grid.md",
        "summary": output_dir / "round308_r13_loop15_redteam_summary.md",
        "stage_rules": output_dir / "round308_r13_loop15_stage_rules.md",
        "stage4b_4c_review": output_dir / "round308_r13_loop15_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round308_r13_loop15_score_adjustments.csv",
        "shadow_weights": output_dir / "round308_r13_loop15_shadow_weights.csv",
        "price_validation_plan": output_dir / "round308_r13_loop15_price_validation_plan.md",
        "row_separation_plan": output_dir / "round308_r13_loop15_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round308_case_rows())
    _write_csv(paths["target_aliases"], round308_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round308_trigger_rows())
    _write_csv(paths["score_adjustments"], round308_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round308_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round308_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round308_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round308_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round308_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round308_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round308_row_separation_plan_markdown(), encoding="utf-8")
    return paths


def _write_csv(path: Path, rows: Iterable[Mapping[str, str]]) -> None:
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
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


__all__ = [
    "ROUND308_CASE_CANDIDATES",
    "ROUND308_GREEN_BLOCKERS",
    "ROUND308_HARD_4C_GATES",
    "ROUND308_LARGE_SECTOR",
    "ROUND308_REQUIRED_TARGET_ALIASES",
    "ROUND308_ROW_SEPARATION_RULES",
    "ROUND308_SCORE_DOWN_AXES",
    "ROUND308_SCORE_UP_AXES",
    "ROUND308_SHADOW_WEIGHT_ROWS",
    "ROUND308_STAGE2_ACTIONABLE_RULES",
    "ROUND308_STAGE3_GREEN_RULES",
    "ROUND308_STAGE3_YELLOW_RULES",
    "ROUND308_STAGE4B_WATCH_TRIGGERS",
    "ROUND308_TRIGGER_RECORDS",
    "render_round308_stage4b_4c_review_markdown",
    "render_round308_stage_rules_markdown",
    "render_round308_trigger_grid_markdown",
    "round308_audit_payload",
    "round308_case_records",
    "round308_case_rows",
    "round308_shadow_weight_rows",
    "round308_summary",
    "round308_trigger_rows",
    "write_round308_r13_loop15_reports",
]
