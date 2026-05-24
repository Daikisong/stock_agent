"""Parsers for generated Stock-Web historical calibration Markdown files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
import io
import json
import re
from typing import Any

from .md_discovery import MarkdownDocument


COLUMN_ALIASES = {
    "MFE30": "MFE_30D_pct",
    "MFE_30D": "MFE_30D_pct",
    "MFE_30D_pct": "MFE_30D_pct",
    "MFE90": "MFE_90D_pct",
    "MFE_90D": "MFE_90D_pct",
    "MFE_90D_pct": "MFE_90D_pct",
    "MFE180": "MFE_180D_pct",
    "MFE_180D": "MFE_180D_pct",
    "MFE_180D_pct": "MFE_180D_pct",
    "MAE30": "MAE_30D_pct",
    "MAE_30D": "MAE_30D_pct",
    "MAE_30D_pct": "MAE_30D_pct",
    "MAE90": "MAE_90D_pct",
    "MAE_90D": "MAE_90D_pct",
    "MAE_90D_pct": "MAE_90D_pct",
    "MAE180": "MAE_180D_pct",
    "MAE_180D": "MAE_180D_pct",
    "MAE_180D_pct": "MAE_180D_pct",
    "type": "trigger_type",
    "trigger": "trigger_id",
    "entry": "entry_date",
    "price": "entry_price",
    "outcome": "trigger_outcome_label",
    "dedupe": "dedupe_for_aggregate",
    "dedupe_for_aggregate": "dedupe_for_aggregate",
    "agg_role": "aggregate_group_role",
    "aggregate_role": "aggregate_group_role",
    "group_role": "aggregate_group_role",
}

ROW_TYPES = {
    "price_source_validation",
    "case",
    "trigger",
    "score_simulation",
    "profile_comparison",
    "shadow_weight",
    "optimization_decision",
    "aggregate_metric",
    "narrative_only",
}

FENCE_RE = re.compile(r"```(?P<lang>[A-Za-z0-9_-]*)\n(?P<body>.*?)```", re.DOTALL)


@dataclass(frozen=True)
class ParsedMarkdown:
    registry_row: dict[str, Any]
    rows_by_type: dict[str, list[dict[str, Any]]]
    failed: bool = False
    failure_reason: str | None = None


def _normalise_key(key: str) -> str:
    stripped = key.strip().strip("`")
    return COLUMN_ALIASES.get(stripped, stripped)


def _normalise_value(value: Any) -> Any:
    if isinstance(value, str):
        stripped = value.strip()
        if stripped.lower() in {"true", "false"}:
            return stripped.lower() == "true"
        return stripped
    return value


def _normalise_row(row: dict[str, Any]) -> dict[str, Any]:
    normalised: dict[str, Any] = {}
    for key, value in row.items():
        if key is None:
            continue
        if isinstance(value, str) and key.startswith("_"):
            normalised[key] = value
            continue
        normalised[_normalise_key(str(key))] = _normalise_value(value)
    return normalised


def _append_row(
    rows_by_type: dict[str, list[dict[str, Any]]],
    row: dict[str, Any],
    *,
    document: MarkdownDocument,
    method: str,
    line_number: int | None,
    raw_snippet: str,
) -> None:
    normalised = _normalise_row(row)
    row_type = str(normalised.get("row_type", "")).strip()
    if row_type not in ROW_TYPES:
        return
    normalised.setdefault("round", document.round)
    normalised.setdefault("loop", document.loop)
    normalised["source_file"] = str(document.path)
    normalised["source_sha256"] = document.sha256
    normalised["source_line_range"] = f"{line_number}" if line_number else None
    normalised["raw_source_snippet"] = raw_snippet[:1000]
    normalised["parse_method"] = method
    rows_by_type.setdefault(row_type, []).append(normalised)


def _parse_metadata(text: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for match in FENCE_RE.finditer(text[:16000]):
        if match.group("lang").strip().lower() not in {"text", ""}:
            continue
        for raw_line in match.group("body").splitlines():
            line = raw_line.strip()
            if "=" not in line:
                continue
            key, value = [part.strip() for part in line.split("=", 1)]
            if key:
                metadata[key] = value
    return metadata


def _line_number_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _parse_json_lines(text: str, rows_by_type: dict[str, list[dict[str, Any]]], document: MarkdownDocument) -> None:
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not (line.startswith("{") and line.endswith("}")):
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "row_type" not in payload and payload.get("source") == "Songdaiki/stock-web":
            payload = {"row_type": "price_source_validation", **payload}
        _append_row(
            rows_by_type,
            payload,
            document=document,
            method="jsonl",
            line_number=line_number,
            raw_snippet=raw_line,
        )


def _parse_csv_fences(text: str, rows_by_type: dict[str, list[dict[str, Any]]], document: MarkdownDocument) -> None:
    for match in FENCE_RE.finditer(text):
        lang = match.group("lang").strip().lower()
        body = match.group("body").strip("\n")
        if lang not in {"csv", "tsv"}:
            continue
        if "row_type" not in body.splitlines()[0]:
            continue
        delimiter = "\t" if lang == "tsv" else ","
        reader = csv.DictReader(io.StringIO(body), delimiter=delimiter)
        start_line = _line_number_for_offset(text, match.start("body"))
        for offset, row in enumerate(reader, start=1):
            _append_row(
                rows_by_type,
                dict(row),
                document=document,
                method=f"{lang}_fence",
                line_number=start_line + offset,
                raw_snippet=",".join(str(value) for value in row.values()),
            )


def _split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _parse_markdown_tables(text: str, rows_by_type: dict[str, list[dict[str, Any]]], document: MarkdownDocument) -> None:
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        if not lines[index].lstrip().startswith("|"):
            index += 1
            continue
        start = index
        block: list[str] = []
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            block.append(lines[index])
            index += 1
        if len(block) < 2:
            continue
        headers = [_normalise_key(cell) for cell in _split_markdown_row(block[0])]
        separator = _split_markdown_row(block[1])
        if not all(set(cell.replace(":", "").strip()) <= {"-"} for cell in separator if cell):
            continue
        data_lines = block[2:]
        has_row_type = "row_type" in headers
        looks_like_trigger = {"trigger_id", "entry_date", "entry_price"}.issubset(set(headers))
        looks_like_price_source = headers == ["field", "value"]
        if not (has_row_type or looks_like_trigger or looks_like_price_source):
            continue
        if looks_like_price_source:
            values = {}
            for line in data_lines:
                cells = _split_markdown_row(line)
                if len(cells) >= 2:
                    values[cells[0]] = cells[1]
            if values.get("source") == "Songdaiki/stock-web" or values.get("price_basis") == "tradable_raw":
                _append_row(
                    rows_by_type,
                    {"row_type": "price_source_validation", **values},
                    document=document,
                    method="markdown_table",
                    line_number=start + 1,
                    raw_snippet="\n".join(block[: min(8, len(block))]),
                )
            continue
        for line in data_lines:
            cells = _split_markdown_row(line)
            if len(cells) != len(headers):
                continue
            row = dict(zip(headers, cells))
            if looks_like_trigger and "row_type" not in row:
                row["row_type"] = "trigger"
            _append_row(
                rows_by_type,
                row,
                document=document,
                method="markdown_table",
                line_number=start + 1,
                raw_snippet=line,
            )


def parse_markdown_document(document: MarkdownDocument) -> ParsedMarkdown:
    text = document.path.read_text(encoding="utf-8", errors="replace")
    metadata = _parse_metadata(text)
    rows_by_type: dict[str, list[dict[str, Any]]] = {row_type: [] for row_type in ROW_TYPES}

    try:
        _parse_json_lines(text, rows_by_type, document)
        _parse_csv_fences(text, rows_by_type, document)
        _parse_markdown_tables(text, rows_by_type, document)
        if not rows_by_type["price_source_validation"]:
            candidate = {
                "row_type": "price_source_validation",
                "source": metadata.get("price_source"),
                "price_basis": metadata.get("price_basis"),
                "price_adjustment_status": metadata.get("price_adjustment_status"),
                "validation_status": "metadata_fallback",
            }
            if candidate["source"]:
                _append_row(
                    rows_by_type,
                    candidate,
                    document=document,
                    method="metadata_fallback",
                    line_number=None,
                    raw_snippet=json.dumps(candidate, ensure_ascii=False),
                )
    except Exception as exc:  # pragma: no cover - defensive registry path
        return ParsedMarkdown(
            registry_row=_registry_row(document, metadata, rows_by_type, "failed", str(exc)),
            rows_by_type=rows_by_type,
            failed=True,
            failure_reason=str(exc),
        )

    status = "parsed" if any(rows_by_type[row_type] for row_type in ROW_TYPES) else "metadata_only"
    return ParsedMarkdown(
        registry_row=_registry_row(document, metadata, rows_by_type, status, None),
        rows_by_type=rows_by_type,
    )


def _registry_row(
    document: MarkdownDocument,
    metadata: dict[str, str],
    rows_by_type: dict[str, list[dict[str, Any]]],
    status: str,
    failure_reason: str | None,
) -> dict[str, Any]:
    trigger_count = len(rows_by_type.get("trigger", []))
    rejected_count = 0
    return {
        "file_path": str(document.path),
        "sha256": document.sha256,
        "round": document.round or metadata.get("round"),
        "loop": document.loop or metadata.get("loop"),
        "sector": metadata.get("sector"),
        "extraction_status": status,
        "parsed_trigger_row_count": trigger_count,
        "rejected_row_count": rejected_count,
        "failure_reason": failure_reason,
        "row_type_counts": {row_type: len(rows) for row_type, rows in sorted(rows_by_type.items()) if rows},
    }
