"""Provider registry used by the production cutover gate.

The registry does not pretend that a stored ``snapshot://`` document is live.
That distinction is the whole point of the gate.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Protocol, Sequence


@dataclass(frozen=True)
class SourceFetchResult:
    provider_name: str
    source_class: str
    mode: str
    request_id: str
    request_params: Mapping[str, Any] = field(default_factory=dict)
    status: str = "PROVIDER_FAILED"
    canonical_url: str | None = None
    official_document_id: str | None = None
    published_at: str | None = None
    available_at: str | None = None
    fetched_at: str | None = None
    content_hash: str | None = None
    raw_text: str = ""
    structured_payload: Mapping[str, Any] = field(default_factory=dict)
    provider_error: str | None = None
    snapshot_run_id: str | None = None
    source_fetch_request_id: str | None = None

    @property
    def has_content_anchor(self) -> bool:
        return bool(self.content_hash and (self.canonical_url or self.official_document_id))

    @property
    def counts_as_live(self) -> bool:
        if self.canonical_url and self.canonical_url.startswith("snapshot://"):
            return False
        return self.mode == "live" and self.status == "FETCHED" and self.has_content_anchor

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class BaseProductionSourceConnector(Protocol):
    provider_name: str
    source_class: str

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        ...


class LocalSnapshotConnector:
    """Read a provider cache as a snapshot result, never as live evidence."""

    provider_name: str
    source_class: str
    path_patterns: tuple[str, ...]

    def __init__(
        self,
        *,
        provider_name: str,
        source_class: str,
        repo_root: str | Path,
        path_patterns: Sequence[str],
    ) -> None:
        self.provider_name = provider_name
        self.source_class = source_class
        self.repo_root = Path(repo_root)
        self.path_patterns = tuple(path_patterns)

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        request_id = _stable_id("SRCREQ", self.provider_name, symbol, as_of_date.isoformat(), mode)
        if mode == "live":
            return SourceFetchResult(
                provider_name=self.provider_name,
                source_class=self.source_class,
                mode="live",
                request_id=request_id,
                request_params={"symbol": symbol, "company_name": company_name},
                status="PROVIDER_FAILED",
                fetched_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
                provider_error="live_connector_not_configured_in_local_environment",
            )
        for pattern in self.path_patterns:
            for path in sorted(self.repo_root.glob(pattern.format(symbol=symbol))):
                text = _read_text_or_json(path)
                if not text.strip():
                    continue
                content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
                return SourceFetchResult(
                    provider_name=self.provider_name,
                    source_class=self.source_class,
                    mode="snapshot",
                    request_id=request_id,
                    request_params={"symbol": symbol, "company_name": company_name, "path": str(path)},
                    status="FETCHED",
                    canonical_url=f"snapshot://{self.provider_name}/{path.name}",
                    official_document_id=None,
                    published_at=_date_from_path(path, as_of_date).isoformat(),
                    available_at=_date_from_path(path, as_of_date).isoformat(),
                    fetched_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
                    content_hash=content_hash,
                    raw_text=text[:200_000],
                    structured_payload={"snapshot_path": str(path), "symbol": symbol, "company_name": company_name},
                    snapshot_run_id=_stable_id("SNAPSHOT", self.provider_name, str(path)),
                    source_fetch_request_id=request_id,
                )
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode="snapshot" if mode != "frozen" else "frozen",
            request_id=request_id,
            request_params={"symbol": symbol, "company_name": company_name},
            status="NO_RESULT",
            fetched_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
            provider_error="no_local_provider_snapshot_found",
        )


class SourceProviderRegistry:
    def __init__(self, connectors: Sequence[BaseProductionSourceConnector]) -> None:
        self._connectors = tuple(connectors)

    @property
    def connectors(self) -> tuple[BaseProductionSourceConnector, ...]:
        return self._connectors

    def fetch_all(
        self,
        *,
        symbol: str,
        company_name: str,
        as_of_date: date,
        mode: str,
    ) -> tuple[SourceFetchResult, ...]:
        return tuple(
            connector.fetch(symbol=symbol, company_name=company_name, as_of_date=as_of_date, mode=mode)
            for connector in self._connectors
        )

    def build_report(self, results: Sequence[SourceFetchResult]) -> Mapping[str, Any]:
        provider_call_counts: dict[str, int] = {}
        provider_failure_counts: dict[str, int] = {}
        for result in results:
            provider_call_counts[result.provider_name] = provider_call_counts.get(result.provider_name, 0) + 1
            if result.status in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED", "REJECTED_BY_POLICY"}:
                provider_failure_counts[result.provider_name] = provider_failure_counts.get(result.provider_name, 0) + 1
        return {
            "schema_version": "production_cutover_source_connector_report_v1",
            "summary": {
                "provider_call_counts": provider_call_counts,
                "provider_failure_counts": provider_failure_counts,
                "dart_call_count": provider_call_counts.get("OpenDART", 0),
                "kind_call_count": provider_call_counts.get("KIND", 0),
                "krx_call_count": provider_call_counts.get("KRX", 0),
                "companyguide_call_count": provider_call_counts.get("CompanyGuide", 0),
                "issuer_ir_call_count": provider_call_counts.get("IssuerIR", 0),
                "trusted_news_call_count": provider_call_counts.get("TrustedNews", 0),
                "fetched_document_count": sum(result.status == "FETCHED" for result in results),
                "real_document_fetched_count": sum(result.counts_as_live for result in results),
                "live_or_fresh_provider_document_count": sum(result.counts_as_live for result in results),
                "snapshot_only_document_count": sum(
                    result.status == "FETCHED" and result.mode in {"snapshot", "frozen"} for result in results
                ),
                "provider_failure_count": sum(
                    result.status in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED", "REJECTED_BY_POLICY"}
                    for result in results
                ),
                "snapshot_only_counted_as_live_count": sum(
                    result.mode in {"snapshot", "frozen"} and result.counts_as_live for result in results
                ),
            },
            "rows": [result.to_dict() for result in results],
        }


def build_default_source_provider_registry(repo_root: str | Path = ".") -> SourceProviderRegistry:
    root = Path(repo_root)
    return SourceProviderRegistry(
        connectors=(
            LocalSnapshotConnector(
                provider_name="OpenDART",
                source_class="DART",
                repo_root=root,
                path_patterns=("data/raw/opendart/disclosures/*.csv", "data/raw/korea_cheap_scan/opendart/disclosures/*.csv"),
            ),
            LocalSnapshotConnector(
                provider_name="KIND",
                source_class="KIND",
                repo_root=root,
                path_patterns=("data/raw/kind/risk_flags/*.csv", "data/raw/korea_cheap_scan/kind/risk_flags/*.csv"),
            ),
            LocalSnapshotConnector(
                provider_name="KRX",
                source_class="KRX",
                repo_root=root,
                path_patterns=("data/raw/krx/instruments/*.csv", "data/raw/krx/prices/{symbol}.csv"),
            ),
            LocalSnapshotConnector(
                provider_name="CompanyGuide",
                source_class="CompanyGuide",
                repo_root=root,
                path_patterns=(
                    "data/cache/company_guide/*/{symbol}_recent_reports.json",
                    "data/cache/company_guide/*/{symbol}_snapshot.html",
                ),
            ),
            LocalSnapshotConnector(
                provider_name="IssuerIR",
                source_class="IR",
                repo_root=root,
                path_patterns=("data/raw/search_html/text/*.txt",),
            ),
            LocalSnapshotConnector(
                provider_name="TrustedNews",
                source_class="TrustedNews",
                repo_root=root,
                path_patterns=("data/raw/naver_news/news/news.json", "fixtures/historical/news.json"),
            ),
        )
    )


def _read_text_or_json(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() == ".json":
        try:
            return json.dumps(json.loads(text), ensure_ascii=False, sort_keys=True)
        except json.JSONDecodeError:
            return text
    return text


def _date_from_path(path: Path, fallback: date) -> date:
    for part in reversed(path.parts):
        try:
            return datetime.fromisoformat(part[:10]).date()
        except ValueError:
            continue
    return fallback


def _stable_id(prefix: str, *parts: object) -> str:
    digest = hashlib.sha256("|".join(str(part) for part in parts).encode("utf-8")).hexdigest()[:20]
    return f"{prefix}-{digest}"


__all__ = [
    "BaseProductionSourceConnector",
    "LocalSnapshotConnector",
    "SourceFetchResult",
    "SourceProviderRegistry",
    "build_default_source_provider_registry",
]
