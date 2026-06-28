"""Parse research artifacts into raw research rows."""

from __future__ import annotations

import csv
import json
import re
from io import StringIO
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.schemas import ArtifactInventoryRow, RawResearchRow


_FENCED_RE = re.compile(r"```(?P<lang>[A-Za-z0-9_-]*)\n(?P<body>.*?)```", re.DOTALL)
_YAML_FRONT_MATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
_NARRATIVE_KEYWORDS = (
    "source_proxy_only",
    "evidence_url_pending",
    "Green",
    "green blocker",
    "false positive",
    "counterexample",
    "4B",
    "4C",
    "source route",
    "query",
    "primitive",
    "Stage",
)


def parse_research_artifact(path: str | Path, inventory_row: ArtifactInventoryRow | None = None) -> tuple[RawResearchRow, ...]:
    artifact_path = Path(path)
    digest = inventory_row.sha256 if inventory_row else ""
    artifact_type = inventory_row.artifact_type if inventory_row else artifact_path.suffix.lower().lstrip(".")
    text = artifact_path.read_text(encoding="utf-8", errors="ignore")
    if artifact_path.suffix.lower() == ".jsonl":
        return _parse_jsonl(text=text, path=artifact_path, digest=digest, artifact_type=artifact_type)
    if artifact_path.suffix.lower() == ".json":
        return _parse_json(text=text, path=artifact_path, digest=digest, artifact_type=artifact_type)
    if artifact_path.suffix.lower() == ".csv":
        return _parse_csv(text=text, path=artifact_path, digest=digest, artifact_type=artifact_type)
    if artifact_path.suffix.lower() == ".md":
        return _parse_markdown(text=text, path=artifact_path, digest=digest, artifact_type=artifact_type)
    return _parse_narrative(text=text, path=artifact_path, digest=digest, artifact_type=artifact_type, offset=1)


def _base_row(
    *,
    path: Path,
    digest: str,
    artifact_type: str,
    span: str,
    row_kind: str,
    data: Mapping[str, Any],
    text: str,
) -> RawResearchRow:
    return RawResearchRow(
        source_artifact_path=str(path),
        source_artifact_sha256=digest,
        source_artifact_type=artifact_type,
        source_line_or_span=span,
        row_kind=row_kind,
        data=data,
        text=text,
    )


def _parse_jsonl(*, text: str, path: Path, digest: str, artifact_type: str) -> tuple[RawResearchRow, ...]:
    rows: list[RawResearchRow] = []
    for index, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            data = json.loads(stripped)
            if not isinstance(data, Mapping):
                data = {"value": data}
            rows.append(
                _base_row(
                    path=path,
                    digest=digest,
                    artifact_type=artifact_type,
                    span=f"L{index}",
                    row_kind="jsonl",
                    data=data,
                    text=stripped[:4_000],
                )
            )
        except json.JSONDecodeError:
            rows.append(
                _base_row(
                    path=path,
                    digest=digest,
                    artifact_type=artifact_type,
                    span=f"L{index}",
                    row_kind="parse_error",
                    data={"parse_error": "json_decode_error"},
                    text=stripped[:4_000],
                )
            )
    return tuple(rows)


def _parse_json(*, text: str, path: Path, digest: str, artifact_type: str) -> tuple[RawResearchRow, ...]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return _parse_narrative(text=text, path=path, digest=digest, artifact_type=artifact_type, offset=1)
    rows: list[RawResearchRow] = []
    for pointer, item in _walk_json_rows(data):
        if isinstance(item, Mapping):
            payload = item
        else:
            payload = {"value": item}
        rows.append(
            _base_row(
                path=path,
                digest=digest,
                artifact_type=artifact_type,
                span=pointer,
                row_kind="json",
                data=payload,
                text=json.dumps(payload, ensure_ascii=False)[:4_000],
            )
        )
    return tuple(rows)


def _walk_json_rows(data: Any, pointer: str = "$") -> tuple[tuple[str, Any], ...]:
    if isinstance(data, list):
        rows: list[tuple[str, Any]] = []
        for index, item in enumerate(data):
            if isinstance(item, (Mapping, list)):
                rows.extend(_walk_json_rows(item, f"{pointer}[{index}]"))
            else:
                rows.append((f"{pointer}[{index}]", item))
        return tuple(rows)
    if isinstance(data, Mapping):
        list_keys = [key for key, value in data.items() if isinstance(value, list)]
        if not list_keys:
            return ((pointer, data),)
        rows: list[tuple[str, Any]] = []
        for key in list_keys:
            value = data[key]
            for index, item in enumerate(value):
                rows.append((f"{pointer}.{key}[{index}]", item))
        if not rows:
            rows.append((pointer, data))
        return tuple(rows)
    return ((pointer, data),)


def _parse_csv(*, text: str, path: Path, digest: str, artifact_type: str) -> tuple[RawResearchRow, ...]:
    rows: list[RawResearchRow] = []
    reader = csv.DictReader(StringIO(text))
    for index, data in enumerate(reader, start=2):
        rows.append(
            _base_row(
                path=path,
                digest=digest,
                artifact_type=artifact_type,
                span=f"L{index}",
                row_kind="csv",
                data={key: value for key, value in data.items() if key is not None},
                text=" ".join(str(value) for value in data.values())[:4_000],
            )
        )
    return tuple(rows)


