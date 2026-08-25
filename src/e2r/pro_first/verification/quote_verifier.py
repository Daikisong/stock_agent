"""Literal quote verification; semantic paraphrases never pass."""

from __future__ import annotations

from dataclasses import dataclass
import re
import unicodedata


@dataclass(frozen=True)
class QuoteVerification:
    matched: bool
    match_mode: str | None
    normalized_quote: str


class ExactQuoteVerifier:
    def verify(self, supporting_excerpt: str, document_text: str) -> QuoteVerification:
        quote = str(supporting_excerpt or "").strip()
        text = str(document_text or "")
        exact_quote = _normalize_whitespace(unicodedata.normalize("NFC", quote))
        exact_text = _normalize_whitespace(unicodedata.normalize("NFC", text))
        if len(exact_quote) >= 8 and exact_quote in exact_text:
            return QuoteVerification(True, "EXACT_NORMALIZED", exact_quote)
        punctuation_quote = _normalize_punctuation(quote)
        punctuation_text = _normalize_punctuation(text)
        if len(punctuation_quote) >= 8 and punctuation_quote in punctuation_text:
            return QuoteVerification(
                True,
                "UNICODE_PUNCTUATION_WHITESPACE_NORMALIZED",
                punctuation_quote,
            )
        ordered_fragments = tuple(
            fragment
            for fragment in (
                _normalize_punctuation(value)
                for value in re.split(r"(?:\.{3,}|…+|\s*;\s*)", quote)
            )
            if len(fragment) >= 4
            or (len(fragment) >= 2 and any(value.isdigit() for value in fragment))
        )
        if (
            len(ordered_fragments) >= 2
            and sum(len(value) for value in ordered_fragments) >= 12
            and _ordered_bounded_fragments(
                ordered_fragments,
                punctuation_text,
                maximum_gap_chars=2_000,
                maximum_span_chars=4_000,
            )
        ):
            return QuoteVerification(
                True,
                "EXACT_ORDERED_FRAGMENT_LIST",
                " … ".join(ordered_fragments),
            )
        return QuoteVerification(False, None, punctuation_quote or exact_quote)


def _normalize_whitespace(value: str) -> str:
    return " ".join(value.split())


def _normalize_punctuation(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    replaced = "".join(
        " "
        if unicodedata.category(character).startswith(("P", "Z"))
        or character in {"|", "│", "┃", "¦"}
        else character
        for character in normalized
    )
    return re.sub(r"\s+", " ", replaced).strip()


def _ordered_bounded_fragments(
    fragments: tuple[str, ...],
    document: str,
    *,
    maximum_gap_chars: int,
    maximum_span_chars: int,
) -> bool:
    if not fragments:
        return False

    def continue_from(
        fragment_index: int,
        *,
        cursor: int,
        first_start: int,
        previous_end: int,
    ) -> bool:
        if fragment_index >= len(fragments):
            return True
        fragment = fragments[fragment_index]
        start = document.find(fragment, cursor)
        while start >= 0:
            if start - previous_end > maximum_gap_chars:
                return False
            end = start + len(fragment)
            if end - first_start > maximum_span_chars:
                return False
            if continue_from(
                fragment_index + 1,
                cursor=end,
                first_start=first_start,
                previous_end=end,
            ):
                return True
            start = document.find(fragment, start + 1)
        return False

    first_fragment = fragments[0]
    first_start = document.find(first_fragment)
    while first_start >= 0:
        first_end = first_start + len(first_fragment)
        if continue_from(
            1,
            cursor=first_end,
            first_start=first_start,
            previous_end=first_end,
        ):
            return True
        first_start = document.find(first_fragment, first_start + 1)
    return False


__all__ = ["ExactQuoteVerifier", "QuoteVerification"]
