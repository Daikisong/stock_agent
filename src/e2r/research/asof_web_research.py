"""Retrospective as-of web research helpers.

This module is intentionally different from strict forward-archive replay:
it may use today's fixture/current search index to reconstruct old public
documents, but it only accepts documents whose report/news date is not after
the replay date.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field, replace
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.cheap_scan.models import CheapScanCandidate
from e2r.llm.theme_provider import ThemeRouteProvider
from e2r.models import Stage
from e2r.research.free_web_research_runner import FreeWebResearchInput, FreeWebResearchRunner, WebResearchPipelineResult
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import EmptySearchProvider, SearchProvider, SearchResult
from e2r.research.search_snapshot_store import SearchSnapshot, SearchSnapshotStore


@dataclass(frozen=True)
class AsOfDocumentDecision:
    """As-of date decision for one discovered web document."""

    url: str
    title: str
    query: str | None
    published_at: datetime | None
    report_date: date | None
    date_verified: bool
    stage_green_allowed: bool
    rejected_reason: str | None = None


@dataclass(frozen=True)
class AsOfWebResearchConfig:
    """Configuration for one candidate's as-of web research."""

    as_of_date: date
    max_queries_per_candidate: int | None = None
    max_results_per_query: int = 100
    require_date_verified_for_green: bool = True
    allow_undated_docs_for_yellow_only: bool = True
    save_reconstructed_snapshots: bool = False
    reconstructed_snapshot_root: str | Path = "data/reconstructed_snapshots"
    theme_rebalance_enabled: bool | None = None
    theme_route_provider: ThemeRouteProvider | None = None
    max_theme_expansion_rounds: int | None = None
    theme_evidence_review_enabled: bool = True

    def __post_init__(self) -> None:
        if self.max_queries_per_candidate is not None and self.max_queries_per_candidate < 0:
            raise ValueError("max_queries_per_candidate cannot be negative")
        if self.theme_rebalance_enabled is None:
            object.__setattr__(self, "theme_rebalance_enabled", self.theme_route_provider is not None)
        if self.max_theme_expansion_rounds is not None and self.max_theme_expansion_rounds < 0:
            raise ValueError("max_theme_expansion_rounds must be non-negative")


@dataclass(frozen=True)
class AsOfWebResearchResult:
    """Web research result plus as-of filtering diagnostics."""

    candidate: CheapScanCandidate
    pipeline_result: WebResearchPipelineResult | None
    document_decisions: tuple[AsOfDocumentDecision, ...]
    rejected_future_count: int = 0
    date_verified_count: int = 0
    date_unverified_count: int = 0
    reconstructed_snapshot_paths: tuple[Path, ...] = field(default_factory=tuple)


class RetrospectiveSnapshotSearchProvider:
    """Search provider for reconstructed as-of research.

    Existing snapshot rows are treated as a current searchable corpus of old
    public documents. Unlike forward-archive replay, ``search_date`` is not a
    visibility gate here; only the document's ``published_at``/report date is.
    """

    def __init__(
        self,
        *,
        store: SearchSnapshotStore | None = None,
        symbol: str | None = None,
        company_name: str | None = None,
    ) -> None:
        self.store = store or SearchSnapshotStore()
        self.symbol = symbol
        self.company_name = company_name

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        snapshots = self.store.load_snapshots(symbol=self.symbol, company_name=self.company_name)
        if not snapshots and (self.symbol or self.company_name):
            snapshots = self.store.load_snapshots()
        matched = [item for item in snapshots if _snapshot_matches(item, query, self.symbol, self.company_name)]
        rows = [_snapshot_to_search_result(item, query=query, rank=index) for index, item in enumerate(matched, start=1)]
        return tuple(rows[:max_results])


class AsOfDateFilteredSearchProvider:
    """Reject future documents and label undated results before parsing."""

    def __init__(self, provider: SearchProvider, as_of_date: date) -> None:
        self.provider = provider
        self.as_of_date = as_of_date
        self.decisions: list[AsOfDocumentDecision] = []

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        rows: list[SearchResult] = []
        for result in self.provider.search(query, as_of_date, max_results):
            if result.published_at is not None and result.published_at.date() > self.as_of_date:
                self.decisions.append(
                    AsOfDocumentDecision(
                        url=result.url,
                        title=result.title,
                        query=query,
                        published_at=result.published_at,
                        report_date=result.published_at.date(),
                        date_verified=True,
                        stage_green_allowed=False,
                        rejected_reason="published_after_as_of_date",
                    )
                )
                continue
            date_verified = result.published_at is not None
            self.decisions.append(
                AsOfDocumentDecision(
                    url=result.url,
                    title=result.title,
                    query=query,
                    published_at=result.published_at,
                    report_date=result.published_at.date() if result.published_at else None,
                    date_verified=date_verified,
                    stage_green_allowed=date_verified,
                    rejected_reason=None,
                )
            )
            if date_verified:
                rows.append(replace(result, date_verified=True, green_allowed_by_date=True))
            else:
                # Downstream parsers need a date to preserve model invariants.
                # The separate decision record keeps the document date-unverified
                # so it cannot create Stage 3-Green by itself.
                synthetic = datetime(self.as_of_date.year, self.as_of_date.month, self.as_of_date.day, 8, 0)
                rows.append(
                    replace(
                        result,
                        published_at=synthetic,
                        date_verified=False,
                        green_allowed_by_date=False,
                    )
                )
        return tuple(rows)