def _parse_markdown(*, text: str, path: Path, digest: str, artifact_type: str) -> tuple[RawResearchRow, ...]:
    rows: list[RawResearchRow] = []
    front_matter = _YAML_FRONT_MATTER_RE.search(text)
    if front_matter:
        rows.append(
            _base_row(
                path=path,
                digest=digest,
                artifact_type=artifact_type,
                span="front_matter",
                row_kind="yaml_front_matter",
                data=_parse_simple_yaml(front_matter.group("body")),
                text=front_matter.group("body")[:4_000],
            )
        )
    for match_index, match in enumerate(_FENCED_RE.finditer(text), start=1):
        lang = match.group("lang").lower()
        body = match.group("body").strip()
        if lang in {"json", "jsonl"}:
            sub_rows = _parse_jsonl(text=body, path=path, digest=digest, artifact_type=artifact_type) if lang == "jsonl" else _parse_json(text=body, path=path, digest=digest, artifact_type=artifact_type)
            for row_index, row in enumerate(sub_rows, start=1):
                rows.append(
                    _base_row(
                        path=path,
                        digest=digest,
                        artifact_type=artifact_type,
                        span=f"fence{match_index}:{row.source_line_or_span}",
                        row_kind=f"fenced_{lang}",
                        data=row.data,
                        text=row.text,
                    )
                )
        elif lang == "csv":
            for row_index, row in enumerate(_parse_csv(text=body, path=path, digest=digest, artifact_type=artifact_type), start=1):
                rows.append(
                    _base_row(
                        path=path,
                        digest=digest,
                        artifact_type=artifact_type,
                        span=f"fence{match_index}:row{row_index}",
                        row_kind="fenced_csv",
                        data=row.data,
                        text=row.text,
                    )
                )
        else:
            rows.append(
                _base_row(
                    path=path,
                    digest=digest,
                    artifact_type=artifact_type,
                    span=f"fence{match_index}",
                    row_kind="fenced_text",
                    data={"language": lang or "text"},
                    text=body[:4_000],
                )
            )
    rows.extend(_parse_markdown_tables(text=text, path=path, digest=digest, artifact_type=artifact_type))
    rows.extend(_parse_narrative(text=text, path=path, digest=digest, artifact_type=artifact_type, offset=1))
    return tuple(rows)


def _parse_markdown_tables(*, text: str, path: Path, digest: str, artifact_type: str) -> tuple[RawResearchRow, ...]:
    lines = text.splitlines()
    rows: list[RawResearchRow] = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not (line.startswith("|") and line.endswith("|")):
            index += 1
            continue
        header = _split_md_table(line)
        if index + 1 >= len(lines) or "---" not in lines[index + 1]:
            index += 1
            continue
        index += 2
        row_number = 0
        while index < len(lines):
            row_line = lines[index].strip()
            if not (row_line.startswith("|") and row_line.endswith("|")):
                break
            values = _split_md_table(row_line)
            row_number += 1
            data = {header[col]: values[col] if col < len(values) else "" for col in range(len(header))}
            rows.append(
                _base_row(
                    path=path,
                    digest=digest,
                    artifact_type=artifact_type,
                    span=f"L{index + 1}:table{row_number}",
                    row_kind="markdown_table",
                    data=data,
                    text=row_line[:4_000],
                )
            )
            index += 1
        index += 1
    return tuple(rows)


def _parse_narrative(*, text: str, path: Path, digest: str, artifact_type: str, offset: int) -> tuple[RawResearchRow, ...]:
    rows: list[RawResearchRow] = []
    paragraph: list[str] = []
    start_line = offset
    for line_number, line in enumerate(text.splitlines(), start=offset):
        if line.strip():
            if not paragraph:
                start_line = line_number
            paragraph.append(line)
            continue
        if paragraph:
            rows.extend(_paragraph_to_row(path, digest, artifact_type, start_line, paragraph))
            paragraph = []
    if paragraph:
        rows.extend(_paragraph_to_row(path, digest, artifact_type, start_line, paragraph))
    return tuple(rows)


def _paragraph_to_row(path: Path, digest: str, artifact_type: str, start_line: int, lines: Sequence[str]) -> tuple[RawResearchRow, ...]:
    text = "\n".join(lines).strip()
    if len(text) < 30:
        return ()
    if not any(keyword.lower() in text.lower() for keyword in _NARRATIVE_KEYWORDS):
        return ()
    return (
        _base_row(
            path=path,
            digest=digest,
            artifact_type=artifact_type,
            span=f"L{start_line}-L{start_line + len(lines) - 1}",
            row_kind="narrative",
            data={"narrative": True},
            text=text[:4_000],
        ),
    )


def _split_md_table(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _parse_simple_yaml(text: str) -> Mapping[str, Any]:
    data: dict[str, Any] = {}
    for line in text.splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


__all__ = ["parse_research_artifact"]
