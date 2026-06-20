"""Join v12 research Green evidence with current runtime gap status."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import json

from .taxonomy import CANONICAL_ARCHETYPE_IDS
from .v12_cross_archetype_score_loss_trace import LOSS_BUCKETS
from .v12_runtime_fixture_candidates import (
    ARCHETYPE_RUNTIME_BRIDGE_SPECS,
    DEFAULT_RUNTIME_BRIDGE_SPEC,
    _case_key,
    _fixture_ready,
    _green_fixture_ready,
    _is_green_row,
    _is_guard_row,
    _is_raw_green_trigger,
    _row_view,
)


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    path_obj = Path(path)
    if not path_obj.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path_obj.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _truthy(value: Any) -> bool:
    return str(value or "").strip().lower() in {"1", "1.0", "true", "yes", "y"}


def _coverage_by_archetype(coverage_payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(row.get("canonical_archetype_id")): row
        for row in coverage_payload.get("archetypes", [])
        if row.get("canonical_archetype_id")
    }


def _spec_by_archetype(spec_payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in spec_payload.get("rows", []):
        archetype = str(row.get("canonical_archetype_id") or "")
        if archetype:
            grouped[archetype].append(row)
    return grouped


def _role_candidate(spec_rows: list[dict[str, Any]], role: str) -> dict[str, Any]:
    row = next((item for item in spec_rows if item.get("role") == role), {})
    return dict(row.get("candidate") or {})


def _top_values(rows: list[dict[str, Any]], key: str, limit: int = 4) -> list[dict[str, Any]]:
    counter = Counter(str(row.get(key) or "") for row in rows if str(row.get(key) or "").strip())
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def _best_green_examples(rows: list[dict[str, Any]], archetype: str, limit: int = 2) -> list[dict[str, Any]]:
    ordered = sorted(rows, key=lambda row: _case_key(row, archetype), reverse=True)
    return [_row_view(row) for row in ordered[:limit]]


def _runtime_bridge_spec(archetype: str) -> dict[str, Any]:
    return dict(ARCHETYPE_RUNTIME_BRIDGE_SPECS.get(archetype, DEFAULT_RUNTIME_BRIDGE_SPEC))


def _loss_layer(status: str) -> str:
    return LOSS_BUCKETS.get(status, LOSS_BUCKETS["runtime_needs_review"])["loss_layer"]


def _root_cause(*, clean_green_count: int, spec_rows: list[dict[str, Any]], runtime_status: str) -> str:
    if clean_green_count <= 0:
        return "research_green_not_source_backed_enough_for_fixture"
    if not spec_rows:
        return "research_green_exists_but_not_materialized_into_replay_spec"
    if runtime_status == "not_in_current_benchmark":
        return "research_green_fixture_not_exercised_by_current_runtime_benchmark"
    if runtime_status == "runtime_input_evidence_missing":
        return "runtime_candidate_has_insufficient_source_backed_inputs"
    if runtime_status == "runtime_bridge_axes_missing":
        return "research_green_axes_not_structured_into_runtime_fields"
    if runtime_status == "runtime_stage3_gate_blocked":
        return "runtime_fields_present_but_weighted_green_gate_still_blocks"
    if runtime_status == "runtime_green_or_near_ready":
        return "near_ready_requires_exact_positive_guard_replay"
    return "manual_review_required"


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def build_v12_research_green_runtime_gap_matrix(
    *,
    representative_rows: list[dict[str, Any]],
    spec_payload: dict[str, Any],
    coverage_payload: dict[str, Any],
) -> dict[str, Any]:
    """Build an archetype matrix from research Green evidence to runtime gaps."""

    rows_by_archetype: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in representative_rows:
        archetype = str(row.get("canonical_archetype_id") or "")
        if archetype:
            rows_by_archetype[archetype].append(row)

    coverage = _coverage_by_archetype(coverage_payload)
    spec = _spec_by_archetype(spec_payload)
    matrix_rows: list[dict[str, Any]] = []
    for archetype in CANONICAL_ARCHETYPE_IDS:
        research_rows = rows_by_archetype.get(archetype, [])
        raw_green_rows = [row for row in research_rows if _is_raw_green_trigger(row)]
        fixture_green_rows = [row for row in research_rows if _is_green_row(row)]
        clean_green_rows = [row for row in research_rows if _green_fixture_ready(row)]
        guard_rows = [row for row in research_rows if _is_guard_row(row)]
        clean_guard_rows = [row for row in guard_rows if _fixture_ready(row)]
        coverage_row = coverage.get(archetype, {})
        spec_rows = spec.get(archetype, [])
        runtime_status = str(coverage_row.get("runtime_gap_status") or "not_in_current_benchmark")
        bridge_spec = _runtime_bridge_spec(archetype)
        matrix_rows.append(
            {
                "canonical_archetype_id": archetype,
                "large_sector_id": coverage_row.get("large_sector_id"),
                "research_representative_row_count": len(research_rows),
                "research_raw_stage3_green_count": len(raw_green_rows),
                "research_fixture_green_count": len(fixture_green_rows),
                "research_clean_green_count": len(clean_green_rows),
                "research_guard_row_count": len(guard_rows),
                "research_clean_guard_count": len(clean_guard_rows),
                "research_green_current_profile_too_late_count": sum(
                    1 for row in raw_green_rows if "too_late" in str(row.get("current_profile_verdict") or "")
                ),
                "research_green_current_profile_false_positive_count": sum(
                    1 for row in raw_green_rows if _truthy(row.get("current_profile_false_positive"))
                ),
                "top_green_fine_archetypes": _top_values(raw_green_rows, "fine_archetype_id"),
                "top_green_verdicts": _top_values(raw_green_rows, "current_profile_verdict"),
                "green_examples": _best_green_examples(clean_green_rows, archetype),
                "runtime_bridge_group": bridge_spec.get("runtime_bridge_group"),
                "expected_runtime_primitives": list(bridge_spec.get("expected_runtime_primitives") or ()),
                "required_bridge_axes": list(coverage_row.get("required_bridge_axes") or ()),
                "missing_required_bridge_axes": list(coverage_row.get("missing_required_bridge_axes") or ()),
                "runtime_gap_status": runtime_status,
                "runtime_loss_layer": _loss_layer(runtime_status),
                "runtime_candidate_count": coverage_row.get("runtime_candidate_count", 0),
                "runtime_stage_distribution": coverage_row.get("runtime_stage_distribution") or {},
                "runtime_max_score": coverage_row.get("runtime_max_score"),
                "runtime_green_count": coverage_row.get("runtime_green_count", 0),
                "top_failed_gates": list(coverage_row.get("top_failed_gates") or ()),
                "spec_green_candidate": _role_candidate(spec_rows, "green"),
                "spec_guard_candidate": _role_candidate(spec_rows, "guard"),
                "root_cause": _root_cause(
                    clean_green_count=len(clean_green_rows),
                    spec_rows=spec_rows,
                    runtime_status=runtime_status,
                ),
            }
        )

    root_cause_counts = Counter(row["root_cause"] for row in matrix_rows)
    status_counts = Counter(row["runtime_gap_status"] for row in matrix_rows)
    missing_axis_counts: Counter[str] = Counter()
    for row in matrix_rows:
        missing_axis_counts.update(row["missing_required_bridge_axes"])
    return {
        "schema_version": "v12_research_green_runtime_gap_matrix_v1",
        "scope": "canonical_archetype_representative_research_rows_to_current_runtime_gap",
        "representative_row_count": len(representative_rows),
        "archetype_count": len(matrix_rows),
        "raw_stage3_green_count": sum(row["research_raw_stage3_green_count"] for row in matrix_rows),
        "fixture_green_count": sum(row["research_fixture_green_count"] for row in matrix_rows),
        "clean_green_count": sum(row["research_clean_green_count"] for row in matrix_rows),
        "clean_guard_count": sum(row["research_clean_guard_count"] for row in matrix_rows),
        "archetypes_with_clean_green_count": sum(1 for row in matrix_rows if row["research_clean_green_count"] > 0),
        "archetypes_with_clean_green_and_clean_guard_count": sum(
            1
            for row in matrix_rows
            if row["research_clean_green_count"] > 0 and row["research_clean_guard_count"] > 0
        ),
        "runtime_gap_status_counts": _counter_dict(status_counts),
        "root_cause_counts": _counter_dict(root_cause_counts),
        "missing_required_bridge_axis_counts": _counter_dict(missing_axis_counts),
        "rows": matrix_rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _join(values: list[Any]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "none"


def _top_text(values: list[dict[str, Any]]) -> str:
    return ", ".join(f"{item.get('value')}:{item.get('count')}" for item in values[:3]) or "none"


def _candidate_text(candidate: dict[str, Any]) -> str:
    symbol = str(candidate.get("symbol") or "").strip()
    as_of = str(candidate.get("as_of_date") or candidate.get("trigger_date") or "").strip()
    case_id = str(candidate.get("case_id") or "").strip()
    return " ".join(part for part in (symbol, as_of, case_id) if part) or "none"


def render_v12_research_green_runtime_gap_matrix(payload: dict[str, Any]) -> str:
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Research Green Runtime Gap Matrix",
        "",
        "이 문서는 누적 연구자료에서 Green으로 보던 근거와 현재 runtime gap을 아키타입별로 붙인 장부다.",
        "핵심은 연구 점수를 runtime score에 그대로 더하지 않고, source-backed primitive로 다시 변환해야 한다는 점이다.",
        "",
        "## Summary",
        "",
        f"- representative_row_count: `{payload.get('representative_row_count', 0)}`",
        f"- archetype_count: `{payload.get('archetype_count', 0)}`",
        f"- raw_stage3_green_count: `{payload.get('raw_stage3_green_count', 0)}`",
        f"- fixture_green_count: `{payload.get('fixture_green_count', 0)}`",
        f"- clean_green_count: `{payload.get('clean_green_count', 0)}`",
        f"- clean_guard_count: `{payload.get('clean_guard_count', 0)}`",
        f"- archetypes_with_clean_green_count: `{payload.get('archetypes_with_clean_green_count', 0)}`",
        f"- archetypes_with_clean_green_and_clean_guard_count: `{payload.get('archetypes_with_clean_green_and_clean_guard_count', 0)}`",
        f"- runtime_gap_status_counts: `{payload.get('runtime_gap_status_counts', {})}`",
        f"- root_cause_counts: `{payload.get('root_cause_counts', {})}`",
        f"- missing_required_bridge_axis_counts: `{payload.get('missing_required_bridge_axis_counts', {})}`",
        "",
        "## Archetype Matrix",
        "",
        "| archetype | research Green clean/fixture/raw | Green evidence shape | runtime gap | layer | missing axes | candidates/max | root cause |",
        "| --- | ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(
        rows,
        key=lambda item: (
            str(item.get("root_cause")),
            -int(item.get("research_clean_green_count") or 0),
            str(item.get("canonical_archetype_id")),
        ),
    ):
        green_counts = "{clean}/{fixture}/{raw}".format(
            clean=row.get("research_clean_green_count", 0),
            fixture=row.get("research_fixture_green_count", 0),
            raw=row.get("research_raw_stage3_green_count", 0),
        )
        runtime = "{status}".format(status=row.get("runtime_gap_status"))
        candidate_score = "{count}/{score}".format(
            count=row.get("runtime_candidate_count", 0),
            score=_fmt(row.get("runtime_max_score")),
        )
        evidence_shape = _top_text(row.get("top_green_fine_archetypes") or [])
        lines.append(
            "| {arch} | {green_counts} | {shape} | {runtime} | {layer} | {axes} | {candidate_score} | {cause} |".format(
                arch=row.get("canonical_archetype_id"),
                green_counts=green_counts,
                shape=evidence_shape,
                runtime=runtime,
                layer=row.get("runtime_loss_layer"),
                axes=_join(row.get("missing_required_bridge_axes") or []),
                candidate_score=candidate_score,
                cause=row.get("root_cause"),
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- `clean/fixture/raw`는 source-backed Green / marker 제외 Green / raw Stage3-Green 순서다.",
            "- 연구 Green은 이미 많다. 하지만 current benchmark가 그 fixture를 실행하지 않거나, 실행해도 bridge field가 0이면 Green 점수로 올라가지 않는다.",
            "- 쉬운 예: 연구 장부에 `C21 삼성화재 capital return Green`이 있어도, runtime replay에 그 as-of fixture가 없으면 점수식이 맞는지조차 시험하지 못한다.",
            "- 쉬운 예: C10 삼성은 runtime 후보와 리포트가 있어 parser-feature bridge를 점검할 수 있지만, C01 산업재는 후보 row의 입력 가족이 약해 먼저 source-backed 입력을 채워야 한다.",
            "",
            "## Fixture Examples",
            "",
            "| archetype | Green candidate | guard candidate | expected primitives |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in sorted(rows, key=lambda item: str(item.get("canonical_archetype_id"))):
        if row.get("research_clean_green_count", 0) <= 0:
            continue
        lines.append(
            "| {arch} | {green} | {guard} | {primitives} |".format(
                arch=row.get("canonical_archetype_id"),
                green=_candidate_text(row.get("spec_green_candidate") or {}),
                guard=_candidate_text(row.get("spec_guard_candidate") or {}),
                primitives=_join(row.get("expected_runtime_primitives") or []),
            )
        )
    return "\n".join(lines) + "\n"


def write_v12_research_green_runtime_gap_matrix(
    *,
    representative_rows_path: str | Path,
    spec_path: str | Path,
    coverage_board_path: str | Path,
    output_json_path: str | Path,
    output_markdown_path: str | Path,
) -> dict[str, Path]:
    payload = build_v12_research_green_runtime_gap_matrix(
        representative_rows=_read_jsonl(representative_rows_path),
        spec_payload=_read_json(spec_path),
        coverage_payload=_read_json(coverage_board_path),
    )
    json_path = Path(output_json_path)
    md_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_research_green_runtime_gap_matrix(payload), encoding="utf-8")
    return {"json": json_path, "markdown": md_path}
