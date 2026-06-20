"""Audit whether v12 fixture spec rows even enter the current runtime funnel."""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any
import json

from .v12_runtime_replay_spec import build_v12_runtime_replay_spec


def _read_json(path: str | Path) -> Any:
    path_obj = Path(path)
    if not path_obj.exists():
        return {} if path_obj.suffix == ".json" else []
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _parse_date(value: Any) -> date | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def _day_delta(left: Any, right: Any) -> int | None:
    left_date = _parse_date(left)
    right_date = _parse_date(right)
    if left_date is None or right_date is None:
        return None
    return abs((left_date - right_date).days)


def _candidate_key(row: dict[str, Any]) -> tuple[str, str]:
    return (str(row.get("symbol") or "").strip(), str(row.get("as_of_date") or "").strip())


def _spec_candidate(row: dict[str, Any]) -> dict[str, Any]:
    candidate = row.get("candidate") or {}
    return {
        "case_id": candidate.get("case_id"),
        "symbol": str(candidate.get("symbol") or "").strip(),
        "as_of_date": str(candidate.get("as_of_date") or "").strip(),
        "trigger_type": candidate.get("trigger_type"),
        "MFE_180D_pct": candidate.get("MFE_180D_pct"),
        "MAE_180D_pct": candidate.get("MAE_180D_pct"),
    }


