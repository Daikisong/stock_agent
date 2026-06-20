"""Audit old Green score-simulation axes against runtime field contracts."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping
import json

from .v12_bridge_spec_runtime_field_audit import build_runtime_field_inventory


DEFAULT_SCORE_SIMULATION_ROOT = Path("docs/round/achieve/achieve_v12")
DEFAULT_CAUSAL_CHAIN_PATH = Path("docs/0619/v12_score_loss_causal_chain_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_green_score_axis_runtime_contract_audit_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_green_score_axis_runtime_contract_audit_2026-06-19.md")

FOCUS_ARCHETYPES = (
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
    "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
    "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
    "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
    "C02_POWER_GRID_DATACENTER_CAPEX",
)

TOP_LEVEL_SCORE_KEYS = {
    "eps_fcf_explosion",
    "earnings_visibility",
    "bottleneck_pricing",
    "market_mispricing",
    "valuation_rerating",
    "capital_allocation",
    "information_confidence",
    "pricing_power",
    "mispricing",
    "info_confidence",
    "simulated_total",
    "raw_total_proxy",
    "weighted_total_proxy",
}

FAMILY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "margin_bridge": ("margin", "opm", "spread", "pricing", "profit", "cash_conversion", "fcf"),
    "customer_quality": ("customer", "client", "hyperscaler", "nvidia"),
    "backlog_orderbook": ("backlog", "orderbook", "order_backlog", "rpo"),
    "contract_quality": ("contract", "lta", "renewal", "retention", "take_or_pay"),
    "capacity_conversion": ("capacity", "capa", "utilization", "shipment", "lead_time"),
    "revision": ("revision", "estimate", "guidance"),
    "valuation_repricing": ("valuation", "repricing", "rerating", "pbr", "multiple"),
    "capital_return": ("capital_return", "shareholder", "buyback", "dividend", "treasury", "roe_pbr"),
    "insurance_quality": ("csm", "kics", "k_ics", "reserve", "loss_ratio"),
    "bio_commercialization": ("commercialization", "approval", "royalty", "reimbursement", "trial"),
    "software_retention": ("arr", "nrr", "retention", "recurring", "subscription", "seat"),
    "consumer_sell_through": ("sell_through", "reorder", "channel", "distribution", "export"),
    "guard_risk": (
        "execution_risk",
        "legal",
        "dilution",
        "accounting",
        "overheat",
        "positioning",
        "thesis_break",
        "mae",
        "theme_spike",
    ),
    "relative_strength": ("relative_strength", "price_stage", "momentum"),
}

FAMILY_RUNTIME_CANDIDATES: dict[str, tuple[str, ...]] = {
    "margin_bridge": (
        "actual_profit_conversion_score",
        "actual_op_yoy_pct",
        "opm_expansion_pctp",
        "actual_opm",
        "high_margin_mix_improvement",
        "pricing_power_confirmed",
    ),
    "customer_quality": (
        "customer_preorder_or_allocation",
        "minimum_revenue_guarantee",
        "government_customer",
        "hyperscaler_customer",
        "retention_or_renewal",
        "partner_economics_visible",
    ),
    "backlog_orderbook": (
        "order_backlog_to_sales",
        "backlog_to_sales",
        "rpo_to_sales",
        "record_backlog",
        "backlog_record_high",
        "ai_infra_backlog_or_rpo",
    ),
    "contract_quality": (
        "contract_quality",
        "contract_duration_months",
        "contract_amount_to_prior_sales",
        "multi_year_contract",
        "take_or_pay",
        "customer_prepayment",
        "contract_renewal_visible",
    ),
    "capacity_conversion": (
        "capa_constraint",
        "capacity_precommitted",
        "hbm_capacity_pre_sold",
        "hbm_capacity_constraint",
        "capacity_utilization_pct",
        "lead_time_months",
        "advanced_packaging_bottleneck",
    ),
    "revision": (
        "revision_score",
        "estimate_upgrade_mentioned",
        "eps_revision_pct",
        "op_revision_pct",
        "target_price_revision_pct",
    ),
    "valuation_repricing": (
        "valuation_score",
        "market_frame_shift",
        "target_multiple_rerating",
        "target_multiple_before",
        "target_multiple_after",
        "pbr_e",
        "est_pbr",
    ),
    "capital_return": (
        "capital_return_execution",
        "shareholder_return_execution",
        "treasury_share_cancellation",
        "buyback_executed",
        "dividend_visibility",
        "roe",
        "pbr_e",
    ),
    "insurance_quality": (
        "csm_growth_visible",
        "k_ics_ratio",
        "reserve_quality_visible",
        "loss_ratio_quality",
        "capital_return_execution",
    ),
    "bio_commercialization": (
        "regulatory_approval_confirmed",
        "approval_to_revenue_bridge",
        "royalty_route",
        "partner_economics_visible",
        "reimbursement_confirmed",
    ),
    "software_retention": (
        "arr_growth_pct",
        "arr_growth_visible",
        "nrr",
        "retention_or_renewal",
        "contract_renewal_visible",
        "recurring_margin_leverage",
    ),
    "consumer_sell_through": (
        "sell_through_confirmed",
        "channel_reorder_confirmed",
        "repeat_order_confirmed",
        "export_channel_expansion",
        "overseas_channel_expansion",
    ),
    "guard_risk": (
        "one_off_shortage_risk",
        "cashflow_deterioration",
        "binary_event_unresolved",
        "policy_headline_only",
        "revision_slowdown",
        "capital_return_unconfirmed",
        "approval_not_confirmed",
    ),
    "relative_strength": ("price_stage_score",),
}


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _top_counter_rows(counter: Counter[str], limit: int = 30) -> list[dict[str, Any]]:
    return [{"key": key, "count": count} for key, count in counter.most_common(limit)]


def _extract_score_simulation_rows(root: str | Path = DEFAULT_SCORE_SIMULATION_ROOT) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    root_path = Path(root)
    if not root_path.exists():
        return rows
    for path in sorted(root_path.glob("**/*.md")):
        with path.open(encoding="utf-8", errors="ignore") as handle:
            for line_no, line in enumerate(handle, start=1):
                text = line.strip()
                if not text.startswith("{") or "score_simulation" not in text:
                    continue
                try:
                    row = json.loads(text)
                except json.JSONDecodeError:
                    continue
                if row.get("row_type") != "score_simulation":
                    continue
                row = dict(row)
                row["source_file"] = str(path)
                row["source_line"] = line_no
                rows.append(row)
    return rows


def _score_simulation_label_text(row: Mapping[str, Any]) -> str:
    return " ".join(
        str(row.get(key) or "")
        for key in ("stage_label_after", "stage_label_before", "simulated_stage", "trigger_type")
    ).lower()


def _is_green_related_score_simulation(row: Mapping[str, Any]) -> bool:
    return "green" in _score_simulation_label_text(row)


def _is_strict_stage3_green_score_simulation(row: Mapping[str, Any]) -> bool:
    return "stage3-green" in _score_simulation_label_text(row)


def _score_keys(row: Mapping[str, Any]) -> set[str]:
    keys: set[str] = set()
    for field in ("raw_component_scores_before", "raw_component_scores_after", "raw_component_score_breakdown"):
        values = row.get(field)
        if isinstance(values, Mapping):
            keys.update(str(key) for key in values)
    keys.update(str(item) for item in row.get("changed_components") or ())
    for key, value in row.items():
        if not isinstance(value, (int, float)):
            continue
        if key.endswith("_score") or key.endswith("_risk") or key in TOP_LEVEL_SCORE_KEYS:
            keys.add(str(key))
    return keys


def _family_for_key(key: str) -> str:
    lowered = key.lower()
    if any(
        token in lowered
        for token in (
            "_risk",
            "risk_score",
            "legal_or_contract",
            "accounting_trust",
            "dilution",
            "positioning_overheat",
            "thesis_break",
            "theme_spike",
            "high_mae",
        )
    ):
        return "guard_risk"
    if any(token in lowered for token in ("roe_pbr", "capital_return", "shareholder_return", "buyback", "dividend")):
        return "capital_return"
    if any(token in lowered for token in ("valuation", "repricing", "rerating", "pbr", "multiple")):
        return "valuation_repricing"
    for family, keywords in FAMILY_KEYWORDS.items():
        if any(keyword in lowered for keyword in keywords):
            return family
    return "other"


def _runtime_sets(inventory: Mapping[str, Any]) -> tuple[set[str], set[str], set[str]]:
    source_fields = set(inventory.get("feature_method_arg_keys", ()))
    source_fields.update(inventory.get("parser_output_keys", ()))
    source_fields.update(inventory.get("bridge_diagnostic_group_keys", ()))
    derived_fields = set(inventory.get("derived_runtime_metrics", ()))
    all_fields = source_fields | derived_fields
    return source_fields, derived_fields, all_fields


def _axis_contract_row(key: str, count: int, inventory: Mapping[str, Any]) -> dict[str, Any]:
    source_fields, derived_fields, all_fields = _runtime_sets(inventory)
    family = _family_for_key(key)
    candidates = list(FAMILY_RUNTIME_CANDIDATES.get(family, ()))
    supported_candidates = sorted(candidate for candidate in candidates if candidate in all_fields)
    if key in source_fields:
        status = "exact_source_runtime_field"
    elif key in derived_fields:
        status = "exact_derived_metric_only"
    elif supported_candidates:
        status = "requires_axis_bridge_to_runtime_primitives"
    else:
        status = "missing_axis_bridge_contract"
    return {
        "research_score_key": key,
        "green_related_occurrence_count": count,
        "family": family,
        "runtime_contract_status": status,
        "candidate_runtime_fields": candidates,
        "supported_candidate_runtime_fields": supported_candidates,
    }


def _causal_focus_rows(payload: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): dict(row) for row in payload.get("focus_archetype_rows", []) or []}


def build_v12_green_score_axis_runtime_contract_audit(
    *,
    score_simulation_rows: Iterable[Mapping[str, Any]] | None = None,
    score_simulation_root: str | Path = DEFAULT_SCORE_SIMULATION_ROOT,
    runtime_inventory: Mapping[str, Any] | None = None,
    causal_chain_payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a reproducible audit from research score axes to runtime field contracts."""

    rows = [dict(row) for row in score_simulation_rows] if score_simulation_rows is not None else _extract_score_simulation_rows(score_simulation_root)
    inventory = dict(runtime_inventory or build_runtime_field_inventory())
    causal_chain = dict(causal_chain_payload or _read_json(DEFAULT_CAUSAL_CHAIN_PATH))
    causal_by_arch = _causal_focus_rows(causal_chain)
    source_fields, derived_fields, all_fields = _runtime_sets(inventory)

    all_key_counts: Counter[str] = Counter()
    green_key_counts: Counter[str] = Counter()
    green_changed_counts: Counter[str] = Counter()
    green_archetype_counts: Counter[str] = Counter()
    strict_green_archetype_counts: Counter[str] = Counter()
    green_rows_by_arch: dict[str, list[dict[str, Any]]] = defaultdict(list)
    green_rows = []
    strict_green_rows = []
    for row in rows:
        keys = _score_keys(row)
        all_key_counts.update(keys)
        if not _is_green_related_score_simulation(row):
            continue
        green_rows.append(row)
        green_key_counts.update(keys)
        green_changed_counts.update(str(item) for item in row.get("changed_components") or ())
        archetype = str(row.get("canonical_archetype_id") or "UNKNOWN")
        green_archetype_counts[archetype] += 1
        green_rows_by_arch[archetype].append(row)
        if _is_strict_stage3_green_score_simulation(row):
            strict_green_rows.append(row)
            strict_green_archetype_counts[archetype] += 1

    source_matches = sorted(set(green_key_counts) & source_fields)
    derived_matches = sorted((set(green_key_counts) & derived_fields) - source_fields)
    top_axis_contract_rows = [
        _axis_contract_row(key, count, inventory)
        for key, count in green_key_counts.most_common(40)
    ]
    status_counts = Counter(row["runtime_contract_status"] for row in top_axis_contract_rows)

    focus_rows: list[dict[str, Any]] = []
    for archetype in FOCUS_ARCHETYPES:
        arch_rows = green_rows_by_arch.get(archetype, [])
        arch_key_counts: Counter[str] = Counter()
        for row in arch_rows:
            arch_key_counts.update(_score_keys(row))
        causal_row = causal_by_arch.get(archetype, {})
        focus_rows.append(
            {
                "canonical_archetype_id": archetype,
                "green_score_simulation_count": len(arch_rows),
                "strict_stage3_green_score_simulation_count": strict_green_archetype_counts.get(archetype, 0),
                "top_green_score_keys": [
                    _axis_contract_row(key, count, inventory)
                    for key, count in arch_key_counts.most_common(8)
                ],
                "current_stop_layer": causal_row.get("stop_layer"),
                "current_runtime": causal_row.get("runtime_best_row"),
                "plain_failure": causal_row.get("plain_failure"),
                "next_fix": causal_row.get("next_fix"),
            }
        )

    return {
        "schema_version": "v12_green_score_axis_runtime_contract_audit_v1",
        "summary": {
            "score_simulation_row_count": len(rows),
            "green_related_score_simulation_row_count": len(green_rows),
            "strict_stage3_green_score_simulation_row_count": len(strict_green_rows),
            "unique_research_score_key_count": len(all_key_counts),
            "unique_green_research_score_key_count": len(green_key_counts),
            "runtime_source_field_key_count": len(source_fields),
            "runtime_derived_metric_count": len(derived_fields),
            "green_score_key_exact_source_field_count": len(source_matches),
            "green_score_key_exact_derived_metric_only_count": len(derived_matches),
            "green_score_key_exact_source_field_matches": source_matches,
            "green_score_key_exact_derived_metric_only_matches": derived_matches,
            "top40_contract_status_counts": _counter_dict(status_counts),
            "plain_conclusion": (
                "예전 Green 연구는 score_simulation 축을 많이 썼지만, 그 축 대부분은 현재 runtime source field와 "
                "1:1로 맞지 않는다. 따라서 누적 연구는 weight까지는 들어갔어도, Green 축을 source-backed primitive로 "
                "번역하는 계약이 없으면 현재 scorer에서는 빈칸처럼 남는다."
            ),
        },
        "top_green_research_score_keys": _top_counter_rows(green_key_counts, limit=40),
        "top_changed_components": _top_counter_rows(green_changed_counts, limit=40),
        "green_score_axis_contract_rows": top_axis_contract_rows,
        "green_score_simulation_archetype_counts": _counter_dict(green_archetype_counts),
        "strict_stage3_green_score_simulation_archetype_counts": _counter_dict(strict_green_archetype_counts),
        "focus_archetype_rows": focus_rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _join(values: Iterable[Any]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "none"


def _runtime_short(row: Mapping[str, Any] | None) -> str:
    if not row:
        return "not scored"
    return "{stage}/{score}/{arch}; deficit={deficit}".format(
        stage=row.get("current_stage"),
        score=row.get("current_score"),
        arch=row.get("canonical_archetype_id"),
        deficit=row.get("green_gate_deficit_summary"),
    )


def _axis_rows_text(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "none"
    return "<br>".join(
        "{key}:{count}:{status}->{fields}".format(
            key=row.get("research_score_key"),
            count=row.get("green_related_occurrence_count"),
            status=row.get("runtime_contract_status"),
            fields=_join((row.get("supported_candidate_runtime_fields") or [])[:4]),
        )
        for row in rows
    )


def render_v12_green_score_axis_runtime_contract_audit(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    lines = [
        "# V12 Green Score Axis Runtime Contract Audit",
        "",
        "이 문서는 예전 연구의 Green score_simulation이 어떤 점수축을 썼고, 그 축이 현재 runtime field contract와 맞는지 본다.",
        "목적은 HBM 보너스가 아니라, Green 연구축이 source-backed primitive로 번역되는지 확인하는 것이다.",
        "",
        "## Summary",
        "",
        f"- plain_conclusion: {summary.get('plain_conclusion')}",
        f"- score_simulation_row_count: `{summary.get('score_simulation_row_count')}`",
        f"- green_related_score_simulation_row_count: `{summary.get('green_related_score_simulation_row_count')}`",
        f"- strict_stage3_green_score_simulation_row_count: `{summary.get('strict_stage3_green_score_simulation_row_count')}`",
        f"- unique_green_research_score_key_count: `{summary.get('unique_green_research_score_key_count')}`",
        f"- runtime_source_field_key_count: `{summary.get('runtime_source_field_key_count')}`",
        f"- runtime_derived_metric_count: `{summary.get('runtime_derived_metric_count')}`",
        f"- green_score_key_exact_source_field_count: `{summary.get('green_score_key_exact_source_field_count')}`",
        f"- green_score_key_exact_derived_metric_only_count: `{summary.get('green_score_key_exact_derived_metric_only_count')}`",
        f"- green_score_key_exact_source_field_matches: `{summary.get('green_score_key_exact_source_field_matches')}`",
        f"- green_score_key_exact_derived_metric_only_matches: `{summary.get('green_score_key_exact_derived_metric_only_matches')}`",
        f"- top40_contract_status_counts: `{summary.get('top40_contract_status_counts')}`",
        "",
        "## Top Green Score Axis Contract Rows",
        "",
        "| research score key | count | family | contract status | supported runtime fields |",
        "| --- | ---: | --- | --- | --- |",
    ]
    for row in payload.get("green_score_axis_contract_rows", [])[:30]:
        lines.append(
            "| {key} | {count} | {family} | {status} | {fields} |".format(
                key=row.get("research_score_key"),
                count=row.get("green_related_occurrence_count"),
                family=row.get("family"),
                status=row.get("runtime_contract_status"),
                fields=_join(row.get("supported_candidate_runtime_fields") or []),
            )
        )
    lines.extend(
        [
            "",
            "## Focus Archetypes",
            "",
            "| archetype | Green score sims | current stop layer | runtime | top research score keys -> runtime fields | plain failure |",
            "| --- | ---: | --- | --- | --- | --- |",
        ]
    )
    for row in payload.get("focus_archetype_rows", []) or []:
        lines.append(
            "| {arch} | {count}/{strict} | {stop} | {runtime} | {keys} | {failure} |".format(
                arch=row.get("canonical_archetype_id"),
                count=row.get("green_score_simulation_count"),
                strict=row.get("strict_stage3_green_score_simulation_count"),
                stop=row.get("current_stop_layer"),
                runtime=_runtime_short(row.get("current_runtime")),
                keys=_axis_rows_text(row.get("top_green_score_keys") or []),
                failure=row.get("plain_failure"),
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 예전 연구의 `margin_bridge_score`, `customer_quality_score`, `backlog_visibility_score`는 Green을 만들던 핵심축이다.",
            "- 현재 runtime은 그 이름을 직접 읽지 않고 `actual_op_yoy_pct`, `customer_preorder_or_allocation`, `order_backlog_to_sales` 같은 원천 field를 읽는다.",
            "- 그래서 연구자료에 `customer_quality_score=9`가 있어도 parser가 `customer_preorder_or_allocation=True`를 만들지 못하면 현재 점수는 안 오른다.",
            "- 하닉 예: `capacity_lock/order_or_contract` 연구축이 runtime bridge field까지 내려와도 Green gate 통과 여부는 positive/guard로 다시 검증해야 한다.",
            "- 삼성/C10 예: 후보와 리포트가 있어도 customer/backlog/contract bridge가 약하면 Stage2에 남는다.",
            "- C01/C19/R13 예: 후보 row의 입력 가족이 약하면 parser가 아니라 replay 입력 보강이 먼저다.",
            "- 비-HBM 예: C21/C23/C26도 Green score_simulation은 있지만 current replay 후보나 field contract가 비어 있으면 똑같이 낮게 나온다.",
            "- 결론: 해결은 Green threshold 완화가 아니라 연구 score axis -> source-backed primitive -> runtime component/gate 계약을 만드는 것이다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_green_score_axis_runtime_contract_audit(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_green_score_axis_runtime_contract_audit()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_green_score_axis_runtime_contract_audit(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_green_score_axis_runtime_contract_audit()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
