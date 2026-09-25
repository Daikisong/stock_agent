"""Generic issuer, subject, and known-publisher alias resolution."""

from __future__ import annotations

from dataclasses import dataclass
import re
import unicodedata
from typing import Mapping, Sequence
from urllib.parse import urlsplit


_GENERIC_ORGANIZATION_WORDS = frozenset(
    {
        "company",
        "corporation",
        "corp",
        "inc",
        "incorporated",
        "limited",
        "ltd",
        "plc",
        "group",
        "holdings",
    }
)


@dataclass(frozen=True)
class IssuerAliasResolution:
    target_aliases: tuple[str, ...]
    subject_aliases: tuple[str, ...]
    canonical_publisher: str
    publisher_alias_applied: bool


class IssuerAliasResolver:
    def __init__(
        self,
        *,
        known_publisher_aliases: Mapping[str, str] | None = None,
    ) -> None:
        self.known_publisher_aliases = {
            _identity(key): str(value).strip()
            for key, value in (known_publisher_aliases or {}).items()
            if str(key).strip() and str(value).strip()
        }

    def normalize_publisher(self, value: str) -> tuple[str, bool]:
        normalized = " ".join(
            unicodedata.normalize("NFKC", str(value or "")).split()
        ).strip()
        canonical = self.known_publisher_aliases.get(
            _identity(normalized), normalized
        )
        return canonical, canonical != str(value or "")

    def resolve(
        self,
        *,
        target_id: str,
        company_name: str,
        target_aliases: Sequence[str],
        fact: Mapping[str, object],
        source_document: Mapping[str, object],
        document_text: str,
    ) -> IssuerAliasResolution:
        publisher, publisher_changed = self.normalize_publisher(
            str(source_document.get("source_publisher") or "")
        )
        canonical_url = str(source_document.get("canonical_url") or "")
        scope = source_document.get("target_scope") or {}
        if not isinstance(scope, Mapping):
            scope = {}
        issuer_candidates = [
            company_name,
            target_id,
            *target_aliases,
        ]
        if fact.get("issuer_scoped") is True and _publisher_matches_hostname(
            publisher, canonical_url
        ):
            issuer_candidates.append(publisher)
        issuer_aliases = tuple(
            dict.fromkeys(
                str(value).strip()
                for value in issuer_candidates
                if str(value or "").strip()
            )
        )
        subject_candidates = (
            str(fact.get("subject") or ""),
            str(scope.get("subject") or ""),
            publisher,
        )
        subject_aliases = tuple(
            dict.fromkeys(
                candidate.strip()
                for candidate in subject_candidates
                if candidate.strip() and _contains(document_text, candidate)
            )
        )
        return IssuerAliasResolution(
            target_aliases=issuer_aliases,
            subject_aliases=subject_aliases,
            canonical_publisher=publisher,
            publisher_alias_applied=publisher_changed,
        )


def _publisher_matches_hostname(publisher: str, url: str) -> bool:
    hostname = (urlsplit(url).hostname or "").casefold()
    compact_host = re.sub(r"[^a-z0-9]+", "", hostname)
    tokens = tuple(
        token
        for token in re.findall(r"[a-z0-9]+", publisher.casefold())
        if len(token) >= 4 and token not in _GENERIC_ORGANIZATION_WORDS
    )
    return bool(tokens and any(token in compact_host for token in tokens))


def _contains(document: str, candidate: str) -> bool:
    return _identity(candidate) in _identity(document)


def _identity(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return re.sub(r"[^\w]+", "", normalized, flags=re.UNICODE)


__all__ = ["IssuerAliasResolution", "IssuerAliasResolver"]
