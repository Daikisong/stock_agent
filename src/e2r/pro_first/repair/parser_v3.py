"""Bounded parser for one compact RepairDeltaV3 JSON object."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from typing import Any, Mapping


REPAIR_BEGIN = "E2R_REPAIR_DELTA_JSON_BEGIN"
REPAIR_END = "E2R_REPAIR_DELTA_JSON_END"


class RepairDeltaV3ParseError(ValueError):
    pass


@dataclass(frozen=True)
class ParsedRepairDeltaV3:
    payload: Mapping[str, Any]
    before_hash: str
    json_hash: str
    parser_operations: tuple[str, ...]


class RepairDeltaV3Parser:
    def parse_text(self, text: str) -> ParsedRepairDeltaV3:
        if not isinstance(text, str) or not text.strip():
            raise RepairDeltaV3ParseError("compact repair response is empty")
        before_hash = _sha256_text(text)
        normalized = text
        operations: list[str] = []
        if normalized.startswith("\ufeff"):
            normalized = normalized[1:]
            operations.append("REMOVE_UTF8_BOM")
        begin_count = normalized.count(REPAIR_BEGIN)
        end_count = normalized.count(REPAIR_END)
        if begin_count or end_count:
            if begin_count != 1 or end_count != 1:
                raise RepairDeltaV3ParseError(
                    "repair delta sentinel block must occur exactly once"
                )
            begin = normalized.index(REPAIR_BEGIN) + len(REPAIR_BEGIN)
            end = normalized.index(REPAIR_END, begin)
            normalized = normalized[begin:end].strip()
            operations.append("EXTRACT_REPAIR_DELTA_SENTINEL_BLOCK")
        stripped = normalized.strip()
        if stripped.startswith("```"):
            lines = stripped.splitlines()
            if len(lines) < 3 or lines[-1].strip() != "```":
                raise RepairDeltaV3ParseError("repair delta JSON fence is incomplete")
            if lines[0].strip().casefold() not in {"```", "```json"}:
                raise RepairDeltaV3ParseError("repair delta fence must be JSON")
            normalized = "\n".join(lines[1:-1]).strip()
            operations.append("REMOVE_JSON_CODE_FENCE")
        try:
            payload = json.loads(normalized)
        except json.JSONDecodeError as error:
            raise RepairDeltaV3ParseError(
                f"repair delta JSON is invalid at line {error.lineno} column {error.colno}"
            ) from error
        if not isinstance(payload, dict):
            raise RepairDeltaV3ParseError("RepairDeltaV3 must be one JSON object")
        return ParsedRepairDeltaV3(
            payload=payload,
            before_hash=before_hash,
            json_hash=_sha256_text(normalized),
            parser_operations=tuple(operations),
        )


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


__all__ = [
    "ParsedRepairDeltaV3",
    "REPAIR_BEGIN",
    "REPAIR_END",
    "RepairDeltaV3ParseError",
    "RepairDeltaV3Parser",
]
