"""Round-298 R3 Loop-15 battery/EV/green trigger-level validation pack.

This module converts ``docs/round/round_298.md`` into calibration-only case
records, trigger rows, and reports. It does not change production scoring,
staging, or candidate generation.

Easy example: a large battery contract is not automatically E2R Green. If the
customer program weakens and the actual call-off disappears, the same headline
becomes a 4C risk case.
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


ROUND298_SOURCE_ROUND_PATH = "docs/round/round_298.md"
ROUND298_ANALYST_ROUND_ID = "round_226"
ROUND298_LARGE_SECTOR = "SECONDARY_BATTERY_EV_GREEN"
ROUND298_METHOD = "trigger_level_backtest_v1"
ROUND298_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round298_r3_loop15_battery_ev_green_trigger_validation"
ROUND298_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop15_round226.jsonl"
ROUND298_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r3_loop15_round226.jsonl"
ROUND298_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round298_r3_loop15_battery_ev_green_trigger_validation_audit.json"
ROUND298_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round226_r3_loop15_v1.csv"

ROUND298_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BATTERY_AMPC_PROFIT_STAGE2_YELLOW": E2RArchetype.BATTERY_AMPC_PROFIT_STAGE2_YELLOW.value,
    "ESS_LFP_PIVOT_STAGE2_ACTIONABLE": E2RArchetype.ESS_LFP_PIVOT_STAGE2_ACTIONABLE.value,
    "EV_DEMAND_CONTRACT_CANCELLATION_4C": E2RArchetype.EV_DEMAND_CONTRACT_CANCELLATION_4C.value,
    "SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C": E2RArchetype.SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C.value,
    "LITHIUM_PRICE_EVENT_PREMIUM": E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM.value,
    "UPSTREAM_LITHIUM_SUPPLY_STAGE2": E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2.value,
    "FEOC_CATHODE_OWNERSHIP_STAGE2": E2RArchetype.FEOC_CATHODE_OWNERSHIP_STAGE2.value,
    "BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE": E2RArchetype.BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE.value,
}

ROUND298_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "contract_value_and_delivery_schedule_are_visible",
    "customer_application_and_chemistry_are_specific",
    "ev_line_to_ess_conversion_execution_evidence_exists",
    "trigger_day_market_relative_return_5pp_plus",
    "ex_subsidy_margin_or_subsidy_durability_is_quantified",
    "feoc_ira_compliance_risk_is_structurally_reduced",
)

ROUND298_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "at_least_two_of_contract_demand_margin_are_numeric",
    "delivery_calloff_subsidy_or_utilization_gate_still_pending",
    "no_battery_safety_or_customer_cancellation_hard_gate_open",
)

ROUND298_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "actual_customer_calloff_or_shipment_converts_to_revenue",
    "ex_subsidy_operating_margin_is_healthy",
    "plant_utilization_is_rising",
    "customer_model_plan_survives",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND298_GREEN_BLOCKERS: tuple[str, ...] = (
    "subsidy_included_op_without_ex_subsidy_margin",
    "signed_contract_amount_without_actual_calloff",
    "customer_name_without_model_survival",
    "line_conversion_without_delivery_or_margin",
    "lithium_price_event_without_durable_asp_margin",
    "battery_safety_or_supplier_disclosure_trust_issue",
    "full_adjusted_ohlc_window_missing_for_green_confirmation",
)

ROUND298_SCORE_UP_AXES: tuple[str, ...] = (
    "actual_customer_calloff",
    "contract_cancellation_risk",
    "ex_subsidy_operating_margin",
    "ampc_subsidy_durability",
    "ess_lfp_contract_quality",
    "line_conversion_execution",
    "customer_model_survival",
    "battery_safety_disclosure_trust",
    "raw_material_price_durability",
    "feoc_ira_compliance_quality",
)

ROUND298_SCORE_DOWN_AXES: tuple[str, ...] = (
    "signed_contract_amount_only",
    "ev_growth_headline_only",
    "subsidy_included_op_only",
    "lithium_price_event_only",
    "upstream_stake_without_margin",
    "line_conversion_without_delivery",
    "customer_name_without_model_survival",
    "battery_safety_ignored",
)

ROUND298_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "lithium_event_rally_without_durable_price_or_margin",
    "subsidy_included_op_beat_with_near_zero_ex_subsidy_op",
    "ess_or_data_center_headline_before_line_conversion_execution",
    "upstream_lithium_stake_priced_as_immediate_earnings",
)

ROUND298_HARD_4C_GATES: tuple[str, ...] = (
    "signed_contract_value_collapse",
    "customer_model_cancellation_or_ev_program_halt",
    "battery_jv_dissolution",
    "plant_layoff_or_utilization_collapse",
    "battery_fire_or_safety_failure",
    "misleading_battery_supplier_disclosure",
    "subsidy_rollback_that_destroys_economics",
    "line_conversion_failure",
)


@dataclass(frozen=True)
class Round298ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round298ShadowWeightRow:
    archetype: E2RArchetype
    actual_customer_calloff: int
    contract_cancellation_risk: int
    ex_subsidy_operating_margin: int
    ampc_subsidy_durability: int
    ess_lfp_contract_quality: int
    line_conversion_execution: int
    customer_model_survival: int
    battery_safety_disclosure_trust: int
    raw_material_price_durability: int
    feoc_ira_compliance_quality: int
    signed_contract_amount_only_penalty: int
    ev_growth_headline_only_penalty: int
    subsidy_included_op_only_penalty: int
    lithium_price_event_only_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "actual_customer_calloff": _signed(self.actual_customer_calloff),
            "contract_cancellation_risk": _signed(self.contract_cancellation_risk),
            "ex_subsidy_operating_margin": _signed(self.ex_subsidy_operating_margin),
            "ampc_subsidy_durability": _signed(self.ampc_subsidy_durability),
            "ess_lfp_contract_quality": _signed(self.ess_lfp_contract_quality),
            "line_conversion_execution": _signed(self.line_conversion_execution),
            "customer_model_survival": _signed(self.customer_model_survival),
            "battery_safety_disclosure_trust": _signed(self.battery_safety_disclosure_trust),
            "raw_material_price_durability": _signed(self.raw_material_price_durability),
            "feoc_ira_compliance_quality": _signed(self.feoc_ira_compliance_quality),
            "signed_contract_amount_only_penalty": _signed(self.signed_contract_amount_only_penalty),
            "ev_growth_headline_only_penalty": _signed(self.ev_growth_headline_only_penalty),
            "subsidy_included_op_only_penalty": _signed(self.subsidy_included_op_only_penalty),
            "lithium_price_event_only_penalty": _signed(self.lithium_price_event_only_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round298TriggerRecord:
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
class Round298CaseCandidate:
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
    trigger_outcome_label: str
    stage_gate_correction: str
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
    market_relative_return_pp: float | None
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

    def to_case_record(self) -> E2RCaseRecord:
        guardrails = [
            "production_scoring_changed_false",
            "candidate_generation_input_false",
            "shadow_weight_only_true",
            "full_adjusted_ohlc_complete_false",
            "stage_candidate_not_downgraded_for_missing_full_ohlc",
            "do_not_use_round298_cases_as_candidate_generation_input",
            "do_not_force_stage3_green_without_actual_calloff_ex_subsidy_margin",
            "battery_safety_and_contract_cancellation_are_hard_gates",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND298_LARGE_SECTOR,
            large_sector=ROUND298_LARGE_SECTOR,
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
            must_have_fields=ROUND298_STAGE2_ACTIONABLE_RULES + ROUND298_STAGE3_YELLOW_RULES + ROUND298_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason=self.round_stage_failure_label,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern=self.round_alignment_label,
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                stage1_price=self.stage1_price_anchor,
                stage2_price=self.stage2_price_anchor,
                stage3_price=self.stage3_price_anchor,
                stage4b_price=self.stage4b_price_anchor,
                stage4c_price=self.stage4c_price_anchor,
                mfe_30d=self.event_mfe_pct if self.event_mfe_pct and self.event_mfe_pct > 0 else None,
                mae_30d=self.event_mae_pct if self.event_mae_pct and self.event_mae_pct < 0 else None,
                price_validation_status=self.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=False,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.7,
            ),
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
            "trigger_outcome_label": self.trigger_outcome_label,
            "stage_gate_correction": self.stage_gate_correction,
            "evidence_fields": ";".join(self.evidence_fields),
            "red_flag_fields": ";".join(self.red_flag_fields),
            "price_data_source": self.price_data_source,
            "reported_price_anchor": self.reported_price_anchor,
            "reported_return_anchor": self.reported_return_anchor,
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "market_relative_return_pp": _value_text(self.market_relative_return_pp),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "round_rerating_label": self.round_rerating_label,
            "stage_failure_type": self.stage_failure_type,
            "round_stage_failure_label": self.round_stage_failure_label,
            "price_validation_status": self.price_validation_status,
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "notes": self.notes,
        }


ROUND298_SCORE_ADJUSTMENTS: tuple[Round298ScoreAdjustment, ...] = (
    Round298ScoreAdjustment("actual_customer_calloff", 5, "raise", "계약 headline이 아니라 실제 call-off, shipment, revenue 전환을 우선한다."),
    Round298ScoreAdjustment("contract_cancellation_risk", 5, "raise", "Ford, Freudenberg, Tesla 사례처럼 cancellation은 배터리 4C 핵심이다."),
    Round298ScoreAdjustment("ex_subsidy_operating_margin", 5, "raise", "AMPC 포함 OP가 좋아도 보조금 제외 margin이 약하면 Green을 막는다."),
    Round298ScoreAdjustment("ampc_subsidy_durability", 4, "raise", "보조금이 반복 가능하고 정책 리스크가 낮아야 Stage3-Yellow 이상을 검토한다."),
    Round298ScoreAdjustment("ess_lfp_contract_quality", 4, "raise", "EV 둔화 국면에서 ESS LFP 계약은 Stage2-Actionable pivot 증거다."),
    Round298ScoreAdjustment("line_conversion_execution", 4, "raise", "EV line을 ESS로 바꾸는 실행 증거는 단순 수요 headline보다 강하다."),
    Round298ScoreAdjustment("customer_model_survival", 5, "raise", "고객 EV 모델과 생산계획이 살아 있어야 계약 가치가 유지된다."),
    Round298ScoreAdjustment("battery_safety_disclosure_trust", 5, "raise", "화재, 품질, supplier disclosure는 배터리 업종 hard gate다."),
    Round298ScoreAdjustment("raw_material_price_durability", 4, "raise", "lithium event는 지속 가격과 ASP/margin 확인 전에는 Stage3가 아니다."),
    Round298ScoreAdjustment("feoc_ira_compliance_quality", 4, "raise", "FEOC/IRA risk reduction은 Stage2 evidence지만 고객 award와 margin 확인이 필요하다."),
    Round298ScoreAdjustment("signed_contract_amount_only", -5, "lower", "signed amount만으로 Green을 만들면 L&F/Tesla 같은 붕괴를 놓친다."),
    Round298ScoreAdjustment("ev_growth_headline_only", -5, "lower", "EV growth headline은 고객 모델 survival과 utilization 없이 약하다."),
    Round298ScoreAdjustment("subsidy_included_op_only", -5, "lower", "subsidy 포함 OP만 보면 margin quality를 과대평가한다."),
    Round298ScoreAdjustment("lithium_price_event_only", -4, "lower", "CATL mine suspension 같은 이벤트성 rally는 durable margin 전까지 premium이다."),
)


ROUND298_SHADOW_WEIGHT_ROWS: tuple[Round298ShadowWeightRow, ...] = (
    Round298ShadowWeightRow(E2RArchetype.BATTERY_AMPC_PROFIT_STAGE2_YELLOW, 5, 5, 5, 5, 2, 2, 5, 3, 1, 3, -5, -5, -5, -3, "OP beat+AMPC+relative strength", "ex-AMPC margin/customer call-off pending", "ex-subsidy margin+durable customer volumes", "LGES AMPC beat is Yellow, not Green."),
    Round298ShadowWeightRow(E2RArchetype.ESS_LFP_PIVOT_STAGE2_ACTIONABLE, 4, 3, 3, 3, 5, 5, 4, 3, 2, 3, -4, -4, -3, -3, "ESS contract+line conversion+relative strength", "delivery/margin pending", "delivery+repeat order+margin", "Samsung SDI ESS pivot Stage2-Actionable."),
    Round298ShadowWeightRow(E2RArchetype.EV_DEMAND_CONTRACT_CANCELLATION_4C, 5, 5, 2, 2, 3, 3, 5, 2, 2, 2, -5, -5, -3, -2, "customer program cancellation or JV break", "EV model survival pending", "customer production schedule intact", "SK On/Ford and LGES/Ford are 4C-watch patterns."),
    Round298ShadowWeightRow(E2RArchetype.SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C, 5, 5, 2, 1, 0, 0, 5, 2, 2, 1, -5, -5, -2, -2, "contract value collapse", "call-off failure", "actual shipment/revenue confirmed", "L&F/Tesla is hard 4C."),
    Round298ShadowWeightRow(E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM, 2, 2, 1, 1, 0, 0, 2, 1, 5, 1, -3, -3, -2, -5, "lithium event rally", "durable lithium price pending", "ASP/margin confirmed", "CATL mine suspension is event premium."),
    Round298ShadowWeightRow(E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2, 3, 2, 2, 2, 0, 0, 3, 1, 5, 4, -3, -3, -2, -3, "upstream stake/offtake rights", "cost advantage pending", "downstream margin/cost advantage", "POSCO/MinRes is supply security Stage2."),
    Round298ShadowWeightRow(E2RArchetype.FEOC_CATHODE_OWNERSHIP_STAGE2, 3, 2, 2, 3, 0, 0, 3, 2, 2, 5, -3, -3, -2, -2, "China stake reduction/FEOC risk down", "customer award pending", "IRA benefit+margin confirmed", "LG Chem/Toyota is regulatory-risk reduction Stage2."),
    Round298ShadowWeightRow(E2RArchetype.BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE, 2, 3, 1, 1, 0, 0, 2, 5, 1, 3, -2, -2, -1, -1, "safety failure/disclosure issue", "investigation/liability pending", "safety compliance/trust restored", "Aricell/S-Connect and Mercedes/Farasis are hard gates."),
)


ROUND298_TRIGGER_RECORDS: tuple[Round298TriggerRecord, ...] = (
    Round298TriggerRecord("r3l15_lges_T1", "r3_loop15_lges_ampc_profit_dealrisk", "Stage3-Yellow_candidate", date(2025, 7, 7), "Q2 OP 492B won, +152% YoY, above 294B consensus, shares +2.4%, but ex-AMPC OP only 1.4B won", 318000, 2.4, None, "Stage3_Yellow_with_subsidy_overlay", "Stage3-Yellow", {"op_vs_consensus_pct": 67.3, "op_ex_ampc_krw_bn": 1.4}),
    Round298TriggerRecord("r3l15_lges_T4", "r3_loop15_lges_ampc_profit_dealrisk", "4C-watch", date(2025, 12, 26), "Ford 9.6T won and Freudenberg 3.9T won cancellations, total 13.5T won expected revenue lost", None, "price_data_unavailable_after_deep_search", None, "thesis_break_watch", "4C-watch", {"total_lost_expected_revenue_krw_trn": 13.5}),
    Round298TriggerRecord("r3l15_sdi_T2", "r3_loop15_samsung_sdi_ess_lfp_pivot", "Stage2-Actionable", date(2025, 12, 10), "U.S. LFP ESS contract >2T won / $1.36B, deliveries from 2027, EV lines converted to ESS, shares +6.1% vs KOSPI -0.1%", None, 6.1, 6.2, "Stage2_promote_candidate", "Stage2-Actionable", {"ess_contract_value_krw_trn": 2.0, "delivery_start": 2027}),
    Round298TriggerRecord("r3l15_skon_T2", "r3_loop15_sk_on_ford_jv_termination", "4C-watch", date(2025, 12, 16), "Ford EV retreat hits Korean battery chain; SK Innovation -3%, LGES -6%, SK IE Tech -5%, EcoPro Materials -5%", None, "SKI -3 / LGES -6 / SKIET -5 / EcoPro Materials -5", None, "thesis_break_watch", "4C-watch", {"q3_2025_sk_on_op_loss_krw_bn": 124.8}),
    Round298TriggerRecord("r3l15_lnf_T2", "r3_loop15_lnf_tesla_cathode_contract_collapse", "hard_4C", date(2025, 12, 29), "Tesla cathode supply deal cut from $2.9B to $7,386 due EV slowdown and 4680 ramp issues", None, "price_data_unavailable_after_deep_search", None, "hard_4c_success", "4C", {"contract_value_collapse_pct": -99.9997}),
    Round298TriggerRecord("r3l15_lithium_T2", "r3_loop15_catl_mine_lithium_price_event", "event_premium", date(2025, 8, 11), "CATL Yichun mine suspended; POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%; CATL says no material impact", None, "POSCO Future M +8.3 / L&F +10 / SDI +3.2 / LGES +2.8", None, "event_premium_not_stage3", "4B-watch", {"license_renewal_possible": True}),
    Round298TriggerRecord("r3l15_posco_T1", "r3_loop15_posco_minres_lithium_supply_security", "Stage2_supply_security", date(2025, 11, 11), "POSCO pays $765M for 30% of MinRes lithium JV, indirect 15% Wodgina/Mt Marion exposure, MinRes +10.8%", None, "POSCO price unavailable / MinRes +10.8", None, "success_candidate_stage2", "Stage2", {"minres_deal_value_usd_mn": 765}),
    Round298TriggerRecord("r3l15_lgchem_T1", "r3_loop15_lg_chem_toyota_tsusho_cathode_feoc", "Stage2_regulatory_risk_reduction", date(2025, 9, 8), "Toyota Tsusho takes 25% stake in LG Chem cathode plant; Huayou stake falls from 49% to 24%", None, "price_data_unavailable_after_deep_search", None, "success_candidate_stage2", "Stage2", {"huayou_stake_after_pct": 24}),
    Round298TriggerRecord("r3l15_aricell_T1", "r3_loop15_aricell_sconnect_battery_safety_hard_4c", "hard_4C", date(2024, 6, 24), "Aricell fire killed 23; S-Connect -22.5%; later police blame quality failures and deadline pressure", None, -22.5, None, "hard_4c_success", "4C", {"fatalities": 23, "lithium_batteries_stored": 35000}),
)


ROUND298_CASE_CANDIDATES: tuple[Round298CaseCandidate, ...] = (
    Round298CaseCandidate(
        "r3_loop15_lges_ampc_profit_dealrisk",
        "373220",
        "LG Energy Solution",
        E2RArchetype.BATTERY_AMPC_PROFIT_STAGE2_YELLOW,
        (E2RArchetype.IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE, E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C),
        "success_candidate",
        "Stage3-Yellow with subsidy and customer-calloff overlay",
        "T1/T2",
        "Stage2-Actionable_to_Stage3-Yellow_with_subsidy_overlay",
        "Stage3-Yellow_candidate",
        date(2025, 7, 7),
        date(2025, 7, 7),
        date(2025, 7, 7),
        date(2025, 7, 7),
        date(2025, 12, 26),
        False,
        "Stage3_Yellow_with_4C_overlay",
        "AMPC-driven profit beat can be Yellow, but Green needs ex-subsidy margin and durable customer call-off.",
        ("Q2_2025_OP_492B_KRW", "OP_plus_152pct_YoY", "OP_consensus_294B_KRW", "OP_ex_AMPC_1_4B_KRW", "event_return_plus_2_4pct"),
        ("ex_AMPC_OP_margin_0_03pct", "Ford_cancel_9_6T_KRW", "Freudenberg_cancel_3_9T_KRW", "sales_minus_9_7pct_YoY"),
        "Reuters/MarketWatch reported event return and financial anchors; no full adjusted OHLC window",
        "318,000 KRW on 2025-07-07",
        "+2.4% event return; later 13.5T KRW expected revenue cancellation",
        2.4,
        None,
        None,
        None,
        None,
        318000,
        None,
        None,
        {"q2_2025_op_krw_bn": 492, "q2_2025_op_yoy_pct": 152, "op_vs_consensus_pct": 67.3, "op_ex_ampc_krw_bn": 1.4, "op_margin_ex_ampc_pct": 0.03, "total_lost_expected_revenue_krw_trn": 13.5, "honda_asset_sale_usd_bn": 2.86, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        "aligned",
        "Stage3_Yellow_with_4C_overlay",
        "unknown",
        "Yellow_not_Green_due_subsidy_and_calloff_risk",
        "yellow_success",
        "green_without_ex_subsidy_margin_would_be_false_positive",
        "reported_event_anchor_not_full_ohlc",
        "AMPC 포함 OP beat는 강하지만 보조금 제외 margin과 고객 call-off가 남아 Green은 막는다.",
    ),
    Round298CaseCandidate(
        "r3_loop15_samsung_sdi_ess_lfp_pivot",
        "006400",
        "Samsung SDI",
        E2RArchetype.ESS_LFP_PIVOT_STAGE2_ACTIONABLE,
        (E2RArchetype.ESS_LFP_CONTRACT_STAGE2_NOT_GREEN, E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA),
        "success_candidate",
        "Stage2-Actionable ESS LFP pivot",
        "T2/T3",
        "Stage2-Actionable_to_Stage3-Yellow_candidate",
        "Stage2-Actionable",
        date(2024, 6, 28),
        date(2025, 12, 10),
        None,
        None,
        None,
        False,
        "Stage2_promote_candidate",
        "ESS LFP contract and EV-to-ESS line conversion make this Stage2-Actionable; Green needs delivery and margin.",
        ("ESS_contract_over_2T_KRW", "ESS_contract_1_36B_USD", "delivery_start_2027", "delivery_duration_3_years", "line_conversion_from_EV_to_ESS", "event_return_plus_6_1pct"),
        ("EV_demand_sluggish_until_H1_2026", "Q4_2024_OP_loss_257B_KRW", "delivery_margin_pending"),
        "Reuters/MarketWatch reported contract and event return anchors; no full adjusted OHLC window",
        "price unavailable",
        "+6.1% vs KOSPI -0.1%, relative +6.2pp",
        6.1,
        None,
        6.2,
        None,
        None,
        None,
        None,
        None,
        {"rivian_sales_target_units": 57000, "rivian_market_expectation_units": 82000, "q4_2024_op_loss_krw_bn": 257, "ess_contract_value_krw_trn": 2.0, "ess_contract_value_usd_bn": 1.36, "market_relative_return_pp": 6.2, "delivery_start": 2027, "delivery_duration_years": 3, "line_conversion_from_ev_to_ess": True, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        "missed_due_to_score",
        "Stage2_promote_candidate",
        "unknown",
        "ESS_pivot_stage2_actionable",
        "stage2_watch_success",
        "delivery_and_converted_line_margin_pending",
        "reported_event_anchor_not_full_ohlc",
        "EV 부진을 ESS LFP 계약과 라인 전환으로 방어하는 Stage2 후보지만, 2027 delivery와 margin 확인 전 Green은 아니다.",
    ),
    Round298CaseCandidate(
        "r3_loop15_sk_on_ford_jv_termination",
        "096770",
        "SK Innovation / SK On",
        E2RArchetype.EV_DEMAND_CONTRACT_CANCELLATION_4C,
        (E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C, E2RArchetype.EV_BATTERY_JV_RESTRUCTURING),
        "4c_thesis_break",
        "EV JV termination thesis-break watch",
        "T1/T2",
        "4C-watch_to_thesis_break",
        "4C-watch",
        date(2022, 1, 1),
        date(2022, 1, 1),
        None,
        None,
        date(2025, 12, 11),
        False,
        "thesis_break_watch",
        "EV JV and battery contract value must be tied to customer model survival and production schedule.",
        ("Ford_SK_On_original_JV_11_4B_USD", "Ford_Kentucky_full_ownership", "SK_On_Tennessee_full_ownership", "Q3_2025_SK_On_OP_loss_124_8B_KRW"),
        ("JV_dissolution", "Ford_EV_retreat", "Georgia_layoffs_958_workers", "utilization_collapse_watch"),
        "Reuters/MarketWatch/AP reported cancellation and event-return anchors",
        "price unavailable",
        "SK Innovation -3%, LGES -6%, SK IE Tech -5%, EcoPro Materials -5%",
        None,
        -6.0,
        None,
        None,
        None,
        None,
        None,
        None,
        {"original_jv_investment_usd_bn": 11.4, "q3_2025_sk_on_op_loss_krw_bn": 124.8, "sk_innovation_event_mae_pct": -3, "lges_event_mae_pct": -6, "sk_ie_tech_event_mae_pct": -5, "ecopro_materials_event_mae_pct": -5, "georgia_layoffs_workers": 958, "georgia_layoffs_pct_workforce": 37, "georgia_plant_cost_usd_bn": 2.6, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        "unknown",
        "thesis_break_watch",
        "thesis_break",
        "EV_contract_4C_watch",
        "unknown",
        "watch_until_impairment_or_funding_gap_is_confirmed",
        "reported_event_anchor_not_full_ohlc",
        "EV 성장 JV가 고객 생산계획과 economics를 잃으면 Stage2가 아니라 4C-watch로 바뀐다.",
    ),
    Round298CaseCandidate(
        "r3_loop15_lnf_tesla_cathode_contract_collapse",
        "066970",
        "L&F",
        E2RArchetype.SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C,
        (E2RArchetype.EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE, E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK),
        "4c_thesis_break",
        "hard 4C signed cathode contract collapse",
        "T2",
        "hard_4C",
        "4C",
        date(2023, 1, 1),
        date(2023, 1, 1),
        None,
        None,
        date(2025, 12, 29),
        True,
        "hard_4c_success",
        "Signed contract amount must not be Green without actual call-off and customer model survival.",
        ("Tesla_affiliates_high_nickel_cathode_contract", "initial_contract_value_2_9B_USD", "supply_period_2024_2025", "Tesla_4680_application"),
        ("revised_contract_value_7386_USD", "contract_value_collapse_minus_99_9997pct", "EV_demand_slowdown", "4680_ramp_difficulty", "Cybertruck_underperformance"),
        "Reuters contract-value-collapse anchor; no KRX OHLC window",
        "price unavailable",
        "contract value collapsed from $2.9B to $7,386",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        {"initial_contract_value_usd_bn": 2.9, "revised_contract_value_usd": 7386, "contract_value_collapse_pct": -99.9997, "supply_period": "2024-01_to_2025-12", "application_context": "Tesla 4680 cells", "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        "false_positive_score",
        "thesis_break",
        "thesis_break",
        "hard_4C",
        "should_have_been_red",
        "signed_contract_amount_without_calloff_would_create_false_green",
        "reported_event_anchor_not_full_ohlc",
        "고객명과 계약금액이 있어도 실제 call-off가 사라지면 hard 4C다.",
    ),
    Round298CaseCandidate(
        "r3_loop15_catl_mine_lithium_price_event",
        "003670/066970/006400/373220",
        "POSCO Future M / L&F / Samsung SDI / LGES",
        E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM,
        (E2RArchetype.EVENT_LITHIUM_PRICE_RALLY, E2RArchetype.LITHIUM_CYCLE_OVERLAY),
        "event_premium",
        "lithium price event premium",
        "T2",
        "event_premium",
        "4B-watch",
        date(2025, 8, 11),
        None,
        None,
        date(2025, 8, 11),
        None,
        False,
        "event_premium_not_stage3",
        "Lithium supply-shock rally requires durable lithium price and ASP/margin confirmation before Stage3.",
        ("CATL_Yichun_mine_suspension", "POSCO_Future_M_plus_8_3pct", "LNF_plus_10pct", "Samsung_SDI_plus_3_2pct", "LGES_plus_2_8pct"),
        ("CATL_no_material_impact_claim", "license_renewal_possible", "lithium_price_event_only"),
        "WSJ reported lithium event returns; no full adjusted OHLC window",
        "event return basket",
        "POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%",
        10.0,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        {"posco_future_m_event_mfe_pct": 8.3, "lnf_event_mfe_pct": 10.0, "samsung_sdi_event_mfe_pct": 3.2, "lges_event_mfe_pct": 2.8, "ganfeng_lithium_event_mfe_pct": 21, "tianqi_lithium_event_mfe_pct": 18, "lithium_price_decline_from_2022_peak_pct": -90, "license_renewal_possible": True, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        "price_moved_without_evidence",
        "event_premium",
        "event_premium",
        "temporary_lithium_event",
        "false_yellow",
        "durable_lithium_price_and_material_margin_missing",
        "reported_event_anchor_not_full_ohlc",
        "lithium 이벤트 반응은 컸지만, 지속 가격과 소재 margin 확인 전에는 Stage3가 아니다.",
    ),
    Round298CaseCandidate(
        "r3_loop15_posco_minres_lithium_supply_security",
        "005490/003670",
        "POSCO Holdings / POSCO Future M",
        E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2,
        (E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA, E2RArchetype.LITHIUM_RESOURCE_SECURITY),
        "success_candidate",
        "Stage2 supply-security",
        "T1",
        "Stage2_supply_security",
        "Stage2",
        date(2025, 11, 11),
        date(2025, 11, 11),
        None,
        None,
        None,
        False,
        "success_candidate_stage2",
        "Upstream stake improves supply security, but Stage3 requires cost advantage and downstream margin.",
        ("MinRes_lithium_JV_30pct_stake", "deal_value_765M_USD", "Wodgina_indirect_15pct", "Mt_Marion_indirect_15pct", "spodumene_offtake_rights"),
        ("spodumene_price_far_below_2022_peak", "downstream_margin_pending", "lithium_price_cycle_risk"),
        "Reuters reported MinRes deal and lithium price anchors; POSCO direct price unavailable",
        "POSCO direct price unavailable",
        "MinRes +10.8%",
        10.8,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        {"minres_deal_value_usd_mn": 765, "minres_event_mfe_pct": 10.8, "posco_effective_interest_wodgina_pct": 15, "posco_effective_interest_mt_marion_pct": 15, "spodumene_price_mid_2025_low_usd_t": 610, "spodumene_price_august_2025_usd_t": 880, "spodumene_2022_peak_usd_t": 6000, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        "aligned",
        "success_candidate_stage2",
        "unknown",
        "supply_security_not_green",
        "stage2_watch_success",
        "cost_advantage_and_downstream_margin_pending",
        "reported_event_anchor_not_full_ohlc",
        "원재료 확보는 Stage2 근거지만, 비용우위와 downstream margin이 없으면 Green은 아니다.",
    ),
    Round298CaseCandidate(
        "r3_loop15_lg_chem_toyota_tsusho_cathode_feoc",
        "051910",
        "LG Chem",
        E2RArchetype.FEOC_CATHODE_OWNERSHIP_STAGE2,
        (E2RArchetype.CATHODE_SUPPLY_CHAIN_DERISKING, E2RArchetype.FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN),
        "success_candidate",
        "Stage2 regulatory-risk reduction",
        "T1",
        "Stage2_regulatory_risk_reduction",
        "Stage2",
        date(2025, 9, 8),
        date(2025, 9, 8),
        None,
        None,
        None,
        False,
        "success_candidate_stage2",
        "Ownership restructuring reduces FEOC risk, but Stage3 requires customer award, IRA benefit and cathode margin.",
        ("Toyota_Tsusho_new_stake_25pct", "Huayou_stake_before_49pct", "Huayou_stake_after_24pct", "China_exposure_reduced", "FEOC_IRA_relevance"),
        ("customer_award_pending", "IRA_benefit_pending", "cathode_margin_pending"),
        "Reuters reported ownership restructuring; direct price anchor unavailable",
        "price unavailable",
        "price_data_unavailable_after_deep_search",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        {"toyota_tsusho_new_stake_pct": 25, "huayou_stake_before_pct": 49, "huayou_stake_after_pct": 24, "china_exposure_reduced": True, "feoc_ira_relevance": True, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        "aligned",
        "success_candidate_stage2",
        "policy_event_rerating",
        "regulatory_risk_reduction_not_green",
        "stage2_watch_success",
        "customer_award_ira_benefit_and_margin_pending",
        "reported_event_anchor_not_full_ohlc",
        "중국 지분 축소는 좋은 risk reduction이지만, 고객 award와 margin 전에는 cashflow trigger가 아니다.",
    ),
    Round298CaseCandidate(
        "r3_loop15_aricell_sconnect_battery_safety_hard_4c",
        "096630/battery_safety_basket",
        "S-Connect / Aricell reference",
        E2RArchetype.BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE,
        (E2RArchetype.BATTERY_SAFETY_HARD_REFERENCE, E2RArchetype.EV_BATTERY_TRANSPARENCY_REGULATORY_OVERLAY),
        "4c_thesis_break",
        "battery safety hard 4C reference",
        "T0/T1",
        "hard_4C_reference",
        "4C",
        date(2024, 6, 24),
        None,
        None,
        None,
        date(2024, 6, 24),
        True,
        "hard_4c_success",
        "Battery safety and supplier disclosure must be explicit hard gates for all battery/EV names.",
        ("Aricell_Hwaseong_lithium_battery_factory_fire", "fatalities_23", "lithium_batteries_stored_35000", "S_Connect_minus_22_5pct"),
        ("quality_inspection_failed_before_fire", "temporary_unskilled_worker_factor", "defect_rate_increase_factor", "EV_supplier_disclosure_issue", "Mercedes_KFTC_fine_11_2B_KRW"),
        "Reuters/AP reported safety event return and regulatory anchors",
        "event price unavailable",
        "S-Connect -22.5% on fire news, -1.37% next day",
        None,
        -22.5,
        None,
        None,
        None,
        None,
        None,
        None,
        {"fatalities": 23, "injuries": 9, "lithium_batteries_stored": 35000, "sconnect_event_mae_pct": -22.5, "sconnect_next_day_return_pct": -1.37, "quality_inspection_failed_before_fire": True, "temporary_unskilled_worker_factor": True, "defect_rate_increase_factor": True, "ev_fire_damaged_or_destroyed_cars": 140, "mercedes_kftc_fine_krw_bn": 11.2, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        "false_positive_score",
        "hard_4c_success",
        "thesis_break",
        "safety_hard_gate",
        "should_have_been_red",
        "battery_safety_ignored_would_create_false_positive_score",
        "reported_event_anchor_not_full_ohlc",
        "배터리 안전/품질/공시 신뢰는 단순 ESG가 아니라 valuation hard gate다.",
    ),
)


def round298_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(case.to_case_record() for case in ROUND298_CASE_CANDIDATES)


def round298_summary() -> dict[str, object]:
    return {
        "source_round": ROUND298_SOURCE_ROUND_PATH,
        "round_id": ROUND298_ANALYST_ROUND_ID,
        "large_sector": ROUND298_LARGE_SECTOR,
        "method": ROUND298_METHOD,
        "case_candidate_count": len(ROUND298_CASE_CANDIDATES),
        "trigger_count": len(ROUND298_TRIGGER_RECORDS),
        "stage2_actionable_candidate_count": 4,
        "stage3_yellow_candidate_count": 2,
        "stage3_green_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 3,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": sum(1 for case in ROUND298_CASE_CANDIDATES if case.hard_4c_confirmed),
        "missed_structural_count": 0,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
    }


def round298_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(case.as_row() for case in ROUND298_CASE_CANDIDATES)


def round298_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND298_TRIGGER_RECORDS)


def round298_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"requested_alias": key, "canonical_archetype": value} for key, value in ROUND298_REQUIRED_TARGET_ALIASES.items())


def round298_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND298_SCORE_ADJUSTMENTS)


def round298_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND298_SHADOW_WEIGHT_ROWS)


def round298_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND298_SOURCE_ROUND_PATH,
        "round_id": ROUND298_ANALYST_ROUND_ID,
        "large_sector": ROUND298_LARGE_SECTOR,
        "method": ROUND298_METHOD,
        "summary": round298_summary(),
        "target_archetypes": dict(ROUND298_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND298_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND298_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND298_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND298_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND298_SCORE_UP_AXES),
        "score_down_axes": list(ROUND298_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND298_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND298_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_apply_round298_shadow_weights_to_production_scoring_yet",
            "do_not_use_round298_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds_for_battery_recall",
            "do_not_treat_signed_contract_amount_as_actual_calloff",
            "do_not_treat_subsidy_included_op_as_ex_subsidy_margin",
            "do_not_ignore_battery_safety_or_supplier_disclosure_trust",
        ],
    }


def render_round298_summary_markdown() -> str:
    summary = round298_summary()
    lines = [
        "# Round 298 R3 Loop 15 Battery/EV/Green Trigger Validation",
        "",
        "이번 라운드는 2차전지, EV, ESS, 소재, 친환경 공급망을 calibration-only로 정리한다.",
        "",
        "쉬운 예: `계약금액 2조원`은 시작점일 뿐이다. 실제 납품, 고객 생산계획, 보조금 제외 margin이 닫히지 않으면 Green이 아니라 Stage2 또는 Yellow에 머문다.",
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
            "- LGES AMPC profit beat는 Stage3-Yellow 후보지만, 보조금 제외 OP와 고객 call-off가 남아 Green은 아니다.",
            "- Samsung SDI ESS LFP pivot은 Stage2-Actionable이다. 다만 delivery와 converted-line margin 전에는 Green이 아니다.",
            "- SK On/Ford, LGES/Ford/Freudenberg, L&F/Tesla는 EV 계약 headline이 4C로 바뀔 수 있음을 보여준다.",
            "- CATL mine suspension에 따른 lithium rally는 event premium이다. 지속 가격과 소재 margin 확인 전 Stage3가 아니다.",
            "- Aricell/S-Connect 및 EV battery disclosure 이슈는 safety/trust hard gate다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round298_trigger_grid_markdown() -> str:
    lines = [
        "# Round 298 Trigger Grid",
        "",
        "| trigger_id | case_id | date | type | outcome | promote_to | evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND298_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {trigger.trigger_date.isoformat()} | {trigger.trigger_type} | {trigger.trigger_outcome_label} | {trigger.promote_to} | {trigger.evidence_available} |"
        )
    return "\n".join(lines) + "\n"


def render_round298_stage_rules_markdown() -> str:
    lines = [
        "# Round 298 Stage Rules",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Stage2-Actionable",
        "",
    ]
    lines.extend(f"- {rule}" for rule in ROUND298_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow", ""])
    lines.extend(f"- {rule}" for rule in ROUND298_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Stage3-Green", ""])
    lines.extend(f"- {rule}" for rule in ROUND298_STAGE3_GREEN_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND298_GREEN_BLOCKERS)
    return "\n".join(lines) + "\n"


def render_round298_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 298 4B/4C Review",
        "",
        "이번 라운드에서는 Stage3-Green 확정이 없다. 핵심은 EV 계약/보조금/안전 risk를 early gate로 올리는 것이다.",
        "",
        "## 4B Watch",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND298_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {item}" for item in ROUND298_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "Confirmed hard 4C examples:",
            "",
            "- L&F/Tesla contract value collapse",
            "- Aricell/S-Connect battery safety reference",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round298_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round 298 Price Validation Plan",
            "",
            "- reported_event_anchor_not_full_ohlc 상태를 유지한다.",
            "- full adjusted OHLC가 없다는 이유로 Stage2/Yellow 후보를 강등하지 않는다.",
            "- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.",
            "- 다음 단계에서는 각 trigger date 기준 30/90/180일 MFE/MAE와 below-entry 여부를 채운다.",
            "",
        ]
    )


def write_round298_r3_loop15_reports(
    *,
    output_directory: str | Path = ROUND298_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND298_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND298_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND298_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND298_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round298_case_records(), cases_path),
        "triggers": write_round298_triggers(triggers_path),
        "audit": _write_json(round298_audit_payload(), audit_path),
        "weight_profile": _write_csv(round298_shadow_weight_rows(), weight_profile_path),
        "summary": output / "round298_r3_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round298_r3_loop15_case_matrix.csv",
        "trigger_grid": output / "round298_r3_loop15_trigger_grid.csv",
        "target_aliases": output / "round298_r3_loop15_target_aliases.csv",
        "score_adjustments": output / "round298_r3_loop15_score_adjustments.csv",
        "shadow_weights": output / "round298_r3_loop15_shadow_weights.csv",
        "stage_rules": output / "round298_r3_loop15_stage_rules.md",
        "trigger_grid_md": output / "round298_r3_loop15_trigger_grid.md",
        "price_validation_plan": output / "round298_r3_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round298_r3_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round298_summary_markdown(), encoding="utf-8")
    _write_csv(round298_case_rows(), paths["case_matrix"])
    _write_csv(round298_trigger_rows(), paths["trigger_grid"])
    _write_csv(round298_target_alias_rows(), paths["target_aliases"])
    _write_csv(round298_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round298_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round298_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round298_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round298_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round298_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round298_triggers(path: str | Path = ROUND298_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND298_TRIGGER_RECORDS]
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
    "ROUND298_CASE_CANDIDATES",
    "ROUND298_GREEN_BLOCKERS",
    "ROUND298_HARD_4C_GATES",
    "ROUND298_LARGE_SECTOR",
    "ROUND298_REQUIRED_TARGET_ALIASES",
    "ROUND298_SCORE_DOWN_AXES",
    "ROUND298_SCORE_UP_AXES",
    "ROUND298_SHADOW_WEIGHT_ROWS",
    "ROUND298_STAGE2_ACTIONABLE_RULES",
    "ROUND298_STAGE3_GREEN_RULES",
    "ROUND298_STAGE3_YELLOW_RULES",
    "ROUND298_STAGE4B_WATCH_TRIGGERS",
    "ROUND298_TRIGGER_RECORDS",
    "render_round298_stage_rules_markdown",
    "render_round298_stage4b_4c_review_markdown",
    "render_round298_trigger_grid_markdown",
    "round298_audit_payload",
    "round298_case_records",
    "round298_case_rows",
    "round298_shadow_weight_rows",
    "round298_summary",
    "round298_trigger_rows",
    "write_round298_r3_loop15_reports",
]
