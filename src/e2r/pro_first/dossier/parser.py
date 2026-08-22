"""Bounded ResearchDossierV1 parser with deletion-only JSON repairs."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Mapping


BEGIN = "E2R_RESEARCH_DOSSIER_JSON_BEGIN"
END = "E2R_RESEARCH_DOSSIER_JSON_END"
_PROTECTED_FIELDS = (
    "dossier_fact_id",
    "source_url",
    "supporting_excerpt",
    "statement",
)


class DossierParseError(ValueError):
    pass


@dataclass(frozen=True)
class ParsedDossier:
    payload: Mapping[str, Any]
    parser_source: str
    before_hash: str
    after_hash: str
    repair_operations: tuple[str, ...]
    protected_values_before: Mapping[str, tuple[str, ...]]
    protected_values_after: Mapping[str, tuple[str, ...]]


class ResearchDossierParser:
    def parse(
        self,
        *,
        downloaded_json_path: str | Path | None = None,
        report_md_path: str | Path | None = None,
        final_response_text: str | None = None,
    ) -> ParsedDossier:
        candidates: list[tuple[str, str]] = []
        if downloaded_json_path is not None and Path(downloaded_json_path).is_file():
            candidates.append(
                (
                    "DOWNLOADED_JSON",
                    Path(downloaded_json_path).read_text(encoding="utf-8-sig"),
                )
            )
        if report_md_path is not None and Path(report_md_path).is_file():
            candidates.append(
                ("MD_SENTINEL", Path(report_md_path).read_text(encoding="utf-8-sig"))
            )
        if final_response_text is not None and final_response_text.strip():
            candidates.append(("FINAL_RESPONSE_SENTINEL", final_response_text))
        if not candidates:
            raise DossierParseError("no dossier JSON, MD, or final response candidate exists")
        errors: list[str] = []
        for source, text in candidates:
            try:
                return self.parse_text(text, parser_source=source)
            except DossierParseError as error:
                errors.append(f"{source}: {error}")
        raise DossierParseError("all dossier parser candidates failed: " + " | ".join(errors))

    def parse_text(self, text: str, *, parser_source: str) -> ParsedDossier:
        if not isinstance(text, str) or not text.strip():
            raise DossierParseError("dossier text is empty")
        before_hash = _text_hash(text)
        protected_before = _protected_values(text)
        repaired = text
        operations: list[str] = []
        if repaired.startswith("\ufeff"):
            repaired = repaired[1:]
            operations.append("REMOVE_UTF8_BOM")
        begin_count = repaired.count(BEGIN)
        end_count = repaired.count(END)
        if begin_count or end_count:
            if begin_count != 1 or end_count != 1:
                raise DossierParseError("dossier sentinel block must occur exactly once")
            begin = repaired.index(BEGIN) + len(BEGIN)
            end = repaired.index(END, begin)
            repaired = repaired[begin:end].strip()
            operations.append("EXTRACT_DOSSIER_SENTINEL_BLOCK")
        stripped = repaired.strip()
        if stripped.startswith("```"):
            lines = stripped.splitlines()
            if len(lines) < 3 or not lines[-1].strip().startswith("```"):
                raise DossierParseError("dossier JSON code fence is incomplete")
            repaired = "\n".join(lines[1:-1]).strip()
            operations.append("REMOVE_JSON_CODE_FENCE")
        # ChatGPT's visible code-block DOM can omit the backticks while
        # retaining the standalone language badge as the first text line.
        # Removing only that exact label is a bounded, deletion-only repair.
        lines = repaired.strip().splitlines()
        if (
            len(lines) >= 2
            and lines[0].strip().casefold() == "json"
            and lines[1].lstrip().startswith("{")
        ):
            repaired = "\n".join(lines[1:]).strip()
            operations.append("REMOVE_STANDALONE_JSON_LANGUAGE_LABEL")
        trailing_fixed, removed_count = _remove_trailing_commas(repaired)
        if removed_count:
            repaired = trailing_fixed
            operations.append(f"REMOVE_TRAILING_COMMAS:{removed_count}")
        try:
            payload = json.loads(repaired)
        except json.JSONDecodeError as error:
            raise DossierParseError(
                f"JSON syntax remains invalid at line {error.lineno} column {error.colno}"
            ) from error
        if not isinstance(payload, dict):
            raise DossierParseError("ResearchDossierV1 must be a JSON object")
        protected_after = _protected_values(repaired)
        for field in _PROTECTED_FIELDS:
            before_values = protected_before[field]
            after_values = protected_after[field]
            if begin_count:
                block_values = _protected_values(text[text.index(BEGIN) : text.index(END)])[field]
                before_values = block_values
            if before_values != after_values:
                raise DossierParseError(
                    f"bounded repair changed protected dossier content: {field}"
                )
        return ParsedDossier(
            payload=payload,
            parser_source=parser_source,
            before_hash=before_hash,
            after_hash=_text_hash(repaired),
            repair_operations=tuple(operations),
            protected_values_before=protected_before,
            protected_values_after=protected_after,
        )


def _remove_trailing_commas(text: str) -> tuple[str, int]:
    output: list[str] = []
    in_string = False
    escaped = False
    removed = 0
    index = 0
    while index < len(text):
        character = text[index]
        if in_string:
            output.append(character)
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
            index += 1
            continue
        if character == '"':
            in_string = True
            output.append(character)
            index += 1
            continue
        if character == ",":
            lookahead = index + 1
            while lookahead < len(text) and text[lookahead].isspace():
                lookahead += 1
            if lookahead < len(text) and text[lookahead] in "}]":
                removed += 1
                index += 1
                continue
        output.append(character)
        index += 1
    return "".join(output), removed


def _protected_values(text: str) -> Mapping[str, tuple[str, ...]]:
    return {
        field: tuple(
            match.group(1)
            for match in re.finditer(
                rf'"{re.escape(field)}"\s*:\s*"((?:\\.|[^"\\])*)"', text
            )
        )
        for field in _PROTECTED_FIELDS
    }


def _text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


__all__ = [
    "DossierParseError",
    "ParsedDossier",
    "ResearchDossierParser",
]
