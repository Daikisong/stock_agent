"""Round-7 case validation framework.

Round 7 tightens how the case library should decide whether an archetype
example is a structural E2R success or a useful counterexample. It is
calibration/report material only and is not imported by production scoring.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import E2RCaseRecord, load_case_library


ROUND7_SOURCE_ROUND_PATH = "docs/round/round_07.md"


class Round7StagePosture(str, Enum):
    """How a validated archetype should be treated before score changes."""

    GREEN_ELIGIBLE_AFTER_VALIDATION = "GREEN_ELIGIBLE_AFTER_VALIDATION"
    WATCH_YELLOW_DEFAULT = "WATCH_YELLOW_DEFAULT"
    REDTEAM_GUARDRAIL = "REDTEAM_GUARDRAIL"


class Round7ValidationBucket(str, Enum):
    """Score/price/evidence validation outcomes for case records."""

    SUCCESS_VALIDATION = "SUCCESS_VALIDATION"
    SCORE_WEIGHT_FAILURE = "SCORE_WEIGHT_FAILURE"
    PRICE_WITHOUT_EPS = "PRICE_WITHOUT_EPS"
    ONE_OFF_CYCLE_4C = "ONE_OFF_CYCLE_4C"
    EVENT_PREMIUM_ONLY = "EVENT_PREMIUM_ONLY"
    NEEDS_PRICE_PATH = "NEEDS_PRICE_PATH"
    UNCLASSIFIED = "UNCLASSIFIED"


@dataclass(frozen=True)
class Round7ArchetypeValidationRule:
    """Round-7 validation rule for one archetype."""

    archetype: E2RArchetype
    posture: Round7StagePosture
    success_requires: tuple[str, ...]
    counterexample_triggers: tuple[str, ...]
    price_validation_focus: tuple[str, ...]
    score_weight_guidance: str
    green_policy: str
    example_cases: tuple[str, ...]


ROUND7_SUCCESS_CRITERIA = (
    "evidence_score_high",
    "stage2_or_stage3_signal",
    "price_rerating_after_signal",
    "eps_op_fcf_revision_confirmed",
    "no_fast_4c",
)


ROUND7_COUNTEREXAMPLE_CRITERIA = (
    "price_up_without_eps_fcf",
    "score_high_but_price_no_rerating",
    "eps_spike_one_off",
    "fast_4c_after_stage2",
    "event_premium_only",
)


ROUND7_PRICE_VALIDATION_FIELDS = (
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "mfe_90d",
    "mfe_180d",
    "mfe_1y",
    "mae_90d",
    "mae_180d",
    "mae_1y",
    "drawdown_after_peak",
    "below_stage3_price_flag",
)


ROUND7_GREEN_ELIGIBLE_ARCHETYPES = frozenset(
    {
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
        E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
        E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG,
        E2RArchetype.EXPORT_RECURRING_CONSUMER,
        E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
        E2RArchetype.MEMORY_HBM_CAPACITY,
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        E2RArchetype.TURNAROUND_COST_RESTRUCTURING,
    }
)


ROUND7_WATCH_YELLOW_ARCHETYPES = frozenset(
    {
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        E2RArchetype.GAME_CONTENT_IP,
        E2RArchetype.ROBOTICS_FACTORY_AUTOMATION,
        E2RArchetype.AUTO_MOBILITY_COMPONENTS,
        E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE,
        E2RArchetype.NUCLEAR_SMR_GRID_POLICY,
        E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
        E2RArchetype.TRAVEL_LEISURE_REOPENING,
        E2RArchetype.EDUCATION_SPECIALTY_SERVICES,
        E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION,
    }
)


ROUND7_REDTEAM_ARCHETYPES = frozenset(
    {
        E2RArchetype.SHIPPING_FREIGHT_CYCLE,
        E2RArchetype.COMMODITY_SPREAD,
        E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
        E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,
        E2RArchetype.BIOTECH_REGULATORY,
        E2RArchetype.BIOTECH_PRE_REVENUE_REGULATORY,
        E2RArchetype.ONE_OFF_EVENT_DEMAND,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        E2RArchetype.GENERIC_UNCLASSIFIED,
    }
)


def _archetype(value: E2RArchetype | str) -> E2RArchetype:
    if isinstance(value, E2RArchetype):
        return value
    return E2RArchetype(str(value))


def round7_stage_posture_for(archetype: E2RArchetype | str) -> Round7StagePosture:
    item = _archetype(archetype)
    if item in ROUND7_GREEN_ELIGIBLE_ARCHETYPES:
        return Round7StagePosture.GREEN_ELIGIBLE_AFTER_VALIDATION
    if item in ROUND7_WATCH_YELLOW_ARCHETYPES:
        return Round7StagePosture.WATCH_YELLOW_DEFAULT
    return Round7StagePosture.REDTEAM_GUARDRAIL


def _rule(
    archetype: E2RArchetype,
    *,
    success_requires: tuple[str, ...],
    counterexample_triggers: tuple[str, ...],
    price_validation_focus: tuple[str, ...],
    score_weight_guidance: str,
    green_policy: str,
    example_cases: tuple[str, ...],
) -> Round7ArchetypeValidationRule:
    return Round7ArchetypeValidationRule(
        archetype=archetype,
        posture=round7_stage_posture_for(archetype),
        success_requires=success_requires,
        counterexample_triggers=counterexample_triggers,
        price_validation_focus=price_validation_focus,
        score_weight_guidance=score_weight_guidance,
        green_policy=green_policy,
        example_cases=example_cases,
    )


ROUND7_SPECIFIC_RULES: Mapping[E2RArchetype, Round7ArchetypeValidationRule] = {
    E2RArchetype.PLATFORM_SOFTWARE_INTERNET: _rule(
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        success_requires=(
            "arpu_or_take_rate_up",
            "opm_improvement",
            "recurring_revenue_growth",
            "fy1_fy2_op_revision",
            "ai_cost_not_hurting_fcf",
            "price_rerating_after_monetization",
        ),
        counterexample_triggers=(
            "mau_or_ai_narrative_without_op_fcf",
            "governance_or_legal_risk",
            "regulatory_pressure",
            "score_high_but_price_no_rerating",
        ),
        price_validation_focus=("mfe_180d", "mfe_1y", "below_stage3_price_flag", "score_high_but_price_no_rerating"),
        score_weight_guidance="Score monetization, OPM, and FCF; do not score MAU or AI narrative by itself.",
        green_policy="Watch/Yellow by default; Green needs monetization plus FCF and low governance/regulatory risk.",
        example_cases=("NAVER", "Kakao", "더존비즈온", "MAU-only platform"),
    ),
    E2RArchetype.GAME_CONTENT_IP: _rule(
        E2RArchetype.GAME_CONTENT_IP,
        success_requires=("actual_revenue_conversion", "repeat_ip_monetization", "global_sales", "op_eps_revision"),
        counterexample_triggers=("new_game_hype_only", "single_ip_dependence", "launch_failure", "contract_or_artist_risk"),
        price_validation_focus=("mfe_90d", "mfe_180d", "stage4c_price", "price_up_without_eps_fcf"),
        score_weight_guidance="Separate release anticipation from repeat IP revenue and OP conversion.",
        green_policy="Watch/Yellow by default; Green requires repeat monetization after launch evidence.",
        example_cases=("Krafton", "Shift Up", "HYBE/JYP/SM", "new-game hype failure"),
    ),
    E2RArchetype.TRAVEL_LEISURE_REOPENING: _rule(
        E2RArchetype.TRAVEL_LEISURE_REOPENING,
        success_requires=("visitor_or_traffic_recovery", "fixed_cost_leverage", "customer_mix_improvement", "op_eps_revision"),
        counterexample_triggers=("one_time_reopening", "oil_fx_shock", "tourism_peak", "cargo_or_route_demand_slowdown"),
        price_validation_focus=("reopening_cycle", "mfe_180d", "mae_180d", "fast_4c_after_stage2"),
        score_weight_guidance="Treat reopening as cyclical until repeated margin and FCF improvement are visible.",
        green_policy="Watch/Yellow by default; Green is exceptional because cycle risk is high.",
        example_cases=("Korean Air", "호텔신라/신세계", "파라다이스/GKL", "China-tourism-only duty free"),
    ),
    E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT: _rule(
        E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,
        success_requires=("pf_risk_resolved", "cash_flow_improvement", "debt_reduction", "cost_ratio_stable"),
        counterexample_triggers=("credit_relief_only", "pf_loss_or_unsold_inventory", "liquidity_support_only", "order_growth_with_margin_damage"),
        price_validation_focus=("credit_relief_rally", "below_stage3_price_flag", "mae_180d", "stage4c_price"),
        score_weight_guidance="Credit/PF risk dominates order score; cap visibility when liquidity is unresolved.",
        green_policy="RedTeam guardrail; Green is very restricted until PF and cash-flow risk are resolved.",
        example_cases=("PF-risk relief builder", "overseas plant order", "PF-stressed builder", "liquidity-support rally"),
    ),
    E2RArchetype.RETAIL_DOMESTIC_CONSUMER: _rule(
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        success_requires=("opm_improvement", "inventory_normalization", "same_store_sales", "customer_mix_or_pb_improvement"),
        counterexample_triggers=("traffic_only_rebound", "inventory_build", "online_competition_margin_pressure", "data_or_regulatory_issue"),
        price_validation_focus=("mfe_180d", "mae_180d", "drawdown_after_peak", "evidence_good_but_price_failed"),
        score_weight_guidance="Revenue recovery is not enough; score OPM, inventory, mix, and FCF durability.",
        green_policy="Green needs repeated margin/FCF improvement, not one-quarter consumer rebound.",
        example_cases=("BGF/GS Retail", "Shinsegae/Gmarket JV", "offline margin squeeze", "China direct-purchase pressure"),
    ),
    E2RArchetype.CDMO_HEALTHCARE_CONTRACT: _rule(
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        success_requires=("long_term_production_contract", "capacity_utilization_ramp", "customer_diversification", "fcf_conversion"),
        counterexample_triggers=("capacity_without_demand", "utilization_delay", "patent_or_litigation_risk", "price_competition"),
        price_validation_focus=("mfe_1y", "mfe_180d", "stage4c_price", "fast_4c_after_stage2"),
        score_weight_guidance="Keep CDMO separate from pre-revenue biotech; score contracted capacity and utilization.",
        green_policy="Green-eligible after long-term contract, utilization, FCF, and litigation risk checks.",
        example_cases=("Samsung Biologics", "Celltrion", "Samsung Bioepis patent litigation", "pre-revenue biotech"),
    ),
    E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION: _rule(
        E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION,
        success_requires=("approval", "commercialization_path", "royalty_or_revenue_visibility", "low_dilution_risk"),
        counterexample_triggers=("clinical_headline_only", "milestone_uncertain", "partner_termination", "cb_or_rights_dilution"),
        price_validation_focus=("event_premium", "mfe_1y", "stage4c_price", "below_stage3_price_flag"),
        score_weight_guidance="Score approval-to-commercialization-to-royalty path, not clinical headlines alone.",
        green_policy="Watch/Yellow by default; Green needs actual commercialization or royalty/revenue visibility.",
        example_cases=("Yuhan/Lazertinib", "Alteogen", "headline-only biotech", "CB/dilution biotech"),
    ),
    E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE: _rule(
        E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
        success_requires=("nav_discount_catalyst", "buyback_cancellation_or_repeat_return", "subsidiary_value_support", "governance_execution"),
        counterexample_triggers=("governance_dispute_only", "event_premium_only", "buyback_without_cancel", "subsidiary_value_impairment"),
        price_validation_focus=("event_premium", "mfe_180d", "drawdown_after_peak", "score_high_but_price_no_rerating"),
        score_weight_guidance="Separate event premium from durable NAV/FCF/shareholder-return rerating.",
        green_policy="Watch/Yellow by default; Green needs executed capital return and durable NAV/FCF support.",
        example_cases=("SK Square", "Korea Zinc", "Samsung C&T", "governance dispute only"),
    ),
    E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET: _rule(
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        success_requires=("roe_improvement", "pbr_roe_gap", "cet1_or_capital_ratio_stable", "shareholder_return_execution"),
        counterexample_triggers=("low_pbr_only", "pf_or_credit_cost_risk", "capital_ratio_deterioration", "return_policy_not_executed"),
        price_validation_focus=("mfe_1y", "below_stage3_price_flag", "score_high_but_price_no_rerating", "credit_cost_4c"),
        score_weight_guidance="Score ROE/PBR plus executed return; low PBR alone is a value trap risk.",
        green_policy="Green-eligible with ROE, capital strength, credit-cost control, and executed return.",
        example_cases=("KB금융", "신한지주/하나금융", "메리츠금융/삼성화재", "low-PBR bank without ROE"),
    ),
    E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS: _rule(
        E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS,
        success_requires=("strategic_supply_chain_role", "smelting_or_material_margin", "cash_flow_improvement", "governance_rerating_support"),
        counterexample_triggers=("metal_price_only", "takeover_premium_only", "governance_dispute_long_tail", "margin_reversal"),
        price_validation_focus=("event_premium", "commodity_cycle", "stage4b_price", "stage4c_price"),
        score_weight_guidance="Separate strategic materials bottleneck from commodity price and takeover premium.",
        green_policy="Watch/Yellow by default; Green needs supply-chain bottleneck plus FCF and governance support.",
        example_cases=("Korea Zinc", "metal-price-only smelter", "takeover premium only", "long governance dispute"),
    ),
}


def round7_rule_for(archetype: E2RArchetype | str) -> Round7ArchetypeValidationRule:
    item = _archetype(archetype)
    if item in ROUND7_SPECIFIC_RULES:
        return ROUND7_SPECIFIC_RULES[item]
    posture = round7_stage_posture_for(item)
    if posture == Round7StagePosture.GREEN_ELIGIBLE_AFTER_VALIDATION:
        return _rule(
            item,
            success_requires=ROUND7_SUCCESS_CRITERIA,
            counterexample_triggers=ROUND7_COUNTEREXAMPLE_CRITERIA,
            price_validation_focus=("mfe_180d", "mfe_1y", "below_stage3_price_flag"),
            score_weight_guidance="Eligible for future shadow scoring only after 2x2 case coverage and price validation.",
            green_policy="Green possible after EPS/FCF, visibility, price rerating, and no fast 4C are confirmed.",
            example_cases=(),
        )
    if posture == Round7StagePosture.WATCH_YELLOW_DEFAULT:
        return _rule(
            item,
            success_requires=("stage2_signal", "evidence_quality", "price_rerating_after_signal", "risk_control"),
            counterexample_triggers=ROUND7_COUNTEREXAMPLE_CRITERIA,
            price_validation_focus=("mfe_180d", "mae_180d", "drawdown_after_peak"),
            score_weight_guidance="Use Watch/Yellow until repeatability and FCF durability are proven.",
            green_policy="Default to Watch/Yellow; Green requires archetype-specific proof.",
            example_cases=(),
        )
    return _rule(
        item,
        success_requires=("hard_evidence", "cycle_or_event_risk_control", "eps_fcf_support"),
        counterexample_triggers=ROUND7_COUNTEREXAMPLE_CRITERIA,
        price_validation_focus=("stage4b_price", "stage4c_price", "drawdown_after_peak", "below_stage3_price_flag"),
        score_weight_guidance="Prioritize RedTeam and 4B/4C defense over Green expansion.",
        green_policy="Green restricted; use as counterexample/risk library first.",
        example_cases=(),
    )


def round7_archetype_validation_rows() -> tuple[dict[str, object], ...]:
    rows: list[dict[str, object]] = []
    for archetype in E2RArchetype:
        rule = round7_rule_for(archetype)
        rows.append(
            {
                "archetype": archetype.value,
                "posture": rule.posture.value,
                "success_requires": "|".join(rule.success_requires),
                "counterexample_triggers": "|".join(rule.counterexample_triggers),
                "price_validation_focus": "|".join(rule.price_validation_focus),
                "green_policy": rule.green_policy,
                "example_cases": "|".join(rule.example_cases),
            }
        )
    return tuple(rows)


def round7_case_validation_gaps(records: Iterable[E2RCaseRecord]) -> tuple[dict[str, object], ...]:
    record_tuple = tuple(records)
    rows: list[dict[str, object]] = []
    for archetype in E2RArchetype:
        subset = tuple(record for record in record_tuple if record.primary_archetype == archetype)
        bucket_counts = _bucket_counts(subset)
        rows.append(
            {
                "archetype": archetype.value,
                "posture": round7_stage_posture_for(archetype).value,
                "case_count": len(subset),
                "success_validation_count": bucket_counts[Round7ValidationBucket.SUCCESS_VALIDATION],
                "score_weight_failure_count": bucket_counts[Round7ValidationBucket.SCORE_WEIGHT_FAILURE],
                "price_without_eps_count": bucket_counts[Round7ValidationBucket.PRICE_WITHOUT_EPS],
                "one_off_cycle_4c_count": bucket_counts[Round7ValidationBucket.ONE_OFF_CYCLE_4C],
                "event_premium_only_count": bucket_counts[Round7ValidationBucket.EVENT_PREMIUM_ONLY],
                "needs_price_path_count": bucket_counts[Round7ValidationBucket.NEEDS_PRICE_PATH],
                "next_action": _next_action(subset, bucket_counts, round7_stage_posture_for(archetype)),
            }
        )
    return tuple(rows)


def classify_round7_case(record: E2RCaseRecord) -> Round7ValidationBucket:
    price_status = record.price_validation.price_validation_status
    if price_status != "price_filled":
        return Round7ValidationBucket.NEEDS_PRICE_PATH
    if record.score_price_alignment == "aligned" and record.rerating_result in {
        "true_rerating",
        "cyclical_rerating",
        "policy_event_rerating",
    }:
        return Round7ValidationBucket.SUCCESS_VALIDATION
    if record.score_price_alignment == "evidence_good_but_price_failed":
        return Round7ValidationBucket.SCORE_WEIGHT_FAILURE
    if record.score_price_alignment == "price_moved_without_evidence":
        return Round7ValidationBucket.PRICE_WITHOUT_EPS
    if record.rerating_result in {"event_premium", "credit_relief_rally"}:
        return Round7ValidationBucket.EVENT_PREMIUM_ONLY
    if (
        record.case_type in {"one_off", "4c_thesis_break", "overheat"}
        or record.rerating_result in {"theme_overheat", "thesis_break"}
        or record.stage_failure_type in {"should_have_been_red", "false_green"}
    ):
        return Round7ValidationBucket.ONE_OFF_CYCLE_4C
    return Round7ValidationBucket.UNCLASSIFIED


def write_round7_case_validation_reports(
    *,
    case_path: str | Path = "data/e2r_case_library/cases_v02.jsonl",
    output_directory: str | Path = "output/e2r_round7_case_validation",
) -> dict[str, Path]:
    records = load_case_library(case_path)
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "framework": output / "round7_case_validation_framework.md",
        "rules": output / "round7_success_counterexample_rules.md",
        "matrix": output / "round7_archetype_validation_matrix.csv",
        "gaps": output / "round7_case_validation_gap_report.md",
        "next_plan": output / "round7_next_backfill_plan.md",
    }
    paths["framework"].write_text(render_round7_framework_markdown(), encoding="utf-8")
    paths["rules"].write_text(render_round7_rules_markdown(), encoding="utf-8")
    _write_round7_matrix_csv(paths["matrix"])
    paths["gaps"].write_text(render_round7_gap_report_markdown(records), encoding="utf-8")
    paths["next_plan"].write_text(render_round7_next_plan_markdown(records), encoding="utf-8")
    return paths


def render_round7_framework_markdown() -> str:
    lines = [
        "# Round-7 Case Validation Framework",
        "",
        f"Source round: `{ROUND7_SOURCE_ROUND_PATH}`",
        "",
        "이 문서는 calibration 전용이다. production scoring과 StageClassifier threshold를 바꾸지 않는다.",
        "",
        "## 핵심",
        "",
        "Round 7은 성공 사례와 반례를 점수-주가-EPS/FCF 정합성으로 다시 나눈다.",
        "",
        "쉬운 예시:",
        "",
        "`주가 +100%`라도 EPS/FCF 상향이 없으면 구조적 E2R 성공이 아니라 테마/이벤트 반례다.",
        "",
        "## Green 허용도",
        "",
        "| posture | archetype_count | interpretation |",
        "|---|---:|---|",
    ]
    for posture in Round7StagePosture:
        count = sum(1 for archetype in E2RArchetype if round7_stage_posture_for(archetype) == posture)
        lines.append(f"| {posture.value} | {count} | {_posture_interpretation(posture)} |")
    lines.extend(
        [
            "",
            "## Guardrails",
            "- 케이스 라이브러리를 candidate generation input으로 쓰지 않는다.",
            "- Stage 3-Green threshold를 낮추지 않는다.",
            "- event premium, one-off demand, credit relief rally를 true rerating으로 부르지 않는다.",
            "- 가격 경로가 없는 케이스는 score weight 변경 근거로 쓰지 않는다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round7_rules_markdown() -> str:
    lines = [
        "# Round-7 Success and Counterexample Rules",
        "",
        "## Success Case",
        "",
        "성공 사례는 점수만 높으면 안 된다. Stage 2/3 근거 이후 가격과 EPS/FCF가 함께 움직여야 한다.",
        "",
    ]
    for item in ROUND7_SUCCESS_CRITERIA:
        lines.append(f"- `{item}`")
    lines.extend(["", "## Counterexample", ""])
    for item in ROUND7_COUNTEREXAMPLE_CRITERIA:
        lines.append(f"- `{item}`")
    lines.extend(["", "## Price Validation Fields", ""])
    for item in ROUND7_PRICE_VALIDATION_FIELDS:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 쉬운 예시",
            "",
            "- 플랫폼: MAU가 늘어도 ARPU/OPM/FCF가 없으면 Stage 3-Green 근거가 아니다.",
            "- 건설: 수주가 늘어도 PF와 유동성 문제가 남아 있으면 credit relief rally일 수 있다.",
            "- CDMO: 바이오 임상 뉴스가 아니라 장기 생산계약, 가동률, FCF가 핵심이다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round7_gap_report_markdown(records: Iterable[E2RCaseRecord]) -> str:
    rows = round7_case_validation_gaps(records)
    lines = [
        "# Round-7 Case Validation Gap Report",
        "",
        "| archetype | posture | cases | success | score_fail | price_no_eps | one_off_4c | event_only | needs_price | next_action |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['archetype']} | {row['posture']} | {row['case_count']} | "
            f"{row['success_validation_count']} | {row['score_weight_failure_count']} | "
            f"{row['price_without_eps_count']} | {row['one_off_cycle_4c_count']} | "
            f"{row['event_premium_only_count']} | {row['needs_price_path_count']} | {row['next_action']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- `needs_price_path`가 많으면 MFE/MAE와 4B/4C 가격을 먼저 채워야 한다.",
            "- `price_no_eps`는 주가가 먼저 갔지만 EPS/FCF 근거가 없는 반례다.",
            "- `score_fail`은 evidence는 좋아 보였지만 가격 리레이팅이 따라오지 않은 점수비중 실패 후보다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round7_next_plan_markdown(records: Iterable[E2RCaseRecord]) -> str:
    rows = round7_case_validation_gaps(records)
    needs_price = sum(int(row["needs_price_path_count"]) for row in rows)
    redteam_archetypes = [row for row in rows if row["posture"] == Round7StagePosture.REDTEAM_GUARDRAIL.value]
    lines = [
        "# Round-7 Next Backfill Plan",
        "",
        f"- needs_price_path_total: {needs_price}",
        f"- redteam_guardrail_archetypes: {len(redteam_archetypes)}",
        "",
        "## Priority",
        "",
        "1. 가격 경로가 없는 케이스부터 stage price, MFE/MAE, drawdown, 4B/4C를 채운다.",
        "2. Platform, Game, Travel, Construction, Retail, CDMO, Royalty biotech, Holding, Financial, Rare Metals는 Round 7 세부 규칙으로 재검증한다.",
        "3. Green 가능 archetype도 성공 2개 + 반례 2개 + price validation 전에는 scoring weight를 적용하지 않는다.",
        "",
        "## What Not To Change",
        "",
        "- Stage 3-Green 기준을 낮추지 않는다.",
        "- benchmark/case label을 production candidate generation에 넣지 않는다.",
        "- price-only rally를 EPS/FCF evidence로 바꾸지 않는다.",
    ]
    return "\n".join(lines) + "\n"


def _write_round7_matrix_csv(path: Path) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = (
            "archetype",
            "posture",
            "success_requires",
            "counterexample_triggers",
            "price_validation_focus",
            "green_policy",
            "example_cases",
        )
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in round7_archetype_validation_rows():
            writer.writerow(row)
    return path


def _bucket_counts(records: Iterable[E2RCaseRecord]) -> dict[Round7ValidationBucket, int]:
    counts = {bucket: 0 for bucket in Round7ValidationBucket}
    for record in records:
        counts[classify_round7_case(record)] += 1
    return counts


def _next_action(
    records: tuple[E2RCaseRecord, ...],
    bucket_counts: Mapping[Round7ValidationBucket, int],
    posture: Round7StagePosture,
) -> str:
    if not records:
        return "add_success_and_counterexample_cases"
    if bucket_counts[Round7ValidationBucket.NEEDS_PRICE_PATH] > 0:
        return "backfill_price_path"
    if posture == Round7StagePosture.REDTEAM_GUARDRAIL:
        return "add_redteam_counterexamples"
    if bucket_counts[Round7ValidationBucket.SUCCESS_VALIDATION] == 0:
        return "validate_success_case_alignment"
    if bucket_counts[Round7ValidationBucket.SCORE_WEIGHT_FAILURE] + bucket_counts[Round7ValidationBucket.PRICE_WITHOUT_EPS] == 0:
        return "add_counterexample_alignment_cases"
    return "ready_for_shadow_score_review"


def _posture_interpretation(posture: Round7StagePosture) -> str:
    if posture == Round7StagePosture.GREEN_ELIGIBLE_AFTER_VALIDATION:
        return "성공/반례와 가격 경로가 채워지면 향후 Green shadow scoring 후보"
    if posture == Round7StagePosture.WATCH_YELLOW_DEFAULT:
        return "기본은 Stage 3-Watch/Yellow, Green은 강한 반복성/FCF 증거 필요"
    return "RedTeam과 4B/4C 방어가 우선"


__all__ = [
    "ROUND7_COUNTEREXAMPLE_CRITERIA",
    "ROUND7_GREEN_ELIGIBLE_ARCHETYPES",
    "ROUND7_PRICE_VALIDATION_FIELDS",
    "ROUND7_REDTEAM_ARCHETYPES",
    "ROUND7_SOURCE_ROUND_PATH",
    "ROUND7_SUCCESS_CRITERIA",
    "ROUND7_WATCH_YELLOW_ARCHETYPES",
    "Round7ArchetypeValidationRule",
    "Round7StagePosture",
    "Round7ValidationBucket",
    "classify_round7_case",
    "render_round7_framework_markdown",
    "render_round7_gap_report_markdown",
    "render_round7_next_plan_markdown",
    "render_round7_rules_markdown",
    "round7_archetype_validation_rows",
    "round7_case_validation_gaps",
    "round7_rule_for",
    "round7_stage_posture_for",
    "write_round7_case_validation_reports",
]
