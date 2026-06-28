"""Repository artifact discovery for Research Brain memory compilation."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, Sequence

from e2r.calibration.taxonomy import (
    CANONICAL_ARCHETYPE_IDS,
    LARGE_SECTOR_IDS,
    large_sector_for_archetype,
    normalise_canonical_archetype_id,
    normalise_large_sector_id,
)
from e2r.research_brain.schemas import ArtifactInventoryRow, sha256_file


DEFAULT_DISCOVERY_ROOTS = (
    "docs",
    "output",
    "reports/e2r_calibration",
    "fixtures/historical",
    "configs",
)
SUPPORTED_SUFFIXES = {".md", ".json", ".jsonl", ".csv", ".txt"}
_URL_RE = re.compile(r"https?://[^\s)>\]\"']+")
_ROUND_RE = re.compile(r"(?:round|Round|ROUND|R)(?:[_\-\s]?)(\d{1,4})")
_LOOP_RE = re.compile(r"(?:loop|Loop|LOOP)(?:[_\-\s]?)(\d{1,4})")


def discover_research_artifacts(
    *,
    root: str | Path = ".",
    discovery_roots: Sequence[str | Path] = DEFAULT_DISCOVERY_ROOTS,
    extra_globs: Sequence[str] = (
        "**/e2r_stock_web_v12_residual_round_*.md",
        "**/*V12*research*",
        "**/*v12*research*",
        "**/*Research*",
    ),
) -> tuple[ArtifactInventoryRow, ...]:
    base = Path(root)
    paths: dict[str, Path] = {}
    for discovery_root in discovery_roots:
        scan_root = base / discovery_root
        if scan_root.exists():
            for path in _iter_supported_files(scan_root):
                paths[str(path)] = path
    for pattern in extra_globs:
        for path in base.glob(pattern):
            if path.is_file() and _supported(path):
                paths[str(path)] = path

    rows: list[ArtifactInventoryRow] = []
    seen_hashes: set[str] = set()
    for path in sorted(paths.values(), key=lambda item: str(item)):
        try:
            digest = sha256_file(path)
            text = _read_text_sample(path)
            stats = path.stat()
            duplicate_count = 1 if digest in seen_hashes else 0
            seen_hashes.add(digest)
            rows.append(
                ArtifactInventoryRow(
                    path=str(path),
                    sha256=digest,
                    artifact_type=_artifact_type(path),
                    size_bytes=stats.st_size,
                    modified_time=stats.st_mtime,
                    schema_family=_detect_schema_family(path, text),
                    detected_canonical_archetype_id=_detect_archetype(path, text),
                    detected_large_sector_id=_detect_large_sector(path, text),
                    detected_round=_detect_round(path, text),
                    detected_loop=_detect_loop(path, text),
                    row_block_count=_count_row_blocks(path, text),
                    jsonl_row_count=_count_jsonl_rows(path),
                    table_row_count=_count_markdown_table_rows(text),
                    evidence_url_count=len(_URL_RE.findall(text)),
                    source_proxy_count=text.count("source_proxy_only") + text.count("source proxy"),
                    evidence_url_pending_count=text.count("evidence_url_pending") + text.count("URL pending"),
                    calibration_usable_count=_count_calibration_usable(text),
                    duplicate_count=duplicate_count,
                )
            )
        except Exception as exc:  # pragma: no cover - defensive inventory path
            rows.append(
                ArtifactInventoryRow(
                    path=str(path),
                    sha256="",
                    artifact_type=_artifact_type(path),
                    size_bytes=0,
                    parse_error_count=1,
                    parse_errors=(f"{type(exc).__name__}: {exc}",),
                )
            )
    return tuple(rows)


def inventory_summary(rows: Sequence[ArtifactInventoryRow]) -> dict[str, int]:
    return {
        "scanned_file_count": len(rows),
        "parsed_artifact_count": sum(1 for row in rows if row.parse_error_count == 0),
        "parse_error_count": sum(row.parse_error_count for row in rows),
        "duplicate_count": sum(row.duplicate_count for row in rows),
        "evidence_url_count": sum(row.evidence_url_count for row in rows),
        "source_proxy_count": sum(row.source_proxy_count for row in rows),
        "evidence_url_pending_count": sum(row.evidence_url_pending_count for row in rows),
        "table_row_count": sum(row.table_row_count for row in rows),
        "jsonl_row_count": sum(row.jsonl_row_count for row in rows),
        "calibration_usable_count": sum(row.calibration_usable_count for row in rows),
    }


def _iter_supported_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file() and _supported(path) and "__pycache__" not in path.parts:
            yield path


def _supported(path: Path) -> bool:
    return path.suffix.lower() in SUPPORTED_SUFFIXES


def _artifact_type(path: Path) -> str:
    suffix = path.suffix.lower().lstrip(".")
    if suffix in {"md", "json", "jsonl", "csv"}:
        return suffix
    return "report"


def _read_text_sample(path: Path, max_bytes: int = 512_000) -> str:
    with path.open("rb") as handle:
        data = handle.read(max_bytes)
    return data.decode("utf-8", errors="ignore")


def _detect_schema_family(path: Path, text: str) -> str:
    lower = f"{path} {text[:4_000]}".lower()
    if "research_memory" in lower:
        return "research_memory"
    if "evidence_os" in lower or "agentic" in lower:
        return "evidence_os"
    if "v12" in lower or "round" in lower or "archetype" in lower:
        return "v12_research"
    if "score" in lower and "stage" in lower:
        return "score_stage_report"
    return "unknown"


def _detect_archetype(path: Path, text: str) -> str | None:
    haystack = f"{path} {text[:20_000]}"
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        if archetype_id in haystack:
            return archetype_id
    match = re.search(r"\b(C\d{2}_[A-Z0-9_]+|R13_[A-Z0-9_]+)\b", haystack)
    if match:
        return normalise_canonical_archetype_id(match.group(1))
    return None


def _detect_large_sector(path: Path, text: str) -> str | None:
    haystack = f"{path} {text[:20_000]}"
    for sector_id in LARGE_SECTOR_IDS:
        if sector_id in haystack:
            return sector_id
    match = re.search(r"\b(L\d{1,2}_[A-Z0-9_]+)\b", haystack)
    if match:
        return normalise_large_sector_id(match.group(1))
    archetype_id = _detect_archetype(path, text)
    return large_sector_for_archetype(archetype_id) if archetype_id else None


def _detect_round(path: Path, text: str) -> str | None:
    match = _ROUND_RE.search(str(path)) or _ROUND_RE.search(text[:4_000])
    return f"R{match.group(1)}" if match else None


def _detect_loop(path: Path, text: str) -> int | None:
    match = _LOOP_RE.search(str(path)) or _LOOP_RE.search(text[:4_000])
    return int(match.group(1)) if match else None


def _count_row_blocks(path: Path, text: str) -> int:
    if path.suffix.lower() == ".jsonl":
        return _count_jsonl_rows(path)
    if path.suffix.lower() == ".csv":
        return max(0, text.count("\n"))
    return text.count("```") // 2 + _count_markdown_table_rows(text)


def _count_jsonl_rows(path: Path) -> int:
    if path.suffix.lower() != ".jsonl":
        return 0
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            return sum(1 for line in handle if line.strip())
    except OSError:
        return 0


def _count_markdown_table_rows(text: str) -> int:
    count = 0
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|") and "---" not in stripped:
            count += 1
    return max(0, count - 1)


def _count_calibration_usable(text: str) -> int:
    tokens = (
        "production_ready_evidence",
        "fixture_usable",
        "url_backed",
        "source_url",
        "evidence_url",
        "accepted_claim",
    )
    lower = text.lower()
    return sum(lower.count(token.lower()) for token in tokens)


__all__ = ["DEFAULT_DISCOVERY_ROOTS", "discover_research_artifacts", "inventory_summary"]
