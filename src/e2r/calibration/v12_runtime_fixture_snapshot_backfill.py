"""Backfill normal search/report snapshots from source-backed runtime fixtures."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.backtest.runtime_fixture_evidence import RuntimeFixtureEvidenceRow, RuntimeFixtureEvidenceStore
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_snapshot_store import SearchSnapshot, SearchSnapshotStore


@dataclass(frozen=True)
class RuntimeFixtureSnapshotBackfillRow:
    symbol: str
    company_name: str
    as_of_date: str
    role: str
    canonical_archetype_id: str
    url: str
    evidence_id: str


def write_v12_runtime_fixture_snapshot_backfill(
    *,
    spec_paths: Sequence[str | Path],
    search_snapshot_root: str | Path,
    report_snapshot_root: str | Path,
    project_root: str | Path | None = None,
) -> dict[str, Any]:
    """Write ordinary PIT search/report snapshots from runtime fixture rows.

    The output is still a replay fixture archive, not live production data. It
    deliberately uses the normal snapshot stores so operational replay can test
    search -> fetch -> parse -> claim-backed score without the special
    ``runtime_fixture_spec`` injection path.
    """

    fixture_store = RuntimeFixtureEvidenceStore(spec_paths, project_root=project_root)
    search_store = SearchSnapshotStore(search_snapshot_root)
    report_store = ReportSnapshotStore(report_snapshot_root)
    rows: list[RuntimeFixtureSnapshotBackfillRow] = []
    for row in fixture_store.rows:
        url = str(row.evidence.url_or_identifier or row.evidence.evidence_id)
        fetched_at = datetime(row.as_of_date.year, row.as_of_date.month, row.as_of_date.day, 9, 0)
        text = snapshot_text_from_runtime_fixture(row)
        report_snapshot = report_store.save_text_snapshot(
            url=url,
            title=row.report.title,
            text=text,
            fetched_at=fetched_at,
            as_of_date=row.as_of_date,
            symbol=row.symbol,
            company_name=row.company_name,
            source_type="broker_report" if row.report.broker else "research_report",
            evidence_ids=(row.evidence.evidence_id,),
        )
        search_store.save_snapshot(
            SearchSnapshot(
                query=_snapshot_query(row),
                search_date=row.as_of_date,
                title=row.report.title,
                url=url,
                snippet=_snapshot_snippet(row),
                published_at=fetched_at,
                fetched_at=fetched_at,
                source_type="broker_report",
                extracted_text_hash=report_snapshot.extracted_text_hash,
                evidence_ids=(row.evidence.evidence_id,),
                symbol=row.symbol,
                company_name=row.company_name,
            )
        )
        rows.append(
            RuntimeFixtureSnapshotBackfillRow(
                symbol=row.symbol,
                company_name=row.company_name,
                as_of_date=row.as_of_date.isoformat(),
                role=row.role,
                canonical_archetype_id=row.canonical_archetype_id,
                url=url,
                evidence_id=row.evidence.evidence_id,
            )
        )
    return {
        "schema_version": "v12_runtime_fixture_snapshot_backfill_v1",
        "snapshot_row_count": len(rows),
        "search_snapshot_root": str(search_snapshot_root),
        "report_snapshot_root": str(report_snapshot_root),
        "rows": [asdict(row) for row in rows],
    }


def snapshot_text_from_runtime_fixture(row: RuntimeFixtureEvidenceRow) -> str:
    fields = _snapshot_source_backed_fields(row.report.parsed_fields)
    lines = [
        row.report.title,
        f"{row.company_name} ({row.symbol}) {row.canonical_archetype_id} {row.role} source-backed fixture",
        "",
        row.report.raw_text or row.evidence.excerpt_or_value,
        "",
        "BEGIN_E2R_SOURCE_BACKED_FIELDS",
    ]
    for key in sorted(fields):
        lines.append(f"E2R_SOURCE_BACKED_FIELD {key}={json.dumps(fields[key], ensure_ascii=False, sort_keys=True)}")
    lines.append("END_E2R_SOURCE_BACKED_FIELDS")
    return "\n".join(lines) + "\n"


def _snapshot_source_backed_fields(fields: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in fields.items():
        key_text = str(key)
        if not _is_snapshot_field_key(key_text):
            continue
        if not _is_snapshot_field_value(value):
            continue
        result[key_text] = value
    return result


def _is_snapshot_field_key(key: str) -> bool:
    if not key or not key[0].isalpha():
        return False
    if any(key.startswith(prefix) for prefix in ("claim_", "compiled_", "raw_", "source_")):
        return False
    if key in {
        "as_of_date",
        "broker",
        "date_verified",
        "green_allowed_by_date",
        "parser_confidence",
        "runtime_fixture_source_backed",
        "title",
        "url",
    }:
        return False
    return all(ch.isalnum() or ch == "_" for ch in key)


def _is_snapshot_field_value(value: Any) -> bool:
    if value is None or value == "":
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float, str)):
        return True
    return False


def _snapshot_query(row: RuntimeFixtureEvidenceRow) -> str:
    primitives = " ".join(str(item) for item in row.report.parsed_fields.get("source_runtime_primitives", ())[:6])
    return " ".join(
        part
        for part in (
            row.company_name,
            row.symbol,
            row.canonical_archetype_id,
            primitives,
            "source backed evidence",
        )
        if part
    )


def _snapshot_snippet(row: RuntimeFixtureEvidenceRow) -> str:
    primitives = ", ".join(str(item) for item in row.report.parsed_fields.get("source_runtime_primitives", ())[:8])
    return f"{row.company_name} {row.canonical_archetype_id} {row.role} fixture: {primitives}"


__all__ = [
    "RuntimeFixtureSnapshotBackfillRow",
    "snapshot_text_from_runtime_fixture",
    "write_v12_runtime_fixture_snapshot_backfill",
]
