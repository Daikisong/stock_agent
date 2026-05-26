"""Markdown discovery for Stock-Web historical calibration result files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import re


PROMPT_SPEC_TERMS = (
    "prompt",
    "프롬프트",
    "calibration_prompt",
    "historical_calibration_prompt",
    "최종프롬프트",
    "e2r historical calibration prompt",
    "e2r post-ohlc breakthrough historical calibration prompt",
    "단일 프롬프트 시작",
)

SCHEMA_V11 = "v11_global_calibration"
SCHEMA_V12 = "v12_sector_archetype_residual"

V11_RESULT_PATTERNS = (
    re.compile(r"e2r_stock_web_historical_calibration_round_R\d+_loop_\d+_.*\.md$", re.IGNORECASE),
    re.compile(r"e2r_stock_web_historical_calibration_round_.*_loop_.*_.*\.md$", re.IGNORECASE),
    re.compile(r".*stock_web_historical_calibration_round_R\d+_loop_.*\.md$", re.IGNORECASE),
)
V12_RESULT_PATTERNS = (
    re.compile(r"e2r_stock_web_v12_residual_round_.*_loop_.*_.*_research.*\.md$", re.IGNORECASE),
    re.compile(r".*stock_web_v12_residual_round_.*_research.*\.md$", re.IGNORECASE),
    re.compile(r".*v12_residual_round_.*_research.*\.md$", re.IGNORECASE),
)

ROUND_LOOP_RE = re.compile(r"round[_-]?(R?\d+)_loop[_-]?(\d+)", re.IGNORECASE)
V12_FILENAME_RE = re.compile(
    r"v12_residual_round_(?P<round>R?\d+)_loop_(?P<loop>\d+)_(?P<large>L\d+_[A-Z0-9_]+?)_(?P<canonical>C\d+_[A-Z0-9_]+?)(?:_research.*)?\.md$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class MarkdownDocument:
    path: Path
    sha256: str
    is_result: bool
    is_prompt_spec: bool
    exclusion_reason: str | None
    round: str | None
    loop: str | None
    schema_family: str | None = None
    filename: str | None = None
    large_sector_id: str | None = None
    canonical_archetype_id: str | None = None
    fine_archetype_id: str | None = None


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _document_title_head(text_head: str) -> str:
    headings: list[str] = []
    for line in text_head.splitlines()[:40]:
        stripped = line.strip()
        if stripped.startswith("#"):
            headings.append(stripped.lstrip("#").strip())
        if len(headings) >= 2:
            break
    return "\n".join(headings)


def _contains_prompt_spec_marker(path: Path, text_head: str) -> bool:
    # The generated result MDs often contain a later "Deferred Coding Agent
    # Handoff Prompt" section. The goal excludes prompt/spec files by filename
    # or document title, not by any later section heading.
    haystack = f"{path.name}\n{_document_title_head(text_head)}".lower()
    return any(term.lower() in haystack for term in PROMPT_SPEC_TERMS)


def _is_generated_result_file(path: Path) -> bool:
    name = path.name
    return any(pattern.match(name) for pattern in V11_RESULT_PATTERNS + V12_RESULT_PATTERNS)


def _schema_family(path: Path) -> str | None:
    name = path.name
    if any(pattern.match(name) for pattern in V12_RESULT_PATTERNS):
        return SCHEMA_V12
    if any(pattern.match(name) for pattern in V11_RESULT_PATTERNS):
        return SCHEMA_V11
    return None


def _parse_round_loop(path: Path, text_head: str) -> tuple[str | None, str | None]:
    match = ROUND_LOOP_RE.search(path.name)
    if match:
        round_value = match.group(1).upper()
        if not round_value.startswith("R"):
            round_value = f"R{int(round_value)}"
        return round_value, str(int(match.group(2)))

    round_value: str | None = None
    loop_value: str | None = None
    for raw_line in text_head.splitlines():
        line = raw_line.strip()
        if "=" not in line:
            continue
        key, value = [part.strip() for part in line.split("=", 1)]
        if key == "round":
            round_value = value.upper()
            if round_value and not round_value.startswith("R") and round_value.isdigit():
                round_value = f"R{int(round_value)}"
        if key == "loop":
            loop_value = str(int(value)) if value.isdigit() else value
    return round_value, loop_value


def _parse_v12_filename_ids(path: Path) -> tuple[str | None, str | None, str | None, str | None]:
    match = V12_FILENAME_RE.search(path.name)
    if not match:
        return None, None, None, None
    round_value = match.group("round").upper()
    if not round_value.startswith("R"):
        round_value = f"R{int(round_value)}"
    return (
        round_value,
        str(int(match.group("loop"))),
        match.group("large").upper(),
        match.group("canonical").upper(),
    )


def discover_markdown_documents(root: str | Path) -> list[MarkdownDocument]:
    """Discover all MD files and classify generated calibration results.

    The function intentionally returns non-result MD files too, because the
    coverage report needs to prove prompt/spec files were excluded rather than
    silently ignored.
    """

    root_path = Path(root)
    documents: list[MarkdownDocument] = []
    for path in sorted(root_path.rglob("*.md")):
        text_head = path.read_text(encoding="utf-8", errors="replace")[:8192]
        is_prompt_spec = _contains_prompt_spec_marker(path, text_head)
        schema_family = _schema_family(path)
        is_result = _is_generated_result_file(path) and not is_prompt_spec
        exclusion_reason = None
        if is_prompt_spec:
            exclusion_reason = "prompt_spec_file_excluded"
        elif not is_result:
            exclusion_reason = "not_generated_stock_web_result_md"
        round_value, loop_value = _parse_round_loop(path, text_head)
        v12_round, v12_loop, large_sector_id, canonical_archetype_id = _parse_v12_filename_ids(path)
        round_value = v12_round or round_value
        loop_value = v12_loop or loop_value
        documents.append(
            MarkdownDocument(
                path=path,
                sha256=_sha256(path),
                is_result=is_result,
                is_prompt_spec=is_prompt_spec,
                exclusion_reason=exclusion_reason,
                round=round_value,
                loop=loop_value,
                schema_family=schema_family,
                filename=path.name,
                large_sector_id=large_sector_id,
                canonical_archetype_id=canonical_archetype_id,
            )
        )
    return documents


def result_documents(documents: list[MarkdownDocument]) -> list[MarkdownDocument]:
    return [document for document in documents if document.is_result]


def prompt_spec_documents(documents: list[MarkdownDocument]) -> list[MarkdownDocument]:
    return [document for document in documents if document.is_prompt_spec]


def v11_result_documents(documents: list[MarkdownDocument]) -> list[MarkdownDocument]:
    return [document for document in documents if document.is_result and document.schema_family == SCHEMA_V11]


def v12_result_documents(documents: list[MarkdownDocument]) -> list[MarkdownDocument]:
    return [document for document in documents if document.is_result and document.schema_family == SCHEMA_V12]
