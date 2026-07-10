"""Real-source acquisition layer for Research Brain v4 production shadow."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from dataclasses import dataclass, replace
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import parse_qs, urlsplit, urlunsplit

from e2r.agentic.evidence_os import AnchorType, EvidenceAnchor, EvidenceDocument, SourceType
from e2r.production.source_connectors.source_provider_registry import (
    SourceFetchResult,
    SourceProviderRegistry,
    build_default_source_provider_registry,
)
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.page_fetcher import FetchResult, PageFetcher
from e2r.research.search_provider import SearchProvider, SearchResult
from e2r.research_brain.schemas import SourceTask
from e2r.research_brain.v2_schemas import CandidateEventV2
from e2r.research_brain.v4_schemas import SourceAcquisitionModeV4, SourceAcquisitionResultV4
from e2r.sources.report_search import is_recognized_report_domain, is_verified_report_original_url


@dataclass(frozen=True)
class StoredSourceSnapshot:
    source_class: str
    provider_name: str
    source_path: Path
    symbol: str
    company_name: str
    published_at: date | None
    text: str
    canonical_url: str
    anchor_type: AnchorType
    normalized_value: Mapping[str, Any]


@dataclass(frozen=True)
class _TargetScopedQueryPlan:
    accepted: tuple[str, ...]
    rejected: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class _OfficialDetailRoute:
    source_class: str
    provider_name: str
    resolver_name: str
    official_document_id: str


@dataclass(frozen=True)
class _VerifiedIssuerWebRoute:
    source_class: str
    provider_name: str
    resolver_name: str
    official_document_id: str
    matched_homepage_host: str
    matched_result_host: str
    authority_source_kind: str = ""
    authority_source_url: str = ""
    authority_source_anchor_text: str = ""
    authority_entry_id: str = ""


@dataclass(frozen=True)
class _IssuerOfficialDomainAuthority:
    host: str
    source_class: str
    source_kind: str
    source_url: str
    source_anchor_text: str
    entry_id: str = ""


@dataclass(frozen=True)
class _VerifiedReportWebRoute:
    source_class: str
    provider_name: str
    resolver_name: str
    official_document_id: str
    matched_result_host: str


class SourceAcquisitionRunnerV4:
    """Acquire real source snapshots or live official-provider results.

    The default ``frozen_real_source_snapshot`` mode reads already stored source
    snapshots. That is intentionally different from v3: a candidate event
    summary is never converted into a score-eligible document.
    """

    def __init__(
        self,
        *,
        mode: str = SourceAcquisitionModeV4.FROZEN_REAL_SOURCE_SNAPSHOT.value,
        repo_root: str | Path = ".",
        source_provider_registry: SourceProviderRegistry | None = None,
        web_search_provider: SearchProvider | None = None,
        web_page_fetcher: PageFetcher | None = None,
    ) -> None:
        self.mode = SourceAcquisitionModeV4(mode)
        self.repo_root = Path(repo_root)
        self._source_provider_registry = source_provider_registry
        self._web_search_provider = web_search_provider
        self._web_page_fetcher = web_page_fetcher

    def acquire(self, *, event: CandidateEventV2, task: SourceTask, as_of_date: date) -> SourceAcquisitionResultV4:
        policy_rejection = _policy_rejection(task)
        if policy_rejection:
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class="policy",
                provider_name="v4_policy_validator",
                status="REJECTED_BY_POLICY",
                provider_errors=policy_rejection,
                budget_used={"queries": 0, "candidates": 0, "fetches": 0},
                stop_reason="source_task_rejected_by_v4_policy",
            )
        if self.mode == SourceAcquisitionModeV4.TEST_FAKE:
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class="test_fake",
                provider_name="test_fake_source_provider",
                status="PROVIDER_FAILED",
                provider_errors=("test_fake_source_not_score_eligible",),
                budget_used={"queries": 1, "candidates": 0, "fetches": 0},
                stop_reason="test_fake_source_never_scores",
            )
        if self.mode in {
            SourceAcquisitionModeV4.LIVE_OFFICIAL_FIRST,
            SourceAcquisitionModeV4.LIVE_OFFICIAL_ONLY,
            SourceAcquisitionModeV4.LIVE_FULL_BOUNDED,
        }:
            if self.mode == SourceAcquisitionModeV4.LIVE_FULL_BOUNDED and _task_prefers_external_web(task):
                return self._acquire_live_web_sources(event=event, task=task, as_of_date=as_of_date)
            live_result = self._acquire_live_official_sources(event=event, task=task, as_of_date=as_of_date)
            if self.mode == SourceAcquisitionModeV4.LIVE_FULL_BOUNDED and _task_requests_external_web(task):
                web_task = _remaining_web_task_after_live_result(task=task, live_result=live_result)
                if web_task is None:
                    return live_result
                web_result = self._acquire_live_web_sources(event=event, task=web_task, as_of_date=as_of_date)
                return _merge_live_official_and_web_results(live_result=live_result, web_result=web_result)
            if live_result.status == "PARSED" or self.mode == SourceAcquisitionModeV4.LIVE_OFFICIAL_ONLY:
                return live_result
            if self.mode == SourceAcquisitionModeV4.LIVE_FULL_BOUNDED and _task_requests_external_web(task):
                return self._acquire_live_web_sources(event=event, task=task, as_of_date=as_of_date)
        snapshots = tuple(
            sorted(
                self._candidate_snapshots(event=event, task=task, as_of_date=as_of_date),
                key=lambda item: _snapshot_relevance(task.primitive_gap, item.text),
                reverse=True,
            )
        )
        if not snapshots:
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class=_first_source_class(task),
                provider_name=f"{self.mode.value}_provider",
                status="PROVIDER_FAILED" if self.mode != SourceAcquisitionModeV4.FROZEN_REAL_SOURCE_SNAPSHOT else "NO_EVIDENCE_FOUND",
                provider_errors=()
                if self.mode == SourceAcquisitionModeV4.FROZEN_REAL_SOURCE_SNAPSHOT
                else (f"{self.mode.value}_provider_has_no_matching_document",),
                budget_used={"queries": 1, "candidates": 0, "fetches": 0},
                stop_reason="no_matching_real_source_snapshot",
            )
        documents: list[EvidenceDocument] = []
        anchors: list[EvidenceAnchor] = []
        text_by_id: dict[str, str] = {}
        for snapshot in snapshots[: task.max_fetches]:
            document = EvidenceDocument.from_text(
                text=snapshot.text,
                canonical_url=snapshot.canonical_url,
                source_type=_source_type(snapshot.source_class),
                source_name=snapshot.provider_name,
                published_at=snapshot.published_at,
                available_at=snapshot.published_at,
                fetched_at=as_of_date,
                parser_version="research_brain_v4_real_source_snapshot",
                source_lineage_id=f"{snapshot.source_class}:{snapshot.source_path}",
                source_proxy_only=False,
            )
            anchor = _anchor_for_snapshot(document=document, snapshot=snapshot)
            documents.append(document)
            anchors.append(anchor)
            text_by_id[document.document_id] = snapshot.text
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class=_first_source_class(task),
            provider_name="stored_real_source_snapshot_provider",
            status="PARSED",
            documents=tuple(documents),
            anchors=tuple(anchors),
            document_text_by_id=text_by_id,
            fetched_document_ids=tuple(document.document_id for document in documents),
            document_urls=tuple(document.canonical_url or "" for document in documents),
            document_hashes=tuple(document.content_hash for document in documents),
            anchor_ids=tuple(anchor.anchor_id for anchor in anchors),
            budget_used={"queries": 1, "candidates": len(snapshots), "fetches": len(documents)},
            stop_reason="stored_real_source_snapshot_parsed",
        )

    def _acquire_live_official_sources(
        self,
        *,
        event: CandidateEventV2,
        task: SourceTask,
        as_of_date: date,
    ) -> SourceAcquisitionResultV4:
        registry = self._source_provider_registry or build_default_source_provider_registry(self.repo_root)
        requested_classes = tuple(
            dict.fromkeys(_normalize_source_class(item) for item in (*task.preferred_source_classes, *task.fallback_source_classes))
        )
        connectors = _ordered_live_official_connectors(
            connectors=registry.connectors,
            requested_classes=requested_classes,
        )
        if not connectors:
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class=_first_source_class(task),
                provider_name="live_official_source_provider_registry",
                status="PROVIDER_FAILED",
                provider_errors=("no_live_connector_for_requested_source_class",),
                budget_used={"queries": 0, "candidates": 0, "fetches": 0},
                stop_reason="no_matching_live_official_connector",
            )

        fetch_results: list[SourceFetchResult] = []
        documents: list[EvidenceDocument] = []
        anchors: list[EvidenceAnchor] = []
        text_by_id: dict[str, str] = {}
        attempts = 0
        max_official_attempts = min(int(task.max_queries), int(task.max_candidates))
        for connector in connectors[:max_official_attempts]:
            if attempts >= int(task.max_queries) or len(documents) >= task.max_fetches:
                break
            attempts += 1
            result = connector.fetch(
                symbol=event.symbol,
                company_name=event.company_name,
                as_of_date=as_of_date,
                mode="live",
            )
            fetch_results.append(result)
            if not result.counts_as_live:
                continue
            text = _source_fetch_text(result)
            if not text.strip():
                continue
            document = EvidenceDocument.from_text(
                text=text,
                canonical_url=result.canonical_url,
                source_type=_source_type(result.source_class),
                source_name=result.provider_name,
                published_at=_date_or_datetime_from_any(result.published_at) or as_of_date,
                available_at=_date_or_datetime_from_any(result.available_at) or as_of_date,
                fetched_at=_date_or_datetime_from_any(result.fetched_at) or as_of_date,
                revision_id=result.content_hash,
                parser_version="research_brain_v4_live_source_fetch",
                source_lineage_id=result.provider_request_id or result.request_id,
                source_proxy_only=False,
                score_block_reasons=_score_block_reasons_for_live_result(result),
            )
            anchor_text = _source_fetch_anchor_text(result=result, fallback_text=text)
            anchor = EvidenceAnchor.structured(
                document=document,
                anchor_type=AnchorType.API_RECORD,
                locator=f"live:{result.provider_name}:{result.official_document_id or result.request_id}",
                normalized_value={
                    "symbol": event.symbol,
                    "company_name": event.company_name,
                    "provider": result.provider_name,
                    "source_class": result.source_class,
                    "official_document_id": result.official_document_id,
                    "provider_request_id": result.provider_request_id,
                    "row": dict(result.structured_payload),
                },
                exact_text=anchor_text,
                anchor_verified=True,
            )
            documents.append(document)
            anchors.append(anchor)
            text_by_id[document.document_id] = text

        provider_errors = tuple(
            dict.fromkeys(
                str(result.provider_error)
                for result in fetch_results
                if result.provider_error and result.status != "FETCHED"
            )
        )
        if not documents:
            status = "NO_EVIDENCE_FOUND" if fetch_results and not provider_errors else "PROVIDER_FAILED"
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class=_first_source_class(task),
                provider_name="live_official_source_provider_registry",
                status=status,
                provider_errors=provider_errors or ("live_official_provider_returned_no_score_anchor",),
                budget_used={"queries": attempts, "candidates": len(fetch_results), "fetches": 0},
                stop_reason="live_official_no_fetchable_document",
            )

        effective_source_class = _effective_source_class_for_documents(task=task, documents=tuple(documents))
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class=effective_source_class,
            provider_name="live_official_source_provider_registry",
            status="PARSED",
            documents=tuple(documents),
            anchors=tuple(anchors),
            document_text_by_id=text_by_id,
            fetched_document_ids=tuple(document.document_id for document in documents),
            document_urls=tuple(document.canonical_url or "" for document in documents),
            document_hashes=tuple(document.content_hash for document in documents),
            anchor_ids=tuple(anchor.anchor_id for anchor in anchors),
            provider_errors=provider_errors,
            budget_used={"queries": attempts, "candidates": len(fetch_results), "fetches": len(documents)},
            stop_reason="live_official_source_parsed",
        )

    def _acquire_live_web_sources(
        self,
        *,
        event: CandidateEventV2,
        task: SourceTask,
        as_of_date: date,
    ) -> SourceAcquisitionResultV4:
        provider = self._web_search_provider or NaverFreeSearchProvider(fixture_mode=False, live_enabled=True)
        fetcher = self._web_page_fetcher or PageFetcher(
            live_enabled=True,
            cache_directory=self.repo_root / "data/cache/research_brain_v4_web_fetch",
        )
        provider_name = _search_provider_name(provider)
        query_plan = _target_scoped_web_queries(task=task, event=event)
        web_task_rows: list[dict[str, Any]] = []
        web_result_rows: list[dict[str, Any]] = []
        web_fetched_rows: list[dict[str, Any]] = []
        web_rejected_rows: list[dict[str, Any]] = []
        provider_errors: list[str] = []
        documents: list[EvidenceDocument] = []
        anchors: list[EvidenceAnchor] = []
        text_by_id: dict[str, str] = {}
        executed_query_count = 0
        search_result_count = 0
        fetch_attempt_count = 0
        fetched_or_attempted_urls: set[str] = set()

        if not query_plan.accepted:
            web_task_rows.append(
                _web_task_row(
                    task=task,
                    event=event,
                    provider_name=provider_name,
                    as_of_date=as_of_date,
                    query=None,
                    status="REJECTED_BY_POLICY",
                    rejection_reason="missing_target_scoped_llm_query_intent",
                    result_count=0,
                    fetched_document_count=0,
                    rejected_document_count=len(query_plan.rejected),
                )
            )
            for query, reason in query_plan.rejected:
                web_rejected_rows.append(
                    _web_rejected_row(
                        task=task,
                        event=event,
                        provider_name=provider_name,
                        as_of_date=as_of_date,
                        query=query,
                        result=None,
                        reason=reason,
                    )
                )
            return SourceAcquisitionResultV4(
                task_id=task.task_id,
                source_class=_first_source_class(task),
                provider_name=provider_name,
                status="REJECTED_BY_POLICY",
                provider_errors=("missing_target_scoped_llm_query_intent",),
                budget_used={"queries": 0, "candidates": 0, "fetches": 0, "fetch_attempts": 0},
                stop_reason="live_web_task_rejected_without_target_scoped_llm_query",
                web_search_tasks=tuple(web_task_rows),
                web_search_results=tuple(web_result_rows),
                web_fetched_documents=tuple(web_fetched_rows),
                web_rejected_documents=tuple(web_rejected_rows),
            )

        max_queries = max(1, int(task.max_queries))
        max_candidates = max(1, int(task.max_candidates))
        max_fetches = max(1, int(task.max_fetches))
        for query in query_plan.accepted[:max_queries]:
            if search_result_count >= max_candidates or fetch_attempt_count >= max_fetches or len(documents) >= max_fetches:
                break
            web_task_id = _web_task_id(task=task, event=event, query=query, provider_name=provider_name)
            task_result_rows: list[dict[str, Any]] = []
            task_rejected_count = 0
            task_fetched_count = 0
            executed_query_count += 1
            try:
                results = _rank_web_search_results_for_fetch(
                    results=provider.search(query, as_of_date=as_of_date, max_results=max(1, max_candidates - search_result_count)),
                    event=event,
                )
            except Exception as exc:  # pragma: no cover - defensive provider boundary
                reason = f"web_search_provider_failed:{type(exc).__name__}:{exc}"
                provider_errors.append(reason)
                web_task_rows.append(
                    _web_task_row(
                        task=task,
                        event=event,
                        provider_name=provider_name,
                        as_of_date=as_of_date,
                        query=query,
                        status="PROVIDER_FAILED",
                        rejection_reason=reason,
                        result_count=0,
                        fetched_document_count=0,
                        rejected_document_count=1,
                    )
                )
                web_rejected_rows.append(
                    _web_rejected_row(
                        task=task,
                        event=event,
                        provider_name=provider_name,
                        as_of_date=as_of_date,
                        query=query,
                        result=None,
                        reason=reason,
                    )
                )
                continue
            provider_errors.extend(_provider_errors(provider))
            for result in results:
                if search_result_count >= max_candidates:
                    break
                search_result_count += 1
                result_row = _web_result_row(
                    web_task_id=web_task_id,
                    task=task,
                    event=event,
                    provider_name=provider_name,
                    repo_root=self.repo_root,
                    as_of_date=as_of_date,
                    query=query,
                    result=result,
                )
                task_result_rows.append(result_row)
                official_route = _official_detail_route_from_web_result(result)
                verified_issuer_route = _verified_issuer_web_route_from_web_result(
                    event=event,
                    result=result,
                    repo_root=self.repo_root,
                    as_of_date=as_of_date,
                )
                verified_report_route = _verified_report_web_route_from_web_result(result)
                published = _date_or_datetime_from_any(result.published_at)
                if isinstance(published, datetime) and published.date() > as_of_date:
                    result_row["selected_for_fetch"] = False
                    result_row["selection_status"] = "REJECTED_FUTURE_DOCUMENT"
                    result_row["status"] = "REJECTED"
                    task_rejected_count += 1
                    web_rejected_rows.append(
                        _web_rejected_row(
                            task=task,
                            event=event,
                            provider_name=provider_name,
                            as_of_date=as_of_date,
                            query=query,
                            result=result,
                            reason="search_result_published_after_as_of_date",
                            web_result_id=result_row["web_result_id"],
                        )
                    )
                    web_result_rows.append(result_row)
                    continue
                metadata_rejection = _web_search_result_non_evidence_rejection_reason(event=event, result=result)
                if metadata_rejection is not None:
                    result_row["selected_for_fetch"] = False
                    result_row["selection_status"] = "REJECTED_NON_EVIDENCE_RESULT_METADATA"
                    result_row["status"] = "REJECTED"
                    task_rejected_count += 1
                    web_rejected_rows.append(
                        _web_rejected_row(
                            task=task,
                            event=event,
                            provider_name=provider_name,
                            as_of_date=as_of_date,
                            query=query,
                            result=result,
                            reason=metadata_rejection,
                            web_result_id=result_row["web_result_id"],
                        )
                    )
                    web_result_rows.append(result_row)
                    continue
                dedupe_url = _dedupe_web_result_url(result.url)
                if dedupe_url and dedupe_url in fetched_or_attempted_urls:
                    result_row["selected_for_fetch"] = False
                    result_row["selection_status"] = "REJECTED_DUPLICATE_WEB_RESULT"
                    result_row["status"] = "REJECTED"
                    task_rejected_count += 1
                    web_rejected_rows.append(
                        _web_rejected_row(
                            task=task,
                            event=event,
                            provider_name=provider_name,
                            as_of_date=as_of_date,
                            query=query,
                            result=result,
                            reason="duplicate_web_result_url_not_refetched",
                            web_result_id=result_row["web_result_id"],
                        )
                    )
                    web_result_rows.append(result_row)
                    continue
                if len(documents) >= max_fetches or fetch_attempt_count >= max_fetches:
                    result_row["selected_for_fetch"] = False
                    result_row["selection_status"] = "NOT_SELECTED_BUDGET_EXHAUSTED"
                    web_result_rows.append(result_row)
                    continue
                result_row["selected_for_fetch"] = True
                result_row["selection_status"] = "SELECTED_FOR_FETCH"
                if dedupe_url:
                    fetched_or_attempted_urls.add(dedupe_url)
                fetch_attempt_count += 1
                fetch_result = fetcher.fetch(result.url, as_of_date=as_of_date)
                if not fetch_result.ok or not (fetch_result.text or "").strip():
                    if official_route is not None:
                        provider_errors.append("official_detail_resolve_failed")
                    rejection_reason = fetch_result.reason or "web_fetch_empty_or_failed"
                    if official_route is not None:
                        rejection_reason = f"official_detail_resolve_failed:{rejection_reason}"
                        result_row["official_detail_resolution_status"] = "FAILED"
                        result_row["official_detail_resolution_failure_reason"] = rejection_reason
                    task_rejected_count += 1
                    web_rejected_rows.append(
                        _web_rejected_row(
                            task=task,
                            event=event,
                            provider_name=provider_name,
                            as_of_date=as_of_date,
                            query=query,
                            result=result,
                            reason=rejection_reason,
                            web_result_id=result_row["web_result_id"],
                            fetch_result=fetch_result,
                        )
                    )
                    web_result_rows.append(result_row)
                    continue
                text = fetch_result.text or ""
                relevance_rejection = _web_fetch_target_rejection_reason(event=event, result=result, text=text)
                if relevance_rejection is not None:
                    task_rejected_count += 1
                    result_row["selected_for_fetch"] = False
                    result_row["selection_status"] = "REJECTED_TARGET_RELEVANCE_AFTER_FETCH"
                    result_row["status"] = "REJECTED"
                    web_rejected_rows.append(
                        _web_rejected_row(
                            task=task,
                            event=event,
                            provider_name=provider_name,
                            as_of_date=as_of_date,
                            query=query,
                            result=result,
                            reason=relevance_rejection,
                            web_result_id=result_row["web_result_id"],
                            fetch_result=fetch_result,
                        )
                    )
                    web_result_rows.append(result_row)
                    continue
                content_rejection = _web_fetch_non_evidence_content_rejection_reason(event=event, result=result, text=text)
                if content_rejection is not None:
                    task_rejected_count += 1
                    result_row["selected_for_fetch"] = False
                    result_row["selection_status"] = "REJECTED_NON_EVIDENCE_CONTENT_AFTER_FETCH"
                    result_row["status"] = "REJECTED"
                    web_rejected_rows.append(
                        _web_rejected_row(
                            task=task,
                            event=event,
                            provider_name=provider_name,
                            as_of_date=as_of_date,
                            query=query,
                            result=result,
                            reason=content_rejection,
                            web_result_id=result_row["web_result_id"],
                            fetch_result=fetch_result,
                        )
                    )
                    web_result_rows.append(result_row)
                    continue
                if official_route is not None:
                    result_row["official_detail_resolution_status"] = "RESOLVED"
                if verified_issuer_route is not None:
                    result_row["verified_issuer_original_status"] = "RESOLVED"
                document = EvidenceDocument.from_text(
                    text=text,
                    canonical_url=result.url,
                    source_type=_web_source_type(result, verified_issuer_route=verified_issuer_route),
                    source_name=(
                        official_route.provider_name
                        if official_route is not None
                        else verified_issuer_route.provider_name
                        if verified_issuer_route is not None
                        else verified_report_route.provider_name
                        if verified_report_route is not None
                        else (result.source or provider_name)
                    ),
                    published_at=published or as_of_date,
                    available_at=published or as_of_date,
                    fetched_at=fetch_result.fetched_at or as_of_date,
                    revision_id=_hash_text(text),
                    parser_version="research_brain_v4_live_web_fetch",
                    source_lineage_id=(
                        f"{provider_name}:{result_row['web_result_id']}:official:{official_route.official_document_id}"
                        if official_route is not None
                        else f"{provider_name}:{result_row['web_result_id']}:verified_issuer_original:{verified_issuer_route.official_document_id}"
                        if verified_issuer_route is not None
                        else f"{provider_name}:{result_row['web_result_id']}:verified_report_original:{verified_report_route.official_document_id}"
                        if verified_report_route is not None
                        else f"{provider_name}:{result_row['web_result_id']}"
                    ),
                    source_proxy_only=False,
                )
                anchor = EvidenceAnchor.text_span(document=document, document_text=text, exact_text=_best_quote(text))
                documents.append(document)
                anchors.append(anchor)
                text_by_id[document.document_id] = text
                task_fetched_count += 1
                web_fetched_rows.append(
                    _web_fetched_row(
                        task=task,
                        event=event,
                        provider_name=provider_name,
                        as_of_date=as_of_date,
                        query=query,
                        result=result,
                        result_row=result_row,
                        fetch_result=fetch_result,
                        document=document,
                        anchor=anchor,
                    )
                )
                web_result_rows.append(result_row)
            web_task_rows.append(
                _web_task_row(
                    task=task,
                    event=event,
                    provider_name=provider_name,
                    as_of_date=as_of_date,
                    query=query,
                    status="SEARCH_EXECUTED",
                    rejection_reason=None,
                    result_count=len(task_result_rows),
                    fetched_document_count=task_fetched_count,
                    rejected_document_count=task_rejected_count,
                    web_task_id=web_task_id,
                )
            )

        status = "PARSED" if documents else ("PROVIDER_FAILED" if provider_errors or web_rejected_rows else "NO_EVIDENCE_FOUND")
        stop_reason = "live_web_source_parsed" if documents else "live_web_no_fetchable_document"
        effective_source_class = _effective_source_class_for_documents(task=task, documents=tuple(documents))
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class=effective_source_class,
            provider_name=provider_name,
            status=status,
            documents=tuple(documents),
            anchors=tuple(anchors),
            document_text_by_id=text_by_id,
            fetched_document_ids=tuple(document.document_id for document in documents),
            document_urls=tuple(document.canonical_url or "" for document in documents),
            document_hashes=tuple(document.content_hash for document in documents),
            anchor_ids=tuple(anchor.anchor_id for anchor in anchors),
            provider_errors=tuple(dict.fromkeys(provider_errors)),
            budget_used={
                "queries": executed_query_count,
                "candidates": search_result_count,
                "fetches": len(documents),
                "fetch_attempts": fetch_attempt_count,
            },
            stop_reason=stop_reason,
            web_search_tasks=tuple(web_task_rows),
            web_search_results=tuple(web_result_rows),
            web_fetched_documents=tuple(web_fetched_rows),
            web_rejected_documents=tuple(web_rejected_rows),
        )

    def _candidate_snapshots(
        self,
        *,
        event: CandidateEventV2,
        task: SourceTask,
        as_of_date: date,
    ) -> Iterable[StoredSourceSnapshot]:
        source_classes = tuple(dict.fromkeys((*task.preferred_source_classes, *task.fallback_source_classes)))
        for source_class in source_classes:
            normalized = _normalize_source_class(source_class)
            if normalized == "CompanyGuide":
                yield from _company_guide_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized == "DART":
                yield from _dart_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized in {"KIND", "KRX"}:
                if normalized == "KIND":
                    yield from _kind_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
                else:
                    yield from _krx_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized in {"IR", "IssuerOfficial", "Official"}:
                yield from _issuer_official_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized in {"TrustedNews", "News"}:
                yield from _trusted_news_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized in {"ReportPDF", "BrokerReportPublicPDF"}:
                yield from _report_pdf_snapshots(self.repo_root, event=event, as_of_date=as_of_date)
            elif normalized == "ReplaySourceSnapshot":
                yield from _replay_source_snapshots(self.repo_root, event=event, task=task, as_of_date=as_of_date)


def _company_guide_snapshots(
    repo_root: Path,
    *,
    event: CandidateEventV2,
    as_of_date: date,
) -> Iterable[StoredSourceSnapshot]:
    cache_root = repo_root / "data/cache/company_guide"
    for recent_path in sorted(cache_root.glob(f"*/{event.symbol}_recent_reports.json"), reverse=True):
        payload = _load_json(recent_path)
        if not isinstance(payload, Mapping):
            continue
        for row in payload.get("lists") or ():
            if not isinstance(row, Mapping):
                continue
            row_date = _yy_mm_dd_date(row.get("ANL_DT"), as_of_date)
            if row_date is None or row_date > as_of_date:
                continue
            comment = _strip_html(str(row.get("COMMENT") or row.get("COMMENT2") or ""))
            title = str(row.get("RPT_TITLE") or "")
            company = str(row.get("CMP_NM_KOR") or event.company_name)
            text = "\n".join(
                item
                for item in (
                    f"CompanyGuide report {row.get('RPT_ID')} {row_date.isoformat()}",
                    f"{company}({event.symbol})",
                    title,
                    comment,
                    f"EPS_ACTION_TYP_NM={row.get('EPS_ACTION_TYP_NM')}",
                    f"PRC_ACTION_TYP_NM={row.get('PRC_ACTION_TYP_NM')}",
                    f"TARGET_PRC={row.get('TARGET_PRC')}",
                    f"EPS={row.get('EPS')}",
                    f"BROKER={row.get('BRK_NM_KOR') or row.get('BRK_NM_SHORT_KOR')}",
                )
                if str(item).strip()
            )
            yield StoredSourceSnapshot(
                source_class="CompanyGuide",
                provider_name="CompanyGuideRecentReportsSnapshot",
                source_path=recent_path,
                symbol=event.symbol,
                company_name=company,
                published_at=row_date,
                text=text,
                canonical_url=f"snapshot://company_guide/{recent_path.parent.name}/{event.symbol}/recent_reports#{row.get('RPT_ID')}",
                anchor_type=AnchorType.API_RECORD,
                normalized_value={
                    "symbol": event.symbol,
                    "company_name": company,
                    "provider": "CompanyGuide",
                    "row": dict(row),
                    "snapshot_path": str(recent_path),
                },
            )
    for snapshot_path in sorted(cache_root.glob(f"*/{event.symbol}_snapshot.html"), reverse=True):
        text = snapshot_path.read_text(encoding="utf-8", errors="ignore")
        published = _snapshot_date_from_text(text) or _date_from_path(snapshot_path) or as_of_date
        if published > as_of_date:
            continue
        yield StoredSourceSnapshot(
            source_class="CompanyGuide",
            provider_name="CompanyGuideSnapshotHtml",
            source_path=snapshot_path,
            symbol=event.symbol,
            company_name=event.company_name,
            published_at=published,
            text=text[:80_000],
            canonical_url=f"snapshot://company_guide/{snapshot_path.parent.name}/{event.symbol}/snapshot",
            anchor_type=AnchorType.TEXT_SPAN,
            normalized_value={
                "symbol": event.symbol,
                "company_name": event.company_name,
                "provider": "CompanyGuide",
                "snapshot_path": str(snapshot_path),
            },
        )


def _dart_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    paths = (
        *(repo_root / "fixtures/historical").glob("disclosures.csv"),
        *(repo_root / "data/raw/opendart/disclosures").glob("*.csv"),
        *(repo_root / "data/raw/korea_cheap_scan/opendart/disclosures").glob("*.csv"),
    )
    for path in sorted(paths):
        for row in _csv_rows(path):
            if str(row.get("symbol") or "") != event.symbol:
                continue
            published = _date_from_any(row.get("published_at") or row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            raw_text = str(row.get("raw_text") or row.get("title") or "")
            text = _row_text("OpenDART", row, raw_text=raw_text, symbol=event.symbol, company_name=event.company_name)
            yield StoredSourceSnapshot(
                source_class="DART",
                provider_name="OpenDARTStoredDisclosure",
                source_path=path,
                symbol=event.symbol,
                company_name=event.company_name,
                published_at=published,
                text=text,
                canonical_url=f"snapshot://opendart/{event.symbol}/{row.get('rcept_no') or path.name}",
                anchor_type=AnchorType.API_RECORD,
                normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "OpenDART", "row": dict(row)},
            )


def _kind_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    paths = (
        *(repo_root / "data/raw/kind/risk_flags").glob("*.csv"),
        *(repo_root / "data/raw/korea_cheap_scan/kind/risk_flags").glob("*.csv"),
    )
    for path in sorted(paths):
        for row in _csv_rows(path):
            if str(row.get("symbol") or "") != event.symbol:
                continue
            published = _date_from_any(row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            text = _row_text("KIND", row, raw_text=str(row.get("title") or ""), symbol=event.symbol, company_name=event.company_name)
            yield StoredSourceSnapshot(
                source_class="KIND",
                provider_name="KINDStoredRiskFlags",
                source_path=path,
                symbol=event.symbol,
                company_name=str(row.get("company_name") or event.company_name),
                published_at=published,
                text=text,
                canonical_url=f"snapshot://kind/{event.symbol}/{published.isoformat()}",
                anchor_type=AnchorType.API_RECORD,
                normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "KIND", "row": dict(row)},
            )


def _krx_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    instrument_paths = (
        *(repo_root / "data/raw/krx/instruments").glob("*.csv"),
        *(repo_root / "data/raw/korea_cheap_scan/krx/instruments").glob("*.csv"),
        repo_root / "fixtures/historical/instruments.csv",
    )
    for path in sorted(path for path in instrument_paths if path.exists()):
        for row in _csv_rows(path):
            if str(row.get("symbol") or "") != event.symbol:
                continue
            listed = _date_from_any(row.get("listed_date")) or as_of_date
            if listed > as_of_date:
                continue
            text = _row_text("KRX", row, raw_text=str(row.get("name") or event.company_name), symbol=event.symbol, company_name=event.company_name)
            yield StoredSourceSnapshot(
                source_class="KRX",
                provider_name="KRXStoredInstrumentStatus",
                source_path=path,
                symbol=event.symbol,
                company_name=str(row.get("name") or event.company_name),
                published_at=as_of_date,
                text=text,
                canonical_url=f"snapshot://krx/instruments/{path.name}#{event.symbol}",
                anchor_type=AnchorType.API_RECORD,
                normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "KRX", "row": dict(row)},
            )
    price_paths = (
        *(repo_root / "data/raw/krx/prices").glob("*.csv"),
        *(repo_root / "data/raw/korea_cheap_scan/krx/prices").glob("*.csv"),
        repo_root / "fixtures/historical/prices.csv",
    )
    for path in sorted(path for path in price_paths if path.exists()):
        latest: Mapping[str, Any] | None = None
        latest_date: date | None = None
        for row in _csv_rows(path):
            if str(row.get("symbol") or "") != event.symbol:
                continue
            row_date = _date_from_any(row.get("date") or row.get("as_of_date")) or as_of_date
            if row_date > as_of_date:
                continue
            if latest_date is None or row_date > latest_date:
                latest = row
                latest_date = row_date
        if latest is None or latest_date is None:
            continue
        text = _row_text("KRX price", latest, raw_text=f"{event.company_name} KRX trading status", symbol=event.symbol, company_name=event.company_name)
        yield StoredSourceSnapshot(
            source_class="KRX",
            provider_name="KRXStoredPriceStatus",
            source_path=path,
            symbol=event.symbol,
            company_name=event.company_name,
            published_at=latest_date,
            text=text,
            canonical_url=f"snapshot://krx/prices/{path.name}#{latest_date.isoformat()}",
            anchor_type=AnchorType.API_RECORD,
            normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "KRX", "row": dict(latest)},
        )


def _issuer_official_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    text_root = repo_root / "data/raw/search_html/text"
    symbol_or_name = _safe_slug(event.company_name)
    for path in sorted(text_root.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if event.symbol not in text and event.company_name not in text and symbol_or_name not in path.stem:
            continue
        yield StoredSourceSnapshot(
            source_class="IR",
            provider_name="StoredIssuerOfficialOrReportSnapshot",
            source_path=path,
            symbol=event.symbol,
            company_name=event.company_name,
            published_at=as_of_date,
            text=text,
            canonical_url=f"snapshot://issuer_official/{path.name}",
            anchor_type=AnchorType.TEXT_SPAN,
            normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "IssuerOfficial", "snapshot_path": str(path)},
        )


def _trusted_news_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    for path in (repo_root / "fixtures/historical/news.json", repo_root / "data/raw/naver_news/news/news.json"):
        payload = _load_json(path)
        rows = payload if isinstance(payload, Sequence) and not isinstance(payload, (str, bytes, bytearray)) else []
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            text = " ".join(str(row.get(key) or "") for key in ("title", "snippet", "raw_text", "description"))
            if event.symbol not in text and event.company_name not in text:
                continue
            published = _date_from_any(row.get("publish_date") or row.get("published_at") or row.get("date")) or as_of_date
            if published > as_of_date:
                continue
            yield StoredSourceSnapshot(
                source_class="TrustedNews",
                provider_name="StoredTrustedNewsSnapshot",
                source_path=path,
                symbol=event.symbol,
                company_name=event.company_name,
                published_at=published,
                text=text,
                canonical_url=str(row.get("url") or f"snapshot://trusted_news/{event.symbol}/{published.isoformat()}"),
                anchor_type=AnchorType.TEXT_SPAN,
                normalized_value={"symbol": event.symbol, "company_name": event.company_name, "provider": "TrustedNews", "row": dict(row)},
            )


def _report_pdf_snapshots(repo_root: Path, *, event: CandidateEventV2, as_of_date: date) -> Iterable[StoredSourceSnapshot]:
    manifest_path = repo_root / "data/report_snapshots/report_snapshots.jsonl"
    if not manifest_path.exists():
        return
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(row, Mapping):
            continue
        if str(row.get("symbol") or "").zfill(6) != event.symbol:
            continue
        source_type = str(row.get("source_type") or "").strip().lower()
        if source_type not in {"broker_report", "report_pdf", "research_report"}:
            continue
        report_url = str(row.get("url") or "").strip()
        if not is_verified_report_original_url(report_url, title=str(row.get("title") or "")):
            continue
        published = _date_from_any(row.get("as_of_date") or row.get("fetched_at")) or as_of_date
        if published > as_of_date:
            continue
        text_path = repo_root / "data/report_snapshots" / str(row.get("extracted_text_path") or "")
        if not text_path.exists():
            continue
        text = text_path.read_text(encoding="utf-8", errors="ignore")
        if event.symbol not in text and event.company_name not in text:
            text = f"{event.company_name}({event.symbol})\n{text}"
        yield StoredSourceSnapshot(
            source_class="BrokerReportPublicPDF",
            provider_name="StoredBrokerReportSnapshot",
            source_path=text_path,
            symbol=event.symbol,
            company_name=str(row.get("company_name") or event.company_name),
            published_at=published,
            text=text[:80_000],
            canonical_url=report_url,
            anchor_type=AnchorType.TEXT_SPAN,
            normalized_value={
                "symbol": event.symbol,
                "company_name": str(row.get("company_name") or event.company_name),
                "provider": "BrokerReportPublicPDF",
                "row": dict(row),
                "snapshot_path": str(text_path),
            },
        )


def _replay_source_snapshots(
    repo_root: Path,
    *,
    event: CandidateEventV2,
    task: SourceTask,
    as_of_date: date,
) -> Iterable[StoredSourceSnapshot]:
    manifest_path = repo_root / "data/replay_source_snapshots/replay_source_snapshots.jsonl"
    if not manifest_path.exists():
        return
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(row, Mapping):
            continue
        if str(row.get("symbol") or "").zfill(6) != event.symbol:
            continue
        if row.get("source_task_id") and str(row.get("source_task_id")) != task.task_id:
            continue
        if row.get("candidate_event_id") and str(row.get("candidate_event_id")) != event.candidate_event_id:
            continue
        if row.get("archetype_id") and str(row.get("archetype_id")) != str(task.archetype_id):
            continue
        if row.get("primitive_gap") and str(row.get("primitive_gap")) != str(task.primitive_gap):
            continue
        published = _date_from_any(row.get("as_of_date") or row.get("published_at") or row.get("fetched_at")) or as_of_date
        if published > as_of_date:
            continue
        text_path = repo_root / "data/replay_source_snapshots" / str(row.get("extracted_text_path") or "")
        if not text_path.exists():
            continue
        text = text_path.read_text(encoding="utf-8", errors="ignore")
        if event.symbol not in text and event.company_name not in text:
            text = f"{event.company_name}({event.symbol})\n{text}"
        yield StoredSourceSnapshot(
            source_class="ReplaySourceSnapshot",
            provider_name="StoredReplaySourceSnapshot",
            source_path=text_path,
            symbol=event.symbol,
            company_name=str(row.get("company_name") or event.company_name),
            published_at=published,
            text=text[:80_000],
            canonical_url=str(row.get("url") or f"snapshot://replay_source/{event.symbol}/{published.isoformat()}"),
            anchor_type=AnchorType.TEXT_SPAN,
            normalized_value={
                "symbol": event.symbol,
                "company_name": str(row.get("company_name") or event.company_name),
                "provider": "ReplaySourceSnapshot",
                "row": dict(row),
                "snapshot_path": str(text_path),
            },
        )


def _merge_live_official_and_web_results(
    *,
    live_result: SourceAcquisitionResultV4,
    web_result: SourceAcquisitionResultV4,
) -> SourceAcquisitionResultV4:
    documents = (*live_result.documents, *web_result.documents)
    anchors = (*live_result.anchors, *web_result.anchors)
    text_by_id = {**dict(live_result.document_text_by_id), **dict(web_result.document_text_by_id)}
    provider_errors = tuple(dict.fromkeys((*live_result.provider_errors, *web_result.provider_errors)))
    budget_used = {
        key: int(live_result.budget_used.get(key, 0) or 0) + int(web_result.budget_used.get(key, 0) or 0)
        for key in set(live_result.budget_used) | set(web_result.budget_used)
    }
    if documents:
        status = "PARSED"
    elif web_result.status == "REJECTED_BY_POLICY":
        status = "REJECTED_BY_POLICY"
    elif live_result.status == "REJECTED_BY_POLICY":
        status = "REJECTED_BY_POLICY"
    else:
        status = "PROVIDER_FAILED" if provider_errors else "NO_EVIDENCE_FOUND"
    if live_result.status == "PARSED" and web_result.status == "PARSED":
        stop_reason = "live_official_and_web_sources_parsed"
    elif live_result.status == "PARSED":
        stop_reason = f"live_official_parsed_web_{web_result.status.lower()}"
    elif web_result.status == "PARSED":
        stop_reason = f"live_web_parsed_official_{live_result.status.lower()}"
    else:
        stop_reason = f"live_official_{live_result.status.lower()}_web_{web_result.status.lower()}"
    source_class = live_result.source_class
    if web_result.documents and not live_result.documents:
        source_class = web_result.source_class
    return SourceAcquisitionResultV4(
        task_id=live_result.task_id,
        source_class=source_class,
        provider_name=f"{live_result.provider_name}+{web_result.provider_name}",
        status=status,
        documents=documents,
        anchors=anchors,
        document_text_by_id=text_by_id,
        fetched_document_ids=(*live_result.fetched_document_ids, *web_result.fetched_document_ids),
        document_urls=(*live_result.document_urls, *web_result.document_urls),
        document_hashes=(*live_result.document_hashes, *web_result.document_hashes),
        anchor_ids=(*live_result.anchor_ids, *web_result.anchor_ids),
        provider_errors=provider_errors,
        budget_used=budget_used,
        stop_reason=stop_reason,
        web_search_tasks=web_result.web_search_tasks,
        web_search_results=web_result.web_search_results,
        web_fetched_documents=web_result.web_fetched_documents,
        web_rejected_documents=web_result.web_rejected_documents,
    )


def _remaining_web_task_after_live_result(
    *,
    task: SourceTask,
    live_result: SourceAcquisitionResultV4,
) -> SourceTask | None:
    """Return a web fallback task constrained by the original task-wide budget."""

    budget = live_result.budget_used or {}

    def remaining(limit_name: str, *used_names: str) -> int:
        limit = int(getattr(task, limit_name))
        used = sum(int(budget.get(name, 0) or 0) for name in used_names)
        return max(0, limit - used)

    remaining_queries = remaining("max_queries", "queries")
    remaining_candidates = remaining("max_candidates", "candidates")
    remaining_fetches = remaining("max_fetches", "fetches", "fetch_attempts")
    if remaining_queries <= 0 or remaining_candidates <= 0 or remaining_fetches <= 0:
        return None
    return replace(
        task,
        max_queries=remaining_queries,
        max_candidates=remaining_candidates,
        max_fetches=remaining_fetches,
    )


def _anchor_for_snapshot(*, document: EvidenceDocument, snapshot: StoredSourceSnapshot) -> EvidenceAnchor:
    if snapshot.anchor_type != AnchorType.TEXT_SPAN:
        return EvidenceAnchor.structured(
            document=document,
            anchor_type=snapshot.anchor_type,
            locator=f"record:{snapshot.source_class}:{snapshot.symbol}",
            normalized_value=snapshot.normalized_value,
            exact_text=snapshot.text[:500],
            anchor_verified=True,
        )
    quote = _best_quote(snapshot.text)
    return EvidenceAnchor.text_span(document=document, document_text=snapshot.text, exact_text=quote)


def _policy_rejection(task: SourceTask) -> tuple[str, ...]:
    reasons: list[str] = []
    for field_name in ("max_queries", "max_candidates", "max_fetches"):
        value = getattr(task, field_name)
        if value is None or int(value) <= 0:
            reasons.append(f"unbounded_or_invalid_{field_name}")
    if "unbounded_general_search" not in tuple(task.forbidden_source_classes):
        reasons.append("missing_unbounded_general_search_guard")
    if _is_official_solvable_gap(task.primitive_gap) and (
        task.general_search_allowed
        or _task_requests_general_web_or_news(task)
        or (_task_requests_external_web(task) and not _allows_bounded_report_fallback_for_official_gap(task.primitive_gap))
    ):
        reasons.append("official_solvable_gap_sent_to_general_web")
    if _is_fcf_gap(task.primitive_gap):
        source_names = {_normalize_source_class(item).lower() for item in (*task.preferred_source_classes, *task.fallback_source_classes)}
        if source_names & {"generalwebsearch", "naversearch", "web", "trustednews", "newsonly", "news"}:
            reasons.append("fcf_gap_sent_to_news_or_general_web")
    return tuple(dict.fromkeys(reasons))


def _first_source_class(task: SourceTask) -> str:
    return _normalize_source_class((task.preferred_source_classes or task.fallback_source_classes or ("unknown",))[0])


def _effective_source_class_for_documents(*, task: SourceTask, documents: Sequence[EvidenceDocument]) -> str:
    requested = tuple(
        dict.fromkeys(_normalize_source_class(item) for item in (*task.preferred_source_classes, *task.fallback_source_classes))
    )
    for document in documents:
        actual = _source_class_from_document_url(document)
        if actual:
            return actual
    document_types = {_document_source_type(document) for document in documents}
    if SourceType.NEWS in document_types:
        for source_class in ("IndustryMedia", "CompanyNewsroom", "TrustedNews", "News", "NaverSearch"):
            if source_class in requested:
                return source_class
    if SourceType.RESEARCH_REPORT in document_types:
        for source_class in ("BrokerReportPublicPDF", "ReportPDF"):
            if source_class in requested:
                return source_class
    if SourceType.IR in document_types:
        for source_class in ("CompanyNewsroom", "IR", "IssuerOfficial"):
            if source_class in requested:
                return source_class
    return _first_source_class(task)


def _source_class_from_document_url(document: EvidenceDocument) -> str | None:
    if _document_has_verified_issuer_original_lineage(document):
        if _document_source_type(document) in {SourceType.NEWS, SourceType.IR}:
            return "CompanyNewsroom"
    if _document_has_verified_report_original_lineage(document):
        if _document_source_type(document) == SourceType.RESEARCH_REPORT:
            return "BrokerReportPublicPDF"
    parsed = urlsplit(str(document.canonical_url or ""))
    host = (parsed.hostname or "").lower()
    if host == "dart.fss.or.kr":
        return "DART"
    if host == "kind.krx.co.kr":
        return "KIND"
    if host in {"data.krx.co.kr", "www.krx.co.kr"}:
        return "KRX"
    if host in {"wcomp.fnguide.com", "comp.fnguide.com"}:
        return "CompanyGuide"
    return None


def _ordered_live_official_connectors(
    *,
    connectors: Sequence[Any],
    requested_classes: Sequence[str],
) -> tuple[Any, ...]:
    """Return live connectors in SourceTask order, not registry construction order."""

    ordered: list[Any] = []
    for requested in requested_classes:
        requested_match = _connector_match_source_class(requested)
        for connector in connectors:
            connector_match = _connector_match_source_class(getattr(connector, "source_class", ""))
            if connector_match != requested_match:
                continue
            if connector in ordered:
                continue
            ordered.append(connector)
    return tuple(ordered)


def _connector_match_source_class(value: str) -> str:
    normalized = _normalize_source_class(value)
    if normalized in {"IssuerIR", "IssuerOfficial", "Official"}:
        return "IR"
    return normalized


def _document_source_type(document: EvidenceDocument) -> SourceType:
    value = document.source_type
    if isinstance(value, SourceType):
        return value
    try:
        return SourceType(str(value))
    except ValueError:
        return SourceType.OTHER


def _normalize_source_class(value: str) -> str:
    clean = str(value).strip()
    lowered = clean.lower()
    aliases = {
        "opendart": "DART",
        "dart": "DART",
        "kind": "KIND",
        "krx": "KRX",
        "companyguide": "CompanyGuide",
        "company_guide": "CompanyGuide",
        "wisereport": "CompanyGuide",
        "ir": "IR",
        "issuerir": "IssuerIR",
        "issuer_ir": "IssuerIR",
        "official": "Official",
        "issuerofficial": "IssuerOfficial",
        "issuer_official": "IssuerOfficial",
        "trustednews": "TrustedNews",
        "trusted_news": "TrustedNews",
        "news": "News",
        "naversearch": "NaverSearch",
        "naver_search": "NaverSearch",
        "generalweb": "GeneralWebSearch",
        "general_web": "GeneralWebSearch",
        "generalwebsearch": "GeneralWebSearch",
        "general_web_search": "GeneralWebSearch",
        "web": "GeneralWebSearch",
        "websearch": "GeneralWebSearch",
        "web_search": "GeneralWebSearch",
        "reportpdf": "ReportPDF",
        "report_pdf": "ReportPDF",
        "brokerreportpublicpdf": "BrokerReportPublicPDF",
        "broker_report_public_pdf": "BrokerReportPublicPDF",
        "broker_report": "BrokerReportPublicPDF",
        "researchreport": "ReportPDF",
        "research_report": "ReportPDF",
        "replaysourcesnapshot": "ReplaySourceSnapshot",
        "replay_source_snapshot": "ReplaySourceSnapshot",
        "replay_snapshot": "ReplaySourceSnapshot",
    }
    return aliases.get(lowered, clean)


def _task_requests_external_web(task: SourceTask) -> bool:
    requested = {_normalize_source_class(item) for item in (*task.preferred_source_classes, *task.fallback_source_classes)}
    return bool(requested & _EXTERNAL_WEB_SOURCE_CLASSES)


_EXTERNAL_WEB_SOURCE_CLASSES = {
        "NaverSearch",
        "GeneralWebSearch",
        "TrustedNews",
        "News",
        "IndustryMedia",
        "CompanyNewsroom",
        "ReportPDF",
        "BrokerReportPublicPDF",
}


def _task_prefers_external_web(task: SourceTask) -> bool:
    """Return true when the planner explicitly made the task an external-source leaf.

    Mixed official-first tasks such as ``DART -> TrustedNews`` must still spend
    official budget first. External-original tasks such as
    ``BrokerReportPublicPDF -> IssuerIR`` should not let fallback official
    connectors consume the only query before the bounded web search can run.
    """

    preferred = tuple(_normalize_source_class(item) for item in task.preferred_source_classes)
    if not preferred:
        return False
    return preferred[0] in _EXTERNAL_WEB_SOURCE_CLASSES


def _task_requests_general_web_or_news(task: SourceTask) -> bool:
    general_or_news = {"NaverSearch", "GeneralWebSearch", "TrustedNews", "News", "IndustryMedia"}
    requested = {_normalize_source_class(item) for item in (*task.preferred_source_classes, *task.fallback_source_classes)}
    return bool(requested & general_or_news)


def _allows_bounded_report_fallback_for_official_gap(primitive: str) -> bool:
    lower = str(primitive or "").lower()
    return lower == "cash_or_revision_conversion" or "revision" in lower


def _target_scoped_web_queries(*, task: SourceTask, event: CandidateEventV2) -> _TargetScopedQueryPlan:
    accepted: list[str] = []
    rejected: list[tuple[str, str]] = []
    for raw_query in tuple(task.query_intents or ()):
        query = re.sub(r"\s+", " ", str(raw_query or "")).strip()
        if not query:
            continue
        if query in accepted:
            rejected.append((query, "duplicate_llm_query_intent"))
            continue
        if not _query_mentions_target(query=query, event=event):
            rejected.append((query, "web_query_not_target_scoped"))
            continue
        accepted.append(query)
        if len(accepted) >= int(task.max_queries):
            break
    if not accepted and not rejected:
        rejected.append(("", "missing_llm_query_intent_for_external_web_task"))
    return _TargetScopedQueryPlan(accepted=tuple(accepted), rejected=tuple(rejected))


def _query_mentions_target(*, query: str, event: CandidateEventV2) -> bool:
    compact_query = re.sub(r"\s+", "", query).lower()
    company = re.sub(r"\s+", "", str(event.company_name or "")).lower()
    symbol = str(event.symbol or "").zfill(6)
    return bool(company and company in compact_query) or bool(symbol and symbol in query)


def _web_fetch_target_rejection_reason(
    *,
    event: CandidateEventV2,
    result: SearchResult,
    text: str,
) -> str | None:
    aliases = _target_aliases_for_web_relevance(event, result=result)
    if not aliases:
        return "web_fetch_target_alias_missing"
    body = str(text or "")
    if not _text_mentions_any_target_alias(body, aliases):
        return "web_fetch_target_not_found_in_full_text"
    lead_text = body[:6000]
    if _text_mentions_any_target_alias(lead_text, aliases):
        return None
    return "web_fetch_target_not_in_title_snippet_or_lead"


def _rank_web_search_results_for_fetch(*, results: Sequence[SearchResult], event: CandidateEventV2) -> tuple[SearchResult, ...]:
    return tuple(
        sorted(
            results,
            key=lambda result: (
                _web_result_evidence_priority(event=event, result=result),
                int(result.rank or 9999),
                result.url,
            ),
        )
    )


def _web_result_evidence_priority(*, event: CandidateEventV2, result: SearchResult) -> int:
    priority = int(result.rank or 9999)
    if _web_search_result_non_evidence_rejection_reason(event=event, result=result) is not None:
        priority += 10_000
    title = str(result.title or "")
    snippet = str(result.snippet or "")
    aliases = _target_aliases_for_web_relevance(event, result=result)
    if _text_mentions_any_target_alias(title, aliases):
        priority -= 300
    elif _text_mentions_any_target_alias(f"{title}\n{snippet}", aliases):
        priority -= 80
    if result.is_disclosure:
        priority -= 250
    if result.is_report_domain or result.is_pdf:
        priority -= 220
    if result.is_news:
        priority -= 160
    if _looks_like_market_digest_or_disclosure_roundup_page(event=event, url=result.url, title=title, snippet=snippet, text=""):
        priority += 600
    return priority


def _web_fetch_non_evidence_content_rejection_reason(*, event: CandidateEventV2, result: SearchResult, text: str) -> str | None:
    if _looks_like_stock_quote_or_profile_page(url=result.url, text=text):
        return "web_fetch_stock_quote_or_profile_page_not_source_document"
    if _looks_like_stock_list_or_channel_page(url=result.url, title=result.title, snippet=result.snippet, text=text):
        return "web_fetch_stock_list_or_channel_page_not_source_document"
    if _looks_like_low_quality_blog_or_social_page(url=result.url, title=result.title, snippet=result.snippet, text=text):
        return "web_fetch_low_quality_blog_or_social_not_score_source"
    if _looks_like_market_digest_or_disclosure_roundup_page(
        event=event,
        url=result.url,
        title=result.title,
        snippet=result.snippet,
        text=text,
    ):
        return "web_fetch_market_digest_or_disclosure_roundup_not_source_document"
    if _looks_like_site_archive_or_sitemap_page(url=result.url, title=result.title, snippet=result.snippet, text=text):
        return "web_fetch_site_archive_or_sitemap_not_source_document"
    return None


def _web_search_result_non_evidence_rejection_reason(*, event: CandidateEventV2, result: SearchResult) -> str | None:
    if _looks_like_stock_quote_or_profile_page(url=result.url, text=f"{result.title}\n{result.snippet or ''}"):
        return "web_result_stock_quote_or_profile_page_not_source_document"
    if _looks_like_stock_list_or_channel_page(url=result.url, title=result.title, snippet=result.snippet, text=""):
        return "web_result_stock_list_or_channel_page_not_source_document"
    if _looks_like_generic_market_or_stock_profile_page(event=event, url=result.url, title=result.title, snippet=result.snippet, text=""):
        return "web_result_market_or_stock_profile_page_not_source_document"
    if _looks_like_low_quality_blog_or_social_page(url=result.url, title=result.title, snippet=result.snippet, text=""):
        return "web_result_low_quality_blog_or_social_not_score_source"
    if _looks_like_market_digest_or_disclosure_roundup_page(
        event=event,
        url=result.url,
        title=result.title,
        snippet=result.snippet,
        text="",
    ):
        return "web_result_market_digest_or_disclosure_roundup_not_source_document"
    if _looks_like_site_archive_or_sitemap_page(url=result.url, title=result.title, snippet=result.snippet, text=""):
        return "web_result_site_archive_or_sitemap_not_source_document"
    return None


def _looks_like_stock_quote_or_profile_page(*, url: str, text: str) -> bool:
    lowered_url = str(url or "").lower()
    compact_text = re.sub(r"\s+", "", str(text or "")).lower()
    if "finance.naver.com/item/" in lowered_url:
        return True
    if "m.stock.naver.com" in lowered_url or "m.stock.naver.com/domestic/stock" in lowered_url:
        return True
    if "investing.com/equities/" in lowered_url:
        return True
    naver_stock_tokens = (
        "npay증권",
        "네이버페이증권",
        "종목시세정보",
        "증권종목명·지수명검색",
    )
    quote_board_tokens = ("현재가", "전일대비", "거래량", "시가", "고가", "저가")
    return any(token in compact_text for token in naver_stock_tokens) and sum(
        1 for token in quote_board_tokens if token in compact_text
    ) >= 3


def _looks_like_stock_list_or_channel_page(*, url: str, title: str, snippet: str | None, text: str) -> bool:
    lowered_url = str(url or "").lower()
    compact = re.sub(r"\s+", "", "\n".join(str(item or "") for item in (title, snippet, text))).lower()
    if "/tag/" in lowered_url or "%ed%83%9c%ea%b7%b8" in lowered_url:
        return True
    if lowered_url.startswith(("https://t.me/", "http://t.me/", "https://telegram.me/", "http://telegram.me/")):
        return True
    if "blog.kakaocdn.net" in lowered_url and any(token in lowered_url for token in (".xlsx", ".xls", ".csv")):
        return True
    list_tokens = (
        "상승률top30",
        "상승률top",
        "오늘의상승률",
        "상한가급등주정리",
        "시간외특징주",
        "태그의글목록",
        "기사제목으로알아보는오늘의증권시장",
        "주식공시정리채널",
    )
    return any(token in compact for token in list_tokens)


def _looks_like_low_quality_blog_or_social_page(*, url: str, title: str, snippet: str | None, text: str) -> bool:
    lowered_url = str(url or "").lower()
    compact = re.sub(r"\s+", "", "\n".join(str(item or "") for item in (title, snippet, text))).lower()
    if _official_detail_route_from_url(url) is not None:
        return False
    low_quality_domain_tokens = (
        "tistory.com",
        "blogspot.",
        "brunch.co.kr",
        "blog.naver.com",
        "post.naver.com",
        "cafe.naver.com",
        "t.me/",
        "telegram.me/",
        "dcinside.com",
        "fmkorea.com",
        "instiz.net",
        "theqoo.net",
    )
    if any(token in lowered_url for token in low_quality_domain_tokens):
        return True
    low_quality_content_tokens = (
        "개인블로그",
        "투자아이디어",
        "관심종목",
        "급등주",
        "상한가",
        "특징주정리",
        "주식리딩",
        "텔레그램방",
        "카카오톡방",
    )
    return any(token in compact for token in low_quality_content_tokens)


def _looks_like_market_digest_or_disclosure_roundup_page(
    *,
    event: CandidateEventV2,
    url: str,
    title: str,
    snippet: str | None,
    text: str,
) -> bool:
    lowered_url = str(url or "").lower()
    title_text = str(title or "")
    compact = re.sub(r"\s+", "", "\n".join(str(item or "") for item in (title, snippet, text))).lower()
    roundup_tokens = (
        "주요공시",
        "주요공시모음",
        "오늘의공시",
        "공시뽑기",
        "공시정리",
        "증시공시",
        "상장사공시",
        "기업공시",
        "장마감후주요공시",
        "시간외공시",
    )
    if not any(token in compact for token in roundup_tokens):
        return False
    if _text_mentions_any_target_alias(title_text, _target_aliases_for_web_relevance(event)):
        return False
    issuer_source_tokens = ("dart.fss.or.kr", "kind.krx.co.kr", "company", "ir")
    if any(token in lowered_url for token in issuer_source_tokens):
        return False
    return True


def _looks_like_generic_market_or_stock_profile_page(
    *,
    event: CandidateEventV2,
    url: str,
    title: str,
    snippet: str | None,
    text: str,
) -> bool:
    lowered_url = str(url or "").lower()
    compact = re.sub(r"\s+", "", "\n".join(str(item or "") for item in (title, snippet, text))).lower()
    aliases = _target_aliases_for_web_relevance(event)
    title_snippet = "\n".join(str(item or "") for item in (title, snippet))
    if _text_mentions_any_target_alias(title_snippet, aliases):
        return False
    if "investing.com/news/stock-market-news/" in lowered_url:
        return True
    if "investing.com/equities/" in lowered_url:
        return True
    generic_market_tokens = (
        "개장체크",
        "증시",
        "3대지수",
        "fomc",
        "국채금리",
        "연준",
        "stock-market-news",
        "stockmarketnews",
        "marketnews",
    )
    stock_profile_tokens = (
        "오늘의주가",
        "실시간티커",
        "주식뉴스(",
        "주식뉴스",
        "stockprice",
        "stocknews",
    )
    return any(token in compact for token in generic_market_tokens) or any(token in compact for token in stock_profile_tokens)


def _looks_like_site_archive_or_sitemap_page(*, url: str, title: str, snippet: str | None, text: str) -> bool:
    lowered_url = str(url or "").lower()
    compact = re.sub(r"\s+", "", "\n".join(str(item or "") for item in (title, snippet, text))).lower()
    if "/sitemap/" in lowered_url or "sitemap/archive" in lowered_url:
        return True
    archive_tokens = (
        "사이트맵",
        "뉴스아카이브",
        "기사목록",
        "전체기사목록",
        "월별기사",
    )
    return any(token in compact for token in archive_tokens)


def _dedupe_web_result_url(url: str) -> str:
    text = str(url or "").strip()
    if not text:
        return ""
    try:
        parsed = urlsplit(text)
    except ValueError:
        return text.rstrip("/")
    path = parsed.path.rstrip("/") or parsed.path
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, ""))


def _target_aliases_for_web_relevance(event: CandidateEventV2, *, result: SearchResult | None = None) -> tuple[str, ...]:
    aliases = [
        str(event.company_name or "").strip(),
        str(event.symbol or "").strip(),
        str(event.symbol or "").zfill(6),
    ]
    aliases.extend(_source_title_target_aliases_for_web_relevance(event=event, result=result))
    return tuple(dict.fromkeys(alias for alias in aliases if alias))


def _source_title_target_aliases_for_web_relevance(
    *,
    event: CandidateEventV2,
    result: SearchResult | None,
) -> tuple[str, ...]:
    if result is None:
        return ()
    symbol = str(event.symbol or "").zfill(6)
    title = str(result.title or "").strip()
    if not title or not symbol or symbol not in title:
        return ()
    before_symbol = title[: title.find(symbol)]
    before_symbol = re.sub(r"[\[(]\s*$", "", before_symbol).strip()
    segments = [segment.strip(" \t-:|/()[]") for segment in re.split(r"\s[|:–—-]\s", before_symbol) if segment.strip()]
    if not segments:
        return ()
    candidate = segments[-1]
    aliases = [candidate, *_company_alias_without_english_suffix_for_web_relevance(candidate)]
    return tuple(dict.fromkeys(alias for alias in aliases if _looks_like_source_title_company_alias_for_web_relevance(alias)))


def _company_alias_without_english_suffix_for_web_relevance(value: str) -> tuple[str, ...]:
    stripped = re.sub(
        r"\b(?:co|corp|corporation|inc|ltd|limited|plc|sa|ag)\b\.?",
        "",
        str(value or ""),
        flags=re.IGNORECASE,
    )
    stripped = re.sub(r"\s+", " ", stripped).strip(" ,.-")
    return (stripped,) if stripped and stripped != value else ()


def _looks_like_source_title_company_alias_for_web_relevance(value: str) -> bool:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) < 2 or len(text) > 80:
        return False
    if not re.search(r"[A-Za-z]", text):
        return False
    blocked = {
        "research report",
        "stock report",
        "company report",
        "equity research",
        "daily report",
        "market report",
        "mirae asset securities",
    }
    return text.casefold() not in blocked


def _text_mentions_any_target_alias(text: str, aliases: Sequence[str]) -> bool:
    compact = re.sub(r"\s+", "", str(text or "")).lower()
    for alias in aliases:
        clean = re.sub(r"\s+", "", str(alias or "")).lower()
        if clean and clean in compact:
            return True
    return False


def _search_provider_name(provider: SearchProvider) -> str:
    return str(getattr(provider, "provider_name", None) or provider.__class__.__name__ or "WebSearchProvider")


def _provider_errors(provider: SearchProvider) -> tuple[str, ...]:
    errors = getattr(provider, "errors", ())
    if not errors:
        return ()
    return tuple(str(item) for item in errors if str(item))


def _web_task_id(*, task: SourceTask, event: CandidateEventV2, query: str, provider_name: str) -> str:
    return _stable_web_id("WEBTASK", task.task_id, event.symbol, provider_name, query)


def _web_result_id(*, web_task_id: str, result: SearchResult) -> str:
    return _stable_web_id("WEBRESULT", web_task_id, result.url, result.title, str(result.rank))


def _web_fetch_id(*, web_result_id: str, document_id: str | None = None, reason: str | None = None) -> str:
    return _stable_web_id("WEBFETCH", web_result_id, document_id or "", reason or "")


def _web_rejected_id(*, task_id: str, query: str | None, url: str | None, reason: str) -> str:
    return _stable_web_id("WEBREJECT", task_id, query or "", url or "", reason)


def _stable_web_id(prefix: str, *parts: str) -> str:
    digest = hashlib.sha256("\x1f".join(str(part) for part in parts).encode("utf-8")).hexdigest()[:20]
    return f"{prefix}-{digest}"


def _hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _web_task_row(
    *,
    task: SourceTask,
    event: CandidateEventV2,
    provider_name: str,
    as_of_date: date,
    query: str | None,
    status: str,
    rejection_reason: str | None,
    result_count: int,
    fetched_document_count: int,
    rejected_document_count: int,
    web_task_id: str | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": "e2r_research_brain_v4_web_search_task_v1",
        "web_task_id": web_task_id or _stable_web_id("WEBTASK", task.task_id, event.symbol, provider_name, query or "NO_QUERY"),
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": task.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "archetype_id": task.archetype_id,
        "primitive_gap": task.primitive_gap,
        "query": query,
        "llm_generated_query": query,
        "query_intent": query,
        "provider_name": provider_name,
        "search_provider": provider_name,
        "as_of_date": as_of_date.isoformat(),
        "status": status,
        "search_call_executed": status == "SEARCH_EXECUTED",
        "rejection_reason": rejection_reason,
        "max_results": int(task.max_candidates),
        "max_fetches": int(task.max_fetches),
        "result_count": int(result_count),
        "fetched_document_count": int(fetched_document_count),
        "rejected_document_count": int(rejected_document_count),
        "snippet_score_forbidden": True,
        "source_origin": "research_brain_v4_attempt",
        "brain_web_origin": "research_brain_v4_attempt",
    }


def _web_result_row(
    *,
    web_task_id: str,
    task: SourceTask,
    event: CandidateEventV2,
    provider_name: str,
    repo_root: Path,
    as_of_date: date,
    query: str,
    result: SearchResult,
) -> dict[str, Any]:
    published = _date_or_datetime_from_any(result.published_at)
    result_id = _web_result_id(web_task_id=web_task_id, result=result)
    official_route = _official_detail_route_from_web_result(result)
    verified_issuer_route = _verified_issuer_web_route_from_web_result(
        event=event,
        result=result,
        repo_root=repo_root,
        as_of_date=as_of_date,
    )
    verified_report_route = _verified_report_web_route_from_web_result(result)
    return {
        "schema_version": "e2r_research_brain_v4_web_search_result_v1",
        "web_result_id": result_id,
        "web_task_id": web_task_id,
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": task.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": query,
        "provider_name": provider_name,
        "search_provider": provider_name,
        "as_of_date": as_of_date.isoformat(),
        "status": "RESULT_DISCOVERED",
        "url": result.url,
        "title": result.title,
        "snippet": result.snippet,
        "snippet_only": True,
        "snippet_score_forbidden": True,
        "source": result.source,
        "discovered_by_provider_name": provider_name if official_route is not None else None,
        "official_detail_resolution_required": official_route is not None,
        "official_source_class": official_route.source_class if official_route is not None else None,
        "official_source_provider_name": official_route.provider_name if official_route is not None else None,
        "official_detail_resolver": official_route.resolver_name if official_route is not None else None,
        "official_document_id": official_route.official_document_id if official_route is not None else None,
        "official_detail_resolution_status": "PENDING" if official_route is not None else None,
        "verified_issuer_original": verified_issuer_route is not None,
        "verified_issuer_original_source_class": verified_issuer_route.source_class if verified_issuer_route is not None else None,
        "verified_issuer_original_provider_name": verified_issuer_route.provider_name if verified_issuer_route is not None else None,
        "verified_issuer_original_resolver": verified_issuer_route.resolver_name if verified_issuer_route is not None else None,
        "verified_issuer_original_document_id": verified_issuer_route.official_document_id if verified_issuer_route is not None else None,
        "verified_issuer_homepage_host": verified_issuer_route.matched_homepage_host if verified_issuer_route is not None else None,
        "verified_issuer_result_host": verified_issuer_route.matched_result_host if verified_issuer_route is not None else None,
        "verified_issuer_authority_source_kind": verified_issuer_route.authority_source_kind if verified_issuer_route is not None else None,
        "verified_issuer_authority_source_url": verified_issuer_route.authority_source_url if verified_issuer_route is not None else None,
        "verified_issuer_authority_source_anchor_text": verified_issuer_route.authority_source_anchor_text if verified_issuer_route is not None else None,
        "verified_issuer_authority_entry_id": verified_issuer_route.authority_entry_id if verified_issuer_route is not None else None,
        "verified_issuer_original_status": "PENDING" if verified_issuer_route is not None else None,
        "verified_report_original": verified_report_route is not None,
        "verified_report_original_source_class": verified_report_route.source_class if verified_report_route is not None else None,
        "verified_report_original_provider_name": verified_report_route.provider_name if verified_report_route is not None else None,
        "verified_report_original_resolver": verified_report_route.resolver_name if verified_report_route is not None else None,
        "verified_report_original_document_id": verified_report_route.official_document_id if verified_report_route is not None else None,
        "verified_report_result_host": verified_report_route.matched_result_host if verified_report_route is not None else None,
        "verified_report_original_status": "PENDING" if verified_report_route is not None else None,
        "rank": result.rank,
        "published_at": published.isoformat() if hasattr(published, "isoformat") else None,
        "is_news": result.is_news,
        "is_pdf": result.is_pdf,
        "is_report_domain": result.is_report_domain,
        "selected_for_fetch": False,
        "selection_status": "NOT_SELECTED",
        "source_origin": "research_brain_v4_attempt",
        "brain_web_origin": "research_brain_v4_attempt",
    }


def _web_fetched_row(
    *,
    task: SourceTask,
    event: CandidateEventV2,
    provider_name: str,
    as_of_date: date,
    query: str,
    result: SearchResult,
    result_row: Mapping[str, Any],
    fetch_result: FetchResult,
    document: EvidenceDocument,
    anchor: EvidenceAnchor,
) -> dict[str, Any]:
    official_required = bool(result_row.get("official_detail_resolution_required"))
    verified_issuer_original = bool(result_row.get("verified_issuer_original"))
    verified_report_original = bool(result_row.get("verified_report_original"))
    return {
        "schema_version": "e2r_research_brain_v4_web_fetched_document_v1",
        "web_fetch_id": _web_fetch_id(web_result_id=str(result_row["web_result_id"]), document_id=document.document_id),
        "web_result_id": result_row["web_result_id"],
        "web_task_id": result_row["web_task_id"],
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": task.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": query,
        "provider_name": provider_name,
        "discovered_by_provider_name": result_row.get("discovered_by_provider_name"),
        "official_detail_resolution_required": official_required,
        "official_source_class": result_row.get("official_source_class"),
        "official_source_provider_name": result_row.get("official_source_provider_name"),
        "official_detail_resolver": result_row.get("official_detail_resolver"),
        "official_document_id": result_row.get("official_document_id"),
        "official_detail_resolution_status": "RESOLVED" if official_required else None,
        "verified_issuer_original": verified_issuer_original,
        "verified_issuer_original_source_class": result_row.get("verified_issuer_original_source_class"),
        "verified_issuer_original_provider_name": result_row.get("verified_issuer_original_provider_name"),
        "verified_issuer_original_resolver": result_row.get("verified_issuer_original_resolver"),
        "verified_issuer_original_document_id": result_row.get("verified_issuer_original_document_id"),
        "verified_issuer_homepage_host": result_row.get("verified_issuer_homepage_host"),
        "verified_issuer_result_host": result_row.get("verified_issuer_result_host"),
        "verified_issuer_authority_source_kind": result_row.get("verified_issuer_authority_source_kind"),
        "verified_issuer_authority_source_url": result_row.get("verified_issuer_authority_source_url"),
        "verified_issuer_authority_source_anchor_text": result_row.get("verified_issuer_authority_source_anchor_text"),
        "verified_issuer_authority_entry_id": result_row.get("verified_issuer_authority_entry_id"),
        "verified_issuer_original_status": "RESOLVED" if verified_issuer_original else None,
        "verified_report_original": verified_report_original,
        "verified_report_original_source_class": result_row.get("verified_report_original_source_class"),
        "verified_report_original_provider_name": result_row.get("verified_report_original_provider_name"),
        "verified_report_original_resolver": result_row.get("verified_report_original_resolver"),
        "verified_report_original_document_id": result_row.get("verified_report_original_document_id"),
        "verified_report_result_host": result_row.get("verified_report_result_host"),
        "verified_report_original_status": "RESOLVED" if verified_report_original else None,
        "as_of_date": as_of_date.isoformat(),
        "status": "FETCHED_FULL_SOURCE",
        "url": result.url,
        "title": result.title,
        "published_at": result_row.get("published_at"),
        "fetched_at": fetch_result.fetched_at.isoformat() if fetch_result.fetched_at else None,
        "content_type": fetch_result.content_type,
        "source_path": fetch_result.source_path,
        "document_id": document.document_id,
        "anchor_id": anchor.anchor_id,
        "document_hash": document.content_hash,
        "full_source_count": 1,
        "snippet_score_forbidden": True,
        "source_origin": "research_brain_v4_attempt",
        "brain_web_origin": "research_brain_v4_attempt",
    }


def _web_rejected_row(
    *,
    task: SourceTask,
    event: CandidateEventV2,
    provider_name: str,
    as_of_date: date,
    query: str | None,
    result: SearchResult | None,
    reason: str,
    web_result_id: str | None = None,
    fetch_result: FetchResult | None = None,
) -> dict[str, Any]:
    url = result.url if result is not None else None
    official_route = _official_detail_route_from_web_result(result) if result is not None else None
    return {
        "schema_version": "e2r_research_brain_v4_web_rejected_document_v1",
        "web_rejected_id": _web_rejected_id(task_id=task.task_id, query=query, url=url, reason=reason),
        "web_result_id": web_result_id,
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": task.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": query,
        "provider_name": provider_name,
        "discovered_by_provider_name": provider_name if official_route is not None else None,
        "official_detail_resolution_required": official_route is not None,
        "official_source_class": official_route.source_class if official_route is not None else None,
        "official_source_provider_name": official_route.provider_name if official_route is not None else None,
        "official_detail_resolver": official_route.resolver_name if official_route is not None else None,
        "official_document_id": official_route.official_document_id if official_route is not None else None,
        "official_detail_resolution_status": "FAILED" if official_route is not None and reason.startswith("official_detail_resolve_failed") else None,
        "as_of_date": as_of_date.isoformat(),
        "status": "REJECTED",
        "url": url,
        "title": result.title if result is not None else None,
        "published_at": result.published_at.isoformat() if result is not None and result.published_at else None,
        "rejection_reason": reason,
        "fetch_reason": fetch_result.reason if fetch_result is not None else None,
        "snippet_score_forbidden": True,
        "source_origin": "research_brain_v4_attempt",
        "brain_web_origin": "research_brain_v4_attempt",
    }


def _web_source_type(result: SearchResult, *, verified_issuer_route: _VerifiedIssuerWebRoute | None = None) -> SourceType:
    if _official_detail_route_from_web_result(result) is not None:
        return SourceType.FILING
    if verified_issuer_route is not None:
        return SourceType.NEWS
    if result.is_news:
        return SourceType.NEWS
    if result.is_pdf or result.is_report_domain:
        return SourceType.RESEARCH_REPORT
    if result.is_disclosure:
        return SourceType.FILING
    return SourceType.OTHER


def _official_detail_route_from_url(url: str) -> _OfficialDetailRoute | None:
    try:
        parsed = urlsplit(str(url or ""))
    except ValueError:
        return None
    host = (parsed.hostname or "").lower()
    query = {key.lower(): value for key, value in parse_qs(parsed.query).items()}
    if host == "dart.fss.or.kr":
        rcp_no = _first_query_value(query, "rcpno", "rcept_no", "rceptno")
        if rcp_no:
            return _OfficialDetailRoute(
                source_class="DART",
                provider_name="DART",
                resolver_name="dart_viewer_rcpno",
                official_document_id=f"opendart:disclosure:{rcp_no}",
            )
    if host == "kind.krx.co.kr":
        acpt_no = _first_query_value(query, "acptno", "acpt_no")
        if acpt_no:
            return _OfficialDetailRoute(
                source_class="KIND",
                provider_name="KIND",
                resolver_name="kind_disclsviewer_acptno",
                official_document_id=f"kind:disclosure:{acpt_no}",
            )
    return None


def _official_detail_route_from_web_result(result: SearchResult) -> _OfficialDetailRoute | None:
    return _official_detail_route_from_url(result.url)


def _verified_report_web_route_from_web_result(result: SearchResult) -> _VerifiedReportWebRoute | None:
    result_host = _normalized_host(result.url)
    if not result_host:
        return None
    if not (result.is_pdf or result.is_report_domain or is_recognized_report_domain(result.url)):
        return None
    if not is_verified_report_original_url(result.url, title=result.title):
        return None
    return _VerifiedReportWebRoute(
        source_class="BrokerReportPublicPDF",
        provider_name="BrokerReportDomain",
        resolver_name="recognized_broker_report_domain",
        official_document_id=f"broker_report_domain:{result_host}",
        matched_result_host=result_host,
    )


def _verified_issuer_web_route_from_web_result(
    *,
    event: CandidateEventV2,
    result: SearchResult,
    repo_root: Path,
    as_of_date: date,
) -> _VerifiedIssuerWebRoute | None:
    result_host = _normalized_host(result.url)
    if not result_host:
        return None
    authorities = _issuer_official_domain_authorities(repo_root=repo_root, event=event, as_of_date=as_of_date)
    matched_authority: _IssuerOfficialDomainAuthority | None = None
    for authority in authorities:
        if _host_matches_homepage_or_subdomain(result_host=result_host, homepage_host=authority.host):
            matched_authority = authority
            break
    if matched_authority is None:
        return None
    title_snippet = "\n".join(str(item or "") for item in (result.title, result.snippet))
    aliases = _target_aliases_for_web_relevance(event, result=result)
    if not _text_mentions_any_target_alias(title_snippet, aliases):
        return None
    return _VerifiedIssuerWebRoute(
        source_class=matched_authority.source_class or "CompanyNewsroom",
        provider_name="IssuerOfficialDomain",
        resolver_name=matched_authority.source_kind or "companyguide_homepage_domain_subdomain",
        official_document_id=f"issuer_official_domain:{matched_authority.host}:{result_host}",
        matched_homepage_host=matched_authority.host,
        matched_result_host=result_host,
        authority_source_kind=matched_authority.source_kind,
        authority_source_url=matched_authority.source_url,
        authority_source_anchor_text=matched_authority.source_anchor_text,
        authority_entry_id=matched_authority.entry_id,
    )


def _issuer_official_domain_authorities(
    *,
    repo_root: Path,
    event: CandidateEventV2,
    as_of_date: date,
) -> tuple[_IssuerOfficialDomainAuthority, ...]:
    authorities = (
        *_issuer_official_domain_authorities_from_companyguide(
            repo_root=repo_root,
            event=event,
            as_of_date=as_of_date,
        ),
        *_issuer_official_domain_authorities_from_registry(
            repo_root=repo_root,
            event=event,
            as_of_date=as_of_date,
        ),
    )
    deduped: list[_IssuerOfficialDomainAuthority] = []
    seen: set[tuple[str, str]] = set()
    for authority in authorities:
        key = (authority.host, authority.source_kind)
        if authority.host and key not in seen:
            seen.add(key)
            deduped.append(authority)
    return tuple(deduped)


def _issuer_official_domain_authorities_from_companyguide(
    *,
    repo_root: Path,
    event: CandidateEventV2,
    as_of_date: date,
) -> tuple[_IssuerOfficialDomainAuthority, ...]:
    cache_root = repo_root / "data/cache/company_guide"
    authorities: list[_IssuerOfficialDomainAuthority] = []
    for snapshot_path in sorted(cache_root.glob(f"*/{event.symbol}_snapshot.html"), reverse=True):
        snapshot_date = _date_from_path(snapshot_path)
        if snapshot_date is not None and snapshot_date > as_of_date:
            continue
        text = snapshot_path.read_text(encoding="utf-8", errors="ignore")
        for url in _companyguide_homepage_urls(text):
            host = _normalized_host(url)
            if host:
                authorities.append(
                    _IssuerOfficialDomainAuthority(
                        host=host,
                        source_class="CompanyNewsroom",
                        source_kind="companyguide_homepage_domain_subdomain",
                        source_url=f"snapshot://company_guide/{snapshot_path.parent.name}/{event.symbol}_snapshot.html",
                        source_anchor_text="홈페이지",
                        entry_id=f"companyguide_homepage:{event.symbol}:{host}:{snapshot_path.parent.name}",
                    )
                )
    return tuple(dict.fromkeys(authorities))


def _issuer_official_domain_authorities_from_registry(
    *,
    repo_root: Path,
    event: CandidateEventV2,
    as_of_date: date,
) -> tuple[_IssuerOfficialDomainAuthority, ...]:
    payload = _load_json(repo_root / "configs/e2r_issuer_official_domains_v1.json")
    if isinstance(payload, Mapping):
        entries = payload.get("entries")
    else:
        entries = payload
    if not isinstance(entries, Sequence) or isinstance(entries, (str, bytes)):
        return ()
    authorities: list[_IssuerOfficialDomainAuthority] = []
    for raw_entry in entries:
        if not isinstance(raw_entry, Mapping):
            continue
        authority = _issuer_official_domain_authority_from_registry_entry(
            entry=raw_entry,
            event=event,
            as_of_date=as_of_date,
        )
        if authority is not None:
            authorities.append(authority)
    return tuple(authorities)


def _issuer_official_domain_authority_from_registry_entry(
    *,
    entry: Mapping[str, Any],
    event: CandidateEventV2,
    as_of_date: date,
) -> _IssuerOfficialDomainAuthority | None:
    if str(entry.get("status") or "ACTIVE").strip().upper() != "ACTIVE":
        return None
    symbol = str(entry.get("symbol") or "").strip()
    if symbol != str(event.symbol or "").strip():
        return None
    host = _normalized_host(str(entry.get("host") or ""))
    source_url = str(entry.get("source_url") or "").strip()
    source_anchor_text = str(entry.get("source_anchor_text") or "").strip()
    if not host or not source_url or not source_anchor_text:
        return None
    valid_from = _date_from_any(entry.get("valid_from"))
    verified_as_of = _date_from_any(entry.get("verified_as_of"))
    valid_to = _date_from_any(entry.get("valid_to"))
    if valid_from is None or verified_as_of is None:
        return None
    if valid_from > as_of_date or verified_as_of > as_of_date:
        return None
    if valid_to is not None and valid_to < as_of_date:
        return None
    source_class = str(entry.get("source_class") or "CompanyNewsroom").strip() or "CompanyNewsroom"
    return _IssuerOfficialDomainAuthority(
        host=host,
        source_class=source_class,
        source_kind="issuer_official_domain_registry",
        source_url=source_url,
        source_anchor_text=source_anchor_text,
        entry_id=str(entry.get("entry_id") or f"issuer_official_domain_registry:{symbol}:{host}").strip(),
    )


def _companyguide_homepage_urls(html: str) -> tuple[str, ...]:
    text = str(html or "")
    urls: list[str] = []
    for match in re.finditer(r"<a\b[^>]*>", text, flags=re.IGNORECASE):
        tag = match.group(0)
        if "홈페이지" not in tag and "homepage" not in tag.lower():
            continue
        href_match = re.search(r"""href\s*=\s*["'](?P<href>[^"']+)["']""", tag, flags=re.IGNORECASE)
        if href_match:
            urls.append(href_match.group("href"))
    return tuple(dict.fromkeys(urls))


def _normalized_host(url: str) -> str:
    value = str(url or "").strip()
    if not value:
        return ""
    try:
        host = (urlsplit(value if "://" in value else f"https://{value}").hostname or "").lower()
    except ValueError:
        return ""
    if host.startswith("www."):
        host = host[4:]
    return host.strip(".")


def _host_matches_homepage_or_subdomain(*, result_host: str, homepage_host: str) -> bool:
    result = _normalized_host(f"https://{result_host}")
    homepage = _normalized_host(f"https://{homepage_host}")
    if not result or not homepage:
        return False
    return result == homepage or result.endswith(f".{homepage}")


def _document_has_verified_issuer_original_lineage(document: EvidenceDocument) -> bool:
    lineage = str(document.source_lineage_id or "")
    marker = "verified_issuer_original:issuer_official_domain:"
    if marker not in lineage:
        return False
    suffix = lineage.split(marker, 1)[1]
    parts = suffix.split(":")
    if len(parts) < 2:
        return False
    authority_host = _normalized_host(parts[0])
    result_host = _normalized_host(parts[1])
    canonical_host = _normalized_host(str(document.canonical_url or ""))
    if not authority_host or not result_host or not canonical_host:
        return False
    if canonical_host != result_host:
        return False
    return result_host == authority_host or result_host.endswith(f".{authority_host}")


def _document_has_verified_report_original_lineage(document: EvidenceDocument) -> bool:
    lineage = str(document.source_lineage_id or "")
    marker = "verified_report_original:broker_report_domain:"
    if marker not in lineage:
        return False
    suffix = lineage.split(marker, 1)[1]
    result_host = _normalized_host(suffix.split(":", 1)[0])
    canonical_url = str(document.canonical_url or "")
    canonical_host = _normalized_host(canonical_url)
    if not result_host or not canonical_host:
        return False
    if canonical_host != result_host:
        return False
    return is_verified_report_original_url(canonical_url)


def _first_query_value(query: Mapping[str, Sequence[str]], *keys: str) -> str:
    for key in keys:
        values = query.get(key.lower()) or ()
        for value in values:
            clean = str(value or "").strip()
            if clean:
                return clean
    return ""


def _source_type(source_class: str) -> SourceType:
    normalized = _normalize_source_class(source_class)
    if normalized in {"DART", "KIND", "KRX"}:
        return SourceType.FILING
    if normalized in {"IR", "IssuerOfficial", "Official"}:
        return SourceType.IR
    if normalized == "CompanyGuide":
        return SourceType.API
    if normalized in {"TrustedNews", "News"}:
        return SourceType.NEWS
    if normalized in {"ReportPDF", "BrokerReportPublicPDF", "ReplaySourceSnapshot"}:
        return SourceType.RESEARCH_REPORT
    return SourceType.OTHER


def _csv_rows(path: Path) -> tuple[dict[str, str], ...]:
    if not path.exists():
        return ()
    with path.open("r", encoding="utf-8", newline="") as handle:
        return tuple(dict(row) for row in csv.DictReader(handle))


def _load_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def _row_text(provider: str, row: Mapping[str, Any], *, raw_text: str, symbol: str, company_name: str) -> str:
    fields = [f"{provider} source record", f"{company_name}({symbol})", raw_text]
    for key, value in row.items():
        if value in (None, "") or key in {"raw_text"}:
            continue
        fields.append(f"{key}={value}")
    return "\n".join(fields)


def _source_fetch_text(result: SourceFetchResult) -> str:
    if result.raw_text.strip():
        return result.raw_text
    if result.structured_payload:
        return json.dumps(result.structured_payload, ensure_ascii=False, sort_keys=True)
    return ""


def _source_fetch_anchor_text(*, result: SourceFetchResult, fallback_text: str) -> str:
    if isinstance(result.structured_payload, Mapping):
        anchor_text = str(result.structured_payload.get("score_anchor_text") or "").strip()
        if anchor_text:
            return anchor_text[:4000]
    return fallback_text[:500]


def _score_block_reasons_for_live_result(result: SourceFetchResult) -> tuple[str, ...]:
    reasons: list[str] = []
    score_usage = result.structured_payload.get("score_usage") if isinstance(result.structured_payload, Mapping) else None
    if score_usage:
        reasons.append(str(score_usage))
    if result.source_class in {"KIND", "KRX"} and result.official_document_id in {"kind:main", "krx:mdc:main"}:
        reasons.append("provider_portal_coverage_only_not_symbol_claim")
    if _date_or_datetime_from_any(result.published_at) is None:
        reasons.append("published_at_unknown_not_source_backed")
    if _date_or_datetime_from_any(result.available_at) is None:
        reasons.append("available_at_unknown_not_source_backed")
    return tuple(dict.fromkeys(reasons))


def _date_or_datetime_from_any(value: Any) -> date | datetime | None:
    if value in (None, ""):
        return None
    if isinstance(value, (date, datetime)):
        return value
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        parsed = _date_from_any(value)
        return parsed


def _best_quote(text: str) -> str:
    stripped = str(text or "").strip()
    if not stripped:
        return str(text or "")[:200]
    return stripped[:500]


def _strip_html(value: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", value, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&").replace("&#39;", "'")
    return re.sub(r"\s+", " ", text).strip()


def _date_from_any(value: Any) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    text = str(value).strip().replace(".", "-")
    if len(text) >= 8 and text[:8].isdigit():
        text = f"{text[:4]}-{text[4:6]}-{text[6:8]}"
    try:
        return datetime.fromisoformat(text[:10]).date()
    except ValueError:
        return None


def _yy_mm_dd_date(value: Any, as_of_date: date) -> date | None:
    text = str(value or "").strip()
    match = re.match(r"(?P<yy>\d{2})[./-](?P<mm>\d{1,2})[./-](?P<dd>\d{1,2})$", text)
    if not match:
        return _date_from_any(value)
    year = 2000 + int(match.group("yy"))
    parsed = date(year, int(match.group("mm")), int(match.group("dd")))
    if parsed > as_of_date and year - 100 >= 1990:
        parsed = date(year - 100, parsed.month, parsed.day)
    return parsed


def _snapshot_date_from_text(text: str) -> date | None:
    match = re.search(r"\[기준\s*:?\s*(\d{4})[.-](\d{2})[.-](\d{2})\]", text)
    if not match:
        return None
    return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))


def _date_from_path(path: Path) -> date | None:
    for part in reversed(path.parts):
        parsed = _date_from_any(part)
        if parsed is not None:
            return parsed
    return None


def _safe_slug(value: str) -> str:
    return re.sub(r"[^0-9A-Za-z가-힣]+", "_", value).strip("_").lower()


_OFFICIAL_SOLVABLE_PRIMITIVE_IDS = {
    "contract_visibility",
    "contract_amount_to_prior_sales",
    "contract_duration_months",
    "contract_quality",
    "delivery_schedule",
    "export_contract",
    "order_backlog_to_sales",
    "order_to_revenue_bridge",
    "revenue_visibility_contract",
}


def _is_official_solvable_gap(primitive: str) -> bool:
    lower = primitive.lower()
    if lower in _OFFICIAL_SOLVABLE_PRIMITIVE_IDS:
        return True
    return any(token in lower for token in ("backlog", "cash", "contract", "fcf", "revision", "rpo"))


def _is_fcf_gap(primitive: str) -> bool:
    lower = primitive.lower()
    return any(token in lower for token in ("cash", "fcf", "revision"))


def _snapshot_relevance(primitive: str, text: str) -> int:
    lower = text.lower()
    primitive_lower = primitive.lower()
    keyword_map = {
        "customer": ("고객", "customer", "엔비디아", "nvidia", "asic", "다변화"),
        "allocation": ("고객", "customer", "allocation", "배정", "다변화"),
        "contract": ("계약", "수주", "long-term", "supply agreement", "backlog", "rpo"),
        "backlog": ("수주잔고", "backlog", "rpo", "order"),
        "capacity": ("공급부족", "공급 부족", "병목", "capacity", "capa", "supply"),
        "price": ("가격", "price", "asp", "상향"),
        "revision": ("추정eps 상향", "목표주가 상향", "revision", "상향"),
        "margin": ("마진", "영업이익", "opm", "margin", "fcf"),
        "fcf": ("fcf", "현금흐름", "cash"),
        "spread": ("spread", "스프레드", "판가", "원재료"),
        "retention": ("renewal", "retention", "churn", "arr", "rpo"),
    }
    score = 0
    for key, needles in keyword_map.items():
        if key in primitive_lower:
            score += sum(5 for needle in needles if needle.lower() in lower)
    score += sum(1 for token in primitive_lower.replace("_", " ").split() if token and token in lower)
    return score


__all__ = ["SourceAcquisitionRunnerV4", "StoredSourceSnapshot"]
