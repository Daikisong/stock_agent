"""Build the next implementation backlog from V12 runtime gap audits."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping
import json


DEFAULT_EXECUTION_PATH_PATH = Path("docs/0619/v12_runtime_execution_path_map_2026-06-19.json")
DEFAULT_REPAIR_BOARD_PATH = Path("docs/0619/v12_runtime_repair_priority_board_2026-06-19.json")
DEFAULT_FIELD_AUDIT_PATH = Path("docs/0619/v12_bridge_spec_runtime_field_audit_2026-06-19.json")
DEFAULT_REPLAY_SPEC_PATH = Path("docs/0619/v12_runtime_replay_fixture_spec_2026-06-19.json")
DEFAULT_READINESS_PATH = Path("docs/0619/v12_exact_fixture_replay_readiness_2026-06-19.json")
DEFAULT_FUNNEL_AUDIT_PATH = Path("docs/0619/v12_fixture_candidate_funnel_audit_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_runtime_repair_execution_backlog_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_runtime_repair_execution_backlog_2026-06-19.md")


IMPLEMENTATION_LANE_BY_STOP_LAYER = {
    "candidate_replay_archive": "01_fixture_archive_and_candidate_funnel",
    "parser_feature_bridge": "02_parser_feature_bridge_contract",
    "stage_gate": "03_weighted_gate_validation_after_fields",
    "manual_review": "04_manual_gap_classification",
}
IMPLEMENTATION_LANE_BY_PRIMARY_REPAIR_LANE = {
    "candidate_funnel_or_benchmark_replay": "01_fixture_archive_and_candidate_funnel",
    "exact_fixture_archive": "01_fixture_archive_and_candidate_funnel",
    "runtime_input_evidence_coverage": "01_fixture_archive_and_candidate_funnel",
    "gate_bridge_axis_alignment": "02_parser_feature_bridge_contract",
    "runtime_field_strength": "02_parser_feature_bridge_contract",
    "weighted_gate_threshold_or_component_balance": "03_weighted_gate_validation_after_fields",
}
STOP_LAYER_BY_IMPLEMENTATION_LANE = {
    "01_fixture_archive_and_candidate_funnel": "candidate_replay_archive",
    "02_parser_feature_bridge_contract": "parser_feature_bridge",
    "03_weighted_gate_validation_after_fields": "stage_gate",
    "04_manual_gap_classification": "manual_review",
}


CODE_FILES_BY_IMPLEMENTATION_LANE = {
    "01_fixture_archive_and_candidate_funnel": [
        "src/e2r/backtest/asof_stage_promotion_autopsy.py",
        "src/e2r/pipeline/korea_live_lite.py",
        "historical official/search/report fixture archive",
    ],
    "02_parser_feature_bridge_contract": [
        "src/e2r/research/report_parser.py",
        "src/e2r/features.py::DeterministicFeatureEngineer.engineer",
        "src/e2r/features.py::_sector_metrics",
        "src/e2r/features.py::_contract_quality_score",
        "src/e2r/features.py::_backlog_rpo_visibility_score",
        "src/e2r/stage_gate_diagnostics.py::diagnose_stage_gates",
    ],
    "03_weighted_gate_validation_after_fields": [
        "src/e2r/scoring.py::_apply_archetype_runtime_weights",
        "src/e2r/staging.py::StageClassifier._is_stage_3_green",
        "src/e2r/stage_gate_diagnostics.py::diagnose_stage_gates",
    ],
    "04_manual_gap_classification": [
        "docs/0619 runtime audits",
        "src/e2r/calibration/v12_* audit scripts",
    ],
}


TESTS_BY_IMPLEMENTATION_LANE = {
    "01_fixture_archive_and_candidate_funnel": [
        "tests/test_v12_exact_fixture_replay_readiness.py",
        "tests/test_v12_fixture_candidate_funnel_audit.py",
        "new exact Green/guard replay fixture tests",
    ],
    "02_parser_feature_bridge_contract": [
        "tests/test_report_parser.py",
        "tests/test_features.py",
        "tests/test_stage_gate_diagnostics.py",
        "new archetype-specific positive/guard feature bridge tests",
    ],
    "03_weighted_gate_validation_after_fields": [
        "tests/test_scoring.py",
        "tests/test_staging.py",
        "tests/test_stage_gate_diagnostics.py",
        "new positive/guard gate parity tests",
    ],
    "04_manual_gap_classification": [
        "tests/test_v12_runtime_execution_path_map.py",
        "tests/test_v12_runtime_repair_execution_backlog.py",
    ],
}


DO_NOT_DO_BY_IMPLEMENTATION_LANE = {
    "01_fixture_archive_and_candidate_funnel": "Green 연구 row를 production score 입력으로 바로 쓰지 않는다. point-in-time archive로 재현 가능해야 한다.",
    "02_parser_feature_bridge_contract": "하닉/HBM 이름 조건으로 보너스를 주지 않는다. parser output, feature field, gate axis를 source-backed로 맞춘다.",
    "03_weighted_gate_validation_after_fields": "field가 비어 있는 상태에서 Green threshold를 낮추지 않는다. positive/guard pair가 준비된 뒤 조정한다.",
    "04_manual_gap_classification": "manual review를 통과 처리로 간주하지 않는다. 후보/field/gate 중 하나로 다시 분류해야 한다.",
}


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _rows_by_archetype(payload: Mapping[str, Any], key: str = "rows") -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): dict(row) for row in payload.get(key, [])}


def _rows_grouped_by_archetype(payload: Mapping[str, Any], key: str = "rows") -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in payload.get(key, []) or []:
        grouped[str(row.get("canonical_archetype_id"))].append(dict(row))
    return dict(grouped)


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _candidate_id(row: Mapping[str, Any]) -> str:
    candidate = row.get("candidate") or {}
    symbol = candidate.get("symbol") or "unknown"
    as_of_date = candidate.get("as_of_date") or "unknown_date"
    role = row.get("role") or "unknown_role"
    return f"{role}:{symbol}@{as_of_date}"


def _fixture_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "row_count": len(rows),
        "roles": sorted({str(row.get("role")) for row in rows}),
        "candidates": [_candidate_id(row) for row in rows[:4]],
    }


def _readiness_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    missing_counter: Counter[str] = Counter()
    status_counter: Counter[str] = Counter()
    for row in rows:
        status_counter[str(row.get("retrospective_readiness_status") or "")] += 1
        for item in row.get("retrospective_missing_inputs") or ():
            missing_counter[str(item)] += 1
    return {
        "retrospective_status_counts": _counter_dict(status_counter),
        "retrospective_missing_input_counts": _counter_dict(missing_counter),
    }


def _funnel_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    status_counter: Counter[str] = Counter()
    root_counter: Counter[str] = Counter()
    for row in rows:
        status_counter[str(row.get("fixture_funnel_status") or "")] += 1
        root_counter[str(row.get("funnel_root_cause") or "")] += 1
    return {
        "fixture_funnel_status_counts": _counter_dict(status_counter),
        "funnel_root_cause_counts": _counter_dict(root_counter),
    }


def _axis_status_counts(field_row: Mapping[str, Any]) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for item in field_row.get("axis_contract_statuses") or ():
        counter[str(item.get("status") or "")] += 1
    return _counter_dict(counter)


def _implementation_lane(row: Mapping[str, Any], repair_row: Mapping[str, Any] | None = None) -> str:
    primary_lane = str((repair_row or {}).get("primary_repair_lane") or "")
    if primary_lane in IMPLEMENTATION_LANE_BY_PRIMARY_REPAIR_LANE:
        return IMPLEMENTATION_LANE_BY_PRIMARY_REPAIR_LANE[primary_lane]
    stop_layer = str(row.get("stop_layer") or "manual_review")
    return IMPLEMENTATION_LANE_BY_STOP_LAYER.get(stop_layer, "04_manual_gap_classification")


def _next_patch_statement(lane: str, row: Mapping[str, Any], field_row: Mapping[str, Any]) -> str:
    archetype = row.get("canonical_archetype_id")
    missing_axes = list(row.get("missing_required_bridge_axes") or ())
    missing_primitives = list(field_row.get("missing_feature_parser_contract_primitives") or ())
    if lane == "01_fixture_archive_and_candidate_funnel":
        return f"{archetype} Green/guard fixture를 official universe, price history, report/search snapshot에 exact as-of로 넣고 current replay 후보에 도달시키는 패치."
    if lane == "02_parser_feature_bridge_contract":
        return f"{archetype}의 missing axes {missing_axes or ['none']}와 missing primitives {missing_primitives or ['none']}를 parser output -> feature field -> gate diagnostic으로 연결하는 패치."
    if lane == "03_weighted_gate_validation_after_fields":
        return f"{archetype}의 positive/guard pair에서 field가 채워진 뒤 weighted total/component gate 부족분을 재검증하는 패치."
    return f"{archetype}를 candidate/archive, parser-feature, stage-gate 중 하나의 lane으로 재분류하는 audit 패치."


def build_v12_runtime_repair_execution_backlog(
    *,
    execution_path_payload: Mapping[str, Any] | None = None,
    repair_board_payload: Mapping[str, Any] | None = None,
    field_audit_payload: Mapping[str, Any] | None = None,
    replay_spec_payload: Mapping[str, Any] | None = None,
    readiness_payload: Mapping[str, Any] | None = None,
    funnel_audit_payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a concrete repair backlog from the current runtime audits."""

    execution_payload = dict(execution_path_payload or _read_json(DEFAULT_EXECUTION_PATH_PATH))
    repair_payload = dict(repair_board_payload or _read_json(DEFAULT_REPAIR_BOARD_PATH))
    field_payload = dict(field_audit_payload or _read_json(DEFAULT_FIELD_AUDIT_PATH))
    replay_payload = dict(replay_spec_payload or _read_json(DEFAULT_REPLAY_SPEC_PATH))
    readiness_payload_dict = dict(readiness_payload or _read_json(DEFAULT_READINESS_PATH))
    funnel_payload = dict(funnel_audit_payload or _read_json(DEFAULT_FUNNEL_AUDIT_PATH))

    execution_rows = _rows_by_archetype(execution_payload, "archetype_rows")
    repair_rows = _rows_by_archetype(repair_payload)
    field_rows = _rows_by_archetype(field_payload)
    replay_rows = _rows_grouped_by_archetype(replay_payload)
    readiness_rows = _rows_grouped_by_archetype(readiness_payload_dict)
    pair_readiness_rows = _rows_by_archetype(readiness_payload_dict, "archetype_pair_rows")
    funnel_rows = _rows_grouped_by_archetype(funnel_payload)
    archetypes = sorted(set(execution_rows) | set(repair_rows) | set(field_rows))

    rows: list[dict[str, Any]] = []
    lane_counts: Counter[str] = Counter()
    stop_layer_counts: Counter[str] = Counter()
    current_candidate_counts: Counter[str] = Counter()
    primitive_gap_counter: Counter[str] = Counter()
    missing_axis_counter: Counter[str] = Counter()
    for archetype in archetypes:
        exec_row = execution_rows.get(archetype, {})
        repair_row = repair_rows.get(archetype, {})
        field_row = field_rows.get(archetype, {})
        lane = _implementation_lane(exec_row, repair_row)
        stop_layer = STOP_LAYER_BY_IMPLEMENTATION_LANE.get(lane, str(exec_row.get("stop_layer") or "manual_review"))
        lane_counts[lane] += 1
        stop_layer_counts[stop_layer] += 1
        runtime_candidate_count = int(exec_row.get("runtime_candidate_count") or repair_row.get("runtime_candidate_count") or 0)
        if runtime_candidate_count > 0:
            current_candidate_counts["has_current_candidates"] += 1
        else:
            current_candidate_counts["no_current_candidates"] += 1
        for primitive in field_row.get("missing_feature_parser_contract_primitives") or ():
            primitive_gap_counter[str(primitive)] += 1
        missing_axes = list(
            repair_row.get("missing_required_bridge_axes")
            if "missing_required_bridge_axes" in repair_row
            else exec_row.get("missing_required_bridge_axes") or ()
        )
        for axis in missing_axes:
            missing_axis_counter[str(axis)] += 1
        pair_row = pair_readiness_rows.get(archetype, {})
        row = {
            "canonical_archetype_id": archetype,
            "implementation_lane": lane,
            "stop_layer": stop_layer,
            "primary_repair_lane": repair_row.get("primary_repair_lane"),
            "priority_score": repair_row.get("priority_score"),
            "weight_support_row_count": exec_row.get("weight_support_row_count"),
            "runtime_candidate_count": runtime_candidate_count,
            "runtime_max_score": repair_row.get("runtime_max_score")
            if "runtime_max_score" in repair_row
            else exec_row.get("runtime_max_score"),
            "missing_required_bridge_axes": missing_axes,
            "missing_feature_parser_contract_primitives": list(
                field_row.get("missing_feature_parser_contract_primitives") or ()
            ),
            "axis_contract_status_counts": _axis_status_counts(field_row),
            "fixture_summary": _fixture_summary(replay_rows.get(archetype, [])),
            "readiness_summary": _readiness_summary(readiness_rows.get(archetype, [])),
            "funnel_summary": _funnel_summary(funnel_rows.get(archetype, [])),
            "pair_retrospective_ready": bool(pair_row.get("pair_retrospective_ready")),
            "pair_strict_pit_ready": bool(pair_row.get("pair_strict_pit_ready")),
            "code_files_to_touch": list(CODE_FILES_BY_IMPLEMENTATION_LANE[lane]),
            "tests_to_add_or_extend": list(TESTS_BY_IMPLEMENTATION_LANE[lane]),
            "next_patch": _next_patch_statement(
                lane,
                {"canonical_archetype_id": archetype, "missing_required_bridge_axes": missing_axes},
                field_row,
            ),
            "do_not_do": DO_NOT_DO_BY_IMPLEMENTATION_LANE[lane],
        }
        rows.append(row)

    rows.sort(
        key=lambda row: (
            row["implementation_lane"],
            -(float(row.get("priority_score") or 0.0)),
            -(int(row.get("weight_support_row_count") or 0)),
            str(row["canonical_archetype_id"]),
        )
    )
    return {
        "schema_version": "v12_runtime_repair_execution_backlog_v1",
        "summary": {
            "archetype_count": len(rows),
            "implementation_lane_counts": _counter_dict(lane_counts),
            "stop_layer_counts": _counter_dict(stop_layer_counts),
            "current_candidate_counts": _counter_dict(current_candidate_counts),
            "pair_retrospective_ready_count": sum(1 for row in rows if row["pair_retrospective_ready"]),
            "pair_strict_pit_ready_count": sum(1 for row in rows if row["pair_strict_pit_ready"]),
            "missing_required_axis_counts": _counter_dict(missing_axis_counter),
            "top_missing_required_axes": [
                {"axis": axis, "count": count} for axis, count in missing_axis_counter.most_common(20)
            ],
            "top_missing_feature_parser_primitives": [
                {"primitive": primitive, "count": count} for primitive, count in primitive_gap_counter.most_common(20)
            ],
            "next_order": [
                "01_fixture_archive_and_candidate_funnel",
                "02_parser_feature_bridge_contract",
                "03_weighted_gate_validation_after_fields",
                "04_manual_gap_classification",
            ],
            "plain_conclusion": (
                "다음 구현은 HBM 점수 보너스가 아니라 fixture archive/candidate funnel, "
                "parser-feature bridge, weighted gate validation 순서로 진행해야 한다."
            ),
        },
        "rows": rows,
    }


