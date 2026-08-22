"""Literal target, subject, segment, and product scope verification."""

from __future__ import annotations

from dataclasses import dataclass
import re
import unicodedata
from typing import Mapping, Sequence


@dataclass(frozen=True)
class SubjectScopeVerification:
    accepted: bool
    status: str
    matched_target_alias: str | None = None


class SubjectScopeVerifier:
    def verify(
        self,
        *,
        fact: Mapping[str, object],
        document_text: str,
        target_id: str,
        company_name: str,
        target_aliases: Sequence[str] = (),
    ) -> SubjectScopeVerification:
        document = _scope_text(document_text)
        aliases = tuple(
            dict.fromkeys(
                value.strip()
                for value in (company_name, target_id, *target_aliases)
                if str(value).strip()
            )
        )
        subject = str(fact.get("subject") or "").strip()
        issuer_scoped = fact.get("issuer_scoped") is True
        matched = next((alias for alias in aliases if _contains(document, alias)), None)
        if issuer_scoped:
            if matched is None or not any(
                _contains(_scope_text(subject), alias) for alias in aliases
            ):
                return SubjectScopeVerification(False, "WRONG_SUBJECT", matched)
            if not _issuer_subject_supported(
                subject=subject,
                document=document,
                aliases=aliases,
            ):
                return SubjectScopeVerification(False, "WRONG_SUBJECT", matched)
        elif not subject or not _contains(document, subject):
            # A peer/customer/partner counterfact need not name the target in
            # the peer document, but its stated subject must be literal.
            return SubjectScopeVerification(False, "WRONG_SUBJECT", matched)
        segment = str(fact.get("business_segment") or "").strip()
        if not segment:
            return SubjectScopeVerification(False, "WRONG_SEGMENT", matched)
        if segment != "CORPORATE_GENERIC" and not _descriptor_supported(
            document, segment
        ):
            return SubjectScopeVerification(False, "WRONG_SEGMENT", matched)
        product = str(fact.get("product_family") or "").strip()
        if not product:
            return SubjectScopeVerification(False, "WRONG_PRODUCT", matched)
        if product != "CORPORATE_GENERIC" and not _descriptor_supported(
            document, product
        ):
            return SubjectScopeVerification(False, "WRONG_PRODUCT", matched)
        return SubjectScopeVerification(True, "SUBJECT_SCOPE_ACCEPTED", matched)


def _scope_text(value: object) -> str:
    normalized = unicodedata.normalize("NFKC", str(value or "")).casefold()
    normalized = "".join(
        " " if unicodedata.category(character).startswith(("P", "Z")) else character
        for character in normalized
    )
    return re.sub(r"\s+", " ", normalized).strip()


def _contains(normalized_document: str, value: str) -> bool:
    needle = _scope_text(value)
    return bool(needle and needle in normalized_document)


def _issuer_subject_supported(
    *,
    subject: str,
    document: str,
    aliases: Sequence[str],
) -> bool:
    """Accept issuer or joint-subject labels only when every party is literal."""

    normalized_subject = _scope_text(subject)
    if not normalized_subject:
        return False
    if normalized_subject in document:
        return True
    alias_needles = tuple(
        sorted(
            (_scope_text(value) for value in aliases if _scope_text(value)),
            key=len,
            reverse=True,
        )
    )
    remainder = normalized_subject
    for alias in alias_needles:
        remainder = remainder.replace(alias, " ")
    remainder = re.sub(r"\b(?:and|with|및|와|과|주식회사|inc|incorporated|co|ltd)\b", " ", remainder)
    parties = tuple(value for value in re.split(r"\s+", remainder) if len(value) >= 2)
    return all(value in document for value in parties)


_DESCRIPTOR_GRAMMAR_WORDS = frozenset(
    {
        "and",
        "or",
        "the",
        "of",
        "for",
        "including",
        "business",
        "segment",
        "product",
        "products",
        "portfolio",
        "corporate",
        "generic",
        "consolidated",
        "strategic",
        "potential",
        "possible",
        "next",
        "generation",
    }
)


def _descriptor_supported(normalized_document: str, descriptor: str) -> bool:
    """Match semantic scope labels by general literal anchors, not full labels.

    A Pro label such as ``Consolidated semiconductor`` is a structured scope
    description, not necessarily a verbatim source phrase.  At least half of
    its non-grammatical literal anchors must occur in the full document.  This
    remains lexical and fail-closed: no sector, symbol, archetype, or expected
    answer is encoded here.
    """

    needle = _scope_text(descriptor)
    if needle and needle in normalized_document:
        return True
    anchors = tuple(
        dict.fromkeys(
            value
            for value in re.findall(r"[^\W_]+", needle, flags=re.UNICODE)
            if len(value) >= 2 and value not in _DESCRIPTOR_GRAMMAR_WORDS
        )
    )
    if not anchors:
        return False
    matches = sum(value in normalized_document for value in anchors)
    required = max(1, (len(anchors) + 1) // 2)
    return matches >= required


__all__ = ["SubjectScopeVerification", "SubjectScopeVerifier"]
