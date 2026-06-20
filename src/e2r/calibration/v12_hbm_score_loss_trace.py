"""Trace the HBM case study inside the broader v12 score-loss problem."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import csv
import json


TRACE_SYMBOLS = ("000660", "005930")
TRACE_COLUMNS = (
    "symbol",
    "company_name",
    "as_of_date",
    "current_stage",
    "current_score",
    "canonical_archetype_id",
    "sector_profile",
    "archetype_component_eps_fcf_explosion",
    "archetype_component_earnings_visibility",
    "archetype_component_bottleneck_pricing",
    "archetype_component_market_mispricing",
    "archetype_component_valuation_rerating",
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


def _compact_row(row: dict[str, str], source_directory: str) -> dict[str, Any]:
    compact = {key: row.get(key) for key in TRACE_COLUMNS}
    compact["source_directory"] = source_directory
    return compact


def _gate_failed(row: dict[str, str]) -> list[str]:
    return [
        key
        for key, value in row.items()
        if key.startswith("failed_") and str(value).strip().lower() in {"1", "1.0", "true", "yes"}
    ]


def _score_key(row: dict[str, Any]) -> tuple[str, str]:
    return (str(row.get("symbol") or ""), str(row.get("as_of_date") or ""))


def _spec_rows_by_symbol(spec_payload: dict[str, Any], symbol: str) -> list[dict[str, Any]]:
    rows = []
    for row in spec_payload.get("rows", []):
        candidate = row.get("candidate") or {}
        if str(candidate.get("symbol") or "") == symbol:
            rows.append(row)
    return rows


def build_v12_hbm_score_loss_trace(
    *,
    spec_payload: dict[str, Any],
    autopsy_directories: list[str | Path],
) -> dict[str, Any]:
    """Build a Samsung/Hynix case trace from refreshed autopsy CSVs.

    This is a diagnostic case study, not an HBM-specific scoring bonus.
    """

    score_rows: list[dict[str, Any]] = []
    gate_rows_by_key: dict[tuple[str, str], dict[str, str]] = {}
    for directory in autopsy_directories:
        directory_path = Path(directory)
        source_name = str(directory_path)
        score_csv = directory_path / "score_components_by_candidate.csv"
        gate_csv = directory_path / "stage_gate_matrix.csv"
        for gate in _read_csv(gate_csv):
            gate_rows_by_key[(str(gate.get("symbol") or ""), str(gate.get("as_of_date") or ""))] = gate
        for row in _read_csv(score_csv):
            if str(row.get("symbol") or "") in TRACE_SYMBOLS:
                compact = _compact_row(row, source_name)
                gate = gate_rows_by_key.get(_score_key(compact), {})
                compact["failed_gates"] = _gate_failed(gate)
                score_rows.append(compact)

    by_symbol = {symbol: [row for row in score_rows if row["symbol"] == symbol] for symbol in TRACE_SYMBOLS}
    sk_rows = by_symbol.get("000660", [])
    samsung_rows = by_symbol.get("005930", [])
    max_sk_score = max((_safe_float(row.get("current_score")) or 0.0 for row in sk_rows), default=0.0)
    max_samsung_score = max((_safe_float(row.get("current_score")) or 0.0 for row in samsung_rows), default=0.0)
    return {
        "schema_version": "v12_hbm_score_loss_trace_v1",
        "autopsy_directories": [str(Path(path)) for path in autopsy_directories],
        "trace_symbols": list(TRACE_SYMBOLS),
        "spec_green_rows_000660": _spec_rows_by_symbol(spec_payload, "000660"),
        "spec_rows_005930": _spec_rows_by_symbol(spec_payload, "005930"),
        "runtime_rows": score_rows,
        "summary": {
            "sk_hynix_runtime_row_count": len(sk_rows),
            "samsung_runtime_row_count": len(samsung_rows),
            "sk_hynix_max_score": round(max_sk_score, 4),
            "samsung_max_score": round(max_samsung_score, 4),
            "sk_hynix_common_loss": "bridge_fields_present_but_weighted_gate_still_short",
            "samsung_common_loss": "c10_memory_recovery_customer_backlog_contract_bridge_still_weak",
        },
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def render_v12_hbm_score_loss_trace(payload: dict[str, Any]) -> str:
    rows = list(payload.get("runtime_rows", []))
    lines = [
        "# V12 HBM Case Score Loss Trace",
        "",
        "이 문서는 HBM 과적합 패치가 아니라 전체 score-loss 문제를 설명하는 케이스 스터디다.",
        "C06 HBM 대표 Green/guard spec과 최신 HBM as-of autopsy를 직접 연결해 bridge field와 gate가 어디서 막히는지 보여준다.",
        "핵심은 하닉 전망이 무시된 것이 아니라, bridge field가 채워진 뒤에도 weighted Green gate 검증이 남는다는 점이다.",
        "",
        "## Summary",
        "",
    ]
    for key, value in payload.get("summary", {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Runtime Rows",
            "",
            "| symbol | name | as-of | stage | score | archetype | EPS/FCF | visibility | bottleneck | revision | bridge margin/customer/backlog/contract | raw bottleneck | deficits | failed gates |",
            "| --- | --- | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |",
        ]
    )
    for row in sorted(rows, key=lambda item: (str(item.get("as_of_date")), str(item.get("symbol")))):
        bridge = "/".join(
            _fmt(row.get(key))
            for key in (
                "research_axis_bridge_margin",
                "research_axis_bridge_customer",
                "research_axis_bridge_backlog",
                "research_axis_bridge_contract",
            )
        )
        raw_bottleneck = "{raw} via {path}, raw deficit {deficit}".format(
            raw=_fmt(row.get("bottleneck_selected_raw")),
            path=_fmt(row.get("bottleneck_selected_path")),
            deficit=_fmt(row.get("bottleneck_raw_deficit_to_green")),
        )
        deficits = _fmt(row.get("green_gate_deficit_summary"))
        failed = ", ".join(row.get("failed_gates") or [])
        lines.append(
            "| {symbol} | {name} | {asof} | {stage} | {score} | {arch} | {eps} | {vis} | {bottleneck} | {revision} | {bridge} | {raw_bottleneck} | {deficits} | {failed} |".format(
                symbol=_fmt(row.get("symbol")),
                name=_fmt(row.get("company_name")),
                asof=_fmt(row.get("as_of_date")),
                stage=_fmt(row.get("current_stage")),
                score=_fmt(row.get("current_score")),
                arch=_fmt(row.get("canonical_archetype_id")),
                eps=_fmt(row.get("archetype_component_eps_fcf_explosion")),
                vis=_fmt(row.get("archetype_component_earnings_visibility")),
                bottleneck=_fmt(row.get("archetype_component_bottleneck_pricing")),
                revision=_fmt(row.get("revision_score")),
                bridge=bridge,
                raw_bottleneck=raw_bottleneck,
                deficits=deficits,
                failed=failed,
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 하닉: `revision_score=100`, EPS/FCF component는 `24`로 강하게 반영됐다.",
            "- 하닉: backlog/contract bridge가 채워진 뒤에도 total/bottleneck gate가 Green 필요치까지는 아직 부족하다.",
            "- 삼성: margin/valuation은 잡히지만 customer/backlog/contract bridge가 약하고, route도 C06 Green이 아니라 C10 memory recovery로 남는다.",
            "- 따라서 해결은 HBM 이름 가산이 아니라, source-backed bridge field와 weighted gate를 positive/guard 쌍으로 함께 검증하는 것이다.",
            "- 같은 방식으로 C21 금융은 capital return, C23 바이오는 commercialization, C28 SW는 retention/RPO가 runtime primitive로 살아나는지 봐야 한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_hbm_score_loss_trace(
    *,
    spec_path: str | Path,
    autopsy_directories: list[str | Path],
    output_json_path: str | Path,
    output_markdown_path: str | Path,
) -> dict[str, Path]:
    payload = build_v12_hbm_score_loss_trace(
        spec_payload=_read_json(spec_path),
        autopsy_directories=autopsy_directories,
    )
    json_path = Path(output_json_path)
    md_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_hbm_score_loss_trace(payload), encoding="utf-8")
    return {"json": json_path, "markdown": md_path}
