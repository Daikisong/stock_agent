"""Fixture-first page fetcher for web research."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Mapping


@dataclass(frozen=True)
class FetchResult:
    """Fetched document text or a clear unavailable reason."""

    url: str
    ok: bool
    text: str | None = None
    content_type: str | None = None
    fetched_at: datetime | None = None
    reason: str | None = None
    source_path: str | None = None


@dataclass(frozen=True)
class PageFetcher:
    """Fetch pages from local fixtures by default.

    Live mode is intentionally not implemented yet. Later checkpoints can add a
    Playwright or requests implementation behind the same interface.
    """

    fixture_text_by_url: Mapping[str, str | Path] | None = None
    live_enabled: bool = False

    def fetch(self, url: str, *, as_of_date: date) -> FetchResult:
        fetched_at = datetime(as_of_date.year, as_of_date.month, as_of_date.day, 8, 0)
        if self.fixture_text_by_url and url in self.fixture_text_by_url:
            value = self.fixture_text_by_url[url]
            if isinstance(value, Path) or (isinstance(value, str) and _path_exists(value)):
                path = Path(value)
                return FetchResult(
                    url=url,
                    ok=True,
                    text=path.read_text(encoding="utf-8"),
                    content_type="text/plain",
                    fetched_at=fetched_at,
                    source_path=str(path),
                )
            return FetchResult(
                url=url,
                ok=True,
                text=str(value),
                content_type="text/plain",
                fetched_at=fetched_at,
            )
        if not self.live_enabled:
            return FetchResult(
                url=url,
                ok=False,
                fetched_at=fetched_at,
                reason="live fetching is disabled and no fixture text was mapped for this URL",
            )
        return FetchResult(
            url=url,
            ok=False,
            fetched_at=fetched_at,
            reason="live fetching adapter is not implemented yet",
        )


def _path_exists(value: str) -> bool:
    try:
        return Path(value).exists()
    except OSError:
        return False


__all__ = ["FetchResult", "PageFetcher"]
