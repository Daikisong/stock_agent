"""Build a repair priority board from v12 runtime gap audits."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Mapping
import json


DEFAULT_SIGNAL_AUDIT_PATH = Path("docs/0619/v12_archetype_signal_runtime_translation_audit_2026-06-19.json")
DEFAULT_FIELD_AUDIT_PATH = Path("docs/0619/v12_bridge_spec_runtime_field_audit_2026-06-19.json")
DEFAULT_READINESS_PATH = Path("docs/0619/v12_exact_fixture_replay_readiness_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_runtime_repair_priority_board_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_runtime_repair_priority_board_2026-06-19.md")


LANE_LABELS: dict[str, str] = {
    "candidate_funnel_or_benchmark_replay": "research Green fixture가 current runtime 후보로 안 들어옴",
    "exact_fixture_archive": "Green/guard exact replay 입력 아카이브가 부족함",
    "runtime_input_evidence_coverage": "후보 row는 있지만 bridge 판정에 필요한 원천 입력 가족이 부족함",
    "parser_feature_field_contract": "bridge primitive가 parser/feature field contract에 없음",
    "gate_bridge_axis_alignment": "bridge spec과 Green gate required axis가 서로 안 맞음",
    "runtime_field_strength": "bridge spec 축은 있지만 runtime row에서 field가 0이거나 약함",
    "weighted_gate_threshold_or_component_balance": "field는 있는데 weighted Stage3 gate에서 막힘",
    "source_backed_fixture_cleaning": "연구 Green이 source-backed fixture로 깨끗하지 않음",
}


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _rows_by_archetype(payload: Mapping[str, Any], key: str = "rows") -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): dict(row) for row in payload.get(key, [])}


def _readiness_by_archetype(payload: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return _rows_by_archetype(payload, "archetype_pair_rows")


def _axis_status_counts(row: Mapping[str, Any]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for item in row.get("axis_contract_statuses", ()) or ():
        counter[str(item.get("status") or "")] += 1
    return counter


def _repair_lanes(
    *,
    signal_row: Mapping[str, Any],
    field_row: Mapping[str, Any],
    readiness_row: Mapping[str, Any],
) -> list[str]:
    lanes: list[str] = []
    runtime_gap_status = str(signal_row.get("runtime_gap_status") or field_row.get("runtime_gap_status") or "")
    axis_counts = _axis_status_counts(field_row)
    missing_contract_count = int(field_row.get("missing_feature_parser_contract_count") or 0)
    pair_ready = bool(readiness_row.get("pair_retrospective_ready"))

    if runtime_gap_status == "not_in_current_benchmark":
        lanes.append("candidate_funnel_or_benchmark_replay")
    if runtime_gap_status == "runtime_input_evidence_missing":
        lanes.append("runtime_input_evidence_coverage")
    if runtime_gap_status == "fixture_not_ready":
        lanes.append("source_backed_fixture_cleaning")
    if not pair_ready:
        lanes.append("exact_fixture_archive")
    if missing_contract_count > 0:
        lanes.append("parser_feature_field_contract")
    if axis_counts["required_by_gate_but_absent_from_bridge_spec"] > 0:
        lanes.append("gate_bridge_axis_alignment")
    if axis_counts["bridge_spec_axis_present_but_runtime_field_missing_or_too_weak"] > 0:
        lanes.append("runtime_field_strength")
    if runtime_gap_status == "runtime_stage3_gate_blocked":
        lanes.append("weighted_gate_threshold_or_component_balance")
    return list(dict.fromkeys(lanes))


def _primary_lane(lanes: list[str], runtime_gap_status: str) -> str:
    if runtime_gap_status == "not_in_current_benchmark":
        return "candidate_funnel_or_benchmark_replay"
    if runtime_gap_status == "runtime_input_evidence_missing":
        return "runtime_input_evidence_coverage"
    if runtime_gap_status == "fixture_not_ready":
        return "source_backed_fixture_cleaning"
    if runtime_gap_status == "runtime_stage3_gate_blocked":
        return "weighted_gate_threshold_or_component_balance"
    for lane in (
        "parser_feature_field_contract",
        "gate_bridge_axis_alignment",
        "runtime_field_strength",
        "exact_fixture_archive",
    ):
        if lane in lanes:
            return lane
    return lanes[0] if lanes else "manual_review"


def _priority_score(
    *,
    signal_row: Mapping[str, Any],
    field_row: Mapping[str, Any],
    readiness_row: Mapping[str, Any],
) -> float:
    clean_green = float(signal_row.get("research_clean_green_count") or field_row.get("research_clean_green_count") or 0)
    raw_green = float(signal_row.get("research_raw_stage3_green_count") or field_row.get("research_raw_stage3_green_count") or 0)
    missing_contract_count = float(field_row.get("missing_feature_parser_contract_count") or 0)
    axis_counts = _axis_status_counts(field_row)
    runtime_gap_status = str(signal_row.get("runtime_gap_status") or field_row.get("runtime_gap_status") or "")
    runtime_candidate_count = float(signal_row.get("runtime_candidate_count") or field_row.get("runtime_candidate_count") or 0)
    runtime_max_score = float(signal_row.get("runtime_max_score") or field_row.get("runtime_max_score") or 0)
    pair_ready = bool(readiness_row.get("pair_retrospective_ready"))
    green_ready = bool(readiness_row.get("green_retrospective_ready"))
    guard_ready = bool(readiness_row.get("guard_retrospective_ready"))

    status_bonus = {
        "runtime_bridge_axes_missing": 18.0,
        "runtime_input_evidence_missing": 12.0,
        "runtime_stage3_gate_blocked": 14.0,
        "not_in_current_benchmark": 10.0,
        "fixture_not_ready": 8.0,
    }.get(runtime_gap_status, 2.0)
    near_runtime_bonus = 8.0 if runtime_candidate_count > 0 and runtime_max_score >= 60.0 else 0.0
    fixture_gap_bonus = 5.0 if not pair_ready else 0.0
    asymmetric_fixture_bonus = 4.0 if green_ready and not guard_ready else 0.0

    score = (
        clean_green * 2.0
        + raw_green * 0.4
        + min(missing_contract_count * 2.0, 12.0)
        + axis_counts["required_by_gate_but_absent_from_bridge_spec"] * 4.0
        + axis_counts["bridge_spec_axis_present_but_runtime_field_missing_or_too_weak"] * 2.0
        + status_bonus
        + near_runtime_bonus
        + fixture_gap_bonus
        + asymmetric_fixture_bonus
    )
    return round(score, 4)


def _why_now(signal_row: Mapping[str, Any], field_row: Mapping[str, Any]) -> str:
    runtime_gap_status = str(signal_row.get("runtime_gap_status") or field_row.get("runtime_gap_status") or "")
    missing_axes = list(signal_row.get("missing_required_bridge_axes") or field_row.get("missing_required_bridge_axes") or ())
    missing_contract_count = int(field_row.get("missing_feature_parser_contract_count") or 0)
    axis_counts = _axis_status_counts(field_row)
    if runtime_gap_status == "not_in_current_benchmark":
        return "Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다."
    if runtime_gap_status == "runtime_input_evidence_missing":
        return "후보 row는 있지만 리포트/뉴스/컨센서스/충분한 공시+재무 입력이 부족해 bridge 변환 실패인지 아직 판정할 수 없다."
    if runtime_gap_status == "runtime_bridge_axes_missing":
        if axis_counts["required_by_gate_but_absent_from_bridge_spec"] > 0:
            return "후보는 들어왔지만 bridge spec과 Green gate required axis가 달라 일부 축이 0점으로 남는다."
        return "후보는 들어왔지만 연구축이 source-backed runtime field로 충분히 구조화되지 않았다."
    if missing_contract_count > 0:
        return "bridge spec primitive 이름이 현재 parser/feature field contract와 맞지 않는다."
    if runtime_gap_status == "runtime_stage3_gate_blocked":
        return "field는 들어왔지만 weighted Stage3-Green total/component gate를 넘지 못했다."
    if runtime_gap_status == "fixture_not_ready":
        return "연구 Green이 source-backed exact replay fixture로 쓰기에는 아직 깨끗하지 않다."
    if missing_axes:
        return f"required axis {', '.join(str(axis) for axis in missing_axes)}가 runtime에서 비어 있거나 약하다."
    return "자동 분류만으로는 충분하지 않아 수동 점검이 필요하다."


def build_v12_runtime_repair_priority_board(
    *,
    signal_audit_payload: Mapping[str, Any] | None = None,
    field_audit_payload: Mapping[str, Any] | None = None,
    readiness_payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build an implementation priority board from accumulated audit outputs."""

    signal_payload = dict(signal_audit_payload or _read_json(DEFAULT_SIGNAL_AUDIT_PATH))
    field_payload = dict(field_audit_payload or _read_json(DEFAULT_FIELD_AUDIT_PATH))
    replay_payload = dict(readiness_payload or _read_json(DEFAULT_READINESS_PATH))
    signal_by_arch = _rows_by_archetype(signal_payload)
    field_by_arch = _rows_by_archetype(field_payload)
    readiness_by_arch = _readiness_by_archetype(replay_payload)
    archetypes = sorted(set(signal_by_arch) | set(field_by_arch) | set(readiness_by_arch))

    rows: list[dict[str, Any]] = []
    lane_counts: Counter[str] = Counter()
    primary_lane_counts: Counter[str] = Counter()
    for archetype in archetypes:
        signal_row = signal_by_arch.get(archetype, {})
        field_row = field_by_arch.get(archetype, {})
        readiness_row = readiness_by_arch.get(archetype, {})
        lanes = _repair_lanes(signal_row=signal_row, field_row=field_row, readiness_row=readiness_row)
        runtime_gap_status = str(signal_row.get("runtime_gap_status") or field_row.get("runtime_gap_status") or "")
        primary = _primary_lane(lanes, runtime_gap_status)
        for lane in lanes:
            lane_counts[lane] += 1
        primary_lane_counts[primary] += 1
        score = _priority_score(signal_row=signal_row, field_row=field_row, readiness_row=readiness_row)
        axis_counts = _axis_status_counts(field_row)
        row = {
            "canonical_archetype_id": archetype,
            "priority_score": score,
            "primary_repair_lane": primary,
            "repair_lanes": lanes,
            "runtime_gap_status": runtime_gap_status,
            "diagnosis": signal_row.get("diagnosis") or field_row.get("diagnosis"),
            "why_low_now": _why_now(signal_row, field_row),
            "research_clean_green_count": signal_row.get("research_clean_green_count")
            if signal_row
            else field_row.get("research_clean_green_count"),
            "research_raw_stage3_green_count": signal_row.get("research_raw_stage3_green_count")
            if signal_row
            else field_row.get("research_raw_stage3_green_count"),
            "runtime_candidate_count": signal_row.get("runtime_candidate_count") or field_row.get("runtime_candidate_count"),
            "runtime_max_score": signal_row.get("runtime_max_score") or field_row.get("runtime_max_score"),
            "missing_required_bridge_axes": list(
                signal_row.get("missing_required_bridge_axes") or field_row.get("missing_required_bridge_axes") or ()
            ),
            "missing_feature_parser_contract_count": int(field_row.get("missing_feature_parser_contract_count") or 0),
            "missing_feature_parser_contract_primitives": list(
                field_row.get("missing_feature_parser_contract_primitives") or ()
            ),
            "axis_contract_status_counts": _counter_dict(axis_counts),
            "green_retrospective_ready": bool(readiness_row.get("green_retrospective_ready")),
            "guard_retrospective_ready": bool(readiness_row.get("guard_retrospective_ready")),
            "pair_retrospective_ready": bool(readiness_row.get("pair_retrospective_ready")),
            "green_strict_pit_ready": bool(readiness_row.get("green_strict_pit_ready")),
            "guard_strict_pit_ready": bool(readiness_row.get("guard_strict_pit_ready")),
            "pair_strict_pit_ready": bool(readiness_row.get("pair_strict_pit_ready")),
        }
        rows.append(row)

    rows.sort(
        key=lambda row: (
            float(row["priority_score"]),
            float(row.get("research_clean_green_count") or 0),
            float(row.get("research_raw_stage3_green_count") or 0),
            str(row["canonical_archetype_id"]),
        ),
        reverse=True,
    )
    return {
        "summary": {
            "archetype_count": len(rows),
            "repair_lane_counts": _counter_dict(lane_counts),
            "primary_repair_lane_counts": _counter_dict(primary_lane_counts),
            "top_priority_archetypes": [
                {
                    "canonical_archetype_id": row["canonical_archetype_id"],
                    "priority_score": row["priority_score"],
                    "primary_repair_lane": row["primary_repair_lane"],
                }
                for row in rows[:10]
            ],
            "pair_retrospective_ready_count": sum(1 for row in rows if row["pair_retrospective_ready"]),
            "pair_strict_pit_ready_count": sum(1 for row in rows if row["pair_strict_pit_ready"]),
        },
        "lane_labels": LANE_LABELS,
        "rows": rows,
    }


