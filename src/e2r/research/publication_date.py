"""Conservative publication-date inference for fetched research documents."""

from __future__ import annotations

import re
from datetime import date, datetime
from typing import Iterable
from urllib.parse import unquote


def infer_publication_date(
    *,
    explicit: date | datetime | None,
    metadata_parts: Iterable[str],
    document_text: str = "",
    as_of_date: date | None = None,
) -> date | None:
    """Return an auditable source date, never an arbitrary body fact date.

    Search APIs often omit a date for issuer pages and PDFs.  We accept a date
    only when it appears in URL/title metadata or on a line explicitly labelled
    as a publication/update date.  Other dates inside the article stay ignored.
    A future inferred date is deliberately returned so the caller can reject it.
    """

    if isinstance(explicit, datetime):
        return explicit.date()
    if isinstance(explicit, date):
        return explicit
    metadata = " ".join(unquote(str(item or "")) for item in metadata_parts if item)
    candidates = list(_date_candidates(metadata, as_of_date=as_of_date))
    candidates.extend(
        _labelled_publication_dates(document_text, as_of_date=as_of_date)
    )
    return max(candidates) if candidates else None


def _date_candidates(text: str, *, as_of_date: date | None) -> tuple[date, ...]:
    candidates: list[date] = []
    for match in re.finditer(
        r"(?<!\d)(20\d{2})[./_-]([01]\d)[./_-]([0-3]\d)(?!\d)",
        text,
    ):
        _append_valid(candidates, *map(int, match.groups()))
    for match in re.finditer(r"(?<!\d)(20\d{2})([01]\d)([0-3]\d)(?!\d)", text):
        _append_valid(candidates, *map(int, match.groups()))
    for match in re.finditer(
        r"(?i)(?:[/_-]|(?:article|view|news|data|html|ecn)[^0-9]{0,12})"
        r"(20\d{2})([01]\d)([0-3]\d)(?=\d{2,18}(?:\D|$))",
        text,
    ):
        _append_valid(candidates, *map(int, match.groups()))
    upper = (as_of_date.year + 1) % 100 if as_of_date is not None else 35
    for match in re.finditer(r"(?<!\d)(\d{2})([01]\d)([0-3]\d)(?!\d)", text):
        year, month, day = map(int, match.groups())
        if year <= upper:
            _append_valid(candidates, 2000 + year, month, day)
    return tuple(dict.fromkeys(candidates))


def _labelled_publication_dates(
    text: str,
    *,
    as_of_date: date | None,
) -> tuple[date, ...]:
    candidates: list[date] = []
    for raw_line in str(text or "").splitlines()[:500]:
        line = raw_line.strip()
        if not line or not _has_publication_label(line):
            continue
        candidates.extend(_date_candidates(line, as_of_date=as_of_date))
        for match in re.finditer(
            r"(?<!\d)(20\d{2})([01]\d)([0-3]\d)(?=\d{2,6}(?:\D|$))",
            line,
        ):
            _append_valid(candidates, *map(int, match.groups()))
    return tuple(dict.fromkeys(candidates))


def _has_publication_label(line: str) -> bool:
    normalized = re.sub(r"\s+", " ", line.strip()).lower()
    prefix = normalized[:32]
    if any(
        label in prefix
        for label in (
            "입력",
            "등록",
            "승인",
            "발행",
            "게시",
            "보도",
            "작성",
            "최종수정",
            "최종 수정",
            "수정",
            "기사입력",
            "기사 입력",
            "기사등록",
            "기사 등록",
        )
    ):
        return True
    return bool(
        re.search(
            r"(?i)^(?:published|posted|updated|publication\s+date|release\s+date|article\s+date|date)\b",
            normalized,
        )
    )


def _append_valid(values: list[date], year: int, month: int, day: int) -> None:
    try:
        values.append(date(year, month, day))
    except ValueError:
        return


__all__ = ["infer_publication_date"]
