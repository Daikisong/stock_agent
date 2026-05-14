"""Round-8 empty-archetype backfill and validation plan.

Round 8 turns the analyst notes into a report-only plan for filling empty or
thin archetypes. It strengthens score-price alignment requirements without
changing production scoring.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import E2RCaseRecord, load_case_library


ROUND8_SOURCE_ROUND_PATH = "docs/round/round_08.md"


class Round8BackfillPriority(str, Enum):
    """Backfill priority from Round 8."""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    WATCH = "WATCH"
    REDTEAM = "REDTEAM"


@dataclass(frozen=True)
class Round8BackfillTarget:
    """Backfill target for one archetype or sub-archetype family."""

    archetype: E2RArchetype
    priority: Round8BackfillPriority
    focus: str
    success_case_candidates: tuple[str, ...]
    counterexample_candidates: tuple[str, ...]
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_requires: tuple[str, ...]
    stage4b_signals: tuple[str, ...]
    stage4c_signals: tuple[str, ...]
    required_alignment_fields: tuple[str, ...]
    score_weight_note: str
    green_policy: str


ROUND8_SCORE_PRICE_ALIGNMENT_VALUES = (
    "aligned",
    "false_positive_score",
    "missed_due_to_score",
    "price_moved_without_evidence",
    "evidence_good_but_price_failed",
)


ROUND8_RERATING_RESULT_VALUES = (
    "true_rerating",
    "cyclical_rerating",
    "event_premium",
    "theme_overheat",
    "no_rerating",
    "thesis_break",
    "credit_relief_rally",
    "policy_event_rerating",
)


ROUND8_PRICE_PATTERN_VALUES = (
    "straight_rerating",
    "stair_step_rerating",
    "cycle_boom_bust",
    "theme_overheat",
    "accounting_trust_break",
    "event_premium",
    "credit_relief_rally",
    "reopening_cycle",
    "policy_contract_delay",
)


ROUND8_SUCCESS_CASE_REQUIREMENTS = (
    "stage1_or_stage2_signal",
    "eps_op_fcf_or_contract_export_price_margin_evidence",
    "meaningful_price_rerating_within_6_to_24_months_after_stage2_or_stage3",
    "price_move_linked_to_evidence_not_theme",
    "stage4b_or_stage4c_explainable_after_the_fact",
)


ROUND8_COUNTEREXAMPLE_REQUIREMENTS = (
    "score_high_but_price_no_rerating",
    "price_up_without_eps_fcf",
    "event_premium_ends_then_price_falls",
    "fast_4c_after_stage3_like_signal",
)


ROUND8_BACKFILL_TARGETS: Mapping[E2RArchetype, Round8BackfillTarget] = {
    E2RArchetype.TURNAROUND_COST_RESTRUCTURING: Round8BackfillTarget(
        archetype=E2RArchetype.TURNAROUND_COST_RESTRUCTURING,
        priority=Round8BackfillPriority.HIGH,
        focus="적자에서 흑자 전환이 아니라 비용구조 변화와 FCF 지속성을 검증한다.",
        success_case_candidates=("적자사업 매각 기업", "비용구조 개선 제조/플랫폼", "구조조정 후 순현금 전환 기업"),
        counterexample_candidates=("일회성 비용절감 기업", "구조조정 실패 기업", "유동성 악화/유증 반복 기업"),
        stage1_signals=("loss_reduction", "cost_cut_plan", "asset_or_business_sale", "debt_refinancing"),
        stage2_signals=("op_turnaround", "fcf_improvement", "net_debt_reduction", "two_quarters_cost_structure_improvement"),
        stage3_requires=("revenue_growth_plus_cost_structure_change", "opm_breaks_prior_band", "old_distressed_frame_remains"),
        stage4b_signals=("turnaround_fully_known", "valuation_normalized", "cost_cut_effect_peaks"),
        stage4c_signals=("loss_reappears", "liquidity_worsens", "rights_or_cb", "fixed_cost_leverage_reverses"),
        required_alignment_fields=("opm_improvement", "fcf_improvement", "net_debt_reduction", "no_one_off_cost_cut"),
        score_weight_note="EPS/FCF and mispricing matter; bottleneck score should stay low unless pricing power exists.",
        green_policy="Green only after durable OP/FCF improvement, not one-time cost cuts.",
    ),
    E2RArchetype.COMMODITY_SPREAD: Round8BackfillTarget(
        archetype=E2RArchetype.COMMODITY_SPREAD,
        priority=Round8BackfillPriority.REDTEAM,
        focus="Refining, chemical, steel/metal spread를 분리하고 중국 공급과잉/재고 반례를 채운다.",
        success_case_candidates=("refining_spread_recovery", "steel_spread_recovery", "cost_curve_advantaged_metal_case"),
        counterexample_candidates=("chemical_china_oversupply", "spread_reversal", "inventory_loss_after_price_spike"),
        stage1_signals=("spread_improvement", "product_price_up", "inventory_gain_possible"),
        stage2_signals=("op_eps_revision", "utilization_up", "demand_recovery"),
        stage3_requires=("structural_supply_shortage", "long_term_cost_advantage", "capacity_discipline"),
        stage4b_signals=("spread_peak", "everyone_recognizes_commodity_upcycle"),
        stage4c_signals=("spread_down", "demand_slowdown", "inventory_loss", "china_capacity_pressure"),
        required_alignment_fields=("spread_data", "op_eps_revision", "inventory_status", "capacity_or_supply_discipline"),
        score_weight_note="Use cyclicality caps; spread improvement alone cannot justify structural Green.",
        green_policy="RedTeam-first; Green is very restricted without structural supply constraint.",
    ),
    E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE: Round8BackfillTarget(
        archetype=E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE,
        priority=Round8BackfillPriority.MEDIUM,
        focus="완성차는 hybrid/mix/shareholder return과 저PBR 프레임 해소를 검증한다.",
        success_case_candidates=("Hyundai Motor hybrid/shareholder return", "Kia mix/shareholder return"),
        counterexample_candidates=("tariff_or_policy_margin_hit", "peak_margin_after_buyback", "recall_or_quality_cost"),
        stage1_signals=("hybrid_or_ev_strategy_change", "sales_target_up", "buyback_or_dividend_plan"),
        stage2_signals=("op_eps_revision", "high_margin_mix", "north_america_global_sales", "return_execution"),
        stage3_requires=("roe_fcf_durability", "valuation_discount_removed", "capital_allocation_improves"),
        stage4b_signals=("shareholder_return_fully_priced", "mix_improvement_fully_priced", "peak_margin_concern"),
        stage4c_signals=("demand_slowdown", "tariff_or_policy_risk", "cost_up", "recall_quality_cost"),
        required_alignment_fields=("op_eps_revision", "mix_improvement", "fcf", "shareholder_return_execution"),
        score_weight_note="Capital allocation deserves explicit credit, but tariff and peak-margin risk must cap Green.",
        green_policy="Watch/Yellow first; Green needs ROE/FCF durability plus executed return.",
    ),
    E2RArchetype.AUTO_MOBILITY_COMPONENTS: Round8BackfillTarget(
        archetype=E2RArchetype.AUTO_MOBILITY_COMPONENTS,
        priority=Round8BackfillPriority.MEDIUM,
        focus="부품주는 고객 다변화와 원가전가가 완성차보다 더 중요하다.",
        success_case_candidates=("ADAS_component_customer_diversification", "electronics_mix_component", "cost_pass_through_component"),
        counterexample_candidates=("single_customer_dependency", "ev_demand_slowdown_component", "cost_pass_through_failure"),
        stage1_signals=("adas_or_electronics_keyword", "new_customer", "mobility_order"),
        stage2_signals=("customer_diversification", "opm_improvement", "cost_pass_through", "op_eps_revision"),
        stage3_requires=("durable_content_per_vehicle_growth", "multi_customer_visibility", "fcf_conversion"),
        stage4b_signals=("ev_or_adas_expectation_fully_priced", "customer_order_peak"),
        stage4c_signals=("ev_demand_slowdown", "inventory_build", "customer_capex_or_model_delay", "margin_squeeze"),
        required_alignment_fields=("customer_diversification", "opm_improvement", "cost_pass_through", "inventory_status"),
        score_weight_note="Do not score EV theme without customer diversification and margin evidence.",
        green_policy="Watch/Yellow first; Green needs multi-customer revenue and margin proof.",
    ),
    E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET: Round8BackfillTarget(
        archetype=E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        priority=Round8BackfillPriority.HIGH,
        focus="ROE-PBR-CET1-주주환원 실행으로 value trap을 분리한다.",
        success_case_candidates=("KB금융", "신한지주", "하나금융", "메리츠금융", "삼성화재", "DB손해보험"),
        counterexample_candidates=("low_pbr_without_roe", "pf_credit_cost_financial", "capital_ratio_weak_insurer_or_broker"),
        stage1_signals=("value_up_disclosure", "buyback_or_dividend", "low_pbr"),
        stage2_signals=("roe_improvement", "cet1_stable", "credit_cost_stable", "return_execution"),
        stage3_requires=("pbr_roe_frame_change", "recurring_roe", "credible_shareholder_return", "low_credit_risk"),
        stage4b_signals=("pbr_normalized", "everyone_recognizes_valueup_success"),
        stage4c_signals=("credit_cost_up", "pf_stress", "capital_ratio_down", "return_policy_retreat"),
        required_alignment_fields=("roe", "pbr", "cet1_or_capital_ratio", "shareholder_return_execution", "credit_cost"),
        score_weight_note="Valuation and capital allocation weights are central; low PBR alone is not evidence.",
        green_policy="Green-eligible only with ROE, capital strength, credit-cost control, and executed return.",
    ),
    E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN: Round8BackfillTarget(
        archetype=E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        priority=Round8BackfillPriority.HIGH,
        focus="저PBR/지주 이벤트와 실제 자사주 소각, 반복 환원, NAV/FCF 개선을 분리한다.",
        success_case_candidates=("SK Square buyback/cancellation", "holding_company_repeat_return"),
        counterexample_candidates=("buyback_without_cancel", "event_premium_only_governance", "subsidiary_value_impairment"),
        stage1_signals=("value_up_disclosure", "buyback_plan", "holding_discount_keyword"),
        stage2_signals=("buyback_cancellation", "repeat_return_policy", "subsidiary_value_support"),
        stage3_requires=("governance_regime_change", "nav_discount_structural_narrowing", "repeat_return"),
        stage4b_signals=("event_premium_fully_priced", "discount_narrowing_completed"),
        stage4c_signals=("return_not_executed", "governance_risk_reappears", "subsidiary_value_down"),
        required_alignment_fields=("nav_discount", "buyback_cancellation", "fcf_support", "governance_execution"),
        score_weight_note="Event premium should not be treated as true rerating unless NAV/FCF and return execution align.",
        green_policy="Green needs executed return and durable NAV/FCF support.",
    ),
    E2RArchetype.CDMO_HEALTHCARE_CONTRACT: Round8BackfillTarget(
        archetype=E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        priority=Round8BackfillPriority.HIGH,
        focus="CDMO는 pre-revenue biotech이 아니라 장기계약, capacity, 가동률, FCF archetype이다.",
        success_case_candidates=("Samsung Biologics", "Celltrion", "Samsung Bioepis", "global_cdmo_peer"),
        counterexample_candidates=("capacity_overbuild", "utilization_down", "patent_litigation", "price_competition"),
        stage1_signals=("large_production_contract", "capacity_expansion", "global_site_expansion"),
        stage2_signals=("utilization_up", "op_revenue_revision", "long_term_contract", "customer_diversification"),
        stage3_requires=("multi_year_production_visibility", "high_fcf_conversion", "contract_utilization_margin_alignment"),
        stage4b_signals=("capacity_expectation_overheated", "valuation_saturated", "new_plant_expectation_fully_priced"),
        stage4c_signals=("utilization_down", "contract_delay", "patent_litigation", "price_competition"),
        required_alignment_fields=("long_term_contract", "capacity_utilization", "customer_diversification", "fcf_conversion"),
        score_weight_note="Score contracted utilization, not biological trial narrative.",
        green_policy="Green-eligible after utilization, FCF, customer, and litigation checks.",
    ),
    E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION: Round8BackfillTarget(
        archetype=E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION,
        priority=Round8BackfillPriority.WATCH,
        focus="Approval -> commercialization -> royalty/revenue 경로를 pre-revenue 임상 뉴스와 분리한다.",
        success_case_candidates=("Yuhan/Lazertinib", "Alteogen", "royalty_visibility_biotech"),
        counterexample_candidates=("clinical_headline_only", "unclear_royalty_tech_transfer", "partner_termination", "cb_dilution"),
        stage1_signals=("clinical_or_approval_news", "tech_transfer", "partner_validation"),
        stage2_signals=("approval_probability", "milestone_payment", "partner_launch_progress"),
        stage3_requires=("actual_royalty_or_revenue", "eps_fcf_conversion", "low_dilution_risk", "repeat_revenue_visibility"),
        stage4b_signals=("drug_expectation_overheated", "valuation_ahead_of_revenue"),
        stage4c_signals=("clinical_failure", "approval_delay", "partner_termination", "rights_or_cb"),
        required_alignment_fields=("approval", "commercialization", "royalty_or_revenue", "dilution_risk"),
        score_weight_note="Pre-revenue weight stays capped; royalty/revenue conversion can raise visibility.",
        green_policy="Watch/Yellow by default; Green needs actual royalty/revenue conversion.",
    ),
    E2RArchetype.PLATFORM_SOFTWARE_INTERNET: Round8BackfillTarget(
        archetype=E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        priority=Round8BackfillPriority.WATCH,
        focus="좋은 회사와 E2R 성공사례를 분리하고 ARPU/OPM/FCF를 확인한다.",
        success_case_candidates=("NAVER_if_OP_FCF_rerates", "Duzon_Bizon_SaaS_candidate"),
        counterexample_candidates=("Kakao_governance_legal", "MAU_only_platform", "AI_cost_margin_pressure"),
        stage1_signals=("mau_or_traffic_recovery", "ads_commerce_recovery", "cost_cut", "ai_cloud_new_business"),
        stage2_signals=("arpu_up", "take_rate_up", "opm_improvement", "fy1_fy2_op_revision", "recurring_revenue_up"),
        stage3_requires=("recurring_revenue_lock_in", "cost_leverage", "low_regulation_risk", "ai_cost_not_hurting_fcf"),
        stage4b_signals=("ai_narrative_overheated", "multiple_expansion_done", "arpu_growth_slowdown"),
        stage4c_signals=("regulation", "governance_legal_risk", "ai_cost_overrun", "take_rate_down"),
        required_alignment_fields=("arpu", "take_rate", "opm", "fcf", "governance_risk"),
        score_weight_note="Do not score MAU or AI narrative unless monetization and FCF follow.",
        green_policy="Watch/Yellow first; Green requires monetization, FCF, and low governance risk.",
    ),
    E2RArchetype.SHIPPING_FREIGHT_CYCLE: Round8BackfillTarget(
        archetype=E2RArchetype.SHIPPING_FREIGHT_CYCLE,
        priority=Round8BackfillPriority.REDTEAM,
        focus="EPS 폭발이 가능하지만 운임 정상화/overcapacity로 cycle boom-bust를 분리한다.",
        success_case_candidates=("HMM_2020_2021_cycle", "Maersk_boom_cycle"),
        counterexample_candidates=("overcapacity_after_freight_peak", "spot_rate_collapse", "new_vessel_supply"),
        stage1_signals=("freight_rate_spike", "container_shortage", "spot_rate_spike"),
        stage2_signals=("contract_freight_reflects", "op_eps_explosion"),
        stage3_requires=("multi_year_contract_freight", "fleet_supply_constraint", "not_spot_only"),
        stage4b_signals=("freight_peak", "new_vessel_supply", "spot_future_divergence"),
        stage4c_signals=("freight_collapse", "overcapacity", "demand_slowdown"),
        required_alignment_fields=("freight_rate", "contract_vs_spot", "new_vessel_supply", "op_eps_revision"),
        score_weight_note="Use as Red/4B defense; cyclical success is not structural Green.",
        green_policy="Green highly restricted; classify boom-bust explicitly.",
    ),
    E2RArchetype.NUCLEAR_SMR_GRID_POLICY: Round8BackfillTarget(
        archetype=E2RArchetype.NUCLEAR_SMR_GRID_POLICY,
        priority=Round8BackfillPriority.WATCH,
        focus="원전은 정책 + 수주 + 법적 리스크 + 기자재 매출화 archetype이다.",
        success_case_candidates=("KHNP_Czech_if_contract_economics", "Doosan_Enerbility", "KEPCO_Engineering"),
        counterexample_candidates=("legal_appeal_delay", "policy_contract_delay", "cost_overrun_or_project_delay"),
        stage1_signals=("nuclear_policy", "preferred_bidder", "smr_theme"),
        stage2_signals=("contract_or_loi", "project_financing", "supplier_revenue_path", "legal_risk_reduced"),
        stage3_requires=("multi_year_backlog", "margin_confirmed", "low_legal_policy_risk", "fy2_fy3_revenue_basis"),
        stage4b_signals=("nuclear_expectation_priced", "theme_group_overheated"),
        stage4c_signals=("lawsuit_loss_or_delay", "policy_reversal", "project_delay", "cost_up"),
        required_alignment_fields=("contract_economics", "legal_risk", "project_financing", "supplier_revenue_path"),
        score_weight_note="Policy headlines stay Stage 1/2 until contract economics and legal risk are resolved.",
        green_policy="Watch/Yellow first; use policy_contract_delay pattern when legal risk appears.",
    ),
    E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE: Round8BackfillTarget(
        archetype=E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        priority=Round8BackfillPriority.HIGH,
        focus="AI 데이터센터 capex가 전력기기, 전선, IDC, 냉각, PCB, ESS로 번지는지 검증한다.",
        success_case_candidates=("HD현대일렉트릭/효성중공업 AI power", "LS ELECTRIC/전선", "이수페타시스", "cooling_hvac_candidate"),
        counterexample_candidates=("ai_keyword_without_order", "ai_capex_cut", "data_center_project_delay"),
        stage1_signals=("data_center_capex_news", "power_shortage_keyword", "cooling_or_grid_keyword"),
        stage2_signals=("confirmed_order_or_contract", "customer_capex_visibility", "op_eps_revision"),
        stage3_requires=("multi_year_capex_visibility", "critical_bottleneck_position", "supply_constraint", "pricing_power"),
        stage4b_signals=("ai_capex_narrative_overheated", "new_capacity_concern"),
        stage4c_signals=("ai_capex_cut", "data_center_delay", "grid_or_permit_bottleneck", "order_delay_or_cancel"),
        required_alignment_fields=("confirmed_order", "customer_capex_visibility", "capacity_bottleneck", "op_eps_revision"),
        score_weight_note="Score confirmed AI infrastructure exposure above keywords.",
        green_policy="Green-eligible with orders, bottleneck, EPS revision, and project delay checks.",
    ),
    E2RArchetype.MEMORY_HBM_CAPACITY: Round8BackfillTarget(
        archetype=E2RArchetype.MEMORY_HBM_CAPACITY,
        priority=Round8BackfillPriority.HIGH,
        focus="SK Hynix류 성공과 4B-watch를 동시에 캘리브레이션한다.",
        success_case_candidates=("SK_Hynix_stage3_success", "Samsung_memory_recovery_candidate"),
        counterexample_candidates=("simple_dram_rebound", "sk_hynix_4b_watch_after_large_run", "ai_capex_or_price_downturn"),
        stage1_signals=("hbm_demand", "memory_price_up", "earnings_turnaround"),
        stage2_signals=("fy1_fy2_fy3_revision", "customer_supply_race", "supply_discipline", "price_up"),
        stage3_requires=("long_term_contract_or_prepayment", "price_band", "capa_constraint", "multi_year_consensus_revision", "pbr_to_per_frame_shift"),
        stage4b_signals=("one_to_two_year_price_surge", "market_cap_or_multiple_saturated", "customer_price_resistance", "capex_expansion_news"),
        stage4c_signals=("hbm_dram_nand_price_down", "ai_capex_slowdown", "supply_glut", "consensus_revision_down"),
        required_alignment_fields=("hbm_demand", "memory_price", "supply_discipline", "long_term_contract_or_prepayment", "revision"),
        score_weight_note="Use memory success and 4B-watch together; do not mistake full rerating for fresh Green.",
        green_policy="Green-eligible early; after massive rerating, move to 4B-watch diagnostics.",
    ),
}


def round8_target_for(archetype: E2RArchetype | str) -> Round8BackfillTarget | None:
    return ROUND8_BACKFILL_TARGETS.get(_archetype(archetype))


def round8_backfill_rows() -> tuple[dict[str, object], ...]:
    rows: list[dict[str, object]] = []
    for target in ROUND8_BACKFILL_TARGETS.values():
        rows.append(
            {
                "archetype": target.archetype.value,
                "priority": target.priority.value,
                "focus": target.focus,
                "success_case_candidates": "|".join(target.success_case_candidates),
                "counterexample_candidates": "|".join(target.counterexample_candidates),
                "required_alignment_fields": "|".join(target.required_alignment_fields),
                "green_policy": target.green_policy,
            }
        )
    return tuple(rows)


def round8_case_gaps(records: Iterable[E2RCaseRecord]) -> tuple[dict[str, object], ...]:
    record_tuple = tuple(records)
    rows: list[dict[str, object]] = []
    for target in ROUND8_BACKFILL_TARGETS.values():
        subset = tuple(record for record in record_tuple if record.primary_archetype == target.archetype)
        positive = tuple(record for record in subset if record.case_type in {"structural_success", "success_candidate", "cyclical_success"})
        counter = tuple(
            record
            for record in subset
            if record.case_type in {"one_off", "overheat", "failed_rerating", "event_premium", "4b_watch", "4c_thesis_break"}
        )
        rows.append(
            {
                "archetype": target.archetype.value,
                "priority": target.priority.value,
                "case_count": len(subset),
                "positive_count": len(positive),
                "counterexample_count": len(counter),
                "needs_price_backfill_count": sum(
                    1 for record in subset if record.price_validation.price_validation_status != "price_filled"
                ),
                "unknown_alignment_count": sum(1 for record in subset if record.score_price_alignment == "unknown"),
                "recommended_action": _recommended_action(target, subset, positive, counter),
            }
        )
    return tuple(rows)


def write_round8_empty_archetype_reports(
    *,
    case_path: str | Path = "data/e2r_case_library/cases_v02.jsonl",
    output_directory: str | Path = "output/e2r_round8_empty_archetype_backfill",
) -> dict[str, Path]:
    records = load_case_library(case_path)
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "framework": output / "round8_empty_archetype_backfill_framework.md",
        "target_matrix": output / "round8_backfill_target_matrix.csv",
        "gap_report": output / "round8_case_gap_report.md",
        "price_pattern_contract": output / "round8_price_pattern_contract.md",
        "next_plan": output / "round8_next_case_record_plan.md",
    }
    paths["framework"].write_text(render_round8_framework_markdown(), encoding="utf-8")
    _write_target_matrix(paths["target_matrix"])
    paths["gap_report"].write_text(render_round8_gap_report_markdown(records), encoding="utf-8")
    paths["price_pattern_contract"].write_text(render_round8_price_pattern_contract_markdown(), encoding="utf-8")
    paths["next_plan"].write_text(render_round8_next_plan_markdown(records), encoding="utf-8")
    return paths


def render_round8_framework_markdown() -> str:
    lines = [
        "# Round-8 Empty-Archetype Backfill Framework",
        "",
        f"Source round: `{ROUND8_SOURCE_ROUND_PATH}`",
        "",
        "이 문서는 calibration 전용이다. production scoring과 StageClassifier threshold를 바꾸지 않는다.",
        "",
        "## 핵심",
        "",
        "Round 8은 빈 archetype과 얇은 archetype을 성공/반례/가격경로까지 채우기 위한 계획이다.",
        "",
        "쉬운 예시:",
        "",
        "`흑자전환`이 한 번 나왔다고 성공이 아니다. OPM과 FCF가 2분기 이상 이어지고 주가가 그 이후 리레이팅돼야 성공 후보가 된다.",
        "",
        "## Targets",
        "",
        "| archetype | priority | focus |",
        "|---|---|---|",
    ]
    for target in ROUND8_BACKFILL_TARGETS.values():
        lines.append(f"| {target.archetype.value} | {target.priority.value} | {target.focus} |")
    lines.extend(
        [
            "",
            "## Guardrails",
            "- 케이스 레코드는 candidate generation input이 아니다.",
            "- Stage 3-Green을 늘리기 위해 threshold를 낮추지 않는다.",
            "- price-only, event-only, one-off EPS는 반드시 반례로 남긴다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round8_gap_report_markdown(records: Iterable[E2RCaseRecord]) -> str:
    rows = round8_case_gaps(records)
    lines = [
        "# Round-8 Case Gap Report",
        "",
        "| archetype | priority | cases | positive | counter | needs_price | unknown_alignment | recommended_action |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['archetype']} | {row['priority']} | {row['case_count']} | {row['positive_count']} | "
            f"{row['counterexample_count']} | {row['needs_price_backfill_count']} | "
            f"{row['unknown_alignment_count']} | {row['recommended_action']} |"
        )
    return "\n".join(lines) + "\n"


def render_round8_price_pattern_contract_markdown() -> str:
    lines = [
        "# Round-8 Price Pattern Contract",
        "",
        "Round 8 requires every serious case record to separate evidence, price, and later lifecycle.",
        "",
        "## Score-Price Alignment",
    ]
    for item in ROUND8_SCORE_PRICE_ALIGNMENT_VALUES:
        lines.append(f"- `{item}`")
    lines.extend(["", "## Rerating Result"])
    for item in ROUND8_RERATING_RESULT_VALUES:
        lines.append(f"- `{item}`")
    lines.extend(["", "## Price Pattern"])
    for item in ROUND8_PRICE_PATTERN_VALUES:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "",
            "- `policy_contract_delay`: 원전처럼 수주 기대는 있지만 소송/정책 지연이 가격 경로를 흔드는 경우.",
            "- `credit_relief_rally`: 건설처럼 유동성 지원으로 반등했지만 PF와 cash flow가 아직 해결되지 않은 경우.",
            "- `cycle_boom_bust`: 해운처럼 EPS가 폭발했지만 운임 정상화로 빠르게 꺾이는 경우.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round8_next_plan_markdown(records: Iterable[E2RCaseRecord]) -> str:
    rows = round8_case_gaps(records)
    empty = [row for row in rows if int(row["case_count"]) == 0]
    needs_price = sum(int(row["needs_price_backfill_count"]) for row in rows)
    lines = [
        "# Round-8 Next Case Record Plan",
        "",
        f"- target_archetypes: {len(ROUND8_BACKFILL_TARGETS)}",
        f"- empty_target_archetypes: {len(empty)}",
        f"- needs_price_backfill_total: {needs_price}",
        "",
        "## Priority",
        "",
        "1. Turnaround, Financial/Value-Up, CDMO, AI Data Center, Memory/HBM부터 가격 경로를 채운다.",
        "2. Commodity, Shipping, Construction은 Green 확장보다 cycle/4C 반례를 먼저 채운다.",
        "3. Auto, Nuclear, Platform, Royalty biotech은 Watch/Yellow 검증 케이스를 먼저 만든다.",
        "",
        "## What Not To Change",
        "",
        "- score weight를 아직 production에 적용하지 않는다.",
        "- 케이스 이름을 scoring 조건으로 쓰지 않는다.",
        "- event premium을 true rerating으로 바꾸지 않는다.",
    ]
    return "\n".join(lines) + "\n"


def _write_target_matrix(path: Path) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = (
            "archetype",
            "priority",
            "focus",
            "success_case_candidates",
            "counterexample_candidates",
            "required_alignment_fields",
            "green_policy",
        )
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in round8_backfill_rows():
            writer.writerow(row)
    return path


def _recommended_action(
    target: Round8BackfillTarget,
    records: tuple[E2RCaseRecord, ...],
    positive: tuple[E2RCaseRecord, ...],
    counter: tuple[E2RCaseRecord, ...],
) -> str:
    if not records:
        return "add_initial_success_and_counterexample_records"
    if len(positive) < 2:
        return "add_positive_or_success_candidate_cases"
    if len(counter) < 2:
        return "add_counterexample_cases"
    if any(record.price_validation.price_validation_status != "price_filled" for record in records):
        return "backfill_price_path"
    if any(record.score_price_alignment == "unknown" for record in records):
        return "classify_score_price_alignment"
    if target.priority in {Round8BackfillPriority.REDTEAM, Round8BackfillPriority.WATCH}:
        return "review_watch_or_redteam_guardrails"
    return "ready_for_shadow_score_simulation"


def _archetype(value: E2RArchetype | str) -> E2RArchetype:
    if isinstance(value, E2RArchetype):
        return value
    return E2RArchetype(str(value))


__all__ = [
    "ROUND8_BACKFILL_TARGETS",
    "ROUND8_COUNTEREXAMPLE_REQUIREMENTS",
    "ROUND8_PRICE_PATTERN_VALUES",
    "ROUND8_RERATING_RESULT_VALUES",
    "ROUND8_SCORE_PRICE_ALIGNMENT_VALUES",
    "ROUND8_SOURCE_ROUND_PATH",
    "ROUND8_SUCCESS_CASE_REQUIREMENTS",
    "Round8BackfillPriority",
    "Round8BackfillTarget",
    "render_round8_framework_markdown",
    "render_round8_gap_report_markdown",
    "render_round8_next_plan_markdown",
    "render_round8_price_pattern_contract_markdown",
    "round8_backfill_rows",
    "round8_case_gaps",
    "round8_target_for",
    "write_round8_empty_archetype_reports",
]