def render_v12_runtime_repair_priority_board(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Runtime Repair Priority Board",
        "",
        "이 문서는 누적 연구 Green이 runtime 점수로 내려오지 못하는 원인을 작업 순서로 바꾼 보드다.",
        "HBM만 올리는 패치가 아니라, 후보 funnel, exact replay archive, parser/feature field contract, Green gate axis 정렬을 나눠 본다.",
        "",
        "## Summary",
        "",
        f"- archetype_count: `{summary.get('archetype_count')}`",
        f"- repair_lane_counts: `{summary.get('repair_lane_counts')}`",
        f"- primary_repair_lane_counts: `{summary.get('primary_repair_lane_counts')}`",
        f"- pair_retrospective_ready_count: `{summary.get('pair_retrospective_ready_count')}`",
        f"- pair_strict_pit_ready_count: `{summary.get('pair_strict_pit_ready_count')}`",
        f"- top_priority_archetypes: `{summary.get('top_priority_archetypes')}`",
        "",
        "## Lane Meaning",
        "",
    ]
    for lane, label in payload.get("lane_labels", {}).items():
        lines.append(f"- `{lane}`: {label}")
    lines.extend(
        [
            "",
            "## Priority Matrix",
            "",
            "| rank | archetype | score | primary lane | Green clean/raw | runtime | missing axes | missing field contract | why low now |",
            "| ---: | --- | ---: | --- | ---: | --- | --- | ---: | --- |",
        ]
    )
    for idx, row in enumerate(rows, start=1):
        missing_primitives = row.get("missing_feature_parser_contract_primitives", [])
        missing_preview = ", ".join(missing_primitives[:3])
        if len(missing_primitives) > 3:
            missing_preview += " ..."
        lines.append(
            f"| {idx} | {row.get('canonical_archetype_id')} | {row.get('priority_score')} | "
            f"{row.get('primary_repair_lane')} | "
            f"{row.get('research_clean_green_count')}/{row.get('research_raw_stage3_green_count')} | "
            f"{row.get('runtime_gap_status')} candidates={row.get('runtime_candidate_count')} max={row.get('runtime_max_score')} | "
            f"{', '.join(row.get('missing_required_bridge_axes') or []) or 'none'} | "
            f"{row.get('missing_feature_parser_contract_count')} {missing_preview} | "
            f"{row.get('why_low_now')} |"
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- C06 하닉형 문제: 후보와 bridge field는 들어왔지만 Green total/bottleneck gate 검증이 남아 있다.",
            "- C10 삼성형 문제: 후보와 리포트는 들어왔지만 customer/backlog/contract bridge field가 아직 약하다.",
            "- C01/C19/R13 입력형 문제: 후보 row는 있지만 bridge를 판정할 리포트/뉴스/컨센서스/충분한 공시+재무 입력 가족이 부족하다.",
            "- C21 금융형 문제: Green 연구는 많지만 current benchmark 후보가 없어 점수식 자체를 시험하지 못했다.",
            "- C26 플랫폼형 문제: bridge spec primitive 이름이 parser/feature field contract와 아직 연결되지 않았다.",
            "- 쉬운 예: 재료 창고에는 좋은 사과가 있는데, 계산대 목록에는 `사과`가 아니라 `과일A`로 적혀 있거나, 계산대까지 물건이 올라오지 않은 상태다. 가격표만 바꿔서는 해결되지 않는다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_runtime_repair_priority_board(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_runtime_repair_priority_board()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_runtime_repair_priority_board(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_runtime_repair_priority_board()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