class AsOfWebResearchRunner:
    """Run free web research with strict as-of document filtering."""

    def run(
        self,
        *,
        candidate: CheapScanCandidate,
        search_provider: SearchProvider,
        fixture_text_by_url: Mapping[str, str | Path] | None = None,
        config: AsOfWebResearchConfig,
    ) -> AsOfWebResearchResult:
        filtered = AsOfDateFilteredSearchProvider(search_provider, config.as_of_date)
        budget = SearchBudget(
            max_total_queries_per_day=config.max_queries_per_candidate,
            max_queries_per_symbol=config.max_queries_per_candidate,
            max_deep_research_symbols=None if config.max_queries_per_candidate is None else 1,
            max_active_monitoring_symbols=None if config.max_queries_per_candidate is None else 1,
        )
        pipeline = FreeWebResearchRunner(
            browser_provider=filtered,
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name=candidate.company_name,
                symbol=candidate.symbol,
                sector=None,
                market=candidate.market,
                as_of_date=config.as_of_date,
                company_aliases=(candidate.company_name, candidate.symbol),
                candidate_reason_codes=candidate.reason_codes,
                budget=budget,
                max_results_per_query=config.max_results_per_query,
                fixture_text_by_url=fixture_text_by_url or {},
                theme_rebalance_enabled=config.theme_rebalance_enabled,
                theme_route_provider=config.theme_route_provider,
                max_theme_expansion_rounds=config.max_theme_expansion_rounds,
                theme_evidence_review_enabled=config.theme_evidence_review_enabled,
            )
        )
        pipeline = _downgrade_green_if_date_unverified_only(pipeline, filtered.decisions, config)
        paths = _save_reconstructed_snapshots(candidate, pipeline, filtered.decisions, config) if config.save_reconstructed_snapshots else ()
        verified = sum(1 for item in filtered.decisions if item.date_verified and item.rejected_reason is None)
        rejected = sum(1 for item in filtered.decisions if item.rejected_reason == "published_after_as_of_date")
        unverified = sum(1 for item in filtered.decisions if not item.date_verified and item.rejected_reason is None)
        return AsOfWebResearchResult(
            candidate=candidate,
            pipeline_result=pipeline,
            document_decisions=tuple(filtered.decisions),
            rejected_future_count=rejected,
            date_verified_count=verified,
            date_unverified_count=unverified,
            reconstructed_snapshot_paths=tuple(paths),
        )


def fixture_text_by_url_for_candidate(
    *,
    store: ReportSnapshotStore | None = None,
    symbol: str | None = None,
    company_name: str | None = None,
) -> Mapping[str, str | Path]:
    """Return all locally available report text for a candidate.

    For retrospective as-of research, visibility is controlled by document
    date filtering, not by the snapshot save date.
    """

    return (store or ReportSnapshotStore()).fixture_text_by_url(symbol=symbol, company_name=company_name)


def _downgrade_green_if_date_unverified_only(
    pipeline: WebResearchPipelineResult,
    decisions: Sequence[AsOfDocumentDecision],
    config: AsOfWebResearchConfig,
) -> WebResearchPipelineResult:
    if not config.require_date_verified_for_green:
        return pipeline
    if pipeline.stage.stage != Stage.STAGE_3_GREEN:
        return pipeline
    if any(item.date_verified and item.rejected_reason is None for item in decisions):
        return pipeline
    stage = replace(
        pipeline.stage,
        stage=Stage.STAGE_3_YELLOW,
        grade="B",
        stage_reason=tuple(pipeline.stage.stage_reason)
        + ("date-unverified documents cannot create Stage 3-Green alone",),
    )
    return replace(pipeline, stage=stage)


