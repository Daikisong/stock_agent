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
        semantic_scope: Mapping[str, object] | None = None,
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
        excerpt = _scope_text(fact.get("supporting_excerpt"))
        excerpt_target_match = next(
            (alias for alias in aliases if _contains(excerpt, alias)),
            None,
        )
        if issuer_scoped:
            # ``subject`` is a structured economic label (for example,
            # ``operating cash flow``), not a second company-name field.  The
            # target is already bound by target_id and must occur literally in
            # the document; requiring the label itself to repeat an issuer
            # alias rejects legitimate bilingual filings wholesale.
            if matched is None or not subject:
                return SubjectScopeVerification(False, "WRONG_SUBJECT", matched)
        elif not subject or (
            excerpt_target_match is None
            and not any(
                _contains(document, candidate)
                for candidate in (
                    subject,
                    *(
                        str(value)
                        for value in fact.get("preflight_subject_aliases") or ()
                    ),
                )
            )
        ):
            # A peer/customer/partner counterfact need not name the target in
            # the peer document, but its stated subject must be literal. When
            # the already quote-verified excerpt itself names the target, a
            # spacing or facility-label variation in the structured subject
            # must not turn target-specific regulator evidence into WRONG_SUBJECT.
            return SubjectScopeVerification(False, "WRONG_SUBJECT", matched)
        segment = str(fact.get("business_segment") or "").strip()
        if not segment:
            return SubjectScopeVerification(False, "WRONG_SEGMENT", matched)
        product = str(fact.get("product_family") or "").strip()
        if not product:
            return SubjectScopeVerification(False, "WRONG_PRODUCT", matched)
        if not _has_complete_semantic_scope(semantic_scope):
            if segment != "CORPORATE_GENERIC" and not _descriptor_supported(
                document, segment
            ):
                return SubjectScopeVerification(False, "WRONG_SEGMENT", matched)
            if product != "CORPORATE_GENERIC" and not _descriptor_supported(
                document, product
            ):
                return SubjectScopeVerification(False, "WRONG_PRODUCT", matched)
        return SubjectScopeVerification(True, "SUBJECT_SCOPE_ACCEPTED", matched)


_SEMANTIC_SCOPE_FIELDS = frozenset(
    {
        "scope_business_segment",
        "scope_product_family",
        "scope_technology_family",
        "scope_transaction_type",
        "scope_economic_mechanism",
        "scope_confidence",
    }
)


def _has_complete_semantic_scope(value: Mapping[str, object] | None) -> bool:
    if not isinstance(value, Mapping) or not _SEMANTIC_SCOPE_FIELDS.issubset(value):
        return False
    confidence = value.get("scope_confidence")
    if isinstance(confidence, bool) or not isinstance(confidence, (int, float)):
        return False
    return 0 <= float(confidence) <= 1 and all(
        str(value.get(key) or "").strip()
        for key in _SEMANTIC_SCOPE_FIELDS - {"scope_confidence"}
    )


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
