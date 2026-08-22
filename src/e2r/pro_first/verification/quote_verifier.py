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
        return QuoteVerification(False, None, punctuation_quote or exact_quote)


def _normalize_whitespace(value: str) -> str:
    return " ".join(value.split())


def _normalize_punctuation(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    replaced = "".join(
        " " if unicodedata.category(character).startswith(("P", "Z")) else character
        for character in normalized
    )
    return re.sub(r"\s+", " ", replaced).strip()


__all__ = ["ExactQuoteVerifier", "QuoteVerification"]
