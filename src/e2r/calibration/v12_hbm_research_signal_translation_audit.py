"""Audit HBM research signals against runtime score fields."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import csv
import json


TRACE_SYMBOLS = ("000660", "005930")
CORE_HBM_ARCHETYPES = {
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
    "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
}
SIGNAL_KEYWORDS = {
    "direct_hbm": ("hbm", "hbm3", "hbm3e", "12-layer", "12 layer", "ai memory", "ai-memory"),
    "named_customer": ("nvidia", "customer", "고객", "allocation", "qualified", "qualification", "supplier"),
    "capacity_lock": ("sold out", "sold-out", "soldout", "booked", "fully booked", "capacity", "capa", "allocation"),
    "order_or_contract": ("order", "contract", "backlog", "supply", "shipment", "shipments", "mass production", "공급"),
    "margin_or_mix": ("asp", "mix", "margin", "opm", "profit", "operating-profit", "영업이익"),
    "revision_or_fcf": ("revision", "eps", "earnings", "fcf", "cash flow", "free cash"),
    "lag_or_guard": ("lag", "failing", "failed", "heat", "power-consumption", "delay", "not pass", "qualification delay"),
}
RUNTIME_FIELDS_FOR_SIGNAL = {
    "named_customer": ("research_axis_bridge_customer",),
    "capacity_lock": ("capa_constraint", "research_axis_bridge_backlog"),
    "order_or_contract": ("research_axis_bridge_contract", "research_axis_bridge_backlog"),
    "margin_or_mix": ("research_axis_bridge_margin", "asp_pricing_power"),
    "revision_or_fcf": ("revision_score", "actual_profit_conversion_score"),
}


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


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


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


def _row_text(row: dict[str, Any]) -> str:
    fields = (
        "symbol",
        "code",
        "company_name",
        "company",
        "canonical_archetype_id",
        "fine_archetype_id",
        "case_id",
        "trigger_id",
        "trigger_type",
        "trigger_outcome_label",
        "current_profile_verdict",
        "evidence_available_at_that_date",
        "evidence_source",
        "raw_source_snippet",
        "source_file",
    )
    return " ".join(str(row.get(field) or "") for field in fields)


def _symbol_for_row(row: dict[str, Any]) -> str | None:
    symbol = str(row.get("symbol") or row.get("code") or "").strip()
    if symbol in TRACE_SYMBOLS:
        return symbol
    text = _row_text(row).lower()
    if "000660" in text or "sk하이닉스" in text or "sk hynix" in text or "hynix" in text:
        return "000660"
    if "005930" in text or "삼성전자" in text or "samsung electronics" in text:
        return "005930"
    return None


def _is_hbm_row(row: dict[str, Any]) -> bool:
    archetype = str(row.get("canonical_archetype_id") or "")
    text = _row_text(row).lower()
    return archetype in CORE_HBM_ARCHETYPES or "hbm" in text or "high bandwidth memory" in text


def _is_raw_green(row: dict[str, Any]) -> bool:
    return "stage3-green" in str(row.get("trigger_type") or "").lower()


def _is_positive_or_green_worthy(row: dict[str, Any]) -> bool:
    if _is_raw_green(row):
        return True
    trigger = str(row.get("trigger_type") or "").lower()
    verdict = str(row.get("current_profile_verdict") or "").lower()
    case_type = str(row.get("case_type") or "").lower()
    mfe_180d = _safe_float(row.get("MFE_180D_pct")) or 0.0
    mae_180d = _safe_float(row.get("MAE_180D_pct"))
    severe_mae = mae_180d is not None and mae_180d <= -35.0
    if "false" in verdict or "counterexample" in case_type or "4c" in trigger:
        return False
    return "stage2-actionable" in trigger and mfe_180d >= 50.0 and not severe_mae


def _signals(row: dict[str, Any]) -> tuple[str, ...]:
    text = _row_text(row).lower()
    found = [
        signal
        for signal, keywords in SIGNAL_KEYWORDS.items()
        if any(keyword.lower() in text for keyword in keywords)
    ]
    return tuple(found)


def _research_view(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "canonical_archetype_id": row.get("canonical_archetype_id"),
        "fine_archetype_id": row.get("fine_archetype_id"),
        "case_id": row.get("case_id"),
        "trigger_id": row.get("trigger_id"),
        "trigger_type": row.get("trigger_type"),
        "trigger_date": row.get("trigger_date"),
        "entry_date": row.get("entry_date"),
        "MFE_180D_pct": row.get("MFE_180D_pct"),
        "MAE_180D_pct": row.get("MAE_180D_pct"),
        "current_profile_verdict": row.get("current_profile_verdict"),
        "source_proxy_only": bool(row.get("source_proxy_only")),
        "evidence_url_pending": bool(row.get("evidence_url_pending")),
        "signals": list(_signals(row)),
        "evidence_available_at_that_date": row.get("evidence_available_at_that_date"),
        "evidence_source": row.get("evidence_source"),
        "source_file": row.get("source_file"),
    }


def _load_runtime_rows(autopsy_directories: list[str | Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for directory in autopsy_directories:
        source_directory = str(Path(directory))
        for row in _read_csv(Path(directory) / "score_components_by_candidate.csv"):
            if str(row.get("symbol") or "") not in TRACE_SYMBOLS:
                continue
            normalized: dict[str, Any] = dict(row)
            normalized["source_directory"] = source_directory
            rows.append(normalized)
    return rows


def _best_runtime_row(rows: list[dict[str, Any]], symbol: str) -> dict[str, Any] | None:
    symbol_rows = [row for row in rows if str(row.get("symbol") or "") == symbol]
    if not symbol_rows:
        return None
    return max(symbol_rows, key=lambda row: _safe_float(row.get("current_score")) or -1.0)


def _runtime_signal_status(runtime_row: dict[str, Any] | None, signal: str) -> dict[str, Any]:
    fields = RUNTIME_FIELDS_FOR_SIGNAL.get(signal, ())
    if runtime_row is None:
        return {"signal": signal, "runtime_fields": list(fields), "field_values": {}, "status": "runtime_row_missing"}
    values = {field: _safe_float(runtime_row.get(field)) for field in fields}
    if not values:
        status = "diagnostic_only"
    elif any(value is not None and value > 0.0 for value in values.values()):
        status = "translated_to_runtime_field"
    else:
        status = "research_signal_present_but_runtime_field_zero"
    return {"signal": signal, "runtime_fields": list(fields), "field_values": values, "status": status}


def _symbol_payload(
    *,
    symbol: str,
    research_rows: list[dict[str, Any]],
    runtime_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    symbol_research = [row for row in research_rows if _symbol_for_row(row) == symbol]
    positive_rows = [row for row in symbol_research if _is_positive_or_green_worthy(row)]
    raw_green_rows = [row for row in symbol_research if _is_raw_green(row)]
    signal_counts: Counter[str] = Counter()
    positive_signal_counts: Counter[str] = Counter()
    for row in symbol_research:
        signal_counts.update(_signals(row))
    for row in positive_rows:
        positive_signal_counts.update(_signals(row))
    runtime_row = _best_runtime_row(runtime_rows, symbol)
    runtime_status = [
        _runtime_signal_status(runtime_row, signal)
        for signal, count in sorted(positive_signal_counts.items())
        if count > 0
    ]
    gap_signals = [
        item["signal"]
        for item in runtime_status
        if item["status"] == "research_signal_present_but_runtime_field_zero"
    ]
    examples = sorted(
        positive_rows,
        key=lambda row: (
            _safe_float(row.get("MFE_180D_pct")) or 0.0,
            str(row.get("entry_date") or row.get("trigger_date") or ""),
        ),
        reverse=True,
    )[:8]
    return {
        "symbol": symbol,
        "company_label": "SK하이닉스" if symbol == "000660" else "삼성전자",
        "research_hbm_row_count": len(symbol_research),
        "research_raw_stage3_green_count": len(raw_green_rows),
        "research_positive_or_green_worthy_count": len(positive_rows),
        "research_signal_counts": _counter_dict(signal_counts),
        "positive_signal_counts": _counter_dict(positive_signal_counts),
        "runtime_best_row": _runtime_view(runtime_row) if runtime_row is not None else None,
        "signal_translation_status": runtime_status,
        "gap_signals": gap_signals,
        "research_examples": [_research_view(row) for row in examples],
    }


def _runtime_view(row: dict[str, Any]) -> dict[str, Any]:
    fields = (
        "symbol",
        "company_name",
        "as_of_date",
        "current_stage",
        "current_score",
        "large_sector_id",
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
        "asp_pricing_power",
        "domain_specific_evidence_score",
        "research_axis_bridge_margin",
        "research_axis_bridge_customer",
        "research_axis_bridge_backlog",
        "research_axis_bridge_contract",
        "research_axis_bridge_valuation_repricing",
        "research_axis_bridge_guard_risk",
        "actual_profit_conversion_score",
        "bottleneck_selected_raw",
        "bottleneck_selected_path",
        "bottleneck_raw_deficit_to_green",
        "stage3_total_deficit",
        "stage3_visibility_deficit",
        "stage3_bottleneck_deficit",
        "stage3_yellow_total_deficit",
        "green_gate_deficit_summary",
        "audit_finding_codes",
        "source_directory",
    )
    return {field: row.get(field) for field in fields}


def build_v12_hbm_research_signal_translation_audit(
    *,
    representative_rows: list[dict[str, Any]],
    autopsy_directories: list[str | Path],
) -> dict[str, Any]:
    """Join accumulated HBM research signals with runtime HBM score fields."""

    hbm_rows = [row for row in representative_rows if _is_hbm_row(row)]
    runtime_rows = _load_runtime_rows(autopsy_directories)
    symbol_rows = [
        _symbol_payload(symbol=symbol, research_rows=hbm_rows, runtime_rows=runtime_rows)
        for symbol in TRACE_SYMBOLS
    ]
    all_gap_signals: Counter[str] = Counter()
    for row in symbol_rows:
        all_gap_signals.update(row["gap_signals"])
    return {
        "schema_version": "v12_hbm_research_signal_translation_audit_v1",
        "scope": "accumulated_hbm_research_rows_vs_runtime_score_fields",
        "filter_rule": "C06-C10 core semiconductor archetypes plus rows whose local text explicitly mentions HBM/high bandwidth memory",
        "hbm_research_row_count": len(hbm_rows),
        "runtime_row_count": len(runtime_rows),
        "hbm_research_archetype_counts": _counter_dict(Counter(str(row.get("canonical_archetype_id") or "") for row in hbm_rows)),
        "hbm_research_trigger_type_counts": _counter_dict(Counter(str(row.get("trigger_type") or "") for row in hbm_rows)),
        "gap_signal_counts": _counter_dict(all_gap_signals),
        "symbol_rows": symbol_rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _join(values: list[Any]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "none"


def _status_text(items: list[dict[str, Any]]) -> str:
    if not items:
        return "none"
    return "; ".join(
        "{signal}:{status}:{values}".format(
            signal=item.get("signal"),
            status=item.get("status"),
            values=item.get("field_values") or {},
        )
        for item in items
    )


def _top_counts(counts: dict[str, int], limit: int = 20) -> dict[str, int]:
    return dict(sorted(counts.items(), key=lambda item: (-int(item[1]), item[0]))[:limit])


def _runtime_text(row: dict[str, Any] | None) -> str:
    if row is None:
        return "none"
    return "{stage}/{score}/{arch}; bridge m,c,b,k={margin}/{customer}/{backlog}/{contract}; capa={capa}; deficit={deficit}".format(
        stage=row.get("current_stage"),
        score=row.get("current_score"),
        arch=row.get("canonical_archetype_id"),
        margin=row.get("research_axis_bridge_margin"),
        customer=row.get("research_axis_bridge_customer"),
        backlog=row.get("research_axis_bridge_backlog"),
        contract=row.get("research_axis_bridge_contract"),
        capa=row.get("capa_constraint"),
        deficit=row.get("green_gate_deficit_summary"),
    )


def render_v12_hbm_research_signal_translation_audit(payload: dict[str, Any]) -> str:
    lines = [
        "# V12 HBM Research Signal Translation Audit",
        "",
        "이 문서는 누적 HBM 연구 row가 runtime score field로 어떻게 번역됐는지 점검한다.",
        "삼전/하닉 전용 보너스가 아니라, 연구 신호가 source-backed primitive로 변환되는지 보는 전 아키타입 문제의 샘플이다.",
        "",
        "## Summary",
        "",
        f"- filter_rule: `{payload.get('filter_rule', '')}`",
        f"- hbm_research_row_count: `{payload.get('hbm_research_row_count', 0)}`",
        f"- runtime_row_count: `{payload.get('runtime_row_count', 0)}`",
        f"- hbm_research_archetype_counts: `{payload.get('hbm_research_archetype_counts', {})}`",
        f"- hbm_research_trigger_type_counts_top20: `{_top_counts(payload.get('hbm_research_trigger_type_counts', {}))}`",
        f"- gap_signal_counts: `{payload.get('gap_signal_counts', {})}`",
        "",
        "## Symbol Translation",
        "",
        "| symbol | research rows | raw Green | positive/green-worthy | positive signals | best runtime row | translation gaps | signal status |",
        "| --- | ---: | ---: | ---: | --- | --- | --- | --- |",
    ]
    for row in payload.get("symbol_rows", []):
        lines.append(
            "| {symbol} {label} | {rows} | {green} | {positive} | {signals} | {runtime} | {gaps} | {status} |".format(
                symbol=row.get("symbol"),
                label=row.get("company_label"),
                rows=row.get("research_hbm_row_count", 0),
                green=row.get("research_raw_stage3_green_count", 0),
                positive=row.get("research_positive_or_green_worthy_count", 0),
                signals=row.get("positive_signal_counts"),
                runtime=_runtime_text(row.get("runtime_best_row")),
                gaps=_join(row.get("gap_signals") or []),
                status=_status_text(row.get("signal_translation_status") or []),
            )
        )
    lines.extend(
        [
            "",
            "## Research Examples",
            "",
            "| symbol | trigger | date | MFE/MAE 180D | signals | verdict | evidence |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for symbol_row in payload.get("symbol_rows", []):
        for example in symbol_row.get("research_examples", []):
            evidence = str(example.get("evidence_available_at_that_date") or example.get("evidence_source") or "")
            if len(evidence) > 180:
                evidence = evidence[:177] + "..."
            lines.append(
                "| {symbol} | {trigger} | {date} | {mfe}/{mae} | {signals} | {verdict} | {evidence} |".format(
                    symbol=symbol_row.get("symbol"),
                    trigger=example.get("trigger_type"),
                    date=example.get("entry_date") or example.get("trigger_date"),
                    mfe=example.get("MFE_180D_pct"),
                    mae=example.get("MAE_180D_pct"),
                    signals=_join(example.get("signals") or []),
                    verdict=example.get("current_profile_verdict"),
                    evidence=evidence.replace("|", "/"),
                )
            )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 하닉은 누적 연구 row가 HBM customer/capacity/order/revision 신호를 여러 번 잡았다.",
            "- runtime도 하닉의 EPS/FCF, revision, customer/backlog/contract bridge를 강하게 반영하지만, Green은 weighted total/bottleneck gate까지 통과해야 한다.",
            "- 삼성은 연구 장부에서도 direct customer lock보다 HBM qualification lag/catch-up 성격이 강하다. 그래서 C06 Green이 아니라 C10 memory recovery로 라우팅되고 customer/backlog/contract bridge가 약하게 남는다.",
            "- 쉬운 예: 연구 문장에 '2024 HBM capacity sold out'이 있어도 runtime field와 Green gate를 positive/guard 쌍으로 검증해야 한다.",
            "- 같은 패턴을 C21/C23/C28에 적용하면 capital return, approval-to-commercialization, retention/RPO 같은 연구 신호가 runtime primitive로 살아나는지 봐야 한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_hbm_research_signal_translation_audit(
    *,
    representative_rows_path: str | Path,
    autopsy_directories: list[str | Path],
    output_json_path: str | Path,
    output_markdown_path: str | Path,
) -> dict[str, Path]:
    payload = build_v12_hbm_research_signal_translation_audit(
        representative_rows=_read_jsonl(representative_rows_path),
        autopsy_directories=autopsy_directories,
    )
    json_path = Path(output_json_path)
    md_path = Path(output_markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_hbm_research_signal_translation_audit(payload), encoding="utf-8")
    return {"json": json_path, "markdown": md_path}