def _save_reconstructed_snapshots(
    candidate: CheapScanCandidate,
    pipeline: WebResearchPipelineResult,
    decisions: Sequence[AsOfDocumentDecision],
    config: AsOfWebResearchConfig,
) -> tuple[Path, ...]:
    root = Path(config.reconstructed_snapshot_root)
    search_dir = root / "search"
    report_dir = root / "reports"
    search_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)
    search_path = search_dir / "reconstructed_search.jsonl"
    report_path = report_dir / "reconstructed_reports.jsonl"
    decision_by_url = {item.url: item for item in decisions}
    searched_at = datetime.utcnow().replace(microsecond=0).isoformat()
    search_rows: list[dict[str, Any]] = []
    for result in pipeline.web_result.search_results:
        decision = decision_by_url.get(result.url)
        search_rows.append(
            {
                "replay_as_of_date": config.as_of_date.isoformat(),
                "searched_at": searched_at,
                "query": result.query,
                "url": result.url,
                "title": result.title,
                "snippet": result.snippet,
                "published_at": result.published_at.isoformat() if result.published_at else None,
                "report_date": decision.report_date.isoformat() if decision and decision.report_date else None,
                "date_verified": bool(decision and decision.date_verified),
                "point_in_time_status": "retrospective_reconstructed",
                "strict_pit_proof": False,
                "used_for_stage": result.url in {item.result.url for item in pipeline.web_result.selected_results},
                "stage_green_allowed": bool(decision and decision.stage_green_allowed),
                "source_type": _source_type(result),
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
            }
        )
    if search_rows:
        with search_path.open("a", encoding="utf-8") as handle:
            for row in search_rows:
                handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    report_rows: list[dict[str, Any]] = []
    for fetch in pipeline.web_result.fetched_documents:
        text = fetch.text or ""
        decision = decision_by_url.get(fetch.url)
        report_rows.append(
            {
                "replay_as_of_date": config.as_of_date.isoformat(),
                "searched_at": searched_at,
                "url": fetch.url,
                "date_verified": bool(decision and decision.date_verified),
                "point_in_time_status": "retrospective_reconstructed",
                "strict_pit_proof": False,
                "used_for_stage": bool(fetch.ok and text),
                "stage_green_allowed": bool(decision and decision.stage_green_allowed),
                "source_type": "fetched_document",
                "extracted_text_hash": hashlib.sha256(text.encode("utf-8")).hexdigest() if text else None,
                "parser_confidence": _parser_confidence_for_url(fetch.url, pipeline),
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
            }
        )
    if report_rows:
        with report_path.open("a", encoding="utf-8") as handle:
            for row in report_rows:
                handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    paths: list[Path] = []
    if search_rows:
        paths.append(search_path)
    if report_rows:
        paths.append(report_path)
    return tuple(paths)


def _parser_confidence_for_url(url: str, pipeline: WebResearchPipelineResult) -> float | None:
    for evidence in pipeline.web_result.evidence:
        if evidence.url_or_identifier == url:
            value = evidence.parsed_fields.get("parser_confidence")
            return float(value) if value is not None else evidence.confidence
    return None


def _source_type(result: SearchResult) -> str:
    if result.is_report_domain or result.is_pdf:
        return "research_report"
    if result.is_news:
        return "news"
    if result.is_disclosure:
        return "disclosure"
    return "search_result"


def _snapshot_matches(snapshot: SearchSnapshot, query: str, symbol: str | None, company_name: str | None) -> bool:
    if symbol and snapshot.symbol == symbol:
        return _query_matches(snapshot, query) or bool(snapshot.company_name and snapshot.company_name in query)
    if company_name and snapshot.company_name == company_name:
        return True
    return _query_matches(snapshot, query)


def _query_matches(snapshot: SearchSnapshot, query: str) -> bool:
    haystack = f"{snapshot.query} {snapshot.title} {snapshot.snippet or ''}"
    if snapshot.company_name and snapshot.company_name in query:
        return True
    terms = {term for term in query.split() if len(term) >= 2}
    return bool(terms and sum(1 for term in terms if term in haystack) >= 2)


def _snapshot_to_search_result(snapshot: SearchSnapshot, *, query: str, rank: int) -> SearchResult:
    return SearchResult(
        title=snapshot.title,
        url=snapshot.url,
        snippet=snapshot.snippet,
        source=snapshot.source_type,
        published_at=snapshot.published_at,
        query=query,
        rank=rank,
        is_pdf=snapshot.url.lower().endswith(".pdf") or "pdf" in snapshot.source_type.lower(),
        is_report_domain=snapshot.source_type in {"research_report", "report", "broker_report"},
        is_news=snapshot.source_type in {"news", "naver_news"},
        is_disclosure=snapshot.source_type in {"disclosure", "opendart"},
        confidence=0.82 if snapshot.source_type in {"research_report", "report", "broker_report"} else 0.65,
    )


__all__ = [
    "AsOfDateFilteredSearchProvider",
    "AsOfDocumentDecision",
    "AsOfWebResearchConfig",
    "AsOfWebResearchResult",
    "AsOfWebResearchRunner",
    "RetrospectiveSnapshotSearchProvider",
    "fixture_text_by_url_for_candidate",
]
