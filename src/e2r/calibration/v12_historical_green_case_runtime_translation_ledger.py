"""Ledger historical Green score-simulation cases against current runtime fields."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping
import json

from .v12_bridge_spec_runtime_field_audit import build_runtime_field_inventory
from .v12_green_score_axis_runtime_contract_audit import (
    DEFAULT_SCORE_SIMULATION_ROOT,
    FAMILY_RUNTIME_CANDIDATES,
    _axis_contract_row,
    _extract_score_simulation_rows,
    _family_for_key,
    _runtime_sets,
)


DEFAULT_CURRENT_CENSUS_PATH = Path("docs/0619/v12_current_runtime_field_failure_census_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_historical_green_case_runtime_translation_ledger_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_historical_green_case_runtime_translation_ledger_2026-06-19.md")


SCORE_DICT_FIELDS = (
    "raw_component_scores_after",
    "component_scores",
    "raw_component_score_breakdown",
    "raw_component_scores_before",
)
CASE_FIELDS = (
    "case_id",
    "trigger_id",
    "symbol",
    "large_sector_id",
    "canonical_archetype_id",
    "weighted_score_before",
    "weighted_score_after",
    "weighted_total_pre_bonus",
    "weighted_total_stage2_actionable_bonus",
    "stage_label_before",
    "stage_label_after",
    "simulated_stage_current_profile",
    "simulated_stage",
    "MFE_90D_pct",
    "MAE_90D_pct",
    "MFE_180D_pct",
    "MAE_180D_pct",
    "score_return_alignment_label",
    "current_profile_verdict",
    "component_delta_explanation",
    "source_file",
    "source_line",
)


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _safe_float(value: Any) -> float | None:
    if isinstance(value, bool) or value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return float(text)
    except (TypeError, ValueError):
        return None


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _verdict_bucket(value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        return "missing"
    if text.startswith("current_profile_false_positive"):
        return "current_profile_false_positive"
    if text.startswith("current_profile_missed_structural"):
        return "current_profile_missed_structural"
    if text.startswith("current_profile_too_late"):
        return "current_profile_too_late"
    if text.startswith("current_profile_too_early"):
        return "current_profile_too_early"
    if text.startswith("current_profile_correct"):
        return "current_profile_correct"
    if text.startswith("current_profile_4B"):
        return "current_profile_4B"
    if text.startswith("current_profile_"):
        parts = text.split("_")
        if len(parts) >= 3:
            return "_".join(parts[:3])
        return text
    return "non_standard_verdict_text"


def _top_counter_rows(counter: Counter[str], limit: int = 30) -> list[dict[str, Any]]:
    return [{"key": key, "count": count} for key, count in counter.most_common(limit)]


def _label_text(row: Mapping[str, Any], keys: Iterable[str]) -> str:
    return " ".join(str(row.get(key) or "") for key in keys).lower()


def _is_stage3_green_after(row: Mapping[str, Any]) -> bool:
    text = _label_text(row, ("stage_label_after", "simulated_stage_current_profile", "simulated_stage"))
    return "stage3-green" in text


def _is_green_trap_downgrade(row: Mapping[str, Any]) -> bool:
    before = _label_text(row, ("stage_label_before",))
    after = _label_text(row, ("stage_label_after", "simulated_stage_current_profile", "simulated_stage"))
    return "stage3-green" in before and "stage3-green" not in after


def _score_dict(row: Mapping[str, Any]) -> dict[str, float]:
    for field in SCORE_DICT_FIELDS:
        value = row.get(field)
        if not isinstance(value, Mapping):
            continue
        parsed: dict[str, float] = {}
        for key, raw in value.items():
            number = _safe_float(raw)
            if number is not None:
                parsed[str(key)] = number
        if parsed:
            return parsed
    return {}


def _top_axes(row: Mapping[str, Any], limit: int = 8) -> list[tuple[str, float]]:
    scores = _score_dict(row)
    positive = [(key, value) for key, value in scores.items() if value > 0]
    positive.sort(key=lambda item: (-item[1], item[0]))
    return positive[:limit]


def _status_for_axis(key: str, inventory: Mapping[str, Any]) -> str:
    return _axis_contract_row(key, 1, inventory)["runtime_contract_status"]


def _current_runtime_by_archetype(census_payload: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row.get("group_key")): dict(row) for row in census_payload.get("archetype_rows", []) or []}


def _runtime_short(row: Mapping[str, Any] | None) -> dict[str, Any]:
    if not row:
        return {
            "current_runtime_status": "not_exercised_in_current_benchmark",
            "runtime_row_count": 0,
            "runtime_max_score": None,
            "runtime_stage_counts": {},
            "runtime_top_zero_fields": [],
            "runtime_top_failed_gates": [],
            "runtime_best_row": None,
        }
    zero_fields = [
        {"field": key, "zero_count": value.get("zero_count"), "row_count": value.get("row_count")}
        for key, value in (row.get("zero_field_counts") or {}).items()
    ]
    zero_fields.sort(key=lambda item: (-(item.get("zero_count") or 0), item["field"]))
    failed_gates = [{"gate": key, "count": value} for key, value in (row.get("failed_gate_counts") or {}).items()]
    failed_gates.sort(key=lambda item: (-int(item.get("count") or 0), item["gate"]))
    return {
        "current_runtime_status": "exercised_in_current_benchmark",
        "runtime_row_count": row.get("row_count", 0),
        "runtime_max_score": row.get("max_score"),
        "runtime_stage_counts": row.get("stage_counts", {}),
        "runtime_top_zero_fields": zero_fields[:6],
        "runtime_top_failed_gates": failed_gates[:6],
        "runtime_best_row": row.get("best_row"),
    }


def _axis_rows_for_case(row: Mapping[str, Any], inventory: Mapping[str, Any], limit: int = 8) -> list[dict[str, Any]]:
    axis_rows = []
    for key, value in _top_axes(row, limit=limit):
        contract = _axis_contract_row(key, 1, inventory)
        axis_rows.append(
            {
                "research_score_key": key,
                "score_value": value,
                "family": contract["family"],
                "runtime_contract_status": contract["runtime_contract_status"],
                "supported_candidate_runtime_fields": list(contract.get("supported_candidate_runtime_fields") or ()),
                "candidate_runtime_fields": list(contract.get("candidate_runtime_fields") or ()),
            }
        )
    return axis_rows


def _plain_case(row: Mapping[str, Any], axis_rows: list[Mapping[str, Any]], runtime: Mapping[str, Any]) -> str:
    archetype = str(row.get("canonical_archetype_id") or "")
    keys = ", ".join(str(axis.get("research_score_key")) for axis in axis_rows[:4]) or "no score axis"
    runtime_status = runtime.get("current_runtime_status")
    if runtime_status == "not_exercised_in_current_benchmark":
        return (
            f"과거 Green은 {keys} 같은 연구축으로 만들어졌지만, 현재 benchmark에는 {archetype} replay row가 없어 "
            "점수식이 시험되지 않았다."
        )
    zeros = ", ".join(str(item.get("field")) for item in runtime.get("runtime_top_zero_fields", [])[:3]) or "none"
    gates = ", ".join(str(item.get("gate")) for item in runtime.get("runtime_top_failed_gates", [])[:3]) or "none"
    return (
        f"과거 Green은 {keys} 같은 연구축으로 만들어졌고, 현재 runtime은 같은 아키타입을 채점했지만 "
        f"{zeros} field와 {gates} gate에서 막힌다."
    )


def _case_row(row: Mapping[str, Any], inventory: Mapping[str, Any], runtime_by_arch: Mapping[str, dict[str, Any]]) -> dict[str, Any]:
    axis_rows = _axis_rows_for_case(row, inventory)
    runtime = _runtime_short(runtime_by_arch.get(str(row.get("canonical_archetype_id") or "")))
    case = {field: row.get(field) for field in CASE_FIELDS}
    case["top_positive_score_axes"] = axis_rows
    case["score_axis_contract_status_counts"] = _counter_dict(
        Counter(str(axis.get("runtime_contract_status")) for axis in axis_rows)
    )
    case["score_axis_family_counts"] = _counter_dict(Counter(str(axis.get("family")) for axis in axis_rows))
    case.update(runtime)
    case["plain_translation_gap"] = _plain_case(row, axis_rows, runtime)
    return case


def _archetype_rows(
    green_rows: list[Mapping[str, Any]],
    inventory: Mapping[str, Any],
    runtime_by_arch: Mapping[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in green_rows:
        grouped[str(row.get("canonical_archetype_id") or "UNKNOWN")].append(row)
    rows = []
    for archetype, group in sorted(grouped.items()):
        axis_counts: Counter[str] = Counter()
        family_counts: Counter[str] = Counter()
        status_counts: Counter[str] = Counter()
        verdict_counts: Counter[str] = Counter()
        for row in group:
            verdict_counts[_verdict_bucket(row.get("current_profile_verdict"))] += 1
            for key, _value in _top_axes(row, limit=8):
                axis_counts[key] += 1
                family = _family_for_key(key)
                family_counts[family] += 1
                status_counts[_status_for_axis(key, inventory)] += 1
        runtime = _runtime_short(runtime_by_arch.get(archetype))
        rows.append(
            {
                "canonical_archetype_id": archetype,
                "historical_green_case_count": len(group),
                "current_profile_verdict_counts": _counter_dict(verdict_counts),
                "top_green_score_axes": _top_counter_rows(axis_counts, limit=10),
                "top_green_score_families": _top_counter_rows(family_counts, limit=10),
                "top_axis_contract_status_counts": _counter_dict(status_counts),
                **runtime,
            }
        )
    return rows


def build_v12_historical_green_case_runtime_translation_ledger(
    *,
    score_simulation_rows: Iterable[Mapping[str, Any]] | None = None,
    score_simulation_root: str | Path = DEFAULT_SCORE_SIMULATION_ROOT,
    runtime_inventory: Mapping[str, Any] | None = None,
    current_census_payload: Mapping[str, Any] | None = None,
    current_census_path: str | Path = DEFAULT_CURRENT_CENSUS_PATH,
    sample_limit: int = 40,
) -> dict[str, Any]:
    """Build a row-level ledger from historical Green research to current runtime."""

    rows = (
        [dict(row) for row in score_simulation_rows]
        if score_simulation_rows is not None
        else _extract_score_simulation_rows(score_simulation_root)
    )
    inventory = dict(runtime_inventory or build_runtime_field_inventory())
    current_census = dict(current_census_payload or _read_json(current_census_path))
    runtime_by_arch = _current_runtime_by_archetype(current_census)
    source_fields, derived_fields, _all_fields = _runtime_sets(inventory)

    green_after_rows = [row for row in rows if _is_stage3_green_after(row)]
    green_trap_rows = [row for row in rows if _is_green_trap_downgrade(row)]
    axis_occurrence_counts: Counter[str] = Counter()
    family_occurrence_counts: Counter[str] = Counter()
    status_occurrence_counts: Counter[str] = Counter()
    archetype_counts: Counter[str] = Counter()
    verdict_counts: Counter[str] = Counter()
    exact_source_occurrences = 0
    exact_derived_occurrences = 0
    for row in green_after_rows:
        archetype_counts[str(row.get("canonical_archetype_id") or "UNKNOWN")] += 1
        verdict_counts[_verdict_bucket(row.get("current_profile_verdict"))] += 1
        for key, _value in _top_axes(row, limit=8):
            axis_occurrence_counts[key] += 1
            family = _family_for_key(key)
            family_occurrence_counts[family] += 1
            status = _status_for_axis(key, inventory)
            status_occurrence_counts[status] += 1
            if key in source_fields:
                exact_source_occurrences += 1
            elif key in derived_fields:
                exact_derived_occurrences += 1

    # Prefer examples that cover different archetypes and current runtime states.
    sorted_green_rows = sorted(
        green_after_rows,
        key=lambda row: (
            str(row.get("canonical_archetype_id") or ""),
            str(row.get("case_id") or ""),
            str(row.get("trigger_id") or ""),
        ),
    )
    sample_rows = [_case_row(row, inventory, runtime_by_arch) for row in sorted_green_rows[:sample_limit]]
    archetype_rows = _archetype_rows(green_after_rows, inventory, runtime_by_arch)
    exercised_green_arch = [
        row for row in archetype_rows if row.get("current_runtime_status") == "exercised_in_current_benchmark"
    ]
    unexercised_green_arch = [
        row for row in archetype_rows if row.get("current_runtime_status") == "not_exercised_in_current_benchmark"
    ]
    return {
        "schema_version": "v12_historical_green_case_runtime_translation_ledger_v1",
        "scope": "historical_stage3_green_score_simulation_cases_to_current_runtime",
        "summary": {
            "plain_answer": (
                "과거 연구에서 Stage3-Green이 된 case들은 실제로 존재한다. 다만 그 Green은 "
                "margin_bridge_score, customer_quality_score, capital_return_execution_score 같은 연구 score축으로 만들어졌고, "
                "현재 runtime scorer는 그 이름을 직접 읽지 않는다. source-backed primitive로 번역되지 않으면 현재 점수는 낮게 남는다."
            ),
            "score_simulation_row_count": len(rows),
            "historical_stage3_green_after_case_count": len(green_after_rows),
            "historical_green_trap_downgrade_count": len(green_trap_rows),
            "historical_green_archetype_count": len(archetype_counts),
            "historical_green_archetype_exercised_in_current_benchmark_count": len(exercised_green_arch),
            "historical_green_archetype_unexercised_in_current_benchmark_count": len(unexercised_green_arch),
            "top_green_archetype_counts": _top_counter_rows(archetype_counts, limit=20),
            "top_green_score_axis_occurrences": _top_counter_rows(axis_occurrence_counts, limit=20),
            "top_green_score_family_occurrences": _top_counter_rows(family_occurrence_counts, limit=20),
            "top_axis_contract_status_counts": _counter_dict(status_occurrence_counts),
            "exact_source_axis_occurrence_count": exact_source_occurrences,
            "exact_derived_axis_occurrence_count": exact_derived_occurrences,
            "current_profile_verdict_counts": _counter_dict(verdict_counts),
            "runtime_translation_conclusion": (
                "누적 연구는 Green 사례와 반례를 만들었지만, 그 score축 대부분은 runtime source field와 1:1이 아니다. "
                "따라서 누적 연구가 weight/profile에는 들어가도 현재 replay에서 후보, parser-feature bridge, gate 중 하나가 비면 Green으로 재현되지 않는다."
            ),
        },
        "archetype_rows": archetype_rows,
        "sample_green_case_rows": sample_rows,
        "green_trap_downgrade_count_by_archetype": _counter_dict(
            Counter(str(row.get("canonical_archetype_id") or "UNKNOWN") for row in green_trap_rows)
        ),
        "family_runtime_candidate_fields": {key: list(value) for key, value in FAMILY_RUNTIME_CANDIDATES.items()},
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _join(values: Iterable[Any]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "none"


def _top_count_text(rows: list[Mapping[str, Any]], limit: int = 5) -> str:
    if not rows:
        return "none"
    return ", ".join(f"{row.get('key')}:{row.get('count')}" for row in rows[:limit]) or "none"


def _axis_text(rows: list[Mapping[str, Any]], limit: int = 5) -> str:
    if not rows:
        return "none"
    return "<br>".join(
        "{key}={value} [{status}] -> {fields}".format(
            key=row.get("research_score_key"),
            value=row.get("score_value"),
            status=row.get("runtime_contract_status"),
            fields=_join((row.get("supported_candidate_runtime_fields") or [])[:3]),
        )
        for row in rows[:limit]
    )


def _runtime_text(row: Mapping[str, Any]) -> str:
    if row.get("current_runtime_status") != "exercised_in_current_benchmark":
        return "not exercised"
    best = row.get("runtime_best_row") or {}
    zeros = ", ".join(str(item.get("field")) for item in row.get("runtime_top_zero_fields", [])[:3]) or "none"
    gates = ", ".join(str(item.get("gate")) for item in row.get("runtime_top_failed_gates", [])[:3]) or "none"
    return "{stage}/{score} max={max_score}; zero={zeros}; gates={gates}".format(
        stage=best.get("current_stage"),
        score=best.get("current_score"),
        max_score=row.get("runtime_max_score"),
        zeros=zeros,
        gates=gates,
    )


def render_v12_historical_green_case_runtime_translation_ledger(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    lines = [
        "# V12 Historical Green Case Runtime Translation Ledger",
        "",
        "이 문서는 과거 연구에서 Stage3-Green으로 처리된 case가 어떤 score축으로 Green이었는지 row 단위로 보여준다.",
        "그리고 그 score축이 현재 runtime field/gate와 어떻게 끊기는지 현재 benchmark census와 붙인다.",
        "",
        "## Summary",
        "",
        f"- plain_answer: {summary.get('plain_answer')}",
        f"- score_simulation_row_count: `{summary.get('score_simulation_row_count')}`",
        f"- historical_stage3_green_after_case_count: `{summary.get('historical_stage3_green_after_case_count')}`",
        f"- historical_green_trap_downgrade_count: `{summary.get('historical_green_trap_downgrade_count')}`",
        f"- historical_green_archetype_count: `{summary.get('historical_green_archetype_count')}`",
        f"- historical_green_archetype_exercised_in_current_benchmark_count: `{summary.get('historical_green_archetype_exercised_in_current_benchmark_count')}`",
        f"- historical_green_archetype_unexercised_in_current_benchmark_count: `{summary.get('historical_green_archetype_unexercised_in_current_benchmark_count')}`",
        f"- top_green_score_axis_occurrences: `{_top_count_text(summary.get('top_green_score_axis_occurrences') or [], limit=10)}`",
        f"- top_green_score_family_occurrences: `{_top_count_text(summary.get('top_green_score_family_occurrences') or [], limit=10)}`",
        f"- top_axis_contract_status_counts: `{summary.get('top_axis_contract_status_counts')}`",
        f"- exact_source_axis_occurrence_count: `{summary.get('exact_source_axis_occurrence_count')}`",
        f"- exact_derived_axis_occurrence_count: `{summary.get('exact_derived_axis_occurrence_count')}`",
        f"- current_profile_verdict_counts: `{summary.get('current_profile_verdict_counts')}`",
        f"- runtime_translation_conclusion: {summary.get('runtime_translation_conclusion')}",
        "",
        "## Archetype Green Translation Rows",
        "",
        "| archetype | historical Green cases | current runtime | top Green score axes | top families | contract status counts | verdicts |",
        "| --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for row in payload.get("archetype_rows", []) or []:
        lines.append(
            "| {arch} | {count} | {runtime} | {axes} | {families} | {statuses} | {verdicts} |".format(
                arch=row.get("canonical_archetype_id"),
                count=row.get("historical_green_case_count"),
                runtime=_runtime_text(row),
                axes=_top_count_text(row.get("top_green_score_axes") or [], limit=5),
                families=_top_count_text(row.get("top_green_score_families") or [], limit=5),
                statuses=row.get("top_axis_contract_status_counts"),
                verdicts=row.get("current_profile_verdict_counts"),
            )
        )
    lines.extend(
        [
            "",
            "## Sample Historical Green Cases",
            "",
            "| case | archetype | stage/score | return label | top positive score axes | current runtime linkage | plain gap |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload.get("sample_green_case_rows", []) or []:
        stage = "{before} -> {after}; score {score_before}->{score_after}".format(
            before=_fmt(row.get("stage_label_before") or row.get("simulated_stage_current_profile")),
            after=_fmt(row.get("stage_label_after") or row.get("simulated_stage")),
            score_before=_fmt(row.get("weighted_score_before") or row.get("weighted_total_pre_bonus")),
            score_after=_fmt(row.get("weighted_score_after") or row.get("weighted_total_stage2_actionable_bonus")),
        )
        case = "{case_id}<br>{symbol} line {line}".format(
            case_id=_fmt(row.get("case_id")),
            symbol=_fmt(row.get("symbol")),
            line=_fmt(row.get("source_line")),
        )
        lines.append(
            "| {case} | {arch} | {stage} | {label} | {axes} | {runtime} | {gap} |".format(
                case=case,
                arch=row.get("canonical_archetype_id"),
                stage=stage,
                label=_fmt(row.get("score_return_alignment_label") or row.get("current_profile_verdict")),
                axes=_axis_text(row.get("top_positive_score_axes") or [], limit=5),
                runtime=_runtime_text(row),
                gap=row.get("plain_translation_gap"),
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 과거 Green은 실제로 있었다. 예를 들어 C21은 `roe_pbr_capital_return_score`, `capital_return_execution_score`로 Green이 됐다.",
            "- 하지만 현재 runtime benchmark가 C21을 채점하지 않으면 그 좋은 연구는 현재 점수로 나타날 기회가 없다.",
            "- C20처럼 현재 runtime에 후보가 있어도, 과거 Green의 `margin_bridge_score`, `revision_score`, `customer_quality_score`가 source-backed sell-through/reorder/margin field로 안 바뀌면 낮게 남는다.",
            "- 하닉/삼성도 같은 구조다. HBM 전망 자체가 문제가 아니라, research score axis를 runtime primitive로 옮기는 다리가 약하다.",
            "- 결론: 누적 연구는 점수표의 방향을 만들었지만, 현재 파이프라인은 그 연구축을 직접 채점하지 않는다. 후보/archive, parser-feature bridge, stage gate가 모두 연결돼야 Green이 재현된다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_historical_green_case_runtime_translation_ledger(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_historical_green_case_runtime_translation_ledger()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_historical_green_case_runtime_translation_ledger(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_historical_green_case_runtime_translation_ledger()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
