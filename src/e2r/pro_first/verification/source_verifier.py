"""Full-document verification and EvidenceFact compilation for Pro dossiers."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
import hashlib
import os
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import urlparse

from e2r.research.page_fetcher import FetchResult, PageFetcher
from e2r.research_brain.researcher_mode.evidence_fact_compiler import (
    EvidenceFactCompiler,
    FactCompilationResult,
)
from e2r.research_brain.scoring.business_mechanism_scope import (
    MechanismScopeValidator,
    infer_business_mechanism_scope,
    load_mechanism_scope_contracts,
)

from ..ids import stable_id
from ..models import ProResearchJob
from .date_verifier import AsOfDateVerifier
from .lifecycle_bridge import EvidenceLifecycleBridge
from .quote_verifier import ExactQuoteVerifier
from .subject_scope_verifier import SubjectScopeVerifier


TERMINAL_SOURCE_STATUSES = frozenset(
    {
        "ACCEPTED_CURRENT",
        "ACCEPTED_COUNTER",
        "ACCEPTED_RESOLUTION",
        "HISTORICAL_ONLY",
        "SUPERSEDED",
        "UNVERIFIED_PENDING",
        "REJECTED_WRONG_SUBJECT",
        "REJECTED_WRONG_SEGMENT",
        "REJECTED_WRONG_PRODUCT",
        "REJECTED_FUTURE",
        "REJECTED_SNIPPET_ONLY",
        "REJECTED_QUOTE_MISMATCH",
        "REJECTED_SOURCE_UNAVAILABLE",
    }
)
ACCEPTED_SOURCE_STATUSES = frozenset(
    {"ACCEPTED_CURRENT", "ACCEPTED_COUNTER", "ACCEPTED_RESOLUTION"}
)


@dataclass(frozen=True)
class FactSourceVerification:
    dossier_fact_id: str
    status: str
    reason: str
    source_url: str
    source_id: str
    content_hash: str | None
    document_path: str | None
    full_document: bool
    cache_reused: bool
    effective_published_at: str | None
    quote_match_mode: str | None
    target_scope_status: str | None
    proposed_component_ids: tuple[str, ...]
    allowed_component_ids: tuple[str, ...]
    component_rejection_reasons: tuple[str, ...]
    compiled_claim_id: str | None

    def __post_init__(self) -> None:
        if self.status not in TERMINAL_SOURCE_STATUSES:
            raise ValueError(f"unknown source verification status: {self.status}")

    def to_dict(self) -> Mapping[str, Any]:
        payload = asdict(self)
        for key in (
            "proposed_component_ids",
            "allowed_component_ids",
            "component_rejection_reasons",
        ):
            payload[key] = list(payload[key])
        return payload


@dataclass(frozen=True)
class SourceVerificationResult:
    verifications: tuple[FactSourceVerification, ...]
    fact_compilation: FactCompilationResult
    full_document_fetch_count: int
    document_cache_reuse_count: int
    source_document_count: int

    @property
    def receipt_payload(self) -> Mapping[str, Any]:
        counts = {
            status: sum(row.status == status for row in self.verifications)
            for status in sorted(TERMINAL_SOURCE_STATUSES)
        }
        return {
            "schema_version": "e2r_pro_source_verification_receipt_v1",
            "status": "SOURCE_VERIFICATION_COMPLETE",
            "candidate_fact_count": len(self.verifications),
            "terminal_fact_count": sum(
                row.status in TERMINAL_SOURCE_STATUSES for row in self.verifications
            ),
            "accepted_fact_candidate_count": sum(
                row.status in ACCEPTED_SOURCE_STATUSES for row in self.verifications
            ),
            "compiled_evidence_fact_count": len(self.fact_compilation.facts),
            "full_document_fetch_count": self.full_document_fetch_count,
            "document_cache_reuse_count": self.document_cache_reuse_count,
            "source_document_count": self.source_document_count,
            "status_counts": counts,
            "fact_graph_ready": self.fact_compilation.fact_graph_ready,
            "query_count": 0,
            "search_count": 0,
            "pro_score_authority": False,
            "pro_stage_authority": False,
        }


@dataclass(frozen=True)
class _FetchedDocument:
    fetch: FetchResult
    text: str
    content_hash: str
    source_id: str
    relative_path: str
    full_document: bool


class ProSourceVerifier:
    def __init__(
        self,
        *,
        page_fetcher: PageFetcher | None = None,
        min_full_document_chars: int = 120,
    ) -> None:
        if min_full_document_chars < 32:
            raise ValueError("full-document minimum is too small")
        self.page_fetcher = page_fetcher or PageFetcher(
            live_enabled=False, max_text_chars=None
        )
        self.min_full_document_chars = min_full_document_chars
        self.quote_verifier = ExactQuoteVerifier()
        self.date_verifier = AsOfDateVerifier()
        self.scope_verifier = SubjectScopeVerifier()
        self.lifecycle_bridge = EvidenceLifecycleBridge()
        self.fact_compiler = EvidenceFactCompiler()
        self._scope_contracts = load_mechanism_scope_contracts(
            Path(__file__).resolve().parents[4]
            / "configs/e2r_archetype_mechanism_scopes_v1.json"
        )

    def verify(
        self,
        *,
        dossier: Mapping[str, Any],
        job: ProResearchJob,
        job_root: str | Path,
    ) -> SourceVerificationResult:
        root = Path(job_root).resolve()
        source_pages = root / "verification/source_pages"
        source_pages.mkdir(parents=True, exist_ok=True)
        fetch_cache: dict[tuple[str, str], _FetchedDocument | FetchResult] = {}
        fetch_count = 0
        cache_reuse_count = 0
        verifications: list[FactSourceVerification] = []
        accepted_claims: list[Mapping[str, Any]] = []
        target = dossier.get("target") or {}
        target_aliases = tuple(str(value) for value in target.get("aliases") or ())
        facts = tuple(dossier.get("material_facts") or ()) + tuple(
            dossier.get("counterfacts") or ()
        )
        for fact in facts:
            url = str(fact.get("source_url") or "")
            cache_key = (url, job.as_of_date)
            cache_reused = cache_key in fetch_cache
            if cache_reused:
                cache_reuse_count += 1
                fetched = fetch_cache[cache_key]
            else:
                result = self.page_fetcher.fetch(url, as_of_date=date.fromisoformat(job.as_of_date))
                fetch_count += 1
                fetched = self._materialize_document(
                    result,
                    url=url,
                    source_pages=source_pages,
                )
                fetch_cache[cache_key] = fetched
            verification, claim = self._verify_fact(
                fact=fact,
                fetched=fetched,
                job=job,
                target_aliases=target_aliases,
                cache_reused=cache_reused,
            )
            verifications.append(verification)
            if claim is not None:
                accepted_claims.append(claim)
        compilation = self.fact_compiler.compile(
            target_id=job.symbol,
            as_of_date=job.as_of_date,
            accepted_claims=accepted_claims,
        )
        if not compilation.fact_graph_ready:
            raise ValueError("verified Pro claims did not compile into a complete EvidenceFact graph")
        return SourceVerificationResult(
            verifications=tuple(verifications),
            fact_compilation=compilation,
            full_document_fetch_count=fetch_count,
            document_cache_reuse_count=cache_reuse_count,
            source_document_count=sum(isinstance(value, _FetchedDocument) for value in fetch_cache.values()),
        )

    def _materialize_document(
        self,
        result: FetchResult,
        *,
        url: str,
        source_pages: Path,
    ) -> _FetchedDocument | FetchResult:
        text = str(result.text or "")
        if not result.ok or not text.strip():
            return result
        content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        source_id = stable_id("PROSRC", {"url": url, "content_hash": content_hash})
        path = source_pages / f"{source_id}.txt"
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != content_hash:
            self._write_text_atomic(path, text)
        full_document = bool(
            result.text_complete is True
            and len(" ".join(text.split())) >= self.min_full_document_chars
        )
        return _FetchedDocument(
            fetch=result,
            text=text,
            content_hash=content_hash,
            source_id=source_id,
            relative_path=path.relative_to(source_pages.parents[1]).as_posix(),
            full_document=full_document,
        )

    def _verify_fact(
        self,
        *,
        fact: Mapping[str, Any],
        fetched: _FetchedDocument | FetchResult,
        job: ProResearchJob,
        target_aliases: Sequence[str],
        cache_reused: bool,
    ) -> tuple[FactSourceVerification, Mapping[str, Any] | None]:
        dossier_fact_id = str(fact.get("dossier_fact_id") or "")
        url = str(fact.get("source_url") or "")
        fallback_source_id = stable_id("PROSRC", {"url": url, "unavailable": True})

        def terminal(
            status: str,
            reason: str,
            *,
            document: _FetchedDocument | None = None,
            published: str | None = None,
            quote_mode: str | None = None,
            scope_status: str | None = None,
            proposed: tuple[str, ...] = (),
            allowed: tuple[str, ...] = (),
            component_reasons: tuple[str, ...] = (),
            claim_id: str | None = None,
        ) -> FactSourceVerification:
            return FactSourceVerification(
                dossier_fact_id=dossier_fact_id,
                status=status,
                reason=reason,
                source_url=url,
                source_id=document.source_id if document else fallback_source_id,
                content_hash=document.content_hash if document else None,
                document_path=document.relative_path if document else None,
                full_document=bool(document and document.full_document),
                cache_reused=cache_reused,
                effective_published_at=published,
                quote_match_mode=quote_mode,
                target_scope_status=scope_status,
                proposed_component_ids=proposed,
                allowed_component_ids=allowed,
                component_rejection_reasons=component_reasons,
                compiled_claim_id=claim_id,
            )

        if not isinstance(fetched, _FetchedDocument):
            return terminal(
                "REJECTED_SOURCE_UNAVAILABLE",
                fetched.reason or "PageFetcher returned no full document",
            ), None
        if not fetched.full_document:
            return terminal(
                "REJECTED_SNIPPET_ONLY",
                "full document text is required; truncated or short text is not evidence",
                document=fetched,
            ), None
        date_result = self.date_verifier.verify(
            claimed_published_at=fact.get("published_at"),
            event_date=fact.get("event_date"),
            as_of_date=job.as_of_date,
            source_url=url,
            source_title=str(fact.get("source_title") or ""),
            source_publisher=str(fact.get("source_publisher") or ""),
            document_text=fetched.text,
            fetch_result=fetched.fetch,
        )
        if date_result.status == "FUTURE_SOURCE":
            return terminal(
                "REJECTED_FUTURE",
                "source, event, or response metadata exceeds as_of_date",
                document=fetched,
                published=date_result.effective_published_at,
            ), None
        if not date_result.accepted:
            return terminal(
                "UNVERIFIED_PENDING",
                date_result.status,
                document=fetched,
            ), None
        quote = self.quote_verifier.verify(
            str(fact.get("supporting_excerpt") or ""), fetched.text
        )
        if not quote.matched:
            return terminal(
                "REJECTED_QUOTE_MISMATCH",
                "supporting excerpt is not a literal normalized substring of the document",
                document=fetched,
                published=date_result.effective_published_at,
            ), None
        scope = self.scope_verifier.verify(
            fact=fact,
            document_text=fetched.text,
            target_id=job.symbol,
            company_name=job.company_name,
            target_aliases=target_aliases,
        )
        if not scope.accepted:
            status = {
                "WRONG_SUBJECT": "REJECTED_WRONG_SUBJECT",
                "WRONG_SEGMENT": "REJECTED_WRONG_SEGMENT",
                "WRONG_PRODUCT": "REJECTED_WRONG_PRODUCT",
            }[scope.status]
            return terminal(
                status,
                scope.status,
                document=fetched,
                published=date_result.effective_published_at,
                quote_mode=quote.match_mode,
                scope_status=scope.status,
            ), None
        lifecycle = self.lifecycle_bridge.classify(fact)
        proposed = tuple(
            dict.fromkeys(str(value) for value in fact.get("candidate_components") or ())
        )
        allowed, component_reasons = self._eligible_components(
            fact=fact,
            job=job,
            proposed_components=proposed,
        )
        if not lifecycle.compile_as_evidence:
            return terminal(
                lifecycle.status,
                f"lifecycle={fact.get('current_status')}",
                document=fetched,
                published=date_result.effective_published_at,
                quote_mode=quote.match_mode,
                scope_status=scope.status,
                proposed=proposed,
                allowed=allowed,
                component_reasons=component_reasons,
            ), None
        if not str(fact.get("period") or "").strip():
            return terminal(
                "UNVERIFIED_PENDING",
                "period is required before EvidenceFact compilation",
                document=fetched,
                published=date_result.effective_published_at,
                quote_mode=quote.match_mode,
                scope_status=scope.status,
                proposed=proposed,
                allowed=allowed,
                component_reasons=component_reasons,
            ), None
        claim_id = stable_id(
            "PROCLAIM",
            {
                "dossier_fact_id": dossier_fact_id,
                "source_id": fetched.source_id,
                "quote": fact.get("supporting_excerpt"),
            },
        )
        quote_id = stable_id(
            "PROQUOTE",
            {"claim_id": claim_id, "quote": fact.get("supporting_excerpt")},
        )
        source_group = _source_independence_group(
            url, str(fact.get("source_publisher") or "")
        )
        claim = {
            "claim_id": claim_id,
            "accepted_by_evidence_os": True,
            "material": True,
            "target_id": job.symbol,
            "as_of_date": job.as_of_date,
            "published_at": date_result.effective_published_at,
            "subject": str(fact.get("subject") or ""),
            "business_segment": str(fact.get("business_segment") or ""),
            "product_family": str(fact.get("product_family") or ""),
            "economic_mechanism": str(fact.get("economic_mechanism") or ""),
            "predicate": str(fact.get("predicate") or ""),
            "value": fact.get("value"),
            "unit": fact.get("unit"),
            "period": str(fact.get("period") or ""),
            "direction": lifecycle.direction,
            "current_lifecycle": lifecycle.current_lifecycle,
            "source_ids": [fetched.source_id],
            "quote_ids": [quote_id],
            "exact_quote": str(fact.get("supporting_excerpt") or ""),
            "source_independence_group": source_group,
            "confidence": float(fact.get("confidence", 0.0)),
            "allowed_component_ids": list(allowed),
            "supersedes_fact_ids": list(fact.get("supersedes_fact_ids") or ()),
            "resolves_fact_ids": list(fact.get("resolves_fact_ids") or ()),
        }
        return terminal(
            lifecycle.status,
            "full document, date, quote, and scope verified",
            document=fetched,
            published=date_result.effective_published_at,
            quote_mode=quote.match_mode,
            scope_status=scope.status,
            proposed=proposed,
            allowed=allowed,
            component_reasons=component_reasons,
            claim_id=claim_id,
        ), claim

    def _eligible_components(
        self,
        *,
        fact: Mapping[str, Any],
        job: ProResearchJob,
        proposed_components: tuple[str, ...],
    ) -> tuple[tuple[str, ...], tuple[str, ...]]:
        selected_contracts = []
        for job_archetype in job.archetype_ids:
            matches = [
                (archetype_id, contract)
                for archetype_id, contract in self._scope_contracts.items()
                if archetype_id == job_archetype
                or archetype_id.startswith(f"{job_archetype}_")
            ]
            selected_contracts.extend(matches)
        if not selected_contracts:
            return (), ("NO_SELECTED_MECHANISM_SCOPE_CONTRACT",)
        allowed: list[str] = []
        reasons: list[str] = []
        claim = {
            **dict(fact),
            "exact_quote": fact.get("supporting_excerpt"),
            "target_id": job.symbol,
        }
        for component_id in proposed_components:
            component_pass = False
            for archetype_id, contract in selected_contracts:
                scope = infer_business_mechanism_scope(
                    claim,
                    primitive_id=str(fact.get("predicate") or ""),
                    archetype_id=archetype_id,
                )
                result = MechanismScopeValidator().validate(
                    scope=scope,
                    contract=contract,
                    component_id=component_id,
                )
                if result.scope_match:
                    component_pass = True
                    break
                reasons.append(f"{component_id}:{result.reason_code}")
            if component_pass:
                allowed.append(component_id)
        return tuple(dict.fromkeys(allowed)), tuple(dict.fromkeys(reasons))

    @staticmethod
    def _write_text_atomic(path: Path, text: str) -> None:
        part = path.with_suffix(path.suffix + ".part")
        with part.open("w", encoding="utf-8") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(part, path)


def _source_independence_group(url: str, publisher: str) -> str:
    hostname = (urlparse(url).hostname or "").lower()
    identity = publisher.strip().casefold() or hostname
    return stable_id("PROSRCGROUP", {"identity": identity})


__all__ = [
    "ACCEPTED_SOURCE_STATUSES",
    "FactSourceVerification",
    "ProSourceVerifier",
    "SourceVerificationResult",
    "TERMINAL_SOURCE_STATUSES",
]
