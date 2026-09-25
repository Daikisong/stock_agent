"""Fetch and resolve exact official representations without new search."""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import date
from typing import Mapping, Protocol, Sequence

from e2r.research.page_fetcher import FetchResult

from .canonical_url import CanonicalURLResolver
from .models import ResolvedSourceRepresentation
from .text_normalizer import TextQuoteNormalizer


class SourceDocumentFetcher(Protocol):
    def fetch(self, url: str, *, as_of_date: date) -> FetchResult: ...


@dataclass(frozen=True)
class SourceRepresentationResolution:
    representations_by_document_id: Mapping[str, ResolvedSourceRepresentation]
    representations_by_fact_id: Mapping[str, ResolvedSourceRepresentation]
    attempted_url_count: int
    successful_url_count: int
    redirect_resolution_count: int
    alternate_representation_fact_count: int


class SourceRepresentationResolver:
    def __init__(
        self,
        *,
        fetcher: SourceDocumentFetcher,
        url_resolver: CanonicalURLResolver | None = None,
        text_normalizer: TextQuoteNormalizer | None = None,
    ) -> None:
        self.fetcher = fetcher
        self.url_resolver = url_resolver or CanonicalURLResolver()
        self.text_normalizer = text_normalizer or TextQuoteNormalizer()

    def resolve(
        self,
        *,
        source_documents: Sequence[Mapping[str, object]],
        facts: Sequence[Mapping[str, object]],
        as_of_date: str,
    ) -> SourceRepresentationResolution:
        cutoff = date.fromisoformat(as_of_date)
        document_by_id = {
            str(row.get("source_document_id") or ""): row
            for row in source_documents
        }
        fetch_cache: dict[str, FetchResult] = {}
        attempts = redirects = 0
        by_document: dict[str, ResolvedSourceRepresentation] = {}
        for document_id, document in document_by_id.items():
            candidates = tuple(
                dict.fromkeys(
                    self.url_resolver.resolve(str(document.get(field) or "")).canonical_url
                    for field in ("canonical_url", "opened_url")
                    if str(document.get(field) or "").strip()
                )
            )
            selected: ResolvedSourceRepresentation | None = None
            for url in candidates:
                if url not in fetch_cache:
                    attempts += 1
                    try:
                        fetch_cache[url] = self.fetcher.fetch(
                            url, as_of_date=cutoff
                        )
                    except Exception as exc:  # provider boundary becomes a receipt
                        fetch_cache[url] = FetchResult(
                            url=url,
                            ok=False,
                            reason=f"{type(exc).__name__}: {exc}",
                        )
                result = fetch_cache[url]
                if result.ok and str(result.text or "").strip():
                    final = self.url_resolver.resolve(
                        url,
                        final_redirect_url=(
                            result.url if str(result.url or "").strip() else None
                        ),
                    )
                    redirects += int(final.redirect_applied)
                    text = self.text_normalizer.normalize_text(
                        str(result.text or "")
                    )
                    normalized_fetch = replace(
                        result,
                        url=final.canonical_url,
                        text=text.normalized_text,
                    )
                    selected = ResolvedSourceRepresentation(
                        source_document_id=document_id,
                        lineage_id=str(document.get("lineage_id") or ""),
                        requested_url=url,
                        resolved_url=final.canonical_url,
                        representation_source_document_id=document_id,
                        fetch_result=normalized_fetch,
                        normalized_text=text.normalized_text,
                        text_hash=text.normalized_hash,
                    )
                    break
                if selected is None:
                    selected = ResolvedSourceRepresentation(
                        source_document_id=document_id,
                        lineage_id=str(document.get("lineage_id") or ""),
                        requested_url=url,
                        resolved_url=url,
                        representation_source_document_id=document_id,
                        fetch_result=result,
                        normalized_text="",
                        text_hash=None,
                    )
            if selected is None:
                failed = FetchResult(
                    url="",
                    ok=False,
                    reason="source document has no canonical/opened URL",
                )
                selected = ResolvedSourceRepresentation(
                    source_document_id=document_id,
                    lineage_id=str(document.get("lineage_id") or ""),
                    requested_url="",
                    resolved_url="",
                    representation_source_document_id=document_id,
                    fetch_result=failed,
                    normalized_text="",
                    text_hash=None,
                )
            by_document[document_id] = selected

        by_fact: dict[str, ResolvedSourceRepresentation] = {}
        alternate_count = 0
        for fact in facts:
            fact_id = str(fact.get("dossier_fact_id") or "")
            document_id = str(fact.get("source_document_id") or "")
            source_document = document_by_id.get(document_id) or {}
            primary = by_document.get(document_id)
            if primary is None:
                continue
            candidates = [primary]
            candidates.extend(
                representation
                for alternate_id, representation in by_document.items()
                if alternate_id != document_id
                and _same_official_lineage(
                    source_document,
                    document_by_id.get(alternate_id) or {},
                )
            )
            selected = primary
            for representation in candidates:
                if not representation.available:
                    continue
                locator = str(
                    fact.get("source_locator")
                    or source_document.get("locator_value")
                    or ""
                )
                match = self.text_normalizer.match_quote(
                    str(fact.get("supporting_excerpt") or ""),
                    representation.normalized_text,
                    locator_value=locator,
                )
                if match.matched:
                    is_alternate = (
                        representation.representation_source_document_id
                        != document_id
                    )
                    selected = replace(
                        representation,
                        source_document_id=document_id,
                        lineage_id=str(source_document.get("lineage_id") or ""),
                        quote_match_mode=(
                            f"ALTERNATE_OFFICIAL_REPRESENTATION:{match.match_mode}"
                            if is_alternate
                            else match.match_mode
                        ),
                        alternate_representation_used=is_alternate,
                    )
                    alternate_count += int(is_alternate)
                    break
                if not selected.available:
                    selected = replace(
                        representation,
                        source_document_id=document_id,
                        lineage_id=str(source_document.get("lineage_id") or ""),
                        alternate_representation_used=(
                            representation.representation_source_document_id
                            != document_id
                        ),
                    )
            by_fact[fact_id] = selected
        return SourceRepresentationResolution(
            representations_by_document_id=by_document,
            representations_by_fact_id=by_fact,
            attempted_url_count=attempts,
            successful_url_count=sum(row.available for row in by_document.values()),
            redirect_resolution_count=redirects,
            alternate_representation_fact_count=alternate_count,
        )


def _same_official_lineage(
    left: Mapping[str, object], right: Mapping[str, object]
) -> bool:
    left_scope = left.get("target_scope") or {}
    right_scope = right.get("target_scope") or {}
    if not isinstance(left_scope, Mapping) or not isinstance(right_scope, Mapping):
        return False
    return bool(
        str(left.get("lineage_id") or "")
        and left.get("lineage_id") == right.get("lineage_id")
        and str(left.get("source_publisher") or "").casefold()
        == str(right.get("source_publisher") or "").casefold()
        and left_scope.get("target_id") == right_scope.get("target_id")
        and left_scope.get("issuer_scoped") is right_scope.get("issuer_scoped")
    )


__all__ = [
    "SourceDocumentFetcher",
    "SourceRepresentationResolution",
    "SourceRepresentationResolver",
]
