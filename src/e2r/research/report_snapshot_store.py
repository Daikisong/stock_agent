"""Point-in-time fetched report/document snapshot storage."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, fields, is_dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class ReportSnapshot:
    """Stored fetched document metadata and extracted text hash."""

    url: str
    title: str
    symbol: str | None
    company_name: str | None
    fetched_at: datetime
    as_of_date: date
    source_type: str
    extracted_text_hash: str
    extracted_text_path: str | None
    evidence_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "evidence_ids", tuple(self.evidence_ids))


class ReportSnapshotStore:
    """JSONL-backed report snapshot store."""

    def __init__(self, root: str | Path = "data/report_snapshots") -> None:
        self.root = Path(root)

    def save_text_snapshot(
        self,
        *,
        url: str,
        title: str,
        text: str,
        fetched_at: datetime,
        as_of_date: date,
        symbol: str | None = None,
        company_name: str | None = None,
        source_type: str = "report",
        evidence_ids: Sequence[str] = (),
    ) -> ReportSnapshot:
        self.root.mkdir(parents=True, exist_ok=True)
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        text_path = self.root / f"{text_hash}.txt"
        text_path.write_text(text, encoding="utf-8")
        snapshot = ReportSnapshot(
            url=url,
            title=title,
            symbol=symbol,
            company_name=company_name,
            fetched_at=fetched_at,
            as_of_date=as_of_date,
            source_type=source_type,
            extracted_text_hash=text_hash,
            extracted_text_path=str(text_path),
            evidence_ids=tuple(evidence_ids),
        )
        self._append(snapshot)
        return snapshot

    def save_snapshot(self, snapshot: ReportSnapshot) -> Path:
        """Append one prepared snapshot."""

        self.root.mkdir(parents=True, exist_ok=True)
        self._append(snapshot)
        return self.root / "report_snapshots.jsonl"

    def load(
        self,
        *,
        as_of_date: date | None = None,
        symbol: str | None = None,
        company_name: str | None = None,
    ) -> tuple[ReportSnapshot, ...]:
        path = self.root / "report_snapshots.jsonl"
        if not path.exists():
            return ()
        rows: list[ReportSnapshot] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = report_snapshot_from_mapping(json.loads(line))
            if as_of_date is not None and item.as_of_date > as_of_date:
                continue
            if symbol is not None and item.symbol != symbol:
                continue
            if company_name is not None and item.company_name != company_name:
                continue
            rows.append(item)
        return tuple(rows)

    def load_snapshots(
        self,
        *,
        as_of_date: date | None = None,
        symbol: str | None = None,
        company_name: str | None = None,
    ) -> tuple[ReportSnapshot, ...]:
        """Load report snapshots visible as of a replay date."""

        return self.load(as_of_date=as_of_date, symbol=symbol, company_name=company_name)

    def text_for_snapshot(self, snapshot: ReportSnapshot) -> str | None:
        if not snapshot.extracted_text_path:
            return None
        path = Path(snapshot.extracted_text_path)
        if not path.is_absolute():
            path = self.root / path
        if not path.exists():
            return None
        return path.read_text(encoding="utf-8")

    def fixture_text_by_url(
        self,
        *,
        as_of_date: date | None = None,
        symbol: str | None = None,
        company_name: str | None = None,
    ) -> Mapping[str, str | Path]:
        """Return URL -> local text mapping for ``PageFetcher``."""

        mapping: dict[str, str | Path] = {}
        for item in self.load_snapshots(as_of_date=as_of_date, symbol=symbol, company_name=company_name):
            if not item.extracted_text_path:
                continue
            path = Path(item.extracted_text_path)
            mapping[item.url] = path if path.is_absolute() else self.root / path
        return mapping

    def _append(self, snapshot: ReportSnapshot) -> None:
        path = self.root / "report_snapshots.jsonl"
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(_jsonable(snapshot), ensure_ascii=False, sort_keys=True) + "\n")


def report_snapshot_from_mapping(row: Mapping[str, Any]) -> ReportSnapshot:
    return ReportSnapshot(
        url=str(row["url"]),
        title=str(row["title"]),
        symbol=row.get("symbol"),
        company_name=row.get("company_name"),
        fetched_at=datetime.fromisoformat(str(row["fetched_at"])),
        as_of_date=date.fromisoformat(str(row["as_of_date"])),
        source_type=str(row["source_type"]),
        extracted_text_hash=str(row["extracted_text_hash"]),
        extracted_text_path=row.get("extracted_text_path"),
        evidence_ids=tuple(row.get("evidence_ids") or ()),
    )


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if is_dataclass(value):
        return {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    return value


__all__ = ["ReportSnapshot", "ReportSnapshotStore", "report_snapshot_from_mapping"]