def render_v12_runtime_repair_execution_backlog(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Runtime Repair Execution Backlog",
        "",
        "이 문서는 다음 구현 순서를 고정한다. 목적은 HBM 과적합이 아니라, 전체 아키타입에서 Green 연구가 runtime 점수로 넘어가는 길을 복구하는 것이다.",
        "",
        "## Summary",
        "",
        f"- plain_conclusion: {summary.get('plain_conclusion')}",
        f"- archetype_count: `{summary.get('archetype_count')}`",
        f"- implementation_lane_counts: `{summary.get('implementation_lane_counts')}`",
        f"- stop_layer_counts: `{summary.get('stop_layer_counts')}`",
        f"- current_candidate_counts: `{summary.get('current_candidate_counts')}`",
        f"- pair_retrospective_ready_count: `{summary.get('pair_retrospective_ready_count')}`",
        f"- pair_strict_pit_ready_count: `{summary.get('pair_strict_pit_ready_count')}`",
        f"- missing_required_axis_counts: `{summary.get('missing_required_axis_counts')}`",
        f"- top_missing_required_axes: `{summary.get('top_missing_required_axes')}`",
        f"- top_missing_feature_parser_primitives: `{summary.get('top_missing_feature_parser_primitives')}`",
        f"- next_order: `{summary.get('next_order')}`",
        "",
        "## Implementation Lanes",
        "",
        "| order | lane | meaning | touch files | tests | do not do |",
        "| ---: | --- | --- | --- | --- | --- |",
        "| 1 | 01_fixture_archive_and_candidate_funnel | 연구 Green/guard가 exact as-of 후보로 재현되게 만든다. | "
        + "<br>".join(CODE_FILES_BY_IMPLEMENTATION_LANE["01_fixture_archive_and_candidate_funnel"])
        + " | "
        + "<br>".join(TESTS_BY_IMPLEMENTATION_LANE["01_fixture_archive_and_candidate_funnel"])
        + f" | {DO_NOT_DO_BY_IMPLEMENTATION_LANE['01_fixture_archive_and_candidate_funnel']} |",
        "| 2 | 02_parser_feature_bridge_contract | source-backed primitive를 feature field와 gate axis로 연결한다. | "
        + "<br>".join(CODE_FILES_BY_IMPLEMENTATION_LANE["02_parser_feature_bridge_contract"])
        + " | "
        + "<br>".join(TESTS_BY_IMPLEMENTATION_LANE["02_parser_feature_bridge_contract"])
        + f" | {DO_NOT_DO_BY_IMPLEMENTATION_LANE['02_parser_feature_bridge_contract']} |",
        "| 3 | 03_weighted_gate_validation_after_fields | field가 채워진 뒤 weighted Green gate가 맞는지 검증한다. | "
        + "<br>".join(CODE_FILES_BY_IMPLEMENTATION_LANE["03_weighted_gate_validation_after_fields"])
        + " | "
        + "<br>".join(TESTS_BY_IMPLEMENTATION_LANE["03_weighted_gate_validation_after_fields"])
        + f" | {DO_NOT_DO_BY_IMPLEMENTATION_LANE['03_weighted_gate_validation_after_fields']} |",
        "| 4 | 04_manual_gap_classification | 아직 lane이 불명확한 row를 다시 분류한다. | "
        + "<br>".join(CODE_FILES_BY_IMPLEMENTATION_LANE["04_manual_gap_classification"])
        + " | "
        + "<br>".join(TESTS_BY_IMPLEMENTATION_LANE["04_manual_gap_classification"])
        + f" | {DO_NOT_DO_BY_IMPLEMENTATION_LANE['04_manual_gap_classification']} |",
        "",
        "## Priority Rows",
        "",
        "| archetype | lane | priority | candidates | max score | missing axes | missing primitives | fixture/readiness/funnel | next patch |",
        "| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |",
    ]
    for row in rows:
        readiness = row.get("readiness_summary") or {}
        funnel = row.get("funnel_summary") or {}
        fixture = row.get("fixture_summary") or {}
        lines.append(
            f"| {row.get('canonical_archetype_id')} | {row.get('implementation_lane')} | "
            f"{row.get('priority_score')} | {row.get('runtime_candidate_count')} | {row.get('runtime_max_score')} | "
            f"{', '.join(row.get('missing_required_bridge_axes') or []) or 'none'} | "
            f"{', '.join(row.get('missing_feature_parser_contract_primitives') or []) or 'none'} | "
            f"fixture={fixture.get('row_count')} rows; readiness={readiness.get('retrospective_status_counts')}; funnel={funnel.get('fixture_funnel_status_counts')} | "
            f"{row.get('next_patch')} |"
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 먼저 시험지를 실제로 준비해야 한다. 이것이 fixture/archive와 candidate funnel이다.",
            "- 그다음 답안지 칸을 채워야 한다. 이것이 parser-feature bridge다.",
            "- 마지막으로 채점 기준이 맞는지 본다. 이것이 weighted gate validation이다.",
            "- 쉬운 예: 시험 문제지도 없는데 채점 기준을 낮추면 안 된다. 문제지와 답안지를 준비한 뒤에야 채점 기준을 조정할 수 있다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_runtime_repair_execution_backlog(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_runtime_repair_execution_backlog()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_runtime_repair_execution_backlog(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_runtime_repair_execution_backlog()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
