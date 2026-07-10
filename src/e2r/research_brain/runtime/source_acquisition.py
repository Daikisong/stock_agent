"""Mode-aware canonical source acquisition for QuestionSourceTask."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol, Sequence
from urllib.parse import parse_qs, urlsplit

from e2r.research.page_fetcher import PageFetcher
from e2r.research.search_provider import SearchProvider, SearchResult
from e2r.research_brain.planning.source_task import (
    QuestionSourceTask,
    SourceBudget,
)
from e2r.research_brain.v4_schemas import SourceAcquisitionResultV4


SOURCE_ACQUISITION_SCHEMA_VERSION = "e2r_source_acquisition_v1"

_SOURCE_FAMILY_ALIASES = {
    "IR": "IssuerIR",
    "BrokerPDF": "ResearchReport",
    "BrokerReport": "ResearchReport",
    "News": "TrustedNews",
    "OfficialDisclosure": "DART",
}
_DISCOVERY_ONLY_SOURCE_FAMILIES = frozenset(
    {
        "Naver",
        "NaverNews",
        "NaverSearch",
        "GeneralWeb",
        "GeneralWebSearch",
        "TrustedNewsSearch",
        "WebSearch",
    }
)


class AcquisitionMode(str, Enum):
    PRODUCTION_BOUNDED = "PRODUCTION_BOUNDED"
    HISTORICAL_REPLAY = "HISTORICAL_REPLAY"
    SOURCE_REPAIR_BACKFILL = "SOURCE_REPAIR_BACKFILL"
    CONTROLLED_SMOKE = "CONTROLLED_SMOKE"


class AcquisitionStatus(str, Enum):
    SELECTED = "SELECTED"
    PARTIAL = "PARTIAL"
    NO_EVIDENCE = "NO_EVIDENCE"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    SOURCE_EXHAUSTED = "SOURCE_EXHAUSTED"
    REJECTED_BY_POLICY = "REJECTED_BY_POLICY"


class DocumentRejectionReason(str, Enum):
    UNKNOWN_DATE = "UNKNOWN_DATE"
    FUTURE_DATE = "FUTURE_DATE"
    SNIPPET_ONLY = "SNIPPET_ONLY"
    FULL_FETCH_FAILED = "FULL_FETCH_FAILED"
    NO_CONTENT_HASH = "NO_CONTENT_HASH"
    CONTENT_HASH_MISMATCH = "CONTENT_HASH_MISMATCH"
    SNAPSHOT_AS_LIVE = "SNAPSHOT_AS_LIVE"
    LIVE_RESULT_IN_HISTORICAL_REPLAY = "LIVE_RESULT_IN_HISTORICAL_REPLAY"
    NON_SNAPSHOT_IN_HISTORICAL_REPLAY = "NON_SNAPSHOT_IN_HISTORICAL_REPLAY"
    REPORT_REPLAY_NOT_REAL_FETCH = "REPORT_REPLAY_NOT_REAL_FETCH"
    SOURCE_CLASS_DOCUMENT_MISMATCH = "SOURCE_CLASS_DOCUMENT_MISMATCH"
    WRONG_SUBJECT = "WRONG_SUBJECT"
    REPOST_WITHOUT_ORIGINAL = "REPOST_WITHOUT_ORIGINAL"
    RECIPE_SECTION_MISSING = "RECIPE_SECTION_MISSING"
    STALE_DOCUMENT = "STALE_DOCUMENT"
    DUPLICATE_DOCUMENT = "DUPLICATE_DOCUMENT"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    TASK_RECIPE_LINK_MISMATCH = "TASK_RECIPE_LINK_MISMATCH"
    OUTSIDE_BUDGET = "OUTSIDE_BUDGET"
    FAKE_PROVIDER_IN_PRODUCTION = "FAKE_PROVIDER_IN_PRODUCTION"


@dataclass(frozen=True)
class BudgetUsage:
    queries: int = 0
    candidates: int = 0
    fetches: int = 0

    def __post_init__(self) -> None:
        for name in ("queries", "candidates", "fetches"):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"budget usage {name} must be a non-negative integer")

    def plus(self, other: "BudgetUsage") -> "BudgetUsage":
        return BudgetUsage(
            queries=self.queries + other.queries,
            candidates=self.candidates + other.candidates,
            fetches=self.fetches + other.fetches,
        )

    def within(self, budget: SourceBudget) -> bool:
        return (
            self.queries <= budget.max_queries
            and self.candidates <= budget.max_candidates
            and self.fetches <= budget.max_fetches
        )

    def remaining(self, budget: SourceBudget) -> SourceBudget | None:
        values = (
            budget.max_queries - self.queries,
            budget.max_candidates - self.candidates,
            budget.max_fetches - self.fetches,
        )
        if min(values) <= 0:
            return None
        return SourceBudget(
            max_queries=values[0],
            max_candidates=values[1],
            max_fetches=values[2],
        )

    def to_dict(self) -> dict[str, int]:
        return asdict(self)


@dataclass(frozen=True)
class DocumentCandidate:
    candidate_id: str
    task_id: str
    recipe_id: str
    provider_name: str
    source_family: str
    document_type: str
    title: str
    canonical_url: str
    original_source_url: str | None
    published_at: str | None
    available_at: str | None
    fetched_at: str | None
    full_text: str | None
    content_hash: str | None
    content_type: str | None
    discovery_source_family: str | None
    snippet: str | None
    full_fetch_performed: bool
    counts_as_live: bool
    is_snapshot: bool
    report_replay: bool
    fake_provider: bool
    is_repost: bool
    original_source_verified: bool
    target_relation: str
    source_lineage_id: str
    provider_error: str | None = None

    def __post_init__(self) -> None:
        required = (
            self.candidate_id,
            self.task_id,
            self.recipe_id,
            self.provider_name,
            self.source_family,
            self.document_type,
            self.title,
            self.canonical_url,
            self.target_relation,
            self.source_lineage_id,
        )
        if not all(item.strip() for item in required):
            raise ValueError("document candidate identity and provenance are required")
        for value in (self.published_at, self.available_at, self.fetched_at):
            if value is not None:
                _parse_date(value)
        if self.content_hash is not None and not _is_sha256(self.content_hash):
            raise ValueError("document candidate content_hash must be SHA-256")
        if self.counts_as_live and self.is_snapshot:
            raise ValueError("snapshot candidate cannot claim live acquisition")
        if self.full_fetch_performed and not str(self.full_text or "").strip():
            raise ValueError("full fetch provenance requires non-empty full text")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SelectedDocumentSection:
    section_id: str
    section_name: str
    text: str
    content_hash: str
    matched_recipe_sections: tuple[str, ...]

    def __post_init__(self) -> None:
        required = (self.section_id, self.section_name, self.text, self.content_hash)
        if not all(item.strip() for item in required):
            raise ValueError("selected document section fields must be non-empty")
        if not _is_sha256(self.content_hash):
            raise ValueError("selected document section hash must be SHA-256")
        if _sha256(self.text) != self.content_hash:
            raise ValueError("selected document section hash mismatch")
        if not self.matched_recipe_sections:
            raise ValueError("selected section requires recipe-section linkage")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AcquiredDocument:
    document_id: str
    candidate_id: str
    task_id: str
    recipe_id: str
    mode: str
    provider_name: str
    source_family: str
    document_type: str
    title: str
    canonical_url: str
    original_source_url: str
    published_at: str
    available_at: str
    fetched_at: str | None
    full_text: str
    content_hash: str
    content_type: str | None
    discovery_source_family: str | None
    selected_sections: tuple[SelectedDocumentSection, ...]
    counts_as_live: bool
    historical_replay: bool
    source_repair_only: bool
    controlled_smoke: bool
    original_source_verified: bool
    source_document_compatible: bool
    target_relation: str
    source_lineage_id: str
    snippet_used_as_document: bool = False
    runtime_score_eligible: bool = False
    schema_version: str = SOURCE_ACQUISITION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        AcquisitionMode(self.mode)
        required = (
            self.document_id,
            self.candidate_id,
            self.task_id,
            self.recipe_id,
            self.provider_name,
            self.source_family,
            self.document_type,
            self.title,
            self.canonical_url,
            self.original_source_url,
            self.published_at,
            self.available_at,
            self.full_text,
            self.content_hash,
            self.target_relation,
            self.source_lineage_id,
        )
        if not all(item.strip() for item in required):
            raise ValueError("acquired document fields must be non-empty")
        _parse_date(self.published_at)
        _parse_date(self.available_at)
        if self.fetched_at is not None:
            _parse_date(self.fetched_at)
        if not _is_sha256(self.content_hash) or _sha256(self.full_text) != self.content_hash:
            raise ValueError("acquired document content hash is missing or mismatched")
        if not self.selected_sections:
            raise ValueError("acquired document requires recipe-selected sections")
        if self.snippet_used_as_document:
            raise ValueError("search snippet can never become an acquired document")
        if not self.original_source_verified:
            raise ValueError("acquired document requires verified original source")
        if not self.source_document_compatible:
            raise ValueError("acquired document source family/type mismatch")
        if self.target_relation != "DIRECT":
            raise ValueError("acquired document must be directly about the target")
        if self.runtime_score_eligible:
            raise ValueError("acquisition output cannot directly score")
        if self.mode == AcquisitionMode.PRODUCTION_BOUNDED.value and not self.counts_as_live:
            raise ValueError("production acquired document must be a real live fetch")
        if self.mode == AcquisitionMode.HISTORICAL_REPLAY.value and self.counts_as_live:
            raise ValueError("historical replay document cannot count as live fetch")
        if self.historical_replay != (
            self.mode == AcquisitionMode.HISTORICAL_REPLAY.value
        ):
            raise ValueError("historical replay provenance mismatch")
        if self.source_repair_only != (
            self.mode == AcquisitionMode.SOURCE_REPAIR_BACKFILL.value
        ):
            raise ValueError("source-repair provenance mismatch")
        if self.controlled_smoke != (
            self.mode == AcquisitionMode.CONTROLLED_SMOKE.value
        ):
            raise ValueError("controlled-smoke provenance mismatch")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class DocumentRejection:
    rejection_id: str
    candidate_id: str
    task_id: str
    recipe_id: str
    mode: str
    reason: str
    detail: str
    provider_name: str
    source_family: str
    canonical_url: str
    discovered_via: str | None = None

    def __post_init__(self) -> None:
        AcquisitionMode(self.mode)
        DocumentRejectionReason(self.reason)
        required = (
            self.rejection_id,
            self.candidate_id,
            self.task_id,
            self.recipe_id,
            self.detail,
            self.provider_name,
            self.source_family,
            self.canonical_url,
        )
        if not all(item.strip() for item in required):
            raise ValueError("document rejection provenance is incomplete")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DocumentSelection:
    document: AcquiredDocument | None
    rejection_reason: str | None
    rejection_detail: str | None

    def __post_init__(self) -> None:
        if self.document is not None:
            if self.rejection_reason is not None or self.rejection_detail is not None:
                raise ValueError("selected document cannot also carry rejection")
        else:
            if self.rejection_reason is None or not str(self.rejection_detail or "").strip():
                raise ValueError("document selection rejection requires reason and detail")
            DocumentRejectionReason(self.rejection_reason)


@dataclass(frozen=True)
class ConnectorBatch:
    connector_name: str
    provider_name: str
    source_family: str
    candidates: tuple[DocumentCandidate, ...]
    provider_errors: tuple[str, ...]
    usage: BudgetUsage
    counts_as_live: bool
    snapshot_batch: bool
    fake_provider: bool
    discovery_only: bool = False

    def __post_init__(self) -> None:
        if not all(
            item.strip()
            for item in (self.connector_name, self.provider_name, self.source_family)
        ):
            raise ValueError("connector batch identity is required")
        if self.counts_as_live and self.snapshot_batch:
            raise ValueError("connector snapshot batch cannot claim live")
        if len({candidate.candidate_id for candidate in self.candidates}) != len(
            self.candidates
        ):
            raise ValueError("connector batch contains duplicate candidate IDs")
        if self.usage.candidates < len(self.candidates):
            raise ValueError("connector batch under-reports candidate usage")
        _require_strings(self.provider_errors, context="provider_errors")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class AcquisitionResult:
    acquisition_id: str
    task_id: str
    recipe_id: str
    mode: str
    status: str
    documents: tuple[AcquiredDocument, ...]
    rejections: tuple[DocumentRejection, ...]
    provider_errors: tuple[str, ...]
    source_gaps: tuple[str, ...]
    usage: BudgetUsage
    candidate_count: int
    candidate_count_by_discovery_source: Mapping[str, int]
    budget_within_task: bool
    official_attempted_before_discovery: bool
    stop_reason: str
    production_runtime_ready: bool = False
    schema_version: str = SOURCE_ACQUISITION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        AcquisitionMode(self.mode)
        AcquisitionStatus(self.status)
        if not all(
            item.strip()
            for item in (
                self.acquisition_id,
                self.task_id,
                self.recipe_id,
                self.stop_reason,
            )
        ):
            raise ValueError("acquisition result identity and stop reason are required")
        terminal_ids = [document.candidate_id for document in self.documents] + [
            rejection.candidate_id for rejection in self.rejections
        ]
        if len(terminal_ids) != len(set(terminal_ids)):
            raise ValueError("acquisition candidate has multiple terminal states")
        if len(terminal_ids) != self.candidate_count:
            raise ValueError("every acquisition candidate requires document or rejection")
        if sum(self.candidate_count_by_discovery_source.values()) != self.candidate_count:
            raise ValueError("candidate discovery-source counts do not reconcile")
        if any(
            not str(key).strip()
            or isinstance(value, bool)
            or not isinstance(value, int)
            or value < 0
            for key, value in self.candidate_count_by_discovery_source.items()
        ):
            raise ValueError("candidate discovery-source counts are invalid")
        if any(
            document.task_id != self.task_id or document.recipe_id != self.recipe_id
            for document in self.documents
        ):
            raise ValueError("acquired document is not linked to task and recipe")
        if any(
            rejection.task_id != self.task_id
            or rejection.recipe_id != self.recipe_id
            for rejection in self.rejections
        ):
            raise ValueError("document rejection is not linked to task and recipe")
        if any(document.mode != self.mode for document in self.documents) or any(
            rejection.mode != self.mode for rejection in self.rejections
        ):
            raise ValueError("acquisition terminal state mode does not match result")
        if self.provider_errors and self.status not in {
            AcquisitionStatus.PROVIDER_FAILED.value,
            AcquisitionStatus.PARTIAL.value,
        }:
            raise ValueError("provider failure cannot be masked by acquisition status")
        if self.status == AcquisitionStatus.SELECTED.value and (
            not self.documents or self.provider_errors
        ):
            raise ValueError("selected acquisition requires documents without provider errors")
        if self.status == AcquisitionStatus.PARTIAL.value and (
            not self.documents or not self.provider_errors
        ):
            raise ValueError("partial acquisition requires documents and provider errors")
        if self.status == AcquisitionStatus.PROVIDER_FAILED.value and (
            self.documents or not self.provider_errors
        ):
            raise ValueError("provider-failed acquisition requires errors and no documents")
        if self.status in {
            AcquisitionStatus.NO_EVIDENCE.value,
            AcquisitionStatus.SOURCE_EXHAUSTED.value,
            AcquisitionStatus.REJECTED_BY_POLICY.value,
        } and self.documents:
            raise ValueError("non-selected acquisition status cannot carry documents")
        if self.production_runtime_ready:
            raise ValueError("Phase 8 acquisition result cannot declare production ready")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


class SourceConnector(Protocol):
    connector_name: str
    provider_name: str
    source_family: str
    discovery_only: bool
    fake_provider: bool

    def acquire(
        self,
        *,
        task: QuestionSourceTask,
        mode: AcquisitionMode,
        remaining_budget: SourceBudget,
    ) -> ConnectorBatch:
        ...


class RecipeDocumentSelectorProtocol(Protocol):
    def select(
        self,
        *,
        task: QuestionSourceTask,
        candidate: DocumentCandidate,
        mode: AcquisitionMode,
        as_of_date: date,
    ) -> DocumentSelection:
        ...


@dataclass
class SourceAcquisitionEngine:
    connectors: tuple[SourceConnector, ...]
    selector: RecipeDocumentSelectorProtocol
    test_mode: bool = False

    def acquire(
        self,
        *,
        task: QuestionSourceTask,
        mode: AcquisitionMode | str,
    ) -> AcquisitionResult:
        acquisition_mode = AcquisitionMode(mode)
        if (
            acquisition_mode == AcquisitionMode.PRODUCTION_BOUNDED
            and not task.production_execution_allowed
        ):
            return _policy_rejected_result(
                task=task,
                mode=acquisition_mode,
                reason="production mode requires a real-provider QuestionSourceTask",
            )
        by_family: dict[str, list[SourceConnector]] = {}
        for connector in self.connectors:
            by_family.setdefault(
                _normalize_source_family(connector.source_family),
                [],
            ).append(connector)

        main_families = tuple(
            dict.fromkeys(
                _normalize_source_family(item)
                for item in (
                    *task.source_route.preferred_source_families,
                    *task.source_route.fallback_source_families,
                )
            )
        )
        discovery_families = tuple(
            dict.fromkeys(
                _normalize_source_family(item)
                for item in task.source_route.discovery_source_families
            )
        )
        usage = BudgetUsage()
        documents: list[AcquiredDocument] = []
        rejections: list[DocumentRejection] = []
        provider_errors: list[str] = []
        source_gaps: list[str] = []
        seen_candidate_ids: set[str] = set()
        seen_content_hashes: set[str] = set()
        candidate_count = 0
        candidate_count_by_discovery_source: dict[str, int] = {}
        official_attempted = False
        discovery_attempted = False

        def run_family(family: str, *, discovery: bool) -> None:
            nonlocal usage, candidate_count, official_attempted, discovery_attempted
            if discovery:
                discovery_attempted = True
            else:
                official_attempted = True
            if not discovery and family in _DISCOVERY_ONLY_SOURCE_FAMILIES:
                source_gaps.append(f"DISCOVERY_ONLY_SOURCE_SKIPPED:{family}")
                return
            connectors = tuple(
                connector
                for connector in by_family.get(family, ())
                if bool(connector.discovery_only) == discovery
            )
            if not connectors:
                source_gaps.append(f"CONNECTOR_NOT_CONFIGURED:{family}")
                return
            for connector in connectors:
                remaining = usage.remaining(task.budget)
                if remaining is None:
                    source_gaps.append("SOURCE_TASK_BUDGET_EXHAUSTED")
                    return
                if (
                    acquisition_mode == AcquisitionMode.PRODUCTION_BOUNDED
                    and connector.fake_provider
                ):
                    provider_errors.append(
                        f"FAKE_PROVIDER_IN_PRODUCTION:{connector.provider_name}"
                    )
                    continue
                if connector.fake_provider and not self.test_mode:
                    provider_errors.append(
                        f"FAKE_PROVIDER_OUTSIDE_TEST_MODE:{connector.provider_name}"
                    )
                    continue
                try:
                    batch = connector.acquire(
                        task=task,
                        mode=acquisition_mode,
                        remaining_budget=remaining,
                    )
                except Exception as exc:
                    provider_errors.append(
                        f"{connector.provider_name}:{type(exc).__name__}:{exc}"
                    )
                    continue
                batch_identity_error = _connector_batch_identity_error(
                    connector=connector,
                    batch=batch,
                    expected_family=family,
                    discovery=discovery,
                )
                if batch_identity_error:
                    provider_errors.append(batch_identity_error)
                usage = usage.plus(batch.usage)
                provider_errors.extend(batch.provider_errors)
                if not batch.candidates and not batch.provider_errors:
                    source_gaps.append(
                        f"NO_CANDIDATES:{family}:{batch.provider_name}"
                    )
                batch_budget_violated = not batch.usage.within(remaining)
                if batch_budget_violated:
                    provider_errors.append(
                        f"CONNECTOR_BUDGET_VIOLATION:{batch.connector_name}"
                    )
                for candidate in batch.candidates:
                    if candidate.candidate_id in seen_candidate_ids:
                        continue
                    seen_candidate_ids.add(candidate.candidate_id)
                    candidate_count += 1
                    discovery_key = candidate.discovery_source_family or "DIRECT"
                    candidate_count_by_discovery_source[discovery_key] = (
                        candidate_count_by_discovery_source.get(discovery_key, 0) + 1
                    )
                    if candidate.provider_error:
                        provider_errors.append(
                            f"{candidate.provider_name}:{candidate.provider_error}"
                        )
                    route_error = batch_identity_error or _candidate_route_error(
                        candidate=candidate,
                        batch=batch,
                        expected_family=family,
                        discovery=discovery,
                    )
                    if route_error:
                        rejections.append(
                            _rejection(
                                task=task,
                                candidate=candidate,
                                mode=acquisition_mode,
                                reason=(
                                    DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH
                                ),
                                detail=route_error,
                            )
                        )
                        continue
                    if batch_budget_violated:
                        rejections.append(
                            _rejection(
                                task=task,
                                candidate=candidate,
                                mode=acquisition_mode,
                                reason=DocumentRejectionReason.OUTSIDE_BUDGET,
                                detail=(
                                    "connector reported usage outside the remaining "
                                    "QuestionSourceTask budget"
                                ),
                            )
                        )
                        continue
                    rejection = _preselection_rejection(
                        task=task,
                        candidate=candidate,
                        mode=acquisition_mode,
                    )
                    if rejection is not None:
                        rejections.append(rejection)
                        continue
                    content_hash = _sha256(str(candidate.full_text))
                    if content_hash in seen_content_hashes:
                        rejections.append(
                            _rejection(
                                task=task,
                                candidate=candidate,
                                mode=acquisition_mode,
                                reason=DocumentRejectionReason.DUPLICATE_DOCUMENT,
                                detail="identical fetched content was already processed",
                            )
                        )
                        continue
                    selection = self.selector.select(
                        task=task,
                        candidate=candidate,
                        mode=acquisition_mode,
                        as_of_date=date.fromisoformat(task.as_of_date),
                    )
                    if selection.document is None:
                        rejections.append(
                            _rejection(
                                task=task,
                                candidate=candidate,
                                mode=acquisition_mode,
                                reason=DocumentRejectionReason(
                                    str(selection.rejection_reason)
                                ),
                                detail=str(selection.rejection_detail),
                            )
                        )
                        continue
                    documents.append(selection.document)
                    seen_content_hashes.add(content_hash)

        for family in main_families:
            run_family(family, discovery=False)
            if usage.remaining(task.budget) is None:
                break
        if usage.remaining(task.budget) is not None and not documents:
            for family in discovery_families:
                run_family(family, discovery=True)
                if usage.remaining(task.budget) is None:
                    break

        provider_errors = list(dict.fromkeys(provider_errors))
        source_gaps = list(dict.fromkeys(source_gaps))
        budget_within = usage.within(task.budget)
        if documents and provider_errors:
            status = AcquisitionStatus.PARTIAL
        elif documents:
            status = AcquisitionStatus.SELECTED
        elif provider_errors:
            status = AcquisitionStatus.PROVIDER_FAILED
        elif rejections or source_gaps:
            status = AcquisitionStatus.SOURCE_EXHAUSTED
        else:
            status = AcquisitionStatus.NO_EVIDENCE
        stop_reason = {
            AcquisitionStatus.SELECTED: "recipe_document_selected_within_budget",
            AcquisitionStatus.PARTIAL: "documents_selected_with_provider_failures_preserved",
            AcquisitionStatus.PROVIDER_FAILED: "provider_failed_without_selected_document",
            AcquisitionStatus.SOURCE_EXHAUSTED: "all_candidates_rejected_or_sources_missing",
            AcquisitionStatus.NO_EVIDENCE: "connectors_returned_no_candidates",
        }[status]
        acquisition_id = _stable_id(
            "ACQ",
            {
                "task_id": task.task_id,
                "mode": acquisition_mode.value,
                "document_ids": [document.document_id for document in documents],
                "rejection_ids": [rejection.rejection_id for rejection in rejections],
                "provider_errors": provider_errors,
                "usage": usage.to_dict(),
            },
        )
        return AcquisitionResult(
            acquisition_id=acquisition_id,
            task_id=task.task_id,
            recipe_id=task.recipe_id,
            mode=acquisition_mode.value,
            status=status.value,
            documents=tuple(documents),
            rejections=tuple(rejections),
            provider_errors=tuple(provider_errors),
            source_gaps=tuple(source_gaps),
            usage=usage,
            candidate_count=candidate_count,
            candidate_count_by_discovery_source=dict(
                sorted(candidate_count_by_discovery_source.items())
            ),
            budget_within_task=budget_within,
            official_attempted_before_discovery=(
                not discovery_attempted or official_attempted
            ),
            stop_reason=stop_reason,
        )


@dataclass
class StaticSourceConnector:
    connector_name: str
    provider_name: str
    source_family: str
    batch_factory: Callable[
        [QuestionSourceTask, AcquisitionMode, SourceBudget], ConnectorBatch
    ]
    discovery_only: bool = False
    fake_provider: bool = True

    def acquire(
        self,
        *,
        task: QuestionSourceTask,
        mode: AcquisitionMode,
        remaining_budget: SourceBudget,
    ) -> ConnectorBatch:
        return self.batch_factory(task, mode, remaining_budget)


@dataclass
class SearchFetchSourceConnector:
    connector_name: str
    provider_name: str
    source_family: str
    fetched_source_family: str
    document_type: str
    search_provider: SearchProvider
    page_fetcher: PageFetcher
    counts_as_live: bool
    fake_provider: bool
    discovery_only: bool = True
    snapshot_results: bool = False
    original_url_resolver: Callable[[SearchResult], str | None] | None = None

    def __post_init__(self) -> None:
        required = (
            self.connector_name,
            self.provider_name,
            self.source_family,
            self.fetched_source_family,
            self.document_type,
        )
        if not all(item.strip() for item in required):
            raise ValueError("search/fetch connector identity is required")
        discovery_family = _normalize_source_family(self.source_family)
        fetched_family = _normalize_source_family(self.fetched_source_family)
        if (
            discovery_family in _DISCOVERY_ONLY_SOURCE_FAMILIES
            and not self.discovery_only
        ):
            raise ValueError("web/search connector must remain discovery-only")
        if fetched_family in _DISCOVERY_ONLY_SOURCE_FAMILIES:
            raise ValueError("search provider family cannot masquerade as fetched source")
        if self.counts_as_live and self.snapshot_results:
            raise ValueError("snapshot search connector cannot count as live")

    def acquire(
        self,
        *,
        task: QuestionSourceTask,
        mode: AcquisitionMode,
        remaining_budget: SourceBudget,
    ) -> ConnectorBatch:
        queries = task.query_intent.literal_queries[: remaining_budget.max_queries]
        candidates: list[DocumentCandidate] = []
        errors: list[str] = []
        seen_urls: set[str] = set()
        query_count = 0
        candidate_count = 0
        fetch_count = 0
        as_of = date.fromisoformat(task.as_of_date)
        for query in queries:
            if candidate_count >= remaining_budget.max_candidates:
                break
            query_count += 1
            try:
                results = self.search_provider.search(
                    query,
                    as_of,
                    max_results=remaining_budget.max_candidates - candidate_count,
                )
            except Exception as exc:
                errors.append(f"search:{type(exc).__name__}:{exc}")
                continue
            for result in results:
                if candidate_count >= remaining_budget.max_candidates:
                    break
                canonical_url = result.url.strip()
                if canonical_url in seen_urls:
                    continue
                seen_urls.add(canonical_url)
                candidate_count += 1
                published = result.published_at.date() if result.published_at else None
                original_url = (
                    self.original_url_resolver(result)
                    if self.original_url_resolver is not None
                    else _default_original_url(result)
                )
                fetch_result = None
                fetch_error = None
                if (
                    published is not None
                    and published <= as_of
                    and original_url
                    and fetch_count < remaining_budget.max_fetches
                ):
                    fetch_count += 1
                    try:
                        fetch_result = self.page_fetcher.fetch(
                            original_url,
                            as_of_date=as_of,
                        )
                    except Exception as exc:
                        fetch_error = (
                            f"full_fetch_exception:{type(exc).__name__}:{exc}"
                        )
                text = (
                    str(fetch_result.text)
                    if fetch_result is not None
                    and fetch_result.ok
                    and str(fetch_result.text or "").strip()
                    else None
                )
                provider_error = (
                    str(fetch_result.reason or "full_fetch_failed")
                    if fetch_result is not None and not fetch_result.ok
                    else fetch_error
                )
                target_relation = (
                    "DIRECT"
                    if text and _mentions_target(f"{result.title}\n{text}", task)
                    else "UNKNOWN"
                )
                fetched_at = (
                    fetch_result.fetched_at.date()
                    if fetch_result is not None and fetch_result.fetched_at
                    else None
                )
                content_hash = _sha256(text) if text else None
                candidate_id = _stable_id(
                    "CAND",
                    {
                        "task_id": task.task_id,
                        "url": canonical_url,
                        "original_url": original_url,
                        "published_at": published.isoformat() if published else None,
                    },
                )
                candidates.append(
                    DocumentCandidate(
                        candidate_id=candidate_id,
                        task_id=task.task_id,
                        recipe_id=task.recipe_id,
                        provider_name=self.provider_name,
                        source_family=self.fetched_source_family,
                        document_type=self.document_type,
                        title=result.title,
                        canonical_url=canonical_url,
                        original_source_url=original_url,
                        published_at=published.isoformat() if published else None,
                        available_at=published.isoformat() if published else None,
                        fetched_at=fetched_at.isoformat() if fetched_at else None,
                        full_text=text,
                        content_hash=content_hash,
                        content_type=(
                            fetch_result.content_type if fetch_result is not None else None
                        ),
                        discovery_source_family=self.source_family,
                        snippet=result.snippet,
                        full_fetch_performed=bool(text),
                        counts_as_live=self.counts_as_live,
                        is_snapshot=self.snapshot_results,
                        report_replay=(
                            self.snapshot_results
                            and self.document_type == "research_report"
                        ),
                        fake_provider=self.fake_provider,
                        is_repost=_is_naver_host(canonical_url),
                        original_source_verified=bool(
                            original_url and not _is_naver_host(original_url)
                        ),
                        target_relation=target_relation,
                        source_lineage_id=(
                            str(fetch_result.source_path)
                            if fetch_result is not None and fetch_result.source_path
                            else f"{self.provider_name}:{canonical_url}"
                        ),
                        provider_error=provider_error,
                    )
                )
        return ConnectorBatch(
            connector_name=self.connector_name,
            provider_name=self.provider_name,
            source_family=self.source_family,
            candidates=tuple(candidates),
            provider_errors=tuple(errors),
            usage=BudgetUsage(
                queries=query_count,
                candidates=candidate_count,
                fetches=fetch_count,
            ),
            counts_as_live=self.counts_as_live,
            snapshot_batch=self.snapshot_results,
            fake_provider=self.fake_provider,
            discovery_only=self.discovery_only,
        )


def adapt_v4_source_acquisition_result(
    *,
    result: SourceAcquisitionResultV4,
    task: QuestionSourceTask,
    mode: AcquisitionMode | str,
) -> ConnectorBatch:
    acquisition_mode = AcquisitionMode(mode)
    snapshot_provider = "snapshot" in result.provider_name.lower()
    fake_provider = _looks_like_fake_provider(result.provider_name)
    batch_source_family = _normalize_source_family(
        str(result.source_class or "UNKNOWN")
    )
    candidates: list[DocumentCandidate] = []
    for document in result.documents:
        document_id = str(getattr(document, "document_id", ""))
        text = str(result.document_text_by_id.get(document_id) or "")
        parser_version = str(getattr(document, "parser_version", "") or "")
        is_snapshot = snapshot_provider or "snapshot" in parser_version.lower()
        source_family = batch_source_family
        document_type = _document_type_from_v4_document(document)
        published = _date_text(getattr(document, "published_at", None))
        available = _date_text(getattr(document, "available_at", None)) or published
        fetched = _date_text(getattr(document, "fetched_at", None))
        canonical_url = str(getattr(document, "canonical_url", "") or "")
        score_block_reasons = {
            str(item)
            for item in getattr(document, "score_block_reasons", ())
        }
        if "published_at_unknown_not_source_backed" in score_block_reasons:
            published = None
        if "available_at_unknown_not_source_backed" in score_block_reasons:
            available = None
        snapshot_date_anchor_text = " ".join(
            (
                canonical_url,
                str(getattr(document, "source_lineage_id", "") or ""),
            )
        )
        if (
            is_snapshot
            and published == task.as_of_date
            and task.as_of_date not in snapshot_date_anchor_text
        ):
            published = None
            available = None
        counts_live = (
            acquisition_mode != AcquisitionMode.HISTORICAL_REPLAY
            and not is_snapshot
            and not fake_provider
            and "live" in parser_version.lower()
        )
        content_hash = str(getattr(document, "content_hash", "") or "") or None
        candidates.append(
            DocumentCandidate(
                candidate_id=_stable_id(
                    "V4CAND",
                    {"task_id": task.task_id, "document_id": document_id},
                ),
                task_id=task.task_id,
                recipe_id=task.recipe_id,
                provider_name=result.provider_name,
                source_family=source_family,
                document_type=document_type,
                title=f"v4:{document_id}",
                canonical_url=canonical_url or f"urn:v4-document:{document_id}",
                original_source_url=canonical_url or None,
                published_at=published,
                available_at=available,
                fetched_at=fetched,
                full_text=text or None,
                content_hash=content_hash,
                content_type=None,
                discovery_source_family=None,
                snippet=None,
                full_fetch_performed=bool(
                    text and document_id in set(result.fetched_document_ids)
                ),
                counts_as_live=counts_live,
                is_snapshot=is_snapshot,
                report_replay=(is_snapshot and document_type == "research_report"),
                fake_provider=fake_provider,
                is_repost=False,
                original_source_verified=bool(canonical_url),
                target_relation=(
                    "DIRECT" if text and _mentions_target(text, task) else "UNKNOWN"
                ),
                source_lineage_id=str(
                    getattr(document, "source_lineage_id", "")
                    or f"v4:{document_id}"
                ),
            )
        )
    usage_map = dict(result.budget_used)
    provider_errors = [str(item) for item in result.provider_errors]
    if result.status == "PROVIDER_FAILED" and not provider_errors:
        provider_errors.append("V4_PROVIDER_FAILED_WITHOUT_DETAIL")
    return ConnectorBatch(
        connector_name="v4_source_acquisition_result_adapter",
        provider_name=result.provider_name,
        source_family=batch_source_family,
        candidates=tuple(candidates),
        provider_errors=tuple(provider_errors),
        usage=BudgetUsage(
            queries=int(usage_map.get("queries") or 0),
            candidates=int(usage_map.get("candidates") or 0),
            fetches=int(usage_map.get("fetches") or 0),
        ),
        counts_as_live=bool(candidates and all(item.counts_as_live for item in candidates)),
        snapshot_batch=bool(candidates and all(item.is_snapshot for item in candidates)),
        fake_provider=fake_provider,
        discovery_only=False,
    )


def audit_acquisition_results(
    results: Sequence[AcquisitionResult],
) -> Mapping[str, Any]:
    documents = [document for result in results for document in result.documents]
    rejections = [rejection for result in results for rejection in result.rejections]
    naver_candidates = {
        item.candidate_id
        for item in (*documents, *rejections)
        if (
            getattr(item, "discovery_source_family", None)
            or getattr(item, "discovered_via", None)
        )
        in {"Naver", "NaverNews", "NaverSearch"}
    }
    expected_naver_candidate_count = sum(
        count
        for result in results
        for source, count in result.candidate_count_by_discovery_source.items()
        if source in {"Naver", "NaverNews", "NaverSearch"}
    )
    critical = {
        "snapshot_as_live": sum(
            document.mode == AcquisitionMode.PRODUCTION_BOUNDED.value
            and not document.counts_as_live
            for document in documents
        ),
        "snippet_as_document": sum(
            document.snippet_used_as_document for document in documents
        ),
        "no_content_hash_fetched": sum(
            not document.content_hash for document in documents
        ),
        "provider_failure_masked": sum(
            bool(result.provider_errors)
            and result.status
            not in {
                AcquisitionStatus.PROVIDER_FAILED.value,
                AcquisitionStatus.PARTIAL.value,
            }
            for result in results
        ),
        "source_class_document_mismatch": sum(
            not document.source_document_compatible for document in documents
        ),
        "report_replay_counted_real_fetch": sum(
            document.historical_replay and document.counts_as_live
            for document in documents
        ),
        "document_missing_task_recipe_link": sum(
            not document.task_id or not document.recipe_id for document in documents
        ),
        "naver_without_full_fetch_or_rejection": max(
            0,
            expected_naver_candidate_count - len(naver_candidates),
        ),
        "budget_violation": sum(not result.budget_within_task for result in results),
        "discovery_before_official": sum(
            not result.official_attempted_before_discovery for result in results
        ),
    }
    return {
        "schema_version": "e2r_source_acquisition_audit_v1",
        "status": (
            "SOURCE_ACQUISITION_CONTRACT_PASS"
            if results and sum(critical.values()) == 0
            else "SOURCE_ACQUISITION_CONTRACT_FAIL"
        ),
        "result_count": len(results),
        "document_count": len(documents),
        "rejection_count": len(rejections),
        "naver_terminal_candidate_count": len(naver_candidates),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": _sha256(
            _stable_json({"results": [result.to_dict() for result in results]})
        ),
        "production_runtime_ready": False,
    }


def _preselection_rejection(
    *,
    task: QuestionSourceTask,
    candidate: DocumentCandidate,
    mode: AcquisitionMode,
) -> DocumentRejection | None:
    if candidate.task_id != task.task_id or candidate.recipe_id != task.recipe_id:
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.TASK_RECIPE_LINK_MISMATCH,
            detail="connector candidate task/recipe identity mismatch",
        )
    if mode == AcquisitionMode.PRODUCTION_BOUNDED:
        if candidate.fake_provider:
            return _rejection(
                task=task,
                candidate=candidate,
                mode=mode,
                reason=DocumentRejectionReason.FAKE_PROVIDER_IN_PRODUCTION,
                detail="fake connector result cannot enter production",
            )
        if candidate.report_replay:
            return _rejection(
                task=task,
                candidate=candidate,
                mode=mode,
                reason=DocumentRejectionReason.REPORT_REPLAY_NOT_REAL_FETCH,
                detail="stored report replay cannot count as a real fetch",
            )
        if candidate.is_snapshot or not candidate.counts_as_live:
            return _rejection(
                task=task,
                candidate=candidate,
                mode=mode,
                reason=DocumentRejectionReason.SNAPSHOT_AS_LIVE,
                detail="production mode requires live connector provenance",
            )
    if mode == AcquisitionMode.HISTORICAL_REPLAY and candidate.counts_as_live:
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.LIVE_RESULT_IN_HISTORICAL_REPLAY,
            detail="historical replay cannot relabel live fetch as replay",
        )
    if mode == AcquisitionMode.HISTORICAL_REPLAY and not candidate.is_snapshot:
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.NON_SNAPSHOT_IN_HISTORICAL_REPLAY,
            detail="historical replay requires frozen snapshot provenance",
        )
    if candidate.provider_error:
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.FULL_FETCH_FAILED,
            detail=candidate.provider_error,
        )
    if candidate.published_at is None or candidate.available_at is None:
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.UNKNOWN_DATE,
            detail="published_at and available_at must be source-backed",
        )
    as_of = date.fromisoformat(task.as_of_date)
    if _parse_date(candidate.published_at) > as_of or _parse_date(candidate.available_at) > as_of:
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.FUTURE_DATE,
            detail="candidate was published or available after as_of_date",
        )
    if candidate.is_repost and (
        not candidate.original_source_verified or not candidate.original_source_url
    ):
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.REPOST_WITHOUT_ORIGINAL,
            detail="repost or Naver page has no verified original source",
        )
    if not candidate.original_source_verified or not candidate.original_source_url:
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.REPOST_WITHOUT_ORIGINAL,
            detail="original source URL was not verified",
        )
    if not candidate.full_fetch_performed or not str(candidate.full_text or "").strip():
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.SNIPPET_ONLY,
            detail="search metadata/snippet is discovery-only; full fetch is required",
        )
    if candidate.target_relation != "DIRECT":
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.WRONG_SUBJECT,
            detail="fetched full text is not directly about the target",
        )
    if candidate.content_hash is None:
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.NO_CONTENT_HASH,
            detail="fetched full text has no content hash",
        )
    if candidate.content_hash != _sha256(str(candidate.full_text)):
        return _rejection(
            task=task,
            candidate=candidate,
            mode=mode,
            reason=DocumentRejectionReason.CONTENT_HASH_MISMATCH,
            detail="connector content hash does not match fetched full text",
        )
    return None


def _connector_batch_identity_error(
    *,
    connector: SourceConnector,
    batch: ConnectorBatch,
    expected_family: str,
    discovery: bool,
) -> str | None:
    mismatches: list[str] = []
    if batch.connector_name != connector.connector_name:
        mismatches.append("connector_name")
    if batch.provider_name != connector.provider_name:
        mismatches.append("provider_name")
    if _normalize_source_family(batch.source_family) != expected_family:
        mismatches.append("source_family")
    if batch.discovery_only != discovery:
        mismatches.append("discovery_only")
    if batch.fake_provider != connector.fake_provider:
        mismatches.append("fake_provider")
    if not mismatches:
        return None
    return "CONNECTOR_BATCH_IDENTITY_MISMATCH:" + ",".join(mismatches)


def _candidate_route_error(
    *,
    candidate: DocumentCandidate,
    batch: ConnectorBatch,
    expected_family: str,
    discovery: bool,
) -> str | None:
    if candidate.provider_name != batch.provider_name:
        return "candidate provider does not match connector batch"
    if candidate.fake_provider != batch.fake_provider:
        return "candidate fake/real provenance does not match connector batch"
    if discovery:
        discovered_via = _normalize_source_family(
            str(candidate.discovery_source_family or "")
        )
        if discovered_via != expected_family:
            return "discovery candidate is not linked to the executing discovery source"
        return None
    if candidate.discovery_source_family is not None:
        return "discovery candidate cannot masquerade as a direct source result"
    if _normalize_source_family(candidate.source_family) != expected_family:
        return "direct candidate source family does not match its connector route"
    return None


def _rejection(
    *,
    task: QuestionSourceTask,
    candidate: DocumentCandidate,
    mode: AcquisitionMode,
    reason: DocumentRejectionReason,
    detail: str,
) -> DocumentRejection:
    return DocumentRejection(
        rejection_id=_stable_id(
            "DREJ",
            {
                "candidate_id": candidate.candidate_id,
                "task_id": task.task_id,
                "reason": reason.value,
                "detail": detail,
            },
        ),
        candidate_id=candidate.candidate_id,
        task_id=task.task_id,
        recipe_id=task.recipe_id,
        mode=mode.value,
        reason=reason.value,
        detail=detail,
        provider_name=candidate.provider_name,
        source_family=candidate.source_family,
        canonical_url=candidate.canonical_url,
        discovered_via=candidate.discovery_source_family,
    )


def _policy_rejected_result(
    *,
    task: QuestionSourceTask,
    mode: AcquisitionMode,
    reason: str,
) -> AcquisitionResult:
    return AcquisitionResult(
        acquisition_id=_stable_id(
            "ACQ",
            {"task_id": task.task_id, "mode": mode.value, "reason": reason},
        ),
        task_id=task.task_id,
        recipe_id=task.recipe_id,
        mode=mode.value,
        status=AcquisitionStatus.REJECTED_BY_POLICY.value,
        documents=(),
        rejections=(),
        provider_errors=(),
        source_gaps=(reason,),
        usage=BudgetUsage(),
        candidate_count=0,
        candidate_count_by_discovery_source={},
        budget_within_task=True,
        official_attempted_before_discovery=True,
        stop_reason=reason,
    )


def _default_original_url(result: SearchResult) -> str | None:
    if not _is_naver_host(result.url):
        return result.url
    query = parse_qs(urlsplit(result.url).query)
    for key in ("url", "outlink", "originalUrl", "original_url"):
        values = query.get(key)
        if values and values[0].startswith(("http://", "https://")):
            return values[0]
    return None


def _is_naver_host(url: str) -> bool:
    host = (urlsplit(url).hostname or "").lower()
    return host == "naver.com" or host.endswith(".naver.com")


def _mentions_target(text: str, task: QuestionSourceTask) -> bool:
    normalized = _normalize_target(text)
    return any(
        token and token in normalized
        for token in (
            _normalize_target(task.company_name),
            _normalize_target(task.symbol),
        )
    )


def _normalize_target(value: str) -> str:
    return re.sub(r"[^0-9a-z가-힣]", "", str(value).casefold())


def _normalize_source_family(value: str) -> str:
    clean = str(value).strip()
    return _SOURCE_FAMILY_ALIASES.get(clean, clean)


def _looks_like_fake_provider(value: str) -> bool:
    return (
        re.search(
            r"(?:^|[_:.-])(?:fake|fixture|mock|stub|test)(?:$|[_:.-])",
            str(value).casefold(),
        )
        is not None
    )


def _document_type_from_v4_document(document: Any) -> str:
    source_type = str(getattr(document, "source_type", "")).lower()
    url = str(getattr(document, "canonical_url", "") or "").lower()
    if "filing" in source_type or "dart" in url or "kind.krx" in url:
        return "filing"
    if "broker" in source_type or url.endswith(".pdf"):
        return "research_report"
    if "news" in source_type:
        return "full_article"
    if "transcript" in source_type:
        return "earnings_call_transcript"
    return "structured_record"


def _date_text(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    try:
        return _parse_date(str(value)).isoformat()
    except ValueError:
        return None


def _parse_date(value: str) -> date:
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError as exc:
        raise ValueError(f"invalid ISO date: {value}") from exc


def _require_strings(values: Sequence[str], *, context: str) -> None:
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError(f"{context} contains an empty or non-string value")


def _stable_id(prefix: str, payload: Mapping[str, Any]) -> str:
    return f"{prefix}-{_sha256(_stable_json(payload))[:24]}"


def _stable_json(value: Mapping[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _is_sha256(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{64}", value) is not None


def _json_safe(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, set, frozenset)):
        return [_json_safe(item) for item in value]
    if hasattr(value, "__dataclass_fields__"):
        return _json_safe(asdict(value))
    return value


__all__ = [
    "SOURCE_ACQUISITION_SCHEMA_VERSION",
    "AcquiredDocument",
    "AcquisitionMode",
    "AcquisitionResult",
    "AcquisitionStatus",
    "BudgetUsage",
    "ConnectorBatch",
    "DocumentCandidate",
    "DocumentRejection",
    "DocumentRejectionReason",
    "DocumentSelection",
    "SearchFetchSourceConnector",
    "SelectedDocumentSection",
    "SourceAcquisitionEngine",
    "SourceConnector",
    "StaticSourceConnector",
    "adapt_v4_source_acquisition_result",
    "audit_acquisition_results",
]
