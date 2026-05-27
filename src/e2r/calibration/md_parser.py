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
    "current": "current_profile_verdict",
    "outcome": "trigger_outcome_label",
    "verdict": "trigger_outcome_label",
    "role": "case_type",
    "fine": "fine_archetype_id",
    "evidence family": "evidence_family",
    "validation status": "validation_status",
    "positive / counterexample": "positive_or_counterexample",
    "positive_or_counterexample": "positive_or_counterexample",
    "4b_case_count": "4B_case_count",
    "4c_case_count": "4C_case_count",
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
    "residual_contribution",
    "stage_transition_summary",
    "coverage_matrix",
    "sector_rule_candidate",
    "canonical_archetype_rule_candidate",
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
    if stripped in COLUMN_ALIASES:
        return COLUMN_ALIASES[stripped]
    for alias_key, alias_value in COLUMN_ALIASES.items():
        if stripped.lower() == alias_key.lower():
            return alias_value
    lowered = re.sub(r"[^0-9A-Za-z가-힣_]+", "_", stripped.strip().lower()).strip("_")
    return COLUMN_ALIASES.get(lowered, lowered or stripped)


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
    normalised.setdefault("schema_family", document.schema_family)
    normalised.setdefault("large_sector_id", document.large_sector_id)
    normalised.setdefault("canonical_archetype_id", document.canonical_archetype_id)
    normalised.setdefault("fine_archetype_id", document.fine_archetype_id)
    if document.schema_family == "v12_sector_archetype_residual":
        normalised.setdefault("price_data_source", "Songdaiki/stock-web")
        normalised.setdefault("price_source", "Songdaiki/stock-web")
        normalised.setdefault("source", "Songdaiki/stock-web")
        normalised.setdefault("price_basis", "tradable_raw")
        normalised.setdefault("price_adjustment_status", "raw_unadjusted_marcap")
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
    for raw_line in text[:24000].splitlines():
        line = raw_line.strip()
        if line.startswith("- "):
            line = line[2:].strip()
        if ":" not in line:
            continue
        key, value = [part.strip() for part in line.split(":", 1)]
        normalised_key = _normalise_key(key)
        if not normalised_key or normalised_key in metadata:
            continue
        cleaned = value.strip().strip("`").strip()
        if cleaned:
            metadata[normalised_key] = cleaned
    if "Songdaiki/stock-web" in text[:24000] and "price_source" not in metadata:
        metadata["price_source"] = "Songdaiki/stock-web"
    return metadata


def _line_number_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _v12_document_flags(text: str) -> dict[str, bool]:
    lower = text.lower()
    return {
        "evidence_url_pending": "evidence url pending" in lower or "url pending" in lower or "urls pending" in lower,
        "source_proxy_only": "source-name-level" in lower
        or "historical public-event proxies" in lower
        or "event proxies" in lower,
    }


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
        looks_like_case = {"case_id", "symbol"}.issubset(set(headers)) and (
            "company_name" in headers or "positive_or_counterexample" in headers or "case_type" in headers
        )
        looks_like_coverage = {"large_sector_id", "canonical_archetype_id"}.issubset(set(headers)) and (
            "calibration_usable_trigger_count" in headers or "representative_trigger_count" in headers
        )
        looks_like_rule_candidate = "rule_scope" in headers or (
            "sector_rule_candidate" in headers or "canonical_rule_candidate" in headers
        )
        looks_like_price_source = headers == ["field", "value"]
        if not (has_row_type or looks_like_trigger or looks_like_case or looks_like_coverage or looks_like_rule_candidate or looks_like_price_source):
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
            elif looks_like_case and "row_type" not in row:
                row["row_type"] = "case"
            elif looks_like_coverage and "row_type" not in row:
                row["row_type"] = "coverage_matrix"
            elif looks_like_rule_candidate and "row_type" not in row:
                row["row_type"] = "sector_rule_candidate"
            _append_row(
                rows_by_type,
                row,
                document=document,
                method="markdown_table",
                line_number=start + 1,
                raw_snippet=line,
            )


def _enrich_trigger_rows_by_trigger_id(rows_by_type: dict[str, list[dict[str, Any]]]) -> None:
    """Merge trigger-grid metadata into OHLC trigger rows with the same id.

    Several v12 research files separate the trigger grid from the price-path
    table. The OHLC table is the row usable for validation because it has
    MFE/MAE, but it may omit ``trigger_type`` and case verdict fields. Treating
    that omission as a valid blank trigger silently weakens stage transition
    aggregation, so we copy non-price metadata from the trigger-grid row.
    """

    trigger_rows = rows_by_type.get("trigger", [])
    metadata_by_trigger_id: dict[str, dict[str, Any]] = {}
    metadata_keys = (
        "case_id",
        "trigger_type",
        "trigger_date",
        "trigger_outcome_label",
        "current_profile_verdict",
        "aggregate_group_role",
        "case_type",
        "positive_or_counterexample",
        "dedupe_for_aggregate",
        "calibration_usable",
        "evidence_source",
        "evidence_available_at_that_date",
    )
    for row in trigger_rows:
        trigger_id = str(row.get("trigger_id") or "").strip()
        if not trigger_id:
            continue
        if not row.get("trigger_type") and not row.get("case_id"):
            continue
        metadata = metadata_by_trigger_id.setdefault(trigger_id, {})
        for key in metadata_keys:
            value = row.get(key)
            if value not in (None, "") and key not in metadata:
                metadata[key] = value
    for row in trigger_rows:
        trigger_id = str(row.get("trigger_id") or "").strip()
        if not trigger_id:
            continue
        metadata = metadata_by_trigger_id.get(trigger_id)
        if not metadata:
            continue
        for key, value in metadata.items():
            if row.get(key) in (None, ""):
                row[key] = value


