"""Conservative publication-date inference for fetched research documents."""

from __future__ import annotations

import re
from datetime import date, datetime
from typing import Iterable
from urllib.parse import unquote


PUBLICATION_DATE_INFERENCE_SEMANTICS_VERSION = (
    "e2r_publication_date_inference_v4"
)

_ENGLISH_MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}
_ENGLISH_MONTH_PATTERN = "|".join(
    sorted(_ENGLISH_MONTHS, key=len, reverse=True)
)


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
    if not candidates:
        candidates.extend(
            _leading_release_publication_dates(
                document_text,
                as_of_date=as_of_date,
            )
        )
    return max(candidates) if candidates else None


def infer_source_locator_publication_date(locator: str) -> date | None:
    """Return only a high-confidence publication date encoded by a URL route.

    Unlike :func:`infer_publication_date`, this helper deliberately ignores
    arbitrary filename dates.  A certificate filename may contain its future
    expiry date, which is not the publication date.  Accepted locator forms
    are named filing receipt parameters, date-segmented official routes, and
    article/news/view routes whose identifier begins with YYYYMMDD.
    """

    text = unquote(str(locator or ""))
    candidates: list[date] = []
    for match in re.finditer(
        r"(?i)(?:rcpno|rcept[_-]?no)\s*[=:/_-]\s*"
        r"(20\d{2})([01]\d)([0-3]\d)(?=\d{2,18}(?:\D|$))",
        text,
    ):
        _append_valid(candidates, *map(int, match.groups()))
    for match in re.finditer(
        r"/(20\d{2})/([01]\d)/([0-3]\d)(?:/|$)",
        text,
    ):
        _append_valid(candidates, *map(int, match.groups()))
    for match in re.finditer(
        r"(?i)(?:article|view|news|data|html|ecn)[^?#]{0,96}?[/=_-]"
        r"(20\d{2})([01]\d)([0-3]\d)(?=\d{2,18}(?:\D|$))",
        text,
    ):
        _append_valid(candidates, *map(int, match.groups()))
    return max(candidates) if candidates else None


def _date_candidates(text: str, *, as_of_date: date | None) -> tuple[date, ...]:
    candidates: list[date] = []
    # DART receipt numbers start with the filing date (YYYYMMDD) followed by
    # a sequence number.  The trailing digits intentionally make the generic
    # bare-date patterns reject them, so recognize only the named official
    # locator parameter here.  This is source-protocol metadata, not a company
    # or archetype-specific heuristic.
    for match in re.finditer(
        r"(?i)(?:rcpno|rcept[_-]?no)\s*[=:/_-]\s*"
        r"(20\d{2})([01]\d)([0-3]\d)(?=\d{2,18}(?:\D|$))",
        text,
    ):
        _append_valid(candidates, *map(int, match.groups()))
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
    for match in re.finditer(
        rf"(?i)\b({_ENGLISH_MONTH_PATTERN})\.?\s+([0-3]?\d)"
        rf"(?:st|nd|rd|th)?\s*,?\s+(20\d{{2}})\b",
        text,
    ):
        month_name, day, year = match.groups()
        _append_valid(
            candidates,
            int(year),
            _ENGLISH_MONTHS[month_name.casefold()],
            int(day),
        )
    for match in re.finditer(
        rf"(?i)\b([0-3]?\d)(?:st|nd|rd|th)?\s+"
        rf"({_ENGLISH_MONTH_PATTERN})\.?\s*,?\s+(20\d{{2}})\b",
        text,
    ):
        day, month_name, year = match.groups()
        _append_valid(
            candidates,
            int(year),
            _ENGLISH_MONTHS[month_name.casefold()],
            int(day),
        )
    return tuple(dict.fromkeys(candidates))


def _labelled_publication_dates(
    text: str,
    *,
    as_of_date: date | None,
) -> tuple[date, ...]:
    strong_candidates: list[date] = []
    fallback_candidates: list[date] = []
    lines = str(text or "").splitlines()[:500]
    for index, raw_line in enumerate(lines):
        line = raw_line.strip()
        label_strength = _publication_label_strength(line)
        if not line or label_strength is None:
            continue
        candidates = list(_date_candidates(line, as_of_date=as_of_date))
        for match in re.finditer(
            r"(?<!\d)(20\d{2})([01]\d)([0-3]\d)(?=\d{2,6}(?:\D|$))",
            line,
        ):
            _append_valid(candidates, *map(int, match.groups()))
        if not candidates:
            # Many Korean news pages render the metadata label and value as
            # separate DOM text nodes, for example ``입력\n2025-09-24 13:34``.
            # The date is still explicit article metadata, not an arbitrary
            # body date.  Inspect only the immediately following non-empty
            # line so the label cannot capture a later body statistic.
            for next_raw_line in lines[index + 1 : index + 3]:
                next_line = next_raw_line.strip()
                if not next_line:
                    continue
                candidates.extend(
                    _date_candidates(next_line, as_of_date=as_of_date)
                )
                for match in re.finditer(
                    r"(?<!\d)(20\d{2})([01]\d)([0-3]\d)(?=\d{2,6}(?:\D|$))",
                    next_line,
                ):
                    _append_valid(candidates, *map(int, match.groups()))
                break
        destination = (
            strong_candidates
            if label_strength == "STRONG"
            else fallback_candidates
        )
        destination.extend(candidates)
    # Article-specific labels such as 입력/기사입력/Updated outrank generic
    # footer labels such as 등록일자 or 발행일자.  Without this precedence a
    # site's 2016 newspaper-registration date can overwrite a 2025 article
    # date and corrupt relative periods such as "내년".
    selected = strong_candidates or fallback_candidates
    return tuple(dict.fromkeys(selected))


