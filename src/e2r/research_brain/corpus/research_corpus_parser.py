"""Structured-row-first parser for historical E2R research artifacts."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from io import StringIO
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.research_brain.intelligence_schema import (
    HistoricalResearchArtifact,
    ParsedResearchArtifact,
    ParsedResearchRow,
    ParsedRowKind,
    QuarantineReason,
    QuarantineRecord,
    SourceLineRange,
    stable_intelligence_id,
)


_FENCE_MARKER = chr(96) * 3
_HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
_HANDOFF_TITLE_RE = re.compile(
    r"(deferred\s+coding\s+agent\s+handoff\s+prompt|coding\s+agent\s+handoff|handoff\s+prompt)",
    re.IGNORECASE,
)
_TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*$")
_URL_RE = re.compile(r"https?://[^\s)>\]\"']+")
_STRUCTURED_KINDS = {
    ParsedRowKind.YAML_FRONT_MATTER.value,
    ParsedRowKind.FENCED_JSON.value,
    ParsedRowKind.FENCED_JSONL.value,
    ParsedRowKind.FENCED_CSV.value,
    ParsedRowKind.MARKDOWN_TABLE.value,
    ParsedRowKind.JSON.value,
    ParsedRowKind.JSONL.value,
    ParsedRowKind.CSV.value,
}


def parse_historical_research_artifact(
    path: str | Path,
    *,
    repo_root: str | Path | None = None,
) -> ParsedResearchArtifact:
    source_path = Path(path)
    raw_bytes = source_path.read_bytes()
    text = raw_bytes.decode("utf-8", errors="replace")
    lines = text.splitlines()
    digest = hashlib.sha256(raw_bytes).hexdigest()
    source_file = _source_name(source_path, repo_root)
    artifact_id = stable_intelligence_id(
        "HART",
        {"source_file": source_file, "sha256": digest},
    )
    suffix = source_path.suffix.lower()
    if suffix == ".md":
        rows, quarantine, handoff_range, metadata = _parse_markdown(
            lines=lines,
            artifact_id=artifact_id,
            source_file=source_file,
        )
    elif suffix == ".jsonl":
        rows, quarantine = _parse_jsonl_lines(
            lines=lines,
            artifact_id=artifact_id,
            source_file=source_file,
            line_offset=1,
            kind=ParsedRowKind.JSONL,
            precedence=3,
        )
        handoff_range, metadata = None, {}
    elif suffix == ".json":
        rows, quarantine = _parse_json_document(
            text=text,
            artifact_id=artifact_id,
            source_file=source_file,
            line_range=SourceLineRange(1, max(1, len(lines))),
            kind=ParsedRowKind.JSON,
            precedence=2,
        )
        handoff_range, metadata = None, {}
    elif suffix == ".csv":
        rows, quarantine = _parse_csv_lines(
            text=text,
            artifact_id=artifact_id,
            source_file=source_file,
            start_line=1,
            kind=ParsedRowKind.CSV,
            precedence=4,
        )
        handoff_range, metadata = None, {}
    else:
        rows = tuple(
            _narrative_rows(
                lines=lines,
                artifact_id=artifact_id,
                source_file=source_file,
                excluded_lines=set(),
            )
        )
        quarantine, handoff_range, metadata = (), None, {}

    artifact = HistoricalResearchArtifact(
        artifact_id=artifact_id,
        source_file=source_file,
        sha256=digest,
        artifact_type=suffix.lstrip(".") or "text",
        line_count=max(1, len(lines)),
        structured_row_count=sum(row.structured for row in rows),
        narrative_row_count=sum(not row.structured for row in rows),
        handoff_line_range=handoff_range,
        metadata=metadata,
    )
    return ParsedResearchArtifact(
        artifact=artifact,
        rows=tuple(rows),
        quarantine=tuple(quarantine),
    )


def _parse_markdown(
    *,
    lines: Sequence[str],
    artifact_id: str,
    source_file: str,
) -> tuple[
    tuple[ParsedResearchRow, ...],
    tuple[QuarantineRecord, ...],
    SourceLineRange | None,
    Mapping[str, Any],
]:
    rows: list[ParsedResearchRow] = []
    quarantine: list[QuarantineRecord] = []
    excluded_lines: set[int] = set()
    metadata: dict[str, Any] = {}

    handoff_range = _handoff_range(lines)
    if handoff_range:
        excluded_lines.update(range(handoff_range.start, handoff_range.end + 1))
        quarantine.append(
            _quarantine(
                artifact_id=artifact_id,
                source_file=source_file,
                line_range=handoff_range,
                reason=QuarantineReason.HANDOFF_PROMPT_EXCLUDED,
                raw_text="\n".join(lines[handoff_range.start - 1 : handoff_range.end]),
                details={"parsed_as_case": False},
            )
        )

    front_range = _front_matter_range(lines)
    if front_range:
        front_text = "\n".join(lines[front_range.start : front_range.end - 1])
        data = _parse_simple_yaml(front_text)
        metadata.update(data)
        rows.append(
            _row(
                artifact_id=artifact_id,
                source_file=source_file,
                line_range=front_range,
                kind=ParsedRowKind.YAML_FRONT_MATTER,
                precedence=1,
                data=data,
                raw_text=front_text,
                structured=True,
            )
        )
        excluded_lines.update(range(front_range.start, front_range.end + 1))

    fence_rows, fence_quarantine, fence_lines = _parse_markdown_fences(
        lines=lines,
        artifact_id=artifact_id,
        source_file=source_file,
        handoff_range=handoff_range,
    )
    rows.extend(fence_rows)
    quarantine.extend(fence_quarantine)
    excluded_lines.update(fence_lines)

    table_rows, table_lines = _parse_markdown_tables(
        lines=lines,
        artifact_id=artifact_id,
        source_file=source_file,
        excluded_lines=excluded_lines,
    )
    rows.extend(table_rows)
    excluded_lines.update(table_lines)

    rows.extend(
        _narrative_rows(
            lines=lines,
            artifact_id=artifact_id,
            source_file=source_file,
            excluded_lines=excluded_lines,
        )
    )
    return tuple(rows), tuple(quarantine), handoff_range, metadata


def _parse_markdown_fences(
    *,
    lines: Sequence[str],
    artifact_id: str,
    source_file: str,
    handoff_range: SourceLineRange | None,
) -> tuple[list[ParsedResearchRow], list[QuarantineRecord], set[int]]:
    rows: list[ParsedResearchRow] = []
    quarantine: list[QuarantineRecord] = []
    excluded: set[int] = set()
    index = 0
    while index < len(lines):
        line_number = index + 1
        stripped = lines[index].strip()
        if not stripped.startswith(_FENCE_MARKER):
            index += 1
            continue
        language = stripped[len(_FENCE_MARKER) :].strip().lower()
        end = index + 1
        while end < len(lines) and not lines[end].strip().startswith(_FENCE_MARKER):
            end += 1
        if end >= len(lines):
            quarantine.append(
                _quarantine(
                    artifact_id=artifact_id,
                    source_file=source_file,
                    line_range=SourceLineRange(line_number, len(lines)),
                    reason=QuarantineReason.MALFORMED_STRUCTURED_ROW,
                    raw_text="\n".join(lines[index:]),
                    details={"error": "unclosed_fence", "language": language},
                )
            )
            excluded.update(range(line_number, len(lines) + 1))
            break
        fence_range = SourceLineRange(line_number, end + 1)
        excluded.update(range(fence_range.start, fence_range.end + 1))
        if handoff_range and _ranges_overlap(fence_range, handoff_range):
            index = end + 1
            continue
        body_lines = lines[index + 1 : end]
        body = "\n".join(body_lines)
        if language == "jsonl":
            parsed, errors = _parse_jsonl_lines(
                lines=body_lines,
                artifact_id=artifact_id,
                source_file=source_file,
                line_offset=index + 2,
                kind=ParsedRowKind.FENCED_JSONL,
                precedence=3,
            )
            rows.extend(parsed)
            quarantine.extend(errors)
        elif language == "json":
            parsed, errors = _parse_json_document(
                text=body,
                artifact_id=artifact_id,
                source_file=source_file,
                line_range=SourceLineRange(index + 2, max(index + 2, end)),
                kind=ParsedRowKind.FENCED_JSON,
                precedence=2,
            )
            rows.extend(parsed)
            quarantine.extend(errors)
        elif language == "csv":
            parsed, errors = _parse_csv_lines(
                text=body,
                artifact_id=artifact_id,
                source_file=source_file,
                start_line=index + 2,
                kind=ParsedRowKind.FENCED_CSV,
                precedence=4,
            )
            rows.extend(parsed)
            quarantine.extend(errors)
        index = end + 1
    return rows, quarantine, excluded


def _parse_jsonl_lines(
    *,
    lines: Sequence[str],
    artifact_id: str,
    source_file: str,
    line_offset: int,
    kind: ParsedRowKind,
    precedence: int,
) -> tuple[list[ParsedResearchRow], list[QuarantineRecord]]:
    rows: list[ParsedResearchRow] = []
    quarantine: list[QuarantineRecord] = []
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        line_number = line_offset + index
        line_range = SourceLineRange(line_number, line_number)
        try:
            data = json.loads(line)
            if not isinstance(data, Mapping):
                raise TypeError("JSONL row must be an object")
        except (json.JSONDecodeError, TypeError) as exc:
            quarantine.append(
                _quarantine(
                    artifact_id=artifact_id,
                    source_file=source_file,
                    line_range=line_range,
                    reason=QuarantineReason.MALFORMED_STRUCTURED_ROW,
                    raw_text=line,
                    details={"error": f"{type(exc).__name__}: {exc}"},
                )
            )
            continue
        rows.append(
            _row(
                artifact_id=artifact_id,
                source_file=source_file,
                line_range=line_range,
                kind=kind,
                precedence=precedence,
                data=data,
                raw_text=line,
                structured=True,
            )
        )
    return rows, quarantine


def _parse_json_document(
    *,
    text: str,
    artifact_id: str,
    source_file: str,
    line_range: SourceLineRange,
    kind: ParsedRowKind,
    precedence: int,
) -> tuple[list[ParsedResearchRow], list[QuarantineRecord]]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        return [], [
            _quarantine(
                artifact_id=artifact_id,
                source_file=source_file,
                line_range=line_range,
                reason=QuarantineReason.MALFORMED_STRUCTURED_ROW,
                raw_text=text,
                details={"error": f"JSONDecodeError: {exc}"},
            )
        ]
    rows: list[ParsedResearchRow] = []
    for item in _json_rows(payload):
        if not isinstance(item, Mapping):
            continue
        rows.append(
            _row(
                artifact_id=artifact_id,
                source_file=source_file,
                line_range=line_range,
                kind=kind,
                precedence=precedence,
                data=item,
                raw_text=json.dumps(item, ensure_ascii=False, sort_keys=True),
                structured=True,
            )
        )
    return rows, []


def _json_rows(payload: Any) -> Iterable[Mapping[str, Any]]:
    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, Mapping):
                yield item
        return
    if not isinstance(payload, Mapping):
        return
    for key in ("rows", "records", "cases", "triggers"):
        value = payload.get(key)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, Mapping):
                    yield item
            return
    yield payload


def _parse_csv_lines(
    *,
    text: str,
    artifact_id: str,
    source_file: str,
    start_line: int,
    kind: ParsedRowKind,
    precedence: int,
) -> tuple[list[ParsedResearchRow], list[QuarantineRecord]]:
    try:
        reader = csv.DictReader(StringIO(text))
        rows: list[ParsedResearchRow] = []
        for index, data in enumerate(reader, start=1):
            if None in data:
                raise ValueError("CSV row has more values than headers")
            line_number = start_line + index
            rows.append(
                _row(
                    artifact_id=artifact_id,
                    source_file=source_file,
                    line_range=SourceLineRange(line_number, line_number),
                    kind=kind,
                    precedence=precedence,
                    data={str(key).strip(): value for key, value in data.items()},
                    raw_text=json.dumps(data, ensure_ascii=False, sort_keys=True),
                    structured=True,
                )
            )
        return rows, []
    except (csv.Error, ValueError) as exc:
        end_line = start_line + max(0, len(text.splitlines()) - 1)
        return [], [
            _quarantine(
                artifact_id=artifact_id,
                source_file=source_file,
                line_range=SourceLineRange(start_line, max(start_line, end_line)),
                reason=QuarantineReason.MALFORMED_STRUCTURED_ROW,
                raw_text=text,
                details={"error": f"{type(exc).__name__}: {exc}"},
            )
        ]


def _parse_markdown_tables(
    *,
    lines: Sequence[str],
    artifact_id: str,
    source_file: str,
    excluded_lines: set[int],
) -> tuple[list[ParsedResearchRow], set[int]]:
    rows: list[ParsedResearchRow] = []
    used: set[int] = set()
    index = 0
    while index + 1 < len(lines):
        line_number = index + 1
        if line_number in excluded_lines:
            index += 1
            continue
        header_line = lines[index].strip()
        separator_line = lines[index + 1].strip()
        if "|" not in header_line or not _TABLE_SEPARATOR_RE.match(separator_line):
            index += 1
            continue
        headers = _split_table_row(header_line)
        if not headers:
            index += 1
            continue
        used.update({line_number, line_number + 1})
        row_index = index + 2
        while row_index < len(lines):
            current_number = row_index + 1
            if current_number in excluded_lines:
                break
            current = lines[row_index].strip()
            if "|" not in current or current.startswith("#"):
                break
            values = _split_table_row(current)
            if not values:
                break
            data = {
                header: values[column] if column < len(values) else ""
                for column, header in enumerate(headers)
            }
            rows.append(
                _row(
                    artifact_id=artifact_id,
                    source_file=source_file,
                    line_range=SourceLineRange(current_number, current_number),
                    kind=ParsedRowKind.MARKDOWN_TABLE,
                    precedence=5,
                    data=data,
                    raw_text=lines[row_index],
                    structured=True,
                )
            )
            used.add(current_number)
            row_index += 1
        index = max(index + 1, row_index)
    return rows, used


def _narrative_rows(
    *,
    lines: Sequence[str],
    artifact_id: str,
    source_file: str,
    excluded_lines: set[int],
) -> Iterable[ParsedResearchRow]:
    paragraph: list[str] = []
    start = 1

    def flush(end: int) -> ParsedResearchRow | None:
        nonlocal paragraph
        raw = "\n".join(paragraph).strip()
        paragraph = []
        if len(raw) < 30:
            return None
        return _row(
            artifact_id=artifact_id,
            source_file=source_file,
            line_range=SourceLineRange(start, end),
            kind=ParsedRowKind.NARRATIVE,
            precedence=6,
            data={"narrative": raw, "urls": _URL_RE.findall(raw)},
            raw_text=raw,
            structured=False,
        )

    for index, line in enumerate(lines, start=1):
        if index in excluded_lines or not line.strip() or line.lstrip().startswith("#"):
            if paragraph:
                row = flush(index - 1)
                if row:
                    yield row
            continue
        if not paragraph:
            start = index
        paragraph.append(line)
    if paragraph:
        row = flush(len(lines))
        if row:
            yield row


def _front_matter_range(lines: Sequence[str]) -> SourceLineRange | None:
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return SourceLineRange(1, index + 1)
    return None


def _handoff_range(lines: Sequence[str]) -> SourceLineRange | None:
    for index, line in enumerate(lines):
        match = _HEADING_RE.match(line.strip())
        if not match or not _HANDOFF_TITLE_RE.search(match.group("title")):
            continue
        level = len(match.group("marks"))
        end = len(lines)
        for next_index in range(index + 1, len(lines)):
            next_match = _HEADING_RE.match(lines[next_index].strip())
            if next_match and len(next_match.group("marks")) <= level:
                end = next_index
                break
        return SourceLineRange(index + 1, max(index + 1, end))
    return None


def _parse_simple_yaml(text: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, raw_value = stripped.split(":", 1)
        data[key.strip()] = _scalar(raw_value.strip())
    return data


def _scalar(value: str) -> Any:
    if not value:
        return ""
    lower = value.lower()
    if lower in {"true", "false"}:
        return lower == "true"
    if lower in {"null", "none", "~"}:
        return None
    try:
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return value.strip("\"'")


def _split_table_row(line: str) -> list[str]:
    stripped = line.strip().strip("|")
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", stripped)]


def _row(
    *,
    artifact_id: str,
    source_file: str,
    line_range: SourceLineRange,
    kind: ParsedRowKind,
    precedence: int,
    data: Mapping[str, Any],
    raw_text: str,
    structured: bool,
) -> ParsedResearchRow:
    payload = {
        "artifact_id": artifact_id,
        "source_file": source_file,
        "line_range": line_range.to_dict(),
        "kind": kind.value,
        "data": data,
    }
    return ParsedResearchRow(
        row_id=stable_intelligence_id("HROW", payload),
        artifact_id=artifact_id,
        source_file=source_file,
        source_line_range=line_range,
        row_kind=kind.value,
        precedence=precedence,
        data=dict(data),
        raw_text=raw_text,
        structured=structured,
    )


def _quarantine(
    *,
    artifact_id: str,
    source_file: str,
    line_range: SourceLineRange,
    reason: QuarantineReason,
    raw_text: str,
    details: Mapping[str, Any],
    row_id: str | None = None,
) -> QuarantineRecord:
    return QuarantineRecord(
        quarantine_id=stable_intelligence_id(
            "HQUAR",
            {
                "artifact_id": artifact_id,
                "line_range": line_range.to_dict(),
                "reason": reason.value,
                "row_id": row_id,
            },
        ),
        artifact_id=artifact_id,
        source_file=source_file,
        source_line_range=line_range,
        reason=reason.value,
        row_id=row_id,
        details=dict(details),
        raw_text=raw_text,
    )


def _source_name(path: Path, repo_root: str | Path | None) -> str:
    if repo_root is None:
        return path.as_posix()
    try:
        return path.resolve().relative_to(Path(repo_root).resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _ranges_overlap(left: SourceLineRange, right: SourceLineRange) -> bool:
    return left.start <= right.end and right.start <= left.end


def is_structured_row(row: ParsedResearchRow) -> bool:
    return row.row_kind in _STRUCTURED_KINDS and row.structured


__all__ = [
    "is_structured_row",
    "parse_historical_research_artifact",
]