def parse_markdown_document(document: MarkdownDocument) -> ParsedMarkdown:
    text = document.path.read_text(encoding="utf-8", errors="replace")
    metadata = _parse_metadata(text)
    if document.large_sector_id is None and metadata.get("large_sector_id"):
        object.__setattr__(document, "large_sector_id", metadata.get("large_sector_id"))
    if document.canonical_archetype_id is None and metadata.get("canonical_archetype_id"):
        object.__setattr__(document, "canonical_archetype_id", metadata.get("canonical_archetype_id"))
    if document.fine_archetype_id is None and metadata.get("fine_archetype_id"):
        object.__setattr__(document, "fine_archetype_id", metadata.get("fine_archetype_id"))
    rows_by_type: dict[str, list[dict[str, Any]]] = {row_type: [] for row_type in ROW_TYPES}

    try:
        _parse_json_lines(text, rows_by_type, document)
        _parse_csv_fences(text, rows_by_type, document)
        _parse_markdown_tables(text, rows_by_type, document)
        _enrich_trigger_rows_by_trigger_id(rows_by_type)
        if not rows_by_type["price_source_validation"]:
            candidate = {
                "row_type": "price_source_validation",
                "source": metadata.get("price_source"),
                "price_data_source": metadata.get("price_source"),
                "price_basis": metadata.get("price_basis", "tradable_raw" if document.schema_family == "v12_sector_archetype_residual" else None),
                "price_adjustment_status": metadata.get(
                    "price_adjustment_status",
                    "raw_unadjusted_marcap" if document.schema_family == "v12_sector_archetype_residual" else None,
                ),
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
        if document.schema_family == "v12_sector_archetype_residual":
            doc_flags = _v12_document_flags(text)
            residual_row = {
                "row_type": "residual_contribution",
                "research_session": metadata.get("research_session"),
                "mode": metadata.get("mode"),
                "round": document.round or metadata.get("round"),
                "loop": document.loop or metadata.get("loop"),
                "large_sector_id": document.large_sector_id or metadata.get("large_sector_id"),
                "canonical_archetype_id": document.canonical_archetype_id or metadata.get("canonical_archetype_id"),
                "fine_archetype_id": document.fine_archetype_id or metadata.get("fine_archetype_id"),
                "loop_objective": metadata.get("loop_objective"),
                "current_default_profile_proxy": metadata.get("current_default_profile_proxy") or metadata.get("current_default_proxy"),
                "previous_baseline_reference": metadata.get("previous_baseline_reference"),
                "new_independent_case_count": metadata.get("new_independent_case_count"),
                "reused_case_count": metadata.get("reused_case_count"),
                "new_symbol_count": metadata.get("new_symbol_count"),
                "same_archetype_new_symbol_count": metadata.get("same_archetype_new_symbol_count"),
                "same_archetype_new_trigger_family_count": metadata.get("same_archetype_new_trigger_family_count"),
                "positive_case_count": metadata.get("positive_case_count"),
                "counterexample_count": metadata.get("counterexample_count"),
                "4B_case_count": metadata.get("4B_case_count"),
                "4C_case_count": metadata.get("4C_case_count"),
                "loop_contribution_label": metadata.get("loop_contribution_label"),
                "do_not_propose_new_weight_delta": metadata.get("do_not_propose_new_weight_delta"),
                "auto_selected_coverage_gap": metadata.get("auto_selected_coverage_gap"),
                **doc_flags,
            }
            _append_row(
                rows_by_type,
                residual_row,
                document=document,
                method="metadata_residual_summary",
                line_number=None,
                raw_snippet=json.dumps(residual_row, ensure_ascii=False),
            )
            for typed_rows in rows_by_type.values():
                for row in typed_rows:
                    row.setdefault("evidence_url_pending", doc_flags["evidence_url_pending"])
                    row.setdefault("source_proxy_only", doc_flags["source_proxy_only"])
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
        "filename": document.filename or document.path.name,
        "schema_family": document.schema_family,
        "round": document.round or metadata.get("round"),
        "loop": document.loop or metadata.get("loop"),
        "sector": metadata.get("sector"),
        "large_sector_id": document.large_sector_id or metadata.get("large_sector_id"),
        "canonical_archetype_id": document.canonical_archetype_id or metadata.get("canonical_archetype_id"),
        "fine_archetype_id": document.fine_archetype_id or metadata.get("fine_archetype_id"),
        "loop_objective": metadata.get("loop_objective"),
        "loop_contribution_label": metadata.get("loop_contribution_label"),
        "extraction_status": status,
        "parsed_trigger_row_count": trigger_count,
        "rejected_row_count": rejected_count,
        "failure_reason": failure_reason,
        "row_type_counts": {row_type: len(rows) for row_type, rows in sorted(rows_by_type.items()) if rows},
    }