def _spec_rows(spec_payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows = list(spec_payload.get("rows") or [])
    if rows:
        return rows
    if spec_payload.get("archetypes"):
        replay_spec = build_v12_runtime_replay_spec(fixture_payload=spec_payload, coverage_payload={})
        return list(replay_spec.get("rows") or [])
    return []


def _runtime_candidate_view(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "symbol": row.get("symbol"),
        "company_name": row.get("company_name"),
        "as_of_date": row.get("as_of_date"),
        "stage": row.get("stage") or row.get("merged_stage"),
        "score": row.get("score") or row.get("merged_score"),
        "candidate_source_path": row.get("candidate_source_path"),
        "layer": row.get("layer"),
        "promotion_band": row.get("promotion_band"),
        "reason_codes": row.get("reason_codes") or [],
    }


def _nearest_runtime_rows(
    *, spec_as_of: str, runtime_rows: list[dict[str, Any]], limit: int = 4
) -> list[dict[str, Any]]:
    rows_with_delta = [
        (_day_delta(spec_as_of, row.get("as_of_date")), row)
        for row in runtime_rows
        if _day_delta(spec_as_of, row.get("as_of_date")) is not None
    ]
    rows_with_delta.sort(key=lambda item: (item[0] if item[0] is not None else 10**9, str(item[1].get("as_of_date"))))
    result: list[dict[str, Any]] = []
    for delta, row in rows_with_delta[:limit]:
        view = _runtime_candidate_view(row)
        view["date_delta_days"] = delta
        result.append(view)
    return result


def _fixture_funnel_status(*, exact: bool, symbol_rows: list[dict[str, Any]]) -> str:
    if exact:
        return "exact_symbol_date_candidate_reached_runtime"
    if symbol_rows:
        return "symbol_reached_runtime_but_not_fixture_date"
    return "symbol_never_reached_current_runtime"


def _funnel_root_cause(status: str) -> str:
    if status == "exact_symbol_date_candidate_reached_runtime":
        return "candidate_reached_scoring_then_score_or_gate_decides"
    if status == "symbol_reached_runtime_but_not_fixture_date":
        return "monthly_schedule_or_fixture_date_mismatch"
    return "benchmark_universe_or_official_cheap_scan_funnel_gap"


def _snapshot_universe_counts(replay_summary: dict[str, Any]) -> dict[str, Any]:
    counts = [
        int(snapshot.get("universe_count") or 0)
        for snapshot in replay_summary.get("snapshots", [])
        if "universe_count" in snapshot
    ]
    if not counts:
        return {"min": 0, "max": 0, "latest": 0}
    return {"min": min(counts), "max": max(counts), "latest": counts[-1]}


def build_v12_fixture_candidate_funnel_audit(
    *,
    spec_payload: dict[str, Any],
    discovered_candidates: list[dict[str, Any]],
    replay_summary: dict[str, Any],
) -> dict[str, Any]:
    """Compare v12 fixture spec rows with current replay discovered candidates."""

    runtime_by_key = {_candidate_key(row): row for row in discovered_candidates}
    runtime_by_symbol: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in discovered_candidates:
        symbol = str(row.get("symbol") or "").strip()
        if symbol:
            runtime_by_symbol[symbol].append(row)

    rows: list[dict[str, Any]] = []
    for spec_row in _spec_rows(spec_payload):
        candidate = _spec_candidate(spec_row)
        key = (candidate["symbol"], candidate["as_of_date"])
        symbol_rows = runtime_by_symbol.get(candidate["symbol"], [])
        exact = key in runtime_by_key
        status = _fixture_funnel_status(exact=exact, symbol_rows=symbol_rows)
        exact_view = _runtime_candidate_view(runtime_by_key[key]) if exact else None
        rows.append(
            {
                "role": spec_row.get("role"),
                "canonical_archetype_id": spec_row.get("canonical_archetype_id"),
                "runtime_bridge_group": spec_row.get("runtime_bridge_group"),
                "current_runtime_gap_status": spec_row.get("current_runtime_gap_status"),
                "expected_outcome": spec_row.get("expected_outcome"),
                "candidate": candidate,
                "fixture_funnel_status": status,
                "funnel_root_cause": _funnel_root_cause(status),
                "runtime_symbol_candidate_count": len(symbol_rows),
                "runtime_symbol_dates": [row.get("as_of_date") for row in symbol_rows[:12]],
                "runtime_candidate_source_paths": sorted(
                    {str(row.get("candidate_source_path") or "") for row in symbol_rows if row.get("candidate_source_path")}
                ),
                "runtime_exact_candidate": exact_view,
                "nearest_runtime_candidates": _nearest_runtime_rows(
                    spec_as_of=candidate["as_of_date"],
                    runtime_rows=symbol_rows,
                ),
            }
        )

    status_counts = Counter(str(row["fixture_funnel_status"]) for row in rows)
    cause_counts = Counter(str(row["funnel_root_cause"]) for row in rows)
    role_status_counts = Counter(f"{row.get('role')}:{row['fixture_funnel_status']}" for row in rows)
    archetypes_with_exact = {row["canonical_archetype_id"] for row in rows if row["fixture_funnel_status"].startswith("exact")}
    archetypes_with_symbol = {
        row["canonical_archetype_id"]
        for row in rows
        if row["fixture_funnel_status"] == "symbol_reached_runtime_but_not_fixture_date"
    }
    config = replay_summary.get("config") or {}
    candidate_source_counts = Counter(str(row.get("candidate_source_path") or "") for row in discovered_candidates)
    return {
        "schema_version": "v12_fixture_candidate_funnel_audit_v1",
        "scope": "v12_runtime_replay_spec_rows_vs_current_benchmark_discovered_candidates",
        "spec_row_count": len(rows),
        "runtime_discovered_candidate_count": len(discovered_candidates),
        "runtime_discovered_symbol_count": len(runtime_by_symbol),
        "fixture_funnel_status_counts": _counter_dict(status_counts),
        "funnel_root_cause_counts": _counter_dict(cause_counts),
        "role_status_counts": _counter_dict(role_status_counts),
        "archetype_exact_candidate_count": len(archetypes_with_exact),
        "archetype_symbol_only_count": len(archetypes_with_symbol),
        "runtime_candidate_source_path_counts": _counter_dict(candidate_source_counts),
        "replay_config_summary": {
            "frequency": config.get("frequency"),
            "fixture_search": config.get("fixture_search"),
            "live_search": config.get("live_search"),
            "allow_snapshot_derived_universe": config.get("allow_snapshot_derived_universe"),
            "benchmark_label_path": config.get("benchmark_label_path"),
            "universe_count": _snapshot_universe_counts(replay_summary),
            "max_candidates_per_date": config.get("max_candidates_per_date"),
            "max_web_research_candidates_per_date": config.get("max_web_research_candidates_per_date"),
        },
        "rows": rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _candidate_text(candidate: dict[str, Any]) -> str:
    return " ".join(
        part
        for part in (
            str(candidate.get("symbol") or "").strip(),
            str(candidate.get("as_of_date") or "").strip(),
            str(candidate.get("case_id") or "").strip(),
        )
        if part
    )


def _nearest_text(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "none"
    return ", ".join(
        "{date}/{stage}/{score}/d{delta}".format(
            date=row.get("as_of_date"),
            stage=row.get("stage"),
            score=row.get("score"),
            delta=row.get("date_delta_days"),
        )
        for row in rows[:3]
    )


def render_v12_fixture_candidate_funnel_audit(payload: dict[str, Any]) -> str:
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Fixture Candidate Funnel Audit",
        "",
        "이 문서는 Green/guard fixture spec이 현재 runtime replay 후보까지 도달했는지 확인한다.",
        "점수가 낮은 문제와 후보가 아예 없는 문제를 분리하기 위한 장부다.",
        "",
        "## Summary",
        "",
        f"- spec_row_count: `{payload.get('spec_row_count', 0)}`",
        f"- runtime_discovered_candidate_count: `{payload.get('runtime_discovered_candidate_count', 0)}`",
        f"- runtime_discovered_symbol_count: `{payload.get('runtime_discovered_symbol_count', 0)}`",
        f"- fixture_funnel_status_counts: `{payload.get('fixture_funnel_status_counts', {})}`",
        f"- funnel_root_cause_counts: `{payload.get('funnel_root_cause_counts', {})}`",
        f"- role_status_counts: `{payload.get('role_status_counts', {})}`",
        f"- runtime_candidate_source_path_counts: `{payload.get('runtime_candidate_source_path_counts', {})}`",
        f"- replay_config_summary: `{payload.get('replay_config_summary', {})}`",
        "",
        "## Fixture Rows",
        "",
        "| role | archetype | fixture candidate | funnel status | symbol hits | nearest runtime rows | root cause |",
        "| --- | --- | --- | --- | ---: | --- | --- |",
    ]
    for row in sorted(
        rows,
        key=lambda item: (
            str(item.get("fixture_funnel_status")),
            str(item.get("canonical_archetype_id")),
            str(item.get("role")),
        ),
    ):
        lines.append(
            "| {role} | {arch} | {candidate} | {status} | {hits} | {nearest} | {cause} |".format(
                role=row.get("role"),
                arch=row.get("canonical_archetype_id"),
                candidate=_candidate_text(row.get("candidate") or {}),
                status=row.get("fixture_funnel_status"),
                hits=row.get("runtime_symbol_candidate_count", 0),
                nearest=_nearest_text(row.get("nearest_runtime_candidates") or []),
                cause=row.get("funnel_root_cause"),
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- `exact_symbol_date_candidate_reached_runtime`: 그 fixture 날짜와 종목이 실제 점수 계산까지 갔다.",
            "- `symbol_reached_runtime_but_not_fixture_date`: 종목은 후보가 됐지만, 연구 Green 날짜와 replay 날짜가 다르다.",
            "- `symbol_never_reached_current_runtime`: current benchmark의 universe/cheap-scan 후보에 종목이 아예 없다.",
            "- 쉬운 예: 하닉 `000660 2024-04-25`는 symbol은 있었지만 current benchmark는 월초 `2024-04-01/2024-05-01` 중심이라 exact fixture가 아니다.",
            "- 쉬운 예: C21/C23/C28 주요 Green 후보는 symbol 자체가 current benchmark에 없어서 점수식을 테스트하지 못한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_fixture_candidate_funnel_audit(
    *,
    spec_path: str | Path,
    discovered_candidates_path: str | Path,
    replay_summary_path: str | Path,
    output_json_path: str | Path,
    output_markdown_path: str | Path,
) -> dict[str, Path]:
    payload = build_v12_fixture_candidate_funnel_audit(
        spec_payload=_read_json(spec_path),
        discovered_candidates=_read_json(discovered_candidates_path),
        replay_summary=_read_json(replay_summary_path),
    )
    json_path = Path(output_json_path)
    md_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_fixture_candidate_funnel_audit(payload), encoding="utf-8")
    return {"json": json_path, "markdown": md_path}
