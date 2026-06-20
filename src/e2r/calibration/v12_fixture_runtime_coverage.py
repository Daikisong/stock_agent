"""Compare v12 fixture candidates with current runtime replay coverage."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import csv
import json
import re


RESEARCH_AXIS_BRIDGE_COLUMNS = (
    "research_axis_bridge_margin",
    "research_axis_bridge_customer",
    "research_axis_bridge_backlog",
    "research_axis_bridge_contract",
    "research_axis_bridge_valuation_repricing",
    "research_axis_bridge_capital_return",
    "research_axis_bridge_insurance_quality",
    "research_axis_bridge_bio_commercialization",
    "research_axis_bridge_software_retention",
    "research_axis_bridge_consumer_sell_through",
    "research_axis_bridge_guard_risk",
)

BRIDGE_GROUP_REQUIRED_AXES: dict[str, tuple[str, ...]] = {
    "industrial_backlog_margin_bridge": ("margin", "backlog", "contract", "customer"),
    "semiconductor_customer_capacity_bridge": ("customer", "backlog", "contract", "margin"),
    "semiconductor_memory_recovery_bridge": ("customer", "backlog", "margin", "valuation_repricing"),
    "valuation_blowoff_guard_bridge": ("guard_risk", "valuation_repricing", "customer"),
    "battery_mobility_contract_bridge": ("margin", "backlog", "contract", "customer", "guard_risk"),
    "materials_spread_supply_bridge": ("margin", "contract", "guard_risk"),
    "consumer_sellthrough_reorder_bridge": ("consumer_sell_through", "margin", "customer"),
    "financial_capital_return_bridge": ("capital_return", "valuation_repricing", "guard_risk"),
    "insurance_reserve_capital_bridge": ("insurance_quality", "capital_return", "guard_risk"),
    "bio_commercialization_reimbursement_bridge": ("bio_commercialization", "guard_risk"),
    "software_platform_recurring_revenue_bridge": ("software_retention", "customer", "margin"),
    "construction_pf_cash_bridge": ("margin", "contract", "guard_risk"),
    "policy_project_cash_bridge": ("guard_risk", "valuation_repricing", "contract"),
    "governance_tender_cash_bridge": ("capital_return", "guard_risk"),
    "cross_archetype_guard_bridge": ("guard_risk",),
}


def _read_csv(path: str | Path) -> list[dict[str, str]]:
    path_obj = Path(path)
    if not path_obj.exists():
        return []
    with path_obj.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _safe_float(value: Any) -> float:
    if isinstance(value, bool) or value is None:
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _truthy(value: Any) -> bool:
    text = str(value or "").strip().lower()
    return text in {"1", "1.0", "true", "yes", "y"}


def _split_csv_text(value: Any) -> set[str]:
    text = str(value or "").strip()
    if not text:
        return set()
    return {item.strip() for item in text.split(",") if item.strip()}


def _variability_input_count(row: dict[str, str], family: str) -> int | None:
    text = str(row.get("score_variability_drivers") or "")
    if not text:
        return None
    match = re.search(rf"(?:^|\|)input_count:{re.escape(family)}=(\d+)", text)
    if match is None:
        return None
    return int(match.group(1))


def _variability_evidence_count(row: dict[str, str]) -> int | None:
    text = str(row.get("score_variability_drivers") or "")
    if not text:
        return None
    match = re.search(r"(?:^|\|)evidence_count:(\d+)", text)
    if match is None:
        return None
    return int(match.group(1))


def _runtime_input_evidence_summary(score_rows: list[dict[str, str]]) -> dict[str, Any]:
    """Summarize whether runtime rows have enough source families to assess bridge translation."""

    if not score_rows:
        return {
            "assessable": False,
            "reason": "no_runtime_candidate_rows",
            "families_present": [],
            "max_evidence_count": 0,
            "max_input_counts": {},
        }

    all_families: set[str] = set()
    max_counts: dict[str, int] = {}
    max_evidence_count = 0
    saw_explicit_evidence_metadata = False
    family_keys = ("research_report", "news_item", "consensus", "consensus_revision", "financial_actual", "price_bar")
    for row in score_rows:
        families = _split_csv_text(row.get("cross_evidence_families_present"))
        if families:
            saw_explicit_evidence_metadata = True
            all_families.update(families)
        evidence_count = _variability_evidence_count(row)
        if evidence_count is not None:
            saw_explicit_evidence_metadata = True
            max_evidence_count = max(max_evidence_count, evidence_count)
        for key in family_keys:
            count = _variability_input_count(row, key)
            if count is not None:
                saw_explicit_evidence_metadata = True
                max_counts[key] = max(max_counts.get(key, 0), count)

    if not saw_explicit_evidence_metadata:
        return {
            "assessable": True,
            "reason": "legacy_rows_without_evidence_metadata",
            "families_present": sorted(all_families),
            "max_evidence_count": max_evidence_count,
            "max_input_counts": max_counts,
        }

    text_source_count = sum(max_counts.get(key, 0) for key in ("research_report", "news_item", "consensus", "consensus_revision"))
    if text_source_count > 0:
        reason = "source_text_family_present"
        assessable = True
    elif {"disclosure", "financial_actual"}.issubset(all_families) and max_evidence_count >= 3:
        reason = "disclosure_and_financial_actual_evidence_present"
        assessable = True
    else:
        reason = "bridge_source_families_missing"
        assessable = False

    return {
        "assessable": assessable,
        "reason": reason,
        "families_present": sorted(all_families),
        "max_evidence_count": max_evidence_count,
        "max_input_counts": max_counts,
    }


def _candidate_symbol(row: dict[str, Any] | None) -> str:
    if not row:
        return ""
    text = str(row.get("symbol") or "").strip()
    return text.split()[0] if text else ""


def _candidate_date(row: dict[str, Any] | None) -> str:
    if not row:
        return ""
    return str(row.get("trigger_date") or row.get("entry_date") or "").strip()


def _avg(values: list[float]) -> float:
    if not values:
        return 0.0
    return round(sum(values) / len(values), 4)


def _bridge_axis_key(axis: str) -> str:
    return f"research_axis_bridge_{axis}"


def _present_bridge_axes(score_rows: list[dict[str, str]]) -> dict[str, dict[str, float]]:
    axis_stats: dict[str, dict[str, float]] = {}
    for column in RESEARCH_AXIS_BRIDGE_COLUMNS:
        values = [_safe_float(row.get(column)) for row in score_rows]
        axis_name = column.removeprefix("research_axis_bridge_")
        axis_stats[axis_name] = {
            "present_count": sum(1 for value in values if value > 0),
            "max": max(values) if values else 0.0,
            "avg": _avg(values),
        }
    return axis_stats


def _missing_required_axes(runtime_bridge_group: str, axis_stats: dict[str, dict[str, float]]) -> list[str]:
    required = BRIDGE_GROUP_REQUIRED_AXES.get(runtime_bridge_group, ())
    return [axis for axis in required if axis_stats.get(axis, {}).get("max", 0.0) <= 0.0]


def _top_failed_gates(gate_rows: list[dict[str, str]], limit: int = 8) -> list[dict[str, Any]]:
    counts: Counter[str] = Counter()
    for row in gate_rows:
        for key, value in row.items():
            if key.startswith("failed_") and _truthy(value):
                counts[key] += 1
    return [{"gate": key, "count": count} for key, count in counts.most_common(limit)]


def _stage_distribution(rows: list[dict[str, str]]) -> dict[str, int]:
    counts = Counter(str(row.get("current_stage") or "") for row in rows)
    return dict(sorted((key, value) for key, value in counts.items() if key))


def _exact_candidate_present(rows: list[dict[str, str]], candidate: dict[str, Any] | None) -> bool:
    symbol = _candidate_symbol(candidate)
    as_of = _candidate_date(candidate)
    if not symbol or not as_of:
        return False
    return any(str(row.get("symbol") or "").strip() == symbol and str(row.get("as_of_date") or "").strip() == as_of for row in rows)


def _max_score(rows: list[dict[str, str]]) -> float | None:
    values = [_safe_float(row.get("current_score")) for row in rows if str(row.get("current_score") or "").strip()]
    if not values:
        return None
    return round(max(values), 4)


def _avg_score(rows: list[dict[str, str]]) -> float | None:
    values = [_safe_float(row.get("current_score")) for row in rows if str(row.get("current_score") or "").strip()]
    if not values:
        return None
    return _avg(values)


def _runtime_gap_status(
    *,
    fixture_status: str,
    score_rows: list[dict[str, str]],
    green_runtime_count: int,
    missing_required_axes: list[str],
    top_failed_gates: list[dict[str, Any]],
    input_evidence_summary: dict[str, Any],
) -> str:
    if fixture_status != "ready_for_runtime_replay_fixture":
        return "fixture_not_ready"
    if not score_rows:
        return "not_in_current_benchmark"
    if green_runtime_count > 0 and not missing_required_axes:
        return "runtime_green_or_near_ready"
    if missing_required_axes:
        if not bool(input_evidence_summary.get("assessable")):
            return "runtime_input_evidence_missing"
        return "runtime_bridge_axes_missing"
    if any(item["gate"] in {"failed_stage3_total_score", "failed_stage3_bottleneck"} for item in top_failed_gates):
        return "runtime_stage3_gate_blocked"
    return "runtime_needs_review"


def build_v12_fixture_runtime_coverage_board(
    *,
    fixture_payload: dict[str, Any],
    score_rows: list[dict[str, str]],
    gate_rows: list[dict[str, str]],
) -> dict[str, Any]:
    """Build an archetype board for fixture readiness vs current runtime replay."""

    scores_by_archetype: dict[str, list[dict[str, str]]] = defaultdict(list)
    gates_by_archetype: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in score_rows:
        archetype = str(row.get("canonical_archetype_id") or "").strip()
        if archetype:
            scores_by_archetype[archetype].append(row)
    for row in gate_rows:
        archetype = str(row.get("canonical_archetype_id") or "").strip()
        if archetype:
            gates_by_archetype[archetype].append(row)

    archetype_rows: list[dict[str, Any]] = []
    for fixture in fixture_payload.get("archetypes", []):
        archetype = str(fixture.get("canonical_archetype_id") or "")
        runtime_rows = scores_by_archetype.get(archetype, [])
        runtime_gate_rows = gates_by_archetype.get(archetype, [])
        axis_stats = _present_bridge_axes(runtime_rows)
        runtime_bridge_group = str(fixture.get("runtime_bridge_group") or "")
        missing_axes = _missing_required_axes(runtime_bridge_group, axis_stats)
        top_gates = _top_failed_gates(runtime_gate_rows)
        green_runtime_count = sum(1 for row in runtime_rows if str(row.get("current_stage") or "") == "3-Green")
        fixture_status = str(fixture.get("fixture_status") or "")
        input_evidence = _runtime_input_evidence_summary(runtime_rows)
        archetype_rows.append(
            {
                "canonical_archetype_id": archetype,
                "large_sector_id": fixture.get("large_sector_id"),
                "runtime_bridge_group": runtime_bridge_group,
                "fixture_status": fixture_status,
                "raw_stage3_green_row_count": fixture.get("raw_stage3_green_row_count", 0),
                "fixture_green_row_count": fixture.get("green_row_count", 0),
                "clean_green_row_count": fixture.get("clean_green_row_count", 0),
                "green_guard_marker_row_count": fixture.get("green_guard_marker_row_count", 0),
                "clean_guard_row_count": fixture.get("clean_guard_row_count", 0),
                "runtime_candidate_count": len(runtime_rows),
                "runtime_stage_distribution": _stage_distribution(runtime_rows),
                "runtime_green_count": green_runtime_count,
                "runtime_max_score": _max_score(runtime_rows),
                "runtime_avg_score": _avg_score(runtime_rows),
                "green_fixture_in_current_benchmark": _exact_candidate_present(
                    runtime_rows,
                    fixture.get("green_fixture_candidate"),
                ),
                "guard_fixture_in_current_benchmark": _exact_candidate_present(
                    runtime_rows,
                    fixture.get("guard_fixture_candidate"),
                ),
                "required_bridge_axes": list(BRIDGE_GROUP_REQUIRED_AXES.get(runtime_bridge_group, ())),
                "missing_required_bridge_axes": missing_axes,
                "bridge_axis_stats": axis_stats,
                "top_failed_gates": top_gates,
                "runtime_input_evidence_summary": input_evidence,
                "runtime_gap_status": _runtime_gap_status(
                    fixture_status=fixture_status,
                    score_rows=runtime_rows,
                    green_runtime_count=green_runtime_count,
                    missing_required_axes=missing_axes,
                    top_failed_gates=top_gates,
                    input_evidence_summary=input_evidence,
                ),
            }
        )

    status_counts = Counter(row["runtime_gap_status"] for row in archetype_rows)
    ready_rows = [row for row in archetype_rows if row["fixture_status"] == "ready_for_runtime_replay_fixture"]
    runtime_rows_with_candidates = [row for row in archetype_rows if row["runtime_candidate_count"] > 0]
    bridge_missing_counts: Counter[str] = Counter()
    for row in archetype_rows:
        bridge_missing_counts.update(row["missing_required_bridge_axes"])
    return {
        "schema_version": "v12_fixture_runtime_coverage_board_v1",
        "archetype_count": len(archetype_rows),
        "ready_fixture_archetype_count": len(ready_rows),
        "runtime_covered_archetype_count": len(runtime_rows_with_candidates),
        "ready_fixture_not_in_current_benchmark_count": sum(
            1 for row in ready_rows if row["runtime_candidate_count"] == 0
        ),
        "ready_fixture_in_benchmark_no_runtime_green_count": sum(
            1 for row in ready_rows if row["runtime_candidate_count"] > 0 and row["runtime_green_count"] == 0
        ),
        "runtime_green_archetype_count": sum(1 for row in archetype_rows if row["runtime_green_count"] > 0),
        "exact_green_fixture_present_count": sum(1 for row in archetype_rows if row["green_fixture_in_current_benchmark"]),
        "exact_guard_fixture_present_count": sum(1 for row in archetype_rows if row["guard_fixture_in_current_benchmark"]),
        "status_counts": dict(sorted(status_counts.items())),
        "missing_required_bridge_axis_counts": dict(sorted(bridge_missing_counts.items())),
        "archetypes": archetype_rows,
    }


def render_v12_fixture_runtime_coverage_board(payload: dict[str, Any]) -> str:
    rows = list(payload.get("archetypes", []))
    lines = [
        "# V12 Fixture Runtime Coverage Board",
        "",
        "이 보고서는 누적 Green/guard fixture 후보가 현재 runtime benchmark에서 실제로 검증되고 있는지 대조한다.",
        "여기서 `not_in_current_benchmark`는 점수식이 맞다/틀리다 이전에 해당 archetype fixture가 현재 replay 후보로 올라오지 않았다는 뜻이다.",
        "",
        "## Summary",
        "",
        f"- archetype_count: `{payload.get('archetype_count', 0)}`",
        f"- ready_fixture_archetype_count: `{payload.get('ready_fixture_archetype_count', 0)}`",
        f"- runtime_covered_archetype_count: `{payload.get('runtime_covered_archetype_count', 0)}`",
        f"- ready_fixture_not_in_current_benchmark_count: `{payload.get('ready_fixture_not_in_current_benchmark_count', 0)}`",
        f"- ready_fixture_in_benchmark_no_runtime_green_count: `{payload.get('ready_fixture_in_benchmark_no_runtime_green_count', 0)}`",
        f"- runtime_green_archetype_count: `{payload.get('runtime_green_archetype_count', 0)}`",
        f"- exact_green_fixture_present_count: `{payload.get('exact_green_fixture_present_count', 0)}`",
        f"- exact_guard_fixture_present_count: `{payload.get('exact_guard_fixture_present_count', 0)}`",
        f"- status_counts: `{payload.get('status_counts', {})}`",
        f"- missing_required_bridge_axis_counts: `{payload.get('missing_required_bridge_axis_counts', {})}`",
        "",
        "## Archetype Board",
        "",
        "| archetype | fixture | runtime candidates | stages | max score | missing required axes | top failed gates | status |",
        "| --- | --- | ---: | --- | ---: | --- | --- | --- |",
    ]
    for row in sorted(rows, key=lambda item: (str(item["runtime_gap_status"]), -int(item["runtime_candidate_count"]), str(item["canonical_archetype_id"]))):
        top_gates = ", ".join(f"{item['gate']}:{item['count']}" for item in row.get("top_failed_gates", [])[:4])
        missing_axes = ", ".join(row.get("missing_required_bridge_axes") or [])
        lines.append(
            "| {arch} | {fixture} | {count} | {stages} | {max_score} | {missing} | {gates} | {status} |".format(
                arch=row["canonical_archetype_id"],
                fixture=row["fixture_status"],
                count=row["runtime_candidate_count"],
                stages=row.get("runtime_stage_distribution") or {},
                max_score="" if row.get("runtime_max_score") is None else row["runtime_max_score"],
                missing=missing_axes or "none",
                gates=top_gates or "none",
                status=row["runtime_gap_status"],
            )
        )
    lines.extend(
        [
            "",
            "## Simple Reading",
            "",
            "- `fixture_not_ready`: 연구 장부 쪽 positive source 또는 Green row가 아직 부족하다.",
            "- `not_in_current_benchmark`: current benchmark 후보 생성/funnel 또는 replay coverage가 그 archetype을 검증하지 못한다.",
            "- `runtime_input_evidence_missing`: 후보 row는 있지만 bridge를 판정할 리포트/뉴스/컨센서스/충분한 공시+재무 입력 가족이 부족하다.",
            "- `runtime_bridge_axes_missing`: 후보는 올라왔지만 필요한 research-axis bridge가 runtime primitive로 충분히 살아나지 않는다.",
            "- `runtime_stage3_gate_blocked`: bridge는 일부 살아도 total/bottleneck/visibility 같은 Stage3 gate에서 막힌다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_fixture_runtime_coverage_board(
    *,
    fixture_candidates_path: str | Path,
    score_components_path: str | Path,
    stage_gate_matrix_path: str | Path,
    output_json_path: str | Path,
    output_markdown_path: str | Path,
) -> dict[str, Path]:
    payload = build_v12_fixture_runtime_coverage_board(
        fixture_payload=_read_json(fixture_candidates_path),
        score_rows=_read_csv(score_components_path),
        gate_rows=_read_csv(stage_gate_matrix_path),
    )
    json_path = Path(output_json_path)
    md_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_fixture_runtime_coverage_board(payload), encoding="utf-8")
    return {"json": json_path, "markdown": md_path}
