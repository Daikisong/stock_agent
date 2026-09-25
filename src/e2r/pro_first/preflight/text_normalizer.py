"""Literal text and quote normalization; semantic similarity is never used."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import html
import re
import unicodedata


@dataclass(frozen=True)
class TextNormalization:
    original_text: str
    normalized_text: str
    normalized_hash: str
    operations: tuple[str, ...]


@dataclass(frozen=True)
class LiteralQuoteMatch:
    matched: bool
    match_mode: str | None
    normalized_quote: str


class TextQuoteNormalizer:
    def normalize_text(self, value: str) -> TextNormalization:
        original = str(value or "")
        operations: list[str] = []
        normalized = original.replace("\r\n", "\n").replace("\r", "\n")
        if normalized != original:
            operations.append("NORMALIZE_LINE_ENDINGS")
        unescaped = html.unescape(normalized)
        if unescaped != normalized:
            operations.append("DECODE_HTML_ENTITIES")
        normalized = unicodedata.normalize("NFC", unescaped)
        if normalized != unescaped:
            operations.append("NORMALIZE_UNICODE_NFC")
        return TextNormalization(
            original_text=original,
            normalized_text=normalized,
            normalized_hash=hashlib.sha256(normalized.encode("utf-8")).hexdigest(),
            operations=tuple(operations),
        )

    def match_quote(
        self,
        supporting_excerpt: str,
        document_text: str,
        *,
        locator_value: str | None = None,
    ) -> LiteralQuoteMatch:
        quote_transport = self.normalize_text(supporting_excerpt).normalized_text.strip()
        document_transport = self.normalize_text(document_text).normalized_text
        if len(quote_transport) >= 8 and quote_transport in document_transport:
            return LiteralQuoteMatch(
                True,
                "EXACT_BYTE_NORMALIZED_EXCERPT",
                quote_transport,
            )
        quote_normalized = _normalize_unicode_whitespace_punctuation(quote_transport)
        document_normalized = _normalize_unicode_whitespace_punctuation(
            document_transport
        )
        if len(quote_normalized) >= 8 and quote_normalized in document_normalized:
            return LiteralQuoteMatch(
                True,
                "UNICODE_WHITESPACE_PUNCTUATION_NORMALIZED_EXACT",
                quote_normalized,
            )
        locator = self.normalize_text(locator_value or "").normalized_text.strip()
        if locator:
            constrained = _locator_window(document_transport, locator)
            if constrained is not None:
                if len(quote_transport) >= 8 and quote_transport in constrained:
                    return LiteralQuoteMatch(
                        True,
                        "LOCATOR_CONSTRAINED_EXACT",
                        quote_transport,
                    )
                constrained_normalized = _normalize_unicode_whitespace_punctuation(
                    constrained
                )
                if (
                    len(quote_normalized) >= 8
                    and quote_normalized in constrained_normalized
                ):
                    return LiteralQuoteMatch(
                        True,
                        "LOCATOR_CONSTRAINED_UNICODE_NORMALIZED_EXACT",
                        quote_normalized,
                    )
        return LiteralQuoteMatch(False, None, quote_normalized or quote_transport)


def _normalize_unicode_whitespace_punctuation(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", str(value or "")).casefold()
    replaced = "".join(
        " " if unicodedata.category(character).startswith(("P", "Z")) else character
        for character in normalized
    )
    return re.sub(r"\s+", " ", replaced).strip()


def _locator_window(document: str, locator: str, *, radius: int = 8_000) -> str | None:
    index = document.find(locator)
    if index < 0:
        normalized_document = _normalize_unicode_whitespace_punctuation(document)
        normalized_locator = _normalize_unicode_whitespace_punctuation(locator)
        index = normalized_document.find(normalized_locator)
        if index < 0:
            return None
        return normalized_document[max(0, index - radius) : index + radius]
    return document[max(0, index - radius) : index + len(locator) + radius]


__all__ = [
    "LiteralQuoteMatch",
    "TextNormalization",
    "TextQuoteNormalizer",
]
