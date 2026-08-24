"""Full-document verification and EvidenceFact compilation for Pro dossiers."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date, datetime
import hashlib
import json
import os
from pathlib import Path
import re
from typing import Any, Mapping, Sequence
from urllib.parse import urlparse

from e2r.research.page_fetcher import FetchResult, PageFetcher
from e2r.research_brain.researcher_mode.evidence_fact_compiler import (
    EvidenceFactCompiler,
    FactCompilationResult,
)
from e2r.research_brain.scoring.business_mechanism_scope import (
    ISSUER_CONSOLIDATED_ACTUAL_SCOPE_CONTRACT,
    MechanismScopeValidator,
    infer_business_mechanism_scope,
    load_mechanism_scope_contracts,
)

from ..ids import canonical_hash, stable_id
from ..models import ProResearchJob
from .date_verifier import AsOfDateVerifier
from .lifecycle_bridge import EvidenceLifecycleBridge
from .mechanism_scope_mapper import MechanismScopeMapper, MechanismScopeMappingRun
from .quote_verifier import ExactQuoteVerifier
from .subject_scope_verifier import SubjectScopeVerifier


SOURCE_VERIFICATION_SEMANTICS_VERSION = "e2r_pro_source_verification_v8"


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
    mechanism_scope_mapping: MechanismScopeMappingRun | None = None

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
            "mechanism_scope_mapping_count": (
                len(self.mechanism_scope_mapping.mappings_by_fact_id)
                if self.mechanism_scope_mapping is not None
                else 0
            ),
            "mechanism_scope_provider_name": (
                self.mechanism_scope_mapping.provider_name
                if self.mechanism_scope_mapping is not None
                else "DETERMINISTIC_LEGACY_INFERENCE"
            ),
            "mechanism_scope_prompt_hash": (
                self.mechanism_scope_mapping.prompt_hash
                if self.mechanism_scope_mapping is not None
                else None
            ),
            "mechanism_scope_response_hash": (
                self.mechanism_scope_mapping.response_hash
                if self.mechanism_scope_mapping is not None
                else None
            ),
            "mechanism_scope_mapping_hash": (
                canonical_hash(self.mechanism_scope_mapping.mappings_by_fact_id)
                if self.mechanism_scope_mapping is not None
                else None
            ),
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
        mechanism_scope_mapper: MechanismScopeMapper | None = None,
    ) -> None:
        if min_full_document_chars < 32:
            raise ValueError("full-document minimum is too small")
        self.page_fetcher = page_fetcher or PageFetcher(
            live_enabled=False, max_text_chars=None
        )
        self.min_full_document_chars = min_full_document_chars
        self.mechanism_scope_mapper = mechanism_scope_mapper
        self.quote_verifier = ExactQuoteVerifier()
        self.date_verifier = AsOfDateVerifier()
        self.scope_verifier = SubjectScopeVerifier()
        self.lifecycle_bridge = EvidenceLifecycleBridge()
        self.fact_compiler = EvidenceFactCompiler()
        self._scope_contracts = load_mechanism_scope_contracts(
            Path(__file__).resolve().parents[4]
            / "configs/e2r_archetype_mechanism_scopes_v1.json"
        )

    @property
    def semantics_version(self) -> str:
        return SOURCE_VERIFICATION_SEMANTICS_VERSION

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
        facts = tuple(
            row
            for collection in ("material_facts", "counterfacts", "resolution_facts")
            for row in dossier.get(collection) or ()
        )
        selected_scope_contracts = self._selected_scope_contracts(job)
        scope_mapping = None
        if self.mechanism_scope_mapper is not None:
            scope_mapping = self._load_durable_mechanism_scope_mapping(
                root=root,
                facts=facts,
            ) or self.mechanism_scope_mapper.map_facts(
                facts=facts,
                contracts=tuple(contract for _, contract in selected_scope_contracts),
            )
        fetch_cache = self._load_durable_document_cache(
            root=root,
            as_of_date=job.as_of_date,
            allowed_urls={str(fact.get("source_url") or "") for fact in facts},
        )
        fetch_count = 0
        cache_reuse_count = 0
        verifications: list[FactSourceVerification] = []
        accepted_claims: list[Mapping[str, Any]] = []
        target = dossier.get("target") or {}
        target_aliases = tuple(
            dict.fromkeys(
                str(value)
                for value in (
                    *(target.get("aliases") or ()),
                    target.get("english_name"),
                    target.get("symbol"),
                    target.get("target_id"),
                    *_issuer_publisher_aliases(facts),
                )
                if str(value or "").strip()
            )
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
                explicit_scope=(
                    scope_mapping.mappings_by_fact_id.get(
                        str(fact.get("dossier_fact_id") or "")
                    )
                    if scope_mapping is not None
                    else None
                ),
            )
            verifications.append(verification)
            if claim is not None:
                accepted_claims.append(claim)
        compilation = self.fact_compiler.compile(
            target_id=job.symbol,
            as_of_date=job.as_of_date,
            accepted_claims=accepted_claims,
        )
        return SourceVerificationResult(
            verifications=tuple(verifications),
            fact_compilation=compilation,
            full_document_fetch_count=fetch_count,
            document_cache_reuse_count=cache_reuse_count,
            source_document_count=sum(isinstance(value, _FetchedDocument) for value in fetch_cache.values()),
            mechanism_scope_mapping=scope_mapping,
        )

    def _load_durable_document_cache(
        self,
        *,
        root: Path,
        as_of_date: str,
        allowed_urls: set[str],
    ) -> dict[tuple[str, str], _FetchedDocument | FetchResult]:
        """Reuse only hash-verified full documents from the same job snapshot."""

        roster_path = root / "verification/source_verifications.jsonl"
        if not roster_path.is_file():
            return {}
        cache: dict[tuple[str, str], _FetchedDocument | FetchResult] = {}
        for line in roster_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            url = str(row.get("source_url") or "")
            relative_path = str(row.get("document_path") or "")
            expected_hash = str(row.get("content_hash") or "")
            if (
                not url
                or url not in allowed_urls
                or not relative_path
                or not expected_hash
                or row.get("full_document") is not True
            ):
                continue
            path = (root / relative_path).resolve()
            try:
                path.relative_to(root)
            except ValueError:
                continue
            if not path.is_file():
                continue
            payload = path.read_bytes()
            if hashlib.sha256(payload).hexdigest() != expected_hash:
                continue
            try:
                text = payload.decode("utf-8")
            except UnicodeDecodeError:
                continue
            source_id = str(row.get("source_id") or "") or stable_id(
                "PROSRC", {"url": url, "content_hash": expected_hash}
            )
            snapshot_date = date.fromisoformat(as_of_date)
            fetch = FetchResult(
                url=url,
                ok=True,
                text=text,
                content_type="text/plain",
                fetched_at=datetime(
                    snapshot_date.year,
                    snapshot_date.month,
                    snapshot_date.day,
                    8,
                    0,
                ),
                source_path=str(path),
                text_complete=True,
                original_text_chars=len(text),
                returned_text_chars=len(text),
            )
            cache[(url, as_of_date)] = _FetchedDocument(
                fetch=fetch,
                text=text,
                content_hash=expected_hash,
                source_id=source_id,
                relative_path=relative_path,
                full_document=True,
            )
        return cache

    def _load_durable_mechanism_scope_mapping(
        self,
        *,
        root: Path,
        facts: Sequence[Mapping[str, Any]],
    ) -> MechanismScopeMappingRun | None:
        mapping_path = root / "verification/mechanism_scope_mappings.jsonl"
        receipt_path = root / "verification/source_verification_receipt.json"
        if not mapping_path.is_file() or not receipt_path.is_file():
            return None
        try:
            rows = tuple(
                json.loads(line)
                for line in mapping_path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            )
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return None
        expected_ids = tuple(
            str(row.get("dossier_fact_id") or "") for row in facts
        )
        actual_ids = tuple(str(row.get("dossier_fact_id") or "") for row in rows)
        if actual_ids != expected_ids:
            return None
        mappings = {
            fact_id: {
                key: value
                for key, value in row.items()
                if key != "dossier_fact_id"
            }
            for fact_id, row in zip(actual_ids, rows)
        }
        expected_hash = str(receipt.get("mechanism_scope_mapping_hash") or "")
        if not expected_hash or canonical_hash(mappings) != expected_hash:
            return None
        return MechanismScopeMappingRun(
            mappings_by_fact_id=mappings,
            provider_name=(
                str(receipt.get("mechanism_scope_provider_name") or "UNKNOWN")
                + ":DURABLE_CACHE"
            ),
            prompt_hash=str(receipt.get("mechanism_scope_prompt_hash") or ""),
            response_hash=str(receipt.get("mechanism_scope_response_hash") or ""),
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
        explicit_scope: Mapping[str, Any] | None = None,
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
            semantic_scope=explicit_scope,
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
            explicit_scope=explicit_scope,
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
            # Confidence becomes deterministic only after the source document,
            # as-of date, literal quote, issuer scope, and mechanism scope have
            # all passed.  A structural placeholder (for example 0.0 in a
            # compact Pro dossier) must not erase an otherwise verified fact,
            # and the model's self-reported confidence must not own scoring.
            "confidence": 1.0,
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
        explicit_scope: Mapping[str, Any] | None = None,
    ) -> tuple[tuple[str, ...], tuple[str, ...]]:
        selected_contracts = self._selected_scope_contracts(job)
        if not selected_contracts:
            return (), ("NO_SELECTED_MECHANISM_SCOPE_CONTRACT",)
        allowed: list[str] = []
        reasons: list[str] = []
        claim = {
            **dict(fact),
            "exact_quote": fact.get("supporting_excerpt"),
            "target_id": job.symbol,
            "raw_assertion": {
                "predicate": fact.get("predicate"),
                "object_text": " ".join(
                    str(fact.get(key) or "")
                    for key in (
                        "statement",
                        "business_segment",
                        "product_family",
                        "economic_mechanism",
                    )
                ),
            },
            "document_context_excerpt": " ".join(
                str(fact.get(key) or "")
                for key in (
                    "supporting_excerpt",
                    "business_segment",
                    "product_family",
                    "economic_mechanism",
                )
            ),
        }
        claim.update(_issuer_consolidated_scope_projection(fact))
        if explicit_scope is not None:
            claim.update(dict(explicit_scope))
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

    def _selected_scope_contracts(self, job: ProResearchJob) -> list[tuple[str, Any]]:
        selected_contracts: list[tuple[str, Any]] = []
        for job_archetype in job.archetype_ids:
            selected_contracts.extend(
                (archetype_id, contract)
                for archetype_id, contract in self._scope_contracts.items()
                if archetype_id == job_archetype
                or archetype_id.startswith(f"{job_archetype}_")
            )
        if not selected_contracts:
            raise ValueError("selected archetype has no mechanism scope contract")
        return selected_contracts

    @staticmethod
    def _write_text_atomic(path: Path, text: str) -> None:
        part = path.with_suffix(path.suffix + ".part")
        # Keep the exact UTF-8 bytes that were hashed above on Windows too;
        # default text mode would translate LF to CRLF after hashing.
        with part.open("w", encoding="utf-8", newline="") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(part, path)


_ISSUER_ALIAS_SOURCE_ROLES = frozenset(
    {"ISSUER_OFFICIAL", "ISSUER_EARNINGS"}
)
_PUBLISHER_ORGANIZATION_WORDS = frozenset(
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


def _issuer_publisher_aliases(
    facts: Sequence[Mapping[str, Any]],
) -> tuple[str, ...]:
    """Derive issuer aliases only from issuer-role publisher/domain affinity.

    This supports bilingual targets without a symbol/company lookup table.  A
    publisher fragment is usable only when a meaningful token is also present
    in that source hostname (for example ``SK hynix`` on ``skhynix.com``).
    Generic regulator labels such as ``U.S. SEC`` on ``sec.gov`` are excluded
    because they have no token of at least four characters.
    """

    aliases: list[str] = []
    for fact in facts:
        roles = {
            str(value).strip().upper()
            for value in fact.get("source_role_ids") or ()
        }
        if not roles.intersection(_ISSUER_ALIAS_SOURCE_ROLES):
            continue
        hostname = (urlparse(str(fact.get("source_url") or "")).hostname or "")
        normalized_host = re.sub(r"[^a-z0-9]+", "", hostname.casefold())
        publisher = str(fact.get("source_publisher") or "")
        for fragment in re.split(r"\s*(?:/|\||;)\s*", publisher):
            candidate = fragment.strip()
            tokens = tuple(
                value
                for value in re.findall(r"[a-z0-9]+", candidate.casefold())
                if len(value) >= 4
                and value not in _PUBLISHER_ORGANIZATION_WORDS
            )
            if candidate and any(value in normalized_host for value in tokens):
                aliases.append(candidate)
    return tuple(dict.fromkeys(aliases))


def _source_independence_group(url: str, publisher: str) -> str:
    hostname = (urlparse(url).hostname or "").lower()
    identity = publisher.strip().casefold() or hostname
    return stable_id("PROSRCGROUP", {"identity": identity})


def _issuer_consolidated_scope_projection(
    fact: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Project generic consolidated actuals onto the existing common contract."""

    if fact.get("issuer_scoped") is not True:
        return {}
    segment = str(fact.get("business_segment") or "").casefold()
    if not any(value in segment for value in ("consolidated", "corporate", "연결")):
        return {}
    text = " ".join(
        str(fact.get(key) or "")
        for key in (
            "statement",
            "predicate",
            "economic_mechanism",
            "business_segment",
            "product_family",
        )
    ).casefold()
    aliases = {
        "revenue": ("revenue", "revenues", "매출"),
        "operating_profit": ("operating profit", "영업이익"),
        "net_income": ("net income", "net profit", "당기순이익"),
        "operating_cash_flow": (
            "operating cash flow",
            "영업활동현금흐름",
        ),
        "capex": ("capex", "capital expenditure", "설비투자"),
        "free_cash_flow": ("free cash flow", "fcf", "잉여현금흐름"),
        "cash_balance": ("cash balance", "net cash", "borrowings", "현금", "차입금"),
    }
    contract = ISSUER_CONSOLIDATED_ACTUAL_SCOPE_CONTRACT
    for metric_name, transaction, mechanism in contract.metric_scope_rows:
        if any(token in text for token in aliases.get(metric_name, (metric_name,))):
            return {
                "scope_business_segment": contract.scope_business_segment,
                "scope_product_family": contract.scope_product_family,
                "scope_technology_family": contract.scope_technology_family,
                "scope_transaction_type": transaction,
                "scope_economic_mechanism": mechanism,
                "scope_confidence": 1.0,
            }
    return {}


__all__ = [
    "ACCEPTED_SOURCE_STATUSES",
    "FactSourceVerification",
    "ProSourceVerifier",
    "SOURCE_VERIFICATION_SEMANTICS_VERSION",
    "SourceVerificationResult",
    "TERMINAL_SOURCE_STATUSES",
]
