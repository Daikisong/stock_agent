"""Input gap manifest for the first V12 runtime repair slice."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping
import json


DEFAULT_FIRST_SLICE_PATH = Path("docs/0619/v12_runtime_first_repair_slice_2026-06-19.json")
DEFAULT_READINESS_PATH = Path("docs/0619/v12_exact_fixture_replay_readiness_2026-06-19.json")
DEFAULT_FUNNEL_PATH = Path("docs/0619/v12_fixture_candidate_funnel_audit_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_runtime_first_repair_input_gap_manifest_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_runtime_first_repair_input_gap_manifest_2026-06-19.md")


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _rows_grouped_by_archetype(payload: Mapping[str, Any], key: str = "rows") -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in payload.get(key, []) or []:
        grouped[str(row.get("canonical_archetype_id"))].append(dict(row))
    return dict(grouped)


def _funnel_by_role_symbol_date(payload: Mapping[str, Any]) -> dict[tuple[str, str, str, str], dict[str, Any]]:
    index: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    for row in payload.get("rows", []) or []:
        candidate = row.get("candidate") or {}
        key = (
            str(row.get("canonical_archetype_id") or ""),
            str(row.get("role") or ""),
            str(candidate.get("symbol") or ""),
            str(candidate.get("as_of_date") or ""),
        )
        index[key] = dict(row)
    return index


def _gap_class(readiness_row: Mapping[str, Any], funnel_row: Mapping[str, Any]) -> str:
    retro_status = str(readiness_row.get("retrospective_readiness_status") or "")
    strict_status = str(readiness_row.get("strict_pit_readiness_status") or "")
    funnel_status = str(funnel_row.get("fixture_funnel_status") or "")
    if funnel_status == "exact_symbol_date_candidate_reached_runtime":
        if retro_status == "ready_retrospective_exact_replay" and strict_status == "ready_strict_pit_exact_replay":
            return "exact_replay_ready"
        if "missing_research_snapshot_inputs" in {retro_status, strict_status}:
            return "exact_candidate_reached_but_research_snapshot_missing"
        return "exact_candidate_reached_but_readiness_inputs_missing"
    if retro_status == "ready_retrospective_exact_replay" and strict_status == "ready_strict_pit_exact_replay":
        return "exact_replay_ready"
    if retro_status == "ready_retrospective_exact_replay" and strict_status == "missing_research_snapshot_inputs":
        return "strict_pit_research_snapshot_missing"
    if funnel_status == "symbol_reached_runtime_but_not_fixture_date":
        return "runtime_symbol_reached_but_schedule_date_mismatch"
    if funnel_status == "symbol_never_reached_current_runtime":
        return "archive_or_candidate_funnel_missing"
    if retro_status == "missing_official_and_research_inputs":
        return "official_price_research_archive_missing"
    return "unclassified_input_gap"


def _candidate_key(row: Mapping[str, Any]) -> tuple[str, str, str, str]:
    candidate = row.get("candidate") or {}
    return (
        str(row.get("canonical_archetype_id") or ""),
        str(row.get("role") or ""),
        str(candidate.get("symbol") or ""),
        str(candidate.get("as_of_date") or ""),
    )


def _role_gap_row(readiness_row: Mapping[str, Any], funnel_row: Mapping[str, Any]) -> dict[str, Any]:
    candidate = dict(readiness_row.get("candidate") or funnel_row.get("candidate") or {})
    return {
        "role": readiness_row.get("role") or funnel_row.get("role"),
        "symbol": candidate.get("symbol"),
        "as_of_date": candidate.get("as_of_date"),
        "case_id": candidate.get("case_id"),
        "trigger_type": candidate.get("trigger_type"),
        "retrospective_readiness_status": readiness_row.get("retrospective_readiness_status"),
        "strict_pit_readiness_status": readiness_row.get("strict_pit_readiness_status"),
        "retrospective_missing_inputs": list(readiness_row.get("retrospective_missing_inputs") or ()),
        "strict_pit_missing_inputs": list(readiness_row.get("strict_pit_missing_inputs") or ()),
        "fixture_funnel_status": funnel_row.get("fixture_funnel_status"),
        "funnel_root_cause": funnel_row.get("funnel_root_cause"),
        "runtime_symbol_candidate_count": funnel_row.get("runtime_symbol_candidate_count"),
        "runtime_symbol_dates": list(funnel_row.get("runtime_symbol_dates") or ()),
        "nearest_runtime_candidates": list(funnel_row.get("nearest_runtime_candidates") or ())[:3],
        "input_gap_class": _gap_class(readiness_row, funnel_row),
    }


def _archetype_action(gap_classes: set[str], lane: str) -> str:
    if not gap_classes:
        return "선택된 manual row라 fixture 후보를 먼저 지정하고 lane을 재분류한다."
    if "archive_or_candidate_funnel_missing" in gap_classes:
        return "official universe, price history, report/search snapshot을 채우고 exact symbol+date 후보가 current replay에 도달하게 한다."
    if "runtime_symbol_reached_but_schedule_date_mismatch" in gap_classes:
        return "월초 replay 날짜와 fixture as_of_date 차이를 처리하는 exact fixture replay 경로를 추가한다."
    if "exact_candidate_reached_but_research_snapshot_missing" in gap_classes:
        return "exact fixture 날짜 후보는 도달했으므로 evidence source search/report snapshot을 보강한다."
    if "exact_candidate_reached_but_readiness_inputs_missing" in gap_classes:
        return "exact fixture 날짜 후보는 도달했으므로 readiness가 요구하는 official/price/research 입력을 채운다."
    if "strict_pit_research_snapshot_missing" in gap_classes:
        return "retrospective replay는 가능하므로 strict PIT search/report snapshot 증거를 보강한다."
    if "exact_replay_ready" in gap_classes and lane == "03_weighted_gate_validation_after_fields":
        return "입력은 있으므로 weighted gate/component deficit을 positive/guard 쌍으로 검증한다."
    return "입력 결손을 보강한 뒤 parser-feature 또는 gate acceptance test를 실행한다."


def build_v12_runtime_first_repair_input_gap_manifest(
    *,
    first_slice_payload: Mapping[str, Any] | None = None,
    readiness_payload: Mapping[str, Any] | None = None,
    funnel_payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build selected first-slice row input gaps from readiness and funnel audits."""

    first_slice = dict(first_slice_payload or _read_json(DEFAULT_FIRST_SLICE_PATH))
    readiness = dict(readiness_payload or _read_json(DEFAULT_READINESS_PATH))
    funnel = dict(funnel_payload or _read_json(DEFAULT_FUNNEL_PATH))
    readiness_by_arch = _rows_grouped_by_archetype(readiness)
    funnel_index = _funnel_by_role_symbol_date(funnel)
    selected_rows = list(first_slice.get("rows", []))
    hbm_or_samsung_related = {
        "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    }

    rows: list[dict[str, Any]] = []
    lane_counts: Counter[str] = Counter()
    role_gap_counts: Counter[str] = Counter()
    retro_status_counts: Counter[str] = Counter()
    strict_status_counts: Counter[str] = Counter()
    funnel_status_counts: Counter[str] = Counter()
    missing_input_counts: Counter[str] = Counter()
    for selected in selected_rows:
        archetype = str(selected.get("canonical_archetype_id") or "")
        lane = str(selected.get("implementation_lane") or "")
        role_rows: list[dict[str, Any]] = []
        for readiness_row in readiness_by_arch.get(archetype, []):
            funnel_row = funnel_index.get(_candidate_key(readiness_row), {})
            role_gap = _role_gap_row(readiness_row, funnel_row)
            role_rows.append(role_gap)
            role_gap_counts[str(role_gap["input_gap_class"])] += 1
            retro_status_counts[str(role_gap.get("retrospective_readiness_status") or "missing_fixture_row")] += 1
            strict_status_counts[str(role_gap.get("strict_pit_readiness_status") or "missing_fixture_row")] += 1
            funnel_status_counts[str(role_gap.get("fixture_funnel_status") or "missing_funnel_row")] += 1
            for item in role_gap.get("retrospective_missing_inputs") or ():
                missing_input_counts[f"retrospective:{item}"] += 1
            for item in role_gap.get("strict_pit_missing_inputs") or ():
                missing_input_counts[f"strict:{item}"] += 1
        if not role_rows:
            role_gap_counts["selected_manual_row_without_fixture_spec"] += 1
        gap_classes = {str(row.get("input_gap_class")) for row in role_rows}
        lane_counts[lane] += 1
        rows.append(
            {
                "canonical_archetype_id": archetype,
                "implementation_lane": lane,
                "selection_reason": selected.get("selection_reason"),
                "acceptance_status_current": selected.get("acceptance_status_current"),
                "runtime_candidate_count": selected.get("runtime_candidate_count"),
                "runtime_max_score": selected.get("runtime_max_score"),
                "missing_required_bridge_axes": list(selected.get("missing_required_bridge_axes") or ()),
                "missing_feature_parser_contract_primitives": list(
                    selected.get("missing_feature_parser_contract_primitives") or ()
                ),
                "role_gap_rows": role_rows,
                "role_gap_classes": sorted(gap_classes) if gap_classes else ["selected_manual_row_without_fixture_spec"],
                "next_input_action": _archetype_action(gap_classes, lane),
                "acceptance_tests_to_add": list(selected.get("acceptance_tests_to_add") or ()),
            }
        )

    return {
        "schema_version": "v12_runtime_first_repair_input_gap_manifest_v1",
        "summary": {
            "selected_archetype_count": len(rows),
            "selected_fixture_role_row_count": sum(len(row["role_gap_rows"]) for row in rows),
            "selected_lane_counts": _counter_dict(lane_counts),
            "selected_hbm_or_samsung_related_count": sum(
                1 for row in rows if row["canonical_archetype_id"] in hbm_or_samsung_related
            ),
            "selected_non_hbm_count": sum(
                1 for row in rows if row["canonical_archetype_id"] not in hbm_or_samsung_related
            ),
            "role_gap_class_counts": _counter_dict(role_gap_counts),
            "retrospective_readiness_status_counts": _counter_dict(retro_status_counts),
            "strict_pit_readiness_status_counts": _counter_dict(strict_status_counts),
            "fixture_funnel_status_counts": _counter_dict(funnel_status_counts),
            "missing_input_counts": _counter_dict(missing_input_counts),
            "generalization_guard": (
                "삼전/하닉은 전체 아키타입 runtime 번역 결손을 보여주는 대표 증상이다. "
                "acceptance는 HBM 이름 보너스가 아니라 비-HBM selected rows까지 같은 입력/archive, parser-feature, gate 경로가 통과할 때만 인정한다."
            ),
            "plain_conclusion": (
                "첫 수리 slice의 대부분은 점수식 문제가 아니라 exact as-of 입력 archive와 candidate funnel 결손이다. "
                "C06/C02처럼 일부 입력이 있는 row는 strict PIT 또는 date mismatch를 따로 고쳐야 한다."
            ),
        },
        "rows": rows,
    }


def render_v12_runtime_first_repair_input_gap_manifest(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Runtime First Repair Input Gap Manifest",
        "",
        "이 문서는 first repair slice 13개가 실제 구현 전에 어떤 입력을 필요로 하는지 고정한다.",
        "점수를 올리기 전에 exact as-of 입력과 candidate funnel 결손부터 채워야 한다.",
        "",
        "## Summary",
        "",
        f"- plain_conclusion: {summary.get('plain_conclusion')}",
        f"- selected_archetype_count: `{summary.get('selected_archetype_count')}`",
        f"- selected_fixture_role_row_count: `{summary.get('selected_fixture_role_row_count')}`",
        f"- selected_lane_counts: `{summary.get('selected_lane_counts')}`",
        f"- selected_hbm_or_samsung_related_count: `{summary.get('selected_hbm_or_samsung_related_count')}`",
        f"- selected_non_hbm_count: `{summary.get('selected_non_hbm_count')}`",
        f"- role_gap_class_counts: `{summary.get('role_gap_class_counts')}`",
        f"- retrospective_readiness_status_counts: `{summary.get('retrospective_readiness_status_counts')}`",
        f"- strict_pit_readiness_status_counts: `{summary.get('strict_pit_readiness_status_counts')}`",
        f"- fixture_funnel_status_counts: `{summary.get('fixture_funnel_status_counts')}`",
        f"- missing_input_counts: `{summary.get('missing_input_counts')}`",
        f"- generalization_guard: {summary.get('generalization_guard')}",
        "",
        "## Archetype Input Actions",
        "",
        "| archetype | lane | gap classes | current candidates | missing axes | next input action | first tests |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row.get('canonical_archetype_id')} | {row.get('implementation_lane')} | "
            f"{', '.join(row.get('role_gap_classes') or [])} | {row.get('runtime_candidate_count')} | "
            f"{', '.join(row.get('missing_required_bridge_axes') or []) or 'none'} | "
            f"{row.get('next_input_action')} | "
            f"{'<br>'.join((row.get('acceptance_tests_to_add') or [])[:2])} |"
        )
    lines.extend(
        [
            "",
            "## Role Rows",
            "",
            "| archetype | role | symbol | as_of_date | retrospective | strict PIT | funnel | missing inputs | runtime dates |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        for role in row.get("role_gap_rows") or []:
            missing_inputs = list(role.get("retrospective_missing_inputs") or []) + list(
                role.get("strict_pit_missing_inputs") or []
            )
            runtime_dates = role.get("runtime_symbol_dates") or []
            lines.append(
                f"| {row.get('canonical_archetype_id')} | {role.get('role')} | {role.get('symbol')} | "
                f"{role.get('as_of_date')} | {role.get('retrospective_readiness_status')} | "
                f"{role.get('strict_pit_readiness_status')} | {role.get('fixture_funnel_status')} | "
                f"{', '.join(missing_inputs) or 'none'} | {', '.join(runtime_dates[:5]) or 'none'} |"
            )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- C21/C23/C26은 점수식이 낮은 게 아니라 시험지가 current replay에 안 들어온 상태다.",
            "- C06 green은 시험지는 어느 정도 있지만 strict PIT search snapshot과 exact 날짜 replay가 부족하다.",
            "- C02는 입력이 가장 많이 준비된 편이라, 다음 단계가 weighted gate 검증이다.",
            "- 하닉/삼전만 좋아지는 패치는 실패다. 같은 수리로 금융, 바이오, 플랫폼, 소비재, 전력망 아키타입도 검증해야 한다.",
            "- 쉬운 예: 채점표를 고치기 전에 시험 당시 문제지와 답안지가 있는지부터 확인해야 한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_runtime_first_repair_input_gap_manifest(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_runtime_first_repair_input_gap_manifest()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_runtime_first_repair_input_gap_manifest(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_runtime_first_repair_input_gap_manifest()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
