"""Manual URL or file fallback provider for free web research."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Mapping, Sequence

from e2r.research.search_provider import SearchResult
from e2r.sources.source_errors import datetime_value


@dataclass(frozen=True)
class ManualSource:
    """Manually supplied source metadata and optional local text."""

    title: str
    url: str
    source: str = "manual-source"
    snippet: str | None = None
    published_at: datetime | date | str | None = None
    queries: Sequence[str] = field(default_factory=tuple)
    text: str | None = None
    file_path: str | Path | None = None
    is_pdf: bool = False
    is_report_domain: bool = False
    is_news: bool = False
    is_disclosure: bool = False
    confidence: float = 0.65


@dataclass(frozen=True)
class ManualSourceProvider:
    """SearchProvider-compatible manual fallback."""

    sources: Sequence[ManualSource] = field(default_factory=tuple)

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        results: list[SearchResult] = []
        for index, source in enumerate(self.sources, start=1):
            if source.queries and query not in source.queries:
                continue
            published = datetime_value(source.published_at) if source.published_at else None
            if published is not None and published.date() > as_of_date:
                continue
            results.append(
                SearchResult(
                    title=source.title,
                    url=source.url,
                    snippet=source.snippet,
                    source=source.source,
                    published_at=published,
                    query=query,
                    rank=index,
                    is_pdf=source.is_pdf,
                    is_report_domain=source.is_report_domain,
                    is_news=source.is_news,
                    is_disclosure=source.is_disclosure,
                    confidence=source.confidence,
                )
            )
        return tuple(results[:max_results])

    def fixture_text_by_url(self) -> Mapping[str, str | Path]:
        mapping: dict[str, str | Path] = {}
        for source in self.sources:
            if source.text is not None:
                mapping[source.url] = source.text
            elif source.file_path is not None:
                mapping[source.url] = source.file_path
        return mapping


__all__ = ["ManualSource", "ManualSourceProvider"]
