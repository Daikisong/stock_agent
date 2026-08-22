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
        matched = next((alias for alias in aliases if _contains(document, alias)), None)
        if matched is None:
            return SubjectScopeVerification(False, "WRONG_SUBJECT")
        subject = str(fact.get("subject") or "").strip()
        if not subject or not _contains(document, subject):
            return SubjectScopeVerification(False, "WRONG_SUBJECT", matched)
        if fact.get("issuer_scoped") is True and not any(
            _scope_text(subject) == _scope_text(alias) for alias in aliases
        ):
            return SubjectScopeVerification(False, "WRONG_SUBJECT", matched)
        segment = str(fact.get("business_segment") or "").strip()
        if not segment:
            return SubjectScopeVerification(False, "WRONG_SEGMENT", matched)
        if segment != "CORPORATE_GENERIC" and not _contains(document, segment):
            return SubjectScopeVerification(False, "WRONG_SEGMENT", matched)
        product = str(fact.get("product_family") or "").strip()
        if not product:
            return SubjectScopeVerification(False, "WRONG_PRODUCT", matched)
        if product != "CORPORATE_GENERIC" and not _contains(document, product):
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


__all__ = ["SubjectScopeVerification", "SubjectScopeVerifier"]
