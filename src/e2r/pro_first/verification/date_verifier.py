"""As-of-safe source and event date resolution."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Iterable

from e2r.research.page_fetcher import FetchResult
from e2r.research.publication_date import infer_publication_date


@dataclass(frozen=True)
class SourceDateVerification:
    accepted: bool
    status: str
    claimed_published_at: str | None
    inferred_published_at: str | None
    effective_published_at: str | None


class AsOfDateVerifier:
    def verify(
        self,
        *,
        claimed_published_at: object,
        event_date: object,
        as_of_date: str,
        source_url: str,
        source_title: str,
        source_publisher: str,
        document_text: str,
        fetch_result: FetchResult,
    ) -> SourceDateVerification:
        cutoff = date.fromisoformat(as_of_date)
        try:
            claimed = _optional_date(claimed_published_at)
            event = _optional_date(event_date)
        except ValueError:
            return SourceDateVerification(False, "INVALID_DATE", None, None, None)
        metadata: Iterable[str] = (
            source_url,
            source_title,
            source_publisher,
            *fetch_result.publication_metadata_parts,
        )
        inferred = infer_publication_date(
            explicit=None,
            metadata_parts=metadata,
            document_text=document_text,
            as_of_date=cutoff,
        )
        last_modified = (
            fetch_result.response_last_modified_at.date()
            if fetch_result.response_last_modified_at is not None
            else None
        )
        dates = tuple(value for value in (claimed, inferred, event, last_modified) if value)
        if any(value > cutoff for value in dates):
            return SourceDateVerification(
                False,
                "FUTURE_SOURCE",
                claimed.isoformat() if claimed else None,
                inferred.isoformat() if inferred else None,
                max(dates).isoformat() if dates else None,
            )
        publication_dates = tuple(value for value in (claimed, inferred) if value)
        if not publication_dates:
            return SourceDateVerification(False, "UNKNOWN_PUBLICATION_DATE", None, None, None)
        effective = max(publication_dates)
        return SourceDateVerification(
            True,
            "DATE_ACCEPTED",
            claimed.isoformat() if claimed else None,
            inferred.isoformat() if inferred else None,
            effective.isoformat(),
        )


def _optional_date(value: object) -> date | None:
    if value is None or str(value).strip() == "":
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value).strip()[:10])


__all__ = ["AsOfDateVerifier", "SourceDateVerification"]
