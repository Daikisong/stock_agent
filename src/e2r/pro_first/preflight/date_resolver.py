"""Published-date precedence over transport Last-Modified metadata."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Mapping

from e2r.research.page_fetcher import FetchResult


@dataclass(frozen=True)
class DatePrecedenceResolution:
    accepted: bool
    status: str
    publication_date: str | None
    availability_date: str | None
    last_modified_date: str | None
    effective_publication_date: str | None
    last_modified_ignored: bool


class DatePrecedenceResolver:
    def resolve(
        self,
        *,
        source_document: Mapping[str, object],
        fetch_result: FetchResult,
        as_of_date: str,
    ) -> DatePrecedenceResolution:
        cutoff = date.fromisoformat(as_of_date)
        try:
            publication = _optional_date(source_document.get("publication_date"))
            availability = _optional_date(source_document.get("availability_date"))
        except ValueError:
            return DatePrecedenceResolution(
                False, "INVALID_SOURCE_DATE", None, None, None, None, False
            )
        last_modified = (
            fetch_result.response_last_modified_at.date()
            if fetch_result.response_last_modified_at is not None
            else None
        )
        if publication is None:
            if last_modified is None or last_modified > cutoff:
                return DatePrecedenceResolution(
                    False,
                    "PUBLICATION_DATE_UNRESOLVED",
                    None,
                    availability.isoformat() if availability else None,
                    last_modified.isoformat() if last_modified else None,
                    None,
                    False,
                )
            publication = last_modified
        if publication > cutoff or (
            availability is not None and availability > cutoff
        ):
            return DatePrecedenceResolution(
                False,
                "FUTURE_SOURCE",
                publication.isoformat(),
                availability.isoformat() if availability else None,
                last_modified.isoformat() if last_modified else None,
                publication.isoformat(),
                False,
            )
        if availability is not None and availability < publication:
            return DatePrecedenceResolution(
                False,
                "AVAILABILITY_PRECEDES_PUBLICATION",
                publication.isoformat(),
                availability.isoformat(),
                last_modified.isoformat() if last_modified else None,
                publication.isoformat(),
                False,
            )
        ignored = bool(last_modified is not None and last_modified != publication)
        return DatePrecedenceResolution(
            True,
            "PUBLISHED_DATE_ACCEPTED",
            publication.isoformat(),
            availability.isoformat() if availability else publication.isoformat(),
            last_modified.isoformat() if last_modified else None,
            publication.isoformat(),
            ignored,
        )


def _optional_date(value: object) -> date | None:
    if value is None or not str(value).strip():
        return None
    return date.fromisoformat(str(value).strip()[:10])


__all__ = ["DatePrecedenceResolution", "DatePrecedenceResolver"]
