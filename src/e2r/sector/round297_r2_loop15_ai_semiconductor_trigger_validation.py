"""Round-297 R2 Loop-15 AI/semiconductor trigger-level validation pack.

This module converts ``docs/round/round_297.md`` into calibration-only case
records, trigger rows, and reports. It does not change production scoring,
staging, or candidate generation.

Easy example: SK Hynix on 2024-09-26 was not just an "AI theme" headline.
HBM3E 12-layer mass production, capacity improvement, customer supply timing,
and strong market-relative price reaction appeared together. That can promote
Stage2 to Stage3-Yellow, while later OpenAI/ASML headlines after a huge rally
must carry a 4B overlay.
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


ROUND297_SOURCE_ROUND_PATH = "docs/round/round_297.md"
ROUND297_ANALYST_ROUND_ID = "round_225"
ROUND297_LARGE_SECTOR = "AI_SEMICONDUCTOR_ELECTRONIC_PARTS"
ROUND297_METHOD = "trigger_level_backtest_v1"
ROUND297_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round297_r2_loop15_ai_semiconductor_trigger_validation"
ROUND297_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop15_round225.jsonl"
ROUND297_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r2_loop15_round225.jsonl"
ROUND297_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round297_r2_loop15_ai_semiconductor_trigger_validation_audit.json"
ROUND297_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round225_r2_loop15_v1.csv"

ROUND297_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "HBM_FIRST_MOVER_STAGE2_TO_GREEN": E2RArchetype.HBM_FIRST_MOVER_STAGE2_TO_GREEN.value,
    "HBM_EQUIPMENT_STAGE2_ACTIONABLE": E2RArchetype.HBM_EQUIPMENT_STAGE2_ACTIONABLE.value,
    "HBM_CATCHUP_LATE_STAGE2": E2RArchetype.HBM_CATCHUP_LATE_STAGE2.value,
    "OPENAI_STARGATE_MEMORY_4B_WATCH": E2RArchetype.OPENAI_STARGATE_MEMORY_4B_WATCH.value,
    "SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH": E2RArchetype.SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH.value,
    "AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE": E2RArchetype.AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE.value,
    "DISPLAY_OLED_APPLE_RECOVERY_STAGE2": E2RArchetype.DISPLAY_OLED_APPLE_RECOVERY_STAGE2.value,
    "SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C": E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C.value,
}

ROUND297_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "hbm_mix_or_ai_revenue_share_or_op_estimate_is_quantified",
    "named_customer_or_product_is_specific",
    "mass_production_certification_shipment_or_supply_deal_confirmed",
    "trigger_day_market_relative_strength_5pp_plus",
    "target_price_or_op_estimate_20pct_plus_above_consensus",
    "repeat_order_or_capacity_allocation_confirmed",
)

ROUND297_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "mass_production_or_customer_qualification_confirmed",
    "op_eps_or_hbm_mix_numeric_improvement_visible",
    "trigger_day_relative_strength_is_strong",
    "forward_allocation_margin_capacity_or_customer_concentration_still_pending",
)

ROUND297_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "hbm_or_ai_component_revenue_confirmed_in_actual_results",
    "op_beat_record_profit_or_consensus_revision_confirmed",
    "mass_production_to_customer_revenue_conversion_confirmed",
    "full_window_price_path_validation_available",
    "4b_and_4c_overlays_do_not_break_the_thesis",
)

ROUND297_GREEN_BLOCKERS: tuple[str, ...] = (
    "full_adjusted_ohlc_window_missing",
    "late_catchup_without_relative_strength",
    "customer_name_without_allocation",
    "sellthrough_or_component_margin_missing",
    "profitability_guidance_missing",
    "parabolic_rally_requires_4b_overlay",
    "china_export_control_or_labor_continuity_4c_watch",
)

ROUND297_SCORE_UP_AXES: tuple[str, ...] = (
    "hbm_mix_revenue_share",
    "op_estimate_revision_vs_consensus",
    "mass_production_or_customer_qualification",
    "named_customer_equipment_order",
    "repeat_order_backlog_quality",
    "relative_strength_on_evidence_day",
    "ai_capex_customer_commitment",
    "device_upgrade_op_estimate",
)

ROUND297_SCORE_DOWN_AXES: tuple[str, ...] = (
    "ai_theme_only",
    "customer_name_without_allocation",
    "target_price_raise_without_price_strength",
    "late_catchup_without_relative_strength",
    "capex_without_ROIC_or_dilution_check",
    "openai_or_nvidia_headline_after_parabolic_rally",
)

ROUND297_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "one_year_200pct_plus_or_prior_year_274pct_rally_before_new_AI_headline",
    "openai_or_nvidia_headline_after_parabolic_move",
    "large_capex_order_without_ROIC_or_dilution_check",
    "possible_listing_or_share_issuance_after_success",
    "customer_concentration_high_and_single_customer_allocation_sensitive",
)

ROUND297_HARD_4C_GATES: tuple[str, ...] = (
    "HBM_qualification_failure",
    "customer_allocation_loss",
    "actual_shipment_delay",
    "china_fab_equipment_license_restriction_blocks_upgrade",
    "major_labor_strike_disrupting_memory_supply",
    "capex_or_dilution_changes_EPS_path",
    "hyperscaler_AI_capex_slowdown",
)


@dataclass(frozen=True)
class Round297ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round297ShadowWeightRow:
    archetype: E2RArchetype
    hbm_mix_revenue_share: int
    op_estimate_revision_vs_consensus: int
    mass_production_or_customer_qualification: int
    named_customer_equipment_order: int
    repeat_order_backlog_quality: int
    relative_strength_on_evidence_day: int
    ai_capex_customer_commitment: int
    device_upgrade_op_estimate: int
    ai_theme_only_penalty: int
    late_catchup_penalty: int
    capex_dilution_4b_overlay: int
    export_control_4c_overlay: int
    labor_continuity_4c_overlay: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "hbm_mix_revenue_share": _signed(self.hbm_mix_revenue_share),
            "op_estimate_revision_vs_consensus": _signed(self.op_estimate_revision_vs_consensus),
            "mass_production_or_customer_qualification": _signed(self.mass_production_or_customer_qualification),
            "named_customer_equipment_order": _signed(self.named_customer_equipment_order),
            "repeat_order_backlog_quality": _signed(self.repeat_order_backlog_quality),
            "relative_strength_on_evidence_day": _signed(self.relative_strength_on_evidence_day),
            "ai_capex_customer_commitment": _signed(self.ai_capex_customer_commitment),
            "device_upgrade_op_estimate": _signed(self.device_upgrade_op_estimate),
            "ai_theme_only_penalty": _signed(self.ai_theme_only_penalty),
            "late_catchup_penalty": _signed(self.late_catchup_penalty),
            "capex_dilution_4b_overlay": _signed(self.capex_dilution_4b_overlay),
            "export_control_4c_overlay": _signed(self.export_control_4c_overlay),
            "labor_continuity_4c_overlay": _signed(self.labor_continuity_4c_overlay),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round297TriggerRecord:
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
class Round297CaseCandidate:
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


ROUND297_SCORE_ADJUSTMENTS: tuple[Round297ScoreAdjustment, ...] = (
    Round297ScoreAdjustment("hbm_mix_revenue_share", 5, "raise", "HBM 매출 mix가 숫자로 보이면 단순 AI 테마보다 강하다."),
    Round297ScoreAdjustment("op_estimate_revision_vs_consensus", 5, "raise", "OP 추정치가 consensus보다 20% 이상 높으면 Stage2-Actionable 승격 후보가 된다."),
    Round297ScoreAdjustment("mass_production_or_customer_qualification", 5, "raise", "양산, 인증, 고객 공급은 테마를 실적 경로로 바꾼다."),
    Round297ScoreAdjustment("named_customer_equipment_order", 5, "raise", "SK Hynix, Nvidia, Apple처럼 고객과 장비명이 닫히면 trigger 품질이 높다."),
    Round297ScoreAdjustment("repeat_order_backlog_quality", 4, "raise", "반복 수주와 backlog는 일회성 장비 기대보다 강하다."),
    Round297ScoreAdjustment("relative_strength_on_evidence_day", 5, "raise", "증거가 나온 날 시장 대비 +5pp 이상이면 실제 자금 반응이 확인된다."),
    Round297ScoreAdjustment("ai_capex_customer_commitment", 4, "raise", "OpenAI/hyperscaler capex는 수요 검증이지만 4B overlay를 같이 본다."),
    Round297ScoreAdjustment("device_upgrade_op_estimate", 4, "raise", "AI device cycle은 OP estimate beat가 붙을 때 Stage2 후보가 된다."),
    Round297ScoreAdjustment("ai_theme_only", -5, "lower", "AI 단어만으로 매출·마진을 만들지 않는다."),
    Round297ScoreAdjustment("customer_name_without_allocation", -4, "lower", "고객 이름만 있고 allocation이나 shipment가 없으면 Green 금지다."),
    Round297ScoreAdjustment("target_price_raise_without_price_strength", -3, "lower", "target 상향만 있고 가격 반응이 없으면 full-window 재검증이 필요하다."),
    Round297ScoreAdjustment("late_catchup_without_relative_strength", -4, "lower", "후발 catch-up은 first mover보다 상대강도 discount를 적용한다."),
    Round297ScoreAdjustment("capex_without_ROIC_or_dilution_check", -4, "lower", "대규모 capex는 ROIC와 희석 가능성을 같이 본다."),
    Round297ScoreAdjustment("openai_or_nvidia_headline_after_parabolic_rally", -4, "lower", "급등 이후 OpenAI/Nvidia headline은 Green만이 아니라 4B overlay다."),
)


ROUND297_SHADOW_WEIGHT_ROWS: tuple[Round297ShadowWeightRow, ...] = (
    Round297ShadowWeightRow(E2RArchetype.HBM_FIRST_MOVER_STAGE2_TO_GREEN, 5, 5, 5, 3, 4, 5, 4, 1, -5, -1, 4, 4, 3, "HBM mix+OP revision+mass production+relative strength", "customer allocation/margin pending", "record profit+volume commitments", "SK Hynix missed-structural template."),
    Round297ShadowWeightRow(E2RArchetype.HBM_EQUIPMENT_STAGE2_ACTIONABLE, 4, 3, 4, 5, 5, 5, 3, 0, -5, -1, 3, 3, 2, "named HBM equipment+customer+repeat order+relative strength", "customer concentration pending", "margin/backlog conversion", "Hanmi Stage2-Actionable template."),
    Round297ShadowWeightRow(E2RArchetype.HBM_CATCHUP_LATE_STAGE2, 4, 4, 5, 3, 2, 3, 4, 1, -5, -4, 3, 4, 5, "Nvidia/OpenAI catch-up requires relative-strength discount", "allocation/timing pending", "shipment+allocation+margin", "Samsung catch-up not Green without allocation."),
    Round297ShadowWeightRow(E2RArchetype.OPENAI_STARGATE_MEMORY_4B_WATCH, 5, 4, 4, 3, 3, 5, 5, 0, -4, -1, 5, 4, 4, "large AI capex commitment+relative strength", "valuation/capex overlay", "volume+profit confirmed", "OpenAI demand validates but 4B after parabolic rally."),
    Round297ShadowWeightRow(E2RArchetype.SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH, 2, 1, 1, 1, 1, 2, 1, 0, -2, -1, 2, 5, 2, "export equipment authorization risk", "license uncertainty", "license relief or alternative equipment", "China fab exposure is explicit 4C overlay."),
    Round297ShadowWeightRow(E2RArchetype.AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE, 0, 5, 2, 3, 3, 5, 3, 5, -4, -1, 2, 2, 1, "AI device upgrade+OP estimate+relative strength", "sell-through pending", "shipments/ASP confirmed", "LG Innotek Stage2-Actionable template."),
    Round297ShadowWeightRow(E2RArchetype.DISPLAY_OLED_APPLE_RECOVERY_STAGE2, 0, 4, 2, 3, 2, 2, 1, 4, -4, -1, 2, 2, 1, "loss beat+Apple OLED order", "profitability guidance missing", "sustained profit and utilization", "LG Display remains Stage2 until sustained profitability."),
    Round297ShadowWeightRow(E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C, 3, 2, 2, 1, 1, 1, 2, 0, -1, -1, 2, 3, 5, "labor continuity affects memory supply", "settlement pending", "production continuity confirmed", "Samsung labor strike is 4C-watch overlay."),
)


ROUND297_TRIGGER_RECORDS: tuple[Round297TriggerRecord, ...] = (
    Round297TriggerRecord("r2l15_skhynix_T0", "r2_loop15_sk_hynix_hbm_first_mover", "Stage2-Actionable", date(2024, 3, 26), "AI/HBM rally, Daiwa EPS forecast +41%, HBM3E contribution, SK Hynix +4.3% vs KOSPI +0.7%", None, 4.3, 3.6, "early_stage2_actionable", "Stage2-Actionable", {"kospi_return_pct": 0.7, "daiwa_eps_forecast_raise_pct": 41}),
    Round297TriggerRecord("r2l15_skhynix_T1", "r2_loop15_sk_hynix_hbm_first_mover", "Stage2-Actionable", date(2024, 6, 26), "HSBC 2Q OP estimate +12% to 5.2T won, HBM share 38% of DRAM revenue by end-2025, target 280,000", 234500, None, None, "Stage2_promote_candidate", "Stage3-Yellow_candidate", {"op_estimate_krw_trn": 5.2, "op_estimate_raise_pct": 12, "hbm_dram_revenue_share_2025e_pct": 38, "target_price_krw": 280000}),
    Round297TriggerRecord("r2l15_skhynix_T2", "r2_loop15_sk_hynix_hbm_first_mover", "Stage3-Yellow", date(2024, 9, 26), "12-layer HBM3E mass production, 50% capacity increase, supply to customers by year-end", None, 9.0, 7.3, "excellent_entry_candidate", "Stage3-Yellow", {"kospi_return_pct": 1.7, "hbm3e_capacity_increase_pct": 50}),
    Round297TriggerRecord("r2l15_hanmi_T1", "r2_loop15_hanmi_semiconductor_hbm_equipment", "Stage2-Actionable", date(2024, 3, 26), "SK Hynix HBM packaging equipment, KRW21.48B supply deal, recent wins KRW200B", None, 16, 15.3, "excellent_stage2_promote_candidate", "Stage2-Actionable", {"sk_hynix_supply_deal_krw_bn": 21.48, "recent_contract_wins_krw_bn": 200}),
    Round297TriggerRecord("r2l15_samsung_T2", "r2_loop15_samsung_electronics_hbm_catchup_labor_watch", "Stage2-Actionable", date(2025, 10, 2), "OpenAI partnership, AI data center memory demand, Samsung +4.7%, SK Hynix +12%", None, 4.7, "relative_to_SK_Hynix_-7.3pp", "late_catchup_candidate", "Stage2-Actionable_only", {"sk_hynix_return_pct": 12, "kospi_return_pct": 3, "relative_to_sk_hynix_pp": -7.3}),
    Round297TriggerRecord("r2l15_skhynix_openai_T1", "r2_loop15_sk_hynix_openai_asml_4b", "Stage3-Green+4B-watch", date(2025, 10, 2), "OpenAI Stargate partnership, Samsung +4.7%, SK Hynix +12%, KOSPI +3%", None, 12, 9, "green_demand_confirmation_with_4b_overlay", "Stage3-Green+4B", {"openai_stargate_project_usd_bn": 500}),
    Round297TriggerRecord("r2l15_export_control_T1", "r2_loop15_memory_china_equipment_export_control", "4C-watch", date(2025, 9, 1), "U.S. revoked authorizations for China fab equipment; Samsung -2.6%, SK Hynix -5%", None, "Samsung -2.6 / SK Hynix -5.0", None, "thesis_break_watch", "4C-watch", {"license_expiry_days": 120, "short_term_impact_limited_view": True}),
    Round297TriggerRecord("r2l15_lginnotek_T1", "r2_loop15_lg_innotek_apple_ai_upgrade", "Stage2-Actionable", date(2024, 6, 12), "Apple/OpenAI AI iPhone upgrade cycle, LG Innotek +19%, OP growth forecast +33%", 272000, 19, 18.6, "excellent_stage2_promote_candidate", "Stage2-Actionable", {"op_2024_forecast_growth_pct": 33}),
    Round297TriggerRecord("r2l15_lgdisplay_T1", "r2_loop15_lg_display_apple_oled_recovery", "Stage2", date(2024, 7, 25), "Q2 loss 94B vs expected 308B, revenue +42%, Apple OLED orders, but no 2H profit guidance", None, None, None, "evidence_good_but_price_data_incomplete", "Stage2_only", {"loss_beat_amount_krw_bn": 214, "revenue_growth_pct": 42}),
    Round297TriggerRecord("r2l15_samsung_labor_T2", "r2_loop15_samsung_labor_supply_chain_4c", "4C-watch", date(2026, 5, 19), "48,000 workers, 18-day strike risk, DRAM supply impact 3-4%, NAND 2-3%", None, None, None, "thesis_break_watch", "4C-watch", {"strike_workers_count": 48000, "strike_days": 18, "government_gdp_impact_estimate_pp": 0.5}),
)


ROUND297_CASE_CANDIDATES: tuple[Round297CaseCandidate, ...] = (
    Round297CaseCandidate(
        case_id="r2_loop15_sk_hynix_hbm_first_mover",
        symbol="000660",
        company_name="SK Hynix",
        primary_archetype=E2RArchetype.HBM_FIRST_MOVER_STAGE2_TO_GREEN,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.HBM_DOMINANCE_STAGE3_AND_4B),
        case_type="structural_success",
        round_case_type="missed_structural / Stage2_promote_candidate / Stage3-Yellow-to-Green candidate / 4B overlay later",
        best_trigger="T1/T2",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow",
        stage_candidate="Stage2-Actionable_to_Stage3-Yellow_to_Green_candidate",
        stage1_date=date(2024, 3, 26),
        stage2_date=date(2024, 6, 26),
        stage3_date=date(2024, 9, 26),
        stage4b_date=date(2025, 9, 12),
        stage4c_date=date(2025, 9, 1),
        hard_4c_confirmed=False,
        trigger_outcome_label="missed_structural_if_stage3_waited_until_record_profit",
        stage_gate_correction="HBM product qualification + OP estimate raise + HBM mix + relative strength should promote Stage2 to Stage3-Yellow",
        evidence_fields=("HBM3E_contribution", "OP_estimate_revision_5_2T_KRW", "HBM_DRAM_revenue_share_38pct_2025e", "12_layer_HBM3E_mass_production", "HBM3E_capacity_increase_50pct"),
        red_flag_fields=("legacy_memory_price_warning", "parabolic_2025_2026_rally", "China_equipment_restriction", "US_listing_dilution_watch"),
        price_data_source="WSJ/Reuters reported event returns and price anchors; no full adjusted OHLC window",
        reported_price_anchor="234,500 KRW at T1; 1,447,000 KRW later OpenAI/capex context",
        reported_return_anchor="T0 +4.3% vs KOSPI +0.7%; T2 +9% vs KOSPI +1.7%; 2025 +274%, 2026 +200%+",
        event_mfe_pct=9.0,
        event_mae_pct=-4.0,
        market_relative_return_pp=7.3,
        stage1_price_anchor=None,
        stage2_price_anchor=234500,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"t0_event_return_pct": 4.3, "t0_kospi_return_pct": 0.7, "t0_market_relative_return_pp": 3.6, "t1_entry_price_anchor_krw": 234500, "t1_op_estimate_krw_trn": 5.2, "t1_op_estimate_raise_pct": 12, "t1_hbm_dram_revenue_share_2025e_pct": 38, "t1_target_price_krw": 280000, "t2_event_return_pct": 9.0, "t2_kospi_return_pct": 1.7, "t2_market_relative_return_pp": 7.3, "t2_hbm3e_capacity_increase_pct": 50, "t3_q4_op_krw_trn": 8.1, "t3_hbm_share_dram_revenue_pct": 40, "t3_event_return_pct": -4.0, "t4_q2_op_krw_trn": 9.2, "t4_revenue_yoy_pct": 35, "t4_ytd_gain_pct": 54.7, "forward_return_anchor_2025_pct": 274, "forward_return_anchor_2026_ytd_pct": 200, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        score_price_alignment="missed_due_to_score",
        round_alignment_label="missed_structural_if_old_gate_used",
        rerating_result="true_rerating",
        round_rerating_label="Stage2_to_Stage3_Yellow_to_Green_candidate",
        stage_failure_type="missed_structural",
        round_stage_failure_label="plain_stage2_understates_HBM_mix_OP_revision_mass_production_relative_strength",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="SK Hynix should not wait until record profit day; 2024 HBM mix, OP revision, mass production and relative strength were earlier triggers.",
    ),
    Round297CaseCandidate(
        case_id="r2_loop15_hanmi_semiconductor_hbm_equipment",
        symbol="042700",
        company_name="Hanmi Semiconductor",
        primary_archetype=E2RArchetype.HBM_EQUIPMENT_STAGE2_ACTIONABLE,
        secondary_archetypes=(E2RArchetype.SEMI_EQUIPMENT_CAPEX, E2RArchetype.TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="Stage2_promote_candidate / HBM equipment 4B concentration watch",
        best_trigger="T1",
        best_trigger_type="Stage2-Actionable",
        stage_candidate="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage1_date=date(2024, 3, 26),
        stage2_date=date(2024, 3, 26),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        hard_4c_confirmed=False,
        trigger_outcome_label="Stage2_promote_candidate",
        stage_gate_correction="specific HBM equipment + named customer order + repeated wins + +15pp relative strength should be Stage2-Actionable",
        evidence_fields=("SK_Hynix_named_customer", "TSV_TC_bonder_HBM_packaging_equipment", "SK_Hynix_supply_deal_21_48B_KRW", "recent_contract_wins_200B_KRW", "event_relative_strength_15_3pp"),
        red_flag_fields=("customer_concentration", "shipment_revenue_margin_pending", "pure_play_4b_watch_after_rally"),
        price_data_source="WSJ reported event return and contract anchors",
        reported_price_anchor="price unavailable; event return +16%",
        reported_return_anchor="+16% vs KOSPI +0.7%, relative +15.3pp",
        event_mfe_pct=16.0,
        event_mae_pct=None,
        market_relative_return_pp=15.3,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"trigger_date": "2024-03-26", "event_return_pct": 16, "kospi_return_pct": 0.7, "market_relative_return_pp": 15.3, "sk_hynix_same_day_return_pct": 4.3, "specific_customer": "SK Hynix", "specific_equipment": "TSV-TC bonders / HBM packaging equipment", "sk_hynix_supply_deal_krw_bn": 21.48, "recent_contract_wins_krw_bn": 200, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        score_price_alignment="missed_due_to_score",
        round_alignment_label="Stage2_promote_candidate",
        rerating_result="unknown",
        round_rerating_label="HBM_equipment_stage2_actionable",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="customer_equipment_contract_relative_strength_should_promote_stage2",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Named customer, named equipment, repeated wins and strong relative strength justify Stage2-Actionable, but not Green before revenue and margin.",
    ),
    Round297CaseCandidate(
        case_id="r2_loop15_samsung_electronics_hbm_catchup_labor_watch",
        symbol="005930",
        company_name="Samsung Electronics",
        primary_archetype=E2RArchetype.HBM_CATCHUP_LATE_STAGE2,
        secondary_archetypes=(E2RArchetype.SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH, E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C),
        case_type="success_candidate",
        round_case_type="late Stage2-Actionable / Stage3-Yellow candidate / labor 4C-watch",
        best_trigger="T2/T3",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage_candidate="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage1_date=date(2025, 10, 2),
        stage2_date=date(2025, 10, 2),
        stage3_date=date(2025, 10, 31),
        stage4b_date=None,
        stage4c_date=date(2026, 5, 19),
        hard_4c_confirmed=False,
        trigger_outcome_label="late_catchup_stage2_actionable_with_labor_4c_watch",
        stage_gate_correction="Samsung catch-up triggers need relative-strength discount vs SK Hynix and labor continuity overlay",
        evidence_fields=("OpenAI_partnership", "Nvidia_HBM3E_HBM4_partnership_acknowledged", "HBM4_talks_confirmed", "Q3_OP_12_2T_KRW", "semiconductor_OP_7T_KRW"),
        red_flag_fields=("relative_strength_minus_7_3pp_vs_SK_Hynix", "SK_Hynix_primary_partner_still", "labor_strike_48000_workers", "DRAM_NAND_supply_impact_watch"),
        price_data_source="Reuters OpenAI/Nvidia/Samsung labor anchors",
        reported_price_anchor="event price unavailable; Samsung +4.7% on OpenAI day and +4% on Nvidia/HBM talks",
        reported_return_anchor="Samsung +4.7% while SK Hynix +12%; later Samsung +4%+",
        event_mfe_pct=4.7,
        event_mae_pct=None,
        market_relative_return_pp=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"t2_event_return_pct": 4.7, "t2_sk_hynix_return_pct": 12, "t2_kospi_return_pct": 3, "relative_to_sk_hynix_pp": -7.3, "t3_event_return_pct": 4.0, "nvidia_partnership_acknowledged": True, "hbm3e_supply_to_related_customers": True, "hbm4_talks_confirmed": True, "sk_hynix_primary_partner_still": True, "q3_2025_op_krw_trn": 12.2, "q3_2025_op_growth_pct": 32.5, "q3_2025_revenue_krw_trn": 86, "semiconductor_division_op_krw_trn": 7, "labor_strike_workers_context": 48000, "potential_dram_supply_impact_pct": "3-4", "potential_nand_supply_impact_pct": "2-3", "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="Stage2-Actionable_but_not_Green",
        rerating_result="unknown",
        round_rerating_label="late_catchup_discount",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="late_catchup_relative_strength_and_labor_overlay_block_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Samsung catch-up is investable research evidence, but it is not SK Hynix-style first-mover Green without allocation and labor continuity.",
    ),
    Round297CaseCandidate(
        case_id="r2_loop15_sk_hynix_openai_asml_4b",
        symbol="000660",
        company_name="SK Hynix",
        primary_archetype=E2RArchetype.OPENAI_STARGATE_MEMORY_4B_WATCH,
        secondary_archetypes=(E2RArchetype.HBM_FIRST_MOVER_STAGE2_TO_GREEN, E2RArchetype.AI_INFRA_MEMORY_SUPPLY_MOU_4B),
        case_type="4b_watch",
        round_case_type="Stage3-Green candidate + 4B-watch",
        best_trigger="T1_before_full_4B",
        best_trigger_type="Stage3-Green_with_4B_overlay",
        stage_candidate="Stage3-Green_candidate_plus_4B-watch",
        stage1_date=date(2025, 10, 2),
        stage2_date=date(2025, 10, 2),
        stage3_date=date(2026, 5, 4),
        stage4b_date=date(2026, 3, 24),
        stage4c_date=None,
        hard_4c_confirmed=False,
        trigger_outcome_label="Stage3_Green_with_4B_overlay",
        stage_gate_correction="OpenAI/capex confirmation validates demand, but after +274%/+200% rally requires 4B sizing overlay",
        evidence_fields=("OpenAI_Stargate_project_500B_USD", "hyperscaler_AI_capex_700B_USD", "SK_Hynix_record_high_1447000_KRW", "ASML_EUV_order_11_95T_KRW", "EUV_machines_about_30"),
        red_flag_fields=("2025_gain_274pct", "2026_gain_200pct_plus", "ASML_capex_ROIC_watch", "US_listing_dilution_watch"),
        price_data_source="Reuters OpenAI, hyperscaler capex, ASML order and listing anchors",
        reported_price_anchor="1,447,000 KRW on 2026-05-04 record high",
        reported_return_anchor="OpenAI +12%; hyperscaler capex +13% vs KOSPI +5.1%; ASML order +5.7%",
        event_mfe_pct=13.0,
        event_mae_pct=None,
        market_relative_return_pp=7.9,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=1447000,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"openai_stargate_project_usd_bn": 500, "t1_event_return_pct": 12, "t1_samsung_return_pct": 4.7, "t1_kospi_return_pct": 3, "t2_event_return_pct": 13, "t2_event_price_krw": 1447000, "t2_kospi_return_pct": 5.1, "ai_capex_2026_usd_bn": 700, "asml_order_krw_trn": 11.95, "asml_order_usd_bn": 7.97, "asml_event_return_pct": 5.7, "estimated_euv_machines": 30, "us_listing_possible_raise_usd_bn": "9.6-14.4", "possible_share_issuance_pct": "2-3", "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        score_price_alignment="aligned",
        round_alignment_label="aligned_if_stage3_plus_4B_overlay_allowed",
        rerating_result="true_rerating",
        round_rerating_label="demand_confirmation_with_4B_overlay",
        stage_failure_type="green_success",
        round_stage_failure_label="green_without_4b_overlay_would_be_unsafe",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="OpenAI and ASML validate demand, but after a parabolic move they must be written as Green candidate plus 4B overlay.",
    ),
    Round297CaseCandidate(
        case_id="r2_loop15_memory_china_equipment_export_control",
        symbol="005930/000660/042700/067310",
        company_name="Samsung / SK Hynix / Hanmi / Hana Micron",
        primary_archetype=E2RArchetype.SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH,
        secondary_archetypes=(E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY),
        case_type="4c_thesis_break",
        round_case_type="4C-watch",
        best_trigger="T1",
        best_trigger_type="4C-watch",
        stage_candidate="4C-watch",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        hard_4c_confirmed=False,
        trigger_outcome_label="thesis_break_watch",
        stage_gate_correction="China fab exposure and equipment-license status must be explicit 4C overlay even in AI memory upcycle",
        evidence_fields=("US_revokes_China_fab_equipment_authorization", "Samsung_minus_2_6pct", "SK_Hynix_minus_5pct", "license_expiry_120_days"),
        red_flag_fields=("China_memory_output_share_30_to_40pct", "Samsung_China_NAND_about_one_third", "equipment_upgrade_block_watch"),
        price_data_source="Reuters export-control event anchor",
        reported_price_anchor="event price unavailable",
        reported_return_anchor="Samsung -2.6%, SK Hynix -5%",
        event_mfe_pct=None,
        event_mae_pct=-5.0,
        market_relative_return_pp=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"trigger_date": "2025-09-01", "samsung_event_mae_pct": -2.6, "sk_hynix_event_mae_pct": -5.0, "license_expiry_days": 120, "sk_hynix_china_memory_output_share_pct": "30-40", "samsung_china_nand_output_share_pct": "about_one_third", "related_firms_affected": ["Hana Micron", "Hanmi Semiconductor"], "short_term_impact_limited_view": True, "hard_4c_confirmed": False, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="export_control_4c_watch",
        stage_failure_type="unknown",
        round_stage_failure_label="watch_not_hard_4c_until_license_denial_or_production_disruption",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="AI memory thesis can remain intact, but China fab equipment access is a separate 4C overlay.",
    ),
    Round297CaseCandidate(
        case_id="r2_loop15_lg_innotek_apple_ai_upgrade",
        symbol="011070",
        company_name="LG Innotek",
        primary_archetype=E2RArchetype.AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE,
        secondary_archetypes=(E2RArchetype.AI_DEVICE_COMPONENT_OPTIONALITY, E2RArchetype.ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2),
        case_type="success_candidate",
        round_case_type="Stage2-Actionable / sell-through gate",
        best_trigger="T1",
        best_trigger_type="Stage2-Actionable",
        stage_candidate="Stage2-Actionable_to_Stage3-Yellow_pending_sellthrough",
        stage1_date=date(2024, 6, 10),
        stage2_date=date(2024, 6, 12),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 11, 1),
        hard_4c_confirmed=False,
        trigger_outcome_label="Stage2_Actionable_but_needs_sellthrough_validation",
        stage_gate_correction="AI device cycle + OP estimate beat + +19% relative strength is Stage2-Actionable, but Green requires sell-through and component ASP",
        evidence_fields=("Apple_OpenAI_AI_iPhone_upgrade_cycle", "LG_Innotek_plus_19pct", "OP_2024_forecast_growth_33pct", "Q2_OP_estimate_31pct_above_consensus"),
        red_flag_fields=("iPhone16_sellthrough_pending", "camera_module_ASP_pending", "inventory_pending", "iOS_growth_only_0_4pct_watch"),
        price_data_source="WSJ and MarketWatch LG Innotek event/estimate anchors",
        reported_price_anchor="272,000 KRW on +19% event move",
        reported_return_anchor="+19% vs KOSPI +0.4%; later estimate day -0.4%",
        event_mfe_pct=19.0,
        event_mae_pct=-0.4,
        market_relative_return_pp=18.6,
        stage1_price_anchor=None,
        stage2_price_anchor=272000,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"t1_date": "2024-06-12", "t1_entry_price_anchor_krw": 272000, "t1_event_return_pct": 19, "t1_kospi_return_pct": 0.4, "t1_market_relative_return_pp": 18.6, "op_2024_forecast_krw_trn": 1.110, "op_2024_forecast_growth_pct": 33, "t2_date": "2024-06-27", "t2_op_estimate_krw_bn": 106.4, "t2_consensus_op_krw_bn": 81.1, "t2_op_estimate_vs_consensus_pct": 31.2, "t2_target_before_krw": 280000, "t2_target_after_krw": 330000, "t2_event_return_pct": -0.4, "stage3_gate_missing": ["actual_iPhone16_sellthrough", "camera_module_ASP", "inventory", "Apple_AI_upgrade_conversion"], "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        score_price_alignment="missed_due_to_score",
        round_alignment_label="Stage2_promote_candidate",
        rerating_result="unknown",
        round_rerating_label="AI_device_stage2_actionable",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="AI_device_OP_estimate_relative_strength_should_promote_stage2",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Apple AI device upgrade plus OP estimate beat and +19% relative strength justify Stage2-Actionable, not Green before sell-through.",
    ),
    Round297CaseCandidate(
        case_id="r2_loop15_lg_display_apple_oled_recovery",
        symbol="034220",
        company_name="LG Display",
        primary_archetype=E2RArchetype.DISPLAY_OLED_APPLE_RECOVERY_STAGE2,
        secondary_archetypes=(E2RArchetype.DISPLAY_OLED_SUPPLYCHAIN, E2RArchetype.OLED_PORTFOLIO_RESTRUCTURING_STAGE2),
        case_type="success_candidate",
        round_case_type="evidence_good_but_price_data_incomplete",
        best_trigger="T1_pending_price",
        best_trigger_type="Stage2",
        stage_candidate="Stage2",
        stage1_date=date(2024, 7, 25),
        stage2_date=date(2024, 7, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        hard_4c_confirmed=False,
        trigger_outcome_label="evidence_good_but_price_data_incomplete",
        stage_gate_correction="loss beat and Apple OLED orders are Stage2, but no Green without sustained profitability",
        evidence_fields=("Q2_operating_loss_94B_vs_expected_308B", "revenue_growth_42pct", "Apple_OLED_iPad_orders", "iPhone_Pro_Max_OLED_orders"),
        red_flag_fields=("second_half_profitability_guidance_refused", "panel_demand_uncertainty", "sustained_profitability_missing", "price_anchor_missing"),
        price_data_source="Reuters LG Display result anchor; no event price anchor",
        reported_price_anchor="no price anchor",
        reported_return_anchor="loss beat and revenue +42%, but price unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        market_relative_return_pp=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"trigger_date": "2024-07-25", "q2_operating_loss_krw_bn": 94, "expected_q2_loss_krw_bn": 308, "loss_beat_amount_krw_bn": 214, "prior_year_loss_krw_bn": 881, "revenue_krw_trn": 6.7, "revenue_growth_pct": 42, "apple_oled_ipad_orders": True, "iphone_pro_max_16_oled_orders": True, "second_half_profitability_guidance_refused": True, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="evidence_good_but_price_data_incomplete",
        rerating_result="unknown",
        round_rerating_label="display_stage2_until_sustained_profitability",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="profitability_guidance_and_price_validation_missing",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Apple OLED and loss beat are Stage2 evidence, but profitability guidance and price validation are missing.",
    ),
    Round297CaseCandidate(
        case_id="r2_loop15_samsung_labor_supply_chain_4c",
        symbol="005930",
        company_name="Samsung Electronics",
        primary_archetype=E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C,
        secondary_archetypes=(E2RArchetype.LABOR_SUPPLY_CHAIN_4C_WATCH, E2RArchetype.SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH),
        case_type="4c_thesis_break",
        round_case_type="4C-watch",
        best_trigger="T2",
        best_trigger_type="4C-watch",
        stage_candidate="4C-watch",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 19),
        hard_4c_confirmed=False,
        trigger_outcome_label="thesis_break_watch",
        stage_gate_correction="memory upcycle scoring must include labor continuity and production continuity overlay",
        evidence_fields=("union_talks_fail", "48000_workers", "18_day_strike_risk", "DRAM_supply_impact_3_to_4pct", "NAND_supply_impact_2_to_3pct"),
        red_flag_fields=("bonus_dispute", "government_mediation", "production_continuity_not_confirmed", "hard_4c_not_confirmed"),
        price_data_source="Reuters Samsung labor strike risk anchor",
        reported_price_anchor="no hard price anchor",
        reported_return_anchor="strike risk without confirmed supply disruption",
        event_mfe_pct=None,
        event_mae_pct=None,
        market_relative_return_pp=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"trigger_date": "2026-05-19", "strike_workers_count": 48000, "strike_days": 18, "union_profit_share_demand_pct": 15, "potential_dram_supply_impact_pct": "3-4", "potential_nand_supply_impact_pct": "2-3", "government_gdp_impact_estimate_pp": 0.5, "hard_4c_confirmed": False, "full_ohlc_status": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="labor_continuity_4c_watch",
        stage_failure_type="unknown",
        round_stage_failure_label="watch_not_hard_4c_until_strike_disrupts_supply",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Labor continuity is a memory supply-chain 4C overlay even when the AI memory cycle is strong.",
    ),
)


def round297_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(_case_record(case) for case in ROUND297_CASE_CANDIDATES)


def round297_summary() -> dict[str, object]:
    cases = ROUND297_CASE_CANDIDATES
    return {
        "source_round": ROUND297_SOURCE_ROUND_PATH,
        "round_id": ROUND297_ANALYST_ROUND_ID,
        "large_sector": ROUND297_LARGE_SECTOR,
        "method": ROUND297_METHOD,
        "case_candidate_count": len(cases),
        "trigger_count": len(ROUND297_TRIGGER_RECORDS),
        "stage2_actionable_candidate_count": sum(1 for case in cases if case.stage2_date is not None),
        "stage3_yellow_candidate_count": sum(1 for case in cases if "Stage3-Yellow" in case.stage_candidate or "Stage3-Yellow" in case.best_trigger_type),
        "stage3_green_candidate_count": sum(1 for case in cases if "Green" in case.stage_candidate),
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.round_case_type or case.stage4b_date is not None),
        "stage4c_watch_count": sum(1 for case in cases if "4C" in case.round_case_type or case.stage4c_date is not None),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "missed_structural_count": sum(1 for case in cases if case.stage_failure_type == "missed_structural"),
        "reported_event_anchor_case_count": sum(1 for case in cases if case.price_validation_status == "reported_event_anchor_not_full_ohlc"),
        "price_data_incomplete_count": sum(1 for case in cases if "incomplete" in case.round_alignment_label),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round297_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(_case_row(case) for case in ROUND297_CASE_CANDIDATES)


def round297_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND297_TRIGGER_RECORDS)


def round297_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND297_REQUIRED_TARGET_ALIASES.items())


def round297_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND297_SCORE_ADJUSTMENTS)


def round297_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND297_SHADOW_WEIGHT_ROWS)


def round297_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND297_SOURCE_ROUND_PATH,
        "round_id": ROUND297_ANALYST_ROUND_ID,
        "large_sector": ROUND297_LARGE_SECTOR,
        "method": ROUND297_METHOD,
        "summary": round297_summary(),
        "target_aliases": dict(ROUND297_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND297_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND297_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND297_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND297_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND297_SCORE_UP_AXES),
        "score_down_axes": list(ROUND297_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND297_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND297_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND297_CASE_CANDIDATES],
        "trigger_ids": [trigger.trigger_id for trigger in ROUND297_TRIGGER_RECORDS],
        "what_not_to_change": [
            "do_not_apply_round297_shadow_weights_to_production_scoring_yet",
            "do_not_use_round297_cases_as_candidate_generation_input",
            "do_not_force_stage3_green_without_full_ohlc_and_margin_allocation_confirmation",
            "do_not_treat_AI_HBM_theme_only_as_revenue_margin_evidence",
            "do_not_ignore_4b_4c_overlays_after_parabolic_rally_or_supply_chain_risk",
        ],
    }


def render_round297_summary_markdown() -> str:
    summary = round297_summary()
    lines = [
        "# Round 297 R2 Loop 15 AI/Semiconductor Trigger-Level Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- method: {summary['method']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- triggers: {summary['trigger_count']}",
        f"- Stage2-Actionable candidates: {summary['stage2_actionable_candidate_count']}",
        f"- Stage3-Yellow candidates: {summary['stage3_yellow_candidate_count']}",
        f"- Stage3-Green candidates: {summary['stage3_green_candidate_count']}",
        f"- Stage3-Green confirmed: {summary['stage3_green_confirmed_count']}",
        f"- 4B watch cases: {summary['stage4b_watch_count']}",
        f"- 4C watch cases: {summary['stage4c_watch_count']}",
        "- price_validation_completed: partial_with_reported_event_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | best trigger | candidate | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND297_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.best_trigger,
                    case.stage_candidate,
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
            "- SK Hynix is the key missed-structural case if HBM mix, OP revision and mass-production triggers stay plain Stage2.",
            "- Hanmi Semiconductor shows named customer + HBM equipment + repeat order + relative strength can be Stage2-Actionable.",
            "- Samsung Electronics is late catch-up; relative-strength discount and labor 4C overlay block Green.",
            "- OpenAI/Stargate and ASML validate memory demand, but after a parabolic rally they require 4B overlay.",
            "- Export-control and labor continuity are explicit 4C overlays in the AI-memory cycle.",
            "- LG Innotek is Stage2-Actionable; LG Display remains Stage2 until sustained profitability and price validation appear.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round297_trigger_grid_markdown() -> str:
    company_by_case = {case.case_id: case.company_name for case in ROUND297_CASE_CANDIDATES}
    lines = [
        "# Round 297 Trigger Grid",
        "",
        "Trigger-level validation separates evidence timing from full OHLC completion. For example, `HBM3E mass production + +9% event move` can support Stage3-Yellow while 90D/180D MFE is still missing.",
        "",
        "| trigger | case | company | type | date | evidence | event return | relative | promote_to |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND297_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {company_by_case.get(trigger.case_id, '')} | {trigger.trigger_type} | {trigger.trigger_date.isoformat()} | "
            f"{trigger.evidence_available} | {_value_text(trigger.event_return_pct)} | {_value_text(trigger.market_relative_return_pp)} | {trigger.promote_to} |"
        )
    return "\n".join(lines) + "\n"


def render_round297_stage_rules_markdown() -> str:
    lines = [
        "# Round 297 Stage2-Actionable / Stage3-Yellow Rules",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Stage2-Actionable Promotion Rules",
        "",
    ]
    lines.extend(f"- {rule}" for rule in ROUND297_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow Rules", ""])
    lines.extend(f"- {rule}" for rule in ROUND297_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Stage3-Green Rules", ""])
    lines.extend(f"- {rule}" for rule in ROUND297_STAGE3_GREEN_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND297_GREEN_BLOCKERS)
    lines.extend(["", "## Easy Examples", ""])
    lines.extend(
        [
            "- `HBM mass production + OP estimate raise + relative strength` can be Stage3-Yellow before record profit is printed.",
            "- `OpenAI headline after +200% rally` is not just Green evidence; it also creates 4B-watch.",
            "- `Apple AI upgrade + OP estimate beat` can be Stage2-Actionable, but Green waits for sell-through and component margin.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round297_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 297 R2 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND297_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND297_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "이번 R2 Loop 15에서 hard 4C 확정은 없다. China equipment restriction and Samsung labor strike are 4C-watch until license denial, production disruption, or shipment delay is confirmed.",
            "",
            "## Case Review",
            "",
            "| case | company | 4B date | 4C watch | hard 4C | interpretation |",
            "|---|---|---|---|---|---|",
        ]
    )
    for case in ROUND297_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.company_name} | {_date_text(case.stage4b_date)} | {_date_text(case.stage4c_date)} | "
            f"{str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round297_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 297 R2 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_event_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Stage candidates are not downgraded merely because full OHLC is missing.",
        "- Do not invent 30D/90D/180D/1Y MFE/MAE, customer allocation, sell-through, margin, or labor settlement data.",
        "",
        "## Case Anchors",
        "",
        "| case | data source | reported anchor | status |",
        "|---|---|---|---|",
    ]
    for case in ROUND297_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round297_r2_loop15_reports(
    output_directory: str | Path = ROUND297_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND297_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND297_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND297_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND297_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round297_case_records(), cases_path),
        "triggers": write_round297_triggers(triggers_path),
        "audit": _write_json(round297_audit_payload(), audit_path),
        "weight_profile": _write_csv(round297_shadow_weight_rows(), weight_profile_path),
        "summary": output / "round297_r2_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round297_r2_loop15_case_matrix.csv",
        "trigger_grid": output / "round297_r2_loop15_trigger_grid.csv",
        "target_aliases": output / "round297_r2_loop15_target_aliases.csv",
        "score_adjustments": output / "round297_r2_loop15_score_adjustments.csv",
        "shadow_weights": output / "round297_r2_loop15_shadow_weights.csv",
        "stage_rules": output / "round297_r2_loop15_stage_rules.md",
        "trigger_grid_md": output / "round297_r2_loop15_trigger_grid.md",
        "price_validation_plan": output / "round297_r2_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round297_r2_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round297_summary_markdown(), encoding="utf-8")
    _write_csv(round297_case_rows(), paths["case_matrix"])
    _write_csv(round297_trigger_rows(), paths["trigger_grid"])
    _write_csv(round297_target_alias_rows(), paths["target_aliases"])
    _write_csv(round297_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round297_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round297_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round297_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round297_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round297_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round297_triggers(path: str | Path = ROUND297_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND297_TRIGGER_RECORDS]
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return target


def _case_record(case: Round297CaseCandidate) -> E2RCaseRecord:
    return E2RCaseRecord(
        case_id=case.case_id,
        symbol=case.symbol,
        company_name=case.company_name,
        market="KR",
        sector_raw=ROUND297_LARGE_SECTOR,
        primary_archetype=case.primary_archetype,
        expected_group=case.expected_group,
        large_sector=ROUND297_LARGE_SECTOR,
        secondary_archetypes=case.secondary_archetypes,
        case_type=case.case_type,
        stage1_date=case.stage1_date,
        stage2_date=case.stage2_date,
        stage3_date=case.stage3_date,
        stage4b_date=case.stage4b_date,
        stage4c_date=case.stage4c_date,
        evidence_summary=case.notes,
        stage1_evidence=case.evidence_fields if case.stage1_date else (),
        stage2_evidence=case.evidence_fields if case.stage2_date else (),
        stage3_evidence=case.evidence_fields if case.stage3_date else (),
        stage4b_evidence=case.red_flag_fields if case.stage4b_date else (),
        stage4c_evidence=case.red_flag_fields if case.stage4c_date else (),
        must_have_fields=ROUND297_STAGE2_ACTIONABLE_RULES + ROUND297_STAGE3_YELLOW_RULES + ROUND297_STAGE3_GREEN_RULES,
        red_flag_fields=case.red_flag_fields,
        key_evidence_fields=case.evidence_fields,
        false_positive_reason=case.round_stage_failure_label,
        score_price_alignment=case.score_price_alignment,
        rerating_result=case.rerating_result,
        stage_failure_type=case.stage_failure_type,
        price_pattern=case.round_alignment_label,
        score_weight_hint={},
        green_guardrails=(
            "production_scoring_changed_false",
            "candidate_generation_input_false",
            "shadow_weight_only_true",
            "full_adjusted_ohlc_complete_false",
            "stage_candidate_not_downgraded_for_missing_full_ohlc",
            "do_not_use_round297_cases_as_candidate_generation_input",
            "do_not_force_stage3_green_without_allocation_margin_price_path",
            "hard_4c_confirmed_false",
        ),
        notes=case.notes,
        price_validation=PriceValidation(
            stage1_price=case.stage1_price_anchor,
            stage2_price=case.stage2_price_anchor,
            stage3_price=case.stage3_price_anchor,
            stage4b_price=case.stage4b_price_anchor,
            stage4c_price=case.stage4c_price_anchor,
            mfe_30d=case.event_mfe_pct,
            mae_30d=case.event_mae_pct,
            price_validation_status=case.price_validation_status,
        ),
        data_quality=CaseDataQuality(official_data_available=False, report_data_available=True, price_data_available=False, stage_dates_confidence=0.7),
    )


def _case_row(case: Round297CaseCandidate) -> dict[str, str]:
    return {
        "case_id": case.case_id,
        "symbol": case.symbol,
        "company_name": case.company_name,
        "primary_archetype": case.primary_archetype.value,
        "secondary_archetypes": "|".join(item.value for item in case.secondary_archetypes),
        "case_type": case.case_type,
        "round_case_type": case.round_case_type,
        "best_trigger": case.best_trigger,
        "best_trigger_type": case.best_trigger_type,
        "stage_candidate": case.stage_candidate,
        "stage1_date": _date_text(case.stage1_date),
        "stage2_date": _date_text(case.stage2_date),
        "stage3_date": _date_text(case.stage3_date),
        "stage4b_date": _date_text(case.stage4b_date),
        "stage4c_date": _date_text(case.stage4c_date),
        "hard_4c_confirmed": str(case.hard_4c_confirmed).lower(),
        "trigger_outcome_label": case.trigger_outcome_label,
        "stage_gate_correction": case.stage_gate_correction,
        "evidence_fields": "|".join(case.evidence_fields),
        "red_flag_fields": "|".join(case.red_flag_fields),
        "price_data_source": case.price_data_source,
        "reported_price_anchor": case.reported_price_anchor,
        "reported_return_anchor": case.reported_return_anchor,
        "event_mfe_pct": _float_text(case.event_mfe_pct),
        "event_mae_pct": _float_text(case.event_mae_pct),
        "market_relative_return_pp": _float_text(case.market_relative_return_pp),
        "score_price_alignment": case.score_price_alignment,
        "round_alignment_label": case.round_alignment_label,
        "rerating_result": case.rerating_result,
        "round_rerating_label": case.round_rerating_label,
        "stage_failure_type": case.stage_failure_type,
        "round_stage_failure_label": case.round_stage_failure_label,
        "price_validation_status": case.price_validation_status,
        "extra_price_metrics": json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True),
        "notes": case.notes,
    }


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


def _value_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:g}"
    return str(value)
