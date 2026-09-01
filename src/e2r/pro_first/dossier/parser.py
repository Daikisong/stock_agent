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
    "source_document_id",
    "source_url",
    "canonical_url",
    "supporting_excerpt",
    "statement",
    "predicate_id",
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
        key_fixed, removed_key_control_count = (
            _remove_raw_control_characters_from_json_keys(repaired)
        )
        if removed_key_control_count:
            repaired = key_fixed
            operations.append(
                "REMOVE_RAW_CONTROL_CHARACTERS_FROM_JSON_KEYS:"
                f"{removed_key_control_count}"
            )
        value_fixed, escaped_value_control_count = (
            _escape_raw_control_characters_in_json_string_values(repaired)
        )
        if escaped_value_control_count:
            repaired = value_fixed
            operations.append(
                "ESCAPE_RAW_CONTROL_CHARACTERS_IN_JSON_STRING_VALUES:"
                f"{escaped_value_control_count}"
            )
        quote_fixed, escaped_naked_quote_count = (
            _escape_decoder_proven_naked_quotes_in_json_string_values(repaired)
        )
        if escaped_naked_quote_count:
            repaired = quote_fixed
            operations.append(
                "ESCAPE_DECODER_PROVEN_NAKED_QUOTES_IN_JSON_STRING_VALUES:"
                f"{escaped_naked_quote_count}"
            )
            # Adding JSON escape bytes does not change the decoded evidence
            # text.  Re-project protected fields from that syntax-safe form so
            # the before/after comparison sees the complete original value,
            # including the literal quote characters that broke the raw JSON.
            protected_before = _protected_values(repaired)
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
            raise DossierParseError("ResearchDossier must be a JSON object")
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


def _remove_raw_control_characters_from_json_keys(text: str) -> tuple[str, int]:
    """Delete raw JSON control characters only from object member names.

    Visible browser code blocks can insert a hard line break immediately before
    a member-name closing quote, for example ``"issuer_scoped\n": true``.
    JSON forbids that raw control character even though the key identity is
    otherwise intact.  Values are deliberately left untouched: deleting a line
    break from a statement or supporting excerpt would mutate evidence content.
    The schema validator remains responsible for rejecting any repaired key that
    is not part of the dossier contract.
    """

    output: list[str] = []
    removed = 0
    index = 0
    while index < len(text):
        if text[index] != '"':
            output.append(text[index])
            index += 1
            continue

        end = index + 1
        escaped = False
        while end < len(text):
            character = text[end]
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                break
            end += 1
        if end >= len(text):
            output.append(text[index:])
            break

        lookahead = end + 1
        while lookahead < len(text) and text[lookahead].isspace():
            lookahead += 1
        is_object_key = lookahead < len(text) and text[lookahead] == ":"
        token = text[index : end + 1]
        if is_object_key:
            cleaned = "".join(
                character
                for character in token
                if not (ord(character) < 0x20 and character not in {'"', "\\"})
            )
            removed += len(token) - len(cleaned)
            output.append(cleaned)
        else:
            output.append(token)
        index = end + 1
    return "".join(output), removed


def _escape_raw_control_characters_in_json_string_values(
    text: str,
) -> tuple[str, int]:
    """Make raw controls JSON-safe while preserving decoded value content.

    A raw newline inside a JSON string is invalid syntax.  Replacing that one
    character with the two-byte JSON encoding ``\\n`` does not delete or infer
    text: ``json.loads`` decodes it back to the same newline.  Object keys are
    excluded because their schema identity is handled by the narrower key
    normalizer above.
    """

    escapes = {
        "\b": "\\b",
        "\f": "\\f",
        "\n": "\\n",
        "\r": "\\r",
        "\t": "\\t",
    }
    output: list[str] = []
    escaped_count = 0
    index = 0
    while index < len(text):
        if text[index] != '"':
            output.append(text[index])
            index += 1
            continue

        end = index + 1
        escaped = False
        while end < len(text):
            character = text[end]
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                break
            end += 1
        if end >= len(text):
            output.append(text[index:])
            break

        lookahead = end + 1
        while lookahead < len(text) and text[lookahead].isspace():
            lookahead += 1
        is_object_key = lookahead < len(text) and text[lookahead] == ":"
        token = text[index : end + 1]
        if not is_object_key:
            repaired_token: list[str] = []
            for character in token:
                if ord(character) < 0x20:
                    repaired_token.append(
                        escapes.get(character, f"\\u{ord(character):04x}")
                    )
                    escaped_count += 1
                else:
                    repaired_token.append(character)
            output.append("".join(repaired_token))
        else:
            output.append(token)
        index = end + 1
    return "".join(output), escaped_count


