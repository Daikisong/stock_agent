"""Bounded official-first acquisition for current QuestionSourceTasks."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_os import EvidenceDocument, SourceType
from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.production.source_connectors.source_provider_registry import (
    SourceFetchResult,
    SourceProviderRegistry,
    build_default_source_provider_registry,
)
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.page_fetcher import PageFetcher
from e2r.research.search_provider import SearchProvider, SearchResult

from .provider_capabilities import ProviderDocumentRole, classify_provider_result


LIVE_SOURCE_ACQUISITION_SCHEMA_VERSION = "e2r_live_source_acquisition_v1"


class AcquisitionResultClass(str, Enum):
    REAL_PROVIDER_FETCH = "REAL_PROVIDER_FETCH"
    FRESH_PROVIDER_CACHE = "FRESH_PROVIDER_CACHE"
    EXISTING_LEDGER_REFRESH = "EXISTING_LEDGER_REFRESH"
    NO_RESULT = "NO_RESULT"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    AUTH_FAILED = "AUTH_FAILED"
    RATE_LIMITED = "RATE_LIMITED"
    REJECTED_BY_POLICY = "REJECTED_BY_POLICY"
    SOURCE_EXHAUSTED = "SOURCE_EXHAUSTED"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"
    PROVIDER_HEALTH_ONLY = "PROVIDER_HEALTH_ONLY"


@dataclass(frozen=True)
class SourceAcquisitionConfig:
    as_of_date: str
    max_tasks: int
    test_mode: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not 1 <= self.max_tasks <= 100:
            raise ValueError("live source acquisition task count must be bounded by 100")


@dataclass(frozen=True)
class ProviderRequestRecord:
    provider_request_record_id: str
    source_task_id: str
    target_id: str
    target_name: str
    as_of_date: str
    source_class: str
    provider_name: str
    attempt: int
    max_retries: int
    actual_provider_call: bool
    cache_key: str
    literal_query_ids: tuple[str, ...]
    request_parameters: Mapping[str, Any]
    schema_version: str = LIVE_SOURCE_ACQUISITION_SCHEMA_VERSION

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ProviderFetchResultRecord:
    provider_fetch_result_id: str
    provider_request_record_id: str
    source_task_id: str
    target_id: str
    source_class: str
    provider_name: str
    provider_status: str
    provider_document_role: str
    acquisition_class: str
    cache_hit: bool
    canonical_url: str | None
    official_document_id: str | None
    published_at: str | None
    available_at: str | None
    fetched_at: str | None
    content_hash: str | None
    document_id: str | None
    provider_error: str | None
    policy_rejection_reason: str | None
    schema_version: str = LIVE_SOURCE_ACQUISITION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        AcquisitionResultClass(self.acquisition_class)

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class EvidenceDocumentRecord:
    document_id: str
    target_id: str
    target_name: str
    source_task_ids: tuple[str, ...]
    source_class: str
    provider_name: str
    canonical_url: str
    official_document_id: str
    published_at: str
    available_at: str
    fetched_at: str
    content_hash: str
    content_text: str
    structured_payload: Mapping[str, Any]
    source_lineage_id: str
    acquisition_class: str
    snippet_only: bool = False
    current_score_eligible: bool = False
    schema_version: str = LIVE_SOURCE_ACQUISITION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not all(
            str(item).strip()
            for item in (
                self.document_id,
                self.target_id,
                self.target_name,
                self.canonical_url,
                self.official_document_id,
                self.published_at,
                self.available_at,
                self.fetched_at,
                self.content_hash,
                self.content_text,
                self.source_lineage_id,
            )
        ):
            raise ValueError("live evidence document requires full source and content lineage")
        if not self.source_task_ids:
            raise ValueError("live evidence document requires SourceTask lineage")
        if self.snippet_only or self.current_score_eligible:
            raise ValueError("acquired document cannot be snippet-only or directly score")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SourceAcquisitionRunResult:
    as_of_date: str
    status: str
    provider_requests: tuple[ProviderRequestRecord, ...]
    provider_fetch_results: tuple[ProviderFetchResultRecord, ...]
    evidence_documents: tuple[EvidenceDocumentRecord, ...]
    web_search_tasks: tuple[Mapping[str, Any], ...]
    web_search_results: tuple[Mapping[str, Any], ...]
    web_fetched_documents: tuple[Mapping[str, Any], ...]
    web_rejected_documents: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]


class CurrentSourceAcquisitionOrchestrator:
    def acquire(
        self,
        config: SourceAcquisitionConfig,
        *,
        source_tasks: Sequence[Mapping[str, Any]],
        question_source_tasks: Sequence[Mapping[str, Any]],
        provider_registry: SourceProviderRegistry | None = None,
        web_search_provider: SearchProvider | None = None,
        page_fetcher: PageFetcher | None = None,
    ) -> SourceAcquisitionRunResult:
        if len(question_source_tasks) > config.max_tasks:
            raise ValueError("source acquisition task count exceeds bounded run budget")
        daily_by_question = _unique_mapping(
            source_tasks,
            key="question_task_id",
            context="daily source tasks",
        )
        question_by_id = _unique_mapping(
            question_source_tasks,
            key="task_id",
            context="question source tasks",
        )
        if set(question_by_id) != set(daily_by_question):
            raise ValueError("daily and canonical QuestionSourceTask identities differ")
        registry = provider_registry or build_default_source_provider_registry()
        connectors = tuple(registry.connectors)
        cache: dict[tuple[str, str, str], SourceFetchResult] = {}
        requests: list[ProviderRequestRecord] = []
        fetch_rows: list[ProviderFetchResultRecord] = []
        document_payloads: dict[str, dict[str, Any]] = {}
        web_task_rows: list[Mapping[str, Any]] = []
        web_result_rows: list[Mapping[str, Any]] = []
        web_fetched_rows: list[Mapping[str, Any]] = []
        web_rejected_rows: list[Mapping[str, Any]] = []
        effective_web_search_provider = web_search_provider
        effective_page_fetcher = page_fetcher

        for question_task in question_source_tasks:
            request_start = len(requests)
            fetch_start = len(fetch_rows)
            question_task_id = str(question_task.get("task_id") or "")
            daily_task = daily_by_question[question_task_id]
            _validate_execution_task(
                question_task=question_task,
                daily_task=daily_task,
                as_of_date=config.as_of_date,
                test_mode=config.test_mode,
            )
            route = question_task.get("source_route") or {}
            requested_sources = tuple(route.get("preferred_source_families") or ())
            budget = question_task.get("budget") or {}
            max_queries = int(budget.get("max_queries") or 0)
            max_retries = int(daily_task.get("max_retries") or 0)
            selected_connectors = _ordered_connectors(
                connectors=connectors,
                requested_sources=requested_sources,
            )
            if not selected_connectors:
                request, fetch = _source_exhausted_records(
                    question_task=question_task,
                    daily_task=daily_task,
                    as_of_date=config.as_of_date,
                    requested_sources=requested_sources,
                )
                requests.append(request)
                fetch_rows.append(fetch)
            else:
                attempted = 0
                for source_class, connector in selected_connectors:
                    if attempted >= max_queries:
                        break
                    attempted += 1
                    target_id = str(question_task.get("target_id") or "")
                    provider_name = str(getattr(connector, "provider_name", ""))
                    cache_tuple = (target_id, provider_name, config.as_of_date)
                    cached = cache.get(cache_tuple)
                    if cached is not None:
                        request = _request_record(
                            question_task=question_task,
                            daily_task=daily_task,
                            as_of_date=config.as_of_date,
                            source_class=source_class,
                            provider_name=provider_name,
                            attempt=1,
                            actual_provider_call=False,
                            request_parameters={"cache_hit": True},
                        )
                        requests.append(request)
                        fetch, document = _fetch_record_and_document(
                            request=request,
                            result=cached,
                            question_task=question_task,
                            source_class=source_class,
                            as_of_date=config.as_of_date,
                            cache_hit=True,
                        )
                        fetch_rows.append(fetch)
                        if document is not None:
                            _merge_document(document_payloads, document)
                        continue

                    final_result: SourceFetchResult | None = None
                    for attempt in range(1, max_retries + 2):
                        result = connector.fetch(
                            symbol=target_id,
                            company_name=str(question_task.get("company_name") or ""),
                            as_of_date=date.fromisoformat(config.as_of_date),
                            mode="live",
                        )
                        request = _request_record(
                            question_task=question_task,
                            daily_task=daily_task,
                            as_of_date=config.as_of_date,
                            source_class=source_class,
                            provider_name=provider_name,
                            attempt=attempt,
                            actual_provider_call=True,
                            request_parameters=_safe_request_parameters(result.request_params),
                        )
                        requests.append(request)
                        fetch, document = _fetch_record_and_document(
                            request=request,
                            result=result,
                            question_task=question_task,
                            source_class=source_class,
                            as_of_date=config.as_of_date,
                            cache_hit=False,
                        )
                        fetch_rows.append(fetch)
                        final_result = result
                        if document is not None:
                            _merge_document(document_payloads, document)
                        if not _retryable(result, attempt=attempt, max_retries=max_retries):
                            break
                    if final_result is not None:
                        cache[cache_tuple] = final_result

            task_requests = tuple(requests[request_start:])
            task_fetch_rows = tuple(fetch_rows[fetch_start:])
            official_gap_reasons = _official_gap_reasons(
                daily_task=daily_task,
                fetch_results=task_fetch_rows,
            )
            if _web_fallback_allowed(
                daily_task=daily_task,
                official_requests=task_requests,
                official_gap_reasons=official_gap_reasons,
            ):
                if effective_web_search_provider is None:
                    effective_web_search_provider = NaverFreeSearchProvider(
                        fixture_mode=config.test_mode,
                        live_enabled=not config.test_mode,
                    )
                if effective_page_fetcher is None:
                    effective_page_fetcher = PageFetcher(
                        live_enabled=not config.test_mode,
                    )
                web = _acquire_bounded_web_fallback(
                    question_task=question_task,
                    daily_task=daily_task,
                    as_of_date=config.as_of_date,
                    test_mode=config.test_mode,
                    official_requests=task_requests,
                    official_gap_reasons=official_gap_reasons,
                    search_provider=effective_web_search_provider,
                    page_fetcher=effective_page_fetcher,
                )
                web_task_rows.extend(web["tasks"])
                web_result_rows.extend(web["results"])
                web_fetched_rows.extend(web["fetched"])
                web_rejected_rows.extend(web["rejected"])
                for document in web["documents"]:
                    _merge_document(document_payloads, document)

        documents = tuple(
            EvidenceDocumentRecord(**payload)
            for _, payload in sorted(document_payloads.items())
        )
        audit = _audit_source_acquisition(
            as_of_date=config.as_of_date,
            question_task_count=len(question_source_tasks),
            requests=requests,
            fetch_results=fetch_rows,
            documents=documents,
            web_search_tasks=web_task_rows,
            web_search_results=web_result_rows,
            web_fetched_documents=web_fetched_rows,
            web_rejected_documents=web_rejected_rows,
        )
        return SourceAcquisitionRunResult(
            as_of_date=config.as_of_date,
            status=(
                "CURRENT_SOURCE_ACQUISITION_PASS"
                if audit["hard_acceptance_pass"]
                else "CURRENT_SOURCE_ACQUISITION_FAIL"
            ),
            provider_requests=tuple(requests),
            provider_fetch_results=tuple(fetch_rows),
            evidence_documents=documents,
            web_search_tasks=tuple(web_task_rows),
            web_search_results=tuple(web_result_rows),
            web_fetched_documents=tuple(web_fetched_rows),
            web_rejected_documents=tuple(web_rejected_rows),
            audit=audit,
        )


def write_source_acquisition_run(
    result: SourceAcquisitionRunResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "provider_requests": root / "provider_requests.jsonl",
        "provider_fetch_results": root / "provider_fetch_results.jsonl",
        "evidence_documents": root / "evidence_documents.jsonl",
        "web_search_tasks": root / "web_search_tasks.jsonl",
        "web_search_results": root / "web_search_results.jsonl",
        "web_fetched_documents": root / "web_fetched_documents.jsonl",
        "web_rejected_documents": root / "web_rejected_documents.jsonl",
        "provider_call_report": root / "provider_call_report.json",
    }
    write_jsonl(paths["provider_requests"], (item.to_dict() for item in result.provider_requests))
    write_jsonl(
        paths["provider_fetch_results"],
        (item.to_dict() for item in result.provider_fetch_results),
    )
    write_jsonl(paths["evidence_documents"], (item.to_dict() for item in result.evidence_documents))
    write_jsonl(paths["web_search_tasks"], result.web_search_tasks)
    write_jsonl(paths["web_search_results"], result.web_search_results)
    write_jsonl(paths["web_fetched_documents"], result.web_fetched_documents)
    write_jsonl(paths["web_rejected_documents"], result.web_rejected_documents)
    write_json(paths["provider_call_report"], {**dict(result.audit), "status": result.status})
    return paths


def _request_record(
    *,
    question_task: Mapping[str, Any],
    daily_task: Mapping[str, Any],
    as_of_date: str,
    source_class: str,
    provider_name: str,
    attempt: int,
    actual_provider_call: bool,
    request_parameters: Mapping[str, Any],
) -> ProviderRequestRecord:
    question_task_id = str(question_task.get("task_id") or "")
    target_id = str(question_task.get("target_id") or "")
    cache_key = stable_hash(
        {"target_id": target_id, "provider_name": provider_name, "as_of_date": as_of_date}
    )
    identity = {
        "question_task_id": question_task_id,
        "source_class": source_class,
        "provider_name": provider_name,
        "attempt": attempt,
        "actual_provider_call": actual_provider_call,
    }
    query_intent = question_task.get("query_intent") or {}
    return ProviderRequestRecord(
        provider_request_record_id="PROVREQ-" + stable_hash(identity)[:24],
        source_task_id=question_task_id,
        target_id=target_id,
        target_name=str(question_task.get("company_name") or ""),
        as_of_date=as_of_date,
        source_class=source_class,
        provider_name=provider_name,
        attempt=attempt,
        max_retries=int(daily_task.get("max_retries") or 0),
        actual_provider_call=actual_provider_call,
        cache_key=cache_key,
        literal_query_ids=tuple(
            "QUERY-" + stable_hash({"query": query})[:20]
            for query in query_intent.get("literal_queries") or ()
        ),
        request_parameters=dict(request_parameters),
    )


def _fetch_record_and_document(
    *,
    request: ProviderRequestRecord,
    result: SourceFetchResult,
    question_task: Mapping[str, Any],
    source_class: str,
    as_of_date: str,
    cache_hit: bool,
) -> tuple[ProviderFetchResultRecord, EvidenceDocumentRecord | None]:
    role = classify_provider_result(result)
    rejection = _document_policy_rejection(result, role=role, as_of_date=as_of_date)
    acquisition_class = _acquisition_class(
        result,
        role=role,
        rejection=rejection,
        cache_hit=cache_hit,
    )
    document: EvidenceDocumentRecord | None = None
    document_id: str | None = None
    if acquisition_class in {
        AcquisitionResultClass.REAL_PROVIDER_FETCH.value,
        AcquisitionResultClass.FRESH_PROVIDER_CACHE.value,
    }:
        raw_text = str(result.raw_text or "")
        published = _date_value(result.published_at) or date.fromisoformat(as_of_date)
        available = _date_value(result.available_at) or published
        fetched = _datetime_text(result.fetched_at) or as_of_date
        evidence = EvidenceDocument.from_text(
            text=raw_text,
            canonical_url=result.canonical_url,
            source_type=_source_type(source_class),
            source_name=result.provider_name,
            published_at=published,
            available_at=available,
            fetched_at=_date_value(result.fetched_at) or date.fromisoformat(as_of_date),
            revision_id=result.content_hash,
            parser_version="e2r_live_source_acquisition_v1",
            source_lineage_id=result.provider_request_id or result.request_id,
            source_proxy_only=False,
        )
        document_id = evidence.document_id
        document = EvidenceDocumentRecord(
            document_id=evidence.document_id,
            target_id=str(question_task.get("target_id") or ""),
            target_name=str(question_task.get("company_name") or ""),
            source_task_ids=(str(question_task.get("task_id") or ""),),
            source_class=source_class,
            provider_name=result.provider_name,
            canonical_url=str(result.canonical_url or ""),
            official_document_id=str(result.official_document_id or ""),
            published_at=published.isoformat(),
            available_at=available.isoformat(),
            fetched_at=fetched,
            content_hash=evidence.content_hash,
            content_text=raw_text,
            structured_payload=dict(result.structured_payload),
            source_lineage_id=str(result.provider_request_id or result.request_id),
            acquisition_class=acquisition_class,
        )
    fetch_id = "PROVFETCH-" + stable_hash(
        {
            "provider_request_record_id": request.provider_request_record_id,
            "provider_status": result.status,
            "content_hash": result.content_hash,
            "cache_hit": cache_hit,
        }
    )[:24]
    return (
        ProviderFetchResultRecord(
            provider_fetch_result_id=fetch_id,
            provider_request_record_id=request.provider_request_record_id,
            source_task_id=request.source_task_id,
            target_id=request.target_id,
            source_class=source_class,
            provider_name=result.provider_name,
            provider_status=result.status,
            provider_document_role=role,
            acquisition_class=acquisition_class,
            cache_hit=cache_hit,
            canonical_url=result.canonical_url,
            official_document_id=result.official_document_id,
            published_at=result.published_at,
            available_at=result.available_at,
            fetched_at=result.fetched_at,
            content_hash=result.content_hash,
            document_id=document_id,
            provider_error=result.provider_error,
            policy_rejection_reason=rejection,
        ),
        document,
    )


def _document_policy_rejection(
    result: SourceFetchResult,
    *,
    role: str,
    as_of_date: str,
) -> str | None:
    if role != ProviderDocumentRole.SYMBOL_EVIDENCE.value:
        return None
    if not result.content_hash or not str(result.raw_text or "").strip():
        return "fetched_document_missing_content_or_hash"
    if len(str(result.raw_text or "").strip()) < 80:
        return "fetched_document_content_too_small"
    if "파일이 존재하지 않습니다" in str(result.raw_text or ""):
        return "provider_error_body_not_document"
    cutoff = date.fromisoformat(as_of_date)
    for label, value in (
        ("published_at", result.published_at),
        ("available_at", result.available_at),
    ):
        parsed = _date_value(value)
        if parsed is not None and parsed > cutoff:
            return f"future_document_{label}"
    score_usage = str((result.structured_payload or {}).get("score_usage") or "")
    if any(
        token in score_usage
        for token in (
            "provider_coverage_only",
            "list_only_detail_not_fetched",
            "not_score_evidence",
            "after_as_of_date",
        )
    ):
        return f"non_evidence_provider_payload:{score_usage}"
    return None


def _acquisition_class(
    result: SourceFetchResult,
    *,
    role: str,
    rejection: str | None,
    cache_hit: bool,
) -> str:
    if rejection:
        return AcquisitionResultClass.REJECTED_BY_POLICY.value
    if role == ProviderDocumentRole.SYMBOL_EVIDENCE.value:
        return (
            AcquisitionResultClass.FRESH_PROVIDER_CACHE.value
            if cache_hit
            else AcquisitionResultClass.REAL_PROVIDER_FETCH.value
        )
    if role == ProviderDocumentRole.PROVIDER_HEALTH_ONLY.value:
        return AcquisitionResultClass.PROVIDER_HEALTH_ONLY.value
    if role == ProviderDocumentRole.SNAPSHOT_ONLY.value:
        return AcquisitionResultClass.REJECTED_BY_POLICY.value
    if result.status == "AUTH_FAILED":
        return AcquisitionResultClass.AUTH_FAILED.value
    if result.status == "RATE_LIMITED":
        return AcquisitionResultClass.RATE_LIMITED.value
    if result.status == "PROVIDER_FAILED":
        return AcquisitionResultClass.PROVIDER_FAILED.value
    if result.status == "REJECTED_BY_POLICY":
        return AcquisitionResultClass.REJECTED_BY_POLICY.value
    return AcquisitionResultClass.NO_RESULT.value


def _ordered_connectors(
    *,
    connectors: Sequence[Any],
    requested_sources: Sequence[str],
) -> tuple[tuple[str, Any], ...]:
    ordered: list[tuple[str, Any]] = []
    seen: set[int] = set()
    for source in requested_sources:
        match = _connector_family(source)
        if match is None:
            continue
        for connector in connectors:
            connector_family = _connector_family(
                str(getattr(connector, "source_class", "")),
                provider_name=str(getattr(connector, "provider_name", "")),
            )
            if connector_family != match or id(connector) in seen:
                continue
            ordered.append((str(source), connector))
            seen.add(id(connector))
            break
    return tuple(ordered)


def _connector_family(value: str, *, provider_name: str = "") -> str | None:
    clean = re.sub(r"[^a-z]", "", str(value).casefold())
    provider = re.sub(r"[^a-z]", "", str(provider_name).casefold())
    if clean in {"dart", "opendart"} or provider == "opendart":
        return "DART"
    if clean == "kind" or provider == "kind":
        return "KIND"
    if clean == "krx" or provider == "krx":
        return "KRX"
    if clean in {"companyguide", "wisereport"} or provider == "companyguide":
        return "CompanyGuide"
    if clean in {
        "ir",
        "issuerir",
        "issuernewsroom",
        "companyearningscall",
        "official",
    } or provider == "issuerir":
        return "IssuerIR"
    return None


def _validate_execution_task(
    *,
    question_task: Mapping[str, Any],
    daily_task: Mapping[str, Any],
    as_of_date: str,
    test_mode: bool,
) -> None:
    if str(question_task.get("as_of_date") or "") != as_of_date:
        raise ValueError("QuestionSourceTask as_of_date differs from acquisition run")
    if not test_mode and question_task.get("production_execution_allowed") is not True:
        raise ValueError("only real-provider canonical QuestionSourceTasks may execute live")
    if str(daily_task.get("target_id") or "") != str(question_task.get("target_id") or ""):
        raise ValueError("daily and canonical SourceTask target identity differs")
    budget = question_task.get("budget") or {}
    for name, maximum in (
        ("max_queries", 10),
        ("max_candidates", 100),
        ("max_fetches", 20),
    ):
        value = budget.get(name)
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= maximum:
            raise ValueError(f"canonical acquisition task {name} is unbounded")
    if question_task.get("runtime_score_eligible") is True:
        raise ValueError("SourceTask cannot directly score")


def _source_exhausted_records(
    *,
    question_task: Mapping[str, Any],
    daily_task: Mapping[str, Any],
    as_of_date: str,
    requested_sources: Sequence[str],
) -> tuple[ProviderRequestRecord, ProviderFetchResultRecord]:
    request = _request_record(
        question_task=question_task,
        daily_task=daily_task,
        as_of_date=as_of_date,
        source_class=str(requested_sources[0] if requested_sources else "unknown"),
        provider_name="unregistered_official_source",
        attempt=1,
        actual_provider_call=False,
        request_parameters={"requested_sources": list(requested_sources)},
    )
    fetch = ProviderFetchResultRecord(
        provider_fetch_result_id="PROVFETCH-" + stable_hash({"request": request.provider_request_record_id})[:24],
        provider_request_record_id=request.provider_request_record_id,
        source_task_id=request.source_task_id,
        target_id=request.target_id,
        source_class=request.source_class,
        provider_name=request.provider_name,
        provider_status="SOURCE_EXHAUSTED",
        provider_document_role=ProviderDocumentRole.NO_RESULT.value,
        acquisition_class=AcquisitionResultClass.SOURCE_EXHAUSTED.value,
        cache_hit=False,
        canonical_url=None,
        official_document_id=None,
        published_at=None,
        available_at=None,
        fetched_at=None,
        content_hash=None,
        document_id=None,
        provider_error="no registered official connector for requested source route",
        policy_rejection_reason=None,
    )
    return request, fetch


def _retryable(result: SourceFetchResult, *, attempt: int, max_retries: int) -> bool:
    if attempt > max_retries or result.status not in {"PROVIDER_FAILED", "RATE_LIMITED"}:
        return False
    detail = str(result.provider_error or "").casefold()
    return any(
        token in detail
        for token in ("timeout", "tempor", "connection", "rate limit", "429", "503")
    )


def _merge_document(
    document_payloads: dict[str, dict[str, Any]],
    document: EvidenceDocumentRecord,
) -> None:
    payload = document_payloads.get(document.document_id)
    if payload is None:
        document_payloads[document.document_id] = dict(document.to_dict())
        return
    if payload["target_id"] != document.target_id or payload["content_hash"] != document.content_hash:
        raise ValueError("document identity collision across targets or content")
    payload["source_task_ids"] = tuple(
        dict.fromkeys((*payload["source_task_ids"], *document.source_task_ids))
    )
    if document.acquisition_class == AcquisitionResultClass.REAL_PROVIDER_FETCH.value:
        payload["acquisition_class"] = document.acquisition_class


def _official_gap_reasons(
    *,
    daily_task: Mapping[str, Any],
    fetch_results: Sequence[ProviderFetchResultRecord],
) -> tuple[str, ...]:
    reasons = [
        str(item).strip()
        for item in daily_task.get("official_gap_reasons") or ()
        if str(item).strip()
    ]
    resolved = any(
        item.acquisition_class
        in {
            AcquisitionResultClass.REAL_PROVIDER_FETCH.value,
            AcquisitionResultClass.FRESH_PROVIDER_CACHE.value,
        }
        for item in fetch_results
    )
    if not resolved:
        for item in fetch_results:
            detail = (
                item.policy_rejection_reason
                or item.provider_error
                or item.provider_status
                or item.acquisition_class
            )
            reasons.append(
                f"{item.source_class}:{item.acquisition_class}:{detail}"
            )
        reasons.append("OFFICIAL_SOURCE_UNRESOLVED_AFTER_BOUNDED_ATTEMPT")
    return tuple(dict.fromkeys(reasons))


def _web_fallback_allowed(
    *,
    daily_task: Mapping[str, Any],
    official_requests: Sequence[ProviderRequestRecord],
    official_gap_reasons: Sequence[str],
) -> bool:
    return bool(
        daily_task.get("allows_general_web") is True
        and official_requests
        and official_gap_reasons
    )


def _acquire_bounded_web_fallback(
    *,
    question_task: Mapping[str, Any],
    daily_task: Mapping[str, Any],
    as_of_date: str,
    test_mode: bool,
    official_requests: Sequence[ProviderRequestRecord],
    official_gap_reasons: Sequence[str],
    search_provider: SearchProvider,
    page_fetcher: PageFetcher,
) -> Mapping[str, tuple[Any, ...]]:
    if not test_mode and (
        not isinstance(search_provider, NaverFreeSearchProvider)
        or search_provider.fixture_mode
        or not search_provider.live_enabled
        or search_provider.fixture_provider is not None
    ):
        raise ValueError("production web fallback requires live NaverFreeSearchProvider")
    if not test_mode and (
        not isinstance(page_fetcher, PageFetcher)
        or not page_fetcher.live_enabled
        or bool(page_fetcher.fixture_text_by_url)
    ):
        raise ValueError("production web fallback requires live PageFetcher")
    queries = _validated_llm_literal_queries(
        question_task=question_task,
        daily_task=daily_task,
        test_mode=test_mode,
    )
    budget = _bounded_web_budget(
        question_task=question_task,
        daily_task=daily_task,
    )
    stop = dict(question_task.get("stop_condition") or {})
    if (
        stop.get("stop_on_resolution") is not True
        or daily_task.get("stop_condition") != "stop_on_resolution"
    ):
        raise ValueError("general-web fallback requires stop-on-resolution")

    target_id = str(question_task.get("target_id") or "")
    target_name = str(question_task.get("company_name") or "")
    candidate_event_id = str(question_task.get("candidate_event_id") or "")
    query_intent = dict(question_task.get("query_intent") or {})
    search_provider_name = type(search_provider).__name__
    page_fetcher_name = type(page_fetcher).__name__
    official_request_ids = tuple(
        item.provider_request_record_id for item in official_requests
    )
    cutoff = date.fromisoformat(as_of_date)
    tasks: list[Mapping[str, Any]] = []
    results: list[Mapping[str, Any]] = []
    fetched: list[Mapping[str, Any]] = []
    rejected: list[Mapping[str, Any]] = []
    documents: list[EvidenceDocumentRecord] = []
    seen_urls: set[str] = set()
    candidate_count = 0
    fetch_count = 0
    resolved = False

    for query_index, query in enumerate(queries[: budget["max_queries"]], start=1):
        if resolved or candidate_count >= budget["max_candidates"]:
            break
        query_id = "WEBQUERY-" + stable_hash(
            {
                "source_task_id": str(question_task.get("task_id") or ""),
                "query": query,
            }
        )[:24]
        web_task_id = "WEBTASK-" + stable_hash(
            {
                "query_id": query_id,
                "as_of_date": as_of_date,
                "official_request_ids": official_request_ids,
            }
        )[:24]
        remaining_candidates = budget["max_candidates"] - candidate_count
        error_start = len(getattr(search_provider, "errors", ()))
        built_request_start = len(getattr(search_provider, "built_requests", ()))
        search_error: str | None = None
        try:
            search_results = tuple(
                search_provider.search(
                    query,
                    cutoff,
                    max_results=remaining_candidates,
                )
            )
        except Exception as exc:
            search_results = ()
            search_error = f"{type(exc).__name__}:{exc}"
        provider_errors = tuple(
            str(item)
            for item in tuple(getattr(search_provider, "errors", ()))[error_start:]
        )
        built_request_count = max(
            0,
            len(getattr(search_provider, "built_requests", ()))
            - built_request_start,
        )
        credential_blocked = any(
            "missing_naver_credentials" in item for item in provider_errors
        )
        search_request_count = (
            0 if credential_blocked else (built_request_count or 1)
        )
        local_result_count = 0
        local_fetch_count = 0
        local_rejection_count = 0

        if search_error is not None or provider_errors:
            rejected.append(
                _web_rejection_row(
                    web_task_id=web_task_id,
                    web_result=None,
                    question_task=question_task,
                    query=query,
                    provider_name=search_provider_name,
                    reason="SEARCH_PROVIDER_ERROR",
                    detail=search_error or "; ".join(provider_errors),
                    fetch_attempted=False,
                    full_fetch_performed=False,
                )
            )
            local_rejection_count += 1

        for search_result in search_results:
            if resolved or candidate_count >= budget["max_candidates"]:
                break
            if not isinstance(search_result, SearchResult):
                raise ValueError("web search provider returned a non-SearchResult row")
            url = str(search_result.url or "").strip()
            if not url or url in seen_urls:
                continue
            seen_urls.add(url)
            candidate_count += 1
            local_result_count += 1
            published = (
                search_result.published_at.date()
                if search_result.published_at is not None
                else None
            )
            web_result_id = "WEBRESULT-" + stable_hash(
                {
                    "web_task_id": web_task_id,
                    "url": url,
                    "published_at": published.isoformat() if published else None,
                }
            )[:24]
            base_result = {
                "schema_version": "e2r_live_web_search_result_v1",
                "web_result_id": web_result_id,
                "web_task_id": web_task_id,
                "task_id": str(daily_task.get("task_id") or ""),
                "source_task_id": str(question_task.get("task_id") or ""),
                "candidate_event_id": candidate_event_id,
                "target_id": target_id,
                "symbol": str(question_task.get("symbol") or target_id),
                "company_name": target_name,
                "query_id": query_id,
                "query": query,
                "query_forwarded_verbatim": search_result.query in {None, query},
                "provider_name": search_provider_name,
                "url": url,
                "title": search_result.title,
                "snippet": search_result.snippet,
                "published_at": published.isoformat() if published else None,
                "rank": search_result.rank,
                "discovery_only": True,
                "snippet_score_forbidden": True,
            }
            if search_result.query not in {None, query}:
                results.append(
                    {**base_result, "selection_status": "REJECTED_QUERY_LINEAGE_MISMATCH"}
                )
                rejected.append(
                    _web_rejection_row(
                        web_task_id=web_task_id,
                        web_result=base_result,
                        question_task=question_task,
                        query=query,
                        provider_name=search_provider_name,
                        reason="SEARCH_RESULT_QUERY_LINEAGE_MISMATCH",
                        detail="search result was not returned for the forwarded LLM query",
                        fetch_attempted=False,
                        full_fetch_performed=False,
                    )
                )
                local_rejection_count += 1
                continue
            if not _is_http_url(url):
                results.append({**base_result, "selection_status": "REJECTED_INVALID_URL"})
                rejected.append(
                    _web_rejection_row(
                        web_task_id=web_task_id,
                        web_result=base_result,
                        question_task=question_task,
                        query=query,
                        provider_name=search_provider_name,
                        reason="INVALID_OR_NON_HTTP_URL",
                        detail="web fallback accepts only an http(s) full-document URL",
                        fetch_attempted=False,
                        full_fetch_performed=False,
                    )
                )
                local_rejection_count += 1
                continue
            if published is None:
                results.append({**base_result, "selection_status": "REJECTED_UNKNOWN_DATE"})
                rejected.append(
                    _web_rejection_row(
                        web_task_id=web_task_id,
                        web_result=base_result,
                        question_task=question_task,
                        query=query,
                        provider_name=search_provider_name,
                        reason="UNKNOWN_PUBLISHED_DATE",
                        detail="search discovery date is absent; page cannot enter current evidence",
                        fetch_attempted=False,
                        full_fetch_performed=False,
                    )
                )
                local_rejection_count += 1
                continue
            if published > cutoff:
                results.append({**base_result, "selection_status": "REJECTED_FUTURE_DATE"})
                rejected.append(
                    _web_rejection_row(
                        web_task_id=web_task_id,
                        web_result=base_result,
                        question_task=question_task,
                        query=query,
                        provider_name=search_provider_name,
                        reason="FUTURE_DOCUMENT",
                        detail="search result was published after as_of_date",
                        fetch_attempted=False,
                        full_fetch_performed=False,
                    )
                )
                local_rejection_count += 1
                continue
            if fetch_count >= budget["max_fetches"]:
                results.append({**base_result, "selection_status": "REJECTED_FETCH_BUDGET"})
                rejected.append(
                    _web_rejection_row(
                        web_task_id=web_task_id,
                        web_result=base_result,
                        question_task=question_task,
                        query=query,
                        provider_name=search_provider_name,
                        reason="WEB_FETCH_BUDGET_EXHAUSTED",
                        detail="SourceTask max_fetches was reached",
                        fetch_attempted=False,
                        full_fetch_performed=False,
                    )
                )
                local_rejection_count += 1
                continue

            fetch_count += 1
            local_fetch_count += 1
            try:
                fetch_result = page_fetcher.fetch(url, as_of_date=cutoff)
            except Exception as exc:
                fetch_result = None
                fetch_error = f"{type(exc).__name__}:{exc}"
            else:
                fetch_error = str(fetch_result.reason or "") if not fetch_result.ok else ""
            text = (
                str(fetch_result.text or "")
                if fetch_result is not None and fetch_result.ok
                else ""
            )
            if not text.strip():
                results.append({**base_result, "selection_status": "REJECTED_NO_FULL_FETCH"})
                rejected.append(
                    _web_rejection_row(
                        web_task_id=web_task_id,
                        web_result=base_result,
                        question_task=question_task,
                        query=query,
                        provider_name=search_provider_name,
                        reason="SNIPPET_ONLY_FULL_FETCH_REQUIRED",
                        detail=fetch_error or "PageFetcher returned no full document text",
                        fetch_attempted=True,
                        full_fetch_performed=False,
                    )
                )
                local_rejection_count += 1
                continue
            content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
            if len(text.strip()) < 80:
                results.append({**base_result, "selection_status": "REJECTED_SMALL_CONTENT"})
                rejected.append(
                    _web_rejection_row(
                        web_task_id=web_task_id,
                        web_result=base_result,
                        question_task=question_task,
                        query=query,
                        provider_name=search_provider_name,
                        reason="FULL_DOCUMENT_CONTENT_TOO_SMALL",
                        detail="PageFetcher text is too small to be a full evidence document",
                        fetch_attempted=True,
                        full_fetch_performed=True,
                        content_hash=content_hash,
                    )
                )
                local_rejection_count += 1
                continue
            if not _document_mentions_target(text, question_task=question_task):
                results.append({**base_result, "selection_status": "REJECTED_WRONG_SUBJECT"})
                rejected.append(
                    _web_rejection_row(
                        web_task_id=web_task_id,
                        web_result=base_result,
                        question_task=question_task,
                        query=query,
                        provider_name=search_provider_name,
                        reason="WRONG_SUBJECT_FULL_DOCUMENT",
                        detail="full fetched page does not mention the task target or symbol",
                        fetch_attempted=True,
                        full_fetch_performed=True,
                        content_hash=content_hash,
                    )
                )
                local_rejection_count += 1
                continue
            if hashlib.sha256(text.encode("utf-8")).hexdigest() != content_hash:
                raise ValueError("web full-document content hash mismatch")

            web_fetch_id = "WEBFETCH-" + stable_hash(
                {
                    "web_result_id": web_result_id,
                    "content_hash": content_hash,
                }
            )[:24]
            fetched_at = (
                fetch_result.fetched_at.isoformat()
                if fetch_result is not None and fetch_result.fetched_at is not None
                else as_of_date
            )
            combined_provider_name = f"{search_provider_name}+{page_fetcher_name}"
            evidence = EvidenceDocument.from_text(
                text=text,
                canonical_url=url,
                source_type=(SourceType.NEWS if search_result.is_news else SourceType.OTHER),
                source_name=combined_provider_name,
                published_at=published,
                available_at=published,
                fetched_at=_date_value(fetched_at) or cutoff,
                revision_id=content_hash,
                parser_version="e2r_live_naver_page_fetch_v1",
                source_lineage_id=web_fetch_id,
                source_proxy_only=False,
            )
            source_class = "TrustedNews" if search_result.is_news else "GeneralWeb"
            document = EvidenceDocumentRecord(
                document_id=evidence.document_id,
                target_id=target_id,
                target_name=target_name,
                source_task_ids=(str(question_task.get("task_id") or ""),),
                source_class=source_class,
                provider_name=combined_provider_name,
                canonical_url=url,
                official_document_id="web:" + stable_hash({"url": url})[:24],
                published_at=published.isoformat(),
                available_at=published.isoformat(),
                fetched_at=fetched_at,
                content_hash=evidence.content_hash,
                content_text=text,
                structured_payload={
                    "discovery_provider": search_provider_name,
                    "query_id": query_id,
                    "web_task_id": web_task_id,
                    "web_result_id": web_result_id,
                    "full_fetch_performed": True,
                    "target_direct": True,
                    "snippet_score_forbidden": True,
                },
                source_lineage_id=web_fetch_id,
                acquisition_class=AcquisitionResultClass.REAL_PROVIDER_FETCH.value,
            )
            documents.append(document)
            fetched.append(
                {
                    "schema_version": "e2r_live_web_fetched_document_v1",
                    "web_fetch_id": web_fetch_id,
                    "web_result_id": web_result_id,
                    "web_task_id": web_task_id,
                    "task_id": str(daily_task.get("task_id") or ""),
                    "source_task_id": str(question_task.get("task_id") or ""),
                    "candidate_event_id": candidate_event_id,
                    "target_id": target_id,
                    "symbol": str(question_task.get("symbol") or target_id),
                    "company_name": target_name,
                    "query_id": query_id,
                    "query": query,
                    "provider_name": combined_provider_name,
                    "url": url,
                    "title": search_result.title,
                    "published_at": published.isoformat(),
                    "available_at": published.isoformat(),
                    "fetched_at": fetched_at,
                    "content_type": (
                        fetch_result.content_type if fetch_result is not None else None
                    ),
                    "content_hash": content_hash,
                    "content_text": text,
                    "document_id": evidence.document_id,
                    "source_lineage_id": web_fetch_id,
                    "full_fetch_performed": True,
                    "target_direct": True,
                    "snippet_used_as_document": False,
                    "snippet_score_forbidden": True,
                    "accepted_for_claim_compilation": True,
                }
            )
            results.append({**base_result, "selection_status": "FETCHED_FULL_DOCUMENT"})
            resolved = True

        if not search_results and search_error is None and not provider_errors:
            rejected.append(
                _web_rejection_row(
                    web_task_id=web_task_id,
                    web_result=None,
                    question_task=question_task,
                    query=query,
                    provider_name=search_provider_name,
                    reason="SEARCH_NO_RESULT",
                    detail="Naver/web discovery returned no bounded candidate",
                    fetch_attempted=False,
                    full_fetch_performed=False,
                )
            )
            local_rejection_count += 1
        tasks.append(
            {
                "schema_version": "e2r_live_web_search_task_v1",
                "web_task_id": web_task_id,
                "task_id": str(daily_task.get("task_id") or ""),
                "source_task_id": str(question_task.get("task_id") or ""),
                "candidate_event_id": candidate_event_id,
                "target_id": target_id,
                "symbol": str(question_task.get("symbol") or target_id),
                "company_name": target_name,
                "as_of_date": as_of_date,
                "query_id": query_id,
                "query": query,
                "query_index": query_index,
                "query_forwarded_verbatim": True,
                "query_generator_kind": query_intent.get("generator_kind"),
                "query_provider_name": query_intent.get("provider_name"),
                "query_prompt_hash": query_intent.get("prompt_hash"),
                "query_response_hash": query_intent.get("response_hash"),
                "provider_name": search_provider_name,
                "page_fetcher_name": page_fetcher_name,
                "search_provider_invoked": True,
                "search_call_executed": search_request_count > 0,
                "search_request_count": search_request_count,
                "status": (
                    "RESOLVED_STOPPED"
                    if resolved
                    else ("PROVIDER_FAILED" if search_error or provider_errors else "SEARCH_EXECUTED")
                ),
                "result_count": local_result_count,
                "fetch_count": local_fetch_count,
                "rejected_count": local_rejection_count,
                "official_first_attempted": True,
                "official_request_record_ids": list(official_request_ids),
                "official_gap_reasons": list(official_gap_reasons),
                "allows_general_web": True,
                "stop_condition": "stop_on_resolution",
                "budget": dict(budget),
                "provider_errors": list(provider_errors),
                "search_error": search_error,
            }
        )

    return {
        "tasks": tuple(tasks),
        "results": tuple(results),
        "fetched": tuple(fetched),
        "rejected": tuple(rejected),
        "documents": tuple(documents),
    }


def _validated_llm_literal_queries(
    *,
    question_task: Mapping[str, Any],
    daily_task: Mapping[str, Any],
    test_mode: bool,
) -> tuple[str, ...]:
    query_intent = dict(question_task.get("query_intent") or {})
    generator_kind = str(query_intent.get("generator_kind") or "")
    allowed = {"REAL_LLM"}
    if test_mode:
        allowed.add("TEST_FIXTURE_LLM")
    if generator_kind not in allowed:
        raise ValueError("web fallback requires LLM-generated QuestionSourceTask queries")
    queries = tuple(
        str(item).strip()
        for item in query_intent.get("literal_queries") or ()
        if str(item).strip()
    )
    if not queries or len(queries) != len(set(queries)):
        raise ValueError("web fallback literal queries are empty or duplicated")
    if not _is_sha256(str(query_intent.get("prompt_hash") or "")) or not _is_sha256(
        str(query_intent.get("response_hash") or "")
    ):
        raise ValueError("web fallback query prompt/response lineage is invalid")
    daily_queries = tuple(
        str(item).strip()
        for item in daily_task.get("literal_queries") or ()
        if str(item).strip()
    )
    if daily_queries and daily_queries != queries:
        raise ValueError("daily SourceTask changed the LLM-generated literal queries")
    return queries


def _bounded_web_budget(
    *,
    question_task: Mapping[str, Any],
    daily_task: Mapping[str, Any],
) -> Mapping[str, int]:
    question_budget = dict(question_task.get("budget") or {})
    result: dict[str, int] = {}
    for name, maximum in (
        ("max_queries", 10),
        ("max_candidates", 100),
        ("max_fetches", 20),
    ):
        question_value = question_budget.get(name)
        daily_value = daily_task.get(name, question_value)
        for value in (question_value, daily_value):
            if (
                isinstance(value, bool)
                or not isinstance(value, int)
                or not 1 <= value <= maximum
            ):
                raise ValueError(f"web fallback {name} is unbounded")
        result[name] = min(question_value, daily_value)
    return result


def _web_rejection_row(
    *,
    web_task_id: str,
    web_result: Mapping[str, Any] | None,
    question_task: Mapping[str, Any],
    query: str,
    provider_name: str,
    reason: str,
    detail: str,
    fetch_attempted: bool,
    full_fetch_performed: bool,
    content_hash: str | None = None,
) -> Mapping[str, Any]:
    web_result_id = str((web_result or {}).get("web_result_id") or "") or None
    identity = {
        "web_task_id": web_task_id,
        "web_result_id": web_result_id,
        "reason": reason,
    }
    return {
        "schema_version": "e2r_live_web_rejected_document_v1",
        "web_rejected_id": "WEBREJECT-" + stable_hash(identity)[:24],
        "web_result_id": web_result_id,
        "web_task_id": web_task_id,
        "source_task_id": str(question_task.get("task_id") or ""),
        "candidate_event_id": str(question_task.get("candidate_event_id") or ""),
        "target_id": str(question_task.get("target_id") or ""),
        "symbol": str(question_task.get("symbol") or question_task.get("target_id") or ""),
        "company_name": str(question_task.get("company_name") or ""),
        "query": query,
        "provider_name": provider_name,
        "url": (web_result or {}).get("url"),
        "title": (web_result or {}).get("title"),
        "published_at": (web_result or {}).get("published_at"),
        "rejection_reason": reason,
        "rejection_detail": detail,
        "fetch_attempted": fetch_attempted,
        "full_fetch_performed": full_fetch_performed,
        "content_hash": content_hash,
        "snippet_used_as_document": False,
        "snippet_score_forbidden": True,
        "accepted_claim_ids": [],
    }


def _document_mentions_target(
    text: str,
    *,
    question_task: Mapping[str, Any],
) -> bool:
    normalized_text = re.sub(r"[^0-9a-z가-힣]", "", text.casefold())
    identities = (
        str(question_task.get("company_name") or ""),
        str(question_task.get("symbol") or ""),
        str(question_task.get("target_id") or ""),
        *(question_task.get("target_aliases") or ()),
    )
    return any(
        len(normalized) >= 2 and normalized in normalized_text
        for normalized in (
            re.sub(r"[^0-9a-z가-힣]", "", str(item).casefold())
            for item in identities
        )
    )


def _is_http_url(value: str) -> bool:
    return bool(re.match(r"^https?://[^\s]+$", value, flags=re.IGNORECASE))


def _is_sha256(value: str) -> bool:
    return bool(re.fullmatch(r"[0-9a-f]{64}", value))


def _audit_source_acquisition(
    *,
    as_of_date: str,
    question_task_count: int,
    requests: Sequence[ProviderRequestRecord],
    fetch_results: Sequence[ProviderFetchResultRecord],
    documents: Sequence[EvidenceDocumentRecord],
    web_search_tasks: Sequence[Mapping[str, Any]],
    web_search_results: Sequence[Mapping[str, Any]],
    web_fetched_documents: Sequence[Mapping[str, Any]],
    web_rejected_documents: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    class_counts: dict[str, int] = {}
    provider_counts: dict[str, int] = {}
    for row in fetch_results:
        class_counts[row.acquisition_class] = class_counts.get(row.acquisition_class, 0) + 1
        provider_counts[row.provider_name] = provider_counts.get(row.provider_name, 0) + int(
            not row.cache_hit
        )
    official_actual_or_fresh = sum(
        row.acquisition_class
        in {
            AcquisitionResultClass.REAL_PROVIDER_FETCH.value,
            AcquisitionResultClass.FRESH_PROVIDER_CACHE.value,
        }
        for row in fetch_results
    )
    web_fetch_attempt_count = len(web_fetched_documents) + sum(
        item.get("fetch_attempted") is True for item in web_rejected_documents
    )
    actual_or_fresh = official_actual_or_fresh + len(web_fetched_documents)
    for item in web_search_tasks:
        provider = str(item.get("provider_name") or "NaverFreeSearchProvider")
        provider_counts[provider] = provider_counts.get(provider, 0) + int(
            item.get("search_request_count") or 0
        )
    if web_fetch_attempt_count:
        provider_counts["PageFetcher"] = web_fetch_attempt_count
    if web_fetched_documents:
        class_counts[AcquisitionResultClass.REAL_PROVIDER_FETCH.value] = (
            class_counts.get(AcquisitionResultClass.REAL_PROVIDER_FETCH.value, 0)
            + len(web_fetched_documents)
        )
    task_by_source_id = {
        str(item.get("source_task_id") or ""): item for item in web_search_tasks
    }
    web_budget_violation = 0
    for source_task_id, task in task_by_source_id.items():
        budget = dict(task.get("budget") or {})
        query_count = sum(
            str(item.get("source_task_id") or "") == source_task_id
            for item in web_search_tasks
        )
        candidate_count = sum(
            str(item.get("source_task_id") or "") == source_task_id
            for item in web_search_results
        )
        fetch_count = sum(
            str(item.get("source_task_id") or "") == source_task_id
            for item in web_fetched_documents
        ) + sum(
            str(item.get("source_task_id") or "") == source_task_id
            and item.get("fetch_attempted") is True
            for item in web_rejected_documents
        )
        web_budget_violation += int(
            query_count > int(budget.get("max_queries") or 0)
            or candidate_count > int(budget.get("max_candidates") or 0)
            or fetch_count > int(budget.get("max_fetches") or 0)
        )
    critical = {
        "actual_live_or_fresh_document_empty": int(actual_or_fresh <= 0),
        "generic_portal_counted_as_symbol_evidence": sum(
            row.provider_document_role == ProviderDocumentRole.PROVIDER_HEALTH_ONLY.value
            and row.document_id is not None
            for row in fetch_results
        ),
        "fetched_without_content_hash": sum(not item.content_hash for item in documents),
        "fetched_content_hash_mismatch": sum(
            hashlib.sha256(item.content_text.encode("utf-8")).hexdigest()
            != item.content_hash
            for item in documents
        ),
        "future_document": sum(
            date.fromisoformat(item.published_at) > date.fromisoformat(as_of_date)
            or date.fromisoformat(item.available_at) > date.fromisoformat(as_of_date)
            for item in documents
        ),
        "snippet_document": sum(item.snippet_only for item in documents)
        + sum(
            item.get("snippet_used_as_document") is True
            for item in web_fetched_documents
        ),
        "snapshot_counted_live": sum(
            row.acquisition_class
            in {
                AcquisitionResultClass.REAL_PROVIDER_FETCH.value,
                AcquisitionResultClass.FRESH_PROVIDER_CACHE.value,
            }
            and row.provider_document_role == ProviderDocumentRole.SNAPSHOT_ONLY.value
            for row in fetch_results
        ),
        "wrong_subject_document_to_claim": sum(
            item.get("target_direct") is not True
            for item in web_fetched_documents
        ),
        "provider_failure_masked_no_result": sum(
            row.provider_status in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED"}
            and row.acquisition_class == AcquisitionResultClass.NO_RESULT.value
            for row in fetch_results
        ),
        "web_fallback_without_official_attempt_or_gap": sum(
            item.get("official_first_attempted") is not True
            or not item.get("official_request_record_ids")
            or not item.get("official_gap_reasons")
            or item.get("allows_general_web") is not True
            for item in web_search_tasks
        ),
        "web_query_not_llm_generated": sum(
            item.get("query_generator_kind") not in {"REAL_LLM", "TEST_FIXTURE_LLM"}
            or not _is_sha256(str(item.get("query_prompt_hash") or ""))
            or not _is_sha256(str(item.get("query_response_hash") or ""))
            for item in web_search_tasks
        ),
        "web_query_mutated_after_llm": sum(
            item.get("query_forwarded_verbatim") is not True
            for item in (*web_search_tasks, *web_search_results)
        ),
        "web_budget_violation": web_budget_violation,
        "web_future_document_accepted": sum(
            date.fromisoformat(str(item.get("published_at")))
            > date.fromisoformat(as_of_date)
            for item in web_fetched_documents
        ),
        "web_full_fetch_hash_mismatch": sum(
            hashlib.sha256(str(item.get("content_text") or "").encode("utf-8")).hexdigest()
            != item.get("content_hash")
            for item in web_fetched_documents
        ),
    }
    return {
        "schema_version": "e2r_live_source_acquisition_audit_v1",
        "as_of_date": as_of_date,
        "question_source_task_count": question_task_count,
        "provider_request_count": len(requests),
        "actual_provider_call_count": sum(item.actual_provider_call for item in requests)
        + sum(int(item.get("search_request_count") or 0) for item in web_search_tasks)
        + web_fetch_attempt_count,
        "fresh_cache_request_count": sum(not item.actual_provider_call for item in requests),
        "provider_fetch_result_count": len(fetch_results),
        "unique_evidence_document_count": len(documents),
        "actual_live_or_fresh_document_count": actual_or_fresh,
        "acquisition_class_counts": dict(sorted(class_counts.items())),
        "actual_provider_call_counts": dict(sorted(provider_counts.items())),
        "web_search_task_count": len(web_search_tasks),
        "web_search_request_count": sum(
            int(item.get("search_request_count") or 0) for item in web_search_tasks
        ),
        "web_search_result_count": len(web_search_results),
        "web_fetch_count": web_fetch_attempt_count,
        "web_fetched_document_count": len(web_fetched_documents),
        "web_rejected_document_count": len(web_rejected_documents),
        "web_fallback_deferred_until_question_resolution": not bool(web_search_tasks),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
        "production_runtime_ready": False,
        "result_hash": hashlib.sha256(
            json.dumps(
                [item.to_dict() for item in documents],
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest(),
    }


def _safe_request_parameters(value: Mapping[str, Any]) -> Mapping[str, Any]:
    forbidden = {"crtfc_key", "api_key", "client_secret", "authorization", "token"}
    return {
        str(key): item
        for key, item in value.items()
        if str(key).casefold() not in forbidden
    }


def _source_type(source_class: str) -> SourceType:
    family = _connector_family(source_class)
    if family in {"DART", "KIND"}:
        return SourceType.FILING
    if family == "IssuerIR":
        return SourceType.IR
    if family == "CompanyGuide":
        return SourceType.RESEARCH_REPORT
    return SourceType.API


def _date_value(value: Any) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        try:
            return date.fromisoformat(text[:10])
        except ValueError:
            return None


def _datetime_text(value: Any) -> str | None:
    text = str(value or "").strip()
    return text or None


def _unique_mapping(
    rows: Sequence[Mapping[str, Any]],
    *,
    key: str,
    context: str,
) -> Mapping[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        identity = str(row.get(key) or "")
        if not identity or identity in result:
            raise ValueError(f"duplicate or empty identity in {context}")
        result[identity] = row
    return result


__all__ = [
    "LIVE_SOURCE_ACQUISITION_SCHEMA_VERSION",
    "AcquisitionResultClass",
    "CurrentSourceAcquisitionOrchestrator",
    "EvidenceDocumentRecord",
    "ProviderFetchResultRecord",
    "ProviderRequestRecord",
    "SourceAcquisitionConfig",
    "SourceAcquisitionRunResult",
    "write_source_acquisition_run",
]