def _publication_label_strength(line: str) -> str | None:
    normalized = re.sub(r"\s+", " ", line.strip()).lower()
    prefix = normalized[:32]
    if any(
        label in prefix
        for label in (
            "입력",
            "송고",
            "최종수정",
            "최종 수정",
            "수정",
            "기사입력",
            "기사 입력",
            "기사등록",
            "기사 등록",
        )
    ):
        return "STRONG"
    if re.search(
        r"(?i)^(?:published|posted|updated|publication\s+date|release\s+date|article\s+date|date)\b",
        normalized,
    ):
        return "STRONG"
    if any(
        label in prefix
        for label in (
            "등록",
            "승인",
            "발행",
            "게시",
            "보도",
            "작성",
        )
    ):
        return "FALLBACK"
    return None


def _leading_release_publication_dates(
    text: str,
    *,
    as_of_date: date | None,
) -> tuple[date, ...]:
    """Read an unlabelled date only from a release document's leading block.

    Some official newsrooms render ``Press Release`` followed by the title,
    subtitle, and a standalone date line, without exposing ``datePublished``
    metadata.  Navigation-heavy investor-relations templates may instead use
    ``Press Release Details`` and repeat their menu between that marker and the
    title.  Treating every standalone body date as publication metadata would
    be unsafe, so this route is deliberately narrow: the release marker must
    occur near the document head, only the stronger details-page marker gets a
    modestly wider menu allowance, its date must be followed immediately by a
    release-download marker, and article/footer boundaries end the search.
    """

    lines = tuple(
        line.strip()
        for line in str(text or "").splitlines()
        if line.strip()
    )
    marker_index: int | None = None
    details_marker = False
    marker_window_end_offset = 25
    for index, line in enumerate(lines[:80]):
        marker = re.fullmatch(
            r"(?i)(?:press|news|media)\s+releases?"
            r"(?P<details>\s+details?)?",
            re.sub(r"\s+", " ", line),
        )
        if marker is not None:
            marker_index = index
            if marker.group("details"):
                details_marker = True
                marker_window_end_offset = 40
            break
    if marker_index is None:
        return ()

    boundary = re.compile(
        r"(?i)^(?:"
        r"news\s+summary|summary|highlights?|key\s+points?"
        r"|more\s+news|related\s+news|latest\s+news"
        r"|related\s+articles?"
        r"|related\s+(?:press|news|media)\s+releases?"
        r"|media\s+contacts?|about\s+.+"
        r")\s*:?$"
    )
    candidates: list[date] = []
    for line_index in range(
        marker_index + 1,
        min(len(lines), marker_index + marker_window_end_offset),
    ):
        line = lines[line_index]
        normalized = re.sub(r"\s+", " ", line)
        if boundary.fullmatch(normalized):
            break
        candidate = _standalone_english_month_date(normalized)
        if candidate is not None:
            if details_marker and not any(
                re.match(
                    r"(?i)^download\s+this\s+"
                    r"(?:press|news|media)\s+releases?\b",
                    re.sub(r"\s+", " ", following_line),
                )
                for following_line in lines[
                    line_index + 1 : line_index + 4
                ]
            ):
                break
            candidates.append(candidate)
            break
    return tuple(candidates)


def _standalone_english_month_date(text: str) -> date | None:
    match = re.fullmatch(
        rf"(?i)({_ENGLISH_MONTH_PATTERN})\.?\s+([0-3]?\d)"
        rf"(?:st|nd|rd|th)?\s*,?\s+(20\d{{2}})",
        text,
    )
    if match is not None:
        month_name, day, year = match.groups()
        values: list[date] = []
        _append_valid(
            values,
            int(year),
            _ENGLISH_MONTHS[month_name.casefold()],
            int(day),
        )
        return values[0] if values else None
    match = re.fullmatch(
        rf"(?i)([0-3]?\d)(?:st|nd|rd|th)?\s+"
        rf"({_ENGLISH_MONTH_PATTERN})\.?\s*,?\s+(20\d{{2}})",
        text,
    )
    if match is None:
        return None
    day, month_name, year = match.groups()
    values = []
    _append_valid(
        values,
        int(year),
        _ENGLISH_MONTHS[month_name.casefold()],
        int(day),
    )
    return values[0] if values else None


def _append_valid(values: list[date], year: int, month: int, day: int) -> None:
    try:
        values.append(date(year, month, day))
    except ValueError:
        return


__all__ = [
    "PUBLICATION_DATE_INFERENCE_SEMANTICS_VERSION",
    "infer_publication_date",
    "infer_source_locator_publication_date",
]