def _escape_decoder_proven_naked_quotes_in_json_string_values(
    text: str,
    *,
    max_repairs: int = 32,
) -> tuple[str, int]:
    """Escape only quotes that the JSON decoder proves ended a value early.

    A visible ChatGPT code block can preserve a source excerpt such as
    ``(이하 "당사")`` while omitting the JSON escape bytes around the two
    inner quote characters.  Guessing quote pairs from prose would be unsafe.
    Instead, repeatedly ask the standard decoder for the exact failure point
    and repair only this narrow shape:

    * the decoder reports ``Expecting ',' delimiter``;
    * the failing token follows an unescaped quote, with only optional
      whitespace between them;
    * that quote was opened inside an existing JSON string value; and
    * the failing character is not JSON structure.

    Prefixing that literal quote with ``\\`` changes only its JSON encoding;
    ``json.loads`` decodes the evidence value back to the original quote.  A
    missing comma, malformed key, or any other structural defect remains a
    hard parse failure.
    """

    repaired = text
    repair_count = 0
    while repair_count < max_repairs:
        try:
            json.loads(repaired)
            return repaired, repair_count
        except json.JSONDecodeError as error:
            quote_index = error.pos - 1
            while quote_index >= 0 and repaired[quote_index].isspace():
                quote_index -= 1
            if (
                error.msg != "Expecting ',' delimiter"
                or quote_index < 0
                or repaired[quote_index] != '"'
                or error.pos >= len(repaired)
                or repaired[error.pos] in '"{}[],: '
                or any(
                    not character.isspace()
                    for character in repaired[quote_index + 1 : error.pos]
                )
                or _is_escaped_character(repaired, quote_index)
                or not _quote_is_inside_json_string(repaired, quote_index)
            ):
                return repaired, repair_count
            repaired = repaired[:quote_index] + "\\" + repaired[quote_index:]
            repair_count += 1
    return repaired, repair_count


def _is_escaped_character(text: str, index: int) -> bool:
    backslash_count = 0
    cursor = index - 1
    while cursor >= 0 and text[cursor] == "\\":
        backslash_count += 1
        cursor -= 1
    return backslash_count % 2 == 1


def _quote_is_inside_json_string(text: str, quote_index: int) -> bool:
    in_string = False
    escaped = False
    for character in text[:quote_index]:
        if escaped:
            escaped = False
            continue
        if character == "\\" and in_string:
            escaped = True
            continue
        if character == '"':
            in_string = not in_string
    return in_string


def _protected_values(text: str) -> Mapping[str, tuple[str, ...]]:
    return {
        field: tuple(
            _decode_json_string_fragment(match.group(1))
            for match in re.finditer(
                rf'"{re.escape(field)}"\s*:\s*"((?:\\.|[^"\\])*)"', text
            )
        )
        for field in _PROTECTED_FIELDS
    }


def _decode_json_string_fragment(value: str) -> str:
    encoded = "".join(
        {
            "\b": "\\b",
            "\f": "\\f",
            "\n": "\\n",
            "\r": "\\r",
            "\t": "\\t",
        }.get(character, f"\\u{ord(character):04x}")
        if ord(character) < 0x20
        else character
        for character in value
    )
    try:
        decoded = json.loads(f'"{encoded}"')
    except json.JSONDecodeError:
        return value
    return str(decoded)


def _text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


__all__ = [
    "DossierParseError",
    "ParsedDossier",
    "ResearchDossierParser",
]
