"""Official-first live source materialization for current Researcher Mode."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl
from e2r.production.source_connectors.source_provider_registry import (
    SourceFetchResult,
    SourceProviderRegistry,
    build_default_source_provider_registry,
)
from e2r.research_brain.intelligence_schema import stable_intelligence_id


OFFICIAL_SOURCE_OUTPUT_FILES: Mapping[str, str] = {
    "documents": "official_evidence_documents.jsonl",
    "attempts": "official_source_attempts.jsonl",
    "structured_payloads": "official_structured_payloads.jsonl",
    "result": "official_source_materialization.json",
    "audit": "official_source_materialization_audit.json",
}


@dataclass(frozen=True)
class OfficialSourceMaterializationResult:
    target_id: str
    as_of_date: str
    status: str
    evidence_documents: tuple[Mapping[str, Any], ...]
    provider_attempts: tuple[Mapping[str, Any], ...]
    structured_payloads: tuple[Mapping[str, Any], ...]
    pending_reasons: tuple[str, ...]
    audit: Mapping[str, Any]
    production_score_authority: bool = False
    schema_version: str = "e2r_v5_official_source_materialization_v1"

    def __post_init__(self) -> None:
        if self.status not in {
            "OFFICIAL_SOURCE_MATERIALIZED",
            "OFFICIAL_SOURCE_PENDING",
        }:
            raise ValueError("unknown official source materialization status")
        if self.status == "OFFICIAL_SOURCE_PENDING" and not self.pending_reasons:
            raise ValueError("pending official source materialization requires reasons")
        if self.production_score_authority:
            raise ValueError("official source materializer cannot assign score")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "status": self.status,
            "evidence_documents": [dict(row) for row in self.evidence_documents],
            "provider_attempts": [dict(row) for row in self.provider_attempts],
            "structured_payloads": [dict(row) for row in self.structured_payloads],
            "pending_reasons": list(self.pending_reasons),
            "audit": dict(self.audit),
            "production_score_authority": False,
        }


class CurrentOfficialSourceMaterializer:
    """Fetch official sources and preserve every normalized text chunk.

    Chunking is a prompt-transport representation of a fully fetched source.
    It does not select a top-N subset: every non-empty chunk is retained and
    must later receive a fact-extraction disposition.
    """

    def __init__(
        self,
        *,
        provider_registry: SourceProviderRegistry | None = None,
        chunk_chars: int = 18_000,
        mandatory_provider_names: Sequence[str] = ("OpenDART",),
    ) -> None:
        if isinstance(chunk_chars, bool) or chunk_chars < 2_000:
            raise ValueError("official source chunk size is too small")
        self.provider_registry = provider_registry
        self.chunk_chars = chunk_chars
        self.mandatory_provider_names = tuple(mandatory_provider_names)

    def materialize(
        self,
        *,
        target_id: str,
        target_name: str,
        as_of_date: str,
        objective_ids: Sequence[str],
        live_materialization_authorized: bool,
        repo_root: str | Path = ".",
    ) -> OfficialSourceMaterializationResult:
        if not live_materialization_authorized:
            raise ValueError("official live materialization requires explicit authorization")
        cutoff = date.fromisoformat(as_of_date)
        registry = self.provider_registry or build_default_source_provider_registry(
            repo_root
        )
        results: list[SourceFetchResult] = []
        for connector in registry.connectors:
            research_fetch = getattr(connector, "fetch_research_document", None)
            if callable(research_fetch):
                result = research_fetch(
                    symbol=target_id,
                    company_name=target_name,
                    as_of_date=cutoff,
                    mode="live",
                )
            else:
                result = connector.fetch(
                    symbol=target_id,
                    company_name=target_name,
                    as_of_date=cutoff,
                    mode="live",
                )
            results.append(result)
        attempts = tuple(_attempt_row(row, target_id=target_id) for row in results)
        structured_payloads = tuple(
            {
                "schema_version": "e2r_v5_official_structured_payload_v1",
                "target_id": target_id,
                "as_of_date": as_of_date,
                "provider_name": row.provider_name,
                "source_class": row.source_class,
                "canonical_url": row.canonical_url,
                "published_at": row.published_at,
                "available_at": row.available_at,
                "provider_content_hash": row.content_hash,
                "payload": dict(row.structured_payload),
                "production_score_authority": False,
            }
            for row in results
            if row.status == "FETCHED" and row.structured_payload
        )
        documents: list[Mapping[str, Any]] = []
        for result in results:
            if not result.counts_as_symbol_evidence or not result.raw_text.strip():
                continue
            published = _date_or_none(result.published_at)
            available = _date_or_none(result.available_at)
            if published is None or available is None:
                continue
            if published > cutoff or available > cutoff:
                continue
            full_text = _plain_text(result.raw_text)
            if not full_text.strip():
                continue
            chunks = _all_chunks(full_text, max_chars=self.chunk_chars)
            full_source_id = stable_intelligence_id(
                "OFFICIALSOURCE",
                {
                    "target_id": target_id,
                    "provider_name": result.provider_name,
                    "canonical_url": result.canonical_url,
                    "provider_content_hash": result.content_hash,
                },
            )
            for index, content in enumerate(chunks):
                content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
                document_id = stable_intelligence_id(
                    "OFFICIALDOC",
                    {
                        "full_source_id": full_source_id,
                        "chunk_index": index,
                        "content_hash": content_hash,
                    },
                )
                source_family = _source_family(result)
                documents.append(
                    {
                        "schema_version": "e2r_v5_official_source_graph_document_v1",
                        "document_id": document_id,
                        "full_source_document_id": full_source_id,
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "canonical_url": str(result.canonical_url or ""),
                        "discovery_urls": [str(result.canonical_url or "")],
                        "title": (
                            str(result.structured_payload.get("title") or "").strip()
                            or f"{result.provider_name} official source"
                        ),
                        "source_family": source_family,
                        "source_provider": result.provider_name,
                        "published_at": published.isoformat(),
                        "available_at": available.isoformat(),
                        "fetched_at": str(result.fetched_at or as_of_date),
                        "content_type": "text/plain",
                        "content_hash": content_hash,
                        "content_text": content,
                        "full_source_content_hash": str(result.content_hash or ""),
                        "full_source_text_chars": len(full_text),
                        "chunk_index": index,
                        "chunk_count": len(chunks),
                        "all_chunks_preserved": True,
                        "query_ids": [],
                        "objective_ids": list(dict.fromkeys(objective_ids)),
                        "source_independence_group": (
                            f"{source_family}:{result.provider_name.casefold()}"
                        ),
                        "referenced_urls": [],
                        "referenced_document_ids": [],
                        "full_fetch_performed": True,
                        "full_source_fetch_performed": True,
                        "snippet_only": False,
                        "snippet_used_as_document": False,
                        "snippet_evidence_eligible": False,
                        "evidence_eligible": True,
                        "evidence_os_ingest_eligible": True,
                        "parser_field_direct_score_authority": False,
                        "production_score_authority": False,
                    }
                )
        pending: list[str] = []
        result_by_name = {row.provider_name: row for row in results}
        for provider_name in self.mandatory_provider_names:
            result = result_by_name.get(provider_name)
            if result is None:
                pending.append(f"MANDATORY_OFFICIAL_PROVIDER_NOT_CONFIGURED:{provider_name}")
            elif result.status != "FETCHED" or not result.counts_as_symbol_evidence:
                pending.append(
                    f"MANDATORY_OFFICIAL_PROVIDER_PENDING:{provider_name}:"
                    f"{result.status}:{result.provider_error or 'no symbol evidence'}"
                )
        if not documents:
            pending.append("NO_FULL_OFFICIAL_EVIDENCE_DOCUMENT")
        critical_counts = {
            "live_materialization_unauthorized_count": int(
                not live_materialization_authorized
            ),
            "mandatory_official_provider_pending_count": sum(
                reason.startswith("MANDATORY_OFFICIAL_PROVIDER") for reason in pending
            ),
            "full_official_document_missing_count": int(not documents),
            "future_official_document_count": sum(
                bool(_date_or_none(row.get("published_at")) and _date_or_none(row.get("published_at")) > cutoff)
                for row in documents
            ),
            "official_chunk_drop_count": sum(
                not bool(row.get("all_chunks_preserved")) for row in documents
            ),
            "snippet_evidence_count": sum(
                bool(row.get("snippet_only")) for row in documents
            ),
        }
        critical_sum = sum(critical_counts.values())
        complete = critical_sum == 0
        audit = {
            "schema_version": "e2r_v5_official_source_materialization_audit_v1",
            "status": (
                "OFFICIAL_SOURCE_MATERIALIZATION_PASS"
                if complete
                else "OFFICIAL_SOURCE_MATERIALIZATION_PENDING"
            ),
            "target_id": target_id,
            "as_of_date": as_of_date,
            "provider_attempt_count": len(results),
            "provider_statuses": {
                row.provider_name: row.status for row in results
            },
            "structured_payload_count": len(structured_payloads),
            "full_source_count": len(
                {str(row["full_source_document_id"]) for row in documents}
            ),
            "evidence_document_chunk_count": len(documents),
            "chunk_transport_chars": self.chunk_chars,
            "chunking_is_top_n_selection": False,
            "all_normalized_chunks_preserved": True,
            "snippet_is_evidence": False,
            "provider_failure_is_zero_score": False,
            "critical_counts": critical_counts,
            "critical_count_sum": critical_sum,
        }
        return OfficialSourceMaterializationResult(
            target_id=target_id,
            as_of_date=as_of_date,
            status=(
                "OFFICIAL_SOURCE_MATERIALIZED"
                if complete
                else "OFFICIAL_SOURCE_PENDING"
            ),
            evidence_documents=tuple(documents),
            provider_attempts=attempts,
            structured_payloads=structured_payloads,
            pending_reasons=tuple(dict.fromkeys(pending)),
            audit=audit,
        )


def write_official_source_materialization(
    result: OfficialSourceMaterializationResult,
    output_directory: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_directory)
    paths = {
        key: root / filename for key, filename in OFFICIAL_SOURCE_OUTPUT_FILES.items()
    }
    write_jsonl(paths["documents"], result.evidence_documents)
    write_jsonl(paths["attempts"], result.provider_attempts)
    write_jsonl(paths["structured_payloads"], result.structured_payloads)
    write_json(paths["result"], result.to_dict())
    write_json(paths["audit"], result.audit)
    return paths


def _attempt_row(result: SourceFetchResult, *, target_id: str) -> Mapping[str, Any]:
    return {
        "schema_version": "e2r_v5_official_source_attempt_v1",
        "target_id": target_id,
        "provider_name": result.provider_name,
        "source_class": result.source_class,
        "mode": result.mode,
        "request_id": result.request_id,
        "provider_request_id": result.provider_request_id,
        "status": result.status,
        "counts_as_live": result.counts_as_live,
        "counts_as_symbol_evidence": result.counts_as_symbol_evidence,
        "canonical_url": result.canonical_url,
        "official_document_id": result.official_document_id,
        "published_at": result.published_at,
        "available_at": result.available_at,
        "fetched_at": result.fetched_at,
        "provider_content_hash": result.content_hash,
        "raw_text_chars": len(result.raw_text),
        "structured_payload_keys": sorted(result.structured_payload),
        "provider_error": result.provider_error,
        "production_score_authority": False,
    }


def _source_family(result: SourceFetchResult) -> str:
    if result.provider_name == "OpenDART" or result.source_class == "DART":
        return "OPENDART"
    if result.provider_name == "KIND" or result.source_class == "KIND":
        return "KIND_KRX"
    if result.provider_name == "CompanyGuide":
        return "CONSENSUS_REVISION"
    if result.provider_name == "TrustedNews":
        return "TRUSTED_BUSINESS_MEDIA"
    if result.source_class == "IR":
        return "ISSUER_PRESENTATION"
    return "ISSUER_NEWSROOM"


def _plain_text(raw: str) -> str:
    parser = _TextExtractor()
    try:
        parser.feed(raw)
        parser.close()
        text = parser.text()
    except Exception:
        text = raw
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _all_chunks(text: str, *, max_chars: int) -> tuple[str, ...]:
    paragraphs = [value.strip() for value in re.split(r"\n+", text) if value.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_chars = 0
    for paragraph in paragraphs:
        pieces = (
            tuple(
                paragraph[index : index + max_chars]
                for index in range(0, len(paragraph), max_chars)
            )
            if len(paragraph) > max_chars
            else (paragraph,)
        )
        for piece in pieces:
            needed = len(piece) + (1 if current else 0)
            if current and current_chars + needed > max_chars:
                chunks.append("\n".join(current))
                current = []
                current_chars = 0
            current.append(piece)
            current_chars += len(piece) + (1 if len(current) > 1 else 0)
    if current:
        chunks.append("\n".join(current))
    return tuple(value for value in chunks if value.strip())


def _date_or_none(value: Any) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        value = " ".join(data.split())
        if value:
            self.parts.append(value)

    def text(self) -> str:
        return "\n".join(self.parts)


__all__ = [
    "CurrentOfficialSourceMaterializer",
    "OFFICIAL_SOURCE_OUTPUT_FILES",
    "OfficialSourceMaterializationResult",
    "write_official_source_materialization",
]
