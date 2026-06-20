"""Audit accumulated Green research signals against runtime translation by archetype."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import csv
import json

from .v12_runtime_fixture_candidates import (
    ARCHETYPE_RUNTIME_BRIDGE_SPECS,
    DEFAULT_RUNTIME_BRIDGE_SPEC,
    _green_fixture_ready,
    _is_raw_green_trigger,
    _row_view,
)


AXIS_KEYWORDS: dict[str, tuple[str, ...]] = {
    "margin": ("margin", "opm", "asp", "mix", "profit", "영업이익", "마진", "spread"),
    "customer": ("customer", "named", "nvidia", "partner", "client", "고객", "j&j", "distribution"),
    "backlog": ("backlog", "rpo", "orderbook", "order backlog", "수주잔고", "booked", "sold out", "pre-sold"),
    "contract": ("contract", "supply", "order", "long-term", "repeat", "renewal", "계약", "공급"),
    "valuation_repricing": ("valuation", "rerating", "pbr", "low-pbr", "value-up", "target price", "재평가"),
    "capital_return": ("capital return", "shareholder", "buyback", "cancellation", "dividend", "treasury", "자사주", "배당"),
    "insurance_quality": ("csm", "k-ics", "reserve", "loss ratio", "underwriting", "준비금", "손해율"),
    "bio_commercialization": ("fda", "approval", "label", "royalty", "commercialization", "launch", "reimbursement", "승인"),
    "software_retention": ("arr", "nrr", "rpo", "retention", "renewal", "subscription", "saas", "recurring"),
    "consumer_sell_through": ("sell-through", "sell through", "reorder", "channel", "export", "distribution", "repeat order"),
    "guard_risk": ("false", "policy_only", "headline_only", "pre-pdufa", "delay", "risk", "overheat", "blowoff"),
}

AXIS_RUNTIME_FIELDS: dict[str, tuple[str, ...]] = {
    "margin": ("research_axis_bridge_margin", "asp_pricing_power", "actual_profit_conversion_score"),
    "customer": ("research_axis_bridge_customer",),
    "backlog": ("research_axis_bridge_backlog", "backlog_rpo_visibility"),
    "contract": ("research_axis_bridge_contract", "contract_quality"),
    "valuation_repricing": ("research_axis_bridge_valuation_repricing", "price_stage_score"),
    "capital_return": ("research_axis_bridge_capital_return",),
    "insurance_quality": ("research_axis_bridge_insurance_quality",),
    "bio_commercialization": ("research_axis_bridge_bio_commercialization",),
    "software_retention": ("research_axis_bridge_software_retention",),
    "consumer_sell_through": ("research_axis_bridge_consumer_sell_through",),
    "guard_risk": ("research_axis_bridge_guard_risk", "research_axis_bridge_guard_risk_penalty_points"),
}


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


def _read_csv(path: str | Path) -> list[dict[str, str]]:
    path_obj = Path(path)
    if not path_obj.exists():
        return []
    with path_obj.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _safe_float(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _coverage_by_archetype(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): row for row in payload.get("rows", [])}


def _readiness_by_archetype(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): row for row in payload.get("archetype_pair_rows", [])}


def _rows_by_archetype(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        archetype = str(row.get("canonical_archetype_id") or "")
        if archetype:
            grouped[archetype].append(row)
    return grouped


def _runtime_rows_by_archetype(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        archetype = str(row.get("canonical_archetype_id") or "")
        if archetype:
            grouped[archetype].append(row)
    return grouped


def _row_text(row: dict[str, Any]) -> str:
    return " ".join(
        str(row.get(key) or "")
        for key in (
            "case_id",
            "trigger_id",
            "trigger_type",
            "trigger_outcome_label",
            "current_profile_verdict",
            "fine_archetype_id",
            "evidence_available_at_that_date",
            "evidence_source",
            "raw_source_snippet",
        )
    ).lower()


def _axis_signal_counts(rows: list[dict[str, Any]], axes: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for axis in axes:
        keywords = AXIS_KEYWORDS.get(axis, ())
        counts[axis] = sum(1 for row in rows if any(keyword in _row_text(row) for keyword in keywords))
    return counts


def _runtime_best_row(rows: list[dict[str, str]]) -> dict[str, str] | None:
    if not rows:
        return None
    return max(rows, key=lambda row: _safe_float(row.get("current_score")) or -1.0)


def _runtime_view(row: dict[str, str] | None) -> dict[str, Any] | None:
    if row is None:
        return None
    keys = (
        "symbol",
        "company_name",
        "as_of_date",
        "current_stage",
        "current_score",
        "canonical_archetype_id",
        "sector_profile",
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
        "green_gate_deficit_summary",
        "explanation",
    )
    return {key: row.get(key) for key in keys}


def _axis_runtime_status(row: dict[str, str] | None, axes: list[str], missing_axes: list[str]) -> list[dict[str, Any]]:
    statuses: list[dict[str, Any]] = []
    missing_axis_set = set(missing_axes)
    for axis in axes:
        fields = AXIS_RUNTIME_FIELDS.get(axis, ())
        if row is None:
            statuses.append({"axis": axis, "runtime_fields": list(fields), "field_values": {}, "status": "runtime_not_exercised"})
            continue
        values = {field: _safe_float(row.get(field)) for field in fields}
        if axis in missing_axis_set:
            status = "runtime_required_axis_missing"
        elif not values:
            status = "no_known_runtime_field"
        elif any(value is not None and value > 0.0 for value in values.values()):
            status = "runtime_field_present"
        else:
            status = "research_axis_present_but_runtime_field_zero"
        statuses.append({"axis": axis, "runtime_fields": list(fields), "field_values": values, "status": status})
    return statuses


def _bridge_spec(archetype: str) -> dict[str, Any]:
    return dict(ARCHETYPE_RUNTIME_BRIDGE_SPECS.get(archetype, DEFAULT_RUNTIME_BRIDGE_SPEC))


def _diagnosis(*, coverage_row: dict[str, Any], readiness_row: dict[str, Any] | None, runtime_row: dict[str, str] | None) -> str:
    status = str(coverage_row.get("runtime_gap_status") or "")
    if status == "not_in_current_benchmark":
        if readiness_row and not readiness_row.get("green_retrospective_ready"):
            return "research_green_fixture_not_archived_for_runtime_replay"
        return "research_green_fixture_not_exercised_by_candidate_funnel"
    if status == "runtime_input_evidence_missing":
        return "runtime_candidate_input_evidence_missing_for_bridge"
    if status == "runtime_bridge_axes_missing":
        return "research_signal_not_structured_into_runtime_fields"
    if status == "runtime_stage3_gate_blocked":
        return "weighted_stage3_gate_blocks_after_fields_present"
    if status == "fixture_not_ready":
        return "research_green_not_source_backed_enough_for_runtime_fixture"
    if runtime_row is None:
        return "runtime_candidate_missing"
    return "runtime_needs_manual_review"


def _top_examples(rows: list[dict[str, Any]], limit: int = 3) -> list[dict[str, Any]]:
    ordered = sorted(
        rows,
        key=lambda row: (
            _safe_float(row.get("MFE_180D_pct")) or 0.0,
            str(row.get("entry_date") or row.get("trigger_date") or ""),
        ),
        reverse=True,
    )
    return [_row_view(row) for row in ordered[:limit]]


def build_v12_archetype_signal_runtime_translation_audit(
    *,
    representative_rows: list[dict[str, Any]],
    gap_matrix_payload: dict[str, Any],
    readiness_payload: dict[str, Any],
    runtime_score_rows: list[dict[str, str]],
) -> dict[str, Any]:
    """Build an archetype-level research-signal to runtime-field audit."""

    coverage = _coverage_by_archetype(gap_matrix_payload)
    readiness = _readiness_by_archetype(readiness_payload)
    research_by_archetype = _rows_by_archetype(representative_rows)
    runtime_by_archetype = _runtime_rows_by_archetype(runtime_score_rows)
    rows: list[dict[str, Any]] = []
    for archetype, coverage_row in sorted(coverage.items()):
        clean_green_rows = [row for row in research_by_archetype.get(archetype, []) if _green_fixture_ready(row)]
        raw_green_rows = [row for row in research_by_archetype.get(archetype, []) if _is_raw_green_trigger(row)]
        if not raw_green_rows and not clean_green_rows:
            continue
        required_axes = list(coverage_row.get("required_bridge_axes") or [])
        bridge_spec = _bridge_spec(archetype)
        runtime_row = _runtime_best_row(runtime_by_archetype.get(archetype, []))
        readiness_row = readiness.get(archetype)
        axis_counts = _axis_signal_counts(clean_green_rows or raw_green_rows, required_axes)
        missing_required_axes = list(coverage_row.get("missing_required_bridge_axes") or ())
        axis_statuses = _axis_runtime_status(runtime_row, required_axes, missing_required_axes)
        missing_axis_statuses = [
            item
            for item in axis_statuses
            if item["status"]
            in {
                "runtime_not_exercised",
                "runtime_required_axis_missing",
                "research_axis_present_but_runtime_field_zero",
                "no_known_runtime_field",
            }
        ]
        rows.append(
            {
                "canonical_archetype_id": archetype,
                "large_sector_id": coverage_row.get("large_sector_id"),
                "runtime_bridge_group": bridge_spec.get("runtime_bridge_group"),
                "expected_runtime_primitives": list(bridge_spec.get("expected_runtime_primitives") or ()),
                "required_bridge_axes": required_axes,
                "research_raw_stage3_green_count": len(raw_green_rows),
                "research_clean_green_count": len(clean_green_rows),
                "research_clean_guard_count": coverage_row.get("research_clean_guard_count", 0),
                "research_axis_signal_counts": axis_counts,
                "runtime_gap_status": coverage_row.get("runtime_gap_status"),
                "runtime_candidate_count": coverage_row.get("runtime_candidate_count", 0),
                "runtime_max_score": coverage_row.get("runtime_max_score"),
                "missing_required_bridge_axes": missing_required_axes,
                "root_cause": coverage_row.get("root_cause"),
                "diagnosis": _diagnosis(
                    coverage_row=coverage_row,
                    readiness_row=readiness_row,
                    runtime_row=runtime_row,
                ),
                "fixture_pair_retrospective_ready": bool(readiness_row and readiness_row.get("pair_retrospective_ready")),
                "green_retrospective_ready": bool(readiness_row and readiness_row.get("green_retrospective_ready")),
                "guard_retrospective_ready": bool(readiness_row and readiness_row.get("guard_retrospective_ready")),
                "runtime_best_row": _runtime_view(runtime_row),
                "axis_runtime_status": axis_statuses,
                "untranslated_axis_status": missing_axis_statuses,
                "green_examples": _top_examples(clean_green_rows or raw_green_rows),
                "spec_green_candidate": coverage_row.get("spec_green_candidate"),
                "spec_guard_candidate": coverage_row.get("spec_guard_candidate"),
            }
        )

    diagnosis_counts = Counter(str(row.get("diagnosis")) for row in rows)
    gap_status_counts = Counter(str(row.get("runtime_gap_status")) for row in rows)
    untranslated_axis_counts: Counter[str] = Counter()
    research_axis_counts: Counter[str] = Counter()
    for row in rows:
        for axis, count in row.get("research_axis_signal_counts", {}).items():
            if count:
                research_axis_counts[axis] += int(count)
        untranslated_axis_counts.update(item["axis"] for item in row.get("untranslated_axis_status", []))
    return {
        "schema_version": "v12_archetype_signal_runtime_translation_audit_v1",
        "scope": "accumulated_clean_green_research_signals_to_runtime_fields_by_archetype",
        "archetype_row_count": len(rows),
        "diagnosis_counts": _counter_dict(diagnosis_counts),
        "runtime_gap_status_counts": _counter_dict(gap_status_counts),
        "research_axis_signal_counts": _counter_dict(research_axis_counts),
        "untranslated_axis_counts": _counter_dict(untranslated_axis_counts),
        "rows": rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _join(values: list[Any]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "none"


def _candidate_text(candidate: dict[str, Any] | None) -> str:
    if not candidate:
        return "none"
    return " ".join(
        part
        for part in (
            str(candidate.get("symbol") or "").strip(),
            str(candidate.get("as_of_date") or candidate.get("trigger_date") or "").strip(),
            str(candidate.get("case_id") or "").strip(),
        )
        if part
    ) or "none"


def _axis_status_text(items: list[dict[str, Any]]) -> str:
    if not items:
        return "none"
    return "; ".join(
        "{axis}:{status}:{values}".format(
            axis=item.get("axis"),
            status=item.get("status"),
            values=item.get("field_values") or {},
        )
        for item in items
    )


def _runtime_text(row: dict[str, Any] | None) -> str:
    if row is None:
        return "none"
    return "{symbol}/{date}/{stage}/{score}".format(
        symbol=row.get("symbol"),
        date=row.get("as_of_date"),
        stage=row.get("current_stage"),
        score=row.get("current_score"),
    )


def render_v12_archetype_signal_runtime_translation_audit(payload: dict[str, Any]) -> str:
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Archetype Signal Runtime Translation Audit",
        "",
        "이 문서는 누적 Green 연구 신호가 runtime 후보/필드/Green gate까지 실제로 이어지는지 아키타입별로 점검한다.",
        "HBM 하나를 보정하기 위한 문서가 아니라, C21 금융/C23 바이오/C28 SW 같은 비-HBM 아키타입에도 같은 문제가 있는지 보는 장부다.",
        "",
        "## Summary",
        "",
        f"- archetype_row_count: `{payload.get('archetype_row_count', 0)}`",
        f"- diagnosis_counts: `{payload.get('diagnosis_counts', {})}`",
        f"- runtime_gap_status_counts: `{payload.get('runtime_gap_status_counts', {})}`",
        f"- research_axis_signal_counts: `{payload.get('research_axis_signal_counts', {})}`",
        f"- untranslated_axis_counts: `{payload.get('untranslated_axis_counts', {})}`",
        "",
        "## Archetype Matrix",
        "",
        "| archetype | research Green clean/raw | runtime status | readiness | runtime best | signal axes | untranslated/runtime missing | diagnosis | Green fixture | guard fixture |",
        "| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(
        rows,
        key=lambda item: (
            str(item.get("diagnosis")),
            -int(item.get("research_clean_green_count") or 0),
            str(item.get("canonical_archetype_id")),
        ),
    ):
        green_counts = f"{row.get('research_clean_green_count', 0)}/{row.get('research_raw_stage3_green_count', 0)}"
        readiness = "green={green}, guard={guard}, pair={pair}".format(
            green=row.get("green_retrospective_ready"),
            guard=row.get("guard_retrospective_ready"),
            pair=row.get("fixture_pair_retrospective_ready"),
        )
        runtime_status = "{status}, candidates={count}, max={score}".format(
            status=row.get("runtime_gap_status"),
            count=row.get("runtime_candidate_count", 0),
            score=_fmt(row.get("runtime_max_score")),
        )
        lines.append(
            "| {arch} | {green_counts} | {runtime_status} | {readiness} | {runtime_best} | {axes} | {untranslated} | {diagnosis} | {green} | {guard} |".format(
                arch=row.get("canonical_archetype_id"),
                green_counts=green_counts,
                runtime_status=runtime_status,
                readiness=readiness,
                runtime_best=_runtime_text(row.get("runtime_best_row")),
                axes=row.get("research_axis_signal_counts"),
                untranslated=_axis_status_text(row.get("untranslated_axis_status") or []),
                diagnosis=row.get("diagnosis"),
                green=_candidate_text(row.get("spec_green_candidate")),
                guard=_candidate_text(row.get("spec_guard_candidate")),
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- `research_green_fixture_not_archived_for_runtime_replay`: 연구 Green은 있지만 local official/search/report archive에 Green fixture 입력이 없어 replay가 못 돈다.",
            "- `research_green_fixture_not_exercised_by_candidate_funnel`: 입력은 있거나 만들 수 있지만 current benchmark 후보군이 그 fixture를 점수식까지 보내지 않았다.",
            "- `runtime_candidate_input_evidence_missing_for_bridge`: 후보 row는 있지만 리포트/뉴스/컨센서스/충분한 공시+재무 입력 가족이 부족해 parser 실패인지 아직 판정할 수 없다.",
            "- `research_signal_not_structured_into_runtime_fields`: 후보와 입력은 있지만 연구축이 runtime field에서 0으로 남는다. C10의 customer/backlog/contract 점검이 이 유형이다.",
            "- `weighted_stage3_gate_blocks_after_fields_present`: 필드는 있는데 Green 문턱/비중/gate에서 막힌다. C02 전력기기가 이 유형이다.",
            "- 쉬운 예: C21 삼성화재 Green 연구는 capital return/valuation 신호가 있지만 current benchmark 후보가 0개라 점수 계산을 시험하지 못했다.",
            "- 쉬운 예: C23 유한양행 Green 연구는 FDA approval-to-revenue 신호가 있지만 local replay archive와 후보 funnel이 없어 bio_commercialization field가 평가되지 않았다.",
            "- 쉬운 예: C28 EMRO Green 연구는 ARR/retention/RPO 성격이 핵심인데 current benchmark에 없어서 software_retention field 자체가 검증되지 않았다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_archetype_signal_runtime_translation_audit(
    *,
    representative_rows_path: str | Path,
    gap_matrix_path: str | Path,
    readiness_path: str | Path,
    runtime_score_csv_path: str | Path,
    output_json_path: str | Path,
    output_markdown_path: str | Path,
) -> dict[str, Path]:
    payload = build_v12_archetype_signal_runtime_translation_audit(
        representative_rows=_read_jsonl(representative_rows_path),
        gap_matrix_payload=_read_json(gap_matrix_path),
        readiness_payload=_read_json(readiness_path),
        runtime_score_rows=_read_csv(runtime_score_csv_path),
    )
    json_path = Path(output_json_path)
    markdown_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    markdown_path.write_text(render_v12_archetype_signal_runtime_translation_audit(payload), encoding="utf-8")
    return {"json": json_path, "markdown": markdown_path}
