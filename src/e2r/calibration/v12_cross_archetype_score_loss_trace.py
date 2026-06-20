"""Trace score-loss layers across all ready v12 archetype fixtures."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import json


LOSS_BUCKETS: dict[str, dict[str, str]] = {
    "fixture_not_ready": {
        "loss_layer": "research_fixture_source_readiness",
        "simple_explanation": "Research rows exist, but a source-backed Green/guard fixture pair is not ready.",
        "next_action": "Repair verified Green source rows before runtime scoring changes.",
    },
    "not_in_current_benchmark": {
        "loss_layer": "candidate_funnel_or_replay_coverage",
        "simple_explanation": "Research has a Green/guard pair, but current runtime replay does not execute it.",
        "next_action": "Materialize point-in-time replay fixtures before changing scoring weights.",
    },
    "runtime_bridge_axes_missing": {
        "loss_layer": "research_axis_to_runtime_field_translation",
        "simple_explanation": "Runtime candidates exist, but required source-backed bridge axes remain zero.",
        "next_action": "Patch parser/feature adapters for the missing bridge axes and keep the guard pair closed.",
    },
    "runtime_input_evidence_missing": {
        "loss_layer": "runtime_input_evidence_coverage",
        "simple_explanation": "Runtime candidates exist, but the source families needed to judge bridge translation are missing.",
        "next_action": "Repair replay input coverage or fixture archive before blaming parser or weights.",
    },
    "runtime_stage3_gate_blocked": {
        "loss_layer": "weighted_component_or_stage3_gate",
        "simple_explanation": "Bridge axes are present enough, but weighted total, bottleneck, or visibility gate blocks Green.",
        "next_action": "Inspect component formula and gate thresholds only with positive/guard replay evidence.",
    },
    "runtime_green_or_near_ready": {
        "loss_layer": "near_ready_or_green",
        "simple_explanation": "Runtime is close enough to inspect exact Green/guard behavior.",
        "next_action": "Run exact fixture replay and verify guard rows do not become false Green.",
    },
    "runtime_needs_review": {
        "loss_layer": "manual_review",
        "simple_explanation": "Runtime state does not fit the main buckets.",
        "next_action": "Review score rows, gate rows, and source-backed evidence ids.",
    },
}


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _candidate_identity(candidate: dict[str, Any] | None) -> dict[str, Any]:
    candidate = candidate or {}
    return {
        "case_id": candidate.get("case_id"),
        "symbol": candidate.get("symbol"),
        "as_of_date": candidate.get("as_of_date"),
        "trigger_type": candidate.get("trigger_type"),
        "MFE_180D_pct": candidate.get("MFE_180D_pct"),
        "MAE_180D_pct": candidate.get("MAE_180D_pct"),
    }


def _coverage_by_archetype(coverage_payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(row.get("canonical_archetype_id")): row
        for row in coverage_payload.get("archetypes", [])
        if row.get("canonical_archetype_id")
    }


def _spec_rows_by_archetype(spec_payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in spec_payload.get("rows", []):
        archetype = str(row.get("canonical_archetype_id") or "")
        if archetype:
            grouped[archetype].append(row)
    return grouped


def _first_role_row(rows: list[dict[str, Any]], role: str) -> dict[str, Any]:
    return next((row for row in rows if row.get("role") == role), {})


def _loss_bucket(status: str) -> dict[str, str]:
    return LOSS_BUCKETS.get(status, LOSS_BUCKETS["runtime_needs_review"])


def _role_gap_counts(rows: list[dict[str, Any]], role: str) -> dict[str, int]:
    counts = Counter(
        str(row.get("current_runtime_gap_status") or "unknown") for row in rows if row.get("role") == role
    )
    return _counter_dict(counts)


def build_v12_cross_archetype_score_loss_trace(
    *,
    spec_payload: dict[str, Any],
    coverage_payload: dict[str, Any],
) -> dict[str, Any]:
    """Build a cross-archetype loss trace from fixture spec and runtime coverage.

    The payload is diagnostic only. It does not grant any sector, archetype, or
    symbol a scoring bonus.
    """

    grouped_spec = _spec_rows_by_archetype(spec_payload)
    coverage = _coverage_by_archetype(coverage_payload)
    rows: list[dict[str, Any]] = []
    for archetype, spec_rows in sorted(grouped_spec.items()):
        coverage_row = coverage.get(archetype, {})
        green_row = _first_role_row(spec_rows, "green")
        guard_row = _first_role_row(spec_rows, "guard")
        status = str(coverage_row.get("runtime_gap_status") or green_row.get("current_runtime_gap_status") or "")
        bucket = _loss_bucket(status)
        rows.append(
            {
                "canonical_archetype_id": archetype,
                "large_sector_id": coverage_row.get("large_sector_id") or green_row.get("large_sector_id"),
                "runtime_bridge_group": coverage_row.get("runtime_bridge_group") or green_row.get("runtime_bridge_group"),
                "loss_layer": bucket["loss_layer"],
                "runtime_gap_status": status or "unknown",
                "simple_explanation": bucket["simple_explanation"],
                "next_action": bucket["next_action"],
                "runtime_candidate_count": coverage_row.get("runtime_candidate_count", 0),
                "runtime_stage_distribution": coverage_row.get("runtime_stage_distribution") or {},
                "runtime_max_score": coverage_row.get("runtime_max_score"),
                "runtime_green_count": coverage_row.get("runtime_green_count", 0),
                "required_bridge_axes": list(coverage_row.get("required_bridge_axes") or ()),
                "missing_required_bridge_axes": list(coverage_row.get("missing_required_bridge_axes") or ()),
                "top_failed_gates": list(coverage_row.get("top_failed_gates") or ()),
                "runtime_input_evidence_summary": dict(coverage_row.get("runtime_input_evidence_summary") or {}),
                "expected_runtime_primitives": list(green_row.get("expected_runtime_primitives") or ()),
                "green_candidate": _candidate_identity(green_row.get("candidate")),
                "guard_candidate": _candidate_identity(guard_row.get("candidate")),
            }
        )

    status_counts = Counter(row["runtime_gap_status"] for row in rows)
    layer_counts = Counter(row["loss_layer"] for row in rows)
    missing_axis_counts: Counter[str] = Counter()
    runtime_candidate_status_counts: Counter[str] = Counter()
    for row in rows:
        missing_axis_counts.update(row["missing_required_bridge_axes"])
        if int(row.get("runtime_candidate_count") or 0) > 0:
            runtime_candidate_status_counts[row["runtime_gap_status"]] += 1

    spec_rows = list(spec_payload.get("rows", []))
    return {
        "schema_version": "v12_cross_archetype_score_loss_trace_v1",
        "scope": "all_ready_v12_archetype_green_guard_fixture_pairs",
        "scoring_policy": "diagnostic_only_no_symbol_or_archetype_bonus",
        "ready_archetype_count": len(rows),
        "spec_row_count": len(spec_rows),
        "role_counts": _counter_dict(Counter(str(row.get("role") or "unknown") for row in spec_rows)),
        "gap_status_counts_by_archetype": _counter_dict(status_counts),
        "gap_status_counts_by_green_role": _role_gap_counts(spec_rows, "green"),
        "gap_status_counts_by_guard_role": _role_gap_counts(spec_rows, "guard"),
        "loss_layer_counts_by_archetype": _counter_dict(layer_counts),
        "runtime_candidate_status_counts_by_archetype": _counter_dict(runtime_candidate_status_counts),
        "missing_required_bridge_axis_counts": _counter_dict(missing_axis_counts),
        "rows": rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _join(values: list[Any]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "none"


def _gate_text(gates: list[dict[str, Any]]) -> str:
    return ", ".join(f"{item.get('gate')}:{item.get('count')}" for item in gates[:3]) or "none"


def render_v12_cross_archetype_score_loss_trace(payload: dict[str, Any]) -> str:
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Cross-Archetype Score Loss Trace",
        "",
        "이 문서는 HBM에 점수를 더 주기 위한 문서가 아니다.",
        "누적 연구 Green/guard 쌍이 전 아키타입에서 runtime 어디서 사라지는지 분해한다.",
        "",
        "## Summary",
        "",
        f"- ready_archetype_count: `{payload.get('ready_archetype_count', 0)}`",
        f"- spec_row_count: `{payload.get('spec_row_count', 0)}`",
        f"- role_counts: `{payload.get('role_counts', {})}`",
        f"- gap_status_counts_by_archetype: `{payload.get('gap_status_counts_by_archetype', {})}`",
        f"- loss_layer_counts_by_archetype: `{payload.get('loss_layer_counts_by_archetype', {})}`",
        f"- runtime_candidate_status_counts_by_archetype: `{payload.get('runtime_candidate_status_counts_by_archetype', {})}`",
        f"- missing_required_bridge_axis_counts: `{payload.get('missing_required_bridge_axis_counts', {})}`",
        f"- scoring_policy: `{payload.get('scoring_policy')}`",
        "",
        "## Loss Buckets",
        "",
        "| status | loss layer | next action |",
        "| --- | --- | --- |",
    ]
    for status, bucket in LOSS_BUCKETS.items():
        lines.append(f"| {status} | {bucket['loss_layer']} | {bucket['next_action']} |")
    lines.extend(
        [
            "",
            "## Archetype Rows",
            "",
            "| archetype | green | guard | status | layer | runtime candidates | max score | missing axes | failed gates |",
            "| --- | --- | --- | --- | --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in sorted(
        rows,
        key=lambda item: (
            str(item.get("runtime_gap_status")),
            -int(item.get("runtime_candidate_count") or 0),
            str(item.get("canonical_archetype_id")),
        ),
    ):
        green = row.get("green_candidate") or {}
        guard = row.get("guard_candidate") or {}
        green_text = "{symbol} {asof}".format(symbol=_fmt(green.get("symbol")), asof=_fmt(green.get("as_of_date"))).strip()
        guard_text = "{symbol} {asof}".format(symbol=_fmt(guard.get("symbol")), asof=_fmt(guard.get("as_of_date"))).strip()
        lines.append(
            "| {arch} | {green} | {guard} | {status} | {layer} | {count} | {score} | {axes} | {gates} |".format(
                arch=row.get("canonical_archetype_id"),
                green=green_text or "none",
                guard=guard_text or "none",
                status=row.get("runtime_gap_status"),
                layer=row.get("loss_layer"),
                count=row.get("runtime_candidate_count", 0),
                score=_fmt(row.get("runtime_max_score")),
                axes=_join(row.get("missing_required_bridge_axes") or []),
                gates=_gate_text(row.get("top_failed_gates") or []),
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 하닉/삼전은 예시다. 같은 구조가 금융, 보험, 바이오, 소프트웨어, 소비재, 건설/정책 이벤트에서도 생긴다.",
            "- `not_in_current_benchmark`는 좋은 연구 사례가 있어도 현재 replay가 그 아키타입을 아예 시험하지 않는다는 뜻이다.",
            "- `runtime_input_evidence_missing`은 후보는 있지만 리포트/뉴스/컨센서스/충분한 공시+재무 입력이 없어 parser 실패인지 판단할 수 없다는 뜻이다.",
            "- `runtime_bridge_axes_missing`은 후보는 올라왔지만 연구 문장이 `backlog`, `contract`, `capital_return`, `bio_commercialization` 같은 runtime field로 못 바뀐다는 뜻이다.",
            "- `runtime_stage3_gate_blocked`는 field가 일부 살아도 weighted component와 Green gate가 아직 부족하다는 뜻이다.",
            "- 쉬운 예: C10 삼성은 후보와 리포트는 있지만 customer/backlog/contract bridge가 약하고, C21 금융은 `capital_return/valuation_repricing` fixture가 benchmark에 안 들어오며, C23 바이오는 `approval`이 매출화 bridge로 검증되지 않을 수 있다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_cross_archetype_score_loss_trace(
    *,
    spec_path: str | Path,
    coverage_board_path: str | Path,
    output_json_path: str | Path,
    output_markdown_path: str | Path,
) -> dict[str, Path]:
    payload = build_v12_cross_archetype_score_loss_trace(
        spec_payload=_read_json(spec_path),
        coverage_payload=_read_json(coverage_board_path),
    )
    json_path = Path(output_json_path)
    md_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_cross_archetype_score_loss_trace(payload), encoding="utf-8")
    return {"json": json_path, "markdown": md_path}
