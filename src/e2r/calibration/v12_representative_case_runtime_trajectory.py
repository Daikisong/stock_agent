"""Audit representative runtime trajectories without creating HBM-specific fixes."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping
import csv
import json


DEFAULT_AUTOPSY_DIRECTORIES = (
    Path("output/0619_asof_stage_promotion_hbm_2024_04_25"),
    Path("output/0619_asof_stage_promotion_hbm_2024_04_26"),
    Path("output/0619_asof_stage_promotion_hbm_2024_04_30"),
    Path("output/0619_asof_stage_promotion_benchmark_current_2023_2026"),
)
DEFAULT_CROSS_ARCHETYPE_TRACE_PATH = Path(
    "docs/0619/v12_cross_archetype_score_loss_trace_2026-06-19.json"
)
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_representative_case_runtime_trajectory_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_representative_case_runtime_trajectory_2026-06-19.md")


REPRESENTATIVE_SYMBOLS = ("000660", "005930")
RUNTIME_TRACE_COLUMNS = (
    "symbol",
    "company_name",
    "as_of_date",
    "current_stage",
    "current_score",
    "score_valid",
    "score_blocked_reason",
    "large_sector_id",
    "canonical_archetype_id",
    "sector_profile",
    "archetype_component_eps_fcf_explosion",
    "archetype_component_earnings_visibility",
    "archetype_component_bottleneck_pricing",
    "archetype_component_market_mispricing",
    "archetype_component_valuation_rerating",
    "archetype_component_capital_allocation",
    "archetype_component_information_confidence",
    "revision_score",
    "contract_quality",
    "backlog_rpo_visibility",
    "capa_constraint",
    "domain_specific_evidence_score",
    "actual_profit_conversion_score",
    "research_axis_bridge_margin",
    "research_axis_bridge_customer",
    "research_axis_bridge_backlog",
    "research_axis_bridge_contract",
    "research_axis_bridge_valuation_repricing",
    "bottleneck_selected_raw",
    "bottleneck_selected_path",
    "bottleneck_raw_deficit_to_green",
    "stage3_total_deficit",
    "stage3_visibility_deficit",
    "stage3_bottleneck_deficit",
    "green_gate_deficit_summary",
)
ZERO_IMPORTANT_FIELDS = (
    "research_axis_bridge_customer",
    "research_axis_bridge_backlog",
    "research_axis_bridge_contract",
    "contract_quality",
    "backlog_rpo_visibility",
    "capa_constraint",
)


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


def _is_zero(value: Any) -> bool:
    number = _safe_float(value)
    return number is not None and number == 0.0


def _failed_gates(row: Mapping[str, Any]) -> list[str]:
    return [
        key
        for key, value in row.items()
        if key.startswith("failed_") and str(value).strip().lower() in {"1", "1.0", "true", "yes"}
    ]


def _trace_key(row: Mapping[str, Any]) -> tuple[str, str, str, str, str]:
    return (
        str(row.get("symbol") or ""),
        str(row.get("as_of_date") or ""),
        str(row.get("current_stage") or ""),
        str(row.get("current_score") or ""),
        str(row.get("canonical_archetype_id") or ""),
    )


def _compact_score_row(row: Mapping[str, str]) -> dict[str, Any]:
    return {column: row.get(column) for column in RUNTIME_TRACE_COLUMNS}


def _zero_important_fields(row: Mapping[str, Any]) -> list[str]:
    return [field for field in ZERO_IMPORTANT_FIELDS if _is_zero(row.get(field))]


def _diagnostic_bucket(row: Mapping[str, Any]) -> str:
    symbol = str(row.get("symbol") or "")
    zero_fields = set(row.get("zero_important_fields") or ())
    if symbol == "005930":
        return "route_and_bridge_gap"
    if {"research_axis_bridge_backlog", "research_axis_bridge_contract", "capa_constraint"} & zero_fields:
        return "parser_feature_bridge_gap"
    if "failed_stage3_total_score" in set(row.get("failed_gates") or ()):
        return "weighted_stage_gate_gap"
    return "runtime_needs_review"


def _plain_case_reading(symbol: str, summary: Mapping[str, Any]) -> str:
    persistent_zero = ", ".join(summary.get("persistent_zero_important_fields") or ()) or "none"
    first = summary.get("first_stage_score")
    last = summary.get("last_stage_score")
    best = f"{summary.get('max_score_stage')}/{summary.get('max_score')} on {summary.get('max_score_as_of_date')}"
    route_counts = summary.get("archetype_route_counts")
    if symbol == "000660":
        return (
            f"하닉은 첫 row {first}, 최고점 {best}, 마지막 row {last}이고 어느 시점에도 Green이 아니다. "
            f"route 분포는 {route_counts}이며, 반복적으로 비는 field는 {persistent_zero}다. "
            "즉 EPS/revision을 못 본 문제가 아니라 bridge field가 채워진 뒤에도 weighted gate까지 검증해야 하는 문제다."
        )
    if symbol == "005930":
        return (
            f"삼성은 첫 row {first}, 최고점 {best}이고 C06 direct Green이 아니라 C10 회복 경로다. "
            f"반복적으로 비는 field는 {persistent_zero}다. 그래서 모든 HBM/반도체를 Green으로 올리는 보정은 오답이다."
        )
    return "대표 사례의 runtime field, route, gate를 같이 확인해야 한다."


def _summarize_symbol(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return {
            "row_count": 0,
            "reaches_stage3_green": False,
            "persistent_zero_important_fields": [],
        }
    ordered = sorted(rows, key=lambda row: str(row.get("as_of_date") or ""))
    scores = [(_safe_float(row.get("current_score")) or 0.0, row) for row in ordered]
    max_score, best_row = max(scores, key=lambda item: item[0])
    failed_counts: Counter[str] = Counter()
    route_counts: Counter[str] = Counter()
    for row in ordered:
        failed_counts.update(row.get("failed_gates") or ())
        route_counts[str(row.get("canonical_archetype_id") or "unknown")] += 1
    field_sets = [set(row.get("zero_important_fields") or ()) for row in ordered]
    persistent_zero = sorted(set.intersection(*field_sets)) if field_sets else []
    first = ordered[0]
    last = ordered[-1]
    symbol = str(first.get("symbol") or "")
    summary = {
        "symbol": symbol,
        "company_name": first.get("company_name"),
        "row_count": len(ordered),
        "first_as_of_date": first.get("as_of_date"),
        "first_stage_score": f"{first.get('current_stage')}/{first.get('current_score')}",
        "last_as_of_date": last.get("as_of_date"),
        "last_stage_score": f"{last.get('current_stage')}/{last.get('current_score')}",
        "max_score": round(max_score, 4),
        "max_score_as_of_date": best_row.get("as_of_date"),
        "max_score_stage": best_row.get("current_stage"),
        "best_archetype": best_row.get("canonical_archetype_id"),
        "reaches_stage3_green": any(str(row.get("current_stage")) == "3-Green" for row in ordered),
        "persistent_zero_important_fields": persistent_zero,
        "top_failed_gates": dict(failed_counts.most_common(5)),
        "archetype_route_counts": dict(route_counts.most_common()),
        "diagnostic_buckets": dict(Counter(str(row.get("diagnostic_bucket")) for row in ordered)),
    }
    summary["plain_reading"] = _plain_case_reading(symbol, summary)
    return summary


def _is_hbm_related_archetype(archetype: str) -> bool:
    upper = archetype.upper()
    return "HBM" in upper or "MEMORY" in upper


def _cross_archetype_summary(cross_trace_payload: Mapping[str, Any]) -> dict[str, Any]:
    rows = [dict(row) for row in cross_trace_payload.get("rows", []) or []]
    non_hbm_rows = [
        row for row in rows if not _is_hbm_related_archetype(str(row.get("canonical_archetype_id") or ""))
    ]
    non_hbm_layer_counts = Counter(str(row.get("loss_layer") or "unknown") for row in non_hbm_rows)
    non_hbm_status_counts = Counter(str(row.get("runtime_gap_status") or "unknown") for row in non_hbm_rows)
    non_hbm_missing_axes: Counter[str] = Counter()
    for row in non_hbm_rows:
        non_hbm_missing_axes.update(str(axis) for axis in row.get("missing_required_bridge_axes") or ())
    return {
        "ready_archetype_count": cross_trace_payload.get("ready_archetype_count", len(rows)),
        "spec_row_count": cross_trace_payload.get("spec_row_count"),
        "loss_layer_counts_by_archetype": cross_trace_payload.get("loss_layer_counts_by_archetype", {}),
        "gap_status_counts_by_archetype": cross_trace_payload.get("gap_status_counts_by_archetype", {}),
        "missing_required_bridge_axis_counts": cross_trace_payload.get("missing_required_bridge_axis_counts", {}),
        "non_hbm_archetype_count": len(non_hbm_rows),
        "non_hbm_loss_layer_counts": dict(sorted(non_hbm_layer_counts.items())),
        "non_hbm_gap_status_counts": dict(sorted(non_hbm_status_counts.items())),
        "non_hbm_missing_required_bridge_axis_counts": dict(sorted(non_hbm_missing_axes.items())),
        "sample_non_hbm_rows": [
            {
                "canonical_archetype_id": row.get("canonical_archetype_id"),
                "runtime_gap_status": row.get("runtime_gap_status"),
                "loss_layer": row.get("loss_layer"),
                "runtime_candidate_count": row.get("runtime_candidate_count"),
                "runtime_max_score": row.get("runtime_max_score"),
                "missing_required_bridge_axes": list(row.get("missing_required_bridge_axes") or ()),
                "simple_explanation": row.get("simple_explanation"),
                "next_action": row.get("next_action"),
            }
            for row in non_hbm_rows[:10]
        ],
    }


def build_v12_representative_case_runtime_trajectory(
    *,
    autopsy_directories: list[str | Path] | tuple[str | Path, ...] = DEFAULT_AUTOPSY_DIRECTORIES,
    cross_trace_payload: Mapping[str, Any] | None = None,
    cross_trace_path: str | Path = DEFAULT_CROSS_ARCHETYPE_TRACE_PATH,
) -> dict[str, Any]:
    """Build a representative case trajectory and cross-archetype guard.

    Samsung/SK Hynix are used only as visible examples. The acceptance rule is
    intentionally cross-archetype: non-HBM fixture rows must improve through the
    same candidate/archive, parser-feature, and gate layers.
    """

    merged_rows: dict[tuple[str, str, str, str, str], dict[str, Any]] = {}
    gate_rows_by_key: dict[tuple[str, str], dict[str, str]] = {}
    for directory in autopsy_directories:
        directory_path = Path(directory)
        for gate_row in _read_csv(directory_path / "stage_gate_matrix.csv"):
            gate_rows_by_key[(str(gate_row.get("symbol") or ""), str(gate_row.get("as_of_date") or ""))] = gate_row
        for score_row in _read_csv(directory_path / "score_components_by_candidate.csv"):
            if str(score_row.get("symbol") or "") not in REPRESENTATIVE_SYMBOLS:
                continue
            compact = _compact_score_row(score_row)
            gate_row = gate_rows_by_key.get((str(compact.get("symbol") or ""), str(compact.get("as_of_date") or "")), {})
            compact["failed_gates"] = _failed_gates(gate_row)
            compact["zero_important_fields"] = _zero_important_fields(compact)
            compact["source_directories"] = [str(directory_path)]
            compact["diagnostic_bucket"] = _diagnostic_bucket(compact)
            key = _trace_key(compact)
            if key in merged_rows:
                merged_rows[key]["source_directories"] = sorted(
                    set(merged_rows[key].get("source_directories") or ()) | {str(directory_path)}
                )
            else:
                merged_rows[key] = compact

    runtime_rows = sorted(
        merged_rows.values(),
        key=lambda row: (str(row.get("symbol") or ""), str(row.get("as_of_date") or "")),
    )
    rows_by_symbol: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in runtime_rows:
        rows_by_symbol[str(row.get("symbol") or "")].append(row)
    symbol_summaries = {
        symbol: _summarize_symbol(rows_by_symbol.get(symbol, [])) for symbol in REPRESENTATIVE_SYMBOLS
    }
    cross_summary = _cross_archetype_summary(cross_trace_payload or _read_json(cross_trace_path))
    return {
        "schema_version": "v12_representative_case_runtime_trajectory_v1",
        "scope": "representative_symbol_trajectory_plus_cross_archetype_guard",
        "scoring_policy": "diagnostic_only_no_hbm_or_symbol_bonus",
        "representative_symbols": list(REPRESENTATIVE_SYMBOLS),
        "autopsy_directories": [str(Path(path)) for path in autopsy_directories],
        "summary": {
            "plain_answer": (
                "삼전/하닉은 HBM 과적합 대상이 아니라 전체 아키타입 evidence-to-runtime 변환 실패를 "
                "눈에 보이게 하는 대표 사례다."
            ),
            "runtime_trajectory_row_count": len(runtime_rows),
            "symbol_reaches_stage3_green_count": sum(
                1 for row in symbol_summaries.values() if row.get("reaches_stage3_green")
            ),
            "representative_case_diagnostic_bucket_counts": dict(
                Counter(str(row.get("diagnostic_bucket") or "unknown") for row in runtime_rows)
            ),
            "cross_archetype_ready_count": cross_summary.get("ready_archetype_count"),
            "cross_archetype_non_hbm_count": cross_summary.get("non_hbm_archetype_count"),
            "cross_archetype_loss_layer_counts": cross_summary.get("loss_layer_counts_by_archetype"),
            "non_hbm_loss_layer_counts": cross_summary.get("non_hbm_loss_layer_counts"),
            "generalization_guard": (
                "하닉만 Green이 되거나 삼성까지 무조건 Green이 되는 패치는 실패다. "
                "C21/C23/C26 등 비-HBM row도 같은 replay/field/gate 기준으로 통과해야 한다."
            ),
        },
        "symbol_summaries": symbol_summaries,
        "runtime_rows": runtime_rows,
        "cross_archetype_summary": cross_summary,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _join(values: list[Any] | tuple[Any, ...]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "none"


def render_v12_representative_case_runtime_trajectory(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    cross_summary = payload.get("cross_archetype_summary", {})
    lines = [
        "# V12 Representative Case Runtime Trajectory",
        "",
        "이 문서는 하닉/삼성을 HBM 특례로 올리기 위한 문서가 아니다.",
        "두 종목을 눈에 잘 보이는 대표 사례로 놓고, 전 아키타입에서 같은 문제가 생기는지 확인한다.",
        "",
        "## Summary",
        "",
        f"- plain_answer: {summary.get('plain_answer')}",
        f"- scoring_policy: `{payload.get('scoring_policy')}`",
        f"- runtime_trajectory_row_count: `{summary.get('runtime_trajectory_row_count')}`",
        f"- symbol_reaches_stage3_green_count: `{summary.get('symbol_reaches_stage3_green_count')}`",
        f"- representative_case_diagnostic_bucket_counts: `{summary.get('representative_case_diagnostic_bucket_counts')}`",
        f"- cross_archetype_ready_count: `{summary.get('cross_archetype_ready_count')}`",
        f"- cross_archetype_non_hbm_count: `{summary.get('cross_archetype_non_hbm_count')}`",
        f"- cross_archetype_loss_layer_counts: `{summary.get('cross_archetype_loss_layer_counts')}`",
        f"- non_hbm_loss_layer_counts: `{summary.get('non_hbm_loss_layer_counts')}`",
        f"- generalization_guard: {summary.get('generalization_guard')}",
        "",
        "## Representative Symbol Summary",
        "",
        "| symbol | rows | first | last | max | reaches Green | route counts | persistent zero fields | top failed gates | reading |",
        "| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for symbol, row in (payload.get("symbol_summaries") or {}).items():
        lines.append(
            "| {symbol} {name} | {rows} | {first_date} {first} | {last_date} {last} | {max_score} {max_date} {max_stage} | {green} | {routes} | {zero} | {gates} | {reading} |".format(
                symbol=symbol,
                name=_fmt(row.get("company_name")),
                rows=row.get("row_count", 0),
                first_date=_fmt(row.get("first_as_of_date")),
                first=_fmt(row.get("first_stage_score")),
                last_date=_fmt(row.get("last_as_of_date")),
                last=_fmt(row.get("last_stage_score")),
                max_score=_fmt(row.get("max_score")),
                max_date=_fmt(row.get("max_score_as_of_date")),
                max_stage=_fmt(row.get("max_score_stage")),
                green=_fmt(row.get("reaches_stage3_green")),
                routes=row.get("archetype_route_counts"),
                zero=_join(row.get("persistent_zero_important_fields") or ()),
                gates=row.get("top_failed_gates"),
                reading=row.get("plain_reading"),
            )
        )

    lines.extend(
        [
            "",
            "## Representative Runtime Rows",
            "",
            "| symbol | as-of | stage | score | archetype | EPS/FCF | visibility | bottleneck | revision | bridge m/c/b/k | zero fields | failed gates | deficit | sources |",
            "| --- | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload.get("runtime_rows", []) or []:
        bridge = "/".join(
            _fmt(row.get(key))
            for key in (
                "research_axis_bridge_margin",
                "research_axis_bridge_customer",
                "research_axis_bridge_backlog",
                "research_axis_bridge_contract",
            )
        )
        lines.append(
            "| {symbol} | {asof} | {stage} | {score} | {arch} | {eps} | {visibility} | {bottleneck} | {revision} | {bridge} | {zero} | {failed} | {deficit} | {sources} |".format(
                symbol=_fmt(row.get("symbol")),
                asof=_fmt(row.get("as_of_date")),
                stage=_fmt(row.get("current_stage")),
                score=_fmt(row.get("current_score")),
                arch=_fmt(row.get("canonical_archetype_id")),
                eps=_fmt(row.get("archetype_component_eps_fcf_explosion")),
                visibility=_fmt(row.get("archetype_component_earnings_visibility")),
                bottleneck=_fmt(row.get("archetype_component_bottleneck_pricing")),
                revision=_fmt(row.get("revision_score")),
                bridge=bridge,
                zero=_join(row.get("zero_important_fields") or ()),
                failed=_join(row.get("failed_gates") or ()),
                deficit=_fmt(row.get("green_gate_deficit_summary")),
                sources=_join(row.get("source_directories") or ()),
            )
        )

    lines.extend(
        [
            "",
            "## Cross-Archetype Guard",
            "",
            f"- ready_archetype_count: `{cross_summary.get('ready_archetype_count')}`",
            f"- non_hbm_archetype_count: `{cross_summary.get('non_hbm_archetype_count')}`",
            f"- non_hbm_loss_layer_counts: `{cross_summary.get('non_hbm_loss_layer_counts')}`",
            f"- non_hbm_gap_status_counts: `{cross_summary.get('non_hbm_gap_status_counts')}`",
            f"- non_hbm_missing_required_bridge_axis_counts: `{cross_summary.get('non_hbm_missing_required_bridge_axis_counts')}`",
            "",
            "| sample non-HBM archetype | status | layer | candidates | max score | missing axes | next action |",
            "| --- | --- | --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in cross_summary.get("sample_non_hbm_rows", []) or []:
        lines.append(
            "| {arch} | {status} | {layer} | {count} | {score} | {axes} | {next_action} |".format(
                arch=row.get("canonical_archetype_id"),
                status=row.get("runtime_gap_status"),
                layer=row.get("loss_layer"),
                count=row.get("runtime_candidate_count"),
                score=_fmt(row.get("runtime_max_score")),
                axes=_join(row.get("missing_required_bridge_axes") or ()),
                next_action=row.get("next_action"),
            )
        )

    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 하닉 예: 2024-04-25에 76점대 Yellow였고 이후에도 Green은 아니다. bridge field가 채워져도 total/bottleneck gate를 통과해야 Green이 된다.",
            "- 삼성 예: C06 direct Green이 아니라 C10 회복 경로다. 그래서 하닉을 보려고 만든 보정이 삼성을 무조건 Green으로 올리면 guard가 무너진 것이다.",
            "- 전체 예: C21 금융, C23 바이오, C26 플랫폼은 HBM이 아닌데도 후보 archive, field 번역, gate 검증 중 하나에서 막힌다.",
            "- 쉬운 비유: 하닉/삼성은 예제 문제다. 답을 외우면 안 되고, 답안지 입력칸과 채점 기준을 모든 단원에 맞게 고쳐야 한다.",
            "",
            "## Repair Acceptance",
            "",
            "- HBM 이름, 삼성/하닉 종목명, 과거 승자 여부로 점수를 더하지 않는다.",
            "- 누적 연구축은 source-backed primitive field로 번역될 때만 점수 재료가 된다.",
            "- positive row와 guard row를 같은 아키타입에서 같이 replay한다.",
            "- 비-HBM row도 같은 기준으로 개선되어야 첫 repair가 통과한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_representative_case_runtime_trajectory(
    *,
    autopsy_directories: list[str | Path] | tuple[str | Path, ...] = DEFAULT_AUTOPSY_DIRECTORIES,
    cross_trace_path: str | Path = DEFAULT_CROSS_ARCHETYPE_TRACE_PATH,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_representative_case_runtime_trajectory(
        autopsy_directories=autopsy_directories,
        cross_trace_path=cross_trace_path,
    )
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_representative_case_runtime_trajectory(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_representative_case_runtime_trajectory()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
