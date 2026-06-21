"""Materialize v12 Green/guard candidates into replay-spec rows."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any
import json


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _case_identity(candidate: dict[str, Any] | None) -> dict[str, Any]:
    candidate = candidate or {}
    identity = {
        "case_id": candidate.get("case_id"),
        "trigger_id": candidate.get("trigger_id"),
        "symbol": candidate.get("symbol"),
        "as_of_date": candidate.get("trigger_date") or candidate.get("entry_date"),
        "trigger_type": candidate.get("trigger_type"),
        "MFE_180D_pct": candidate.get("MFE_180D_pct"),
        "MAE_180D_pct": candidate.get("MAE_180D_pct"),
        "evidence_available_at_that_date": candidate.get("evidence_available_at_that_date"),
        "evidence_source": candidate.get("evidence_source"),
        "source_file": candidate.get("source_file"),
        "source_proxy_only": bool(candidate.get("source_proxy_only")),
        "evidence_url_pending": bool(candidate.get("evidence_url_pending")),
    }
    source_primitives = candidate.get("source_expected_runtime_primitives")
    if isinstance(source_primitives, list):
        identity["source_expected_runtime_primitives"] = list(source_primitives)
    for key in ("source_canonical_archetype_id", "source_large_sector_id"):
        value = candidate.get(key)
        if value:
            identity[key] = value
    return identity


def _coverage_by_archetype(coverage_payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(row.get("canonical_archetype_id")): row
        for row in coverage_payload.get("archetypes", [])
        if row.get("canonical_archetype_id")
    }


def _spec_row(
    *,
    archetype_row: dict[str, Any],
    coverage_row: dict[str, Any],
    role: str,
    candidate: dict[str, Any] | None,
) -> dict[str, Any]:
    expected_outcome = (
        "green_candidate_should_reach_stage3_green_or_emit_field_level_deficit"
        if role == "green"
        else "guard_candidate_must_not_reach_stage3_green"
    )
    return {
        "schema_version": "v12_runtime_replay_spec_v1",
        "role": role,
        "expected_outcome": expected_outcome,
        "canonical_archetype_id": archetype_row.get("canonical_archetype_id"),
        "large_sector_id": archetype_row.get("large_sector_id"),
        "runtime_bridge_group": archetype_row.get("runtime_bridge_group"),
        "fixture_status": archetype_row.get("fixture_status"),
        "expected_runtime_primitives": list(archetype_row.get("expected_runtime_primitives") or ()),
        "required_bridge_axes": list(coverage_row.get("required_bridge_axes") or ()),
        "current_runtime_gap_status": coverage_row.get("runtime_gap_status"),
        "current_runtime_candidate_count": coverage_row.get("runtime_candidate_count", 0),
        "current_runtime_stage_distribution": coverage_row.get("runtime_stage_distribution") or {},
        "current_runtime_max_score": coverage_row.get("runtime_max_score"),
        "current_missing_required_bridge_axes": list(coverage_row.get("missing_required_bridge_axes") or ()),
        "current_top_failed_gates": list(coverage_row.get("top_failed_gates") or ()),
        "candidate": _case_identity(candidate),
        "replay_note": (
            "diagnostic_only_not_production_scoring_input; "
            "convert_to_historical_or_asof_fixture_with_point_in_time_sources_before using as proof"
        ),
    }


def _is_stage3_green_candidate(candidate: dict[str, Any] | None) -> bool:
    return str((candidate or {}).get("trigger_type") or "") == "Stage3-Green"


def build_v12_runtime_replay_spec(
    *,
    fixture_payload: dict[str, Any],
    coverage_payload: dict[str, Any],
) -> dict[str, Any]:
    """Build a stable Green/guard replay-spec from fixture candidates.

    The output is intentionally a diagnostic spec, not a scoring input. It says
    which cases should be converted into full point-in-time fixtures next.
    """

    coverage = _coverage_by_archetype(coverage_payload)
    rows: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    for archetype in fixture_payload.get("archetypes", []):
        coverage_row = coverage.get(str(archetype.get("canonical_archetype_id")), {})
        green = archetype.get("green_fixture_candidate")
        guard = archetype.get("guard_fixture_candidate")
        if archetype.get("fixture_status") != "ready_for_runtime_replay_fixture":
            skipped.append(
                {
                    "canonical_archetype_id": archetype.get("canonical_archetype_id"),
                    "fixture_status": archetype.get("fixture_status"),
                    "included_roles": ["guard"] if guard else [],
                }
            )
            if guard:
                rows.append(_spec_row(archetype_row=archetype, coverage_row=coverage_row, role="guard", candidate=guard))
            continue
        if green and _is_stage3_green_candidate(green):
            rows.append(_spec_row(archetype_row=archetype, coverage_row=coverage_row, role="green", candidate=green))
        elif green:
            skipped.append(
                {
                    "canonical_archetype_id": archetype.get("canonical_archetype_id"),
                    "fixture_status": archetype.get("fixture_status"),
                    "included_roles": [],
                    "skipped_green_candidate_trigger_type": green.get("trigger_type"),
                    "skip_reason": "green_replay_role_requires_raw_stage3_green_trigger",
                }
            )
        if guard:
            rows.append(_spec_row(archetype_row=archetype, coverage_row=coverage_row, role="guard", candidate=guard))

    role_counts = Counter(row["role"] for row in rows)
    gap_counts = Counter(row["current_runtime_gap_status"] for row in rows)
    ready_archetypes = {
        row.get("canonical_archetype_id")
        for row in fixture_payload.get("archetypes", [])
        if row.get("fixture_status") == "ready_for_runtime_replay_fixture"
    }
    return {
        "schema_version": "v12_runtime_replay_spec_manifest_v1",
        "spec_row_count": len(rows),
        "ready_archetype_count": len(ready_archetypes),
        "covered_archetype_count": len({row["canonical_archetype_id"] for row in rows}),
        "role_counts": dict(sorted(role_counts.items())),
        "current_runtime_gap_status_counts": dict(sorted(gap_counts.items(), key=lambda item: str(item[0]))),
        "skipped_archetypes": skipped,
        "rows": rows,
    }


def render_v12_runtime_replay_spec(payload: dict[str, Any]) -> str:
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Runtime Replay Fixture Spec",
        "",
        "이 문서는 누적 연구 Green/guard 후보를 다음 runtime replay fixture로 바꾸기 위한 실행 spec이다.",
        "아직 production scoring 입력이 아니며, full point-in-time source fixture로 변환하기 전까지는 증명으로 쓰지 않는다.",
        "",
        "## Summary",
        "",
        f"- spec_row_count: `{payload.get('spec_row_count', 0)}`",
        f"- ready_archetype_count: `{payload.get('ready_archetype_count', 0)}`",
        f"- covered_archetype_count: `{payload.get('covered_archetype_count', payload.get('ready_archetype_count', 0))}`",
        f"- role_counts: `{payload.get('role_counts', {})}`",
        f"- current_runtime_gap_status_counts: `{payload.get('current_runtime_gap_status_counts', {})}`",
        f"- skipped_archetypes: `{len(payload.get('skipped_archetypes', []))}`",
        "",
        "## Replay Rows",
        "",
        "| role | archetype | symbol | as-of | expected outcome | current gap | missing axes | top failed gates |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(rows, key=lambda item: (str(item["canonical_archetype_id"]), str(item["role"]))):
        candidate = row.get("candidate") or {}
        top_gates = ", ".join(
            f"{item.get('gate')}:{item.get('count')}" for item in row.get("current_top_failed_gates", [])[:3]
        )
        missing_axes = ", ".join(row.get("current_missing_required_bridge_axes") or [])
        lines.append(
            "| {role} | {arch} | {symbol} | {asof} | {outcome} | {gap} | {axes} | {gates} |".format(
                role=row["role"],
                arch=row["canonical_archetype_id"],
                symbol=candidate.get("symbol") or "",
                asof=candidate.get("as_of_date") or "",
                outcome=row["expected_outcome"],
                gap=row.get("current_runtime_gap_status") or "",
                axes=missing_axes or "none",
                gates=top_gates or "none",
            )
        )
    lines.extend(
        [
            "",
            "## Conversion Rule",
            "",
            "1. `green` row는 source-backed primitive가 component/gate까지 올라와야 한다.",
            "2. `guard` row는 같은 primitive를 일부 갖더라도 false Green으로 열리면 안 된다.",
            "3. 현재 `not_in_current_benchmark`인 row는 candidate funnel/replay coverage부터 고쳐야 한다.",
            "4. 현재 `runtime_input_evidence_missing`인 row는 parser가 아니라 source-backed 입력 가족부터 채워야 한다.",
            "5. 현재 `runtime_bridge_axes_missing`인 row는 parser/feature adapter에서 누락 primitive를 먼저 본다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_runtime_replay_spec(
    *,
    fixture_candidates_path: str | Path,
    coverage_board_path: str | Path,
    output_json_path: str | Path,
    output_jsonl_path: str | Path,
    output_markdown_path: str | Path,
) -> dict[str, Path]:
    payload = build_v12_runtime_replay_spec(
        fixture_payload=_read_json(fixture_candidates_path),
        coverage_payload=_read_json(coverage_board_path),
    )
    json_path = Path(output_json_path)
    jsonl_path = Path(output_jsonl_path)
    md_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for row in payload["rows"]:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n")
    md_path.write_text(render_v12_runtime_replay_spec(payload), encoding="utf-8")
    return {"json": json_path, "jsonl": jsonl_path, "markdown": md_path}
