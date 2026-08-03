from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from unittest import mock
from dataclasses import replace
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.page_fetcher import FetchResult, PageFetcher
from e2r.research.publication_date import (
    PUBLICATION_DATE_INFERENCE_SEMANTICS_VERSION,
    infer_publication_date,
    infer_source_locator_publication_date,
)
from e2r.research.search_provider import SearchResult
from e2r.cli.run_e2r_researcher_mode_until_pass import (
    _source_transport_work_state,
)
import e2r.research_brain.researcher_mode.source_graph_explorer as source_graph_module
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    _source_checkpoint_is_ready_for_readonly_replay,
)
from e2r.research_brain.researcher_mode.prompt_projection import (
    project_source_graph_checkpoint,
)
from e2r.research_brain.researcher_mode import (
    PHASE85_PASS,
    CodexResearcherProvider,
    ComponentResearchPlan,
    ResearcherDocumentRanker,
    ResearcherSourceGraphAcquirer,
    ResearcherSourceQueryPlanner,
    SourceGraphAcquisitionConfig,
    SourceGraphExplorer,
    SourceResearchObjective,
    compile_phase85_source_graph_acquisition_audit,
    load_source_graph_checkpoint,
    write_source_graph_acquisition_run,
)


TARGET = "CURRENT"
TARGET_NAME = "Current Corp"
AS_OF_DATE = "2026-06-29"
QUERY = "Current Corp 2026 Q2 earnings call capacity allocation"
ALTERNATE_QUERY = "Current Corp official mirror earnings call cash conversion"
FAILED_URL = "https://tls.example.com/report.pdf"
ALTERNATE_URL = "https://mirror.example.com/report"


def _bind_candidate_reference_scope(
    row: dict[str, Any],
    *,
    decision_id: str,
) -> None:
    row.setdefault("normalized_url", row["url"])
    row["materiality_query_ids"] = list(row.get("query_ids") or ())
    row["matched_requested_source_family"] = next(
        iter(row.get("requested_source_families") or ()),
        "NONE",
    )
    row["materiality_decision_id"] = decision_id
    row["ranking_status"] = "MATERIAL"
    row["materiality_scope_hash"] = (
        source_graph_module._candidate_materiality_scope_hash(row)
    )


def _bind_document_reference_scope(
    row: dict[str, Any],
    *,
    decision_id: str,
) -> None:
    row["materiality_query_ids"] = list(row.get("query_ids") or ())
    row["matched_requested_source_family"] = next(
        iter(row.get("requested_source_families") or ()),
        "NONE",
    )
    row["source_materiality_decision_id"] = decision_id
    row["materiality_scope_url"] = row["canonical_url"]
    row["materiality_scope_hash"] = (
        source_graph_module._candidate_materiality_scope_hash(
            {
                "normalized_url": row["materiality_scope_url"],
                "objective_ids": row["objective_ids"],
                "requested_source_families": row[
                    "requested_source_families"
                ],
            }
        )
    )


class SourceBrainProvider:
    provider_name = "TEST_FIXTURE_SOURCE_BRAIN"

    def __init__(
        self,
        *,
        queries: Sequence[str] = (QUERY,),
        source_families: Sequence[str] = ("NAVER_DISCOVERY",),
        material_titles: Sequence[str] = (),
        omit_last_ranking: bool = False,
    ) -> None:
        self.queries = tuple(queries)
        self.source_families = tuple(source_families)
        self.material_titles = tuple(material_titles)
        self.omit_last_ranking = omit_last_ranking
        self.calls: list[Mapping[str, Any]] = []

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        self.calls.append({"pass_name": pass_name, "payload": payload})
        if pass_name == "SOURCE_QUERY_GENERATION":
            objective_id = payload["open_research_objectives"][0]["objective_id"]
            return {
                "suggested_queries": [
                    {
                        "objective_id": objective_id,
                        "literal_query": query,
                        "source_families": list(self.source_families),
                        "rationale": "현재 gap을 원문 source에서 확인한다.",
                        "counter_or_supersession_search": False,
                    }
                    for query in self.queries
                ],
                "new_source_directions": [],
                "unresolved_research_notes": [],
            }
        if pass_name == "SOURCE_CANDIDATE_RANKING":
            rows = list(payload["discovery_candidates"])
            if self.omit_last_ranking:
                rows = rows[:-1]
            return {
                "decisions": [
                    {
                        "candidate_id": row["candidate_id"],
                        "material_relevance": (
                            not self.material_titles
                            or any(value in str(row["title"]) for value in self.material_titles)
                        ),
                        "priority": 1.0 - index * 0.01,
                        "objective_ids": list(row["objective_ids"]),
                        "matched_requested_source_family": (
                            next(
                                iter(
                                    row.get(
                                        "requested_source_families"
                                    )
                                    or ()
                                ),
                                "NONE",
                            )
                            if (
                                not self.material_titles
                                or any(
                                    value in str(row["title"])
                                    for value in self.material_titles
                                )
                            )
                            else "NONE"
                        ),
                        "rationale": "research objective와 직접 관련된 후보",
                    }
                    for index, row in enumerate(rows)
                ],
                "ranking_complete": True,
                "unresolved_notes": [],
            }
        raise AssertionError(pass_name)


class PendingThenCompleteRankingProvider(SourceBrainProvider):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.ranking_pending = True

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        if pass_name == "SOURCE_CANDIDATE_RANKING" and self.ranking_pending:
            self.calls.append({"pass_name": pass_name, "payload": payload})
            raise RuntimeError(
                "COLLABORATION_RESPONSE_PENDING:"
                "COLLABREQ-" + "d" * 64
            )
        return super().complete(pass_name=pass_name, payload=payload)


class EpochPendingRankingProvider(SourceBrainProvider):
    def __init__(
        self,
        *,
        pending_request_ids: Sequence[str],
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.pending_request_ids = list(pending_request_ids)

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        if pass_name == "SOURCE_CANDIDATE_RANKING" and self.pending_request_ids:
            request_id = self.pending_request_ids.pop(0)
            self.calls.append({"pass_name": pass_name, "payload": payload})
            raise RuntimeError(
                "COLLABORATION_RESPONSE_PENDING:" + request_id
            )
        return super().complete(pass_name=pass_name, payload=payload)


class PartialThenCompleteRankingProvider(SourceBrainProvider):
    candidate_ranking_page_candidate_limit = 1

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.partial_ranking_pending = True

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        if (
            pass_name == "SOURCE_CANDIDATE_RANKING"
            and self.partial_ranking_pending
            and str(payload["discovery_candidates"][0]["title"]).endswith(
                "2"
            )
        ):
            self.calls.append({"pass_name": pass_name, "payload": payload})
            raise RuntimeError(
                "COLLABORATION_RESPONSE_PENDING:"
                "COLLABREQ-" + "e" * 64
            )
        return super().complete(pass_name=pass_name, payload=payload)


class PendingThenCompleteQueryProvider(SourceBrainProvider):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.query_pending = True

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        if pass_name == "SOURCE_QUERY_GENERATION" and self.query_pending:
            self.calls.append({"pass_name": pass_name, "payload": payload})
            raise RuntimeError(
                "COLLABORATION_RESPONSE_PENDING:"
                "COLLABREQ-" + "c" * 64
            )
        return super().complete(pass_name=pass_name, payload=payload)


class SparseReferenceRevalidationProvider(SourceBrainProvider):
    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        if pass_name != "SOURCE_CANDIDATE_RANKING":
            return super().complete(pass_name=pass_name, payload=payload)
        self.calls.append({"pass_name": pass_name, "payload": payload})
        decisions = []
        for index, row in enumerate(payload["discovery_candidates"]):
            context = row.get("reference_transport_context") or {}
            sparse = bool(context.get("metadata_sparse"))
            has_full_text = bool(context.get("full_fetch_content_text"))
            material = bool(not sparse or has_full_text)
            decisions.append(
                {
                    "candidate_id": row["candidate_id"],
                    "material_relevance": material,
                    "priority": 1.0 - index * 0.01,
                    "objective_ids": list(row["objective_ids"]),
                    "matched_requested_source_family": (
                        next(
                            iter(row.get("requested_source_families") or ()),
                            "NONE",
                        )
                        if material
                        else "NONE"
                    ),
                    "rationale": (
                        "full fetched text resolves materiality"
                        if has_full_text
                        else "sparse discovery metadata is inconclusive"
                        if sparse
                        else "direct candidate is material"
                    ),
                }
            )
        return {
            "decisions": decisions,
            "ranking_complete": True,
            "unresolved_notes": [],
        }


class TwoScopeRepairProvider(SourceBrainProvider):
    def __init__(self, *, query_by_objective: Mapping[str, str]) -> None:
        super().__init__(queries=())
        self.query_by_objective = dict(query_by_objective)

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        if pass_name == "SOURCE_QUERY_GENERATION":
            self.calls.append({"pass_name": pass_name, "payload": payload})
            return {
                "suggested_queries": [
                    {
                        "objective_id": row["objective_id"],
                        "literal_query": self.query_by_objective[
                            row["objective_id"]
                        ],
                        "source_families": ["ISSUER_NEWSROOM"],
                        "rationale": "각 objective의 공식 원문을 확인한다.",
                        "counter_or_supersession_search": False,
                    }
                    for row in payload["open_research_objectives"]
                    if row["objective_id"] in self.query_by_objective
                ],
                "new_source_directions": [],
                "unresolved_research_notes": [],
            }
        return super().complete(pass_name=pass_name, payload=payload)


class RecordingSearchProvider:
    def __init__(self, results_by_query: Mapping[str, Sequence[SearchResult]]) -> None:
        self.results_by_query = results_by_query
        self.calls: list[tuple[str, str, int]] = []
        self.errors: list[str] = []

    def search(
        self, query: str, as_of_date, max_results: int = 100
    ) -> tuple[SearchResult, ...]:
        self.calls.append((query, as_of_date.isoformat(), max_results))
        return tuple(self.results_by_query.get(query, ()))[:max_results]


class NoNetworkLiveNaver(NaverFreeSearchProvider):
    def __init__(self) -> None:
        super().__init__(
            client_id="not-used",
            client_secret="not-used",
            fixture_mode=False,
            live_enabled=True,
        )
        self.calls: list[str] = []

    def search(self, query, as_of_date, max_results=100):
        self.calls.append(query)
        return ()


class AdaptiveSourceBrainProvider(SourceBrainProvider):
    def __init__(self) -> None:
        super().__init__(queries=())
        self.query_call_count = 0

    def complete(self, *, pass_name, payload):
        if pass_name == "SOURCE_QUERY_GENERATION":
            self.query_call_count += 1
            self.queries = () if self.query_call_count == 1 else (QUERY,)
        return super().complete(pass_name=pass_name, payload=payload)


class AlternateRouteSourceBrainProvider(SourceBrainProvider):
    def __init__(self) -> None:
        super().__init__(queries=())
        self.query_call_count = 0

    def complete(self, *, pass_name, payload):
        if pass_name == "SOURCE_QUERY_GENERATION":
            self.query_call_count += 1
            self.queries = (
                (QUERY,)
                if self.query_call_count == 1
                else (ALTERNATE_QUERY,)
            )
        return super().complete(pass_name=pass_name, payload=payload)


class InvalidThenCorrectRankingProvider(SourceBrainProvider):
    def __init__(self) -> None:
        super().__init__()
        self.ranking_call_count = 0
        self.invalidations: list[str] = []

    def invalidate_last_response_cache(self, reason: str) -> None:
        self.invalidations.append(reason)

    def complete(self, *, pass_name, payload):
        if pass_name == "SOURCE_CANDIDATE_RANKING":
            self.ranking_call_count += 1
            if self.ranking_call_count == 1:
                self.calls.append({"pass_name": pass_name, "payload": payload})
                return {
                    "decisions": [
                        {
                            "candidate_id": "UNKNOWN-CANDIDATE",
                            "material_relevance": True,
                            "priority": 1.0,
                            "objective_ids": ["OBJECTIVE-1"],
                            "matched_requested_source_family": (
                                "NAVER_DISCOVERY"
                            ),
                            "rationale": "잘못된 첫 응답",
                        }
                    ],
                    "ranking_complete": True,
                    "unresolved_notes": [],
                }
        return super().complete(pass_name=pass_name, payload=payload)


class IncompleteThenCorrectRankingProvider(SourceBrainProvider):
    def __init__(self) -> None:
        super().__init__()
        self.ranking_call_count = 0
        self.invalidations: list[str] = []

    def invalidate_last_response_cache(self, reason: str) -> None:
        self.invalidations.append(reason)

    def complete(self, *, pass_name, payload):
        if pass_name == "SOURCE_CANDIDATE_RANKING":
            self.ranking_call_count += 1
            if self.ranking_call_count == 1:
                self.calls.append({"pass_name": pass_name, "payload": payload})
                rows = list(payload["discovery_candidates"])
                return {
                    "decisions": [
                        {
                            "candidate_id": row["candidate_id"],
                            "material_relevance": True,
                            "priority": 1.0,
                            "objective_ids": list(row["objective_ids"]),
                            "matched_requested_source_family": next(
                                iter(
                                    row.get(
                                        "requested_source_families"
                                    )
                                    or ()
                                ),
                                "NONE",
                            ),
                            "rationale": "모든 후보를 분류했지만 완료 표시는 잘못 남겼다.",
                        }
                        for row in rows
                    ],
                    "ranking_complete": False,
                    "unresolved_notes": ["후보가 증거로 충분하지 않을 수 있다."],
                }
        return super().complete(pass_name=pass_name, payload=payload)


class RepeatedIncompleteCompleteRosterProvider(SourceBrainProvider):
    def __init__(self) -> None:
        super().__init__()
        self.ranking_call_count = 0
        self.invalidations: list[str] = []

    def invalidate_last_response_cache(self, reason: str) -> None:
        self.invalidations.append(reason)

    def complete(self, *, pass_name, payload):
        if pass_name != "SOURCE_CANDIDATE_RANKING":
            return super().complete(pass_name=pass_name, payload=payload)
        self.ranking_call_count += 1
        self.calls.append({"pass_name": pass_name, "payload": payload})
        rows = list(payload["discovery_candidates"])
        return {
            "decisions": [
                {
                    "candidate_id": row["candidate_id"],
                    "material_relevance": True,
                    "priority": 1.0,
                    "objective_ids": list(row["objective_ids"]),
                    "matched_requested_source_family": next(
                        iter(
                            row.get("requested_source_families") or ()
                        ),
                        "NONE",
                    ),
                    "rationale": "후보 분류는 끝났지만 원문 수집은 남았다.",
                }
                for row in rows
            ],
            "ranking_complete": False,
            "unresolved_notes": ["원문 fetch와 증거 검증이 남아 있다."],
        }


class SplitRecoveryRankingProvider(SourceBrainProvider):
    def __init__(self) -> None:
        super().__init__()
        self.ranking_batch_sizes: list[int] = []
        self.invalidations: list[str] = []

    def invalidate_last_response_cache(self, reason: str) -> None:
        self.invalidations.append(reason)

    def complete(self, *, pass_name, payload):
        if pass_name != "SOURCE_CANDIDATE_RANKING":
            return super().complete(pass_name=pass_name, payload=payload)
        self.calls.append({"pass_name": pass_name, "payload": payload})
        rows = list(payload["discovery_candidates"])
        self.ranking_batch_sizes.append(len(rows))
        response_rows = rows[:-1] if len(rows) > 2 else rows
        return {
            "decisions": [
                {
                    "candidate_id": row["candidate_id"],
                    "material_relevance": True,
                    "priority": 1.0,
                    "objective_ids": list(row["objective_ids"]),
                    "matched_requested_source_family": next(
                        iter(
                            row.get("requested_source_families") or ()
                        ),
                        "NONE",
                    ),
                    "rationale": "분할된 후보 roster를 모두 직접 검토했다.",
                }
                for row in response_rows
            ],
            "ranking_complete": True,
            "unresolved_notes": [],
        }


class SelectiveRetryFailureFetcher:
    def __init__(self) -> None:
        self.delegate = PageFetcher(
            fixture_text_by_url={
                ALTERNATE_URL: _document_text("alternate-public-route")
            }
        )
        self.calls: list[str] = []

    def fetch(self, url, *, as_of_date):
        self.calls.append(url)
        if url == FAILED_URL:
            return FetchResult(
                url=url,
                ok=False,
                reason=(
                    "live_fetch_failed:URLError:"
                    "certificate verify failed"
                ),
            )
        return self.delegate.fetch(url, as_of_date=as_of_date)


class ReferencedRouteFetcher:
    def __init__(
        self,
        *,
        parent_url: str,
        child_url: str,
        parent_text: str = "Current Corp official redirect",
        parent_ok: bool = True,
    ) -> None:
        self.parent_url = parent_url
        self.child_url = child_url
        self.parent_text = parent_text
        self.parent_ok = parent_ok
        self.calls: list[str] = []

    def fetch(self, url, *, as_of_date):
        self.calls.append(url)
        if url == self.parent_url:
            return FetchResult(
                url=url,
                ok=self.parent_ok,
                text=self.parent_text if self.parent_ok else None,
                content_type="text/html",
                fetched_at=datetime(2026, 6, 20, 8),
                reason=(
                    None
                    if self.parent_ok
                    else "live_fetch_unreadable_text:empty_extracted_text"
                ),
                referenced_urls=(self.child_url,),
            )
        if url == self.child_url:
            return FetchResult(
                url=url,
                ok=True,
                text=_document_text("linked-official-transcript"),
                content_type="application/pdf",
                fetched_at=datetime(2026, 6, 20, 8),
                response_last_modified_at=datetime(2026, 5, 11, 2, 39, 25),
            )
        return FetchResult(url=url, ok=False, reason="fixture URL missing")


class LastModifiedFetcher:
    def __init__(
        self,
        *,
        url: str,
        text: str | None = None,
        last_modified_at: datetime = datetime(2026, 5, 11, 2, 39, 25),
    ) -> None:
        self.url = url
        self.text = text
        self.last_modified_at = last_modified_at

    def fetch(self, url, *, as_of_date):
        if url != self.url:
            return FetchResult(url=url, ok=False, reason="fixture URL missing")
        return FetchResult(
            url=url,
            ok=True,
            text=self.text
            or (
                "Current Corp disclosed current earnings, capacity, cash conversion, "
                "customer allocation, and counter evidence. "
                + "source-backed unlabelled detail " * 12
            ),
            content_type="application/pdf",
            fetched_at=datetime(2026, 6, 20, 8),
            response_last_modified_at=self.last_modified_at,
        )


class PublicationMetadataFetcher:
    def __init__(self, *, url: str, published_at: str) -> None:
        self.url = url
        self.published_at = published_at

    def fetch(self, url, *, as_of_date):
        if url != self.url:
            return FetchResult(url=url, ok=False, reason="fixture URL missing")
        return FetchResult(
            url=url,
            ok=True,
            text=(
                "Current Corp disclosed current earnings, capacity, cash conversion, "
                "customer allocation, and counter evidence. "
                + "source-backed document detail " * 12
            ),
            content_type="text/html",
            fetched_at=datetime(2026, 6, 20, 8),
            publication_metadata_parts=(
                f"JSON_LD_DATE_PUBLISHED:{self.published_at}",
            ),
            publication_metadata_semantics_version=(
                "e2r_page_fetch_publication_metadata_v1"
            ),
        )


class IncompleteBoundedRepairFetcher(PageFetcher):
    def fetch(self, url, *, as_of_date):
        returned = self.max_text_chars or 2_000_000
        return FetchResult(
            url=url,
            ok=True,
            text="Current Corp incomplete bounded filing",
            content_type="application/pdf",
            fetched_at=datetime(2026, 6, 20, 8),
            text_complete=False,
            original_text_chars=returned + 1,
            returned_text_chars=returned,
        )


class TimeoutRepairFetcher(PageFetcher):
    def fetch(self, url, *, as_of_date):
        return FetchResult(
            url=url,
            ok=False,
            reason="live_fetch_failed:timeout",
        )


class E2RV5SourceGraphAcquisitionTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_source_locator_date_accepts_filing_route_not_certificate_expiry(
        self,
    ) -> None:
        self.assertEqual(
            infer_source_locator_publication_date(
                "https://englishdart.fss.or.kr/dsbh001/main.do"
                "?rcpNo=20260716000552"
            ),
            date(2026, 7, 16),
        )
        self.assertEqual(
            infer_source_locator_publication_date(
                "https://kind.krx.co.kr/external/2026/07/16/001066/"
                "20260716002384/10001.htm"
            ),
            date(2026, 7, 16),
        )
        self.assertIsNone(
            infer_source_locator_publication_date(
                "https://issuer.example/certificate-20231015-20261014.pdf"
            )
        )

    def test_publication_metadata_accepts_english_month_name_date(self) -> None:
        self.assertEqual(
            infer_publication_date(
                explicit=None,
                metadata_parts=(
                    "SINGLE_ARTICLE_DATE:April 22, 2026",
                ),
                as_of_date=date(2026, 7, 12),
            ),
            date(2026, 4, 22),
        )
        self.assertEqual(
            infer_publication_date(
                explicit=None,
                metadata_parts=(
                    "HTML_META_datepublished:22 Apr 2026",
                ),
                as_of_date=date(2026, 7, 12),
            ),
            date(2026, 4, 22),
        )

    def test_leading_press_release_accepts_standalone_english_date(self) -> None:
        self.assertEqual(
            infer_publication_date(
                explicit=None,
                metadata_parts=(),
                document_text=(
                    "Official Newsroom\n"
                    "Press Release\n"
                    "Share\nTweet\nLinkedIn\nEmail\n"
                    "Current Corp and Partner Announce Technology Partnership\n"
                    "Collaboration Supports Next-Generation Systems\n"
                    "June 7, 2026\n"
                    "News Summary:\n"
                    "The companies announced a multiyear collaboration.\n"
                ),
                as_of_date=date(2026, 7, 12),
            ),
            date(2026, 6, 7),
        )

    def test_navigation_heavy_press_release_details_accepts_date(self) -> None:
        self.assertEqual(
            infer_publication_date(
                explicit=None,
                metadata_parts=(),
                document_text=(
                    _navigation_heavy_press_release_details_text()
                ),
                as_of_date=date(2026, 7, 12),
            ),
            date(2025, 10, 31),
        )

    def test_press_release_details_stops_before_more_news_footer(self) -> None:
        self.assertIsNone(
            infer_publication_date(
                explicit=None,
                metadata_parts=(),
                document_text=(
                    "Press Release Details\n"
                    + "\n".join(
                        f"Investor navigation item {index}"
                        for index in range(30)
                    )
                    + "\nMore News\n"
                    "Another Company Announces a Product\n"
                    "November 14, 2025\n"
                ),
                as_of_date=date(2026, 7, 12),
            )
        )

    def test_press_release_details_view_all_news_date_needs_download_marker(
        self,
    ) -> None:
        self.assertIsNone(
            infer_publication_date(
                explicit=None,
                metadata_parts=(),
                document_text=(
                    "Press Release Details\n"
                    + "\n".join(
                        f"Investor navigation item {index}"
                        for index in range(30)
                    )
                    + "\nView all news\n"
                    "Related Company Announces a Product\n"
                    "July 29, 2026\n"
                    "Read the related article\n"
                ),
                as_of_date=date(2026, 7, 12),
            )
        )

    def test_press_release_details_stops_before_related_sections(self) -> None:
        for related_heading in (
            "Related Articles",
            "Related Press Releases",
        ):
            with self.subTest(related_heading=related_heading):
                self.assertIsNone(
                    infer_publication_date(
                        explicit=None,
                        metadata_parts=(),
                        document_text=(
                            "Press Release Details\n"
                            "Current release has no visible date\n"
                            f"{related_heading}\n"
                            "Related Company Announces a Product\n"
                            "July 29, 2026\n"
                            "Download this Press Release\n"
                        ),
                        as_of_date=date(2026, 7, 12),
                    )
                )

    def test_release_footer_more_news_date_is_not_publication_date(self) -> None:
        self.assertIsNone(
            infer_publication_date(
                explicit=None,
                metadata_parts=(),
                document_text=(
                    "Official Newsroom\n"
                    "Press Release\n"
                    "Current Corp Announces Technology Partnership\n"
                    "News Summary:\n"
                    "The full release contains no visible publication date.\n"
                    "More News\n"
                    "Another Company Announces a Product\n"
                    "July 29, 2026\n"
                ),
                as_of_date=date(2026, 7, 12),
            )
        )

    def test_release_head_fallback_does_not_override_metadata_date(self) -> None:
        self.assertEqual(
            infer_publication_date(
                explicit=None,
                metadata_parts=(
                    "JSON_LD_DATE_PUBLISHED:2026-06-06",
                ),
                document_text=(
                    "Official Newsroom\n"
                    "Press Release\n"
                    "Current Corp Announces Technology Partnership\n"
                    "June 7, 2026\n"
                    "News Summary:\n"
                ),
                as_of_date=date(2026, 7, 12),
            ),
            date(2026, 6, 6),
        )

    def test_operational_phase85_audit_is_reproducible_and_complete(self) -> None:
        actual = compile_phase85_source_graph_acquisition_audit(self.ROOT)
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_source_graph_acquisition_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, committed)
        self.assertEqual(actual["status"], PHASE85_PASS)
        self.assertEqual(actual["critical_count_sum"], 0)
        self.assertEqual(
            actual["default_config"]["max_results_per_query"], 100
        )
        self.assertNotIn("top_results", actual["default_config"])
        self.assertFalse(actual["snippet_is_evidence"])

    def test_seed_hint_prioritizes_but_does_not_narrow_broad_source_graph(self) -> None:
        plan = ComponentResearchPlan(
            plan_id="PLAN-1",
            target_id=TARGET,
            archetype_id="GENERIC-ARCHETYPE",
            component_id="eps_fcf_explosion",
            researcher_role="EPSFCFResearcher",
            component_max_points=20.0,
            research_questions=(
                "earnings conversion",
                "counter capacity expansion",
                "superseding customer terms",
            ),
            source_route_hints=("issuer_ir",),
            counter_route_hints=("earnings_counter",),
            structured_metric_requirements=(),
            candidate_fact_ids=(),
            candidate_anchor_ids=(),
        )
        graph = SourceGraphExplorer().explore(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            documents=(),
            research_plans=(plan,),
            source_coverage=(),
        )
        self.assertEqual(len(graph.open_objectives), 1)
        self.assertIn(
            "not independent checklist gates",
            graph.open_objectives[0].research_objective,
        )
        families = graph.open_objectives[0].preferred_source_families
        self.assertEqual(families[0], "ISSUER_PRESENTATION")
        self.assertTrue(
            {"OPENDART", "FINANCIAL_STATEMENTS", "REUTERS"}.issubset(families)
        )

    def test_llm_query_is_forwarded_verbatim_and_only_full_fetch_is_evidence(self) -> None:
        provider = SourceBrainProvider(material_titles=("material",))
        search = RecordingSearchProvider(
            {
                QUERY: (
                    _result("irrelevant market list", "https://example.com/list", rank=1),
                    _result("Current Corp material report", "https://example.com/report", rank=99),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                "https://example.com/report": _document_text("material")
            }
        )
        run = self._run(provider=provider, search=search, fetcher=fetcher)
        self.assertEqual(search.calls, [(QUERY, AS_OF_DATE, 100)])
        self.assertEqual(len(run.evidence_documents), 1)
        document = run.evidence_documents[0]
        self.assertTrue(document["full_fetch_performed"])
        self.assertFalse(document["snippet_used_as_document"])
        self.assertFalse(document["parser_field_direct_score_authority"])
        self.assertEqual(document["canonical_url"], "https://example.com/report")
        candidates = run.checkpoint["search_candidates"]
        self.assertTrue(all(row["snippet_discovery_only"] for row in candidates))
        self.assertTrue(all(not row["snippet_evidence_eligible"] for row in candidates))
        relationships = {row.relationship for row in run.source_graph.edges}
        self.assertIn("DISCOVERED", relationships)
        self.assertIn("FULL_FETCH_OF", relationships)
        self.assertEqual(run.audit["critical_count_sum"], 0)

    def test_invalid_candidate_ids_are_reprompted_without_deterministic_coercion(
        self,
    ) -> None:
        provider = InvalidThenCorrectRankingProvider()
        url = "https://example.com/retry-ranking"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {QUERY: (_result("Current Corp material", url),)}
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={url: _document_text("ranking-retry")}
            ),
        )
        self.assertEqual(provider.ranking_call_count, 2)
        self.assertEqual(len(provider.invalidations), 1)
        self.assertIn("unknown or duplicate id", provider.invalidations[0])
        self.assertEqual(len(run.evidence_documents), 1)
        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        retry = ranking_payloads[-1]["ranking_retry_context"]
        self.assertIn("unknown or duplicate id", retry["validation_error"])
        self.assertEqual(
            retry["required_candidate_ids"],
            [run.checkpoint["search_candidates"][0]["candidate_id"]],
        )
        self.assertNotIn(
            "UNKNOWN-CANDIDATE",
            {row["candidate_id"] for row in run.checkpoint["candidate_materiality_decisions"]},
        )

    def test_complete_candidate_roster_with_false_completion_is_reprompted(
        self,
    ) -> None:
        provider = IncompleteThenCorrectRankingProvider()
        url = "https://example.com/incomplete-ranking"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {QUERY: (_result("Current Corp material", url),)}
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={url: _document_text("ranking-retry")}
            ),
        )
        self.assertEqual(provider.ranking_call_count, 2)
        self.assertEqual(len(provider.invalidations), 1)
        self.assertIn("declared incomplete", provider.invalidations[0])
        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        retry = ranking_payloads[-1]["ranking_retry_context"]
        self.assertIn("declared incomplete", retry["validation_error"])
        self.assertIn(
            "every discovery candidate was classified",
            retry["instruction"],
        )
        self.assertEqual(len(run.evidence_documents), 1)
        self.assertEqual(
            len(run.checkpoint["candidate_materiality_decisions"]),
            1,
        )

    def test_second_false_flag_is_reconciled_only_for_complete_roster(
        self,
    ) -> None:
        provider = RepeatedIncompleteCompleteRosterProvider()
        candidates = tuple(
            {
                "candidate_id": f"RECONCILE-CANDIDATE-{index}",
                "title": f"Current Corp candidate {index}",
                "url": f"https://example.com/reconcile-{index}",
                "snippet": "discovery only",
                "source": "fixture-search",
                "published_at": "2026-06-20",
                "is_pdf": False,
                "is_news": False,
                "is_disclosure": False,
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
                "requested_source_families": ["NAVER_DISCOVERY"],
            }
            for index in range(4)
        )

        result = ResearcherDocumentRanker(provider=provider).rank_candidates(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            open_objectives=[_objective().to_dict()],
            candidates=candidates,
            current_evidence_facts=(),
            target_business_model=None,
            source_coverage=(),
        )

        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(len(result.decisions), len(candidates))
        self.assertTrue(result.completion_flag_reconciled)
        self.assertEqual(provider.ranking_call_count, 2)
        self.assertEqual(len(provider.invalidations), 1)
        retry = provider.calls[-1]["payload"]["ranking_retry_context"]
        self.assertIn(
            "every discovery candidate was classified",
            retry["instruction"],
        )

    def test_repeated_large_roster_omission_splits_and_recombines_every_candidate(
        self,
    ) -> None:
        provider = SplitRecoveryRankingProvider()
        rows = tuple(
            _result(
                f"Current Corp split candidate {index}",
                f"https://example.com/split-{index}",
                rank=index + 1,
            )
            for index in range(4)
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider({QUERY: rows}),
            fetcher=PageFetcher(
                fixture_text_by_url={
                    row.url: _document_text(f"split-{index}")
                    for index, row in enumerate(rows)
                }
            ),
        )
        self.assertEqual(provider.ranking_batch_sizes, [4, 4, 2, 2])
        self.assertEqual(len(provider.invalidations), 2)
        self.assertEqual(len(run.checkpoint["candidate_materiality_decisions"]), 4)
        self.assertEqual(len(run.evidence_documents), 4)
        self.assertEqual(
            {
                row["candidate_id"]
                for row in run.checkpoint["candidate_materiality_decisions"]
            },
            {
                row["candidate_id"]
                for row in run.checkpoint["search_candidates"]
            },
        )
        self.assertFalse(
            any(
                "SEMANTIC_RANKING_SPLIT_PENDING" in reason
                for reason in run.checkpoint["pending_reasons"]
            )
        )

    def test_ollama_sized_candidate_roster_is_partitioned_before_transport(
        self,
    ) -> None:
        provider = SourceBrainProvider()
        provider.semantic_prompt_chunk_chars = 10_000
        candidates = tuple(
            {
                "candidate_id": f"CANDIDATE-{index}",
                "title": f"Current Corp candidate {index}",
                "url": f"https://example.com/candidate-{index}",
                "snippet": "긴 검색 발견 메타데이터 " * 150,
                "source": "fixture-search",
                "published_at": "2026-06-20",
                "is_pdf": False,
                "is_news": False,
                "is_disclosure": False,
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
                "requested_source_families": ["NAVER_DISCOVERY"],
            }
            for index in range(8)
        )

        result = ResearcherDocumentRanker(provider=provider).rank_candidates(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            open_objectives=[_objective().to_dict()],
            candidates=candidates,
            current_evidence_facts=(),
            target_business_model=None,
            source_coverage=(),
        )

        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(len(result.decisions), len(candidates))
        emitted_ids = [
            row["candidate_id"]
            for payload in ranking_payloads
            for row in payload["discovery_candidates"]
        ]
        self.assertEqual(
            sorted(emitted_ids),
            sorted(row["candidate_id"] for row in candidates),
        )
        self.assertEqual(len(emitted_ids), len(set(emitted_ids)))
        self.assertGreater(len(ranking_payloads), 1)
        self.assertTrue(
            all(
                len(
                    json.dumps(
                        payload,
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    )
                )
                <= provider.semantic_prompt_chunk_chars
                for payload in ranking_payloads
            )
        )

    def test_candidate_count_pages_do_not_inherit_fact_chunk_limit(self) -> None:
        provider = SourceBrainProvider()
        provider.semantic_prompt_chunk_chars = 10_000
        provider.candidate_ranking_prompt_chunk_chars = 100_000
        provider.candidate_ranking_page_candidate_limit = 3
        candidates = tuple(
            {
                "candidate_id": f"COUNT-CANDIDATE-{index}",
                "title": f"Current Corp count candidate {index}",
                "url": f"https://example.com/count-candidate-{index}",
                "snippet": "lossless candidate roster",
                "source": "fixture-search",
                "published_at": "2026-06-20",
                "is_pdf": False,
                "is_news": False,
                "is_disclosure": False,
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
                "requested_source_families": ["NAVER_DISCOVERY"],
            }
            for index in range(8)
        )

        result = ResearcherDocumentRanker(provider=provider).rank_candidates(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            open_objectives=[_objective().to_dict()],
            candidates=candidates,
            current_evidence_facts=(),
            target_business_model=None,
            source_coverage=(),
        )

        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(len(result.decisions), len(candidates))
        self.assertGreater(len(ranking_payloads), 1)
        self.assertTrue(
            all(
                len(payload["discovery_candidates"]) <= 3
                for payload in ranking_payloads
            )
        )
        self.assertEqual(
            {
                row["candidate_id"]
                for payload in ranking_payloads
                for row in payload["discovery_candidates"]
            },
            {row["candidate_id"] for row in candidates},
        )

    def test_codex_candidate_ranking_pages_match_output_schema_limit(
        self,
    ) -> None:
        class RecordingCodexProvider(CodexResearcherProvider):
            def complete(self, *, pass_name, payload):
                self.calls.append(
                    {"pass_name": pass_name, "payload": payload}
                )
                rows = list(payload["discovery_candidates"])
                return {
                    "decisions": [
                        {
                            "candidate_id": row["candidate_id"],
                            "material_relevance": True,
                            "priority": 1.0,
                            "objective_ids": list(row["objective_ids"]),
                            "matched_requested_source_family": next(
                                iter(
                                    row.get(
                                        "requested_source_families"
                                    )
                                    or ()
                                ),
                                "NONE",
                            ),
                            "rationale": "Codex 공통 페이지의 후보를 전수 분류했다.",
                        }
                        for row in rows
                    ],
                    "ranking_complete": True,
                    "unresolved_notes": [],
                }

        provider = RecordingCodexProvider(transport=object())  # type: ignore[arg-type]
        candidates = tuple(
            {
                "candidate_id": f"CODEX-CANDIDATE-{index}",
                "title": f"Current Corp Codex candidate {index}",
                "url": f"https://example.com/codex-candidate-{index}",
                "snippet": "lossless Codex candidate roster",
                "source": "fixture-search",
                "published_at": "2026-06-20",
                "is_pdf": False,
                "is_news": False,
                "is_disclosure": False,
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
                "requested_source_families": ["NAVER_DISCOVERY"],
            }
            for index in range(100)
        )

        result = ResearcherDocumentRanker(provider=provider).rank_candidates(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            open_objectives=[_objective().to_dict()],
            candidates=candidates,
            current_evidence_facts=(),
            target_business_model=None,
            source_coverage=(),
        )

        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(len(ranking_payloads), 9)
        self.assertTrue(
            all(
                len(payload["discovery_candidates"])
                <= provider.candidate_ranking_page_candidate_limit
                for payload in ranking_payloads
            )
        )
        emitted_ids = [
            row["candidate_id"]
            for payload in ranking_payloads
            for row in payload["discovery_candidates"]
        ]
        self.assertEqual(
            emitted_ids,
            [row["candidate_id"] for row in candidates],
        )
        self.assertEqual(len(emitted_ids), len(set(emitted_ids)))

    def test_empty_or_duplicate_llm_query_is_pending_without_fallback(self) -> None:
        provider = SourceBrainProvider(queries=())
        search = RecordingSearchProvider({})
        run = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={}),
        )
        self.assertEqual(run.status, "QUERY_GENERATION_PENDING")
        self.assertEqual(search.calls, [])
        self.assertFalse(
            run.query_generation.deterministic_fallback_query_used  # type: ignore[union-attr]
        )
        duplicate_provider = SourceBrainProvider(queries=(QUERY,))
        result = ResearcherSourceQueryPlanner(provider=duplicate_provider).generate(
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            as_of_date=AS_OF_DATE,
            open_objectives=[_objective().to_dict()],
            current_evidence_facts=(),
            current_counterfacts=(),
            target_business_model=None,
            source_coverage=(),
            prior_query_failures=(),
            previously_executed_queries=(QUERY,),
            theme_context={},
            score_gap_context={},
            generator_kind="TEST_FIXTURE_LLM",
        )
        self.assertEqual(result.status, "PENDING")
        self.assertIn("DUPLICATE_OR_ALREADY_EXECUTED_QUERY", result.feedback_for_next_llm_call[0])

    def test_query_prompt_hash_stays_stable_while_collaboration_response_waits(
        self,
    ) -> None:
        provider = SourceBrainProvider()
        request_a = "COLLABREQ-" + "a" * 64
        request_b = "COLLABREQ-" + "b" * 64
        real_failure = {
            "failure_stage": "FULL_DOCUMENT_FETCH",
            "failure_reason": "FETCH_TIMEOUT",
            "objective_id": _objective().objective_id,
            "query_id": "QUERY-REAL",
        }
        wait_a = {
            "failure_reason": (
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:"
                + request_a
            ),
            "objective_id": "MULTI_OBJECTIVE",
            "query_id": "QUERY_GENERATION",
        }
        wait_b = {
            "failure_reason": (
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:"
                + request_b
            ),
            "objective_id": "MULTI_OBJECTIVE",
            "query_id": "QUERY_GENERATION",
        }
        common = {
            "target_id": TARGET,
            "target_name": TARGET_NAME,
            "target_aliases": (),
            "as_of_date": AS_OF_DATE,
            "open_objectives": [_objective().to_dict()],
            "current_evidence_facts": (),
            "current_counterfacts": (),
            "target_business_model": None,
            "source_coverage": (),
            "previously_executed_queries": (),
            "theme_context": {},
            "generator_kind": "TEST_FIXTURE_LLM",
        }

        def score_gap_context(request_id: str) -> Mapping[str, Any]:
            supervisor_wait = (
                "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderUnavailable:"
                "COLLABORATION_RESPONSE_PENDING:"
                + request_id
            )
            return {
                "prior_fact_extraction_feedback": [
                    "UNRESOLVED_RESEARCH_NOTE:peer band source가 필요하다.",
                    (
                        "FACT_EXTRACTION_RETRY_CONTEXT:"
                        "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                        "StructuredProviderUnavailable:"
                        "COLLABORATION_RESPONSE_PENDING:"
                        + request_id
                    ),
                ],
                "prior_supervisor_gap": {
                    "unresolved_material_questions": [
                        supervisor_wait,
                        "PEER_BAND를 확인해야 한다.",
                    ],
                },
                "prior_research_epoch": {
                    "unresolved_material_questions": [
                        supervisor_wait,
                        "PEER_BAND를 확인해야 한다.",
                    ],
                },
            }

        first = ResearcherSourceQueryPlanner(provider=provider).generate(
            **common,
            prior_query_failures=(real_failure, wait_a),
            score_gap_context=score_gap_context(request_a),
        )
        repeated_wait = ResearcherSourceQueryPlanner(provider=provider).generate(
            **common,
            prior_query_failures=(
                real_failure,
                wait_a,
                wait_b,
                wait_b,
            ),
            score_gap_context=score_gap_context(request_b),
        )
        changed_real_failure = ResearcherSourceQueryPlanner(
            provider=provider
        ).generate(
            **common,
            prior_query_failures=(
                {
                    **real_failure,
                    "failure_reason": "HTTP_503",
                },
                wait_b,
            ),
            score_gap_context=score_gap_context(request_b),
        )

        query_payloads = [
            call["payload"]
            for call in provider.calls
            if call["pass_name"] == "SOURCE_QUERY_GENERATION"
        ]
        self.assertEqual(query_payloads[0], query_payloads[1])
        self.assertEqual(first.prompt_hash, repeated_wait.prompt_hash)
        self.assertNotEqual(query_payloads[1], query_payloads[2])
        self.assertNotEqual(
            repeated_wait.prompt_hash,
            changed_real_failure.prompt_hash,
        )

    def test_pending_query_response_survives_downstream_gap_projection_loss(
        self,
    ) -> None:
        provider = PendingThenCompleteQueryProvider()
        search = RecordingSearchProvider({QUERY: ()})
        gap_context = {
            "prior_supervisor_gap": {
                "status": "NEXT_RESEARCH_REQUIRED",
                "missing_material_facts": [
                    {
                        "objective_id": "OBJECTIVE-1",
                        "component_id": "eps_fcf_explosion",
                        "missing_fact": "counterparty official confirmation",
                    }
                ],
                "new_source_family_directions": [
                    {
                        "objective_id": "OBJECTIVE-1",
                        "component_id": "eps_fcf_explosion",
                        "source_family": "CUSTOMER_OFFICIAL",
                        "direction": "check the named counterparty catalog",
                    }
                ],
                "query_direction_briefs": [
                    {
                        "objective_id": "OBJECTIVE-1",
                        "component_id": "eps_fcf_explosion",
                        "source_family": "CUSTOMER_OFFICIAL",
                        "direction": "check the named counterparty catalog",
                    }
                ],
            }
        }
        first = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={}),
            score_gap_context=gap_context,
        )
        self.assertEqual(first.status, "QUERY_GENERATION_PENDING")
        self.assertEqual(search.calls, [])
        replay = first.checkpoint[
            "pending_query_generation_replay_context"
        ]
        self.assertEqual(
            replay["unresolved_objective_ids"], ["OBJECTIVE-1"]
        )
        first_payload = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_QUERY_GENERATION"
        ][-1]

        # Simulate the real async race: the downstream component/supervisor
        # projection temporarily loses the material gap and marks the
        # objective resolved before the collaboration response is consumed.
        provider.query_pending = False
        second = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=first.checkpoint,
            score_gap_context={},
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        query_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_QUERY_GENERATION"
        ]
        self.assertEqual(len(query_payloads), 2)
        self.assertEqual(query_payloads[0], query_payloads[1])
        self.assertEqual(search.calls[0][0], QUERY)
        self.assertTrue(
            second.audit[
                "pending_query_generation_replay_context_consumed"
            ]
        )
        self.assertNotIn(
            "pending_query_generation_replay_context", second.checkpoint
        )

    def test_query_replay_dedupe_preserves_distinct_failure_lineage(
        self,
    ) -> None:
        rows = [
            {
                "query_id": "QUERY-1",
                "candidate_id": "CANDIDATE-1",
                "document_id": "DOCUMENT-1",
                "objective_id": "OBJECTIVE-1",
                "failure_reason": "FETCH_TIMEOUT",
            },
            {
                "query_id": "QUERY-1",
                "candidate_id": "CANDIDATE-2",
                "document_id": "DOCUMENT-2",
                "objective_id": "OBJECTIVE-1",
                "failure_reason": "FETCH_TIMEOUT",
            },
        ]

        deduped = source_graph_module._dedupe_exact_mapping_rows(
            [rows[0], rows[1], dict(rows[0])]
        )

        self.assertEqual(len(deduped), 2)
        self.assertEqual(
            {row["candidate_id"] for row in deduped},
            {"CANDIDATE-1", "CANDIDATE-2"},
        )

    def test_query_replay_keeps_gap_after_empty_collaboration_response(
        self,
    ) -> None:
        provider = PendingThenCompleteQueryProvider(queries=())
        search = RecordingSearchProvider({QUERY: ()})
        gap_context = {
            "prior_supervisor_gap": {
                "status": "NEXT_RESEARCH_REQUIRED",
                "new_source_family_directions": [
                    {
                        "objective_id": "OBJECTIVE-1",
                        "component_id": "eps_fcf_explosion",
                        "source_family": "CUSTOMER_OFFICIAL",
                        "direction": "check counterparty official material",
                    }
                ],
            }
        }
        first = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={}),
            score_gap_context=gap_context,
        )
        self.assertEqual(first.status, "QUERY_GENERATION_PENDING")

        provider.query_pending = False
        empty = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=first.checkpoint,
            score_gap_context={},
            resolved_objective_ids=("OBJECTIVE-1",),
        )
        self.assertEqual(empty.status, "QUERY_GENERATION_PENDING")
        self.assertEqual(
            empty.checkpoint["pending_query_generation_replay_context"][
                "replay_phase"
            ],
            "POST_RESPONSE_SEMANTIC_RETRY",
        )
        self.assertEqual(search.calls, [])

        provider.queries = (QUERY,)
        completed = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=empty.checkpoint,
            score_gap_context={},
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        query_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_QUERY_GENERATION"
        ]
        self.assertEqual(len(query_payloads), 3)
        self.assertEqual(query_payloads[0], query_payloads[1])
        self.assertNotEqual(query_payloads[1], query_payloads[2])
        self.assertEqual(search.calls[0][0], QUERY)
        self.assertNotIn(
            "pending_query_generation_replay_context",
            completed.checkpoint,
        )

    def test_future_dated_llm_query_is_rejected_before_search(self) -> None:
        provider = SourceBrainProvider(
            queries=("Current Corp report published 2026-06-30",)
        )
        search = RecordingSearchProvider({})
        run = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={}),
        )
        self.assertEqual(run.status, "QUERY_GENERATION_PENDING")
        self.assertEqual(search.calls, [])
        self.assertIn(
            "FUTURE_DATE_QUERY",
            run.query_generation.feedback_for_next_llm_call[0],  # type: ignore[union-attr]
        )

    def test_empty_query_feedback_is_reprompted_on_resume_without_template(self) -> None:
        provider = AdaptiveSourceBrainProvider()
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp material", "https://example.com/new"),)}
        )
        fetcher = PageFetcher(
            fixture_text_by_url={"https://example.com/new": _document_text("new")}
        )
        first = self._run(provider=provider, search=search, fetcher=fetcher)
        self.assertEqual(first.status, "QUERY_GENERATION_PENDING")
        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=first.checkpoint,
        )
        self.assertEqual(provider.query_call_count, 2)
        self.assertEqual(search.calls[0][0], QUERY)
        query_payload = [
            call["payload"]
            for call in provider.calls
            if call["pass_name"] == "SOURCE_QUERY_GENERATION"
        ][-1]
        failure_projection = query_payload["prior_query_or_source_failures"]
        self.assertGreater(failure_projection["failure_count"], 0)
        self.assertTrue(
            any(
                "LLM_RETURNED_NO_NEW_VALID_QUERY"
                in str(row.get("failure_reason") or "")
                for row in failure_projection["failures"]
            )
        )
        self.assertEqual(len(second.evidence_documents), 1)

    def test_future_result_and_fetch_failure_never_promote_snippet(self) -> None:
        provider = SourceBrainProvider()
        search = RecordingSearchProvider(
            {
                QUERY: (
                    _result(
                        "Current Corp future",
                        "https://example.com/future",
                        published="2026-06-30",
                    ),
                    _result(
                        "Current Corp future DART locator",
                        (
                            "https://englishdart.fss.or.kr/dsbh001/main.do"
                            "?rcpNo=20260716000552"
                        ),
                        published=None,
                    ),
                    _result("Current Corp current", "https://example.com/missing"),
                )
            }
        )
        run = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={}),
        )
        self.assertEqual(run.evidence_documents, ())
        reasons = {
            row["rejection_reason"]
            for row in run.checkpoint["rejected_documents"]
        }
        self.assertIn("FUTURE_SEARCH_RESULT", reasons)
        self.assertIn("FUTURE_CANDIDATE_SOURCE_LOCATOR_DATE", reasons)
        future_locator = next(
            row
            for row in run.checkpoint["search_candidates"]
            if "rcpNo=20260716000552" in str(row.get("url") or "")
        )
        self.assertEqual(future_locator["ranking_status"], "REJECTED_FUTURE")
        self.assertEqual(future_locator["fetch_status"], "FETCH_REJECTED")
        self.assertTrue(future_locator["future_candidate_rejected_before_llm"])
        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertTrue(
            all(
                "20260716000552"
                not in json.dumps(payload, ensure_ascii=False)
                for payload in ranking_payloads
            )
        )
        self.assertTrue(
            any(reason.startswith("SNIPPET_ONLY_FULL_FETCH_REQUIRED") for reason in reasons)
        )
        self.assertEqual(run.audit["critical_counts"]["snippet_evidence_document_count"], 0)

    def test_repeated_identical_fetch_failure_returns_to_llm_for_alternate_route(
        self,
    ) -> None:
        provider = AlternateRouteSourceBrainProvider()
        search = RecordingSearchProvider(
            {
                QUERY: (_result("Current Corp TLS report", FAILED_URL),),
                ALTERNATE_QUERY: (
                    _result(
                        "Current Corp official mirror",
                        ALTERNATE_URL,
                        query=ALTERNATE_QUERY,
                    ),
                ),
            }
        )
        fetcher = SelectiveRetryFailureFetcher()

        first = self._run(provider=provider, search=search, fetcher=fetcher)
        failed_candidate = first.checkpoint["search_candidates"][0]
        self.assertEqual(failed_candidate["fetch_status"], "FETCH_RETRY_PENDING")

        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=first.checkpoint,
        )
        failed_candidate = next(
            row
            for row in second.checkpoint["search_candidates"]
            if row["url"] == FAILED_URL
        )
        self.assertEqual(failed_candidate["fetch_status"], "FETCH_ROUTE_EXHAUSTED")
        self.assertTrue(failed_candidate["alternate_route_required"])
        self.assertFalse(second.checkpoint["semantic_saturation_certified"])
        self.assertTrue(
            any(
                row.get("alternate_route_required") is True
                for row in second.checkpoint["query_failures"]
            )
        )

        third = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=second.checkpoint,
        )
        self.assertEqual(provider.query_call_count, 2)
        self.assertEqual([row[0] for row in search.calls], [QUERY, ALTERNATE_QUERY])
        self.assertEqual(len(third.evidence_documents), 1)
        self.assertEqual(
            third.evidence_documents[0]["canonical_url"], ALTERNATE_URL
        )
        query_payload = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_QUERY_GENERATION"
        ][-1]
        self.assertTrue(
            any(
                row.get("alternate_route_required") is True
                for row in query_payload["prior_query_or_source_failures"][
                    "failures"
                ]
            )
        )

    def test_checkpoint_resume_fetches_every_material_candidate_without_research_completion(self) -> None:
        provider = SourceBrainProvider()
        results = tuple(
            _result(
                f"Current Corp material {index}",
                f"https://example.com/{index}",
                rank=index,
            )
            for index in range(5)
        )
        search = RecordingSearchProvider({QUERY: results})
        fetcher = PageFetcher(
            fixture_text_by_url={
                row.url: _document_text(f"unique-{index}")
                for index, row in enumerate(results)
            }
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=5,
            max_fetches_per_checkpoint=2,
        )
        run1 = self._run(
            provider=provider, search=search, fetcher=fetcher, config=config
        )
        self.assertEqual(run1.status, "CHECKPOINT_PENDING")
        self.assertEqual(len(run1.evidence_documents), 2)
        run2 = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=run1.checkpoint,
        )
        self.assertEqual(len(run2.evidence_documents), 4)
        run3 = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=run2.checkpoint,
        )
        self.assertEqual(len(run3.evidence_documents), 5)
        self.assertEqual(run3.status, "EPOCH_COMPLETE_REQUIRES_SUPERVISOR")
        self.assertFalse(run3.checkpoint["semantic_saturation_certified"])
        self.assertEqual(len(search.calls), 1)
        self.assertEqual(
            sum(call["pass_name"] == "SOURCE_QUERY_GENERATION" for call in provider.calls),
            1,
        )
        with tempfile.TemporaryDirectory() as directory:
            paths = write_source_graph_acquisition_run(run3, output_root=directory)
            loaded = load_source_graph_checkpoint(paths["checkpoint"])
            self.assertEqual(loaded["checkpoint_hash"], run3.checkpoint["checkpoint_hash"])

    def test_collaboration_pending_ranking_replays_after_resolved_and_fetches(
        self,
    ) -> None:
        provider = PendingThenCompleteRankingProvider(
            queries=(QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        url = "https://customer.example.com/current-official-platform"
        search = RecordingSearchProvider(
            {
                QUERY: (
                    _result(
                        "Current Corp customer official platform",
                        url,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: _document_text("customer-official-platform")
            }
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=1,
            max_fetches_per_checkpoint=1,
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
        )

        self.assertEqual(first.status, "CANDIDATE_RANKING_PENDING")
        first_context = first.checkpoint[
            "pending_candidate_ranking_replay_context"
        ]
        self.assertEqual(
            first_context["replay_phase"],
            "AWAITING_COLLABORATION_RESPONSE",
        )
        first_ranking_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )

        provider.ranking_pending = False
        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=first.checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(len(ranking_payloads), 2)
        self.assertEqual(ranking_payloads[-1], first_ranking_payload)
        candidate = second.checkpoint["search_candidates"][0]
        self.assertEqual(candidate["ranking_status"], "MATERIAL")
        self.assertEqual(
            candidate["fetch_status"],
            "FULL_DOCUMENT_FETCHED",
        )
        self.assertEqual(candidate["full_fetch_attempt_count"], 1)
        self.assertEqual(len(second.evidence_documents), 1)
        self.assertEqual(second.status, "STOPPED_ON_RESOLUTION")
        self.assertNotIn(
            "pending_candidate_ranking_replay_context",
            second.checkpoint,
        )

    def test_collaboration_ranking_prompt_lineage_allows_a_b_a_revisit(
        self,
    ) -> None:
        request_ids = tuple(
            "COLLABREQ-" + value * 64 for value in ("a", "b", "c")
        )
        provider = EpochPendingRankingProvider(
            pending_request_ids=request_ids,
            queries=(QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        url = "https://customer.example.com/prompt-lineage-official"
        search = RecordingSearchProvider(
            {
                QUERY: (
                    _result(
                        "Current Corp prompt lineage official",
                        url,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={url: _document_text("prompt-lineage")}
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=1,
            max_fetches_per_checkpoint=1,
        )
        business_model_a = {"revenue_model": "capacity hardware"}
        business_model_b = {"revenue_model": "recurring service"}

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            target_business_model=business_model_a,
            source_coverage=(),
        )
        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=first.checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
            target_business_model=business_model_b,
            source_coverage=("ISSUER_FILING",),
        )
        third = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=second.checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
            target_business_model=business_model_a,
            source_coverage=(),
        )

        first_context = first.checkpoint[
            "pending_candidate_ranking_replay_context"
        ]
        second_context = second.checkpoint[
            "pending_candidate_ranking_replay_context"
        ]
        third_context = third.checkpoint[
            "pending_candidate_ranking_replay_context"
        ]
        self.assertNotEqual(
            first_context["prompt_hash"],
            second_context["prompt_hash"],
        )
        self.assertEqual(
            third_context["prompt_hash"],
            first_context["prompt_hash"],
        )
        self.assertEqual(
            third_context["prompt_hash_lineage"],
            [first_context["prompt_hash"], second_context["prompt_hash"]],
        )
        self.assertEqual(
            third_context["collaboration_request_ids"],
            list(request_ids),
        )

        completed = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=third.checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
            target_business_model=business_model_a,
            source_coverage=(),
        )

        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(len(ranking_payloads), 4)
        self.assertEqual(ranking_payloads[0], ranking_payloads[2])
        self.assertEqual(ranking_payloads[2], ranking_payloads[3])
        self.assertNotEqual(ranking_payloads[0], ranking_payloads[1])
        self.assertEqual(completed.status, "STOPPED_ON_RESOLUTION")
        self.assertEqual(len(completed.evidence_documents), 1)
        self.assertNotIn(
            "pending_candidate_ranking_replay_context",
            completed.checkpoint,
        )

    def test_collaboration_ranking_replay_survives_migration_only_resume(
        self,
    ) -> None:
        provider = PendingThenCompleteRankingProvider(
            queries=(QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        url = "https://customer.example.com/migration-replay-official"
        search = RecordingSearchProvider(
            {
                QUERY: (
                    _result(
                        "Current Corp migration replay official",
                        url,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={url: _document_text("migration-replay")}
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=1,
            max_fetches_per_checkpoint=1,
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
        )
        provider_call_count = len(provider.calls)
        migrated = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=first.checkpoint,
            checkpoint_migration_only=True,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        self.assertEqual(len(provider.calls), provider_call_count)
        self.assertEqual(migrated.status, "CANDIDATE_RANKING_PENDING")
        self.assertTrue(migrated.audit["checkpoint_migration_only"])
        self.assertEqual(
            migrated.checkpoint[
                "pending_candidate_ranking_replay_context"
            ],
            first.checkpoint["pending_candidate_ranking_replay_context"],
        )
        self.assertTrue(
            all(
                row["ranking_status"] == "PENDING"
                for row in migrated.checkpoint["search_candidates"]
            )
        )

        provider.ranking_pending = False
        completed = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=migrated.checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        self.assertEqual(completed.status, "STOPPED_ON_RESOLUTION")
        self.assertEqual(len(completed.evidence_documents), 1)
        self.assertNotIn(
            "pending_candidate_ranking_replay_context",
            completed.checkpoint,
        )

    def test_collaboration_ranking_replay_uses_prompt_semantic_candidate_hash(
        self,
    ) -> None:
        provider = PendingThenCompleteRankingProvider(
            queries=(QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        url = "https://customer.example.com/semantic-replay-official"
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp semantic replay", url),)}
        )
        fetcher = PageFetcher(
            fixture_text_by_url={url: _document_text("semantic-replay")}
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=1,
            max_fetches_per_checkpoint=1,
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
        )
        state = json.loads(json.dumps(first.checkpoint))
        state.pop("checkpoint_id")
        state.pop("checkpoint_hash")
        candidate = state["search_candidates"][0]
        prompt_query_ids = list(candidate["materiality_query_ids"])
        candidate["query_ids"].append("SGQUERY-HISTORICAL-AUDIT-ONLY")
        checkpoint = source_graph_module._finalize_checkpoint(state)

        provider.ranking_pending = False
        completed = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        self.assertEqual(
            completed.ranking_results[0].status,
            "COMPLETE",
        )
        self.assertEqual(
            next(
                row["payload"]["discovery_candidates"][0]["query_ids"]
                for row in reversed(provider.calls)
                if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
            ),
            prompt_query_ids,
        )
        self.assertEqual(completed.status, "STOPPED_ON_RESOLUTION")

    def test_legacy_candidate_ranking_full_row_hash_migrates_once(self) -> None:
        provider = PendingThenCompleteRankingProvider(
            queries=(QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        url = "https://customer.example.com/legacy-ranking-replay"
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp legacy replay", url),)}
        )
        fetcher = PageFetcher(
            fixture_text_by_url={url: _document_text("legacy-replay")}
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=1,
            max_fetches_per_checkpoint=1,
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
        )
        state = json.loads(json.dumps(first.checkpoint))
        state.pop("checkpoint_id")
        state.pop("checkpoint_hash")
        context = state["pending_candidate_ranking_replay_context"]
        context["schema_version"] = (
            "e2r_v5_candidate_ranking_replay_context_v1"
        )
        context["rank_batch_hash"] = "RANKBATCH-LEGACY-MUTABLE-ROW-HASH"
        context.pop("candidate_prompt_projection_hash")
        checkpoint = source_graph_module._finalize_checkpoint(state)

        migrated = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=checkpoint,
            checkpoint_migration_only=True,
        )

        migrated_context = migrated.checkpoint[
            "pending_candidate_ranking_replay_context"
        ]
        self.assertEqual(
            migrated_context["schema_version"],
            "e2r_v5_candidate_ranking_replay_context_v2",
        )
        self.assertEqual(
            migrated_context["legacy_schema_migrated_from"],
            "e2r_v5_candidate_ranking_replay_context_v1",
        )
        self.assertTrue(
            migrated_context["candidate_prompt_projection_hash"].startswith(
                "RANKCANDIDATEPROMPT"
            )
        )

    def test_collaboration_ranking_wait_defers_reference_history_merge(
        self,
    ) -> None:
        provider = PendingThenCompleteRankingProvider(
            queries=(QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        child_url = "https://customer.example.com/replay-child"
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp replay child", child_url),)}
        )
        fetcher = PageFetcher(
            fixture_text_by_url={child_url: _document_text("replay-child")}
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=2,
            max_fetches_per_checkpoint=1,
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
        )
        state = json.loads(json.dumps(first.checkpoint))
        state.pop("checkpoint_id")
        state.pop("checkpoint_hash")
        child = state["search_candidates"][0]
        child_query_ids = list(child["query_ids"])
        parent_url = "https://customer.example.com/official-reference-parent"
        normalized_parent_url = source_graph_module._normalize_url(parent_url)
        parent = dict(child)
        parent.update(
            {
                "candidate_id": source_graph_module.stable_intelligence_id(
                    "SGCAND",
                    {
                        "target_id": TARGET,
                        "as_of_date": AS_OF_DATE,
                        "normalized_url": normalized_parent_url,
                    },
                ),
                "url": parent_url,
                "normalized_url": normalized_parent_url,
                "title": "Current Corp official reference parent",
                "query_ids": ["SGQUERY-PARENT-HISTORICAL"],
                "materiality_query_ids": ["SGQUERY-PARENT-HISTORICAL"],
                "ranking_status": "NOT_MATERIAL",
                "fetch_status": "DISCOVERY_ONLY_NOT_FETCHED",
                "verified_official_domain_candidate": True,
                "candidate_source_family_hint": "CUSTOMER_OFFICIAL",
                "discovered_referenced_urls": [child_url],
            }
        )
        state["search_candidates"].append(parent)
        checkpoint = source_graph_module._finalize_checkpoint(state)

        resumed = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=checkpoint,
        )

        resumed_child = next(
            row
            for row in resumed.checkpoint["search_candidates"]
            if row["candidate_id"] == child["candidate_id"]
        )
        self.assertEqual(resumed_child["query_ids"], child_query_ids)
        self.assertNotIn(
            parent["candidate_id"],
            resumed_child.get("graph_expansion_parent_candidate_ids", ()),
        )
        self.assertEqual(resumed.status, "CANDIDATE_RANKING_PENDING")

    def test_collaboration_ranking_wait_defers_full_fetch(self) -> None:
        provider = PendingThenCompleteRankingProvider(
            queries=(QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        url = "https://customer.example.com/replay-fetch-boundary"
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp replay fetch boundary", url),)}
        )
        fetcher = PageFetcher(
            fixture_text_by_url={url: _document_text("replay-fetch-boundary")}
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=1,
            max_fetches_per_checkpoint=1,
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
        )
        state = json.loads(json.dumps(first.checkpoint))
        state.pop("checkpoint_id")
        state.pop("checkpoint_hash")
        state["search_candidates"][0]["fetch_status"] = (
            "MATERIAL_PENDING_FETCH"
        )
        checkpoint = source_graph_module._finalize_checkpoint(state)

        resumed = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=checkpoint,
        )

        candidate = resumed.checkpoint["search_candidates"][0]
        self.assertEqual(candidate["fetch_status"], "MATERIAL_PENDING_FETCH")
        self.assertEqual(int(candidate.get("full_fetch_attempt_count") or 0), 0)
        self.assertEqual(resumed.evidence_documents, ())
        self.assertEqual(resumed.status, "CANDIDATE_RANKING_PENDING")

    def test_collaboration_ranking_fetch_handoff_survives_resolved_resume(
        self,
    ) -> None:
        provider = PendingThenCompleteRankingProvider(
            queries=(QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        urls = (
            "https://customer.example.com/current-official-platform-a",
            "https://customer.example.com/current-official-platform-b",
        )
        search = RecordingSearchProvider(
            {
                QUERY: tuple(
                    _result(
                        f"Current Corp customer official platform {index}",
                        url,
                        rank=index,
                    )
                    for index, url in enumerate(urls, start=1)
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: _document_text(f"customer-official-{index}")
                for index, url in enumerate(urls, start=1)
            }
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=2,
            max_fetches_per_checkpoint=1,
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
        )
        first_ranking_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )
        provider.ranking_pending = False

        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=first.checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(ranking_payloads[-1], first_ranking_payload)
        second_candidates = second.checkpoint["search_candidates"]
        self.assertEqual(
            sum(
                row["fetch_status"] == "FULL_DOCUMENT_FETCHED"
                for row in second_candidates
            ),
            1,
        )
        self.assertEqual(
            sum(
                row["fetch_status"] == "MATERIAL_PENDING_FETCH"
                for row in second_candidates
            ),
            1,
        )
        self.assertEqual(second.status, "CHECKPOINT_PENDING")
        second_context = second.checkpoint[
            "pending_candidate_ranking_replay_context"
        ]
        self.assertEqual(
            second_context["replay_phase"],
            "FETCH_HANDOFF_PENDING",
        )
        self.assertEqual(
            len(second_context["fetch_handoff_candidate_ids"]),
            1,
        )

        provider.calls.clear()
        third = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=second.checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        self.assertFalse(
            any(
                row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
                for row in provider.calls
            )
        )
        self.assertTrue(
            all(
                row["fetch_status"] == "FULL_DOCUMENT_FETCHED"
                for row in third.checkpoint["search_candidates"]
            )
        )
        self.assertEqual(
            sum(
                int(row.get("full_fetch_attempt_count") or 0)
                for row in third.checkpoint["search_candidates"]
            ),
            2,
        )
        self.assertEqual(len(third.evidence_documents), 2)
        self.assertEqual(third.status, "STOPPED_ON_RESOLUTION")
        self.assertNotIn(
            "pending_candidate_ranking_replay_context",
            third.checkpoint,
        )

    def test_partial_collaboration_partition_replays_original_exact_batch(
        self,
    ) -> None:
        provider = PartialThenCompleteRankingProvider(
            queries=(QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        urls = (
            "https://customer.example.com/partitioned-official-1",
            "https://customer.example.com/partitioned-official-2",
        )
        search = RecordingSearchProvider(
            {
                QUERY: tuple(
                    _result(
                        f"Current Corp partitioned official {index}",
                        url,
                        rank=index,
                    )
                    for index, url in enumerate(urls, start=1)
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: _document_text(f"partitioned-official-{index}")
                for index, url in enumerate(urls, start=1)
            }
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=2,
            max_fetches_per_checkpoint=2,
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
        )

        first_ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(len(first_ranking_payloads), 2)
        self.assertTrue(
            all(
                row["ranking_status"] == "PENDING"
                for row in first.checkpoint["search_candidates"]
            )
        )
        self.assertEqual(
            first.checkpoint["candidate_materiality_decisions"],
            [],
        )
        self.assertEqual(first.checkpoint["query_failures"], [])
        self.assertTrue(
            all(
                "materiality_decision_id" not in row
                and "material_priority" not in row
                for row in first.checkpoint["search_candidates"]
            )
        )
        self.assertEqual(
            first.checkpoint[
                "pending_candidate_ranking_replay_context"
            ]["rank_batch_candidate_ids"],
            [
                row["candidate_id"]
                for row in first.checkpoint["search_candidates"]
            ],
        )

        provider.partial_ranking_pending = False
        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=first.checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        all_ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(len(all_ranking_payloads), 4)
        self.assertEqual(
            all_ranking_payloads[:2],
            all_ranking_payloads[2:],
        )
        self.assertTrue(
            all(
                row["fetch_status"] == "FULL_DOCUMENT_FETCHED"
                for row in second.checkpoint["search_candidates"]
            )
        )
        self.assertEqual(len(second.evidence_documents), 2)
        self.assertEqual(second.status, "STOPPED_ON_RESOLUTION")

    def test_resume_finishes_pending_ranking_before_executing_pending_query(
        self,
    ) -> None:
        provider = PendingThenCompleteRankingProvider(queries=(QUERY,))
        old_url = "https://example.com/pending-ranking"
        fresh_url = "https://example.com/deferred-query-result"
        search = RecordingSearchProvider(
            {
                QUERY: (
                    _result("Current Corp pending ranking", old_url),
                ),
                ALTERNATE_QUERY: (
                    _result(
                        "Current Corp deferred query result",
                        fresh_url,
                        query=ALTERNATE_QUERY,
                    ),
                ),
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                old_url: _document_text("pending-ranking"),
                fresh_url: _document_text("deferred-query-result"),
            }
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=2,
            max_fetches_per_checkpoint=2,
        )

        bootstrap = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
        )
        old_candidate_id = bootstrap.checkpoint["search_candidates"][0][
            "candidate_id"
        ]
        state = json.loads(json.dumps(bootstrap.checkpoint))
        state.pop("checkpoint_id")
        state.pop("checkpoint_hash")
        state["generated_queries"].append(
            {
                "query_id": "QUERY-PENDING-AFTER-RANKING",
                "objective_id": "OBJECTIVE-1",
                "literal_query": ALTERNATE_QUERY,
                "source_families": ["NAVER_DISCOVERY"],
                "rationale": "랭킹 완료 뒤 남은 source gap을 확인한다.",
                "counter_or_supersession_search": False,
                "generator_kind": "TEST_FIXTURE_LLM",
                "provider_name": provider.provider_name,
                "prompt_hash": "TEST-PENDING-QUERY-PROMPT",
                "response_hash": "TEST-PENDING-QUERY-RESPONSE",
                "production_score_authority": False,
                "execution_status": "PENDING",
                "official_gap_reasons": ["official source gap recorded"],
            }
        )
        checkpoint = source_graph_module._finalize_checkpoint(state)
        provider.calls.clear()
        search.calls.clear()

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=checkpoint,
        )
        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=first.checkpoint,
        )
        self.assertEqual(search.calls, [])
        self.assertEqual(
            first.ranking_results[0].prompt_hash,
            second.ranking_results[0].prompt_hash,
        )
        pending_ranking_calls = [
            row
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(len(pending_ranking_calls), 2)
        self.assertEqual(
            [
                tuple(
                    candidate["candidate_id"]
                    for candidate in row["payload"]["discovery_candidates"]
                )
                for row in pending_ranking_calls
            ],
            [(old_candidate_id,), (old_candidate_id,)],
        )

        provider.ranking_pending = False
        third = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=second.checkpoint,
        )
        self.assertEqual(search.calls, [])
        self.assertEqual(
            third.ranking_results[0].prompt_hash,
            first.ranking_results[0].prompt_hash,
        )
        self.assertEqual(
            next(
                row
                for row in third.checkpoint["generated_queries"]
                if row["query_id"] == "QUERY-PENDING-AFTER-RANKING"
            )["execution_status"],
            "PENDING",
        )

        fourth = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=third.checkpoint,
        )
        self.assertEqual([row[0] for row in search.calls], [ALTERNATE_QUERY])
        self.assertEqual(
            next(
                row
                for row in fourth.checkpoint["generated_queries"]
                if row["query_id"] == "QUERY-PENDING-AFTER-RANKING"
            )["execution_status"],
            "SEARCH_EXECUTED",
        )
        self.assertTrue(
            any(
                row["url"] == fresh_url
                for row in fourth.checkpoint["search_candidates"]
            )
        )

    def test_bounded_fetch_prioritizes_current_official_original_over_old_higher_score(
        self,
    ) -> None:
        provider = SourceBrainProvider(
            source_families=("ISSUER_PRESENTATION",),
        )
        old_url = "https://ir.example.com/2023Q1/earnings-script.pdf"
        current_url = "https://ir.example.com/2026Q1/earnings-script.pdf"
        rows = (
            _result(
                "Current Corp 2023 Q1 earnings script",
                old_url,
                rank=1,
                published="2023-04-27",
            ),
            _result(
                "Current Corp 2026 Q1 earnings script",
                current_url,
                rank=2,
                published="2026-04-30",
            ),
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider({QUERY: rows}),
            fetcher=PageFetcher(
                fixture_text_by_url={
                    old_url: _document_text("old-official-original"),
                    current_url: _document_text("current-official-original"),
                }
            ),
            config=SourceGraphAcquisitionConfig(
                mode="TEST",
                max_candidates_per_checkpoint=2,
                max_fetches_per_checkpoint=1,
            ),
            official_domains=("ir.example.com",),
        )

        self.assertEqual(
            [row["canonical_url"] for row in run.evidence_documents],
            [current_url],
        )
        by_url = {
            row["url"]: row for row in run.checkpoint["search_candidates"]
        }
        self.assertEqual(
            by_url[current_url]["fetch_status"],
            "FULL_DOCUMENT_FETCHED",
        )
        self.assertEqual(
            by_url[old_url]["fetch_status"],
            "MATERIAL_PENDING_FETCH",
        )
        self.assertGreater(
            by_url[old_url]["material_priority"],
            by_url[current_url]["material_priority"],
        )

    def test_checkpoint_resume_quarantines_previously_accepted_unreadable_pdf_text(
        self,
    ) -> None:
        provider = SourceBrainProvider()
        url = "https://broker.example.com/custom-font.pdf"
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp custom font report", url),)}
        )
        fetcher = PageFetcher(
            fixture_text_by_url={url: _document_text("initial-readable-document")}
        )
        first = self._run(provider=provider, search=search, fetcher=fetcher)
        self.assertEqual(len(first.evidence_documents), 1)

        stale_state = json.loads(json.dumps(first.checkpoint))
        stale_state.pop("checkpoint_id")
        stale_state.pop("checkpoint_hash")
        broken_text = ("Current Corp 2026-06-20 " + ("\x01\x0f\x11" * 50)) * 20
        stale_document = stale_state["evidence_documents"][0]
        stale_document["content_text"] = broken_text
        stale_document["content_hash"] = hashlib.sha256(
            broken_text.encode("utf-8")
        ).hexdigest()
        stale_checkpoint = source_graph_module._finalize_checkpoint(stale_state)

        resumed = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=stale_checkpoint,
        )

        self.assertEqual(resumed.evidence_documents, ())
        self.assertEqual(resumed.audit["critical_counts"]["unreadable_evidence_document_count"], 0)
        self.assertEqual(len(resumed.checkpoint["quarantined_documents"]), 1)
        quarantine = resumed.checkpoint["quarantined_documents"][0]
        self.assertEqual(quarantine["document_id"], stale_document["document_id"])
        self.assertIn("excessive_control_characters", quarantine["quarantine_reason"])
        candidate = resumed.checkpoint["search_candidates"][0]
        self.assertEqual(candidate["fetch_status"], "FETCH_REJECTED_UNREADABLE_TEXT")
        self.assertTrue(candidate["alternate_route_required"])
        self.assertTrue(
            any(
                row.get("failure_stage")
                == "FULL_DOCUMENT_READABILITY_VALIDATION"
                for row in resumed.checkpoint["query_failures"]
            )
        )

    def test_fact_extractor_unreadable_feedback_quarantines_same_html_body(
        self,
    ) -> None:
        provider = SourceBrainProvider()
        url = "https://news.example.com/parser-fragmented"
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp fragmented article", url),)}
        )
        fetcher = PageFetcher(
            fixture_text_by_url={url: _document_text("fragmented-html")}
        )
        first = self._run(provider=provider, search=search, fetcher=fetcher)
        document_id = first.evidence_documents[0]["document_id"]

        resumed = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=first.checkpoint,
            score_gap_context={
                "prior_fact_extraction_feedback": [
                    f"FACT_EXTRACTION_RETRY_CONTEXT:UNREADABLE_FULL_DOCUMENT:{document_id}"
                ]
            },
        )

        self.assertNotIn(
            document_id,
            {row["document_id"] for row in resumed.evidence_documents},
        )
        quarantine = next(
            row
            for row in resumed.checkpoint["quarantined_documents"]
            if row["document_id"] == document_id
        )
        self.assertEqual(
            quarantine["quarantine_reason"],
            "FACT_EXTRACTOR_REPORTED_UNREADABLE_FULL_DOCUMENT",
        )
        self.assertFalse(quarantine["parser_refetch_required"])
        self.assertEqual(
            source_graph_module.validate_source_graph_checkpoint(
                resumed.checkpoint
            )["checkpoint_id"],
            resumed.checkpoint["checkpoint_id"],
        )

    def test_checkpoint_resume_refetches_stale_split_article_date(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/stale-split-article-date"
        text = (
            "입력\n2025-09-24 13:34\n"
            "Current Corp disclosed HBM capacity, customer qualification, pricing, "
            "cash conversion, and counter evidence in the full article. "
            + "source-backed article detail " * 12
            + "\n인터넷신문 등록번호\n등록일자 : 2016.04.26\n"
        )
        search = RecordingSearchProvider(
            {
                QUERY: (
                    _result(
                        "Current Corp HBM article",
                        url,
                        published=None,
                    ),
                )
            }
        )
        fetcher = PageFetcher(fixture_text_by_url={url: text})
        first = self._run(provider=provider, search=search, fetcher=fetcher)
        self.assertEqual(first.evidence_documents[0]["published_at"], "2025-09-24")

        stale_state = json.loads(json.dumps(first.checkpoint))
        stale_state.pop("checkpoint_id")
        stale_state.pop("checkpoint_hash")
        stale_document = stale_state["evidence_documents"][0]
        old_document_id = source_graph_module.stable_intelligence_id(
            "SGDOC",
            {
                "target_id": TARGET,
                "content_hash": stale_document["content_hash"],
                "published_at": "2016-04-26",
            },
        )
        stale_document["document_id"] = old_document_id
        stale_document["published_at"] = "2016-04-26"
        stale_document["available_at"] = "2016-04-26"
        stale_document["publication_date_source"] = "DOCUMENT_CONTENT_INFERENCE"
        stale_state["search_candidates"][0]["document_id"] = old_document_id
        stale_checkpoint = source_graph_module._finalize_checkpoint(stale_state)

        resumed = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=stale_checkpoint,
        )

        self.assertEqual(len(resumed.evidence_documents), 1)
        repaired = resumed.evidence_documents[0]
        self.assertEqual(repaired["published_at"], "2025-09-24")
        self.assertNotEqual(repaired["document_id"], old_document_id)
        quarantine = resumed.checkpoint["quarantined_documents"][0]
        self.assertEqual(quarantine["document_id"], old_document_id)
        self.assertEqual(
            quarantine["quarantine_reason"],
            "STALE_PUBLICATION_DATE_INFERENCE:2016-04-26->2025-09-24",
        )
        self.assertTrue(quarantine["publication_date_refetch_required"])
        self.assertEqual(
            resumed.checkpoint["search_candidates"][0]["document_id"],
            repaired["document_id"],
        )
        with tempfile.TemporaryDirectory() as directory:
            paths = write_source_graph_acquisition_run(resumed, output_root=directory)
            loaded = load_source_graph_checkpoint(paths["checkpoint"])
            self.assertEqual(
                loaded["checkpoint_hash"],
                resumed.checkpoint["checkpoint_hash"],
            )

    def test_checkpoint_resume_rejects_newly_detected_future_article(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/stale-future-article-date"
        initial_text = (
            "입력\n2025-09-24 13:34\n"
            "Current Corp disclosed HBM capacity, customer qualification, pricing, "
            "cash conversion, and counter evidence in the full article. "
            + "source-backed article detail " * 12
        )
        future_text = (
            "입력\n2026-07-02 09:30\n"
            "Current Corp disclosed HBM capacity, customer qualification, pricing, "
            "cash conversion, and counter evidence in the full article. "
            + "source-backed future article detail " * 12
            + "\n인터넷신문 등록번호\n등록일자 : 2016.04.26\n"
        )
        search = RecordingSearchProvider(
            {
                QUERY: (
                    _result(
                        "Current Corp HBM article",
                        url,
                        published=None,
                    ),
                )
            }
        )
        first = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={url: initial_text}),
        )
        stale_state = json.loads(json.dumps(first.checkpoint))
        stale_state.pop("checkpoint_id")
        stale_state.pop("checkpoint_hash")
        stale_document = stale_state["evidence_documents"][0]
        stale_document["content_text"] = future_text
        stale_document["content_hash"] = hashlib.sha256(
            future_text.encode("utf-8")
        ).hexdigest()
        old_document_id = source_graph_module.stable_intelligence_id(
            "SGDOC",
            {
                "target_id": TARGET,
                "content_hash": stale_document["content_hash"],
                "published_at": "2016-04-26",
            },
        )
        stale_document["document_id"] = old_document_id
        stale_document["published_at"] = "2016-04-26"
        stale_document["available_at"] = "2016-04-26"
        stale_document["publication_date_source"] = "DOCUMENT_CONTENT_INFERENCE"
        stale_state["search_candidates"][0]["document_id"] = old_document_id
        stale_checkpoint = source_graph_module._finalize_checkpoint(stale_state)

        resumed = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={url: future_text}),
            checkpoint=stale_checkpoint,
        )

        self.assertEqual(resumed.evidence_documents, ())
        self.assertEqual(
            resumed.checkpoint["search_candidates"][0]["fetch_status"],
            "FETCH_REJECTED",
        )
        self.assertTrue(
            any(
                row.get("rejection_reason")
                == "FUTURE_DOCUMENT_AFTER_FULL_FETCH"
                for row in resumed.checkpoint["rejected_documents"]
            )
        )
        self.assertEqual(
            resumed.checkpoint["quarantined_documents"][0]["document_id"],
            old_document_id,
        )

    def test_prior_facts_from_quarantined_source_are_not_reused(self) -> None:
        active_id = "SGDOC-" + "a" * 24
        quarantined_id = "SGDOC-" + "b" * 24
        facts = (
            {"fact_id": "FACT-A", "source_ids": [active_id]},
            {"fact_id": "FACT-B", "source_ids": [quarantined_id]},
            {
                "fact_id": "FACT-C",
                "source_ids": [active_id, quarantined_id],
            },
        )

        kept, invalidated = (
            source_graph_module._filter_facts_to_active_source_documents(
                facts,
                ({"document_id": active_id},),
            )
        )

        self.assertEqual([row["fact_id"] for row in kept], ["FACT-A"])
        self.assertEqual(invalidated, 2)

    def test_candidate_transport_budget_defers_next_query_instead_of_dropping_it(self) -> None:
        second_query = "Current Corp counter evidence cancellation terms"
        provider = SourceBrainProvider(queries=(QUERY, second_query))
        first_result = _result("Current Corp first", "https://example.com/first")
        second_result = _result(
            "Current Corp second",
            "https://example.com/second",
            query=second_query,
        )
        search = RecordingSearchProvider(
            {QUERY: (first_result,), second_query: (second_result,)}
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                first_result.url: _document_text("first"),
                second_result.url: _document_text("second"),
            }
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_queries_per_checkpoint=2,
            max_candidates_per_checkpoint=1,
            max_fetches_per_checkpoint=1,
        )
        first = self._run(
            provider=provider, search=search, fetcher=fetcher, config=config
        )
        self.assertEqual(search.calls, [(QUERY, AS_OF_DATE, 1)])
        self.assertEqual(
            [row["execution_status"] for row in first.checkpoint["generated_queries"]],
            ["SEARCH_EXECUTED", "PENDING"],
        )
        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            config=config,
            checkpoint=first.checkpoint,
        )
        self.assertEqual(search.calls[-1], (second_query, AS_OF_DATE, 1))
        self.assertEqual(len(second.evidence_documents), 2)

    def test_same_content_from_two_urls_is_one_economic_document(self) -> None:
        provider = SourceBrainProvider()
        rows = (
            _result("Current Corp A", "https://a.example.com/report"),
            _result("Current Corp B", "https://b.example.com/mirror"),
        )
        same_text = _document_text("same-content")
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider({QUERY: rows}),
            fetcher=PageFetcher(
                fixture_text_by_url={row.url: same_text for row in rows}
            ),
        )
        self.assertEqual(len(run.evidence_documents), 1)
        dispositions = {
            row["disposition"] for row in run.checkpoint["fetch_records"]
        }
        self.assertEqual(dispositions, {"FULL_DOCUMENT_FETCHED", "DUPLICATE_CONTENT"})
        duplicate_record = next(
            row
            for row in run.checkpoint["fetch_records"]
            if row["disposition"] == "DUPLICATE_CONTENT"
        )
        duplicate_candidate = next(
            row
            for row in run.checkpoint["search_candidates"]
            if row["candidate_id"] == duplicate_record["candidate_id"]
        )
        self.assertEqual(
            duplicate_candidate["document_id"],
            run.evidence_documents[0]["document_id"],
        )
        self.assertEqual(
            duplicate_candidate["duplicate_content_document_id"],
            run.evidence_documents[0]["document_id"],
        )

    def test_duplicate_bytes_from_verified_issuer_upgrade_provenance_once(self) -> None:
        provider = SourceBrainProvider(
            source_families=("ISSUER_PRESENTATION",),
        )
        mirror_url = "https://independent.example.net/report"
        issuer_url = "https://ir.example.com/report"
        rows = (
            _result("Current Corp mirror", mirror_url, rank=1),
            _result("Current Corp issuer original", issuer_url, rank=2),
        )
        same_text = _document_text("same-issuer-content")
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider({QUERY: rows}),
            fetcher=PageFetcher(
                fixture_text_by_url={row.url: same_text for row in rows}
            ),
            config=SourceGraphAcquisitionConfig(
                mode="TEST",
                official_first_required=False,
            ),
            official_domains=("example.com",),
        )
        self.assertEqual(len(run.evidence_documents), 1)
        document = run.evidence_documents[0]
        self.assertEqual(document["canonical_url"], issuer_url)
        self.assertEqual(document["source_family"], "ISSUER_NEWSROOM")
        self.assertTrue(document["official_provenance_upgrade"])
        self.assertEqual(
            document["source_family_observations"],
            ["GENERAL_WEB_DISCOVERY", "ISSUER_NEWSROOM"],
        )
        self.assertEqual(document["verified_official_discovery_urls"], [issuer_url])

    def test_incomplete_materiality_ranking_fetches_nothing_and_stays_pending(self) -> None:
        provider = SourceBrainProvider(omit_last_ranking=True)
        rows = (
            _result("Current Corp A", "https://example.com/a"),
            _result("Current Corp B", "https://example.com/b"),
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider({QUERY: rows}),
            fetcher=PageFetcher(
                fixture_text_by_url={row.url: _document_text(row.title) for row in rows}
            ),
        )
        self.assertEqual(run.status, "CANDIDATE_RANKING_PENDING")
        self.assertEqual(run.evidence_documents, ())
        self.assertTrue(
            any("INVALID_RANKING_OUTPUT" in reason for reason in run.checkpoint["pending_reasons"])
        )

    def test_resolved_objective_pending_candidates_do_not_block_open_objective(
        self,
    ) -> None:
        stale_provider = SourceBrainProvider(omit_last_ranking=True)
        stale_urls = (
            "https://example.com/stale-a",
            "https://example.com/stale-b",
        )
        first = self._run(
            provider=stale_provider,
            search=RecordingSearchProvider(
                {
                    QUERY: tuple(
                        _result(f"Current Corp stale {index}", url)
                        for index, url in enumerate(stale_urls)
                    )
                }
            ),
            fetcher=PageFetcher(fixture_text_by_url={}),
        )
        self.assertEqual(first.status, "CANDIDATE_RANKING_PENDING")
        self.assertTrue(
            all(
                row["ranking_status"] == "PENDING"
                for row in first.checkpoint["search_candidates"]
            )
        )

        open_objective = SourceResearchObjective(
            objective_id="OBJECTIVE-2",
            component_id="earnings_visibility",
            research_objective="forward revision and customer allocation",
            preferred_source_families=("NAVER_DISCOVERY",),
            counter_or_supersession_required=True,
        )
        provider = SourceBrainProvider(queries=(ALTERNATE_QUERY,))
        search = RecordingSearchProvider(
            {
                ALTERNATE_QUERY: (
                    _result(
                        "Current Corp open objective report",
                        ALTERNATE_URL,
                        query=ALTERNATE_QUERY,
                    ),
                )
            }
        )
        second = ResearcherSourceGraphAcquirer(
            query_provider=provider,
            search_provider=search,
            page_fetcher=PageFetcher(
                fixture_text_by_url={
                    ALTERNATE_URL: _document_text("open-objective")
                }
            ),
        ).acquire(
            config=SourceGraphAcquisitionConfig(mode="TEST"),
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            as_of_date=AS_OF_DATE,
            open_objectives=(_objective(), open_objective),
            current_evidence_facts=(),
            target_business_model=None,
            source_coverage=(),
            official_gap_reasons_by_objective={
                "OBJECTIVE-1": ("official source gap recorded",),
                "OBJECTIVE-2": ("official source gap recorded",),
            },
            resolved_objective_ids=("OBJECTIVE-1",),
            prior_checkpoint=first.checkpoint,
        )
        self.assertEqual(search.calls, [(ALTERNATE_QUERY, AS_OF_DATE, 100)])
        self.assertNotEqual(second.status, "CANDIDATE_RANKING_PENDING")
        self.assertEqual(len(second.evidence_documents), 1)
        stale_candidates = [
            row
            for row in second.checkpoint["search_candidates"]
            if row.get("url") in stale_urls
        ]
        self.assertTrue(
            all(
                row["ranking_status"] == "RESOLVED_SCOPE_NOT_RANKED"
                and row["objective_resolution_transport_disposition"]
                == "RANKING_NOT_REQUIRED_SCOPE_RESOLVED"
                for row in stale_candidates
            )
        )
        ranked_candidate_ids = {
            candidate["candidate_id"]
            for call in provider.calls
            if call["pass_name"] == "SOURCE_CANDIDATE_RANKING"
            for candidate in call["payload"]["discovery_candidates"]
        }
        self.assertTrue(
            {
                row["candidate_id"] for row in stale_candidates
            }.isdisjoint(ranked_candidate_ids)
        )
        self.assertNotIn(
            "pending_candidate_ranking_replay_context",
            second.checkpoint,
        )

    def test_production_general_web_requires_recorded_official_gap(self) -> None:
        provider = SourceBrainProvider()
        naver = NoNetworkLiveNaver()
        fetcher = PageFetcher(
            live_enabled=True,
            max_text_chars=(
                source_graph_module.PRODUCTION_PAGE_FETCH_TEXT_CHAR_BOUND
            ),
        )
        config = SourceGraphAcquisitionConfig(
            mode="PRODUCTION_DAILY",
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=10,
            max_fetches_per_checkpoint=2,
        )
        run = self._run(
            provider=provider,
            search=naver,
            fetcher=fetcher,
            config=config,
            official_gaps={},
        )
        self.assertIn("GENERAL_WEB_WITHOUT_OFFICIAL_GAP", run.checkpoint["pending_reasons"])
        self.assertEqual(naver.built_requests, [])
        self.assertEqual(run.checkpoint["generated_queries"][0]["execution_status"], "BLOCKED_OFFICIAL_FIRST")
        resumed = self._run(
            provider=provider,
            search=naver,
            fetcher=fetcher,
            config=config,
            checkpoint=run.checkpoint,
            official_gaps={"OBJECTIVE-1": ("official provider returned no document",)},
        )
        self.assertEqual(naver.calls, [QUERY])
        self.assertEqual(len(resumed.checkpoint["generated_queries"]), 1)

    def test_production_daily_rejects_unbounded_page_fetcher(self) -> None:
        with self.assertRaisesRegex(ValueError, "bounded PageFetcher"):
            self._run(
                provider=SourceBrainProvider(),
                search=NoNetworkLiveNaver(),
                fetcher=PageFetcher(
                    live_enabled=True,
                    max_text_chars=None,
                ),
                config=SourceGraphAcquisitionConfig(
                    mode="PRODUCTION_DAILY",
                    max_queries_per_checkpoint=1,
                    max_candidates_per_checkpoint=10,
                    max_fetches_per_checkpoint=2,
                ),
                official_gaps={},
            )

    def test_production_daily_rejects_legacy_small_text_bound(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "complete-filing transport minimum",
        ):
            self._run(
                provider=SourceBrainProvider(),
                search=NoNetworkLiveNaver(),
                fetcher=PageFetcher(
                    live_enabled=True,
                    max_text_chars=200_000,
                ),
                config=SourceGraphAcquisitionConfig(
                    mode="PRODUCTION_DAILY",
                    max_queries_per_checkpoint=1,
                    max_candidates_per_checkpoint=10,
                    max_fetches_per_checkpoint=2,
                ),
                official_gaps={},
            )

    def test_backfill_checkpoint_migrates_one_way_to_production_daily(
        self,
    ) -> None:
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="RESEARCH_BACKFILL",
        )
        checkpoint = source_graph_module._finalize_checkpoint(state)

        resumed = source_graph_module._resume_acquisition_state(
            checkpoint,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            mode="PRODUCTION_DAILY",
        )

        self.assertEqual(resumed["mode"], "PRODUCTION_DAILY")
        self.assertEqual(
            resumed["mode_migration"]["from"],
            "RESEARCH_BACKFILL",
        )
        self.assertTrue(
            resumed["mode_migration"][
                "historical_evidence_requires_downstream_validation"
            ]
        )
        self.assertTrue(
            resumed["mode_migration"][
                "transport_history_does_not_certify_completion"
            ]
        )
        with self.assertRaisesRegex(ValueError, "mode mismatch"):
            source_graph_module._resume_acquisition_state(
                checkpoint,
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                mode="TEST",
            )

    def test_legacy_production_checkpoint_needs_downstream_roster_migration(
        self,
    ) -> None:
        checkpoint = {
            "mode": "PRODUCTION_DAILY",
            "status": "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
            "generated_queries": [],
            "search_candidates": [],
            "evidence_documents": [],
        }

        self.assertFalse(
            _source_checkpoint_is_ready_for_readonly_replay(checkpoint)
        )
        checkpoint["production_downstream_document_ids"] = []
        self.assertTrue(
            _source_checkpoint_is_ready_for_readonly_replay(checkpoint)
        )

        checkpoint["evidence_documents"] = [
            {
                "document_id": "SGDOC-legacy-cap",
                "source_provider": "PageFetcher",
                "content_text": "x" * 199_999,
            }
        ]
        checkpoint["production_downstream_document_ids"] = [
            "SGDOC-legacy-cap"
        ]
        self.assertFalse(
            _source_checkpoint_is_ready_for_readonly_replay(checkpoint)
        )
        checkpoint["evidence_documents"][0]["text_complete"] = True
        self.assertTrue(
            _source_checkpoint_is_ready_for_readonly_replay(checkpoint)
        )

    def test_same_url_new_source_scope_invalidates_legacy_materiality(
        self,
    ) -> None:
        url = "https://writer.example.net/legacy-hbm-retelling"
        existing = {
            "candidate_id": "LEGACY-CANDIDATE",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "url": url,
            "normalized_url": url,
            "query_ids": ["OLD-QUERY"],
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["TRUSTED_BUSINESS_MEDIA"],
            "ranking_status": "MATERIAL",
            "fetch_status": "MATERIAL_PENDING_FETCH",
            "materiality_decision_id": "LEGACY-DECISION",
            "material_priority": 1.0,
        }
        newly_discovered = {
            **existing,
            "query_ids": ["NEW-QUERY"],
            "objective_ids": ["OBJECTIVE-2"],
            "requested_source_families": ["CUSTOMER_OFFICIAL"],
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
            "query_lineage_valid": True,
        }
        candidates = [existing]

        source_graph_module._merge_search_candidates(
            candidates,
            [],
            [newly_discovered],
            cutoff=date.fromisoformat(AS_OF_DATE),
        )

        self.assertEqual(existing["ranking_status"], "PENDING")
        self.assertEqual(existing["fetch_status"], "NOT_STARTED")
        self.assertNotIn("materiality_decision_id", existing)
        self.assertEqual(
            existing["materiality_revalidation_reason"],
            "QUERY_OBJECTIVE_OR_REQUESTED_SOURCE_SCOPE_EXPANDED",
        )
        self.assertEqual(
            set(existing["requested_source_families"]),
            {"CUSTOMER_OFFICIAL"},
        )
        self.assertEqual(
            set(existing["historical_requested_source_families"]),
            {"TRUSTED_BUSINESS_MEDIA"},
        )
        self.assertEqual(
            existing["objective_ids"],
            ["OBJECTIVE-2"],
        )
        self.assertEqual(
            existing["historical_objective_ids"],
            ["OBJECTIVE-1"],
        )

    def test_production_reopens_legacy_pending_material_before_fetch(
        self,
    ) -> None:
        candidate = {
            "candidate_id": "LEGACY-PENDING",
            "url": "https://writer.example.net/pending",
            "normalized_url": "https://writer.example.net/pending",
            "query_ids": ["QUERY-1"],
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["CUSTOMER_OFFICIAL"],
            "ranking_status": "MATERIAL",
            "fetch_status": "MATERIAL_PENDING_FETCH",
            "materiality_decision_id": "LEGACY-DECISION",
        }

        reopened = (
            source_graph_module._reopen_stale_pending_materiality_candidates(
                [candidate]
            )
        )

        self.assertEqual(reopened, 1)
        self.assertEqual(candidate["ranking_status"], "PENDING")
        self.assertEqual(candidate["fetch_status"], "NOT_STARTED")
        self.assertNotIn("materiality_decision_id", candidate)

    def test_production_downstream_requires_fact_or_current_source_match(
        self,
    ) -> None:
        current_candidate = {
            "candidate_id": "CURRENT-MATCHED",
            "document_id": "SGDOC-current",
            "url": "https://customer.example.com/platform",
            "normalized_url": "https://customer.example.com/platform",
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["CUSTOMER_OFFICIAL"],
            "matched_requested_source_family": "CUSTOMER_OFFICIAL",
        }
        current_candidate["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(
                current_candidate
            )
        )
        documents = (
            {
                "document_id": "SGDOC-fact-backed",
                "source_provider": "PageFetcher",
            },
            {
                "document_id": "SGDOC-legacy-unvalidated",
                "source_provider": "PageFetcher",
            },
            {
                "document_id": "SGDOC-current",
                "source_provider": "PageFetcher",
                "requested_source_families": ["CUSTOMER_OFFICIAL"],
                "matched_requested_source_family": "CUSTOMER_OFFICIAL",
                "materiality_scope_hash": current_candidate[
                    "materiality_scope_hash"
                ],
            },
            {
                "document_id": "SGDOC-official-merge",
                "source_provider": "OpenDart",
            },
        )

        active = source_graph_module._production_downstream_documents(
            documents=documents,
            facts=(
                {
                    "fact_id": "FACT-1",
                    "source_ids": ["SGDOC-fact-backed"],
                },
            ),
            candidates=(current_candidate,),
        )

        self.assertEqual(
            {row["document_id"] for row in active},
            {
                "SGDOC-fact-backed",
                "SGDOC-current",
                "SGDOC-official-merge",
            },
        )

    def test_production_downstream_preserves_valid_fetched_scope_when_later_scope_is_unrelated(
        self,
    ) -> None:
        url = "https://issuer.example.com/q1-results"
        content = "Q1 preliminary results are unaudited and may change."
        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        published_at = "2026-04-24"
        target_id = "005930"
        document_id = source_graph_module.stable_intelligence_id(
            "SGDOC",
            {
                "target_id": target_id,
                "content_hash": content_hash,
                "published_at": published_at,
            },
        )
        document = {
            "document_id": document_id,
            "target_id": target_id,
            "source_provider": "PageFetcher",
            "canonical_url": url,
            "published_at": published_at,
            "content_text": content,
            "content_hash": content_hash,
            "full_fetch_performed": True,
            "evidence_eligible": True,
            "snippet_only": False,
            "snippet_used_as_document": False,
            "materiality_query_ids": ["QUERY-Q1-DISCLAIMER"],
            "objective_ids": ["OBJECTIVE-Q1-DISCLAIMER"],
            "requested_source_families": ["ISSUER_EARNINGS_RELEASE"],
            "matched_requested_source_family": "ISSUER_EARNINGS_RELEASE",
            "source_materiality_decision_id": "DECISION-Q1-MATERIAL",
            "materiality_scope_url": url,
        }
        document["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(
                {
                    "normalized_url": url,
                    "objective_ids": document["objective_ids"],
                    "requested_source_families": document[
                        "requested_source_families"
                    ],
                }
            )
        )
        current_candidate = {
            "candidate_id": "SGCAND-SAME-URL",
            "document_id": document["document_id"],
            "url": url,
            "normalized_url": url,
            "materiality_query_ids": ["QUERY-ANNUAL-MIX"],
            "objective_ids": ["OBJECTIVE-ANNUAL-MIX"],
            "requested_source_families": ["ISSUER_EARNINGS_RELEASE"],
            "matched_requested_source_family": "ISSUER_EARNINGS_RELEASE",
            "materiality_decision_id": "DECISION-ANNUAL-NOT-MATERIAL",
            "ranking_status": "NOT_MATERIAL",
            "fetch_status": "FULL_DOCUMENT_REVALIDATION_REJECTED",
        }
        current_candidate["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(
                current_candidate
            )
        )
        original_material_decision = {
            "candidate_id": current_candidate["candidate_id"],
            "decision_id": document["source_materiality_decision_id"],
            "material_relevance": True,
            "matched_requested_source_family": "ISSUER_EARNINGS_RELEASE",
            "objective_ids": document["objective_ids"],
        }
        current_not_material_decision = {
            "candidate_id": current_candidate["candidate_id"],
            "decision_id": current_candidate["materiality_decision_id"],
            "material_relevance": False,
            "matched_requested_source_family": "ISSUER_EARNINGS_RELEASE",
            "objective_ids": current_candidate["objective_ids"],
        }
        fetch_record = {
            "candidate_id": current_candidate["candidate_id"],
            "content_hash": content_hash,
            "disposition": "FULL_DOCUMENT_FETCHED",
            "document_id": document_id,
            "full_fetch_attempted": True,
            "provider_error": None,
            "objective_ids": document["objective_ids"],
        }

        self.assertEqual(
            source_graph_module._production_downstream_documents(
                documents=(document,),
                facts=(),
                candidates=(current_candidate,),
            ),
            (),
        )
        self.assertEqual(
            source_graph_module._production_downstream_documents(
                documents=(document,),
                facts=(),
                candidates=(current_candidate,),
                materiality_decisions=(
                    original_material_decision,
                    current_not_material_decision,
                ),
                fetch_records=(fetch_record,),
            ),
            (document,),
        )

        same_scope_candidate = {
            **current_candidate,
            "materiality_query_ids": document["materiality_query_ids"],
            "objective_ids": document["objective_ids"],
            "materiality_scope_hash": document["materiality_scope_hash"],
        }
        same_scope_not_material_decision = {
            **current_not_material_decision,
            "objective_ids": document["objective_ids"],
        }
        self.assertEqual(
            source_graph_module._production_downstream_documents(
                documents=(document,),
                facts=(),
                candidates=(same_scope_candidate,),
                materiality_decisions=(
                    original_material_decision,
                    same_scope_not_material_decision,
                ),
                fetch_records=(fetch_record,),
            ),
            (),
        )

        forged_document = {
            **document,
            "content_text": "forged",
            "full_fetch_performed": False,
            "evidence_eligible": False,
        }
        self.assertEqual(
            source_graph_module._production_downstream_documents(
                documents=(forged_document,),
                facts=(),
                candidates=(current_candidate,),
                materiality_decisions=(
                    original_material_decision,
                    current_not_material_decision,
                ),
                fetch_records=(fetch_record,),
            ),
            (),
        )

    def test_requested_family_is_not_coverage_until_matched_fetch(self) -> None:
        query = {
            "query_id": "QUERY-CUSTOMER",
            "objective_id": "OBJECTIVE-1",
            "source_families": ["CUSTOMER_OFFICIAL"],
            "execution_status": "SEARCH_EXECUTED",
        }
        unrelated_document = {
            "document_id": "SGDOC-ISSUER",
            "source_provider": "OpenDart",
            "source_family": "OPENDART",
            "objective_ids": ["OBJECTIVE-1"],
            "evidence_eligible": True,
        }

        missing = (
            source_graph_module
            ._requested_source_family_without_matched_fetch_failures(
                generated_queries=(query,),
                documents=(unrelated_document,),
                candidates=(),
                facts=(),
                unresolved_objectives=(
                    {"objective_id": "OBJECTIVE-1"},
                ),
            )
        )

        self.assertEqual(len(missing), 1)
        self.assertEqual(
            missing[0]["failure_reason"],
            "REQUESTED_SOURCE_FAMILY_WITHOUT_ACCEPTED_CLAIM_FACT_LINEAGE",
        )
        self.assertEqual(
            missing[0]["source_family"],
            "CUSTOMER_OFFICIAL",
        )
        self.assertFalse(missing[0]["absence_eligible"])

        fetched_without_accepted_fact = (
            source_graph_module
            ._requested_source_family_without_matched_fetch_failures(
                generated_queries=(query,),
                documents=(
                    unrelated_document,
                    {
                        "document_id": "SGDOC-CUSTOMER",
                        "source_provider": "CustomerOfficialFetcher",
                        "source_family": "CUSTOMER_OFFICIAL",
                        "objective_ids": ["OBJECTIVE-1"],
                        "evidence_eligible": True,
                    },
                ),
                candidates=(),
                facts=(),
                unresolved_objectives=(
                    {"objective_id": "OBJECTIVE-1"},
                ),
            )
        )

        self.assertEqual(len(fetched_without_accepted_fact), 1)

        reached = (
            source_graph_module
            ._requested_source_family_without_matched_fetch_failures(
                generated_queries=(query,),
                documents=(
                    unrelated_document,
                    {
                        "document_id": "SGDOC-CUSTOMER",
                        "source_provider": "CustomerOfficialFetcher",
                        "source_family": "CUSTOMER_OFFICIAL",
                        "objective_ids": ["OBJECTIVE-1"],
                        "evidence_eligible": True,
                        "snippet_only": False,
                    },
                ),
                candidates=(),
                facts=(
                    {
                        "fact_id": "FACT-CUSTOMER",
                        "source_ids": ["SGDOC-CUSTOMER"],
                        "claim_ids": ["CLAIM-CUSTOMER"],
                    },
                ),
                unresolved_objectives=(
                    {"objective_id": "OBJECTIVE-1"},
                ),
            )
        )

        self.assertEqual(reached, ())

        pending = (
            source_graph_module
            ._requested_source_family_without_matched_fetch_failures(
                generated_queries=(query,),
                documents=(unrelated_document,),
                candidates=(
                    {
                        "objective_ids": ["OBJECTIVE-1"],
                        "requested_source_families": [
                            "CUSTOMER_OFFICIAL"
                        ],
                        "ranking_status": "PENDING",
                        "fetch_status": "NOT_STARTED",
                    },
                ),
                facts=(),
                unresolved_objectives=(
                    {"objective_id": "OBJECTIVE-1"},
                ),
            )
        )

        self.assertEqual(pending, ())

    def test_resolved_historical_requested_family_gap_does_not_reopen(
        self,
    ) -> None:
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state.update(
            status="STOPPED_ON_RESOLUTION",
            generated_queries=[
                {
                    "query_id": "QUERY-CUSTOMER-1",
                    "objective_id": "OBJECTIVE-1",
                    "literal_query": QUERY,
                    "source_families": ["CUSTOMER_OFFICIAL"],
                    "execution_status": "SEARCH_EXECUTED",
                }
            ],
            executed_queries=[QUERY],
            resolved_objective_ids=["OBJECTIVE-1"],
        )
        checkpoint = source_graph_module._finalize_checkpoint(state)
        provider = SourceBrainProvider(
            queries=(ALTERNATE_QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )

        run = self._run(
            provider=provider,
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
            score_gap_context={
                "prior_supervisor_gap": {
                    # Neither a legacy string nor an allowed-family roster has
                    # objective-bound mandatory-family authority.
                    "source_family_gaps": ["CUSTOMER_OFFICIAL"],
                    "missing_role_resolution_contracts": [
                        {
                            "objective_id": "OBJECTIVE-1",
                            "allowed_source_families": [
                                "CUSTOMER_OFFICIAL"
                            ],
                        }
                    ],
                    "failure_assessments": [
                        {
                            "objective_id": "OBJECTIVE-1",
                            "source_family": "CUSTOMER_OFFICIAL",
                            "classification": "FETCH_FAILURE",
                        }
                    ],
                }
            },
        )

        self.assertEqual(run.status, "STOPPED_ON_RESOLUTION")
        self.assertIn(
            "OBJECTIVE-1",
            run.checkpoint["resolved_objective_ids"],
        )
        self.assertFalse(provider.calls)
        self.assertFalse(
            any(
                row.get("failure_reason")
                == "REQUESTED_SOURCE_FAMILY_WITHOUT_"
                "ACCEPTED_CLAIM_FACT_LINEAGE"
                for row in run.checkpoint["query_failures"]
            )
        )

    def test_mandatory_family_pairs_use_only_current_supervisor_gap_keys(
        self,
    ) -> None:
        pairs = (
            source_graph_module
            ._current_supervisor_mandatory_source_family_pairs(
                score_gap_context={
                    "prior_supervisor_gap": {
                        "new_source_family_directions": [
                            {
                                "component_id": "eps_fcf_explosion",
                                "source_family": "CUSTOMER_OFFICIAL",
                            },
                            {
                                "objective_id": "OTHER-OBJECTIVE",
                                "component_id": "eps_fcf_explosion",
                                "source_family": "REUTERS",
                            }
                        ],
                        "source_family_gaps": [
                            "REUTERS",
                            {
                                "objective_id": "OBJECTIVE-1",
                                "source_family": "KIND_KRX",
                            },
                            {
                                "objective_id": "OBJECTIVE-1",
                                "allowed_source_families": ["REUTERS"],
                            },
                        ],
                        "failure_assessments": [
                            {
                                "objective_id": "OBJECTIVE-1",
                                "source_family": "REUTERS",
                            }
                        ],
                    }
                },
                objectives=(_objective().to_dict(),),
            )
        )

        self.assertEqual(
            pairs,
            frozenset(
                {
                    ("OBJECTIVE-1", "CUSTOMER_OFFICIAL"),
                    ("OBJECTIVE-1", "KIND_KRX"),
                }
            ),
        )

    def test_current_supervisor_mandatory_family_gap_reopens_then_pending(
        self,
    ) -> None:
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state.update(
            status="STOPPED_ON_RESOLUTION",
            generated_queries=[
                {
                    "query_id": "QUERY-CUSTOMER-1",
                    "objective_id": "OBJECTIVE-1",
                    "literal_query": QUERY,
                    "source_families": ["CUSTOMER_OFFICIAL"],
                    "execution_status": "SEARCH_EXECUTED",
                }
            ],
            executed_queries=[QUERY],
            resolved_objective_ids=["OBJECTIVE-1"],
        )
        checkpoint = source_graph_module._finalize_checkpoint(state)
        mandatory_gap_context = {
            "prior_supervisor_gap": {
                "new_source_family_directions": [
                    {
                        # The existing objective roster provides the only
                        # allowed component-to-objective fallback.
                        "component_id": "eps_fcf_explosion",
                        "source_family": "CUSTOMER_OFFICIAL",
                    }
                ]
            }
        }
        first_provider = SourceBrainProvider(
            queries=(ALTERNATE_QUERY,),
            source_families=("CUSTOMER_OFFICIAL",),
        )

        first = self._run(
            provider=first_provider,
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
            score_gap_context=mandatory_gap_context,
        )

        query_payload = next(
            row["payload"]
            for row in first_provider.calls
            if row["pass_name"] == "SOURCE_QUERY_GENERATION"
        )
        projected_failures = json.dumps(
            query_payload["prior_query_or_source_failures"],
            ensure_ascii=False,
        )
        self.assertIn(
            "REQUESTED_SOURCE_FAMILY_WITHOUT_"
            "ACCEPTED_CLAIM_FACT_LINEAGE",
            projected_failures,
        )
        self.assertIn("CUSTOMER_OFFICIAL", projected_failures)
        self.assertNotIn(
            "OBJECTIVE-1",
            first.checkpoint["resolved_objective_ids"],
        )

        second_provider = SourceBrainProvider(
            queries=("Current Corp another customer official route",),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        second = self._run(
            provider=second_provider,
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=first.checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
            score_gap_context=mandatory_gap_context,
        )

        self.assertEqual(second.status, "SOURCE_PROVIDER_PENDING")
        self.assertFalse(second_provider.calls)
        self.assertTrue(
            any(
                value
                == "SOURCE_FAMILY_ACCEPTED_LINEAGE_PENDING:"
                "OBJECTIVE-1:CUSTOMER_OFFICIAL"
                for value in second.checkpoint["pending_reasons"]
            )
        )

    def test_new_supervisor_family_direction_reopens_resolved_without_prior_query(
        self,
    ) -> None:
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state.update(
            status="STOPPED_ON_RESOLUTION",
            resolved_objective_ids=["OBJECTIVE-1"],
        )
        checkpoint = source_graph_module._finalize_checkpoint(state)
        provider = SourceBrainProvider(
            queries=("Current Corp independent official relationship",),
            source_families=("CUSTOMER_OFFICIAL",),
        )
        mandatory_gap_context = {
            "prior_supervisor_gap": {
                "new_source_family_directions": [
                    {
                        "objective_id": "OBJECTIVE-1",
                        "source_family": "CUSTOMER_OFFICIAL",
                        "direction": "independent official corroboration",
                    }
                ]
            }
        }

        run = self._run(
            provider=provider,
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
            score_gap_context=mandatory_gap_context,
        )

        self.assertNotIn(
            "OBJECTIVE-1",
            run.checkpoint["resolved_objective_ids"],
        )
        query_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_QUERY_GENERATION"
        )
        projected_failures = json.dumps(
            query_payload["prior_query_or_source_failures"],
            ensure_ascii=False,
        )
        self.assertIn(
            "REQUESTED_SOURCE_FAMILY_WITHOUT_"
            "ACCEPTED_CLAIM_FACT_LINEAGE",
            projected_failures,
        )
        self.assertIn("CUSTOMER_OFFICIAL", projected_failures)

    def test_sparse_verified_reference_gets_one_fetch_then_full_text_revalidation(
        self,
    ) -> None:
        provider = SparseReferenceRevalidationProvider(
            source_families=("ISSUER_NEWSROOM",),
        )
        parent_url = "https://issuer.example.com/current"
        child_url = "https://issuer.example.com/current/full.pdf"
        fetcher = ReferencedRouteFetcher(
            parent_url=parent_url,
            child_url=child_url,
            parent_text="Current Corp official landing page",
        )
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp official landing", parent_url),)}
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            official_domains=("issuer.example.com",),
        )
        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=first.checkpoint,
            official_domains=("issuer.example.com",),
        )
        child_after_fetch = next(
            row
            for row in second.checkpoint["search_candidates"]
            if row.get("url") == child_url
        )
        self.assertEqual(
            child_after_fetch["fetch_status"],
            "FULL_DOCUMENT_REVALIDATION_PENDING",
        )
        self.assertTrue(
            child_after_fetch[
                "sparse_reference_transport_revalidation_attempted"
            ]
        )
        self.assertEqual(fetcher.calls.count(child_url), 1)

        third = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=second.checkpoint,
            official_domains=("issuer.example.com",),
        )
        child_final = next(
            row
            for row in third.checkpoint["search_candidates"]
            if row.get("url") == child_url
        )
        self.assertEqual(child_final["ranking_status"], "MATERIAL")
        self.assertEqual(child_final["fetch_status"], "FULL_DOCUMENT_FETCHED")
        self.assertEqual(fetcher.calls.count(child_url), 1)
        full_text_payload = next(
            row["payload"]
            for row in reversed(provider.calls)
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
            and any(
                (candidate.get("reference_transport_context") or {}).get(
                    "full_fetch_content_text"
                )
                for candidate in row["payload"]["discovery_candidates"]
            )
        )
        self.assertIn(
            "linked-official-transcript",
            json.dumps(full_text_payload, ensure_ascii=False),
        )

    def test_supervisor_query_direction_preempts_reference_backlog(
        self,
    ) -> None:
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state["status"] = "CHECKPOINT_PENDING"
        state["generated_queries"] = [
            {
                "query_id": "OLD-QUERY",
                "objective_id": "OBJECTIVE-1",
                "literal_query": "Current Corp old issuer archive",
                "source_families": ["ISSUER_NEWSROOM"],
                "execution_status": "SEARCH_EXECUTED",
            }
        ]
        state["executed_queries"] = [
            "Current Corp old issuer archive"
        ]
        state["search_candidates"] = [
            {
                "candidate_id": "REFERENCE-BACKLOG",
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "url": "https://issuer.example.com/old-menu-link",
                "normalized_url": (
                    "https://issuer.example.com/old-menu-link"
                ),
                "title": "old inherited reference",
                "snippet": None,
                "source": "issuer.example.com",
                "published_at": None,
                "rank": 0,
                "is_pdf": False,
                "is_report_domain": False,
                "is_news": False,
                "is_disclosure": False,
                "query_ids": ["OLD-QUERY"],
                "objective_ids": ["OBJECTIVE-1"],
                "requested_source_families": [
                    "ISSUER_NEWSROOM"
                ],
                "query_lineage_valid": True,
                "graph_expansion_parent_document_ids": ["OLD-DOC"],
                "discovery_only": True,
                "snippet_discovery_only": True,
                "ranking_status": "PENDING",
                "fetch_status": "NOT_STARTED",
            }
        ]
        checkpoint = source_graph_module._finalize_checkpoint(state)
        provider = SourceBrainProvider()
        direct_url = "https://example.com/new-supervisor-route"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp material new route",
                            direct_url,
                        ),
                    )
                }
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={
                    direct_url: _document_text("supervisor-route")
                }
            ),
            config=SourceGraphAcquisitionConfig(
                mode="TEST",
                max_results_per_query=1,
                max_queries_per_checkpoint=1,
                max_candidates_per_checkpoint=1,
                max_fetches_per_checkpoint=1,
            ),
            checkpoint=checkpoint,
            score_gap_context={
                "prior_supervisor_gap": {
                    "query_direction_briefs": [
                        {
                            "objective_id": "OBJECTIVE-1",
                            "research_need": (
                                "try a distinct official counterparty route"
                            ),
                        }
                    ]
                }
            },
        )

        self.assertIsNotNone(run.query_generation)
        ranking_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )
        self.assertEqual(
            [row["url"] for row in ranking_payload["discovery_candidates"]],
            [direct_url],
        )
        reference = next(
            row
            for row in run.checkpoint["search_candidates"]
            if row["candidate_id"] == "REFERENCE-BACKLOG"
        )
        self.assertEqual(reference["ranking_status"], "PENDING")
        self.assertTrue(
            run.audit[
                "supervisor_query_direction_prioritized_over_reference_backlog"
            ]
        )

    def test_candidate_query_edge_repair_preempts_candidate_backlog(
        self,
    ) -> None:
        repair_query = "Current Corp official preliminary results newsroom"
        official_url = "https://issuer.example.com/current-results"
        candidate_id = source_graph_module.stable_intelligence_id(
            "SGCAND",
            {
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "normalized_url": official_url,
            },
        )
        alternate_url = "https://issuer.example.com/alternate-results"
        stale_terminal_url = "https://issuer.example.com/stale-results"
        backlog_url = "https://example.com/unrelated-backlog"
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state.update(
            status="CHECKPOINT_PENDING",
            generated_queries=[
                {
                    "query_id": "QUERY-VALUATION",
                    "objective_id": "OBJECTIVE-1",
                    "literal_query": "Current Corp valuation multiples",
                    "source_families": ["VALUATION_MULTIPLES"],
                    "execution_status": "SEARCH_EXECUTED",
                }
            ],
            executed_queries=["Current Corp valuation multiples"],
            search_candidates=[
                {
                    "candidate_id": candidate_id,
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "url": official_url,
                    "normalized_url": official_url,
                    "title": "Current Corp official preliminary results",
                    "snippet": None,
                    "source": "issuer.example.com",
                    "published_at": "2026-06-20",
                    "rank": 1,
                    "is_pdf": False,
                    "is_report_domain": False,
                    "is_news": True,
                    "is_disclosure": False,
                    "query_ids": ["QUERY-VALUATION"],
                    "materiality_query_ids": ["QUERY-VALUATION"],
                    "objective_ids": ["OBJECTIVE-1"],
                    "requested_source_families": [
                        "VALUATION_MULTIPLES"
                    ],
                    "query_lineage_valid": True,
                    "discovery_only": True,
                    "snippet_discovery_only": True,
                    "ranking_status": "NOT_MATERIAL",
                    "fetch_status": "DISCOVERY_ONLY_NOT_FETCHED",
                    "candidate_source_family_hint": "ISSUER_NEWSROOM",
                    "verified_official_domain_candidate": True,
                    "alternate_route_required": True,
                    "materiality_revalidation_reason": (
                        "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
                    ),
                    "matched_requested_source_family": "NONE",
                },
                {
                    "candidate_id": "UNRELATED-BACKLOG",
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "url": backlog_url,
                    "normalized_url": backlog_url,
                    "title": "unrelated inherited candidate",
                    "snippet": None,
                    "source": "example.com",
                    "published_at": "2026-06-19",
                    "rank": 0,
                    "is_pdf": False,
                    "is_report_domain": False,
                    "is_news": False,
                    "is_disclosure": False,
                    "query_ids": ["QUERY-VALUATION"],
                    "objective_ids": ["OBJECTIVE-1"],
                    "requested_source_families": [
                        "VALUATION_MULTIPLES"
                    ],
                    "query_lineage_valid": True,
                    "discovery_only": True,
                    "snippet_discovery_only": True,
                    "ranking_status": "PENDING",
                    "fetch_status": "NOT_STARTED",
                },
                {
                    "candidate_id": "STALE-TERMINAL-SAME-SCOPE",
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "url": stale_terminal_url,
                    "normalized_url": stale_terminal_url,
                    "title": "Current Corp stale official results",
                    "snippet": None,
                    "source": "issuer.example.com",
                    "published_at": "2026-06-18",
                    "rank": 3,
                    "is_pdf": False,
                    "is_report_domain": False,
                    "is_news": True,
                    "is_disclosure": False,
                    "query_ids": ["QUERY-VALUATION"],
                    "materiality_query_ids": ["QUERY-VALUATION"],
                    "objective_ids": ["OBJECTIVE-1"],
                    "requested_source_families": [
                        "VALUATION_MULTIPLES"
                    ],
                    "query_lineage_valid": True,
                    "discovery_only": True,
                    "snippet_discovery_only": True,
                    "ranking_status": "PENDING",
                    "fetch_status": "FETCH_ROUTE_EXHAUSTED",
                    "candidate_source_family_hint": "ISSUER_NEWSROOM",
                    "verified_official_domain_candidate": True,
                    "alternate_route_required": True,
                    "materiality_revalidation_reason": (
                        "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
                    ),
                },
            ],
            query_failures=[
                {
                    "query_id": (
                        "CANDIDATE_QUERY_EDGE:"
                        + candidate_id
                        + ":ISSUER_NEWSROOM"
                    ),
                    "objective_id": "OBJECTIVE-1",
                    "candidate_id": candidate_id,
                    "query_ids": ["QUERY-VALUATION"],
                    "failure_kind": "SOURCE_FAMILY_QUERY_EDGE",
                    "failure_stage": "SOURCE_CANDIDATE_RANKING",
                    "failure_reason": (
                        "LLM_IDENTIFIED_SOURCE_FAMILY_OUTSIDE_QUERY_EDGE"
                    ),
                    "source_family": "ISSUER_NEWSROOM",
                    "requested_source_families": [
                        "VALUATION_MULTIPLES"
                    ],
                    "retryable": True,
                    "alternate_route_required": True,
                    "absence_eligible": False,
                    "resolved": False,
                }
            ],
        )
        persisted_candidate = state["search_candidates"][0]
        persisted_candidate["materiality_decision_id"] = "MATDEC-PERSISTED"
        persisted_candidate["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(
                persisted_candidate
            )
        )
        state["candidate_materiality_decisions"] = [
            {
                "decision_id": "MATDEC-PERSISTED",
                "candidate_id": candidate_id,
                "material_relevance": False,
                "matched_requested_source_family": "NONE",
                "objective_ids": ["OBJECTIVE-1"],
                "priority": 0.12,
                "rationale": (
                    "공식 원문이지만 현재 query edge의 family와 다르다."
                ),
            }
        ]
        state["search_candidates"][1]["material_priority"] = 1.0
        state["query_failures"] = [
            {
                "query_id": (
                    "CANDIDATE_QUERY_EDGE:UNRELATED-BACKLOG:"
                    "ISSUER_NEWSROOM"
                ),
                "objective_id": "OBJECTIVE-1",
                "candidate_id": "UNRELATED-BACKLOG",
                "failure_reason": (
                    "LLM_IDENTIFIED_SOURCE_FAMILY_OUTSIDE_QUERY_EDGE"
                ),
                "source_family": "ISSUER_NEWSROOM",
                "detection_basis": (
                    "LLM_UNRESOLVED_NOTE_CANDIDATE_REFERENCE"
                ),
            }
        ]
        checkpoint = source_graph_module._finalize_checkpoint(state)
        provider = PendingThenCompleteRankingProvider(
            queries=(repair_query,),
            source_families=("ISSUER_NEWSROOM",),
            material_titles=("official preliminary results",),
        )

        first = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    repair_query: (
                        _result(
                            "Current Corp official preliminary results",
                            official_url,
                            query=repair_query,
                        ),
                        _result(
                            "Current Corp alternate official results",
                            alternate_url,
                            rank=2,
                            query=repair_query,
                        ),
                        _result(
                            "Current Corp stale official results",
                            stale_terminal_url,
                            rank=3,
                            query=repair_query,
                        ),
                    )
                }
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={
                    official_url: _document_text("current-results"),
                    alternate_url: _document_text("alternate-results"),
                    stale_terminal_url: _document_text("stale-results"),
                }
            ),
            config=SourceGraphAcquisitionConfig(
                mode="TEST",
                max_results_per_query=3,
                max_queries_per_checkpoint=1,
                max_candidates_per_checkpoint=3,
                max_fetches_per_checkpoint=1,
            ),
            checkpoint=checkpoint,
            official_domains=("issuer.example.com",),
        )

        self.assertIsNotNone(first.query_generation)
        query_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_QUERY_GENERATION"
        )
        serialized_query_failures = json.dumps(
            query_payload["prior_query_or_source_failures"],
            ensure_ascii=False,
        )
        self.assertNotIn(
            "CANDIDATE_QUERY_EDGE:UNRELATED-BACKLOG:ISSUER_NEWSROOM",
            serialized_query_failures,
        )
        self.assertIn(
            "CANDIDATE_QUERY_EDGE:"
            + candidate_id
            + ":ISSUER_NEWSROOM",
            serialized_query_failures,
        )
        first_ranking_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )
        self.assertEqual(
            [
                row["candidate_id"]
                for row in first_ranking_payload["discovery_candidates"]
            ],
            [candidate_id],
        )
        first_repaired = next(
            row
            for row in first.checkpoint["search_candidates"]
            if row["candidate_id"] == candidate_id
        )
        first_backlog = next(
            row
            for row in first.checkpoint["search_candidates"]
            if row["candidate_id"] == "UNRELATED-BACKLOG"
        )
        first_alternate = next(
            row
            for row in first.checkpoint["search_candidates"]
            if row["url"] == alternate_url
        )
        first_stale_terminal = next(
            row
            for row in first.checkpoint["search_candidates"]
            if row["url"] == stale_terminal_url
        )
        self.assertEqual(
            first_repaired["requested_source_families"],
            ["ISSUER_NEWSROOM"],
        )
        self.assertEqual(first_repaired["ranking_status"], "PENDING")
        self.assertEqual(first_backlog["ranking_status"], "PENDING")
        self.assertEqual(first_alternate["ranking_status"], "PENDING")
        self.assertEqual(
            first_repaired[
                "candidate_query_edge_exact_rebound_query_ids"
            ],
            first_repaired["materiality_query_ids"],
        )
        self.assertEqual(first_stale_terminal["ranking_status"], "PENDING")
        self.assertEqual(
            first_stale_terminal["fetch_status"],
            "FETCH_ROUTE_EXHAUSTED",
        )
        self.assertNotIn(
            "candidate_query_edge_exact_rebound_query_ids",
            first_stale_terminal,
        )
        self.assertTrue(
            first.audit[
                "candidate_query_edge_direction_prioritized_over_candidate_backlog"
            ]
        )

        provider.ranking_pending = False
        second = self._run(
            provider=provider,
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(
                fixture_text_by_url={
                    official_url: _document_text("current-results"),
                    alternate_url: _document_text("alternate-results"),
                    stale_terminal_url: _document_text("stale-results"),
                }
            ),
            config=SourceGraphAcquisitionConfig(
                mode="TEST",
                max_results_per_query=3,
                max_queries_per_checkpoint=1,
                max_candidates_per_checkpoint=3,
                max_fetches_per_checkpoint=1,
            ),
            checkpoint=first.checkpoint,
            official_domains=("issuer.example.com",),
        )

        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertEqual(len(ranking_payloads), 2)
        self.assertEqual(
            [
                row["candidate_id"]
                for row in ranking_payloads[-1]["discovery_candidates"]
            ],
            [candidate_id],
        )
        second_by_id = {
            row["candidate_id"]: row
            for row in second.checkpoint["search_candidates"]
        }
        second_alternate = next(
            row
            for row in second.checkpoint["search_candidates"]
            if row["url"] == alternate_url
        )
        second_stale_terminal = next(
            row
            for row in second.checkpoint["search_candidates"]
            if row["url"] == stale_terminal_url
        )
        self.assertEqual(
            second_by_id[candidate_id]["ranking_status"],
            "MATERIAL",
        )
        self.assertEqual(
            second_by_id["UNRELATED-BACKLOG"]["ranking_status"],
            "PENDING",
        )
        self.assertEqual(second_alternate["ranking_status"], "PENDING")
        self.assertEqual(second_stale_terminal["ranking_status"], "PENDING")
        self.assertNotIn(
            "candidate_query_edge_exact_rebound_query_ids",
            second_by_id[candidate_id],
        )
        self.assertIsNone(second.query_generation)
        self.assertFalse(
            second.audit["candidate_query_edge_direction_priority_requested"]
        )
        self.assertTrue(
            second.audit["candidate_query_edge_rebound_priority_requested"]
        )
        self.assertTrue(
            second.audit[
                "candidate_query_edge_direction_prioritized_over_candidate_backlog"
            ]
        )

    def test_candidate_query_edge_exact_rebound_only_shadows_its_scope(
        self,
    ) -> None:
        first_candidate_id = "SGCAND-111111111111111111111111"
        second_candidate_id = "SGCAND-222222222222222222222222"
        first_query = "Current Corp first official newsroom result"
        second_query = "Current Corp second official newsroom result"
        first_url = "https://issuer.example.com/first-original"
        first_alternate_url = "https://issuer.example.com/first-alternate"
        second_url = "https://issuer.example.com/second-original"
        second_alternate_url = "https://issuer.example.com/second-alternate"
        backlog_url = "https://example.com/unrelated-backlog"
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        common = {
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "snippet": None,
            "published_at": "2026-06-20",
            "rank": 1,
            "is_pdf": False,
            "is_report_domain": False,
            "is_news": True,
            "is_disclosure": False,
            "query_lineage_valid": True,
            "discovery_only": True,
            "snippet_discovery_only": True,
        }

        def _repair_candidate(
            *, candidate_id: str, objective_id: str, url: str
        ) -> dict[str, Any]:
            row = {
                **common,
                "candidate_id": candidate_id,
                "url": url,
                "normalized_url": url,
                "title": objective_id + " original official result",
                "source": "issuer.example.com",
                "query_ids": ["OLD-" + objective_id],
                "materiality_query_ids": ["OLD-" + objective_id],
                "objective_ids": [objective_id],
                "requested_source_families": ["VALUATION_MULTIPLES"],
                "ranking_status": "NOT_MATERIAL",
                "fetch_status": "DISCOVERY_ONLY_NOT_FETCHED",
                "candidate_source_family_hint": "ISSUER_NEWSROOM",
                "verified_official_domain_candidate": True,
                "alternate_route_required": True,
                "materiality_revalidation_reason": (
                    "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
                ),
                "matched_requested_source_family": "NONE",
                "materiality_decision_id": "DECISION-" + objective_id,
            }
            row["materiality_scope_hash"] = (
                source_graph_module._candidate_materiality_scope_hash(row)
            )
            return row

        first_candidate = _repair_candidate(
            candidate_id=first_candidate_id,
            objective_id="OBJECTIVE-1",
            url=first_url,
        )
        second_candidate = _repair_candidate(
            candidate_id=second_candidate_id,
            objective_id="OBJECTIVE-2",
            url=second_url,
        )
        backlog = {
            **common,
            "candidate_id": "UNRELATED-BACKLOG",
            "url": backlog_url,
            "normalized_url": backlog_url,
            "title": "unrelated inherited candidate",
            "source": "example.com",
            "query_ids": ["OLD-OBJECTIVE-1"],
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["VALUATION_MULTIPLES"],
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
        }
        state.update(
            status="CHECKPOINT_PENDING",
            generated_queries=[
                {
                    "query_id": "OLD-OBJECTIVE-1",
                    "objective_id": "OBJECTIVE-1",
                    "literal_query": "Current Corp old first valuation",
                    "source_families": ["VALUATION_MULTIPLES"],
                    "execution_status": "SEARCH_EXECUTED",
                },
                {
                    "query_id": "OLD-OBJECTIVE-2",
                    "objective_id": "OBJECTIVE-2",
                    "literal_query": "Current Corp old second valuation",
                    "source_families": ["VALUATION_MULTIPLES"],
                    "execution_status": "SEARCH_EXECUTED",
                },
            ],
            executed_queries=[
                "Current Corp old first valuation",
                "Current Corp old second valuation",
            ],
            search_candidates=[first_candidate, second_candidate, backlog],
            candidate_materiality_decisions=[
                {
                    "decision_id": "DECISION-OBJECTIVE-1",
                    "candidate_id": first_candidate_id,
                    "material_relevance": False,
                    "matched_requested_source_family": "NONE",
                    "objective_ids": ["OBJECTIVE-1"],
                    "priority": 0.9,
                    "rationale": "첫 scope의 현재 query family와 다르다.",
                },
                {
                    "decision_id": "DECISION-OBJECTIVE-2",
                    "candidate_id": second_candidate_id,
                    "material_relevance": False,
                    "matched_requested_source_family": "NONE",
                    "objective_ids": ["OBJECTIVE-2"],
                    "priority": 0.8,
                    "rationale": "둘째 scope의 현재 query family와 다르다.",
                },
            ],
        )
        second_objective = SourceResearchObjective(
            objective_id="OBJECTIVE-2",
            component_id="earnings_visibility",
            research_objective="second official result visibility",
            preferred_source_families=("ISSUER_NEWSROOM",),
            counter_or_supersession_required=True,
        )
        provider = TwoScopeRepairProvider(
            query_by_objective={
                "OBJECTIVE-1": first_query,
                "OBJECTIVE-2": second_query,
            }
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    first_query: (
                        _result(
                            "first exact official result",
                            first_url,
                            query=first_query,
                        ),
                        _result(
                            "first alternate official result",
                            first_alternate_url,
                            rank=2,
                            query=first_query,
                        ),
                    ),
                    second_query: (
                        _result(
                            "second alternate official result",
                            second_alternate_url,
                            query=second_query,
                        ),
                    ),
                }
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={
                    first_url: _document_text("first-exact"),
                    first_alternate_url: _document_text("first-alternate"),
                    second_alternate_url: _document_text("second-alternate"),
                }
            ),
            config=SourceGraphAcquisitionConfig(
                mode="TEST",
                max_results_per_query=2,
                max_queries_per_checkpoint=2,
                max_candidates_per_checkpoint=4,
                max_fetches_per_checkpoint=2,
            ),
            checkpoint=source_graph_module._finalize_checkpoint(state),
            official_domains=("issuer.example.com",),
            official_gaps={
                "OBJECTIVE-1": ("official source gap recorded",),
                "OBJECTIVE-2": ("official source gap recorded",),
            },
            open_objectives=(_objective(), second_objective),
        )

        ranking_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )
        ranked_urls = {
            row["url"]
            for row in ranking_payload["discovery_candidates"]
        }
        self.assertEqual(
            ranked_urls,
            {first_url, second_alternate_url},
        )
        self.assertNotIn(first_alternate_url, ranked_urls)
        self.assertNotIn(backlog_url, ranked_urls)

    def test_candidate_query_edge_alternate_url_closes_then_resumes_backlog(
        self,
    ) -> None:
        candidate_id = "SGCAND-0123456789abcdef01234567"
        original_url = "https://issuer.example.com/current-results"
        alternate_url = "https://issuer.example.com/current-results-mirror"
        ranking_backlog_url = "https://example.com/ranking-backlog"
        fetch_backlog_url = "https://example.com/fetch-backlog"
        repair_query = "Current Corp official preliminary results mirror"
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        common = {
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "snippet": None,
            "published_at": "2026-06-20",
            "rank": 1,
            "is_pdf": False,
            "is_report_domain": False,
            "is_news": True,
            "is_disclosure": False,
            "query_lineage_valid": True,
            "discovery_only": True,
            "snippet_discovery_only": True,
        }
        original = {
            **common,
            "candidate_id": candidate_id,
            "url": original_url,
            "normalized_url": original_url,
            "title": "Current Corp official preliminary results",
            "source": "issuer.example.com",
            "query_ids": ["QUERY-VALUATION"],
            "materiality_query_ids": ["QUERY-VALUATION"],
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["VALUATION_MULTIPLES"],
            "ranking_status": "NOT_MATERIAL",
            "fetch_status": "DISCOVERY_ONLY_NOT_FETCHED",
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "verified_official_domain_candidate": True,
            "alternate_route_required": True,
            "materiality_revalidation_reason": (
                "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
            ),
            "matched_requested_source_family": "NONE",
        }
        ranking_backlog = {
            **common,
            "candidate_id": "UNRELATED-RANKING-BACKLOG",
            "url": ranking_backlog_url,
            "normalized_url": ranking_backlog_url,
            "title": "unrelated ranking backlog",
            "source": "example.com",
            "query_ids": ["QUERY-VALUATION"],
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["VALUATION_MULTIPLES"],
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
        }
        fetch_backlog = {
            **common,
            "candidate_id": "UNRELATED-FETCH-BACKLOG",
            "url": fetch_backlog_url,
            "normalized_url": fetch_backlog_url,
            "title": "unrelated material fetch backlog",
            "source": "example.com",
            "query_ids": ["QUERY-VALUATION"],
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["VALUATION_MULTIPLES"],
            "ranking_status": "MATERIAL",
            "fetch_status": "MATERIAL_PENDING_FETCH",
            "material_priority": 2.0,
            "matched_requested_source_family": "VALUATION_MULTIPLES",
        }
        state.update(
            status="CHECKPOINT_PENDING",
            generated_queries=[
                {
                    "query_id": "QUERY-VALUATION",
                    "objective_id": "OBJECTIVE-1",
                    "literal_query": "Current Corp valuation multiples",
                    "source_families": ["VALUATION_MULTIPLES"],
                    "execution_status": "SEARCH_EXECUTED",
                }
            ],
            executed_queries=["Current Corp valuation multiples"],
            search_candidates=[original, ranking_backlog, fetch_backlog],
            query_failures=[
                {
                    "query_id": (
                        "CANDIDATE_QUERY_EDGE:"
                        + candidate_id
                        + ":ISSUER_NEWSROOM"
                    ),
                    "objective_id": "OBJECTIVE-1",
                    "candidate_id": candidate_id,
                    "failure_reason": (
                        "LLM_IDENTIFIED_SOURCE_FAMILY_OUTSIDE_QUERY_EDGE"
                    ),
                    "source_family": "ISSUER_NEWSROOM",
                    "retryable": True,
                    "resolved": False,
                }
            ],
        )
        original["materiality_decision_id"] = "MATDEC-ORIGINAL"
        original["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(original)
        )
        state["candidate_materiality_decisions"] = [
            {
                "decision_id": "MATDEC-ORIGINAL",
                "candidate_id": candidate_id,
                "material_relevance": False,
                "matched_requested_source_family": "NONE",
                "objective_ids": ["OBJECTIVE-1"],
                "priority": 0.8,
                "rationale": (
                    "공식 원문이지만 현재 query edge의 family와 다르다."
                ),
            }
        ]
        provider = SourceBrainProvider(
            queries=(repair_query,),
            source_families=("ISSUER_NEWSROOM",),
            material_titles=("official preliminary results mirror",),
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                alternate_url: _document_text("alternate-official"),
                fetch_backlog_url: _document_text("fetch-backlog"),
                ranking_backlog_url: _document_text("ranking-backlog"),
            }
        )
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_results_per_query=1,
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=1,
            max_fetches_per_checkpoint=1,
        )

        first = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    repair_query: (
                        _result(
                            "Current Corp official preliminary results mirror",
                            alternate_url,
                            query=repair_query,
                        ),
                    )
                }
            ),
            fetcher=fetcher,
            config=config,
            checkpoint=source_graph_module._finalize_checkpoint(state),
            official_domains=("issuer.example.com",),
        )

        first_by_url = {
            row["url"]: row
            for row in first.checkpoint["search_candidates"]
        }
        self.assertEqual(
            first_by_url[alternate_url]["fetch_status"],
            "FULL_DOCUMENT_FETCHED",
        )
        self.assertEqual(
            first_by_url[fetch_backlog_url]["fetch_status"],
            "MATERIAL_PENDING_FETCH",
        )
        self.assertEqual(
            first_by_url[ranking_backlog_url]["ranking_status"],
            "PENDING",
        )
        first_ranking_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )
        self.assertEqual(
            [
                row["url"]
                for row in first_ranking_payload["discovery_candidates"]
            ],
            [alternate_url],
        )
        self.assertTrue(
            first.audit["candidate_query_edge_direction_priority_requested"]
        )
        self.assertTrue(
            first.audit[
                "candidate_query_edge_direction_prioritized_over_candidate_backlog"
            ]
        )

        second_provider = SourceBrainProvider()
        second = self._run(
            provider=second_provider,
            search=RecordingSearchProvider({}),
            fetcher=fetcher,
            config=config,
            checkpoint=first.checkpoint,
            official_domains=("issuer.example.com",),
        )

        second_by_url = {
            row["url"]: row
            for row in second.checkpoint["search_candidates"]
        }
        self.assertNotEqual(
            second_by_url[ranking_backlog_url]["ranking_status"],
            "PENDING",
        )
        self.assertFalse(
            second.audit["candidate_query_edge_direction_priority_requested"]
        )
        self.assertFalse(
            second.audit[
                "candidate_query_edge_direction_prioritized_over_candidate_backlog"
            ]
        )
        self.assertEqual(
            source_graph_module._unresolved_candidate_source_family_query_edge_failures(
                second.checkpoint["query_failures"],
                candidates=second.checkpoint["search_candidates"],
                generated_queries=second.checkpoint["generated_queries"],
            ),
            (),
        )

    def test_candidate_query_edge_zero_result_is_bounded_and_audited(
        self,
    ) -> None:
        candidate_id = "SGCAND-0123456789abcdef01234567"
        official_url = "https://issuer.example.com/current-results"
        repair_query = "Current Corp official preliminary results newsroom"
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state.update(
            status="CHECKPOINT_PENDING",
            generated_queries=[
                {
                    "query_id": "QUERY-VALUATION",
                    "objective_id": "OBJECTIVE-1",
                    "literal_query": "Current Corp valuation multiples",
                    "source_families": ["VALUATION_MULTIPLES"],
                    "execution_status": "SEARCH_EXECUTED",
                }
            ],
            executed_queries=["Current Corp valuation multiples"],
            search_candidates=[
                {
                    "candidate_id": candidate_id,
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "url": official_url,
                    "normalized_url": official_url,
                    "title": "Current Corp official preliminary results",
                    "source": "issuer.example.com",
                    "published_at": "2026-06-20",
                    "query_ids": ["QUERY-VALUATION"],
                    "materiality_query_ids": ["QUERY-VALUATION"],
                    "objective_ids": ["OBJECTIVE-1"],
                    "requested_source_families": [
                        "VALUATION_MULTIPLES"
                    ],
                    "query_lineage_valid": True,
                    "ranking_status": "NOT_MATERIAL",
                    "fetch_status": "DISCOVERY_ONLY_NOT_FETCHED",
                    "candidate_source_family_hint": "ISSUER_NEWSROOM",
                    "verified_official_domain_candidate": True,
                    "alternate_route_required": True,
                    "materiality_revalidation_reason": (
                        "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
                    ),
                    "matched_requested_source_family": "NONE",
                }
            ],
            query_failures=[
                {
                    "query_id": (
                        "CANDIDATE_QUERY_EDGE:"
                        + candidate_id
                        + ":ISSUER_NEWSROOM"
                    ),
                    "objective_id": "OBJECTIVE-1",
                    "candidate_id": candidate_id,
                    "failure_reason": (
                        "LLM_IDENTIFIED_SOURCE_FAMILY_OUTSIDE_QUERY_EDGE"
                    ),
                    "source_family": "ISSUER_NEWSROOM",
                }
            ],
        )
        zero_result_candidate = state["search_candidates"][0]
        zero_result_candidate["materiality_decision_id"] = (
            "MATDEC-ZERO-RESULT"
        )
        zero_result_candidate["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(
                zero_result_candidate
            )
        )
        state["candidate_materiality_decisions"] = [
            {
                "decision_id": "MATDEC-ZERO-RESULT",
                "candidate_id": candidate_id,
                "material_relevance": False,
                "matched_requested_source_family": "NONE",
                "objective_ids": ["OBJECTIVE-1"],
                "priority": 0.8,
                "rationale": (
                    "공식 원문이지만 현재 query edge의 family와 다르다."
                ),
            }
        ]
        config = SourceGraphAcquisitionConfig(
            mode="TEST",
            max_results_per_query=1,
            max_queries_per_checkpoint=1,
            max_candidates_per_checkpoint=1,
            max_fetches_per_checkpoint=1,
        )
        first_provider = SourceBrainProvider(
            queries=(repair_query,),
            source_families=("ISSUER_NEWSROOM",),
        )
        first_search = RecordingSearchProvider({})

        first = self._run(
            provider=first_provider,
            search=first_search,
            fetcher=PageFetcher(fixture_text_by_url={}),
            config=config,
            checkpoint=source_graph_module._finalize_checkpoint(state),
            official_domains=("issuer.example.com",),
        )

        self.assertEqual(len(first_search.calls), 1)
        self.assertFalse(
            any(
                row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
                for row in first_provider.calls
            )
        )
        self.assertTrue(
            first.audit[
                "candidate_query_edge_direction_prioritized_over_candidate_backlog"
            ]
        )

        second_provider = SourceBrainProvider(
            queries=(repair_query,),
            source_families=("ISSUER_NEWSROOM",),
        )
        second_search = RecordingSearchProvider({})
        second = self._run(
            provider=second_provider,
            search=second_search,
            fetcher=PageFetcher(fixture_text_by_url={}),
            config=config,
            checkpoint=first.checkpoint,
            official_domains=("issuer.example.com",),
        )

        self.assertEqual(second.status, "QUERY_GENERATION_PENDING")
        self.assertEqual(second_search.calls, [])
        self.assertIsNotNone(second.query_generation)
        self.assertEqual(second.query_generation.queries, ())
        self.assertTrue(
            second.audit["candidate_query_edge_direction_priority_requested"]
        )
        self.assertFalse(
            second.audit[
                "candidate_query_edge_direction_prioritized_over_candidate_backlog"
            ]
        )

    def test_candidate_query_edge_duplicate_content_closes_repair(self) -> None:
        candidate_id = "SGCAND-0123456789abcdef01234567"
        failure = {
            "query_id": (
                "CANDIDATE_QUERY_EDGE:"
                + candidate_id
                + ":ISSUER_NEWSROOM"
            ),
            "objective_id": "OBJECTIVE-1",
            "candidate_id": candidate_id,
            "failure_reason": (
                "LLM_IDENTIFIED_SOURCE_FAMILY_OUTSIDE_QUERY_EDGE"
            ),
            "source_family": "ISSUER_NEWSROOM",
        }
        original = {
            "candidate_id": candidate_id,
            "requested_source_families": ["VALUATION_MULTIPLES"],
        }
        duplicate_route = {
            "candidate_id": "SGCAND-fedcba9876543210fedcba98",
            "normalized_url": (
                "https://issuer.example.com/current-results-mirror"
            ),
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["ISSUER_NEWSROOM"],
            "materiality_query_ids": ["QUERY-REPAIR"],
            "matched_requested_source_family": "ISSUER_NEWSROOM",
            "ranking_status": "MATERIAL",
            "fetch_status": "DUPLICATE_CONTENT",
            "document_id": "SGDOC-existing-document",
        }
        duplicate_route["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(
                duplicate_route
            )
        )

        unresolved = source_graph_module._unresolved_candidate_source_family_query_edge_failures(
            (failure,),
            candidates=(original, duplicate_route),
            generated_queries=(
                {
                    "query_id": "QUERY-REPAIR",
                    "objective_id": "OBJECTIVE-1",
                    "source_families": ["ISSUER_NEWSROOM"],
                    "execution_status": "SEARCH_EXECUTED",
                },
            ),
        )

        self.assertEqual(unresolved, ())

    def test_candidate_query_edge_uses_llm_priority_per_scope(self) -> None:
        high_id = "SGCAND-0123456789abcdef01234567"
        low_id = "SGCAND-fedcba9876543210fedcba98"
        candidates = (
            {
                "candidate_id": high_id,
                "material_priority": 0.12,
                "rank": 2,
            },
            {
                "candidate_id": low_id,
                "material_priority": 0.03,
                "rank": 12,
            },
        )
        failures = tuple(
            {
                "query_id": "CANDIDATE_QUERY_EDGE:" + candidate_id,
                "candidate_id": candidate_id,
                "objective_id": "OBJECTIVE-1",
                "source_family": "ISSUER_NEWSROOM",
                "failure_reason": (
                    "LLM_IDENTIFIED_SOURCE_FAMILY_OUTSIDE_QUERY_EDGE"
                ),
            }
            for candidate_id in (low_id, high_id)
        )

        selected = source_graph_module._prioritize_candidate_source_family_query_edge_failures(
            failures,
            candidates=candidates,
        )

        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["candidate_id"], high_id)

    def test_graph_keeps_official_structured_independent_and_reference_expansion(self) -> None:
        provider = SourceBrainProvider()
        web_url = "https://www.reuters.com/current-report"
        official = (
            _official_document("OFFICIAL", "OPENDART"),
            _official_document("STRUCTURED", "FINANCIAL_STATEMENTS"),
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {QUERY: (_result("Current Corp Reuters", web_url),)}
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={
                    web_url: _document_text("independent")
                    + " https://current.example.com/investor-relations"
                }
            ),
            official_documents=official,
        )
        families = {row.source_family for row in run.source_graph.nodes}
        self.assertTrue({"OPENDART", "FINANCIAL_STATEMENTS", "REUTERS"}.issubset(families))
        self.assertTrue(
            any(
                row.metadata.get("graph_expansion_parent_document_ids")
                for row in run.source_graph.nodes
                if row.node_type == "SEARCH_CANDIDATE"
            )
        )
        self.assertIn(
            "REFERENCES_URL", {row.relationship for row in run.source_graph.edges}
        )

    def test_reference_url_is_ranked_and_fetched_on_checkpoint_resume(self) -> None:
        provider = SourceBrainProvider()
        parent_url = "https://example.com/parent"
        child_url = "https://example.com/child"
        fetcher = PageFetcher(
            fixture_text_by_url={
                parent_url: _document_text("parent") + f" {child_url}",
                child_url: _document_text("child-original-source"),
            }
        )
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp parent", parent_url),)}
        )
        first = self._run(provider=provider, search=search, fetcher=fetcher)
        self.assertEqual(len(first.evidence_documents), 1)
        self.assertTrue(
            any(
                row.get("graph_expansion_parent_document_ids")
                for row in first.checkpoint["search_candidates"]
            )
        )
        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=first.checkpoint,
        )
        self.assertEqual(len(second.evidence_documents), 2)
        self.assertEqual(len(search.calls), 1)

    def test_future_dart_reference_locator_is_rejected_before_resume_ranking(
        self,
    ) -> None:
        provider = SourceBrainProvider(
            source_families=("ISSUER_PRESENTATION",),
        )
        parent_url = "https://ir.example.com/redirect"
        child_url = (
            "https://englishdart.fss.or.kr/dsbh001/main.do"
            "?rcpNo=20260716000552"
        )
        fetcher = ReferencedRouteFetcher(
            parent_url=parent_url,
            child_url=child_url,
        )
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp official call", parent_url),)}
        )
        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            official_domains=("example.com",),
        )
        child_candidate = next(
            row
            for row in first.checkpoint["search_candidates"]
            if row.get("url") == child_url
        )
        self.assertEqual(child_candidate["ranking_status"], "PENDING")
        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=first.checkpoint,
            official_domains=("example.com",),
        )
        child_candidate = next(
            row
            for row in second.checkpoint["search_candidates"]
            if row.get("url") == child_url
        )
        self.assertEqual(child_candidate["ranking_status"], "REJECTED_FUTURE")
        self.assertEqual(child_candidate["fetch_status"], "FETCH_REJECTED")
        self.assertNotIn(child_url, fetcher.calls)
        ranking_payloads = [
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        ]
        self.assertTrue(
            all(
                "20260716000552"
                not in json.dumps(payload, ensure_ascii=False)
                for payload in ranking_payloads
            )
        )
        matching_rejections = [
            row
            for row in second.checkpoint["rejected_documents"]
            if row.get("candidate_id") == child_candidate["candidate_id"]
            and row.get("rejection_reason")
            == "FUTURE_CANDIDATE_SOURCE_LOCATOR_DATE"
        ]
        self.assertEqual(len(matching_rejections), 1)
        self.assertTrue(
            matching_rejections[0]["future_candidate_rejected_before_llm"]
        )

    def test_rejected_parent_still_discovers_and_fetches_linked_original(self) -> None:
        provider = SourceBrainProvider(
            source_families=("ISSUER_PRESENTATION",),
        )
        parent_url = "https://ir.example.com/redirect"
        child_url = "https://ir.example.com/2026q1-transcript.pdf"
        fetcher = ReferencedRouteFetcher(
            parent_url=parent_url,
            child_url=child_url,
        )
        search = RecordingSearchProvider(
            {QUERY: (_result("Current Corp official call", parent_url),)}
        )

        first = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            official_domains=("example.com",),
        )
        child_candidate = next(
            row
            for row in first.checkpoint["search_candidates"]
            if row.get("url") == child_url
        )
        self.assertEqual(child_candidate["ranking_status"], "PENDING")
        self.assertTrue(child_candidate["graph_expansion_parent_candidate_ids"])
        self.assertIn(
            "REFERENCES_URL",
            {row.relationship for row in first.source_graph.edges},
        )
        self.assertTrue(
            any(
                row.get("rejection_reason") == "FULL_DOCUMENT_CONTENT_TOO_SMALL"
                for row in first.checkpoint["rejected_documents"]
            )
        )

        second = self._run(
            provider=provider,
            search=search,
            fetcher=fetcher,
            checkpoint=first.checkpoint,
            official_domains=("example.com",),
        )
        linked_document = next(
            row
            for row in second.evidence_documents
            if row.get("canonical_url") == child_url
        )
        self.assertEqual(linked_document["source_family"], "ISSUER_NEWSROOM")
        self.assertEqual(
            linked_document["requested_source_families"],
            ["ISSUER_PRESENTATION"],
        )
        self.assertEqual(len(search.calls), 1)

    def test_unverified_page_navigation_is_not_graph_expanded(self) -> None:
        provider = SourceBrainProvider()
        parent_url = "https://media.example.net/article"
        navigation_url = "https://www.naver.com"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {QUERY: (_result("Current Corp media page", parent_url),)}
            ),
            fetcher=ReferencedRouteFetcher(
                parent_url=parent_url,
                child_url=navigation_url,
                parent_text=_document_text("accepted-media-page-with-menu-link"),
            ),
        )
        self.assertEqual(len(run.evidence_documents), 1)
        self.assertFalse(
            any(
                row.get("url") == navigation_url
                for row in run.checkpoint["search_candidates"]
            )
        )

    def test_failed_official_frame_page_still_discovers_linked_route(self) -> None:
        provider = SourceBrainProvider(
            source_families=("ISSUER_PRESENTATION",),
        )
        parent_url = "https://ir.example.com/frameset"
        child_url = "https://ir.example.com/transcript.pdf"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {QUERY: (_result("Current Corp official frameset", parent_url),)}
            ),
            fetcher=ReferencedRouteFetcher(
                parent_url=parent_url,
                child_url=child_url,
                parent_ok=False,
            ),
            official_domains=("example.com",),
        )
        child = next(
            row
            for row in run.checkpoint["search_candidates"]
            if row.get("url") == child_url
        )
        self.assertEqual(child["ranking_status"], "PENDING")
        self.assertEqual(
            child["graph_expansion_parent_candidate_ids"],
            [
                next(
                    row["candidate_id"]
                    for row in run.checkpoint["search_candidates"]
                    if row.get("url") == parent_url
                )
            ],
        )

    def test_official_reference_expansion_skips_navigation_only_urls(self) -> None:
        parent = {
            "candidate_id": "OFFICIAL-ARTICLE",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "url": "https://issuer.example.com/news/current-results",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "objective_ids": ["OBJECTIVE-1"],
            "query_ids": ["QUERY-1"],
            "requested_source_families": ["ISSUER_NEWSROOM"],
            "discovered_referenced_urls": [
                "https://issuer.example.com/tag/results",
                "https://issuer.example.com/category/press",
                "https://issuer.example.com/page/2/",
                "https://issuer.example.com/?s=HBM4",
                "https://issuer.example.com/news/customer-allocation-update",
                "https://issuer.example.com/category/results/earnings.pdf",
            ],
        }
        _bind_candidate_reference_scope(
            parent,
            decision_id="DECISION-OFFICIAL-ARTICLE",
        )
        candidates = [parent]

        deferred = source_graph_module._enqueue_candidate_discovery_references(
            candidates,
            parent_candidate=parent,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
        )

        self.assertEqual(deferred, 0)
        self.assertEqual(
            [row["url"] for row in candidates[1:]],
            [
                "https://issuer.example.com/category/results/earnings.pdf",
                "https://issuer.example.com/news/customer-allocation-update",
            ],
        )

    def test_source_document_reference_keeps_cited_article_and_pdf_only(
        self,
    ) -> None:
        article_url = "https://issuer.example.com/news/customer-allocation-update"
        pdf_url = "https://issuer.example.com/category/results/earnings.pdf"
        document = {
            "document_id": "DOC-OFFICIAL-ARTICLE",
            "canonical_url": "https://issuer.example.com/news/current-results",
            "content_text": (
                f"본문은 원문 기사 {article_url}와 실적표 {pdf_url}를 직접 인용한다."
            ),
            "source_family": "ISSUER_NEWSROOM",
            "objective_ids": ["OBJECTIVE-1"],
            "query_ids": ["QUERY-1"],
            "requested_source_families": ["ISSUER_NEWSROOM"],
            "referenced_urls": [
                "https://issuer.example.com/tag/results",
                "https://issuer.example.com/category/press",
                "https://issuer.example.com/page/2/",
                "https://issuer.example.com/?s=HBM4",
                article_url,
                pdf_url,
            ],
        }
        _bind_document_reference_scope(
            document,
            decision_id="DECISION-OFFICIAL-DOCUMENT",
        )
        candidates = []

        deferred = source_graph_module._enqueue_reference_candidates(
            candidates,
            document=document,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            default_objective_ids=("OBJECTIVE-1",),
        )

        self.assertEqual(deferred, 0)
        self.assertEqual(
            [row["url"] for row in candidates],
            [pdf_url, article_url],
        )
        self.assertTrue(
            all(
                row["graph_expansion_parent_document_ids"]
                == ["DOC-OFFICIAL-ARTICLE"]
                for row in candidates
            )
        )

    def test_legacy_candidate_reference_cannot_widen_direct_current_edge(
        self,
    ) -> None:
        child_url = "https://issuer.example.com/reports/current.pdf"
        parent = {
            "candidate_id": "LEGACY-PARENT",
            "url": "https://issuer.example.com/reports",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "query_ids": ["OLD-QUERY-1", "OLD-QUERY-2"],
            "objective_ids": ["OLD-OBJECTIVE-1", "OLD-OBJECTIVE-2"],
            "requested_source_families": [
                "GENERAL_WEB_DISCOVERY",
                "ISSUER_NEWSROOM",
            ],
            "discovered_referenced_urls": [child_url],
        }
        child = {
            "candidate_id": "DIRECT-CHILD",
            "url": child_url,
            "normalized_url": child_url,
            "query_ids": ["CURRENT-QUERY"],
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["FINANCIAL_STATEMENTS"],
            "direct_search_discovery": True,
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
        }
        candidates = [parent, child]

        deferred = source_graph_module._enqueue_candidate_discovery_references(
            candidates,
            parent_candidate=parent,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
        )

        self.assertEqual(deferred, 0)
        self.assertEqual(child["materiality_query_ids"], ["CURRENT-QUERY"])
        self.assertEqual(child["objective_ids"], ["CURRENT-OBJECTIVE"])
        self.assertEqual(
            child["requested_source_families"],
            ["FINANCIAL_STATEMENTS"],
        )
        self.assertEqual(
            child["graph_expansion_parent_candidate_ids"],
            ["LEGACY-PARENT"],
        )
        self.assertTrue(
            {"OLD-QUERY-1", "OLD-QUERY-2"}.issubset(child["query_ids"])
        )

    def test_verified_candidate_reference_inherits_only_current_edge(
        self,
    ) -> None:
        child_url = "https://issuer.example.com/reports/current.pdf"
        parent = {
            "candidate_id": "CURRENT-PARENT",
            "url": "https://issuer.example.com/reports/current",
            "normalized_url": "https://issuer.example.com/reports/current",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "query_ids": ["OLD-QUERY", "CURRENT-QUERY"],
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["ISSUER_NEWSROOM"],
            "matched_requested_source_family": "ISSUER_NEWSROOM",
            "materiality_decision_id": "DECISION-CURRENT-PARENT",
            "ranking_status": "MATERIAL",
            "fetch_status": "FETCH_REJECTED",
            "discovered_referenced_urls": [child_url],
        }
        parent["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(parent)
        )
        candidates = [parent]

        source_graph_module._enqueue_candidate_discovery_references(
            candidates,
            parent_candidate=parent,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
        )

        child = candidates[1]
        self.assertEqual(child["materiality_query_ids"], ["CURRENT-QUERY"])
        self.assertEqual(child["objective_ids"], ["CURRENT-OBJECTIVE"])
        self.assertEqual(
            child["requested_source_families"],
            ["ISSUER_NEWSROOM"],
        )
        self.assertEqual(child["ranking_status"], "PENDING")
        self.assertEqual(child["fetch_status"], "NOT_STARTED")
        self.assertIn("OLD-QUERY", child["query_ids"])

    def test_legacy_document_reference_cannot_widen_direct_current_edge(
        self,
    ) -> None:
        child_url = "https://issuer.example.com/reports/current.pdf"
        child = {
            "candidate_id": "DIRECT-CHILD",
            "url": child_url,
            "normalized_url": child_url,
            "query_ids": ["CURRENT-QUERY"],
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["FINANCIAL_STATEMENTS"],
            "direct_search_discovery": True,
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
        }
        document = {
            "document_id": "LEGACY-DOCUMENT",
            "canonical_url": "https://issuer.example.com/reports",
            "source_family": "ISSUER_NEWSROOM",
            "query_ids": ["OLD-QUERY"],
            "objective_ids": ["OLD-OBJECTIVE"],
            "requested_source_families": ["GENERAL_WEB_DISCOVERY"],
            "referenced_urls": [child_url],
        }

        source_graph_module._enqueue_reference_candidates(
            [child],
            document=document,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            default_objective_ids=("OLD-OBJECTIVE",),
        )

        self.assertEqual(child["materiality_query_ids"], ["CURRENT-QUERY"])
        self.assertEqual(child["objective_ids"], ["CURRENT-OBJECTIVE"])
        self.assertEqual(
            child["requested_source_families"],
            ["FINANCIAL_STATEMENTS"],
        )
        self.assertEqual(
            child["graph_expansion_parent_document_ids"],
            ["LEGACY-DOCUMENT"],
        )

    def test_verified_document_reference_inherits_only_materiality_edge(
        self,
    ) -> None:
        parent_url = "https://issuer.example.com/reports/current"
        child_url = "https://issuer.example.com/reports/current.pdf"
        document = {
            "document_id": "CURRENT-DOCUMENT",
            "canonical_url": parent_url,
            "source_family": "ISSUER_NEWSROOM",
            "query_ids": ["OLD-QUERY", "CURRENT-QUERY"],
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["ISSUER_NEWSROOM"],
            "matched_requested_source_family": "ISSUER_NEWSROOM",
            "source_materiality_decision_id": (
                "DECISION-CURRENT-DOCUMENT"
            ),
            "materiality_scope_url": parent_url,
            "referenced_urls": [child_url],
        }
        document["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(
                {
                    "normalized_url": parent_url,
                    "objective_ids": document["objective_ids"],
                    "requested_source_families": document[
                        "requested_source_families"
                    ],
                }
            )
        )
        candidates = []

        source_graph_module._enqueue_reference_candidates(
            candidates,
            document=document,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            default_objective_ids=("CURRENT-OBJECTIVE",),
        )

        child = candidates[0]
        self.assertEqual(child["materiality_query_ids"], ["CURRENT-QUERY"])
        self.assertEqual(child["objective_ids"], ["CURRENT-OBJECTIVE"])
        self.assertEqual(
            child["requested_source_families"],
            ["ISSUER_NEWSROOM"],
        )
        self.assertEqual(child["ranking_status"], "PENDING")
        self.assertEqual(child["fetch_status"], "NOT_STARTED")

    def test_resume_reconciles_reference_pollution_to_exact_query_edge(
        self,
    ) -> None:
        current_query = {
            "query_id": "CURRENT-QUERY",
            "objective_id": "CURRENT-OBJECTIVE",
            "source_families": [
                "CASH_FLOW",
                "FINANCIAL_STATEMENTS",
            ],
        }
        candidate = {
            "candidate_id": "POLLUTED-CANDIDATE",
            "url": "https://issuer.example.com/reports/current.pdf",
            "normalized_url": (
                "https://issuer.example.com/reports/current.pdf"
            ),
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": [
                "CURRENT-OBJECTIVE",
                "LEGACY-OBJECTIVE",
            ],
            "requested_source_families": [
                "CASH_FLOW",
                "FINANCIAL_STATEMENTS",
                "GENERAL_WEB_DISCOVERY",
            ],
            "matched_requested_source_family": "CASH_FLOW",
            "materiality_decision_id": "DECISION-1",
            "ranking_status": "MATERIAL",
            "fetch_status": "FULL_DOCUMENT_FETCHED",
            "document_id": "DOCUMENT-1",
        }
        expected_scope = {
            **candidate,
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": [
                "CASH_FLOW",
                "FINANCIAL_STATEMENTS",
            ],
        }
        candidate["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(
                expected_scope
            )
        )

        repaired = (
            source_graph_module._reconcile_candidate_current_query_edge_scopes(
                [candidate],
                [current_query],
                [
                    {
                        "decision_id": "DECISION-1",
                        "candidate_id": "POLLUTED-CANDIDATE",
                        "material_relevance": True,
                        "objective_ids": ["CURRENT-OBJECTIVE"],
                        "matched_requested_source_family": "CASH_FLOW",
                    }
                ],
            )
        )

        self.assertEqual(repaired, 1)
        self.assertEqual(candidate["objective_ids"], ["CURRENT-OBJECTIVE"])
        self.assertEqual(
            candidate["requested_source_families"],
            ["CASH_FLOW", "FINANCIAL_STATEMENTS"],
        )
        self.assertEqual(candidate["materiality_decision_id"], "DECISION-1")
        self.assertEqual(candidate["ranking_status"], "MATERIAL")
        self.assertEqual(candidate["fetch_status"], "FULL_DOCUMENT_FETCHED")
        self.assertTrue(
            candidate[
                "current_query_edge_scope_reused_exact_prior_decision"
            ]
        )

    def test_resume_reconciles_unbound_terminal_decision_for_reranking(
        self,
    ) -> None:
        candidate = {
            "candidate_id": "UNBOUND-CANDIDATE",
            "url": "https://issuer.example.com/reports/current.pdf",
            "normalized_url": (
                "https://issuer.example.com/reports/current.pdf"
            ),
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": [
                "CURRENT-OBJECTIVE",
                "LEGACY-OBJECTIVE",
            ],
            "requested_source_families": [
                "FINANCIAL_STATEMENTS",
                "GENERAL_WEB_DISCOVERY",
            ],
            "matched_requested_source_family": "FINANCIAL_STATEMENTS",
            "materiality_decision_id": "UNBOUND-DECISION",
            "ranking_status": "MATERIAL",
            "fetch_status": "FETCH_REJECTED",
        }

        repaired = (
            source_graph_module._reconcile_candidate_current_query_edge_scopes(
                [candidate],
                [
                    {
                        "query_id": "CURRENT-QUERY",
                        "objective_id": "CURRENT-OBJECTIVE",
                        "source_families": ["FINANCIAL_STATEMENTS"],
                    }
                ],
            )
        )

        self.assertEqual(repaired, 1)
        self.assertEqual(candidate["ranking_status"], "PENDING")
        self.assertEqual(candidate["fetch_status"], "FETCH_REJECTED")
        self.assertEqual(
            candidate[
                "terminal_fetch_status_before_materiality_revalidation"
            ],
            "FETCH_REJECTED",
        )
        self.assertNotIn("materiality_decision_id", candidate)
        self.assertNotIn("matched_requested_source_family", candidate)

    def test_resume_reopens_same_scope_without_bound_decision(self) -> None:
        candidate = {
            "candidate_id": "MISSING-DECISION-CANDIDATE",
            "url": "https://issuer.example.com/reports/current.pdf",
            "normalized_url": (
                "https://issuer.example.com/reports/current.pdf"
            ),
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["FINANCIAL_STATEMENTS"],
            "matched_requested_source_family": "FINANCIAL_STATEMENTS",
            "materiality_decision_id": "MISSING-DECISION",
            "ranking_status": "MATERIAL",
            "fetch_status": "FULL_DOCUMENT_FETCHED",
            "document_id": "DOCUMENT-1",
        }
        candidate["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(candidate)
        )

        repaired = (
            source_graph_module._reconcile_candidate_current_query_edge_scopes(
                [candidate],
                [
                    {
                        "query_id": "CURRENT-QUERY",
                        "objective_id": "CURRENT-OBJECTIVE",
                        "source_families": ["FINANCIAL_STATEMENTS"],
                    }
                ],
                (),
            )
        )

        self.assertEqual(repaired, 1)
        self.assertEqual(candidate["ranking_status"], "PENDING")
        self.assertEqual(
            candidate["fetch_status"],
            "FULL_DOCUMENT_REVALIDATION_PENDING",
        )
        self.assertEqual(candidate["revalidation_document_id"], "DOCUMENT-1")
        self.assertNotIn("materiality_decision_id", candidate)

    def test_material_decision_with_none_family_cannot_be_reused(
        self,
    ) -> None:
        candidate = {
            "candidate_id": "NONE-FAMILY-CANDIDATE",
            "url": "https://issuer.example.com/reports/current.pdf",
            "normalized_url": (
                "https://issuer.example.com/reports/current.pdf"
            ),
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["FINANCIAL_STATEMENTS"],
            "matched_requested_source_family": "NONE",
            "materiality_decision_id": "DECISION-NONE",
            "ranking_status": "MATERIAL",
            "fetch_status": "FULL_DOCUMENT_FETCHED",
            "document_id": "DOCUMENT-1",
        }
        candidate["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(candidate)
        )

        source_graph_module._reconcile_candidate_current_query_edge_scopes(
            [candidate],
            [
                {
                    "query_id": "CURRENT-QUERY",
                    "objective_id": "CURRENT-OBJECTIVE",
                    "source_families": ["FINANCIAL_STATEMENTS"],
                }
            ],
            [
                {
                    "decision_id": "DECISION-NONE",
                    "candidate_id": "NONE-FAMILY-CANDIDATE",
                    "material_relevance": True,
                    "objective_ids": ["CURRENT-OBJECTIVE"],
                    "matched_requested_source_family": "NONE",
                }
            ],
        )

        self.assertEqual(candidate["ranking_status"], "PENDING")
        self.assertEqual(
            candidate["fetch_status"],
            "FULL_DOCUMENT_REVALIDATION_PENDING",
        )
        self.assertNotIn("materiality_decision_id", candidate)

    def test_direct_search_reopens_dormant_reference_candidate(self) -> None:
        url = "https://issuer.example.com/reports/current.pdf"
        existing = {
            "candidate_id": "DORMANT-REFERENCE",
            "url": url,
            "normalized_url": url,
            "query_ids": ["PARENT-QUERY"],
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["FINANCIAL_STATEMENTS"],
            "ranking_status": "NOT_MATERIAL",
            "fetch_status": (
                "REFERENCE_DISCOVERY_PENDING_PARENT_REVALIDATION"
            ),
        }
        direct = {
            "candidate_id": "DIRECT-RESULT",
            "url": url,
            "normalized_url": url,
            "query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["FINANCIAL_STATEMENTS"],
            "query_lineage_valid": True,
            "direct_search_discovery": True,
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
        }

        source_graph_module._merge_search_candidates(
            [existing],
            [],
            [direct],
            cutoff=date.fromisoformat(AS_OF_DATE),
        )

        self.assertTrue(existing["direct_search_discovery"])
        self.assertEqual(existing["ranking_status"], "PENDING")
        self.assertEqual(existing["fetch_status"], "NOT_STARTED")

    def test_reference_scope_adoption_preserves_terminal_transport(
        self,
    ) -> None:
        child_url = "https://issuer.example.com/reports/current.pdf"
        parent = {
            "candidate_id": "CURRENT-PARENT",
            "url": "https://issuer.example.com/reports/current",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["ISSUER_NEWSROOM"],
            "discovered_referenced_urls": [child_url],
        }
        _bind_candidate_reference_scope(
            parent,
            decision_id="DECISION-CURRENT-PARENT",
        )
        child = {
            "candidate_id": "TERMINAL-CHILD",
            "url": child_url,
            "normalized_url": child_url,
            "query_ids": ["LEGACY-QUERY"],
            "objective_ids": ["LEGACY-OBJECTIVE"],
            "requested_source_families": ["GENERAL_WEB_DISCOVERY"],
            "ranking_status": "NOT_MATERIAL",
            "fetch_status": "FETCH_REJECTED",
        }

        source_graph_module._enqueue_candidate_discovery_references(
            [parent, child],
            parent_candidate=parent,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
        )

        self.assertEqual(child["ranking_status"], "PENDING")
        self.assertEqual(child["fetch_status"], "FETCH_REJECTED")
        self.assertEqual(
            child[
                "terminal_fetch_status_before_materiality_revalidation"
            ],
            "FETCH_REJECTED",
        )

    def test_unproven_parent_edges_create_no_new_candidate(self) -> None:
        child_url = "https://issuer.example.com/reports/current.pdf"
        parent = {
            "candidate_id": "UNPROVEN-PARENT",
            "url": "https://issuer.example.com/reports/current",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "query_ids": ["CURRENT-QUERY"],
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["ISSUER_NEWSROOM"],
            "matched_requested_source_family": "ISSUER_NEWSROOM",
            "ranking_status": "MATERIAL",
            "discovered_referenced_urls": [child_url],
        }
        parent["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(parent)
        )
        candidates = [parent]
        source_graph_module._enqueue_candidate_discovery_references(
            candidates,
            parent_candidate=parent,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
        )
        self.assertEqual(candidates, [parent])

        document = {
            "document_id": "UNPROVEN-DOCUMENT",
            "canonical_url": parent["url"],
            "source_family": "ISSUER_NEWSROOM",
            "query_ids": ["CURRENT-QUERY"],
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["ISSUER_NEWSROOM"],
            "matched_requested_source_family": "ISSUER_NEWSROOM",
            "materiality_scope_hash": parent["materiality_scope_hash"],
            "referenced_urls": [child_url],
        }
        document_candidates: list[dict[str, Any]] = []
        source_graph_module._enqueue_reference_candidates(
            document_candidates,
            document=document,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            default_objective_ids=("CURRENT-OBJECTIVE",),
        )
        self.assertEqual(document_candidates, [])

    def test_duplicate_document_adopts_url_bound_current_provenance(
        self,
    ) -> None:
        original_url = "https://mirror.example.net/report"
        current_url = "https://issuer.example.com/report"
        text = _document_text("same-bytes-different-url")
        content_hash = hashlib.sha256(
            text.strip().encode("utf-8")
        ).hexdigest()
        published_at = "2026-06-20"
        existing_document_id = source_graph_module.stable_intelligence_id(
            "SGDOC",
            {
                "target_id": TARGET,
                "content_hash": content_hash,
                "published_at": published_at,
            },
        )
        existing_document = {
            "document_id": existing_document_id,
            "target_id": TARGET,
            "canonical_url": original_url,
            "source_provider": "PageFetcher",
            "source_family": "GENERAL_WEB_DISCOVERY",
            "published_at": published_at,
            "content_hash": content_hash,
            "content_text": text.strip(),
            "full_fetch_performed": True,
            "evidence_eligible": True,
            "snippet_only": False,
            "snippet_used_as_document": False,
            "query_ids": ["LEGACY-QUERY"],
            "objective_ids": ["LEGACY-OBJECTIVE"],
            "requested_source_families": ["GENERAL_WEB_DISCOVERY"],
        }
        candidate = {
            "candidate_id": "CURRENT-DUPLICATE",
            "url": current_url,
            "normalized_url": current_url,
            "query_ids": ["CURRENT-QUERY"],
            "materiality_query_ids": ["CURRENT-QUERY"],
            "objective_ids": ["CURRENT-OBJECTIVE"],
            "requested_source_families": ["ISSUER_NEWSROOM"],
            "matched_requested_source_family": "ISSUER_NEWSROOM",
            "materiality_decision_id": "DECISION-CURRENT-DUPLICATE",
            "ranking_status": "MATERIAL",
            "published_at": published_at,
        }
        candidate["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(candidate)
        )

        record, document, rejection = (
            source_graph_module._fetch_candidate_document(
                candidate=candidate,
                target_id=TARGET,
                target_name=TARGET_NAME,
                target_aliases=(),
                as_of_date=date.fromisoformat(AS_OF_DATE),
                page_fetcher=PageFetcher(
                    fixture_text_by_url={current_url: text}
                ),
                min_chars=10,
                require_date_verified=True,
                official_hosts={"issuer.example.com"},
                content_hash_to_document={
                    content_hash: existing_document
                },
            )
        )

        self.assertIsNone(rejection)
        self.assertEqual(record["disposition"], "DUPLICATE_CONTENT")
        self.assertIs(document, existing_document)
        self.assertEqual(
            document["materiality_scope_url"],
            current_url,
        )
        self.assertEqual(
            document["source_materiality_decision_id"],
            "DECISION-CURRENT-DUPLICATE",
        )
        self.assertIsNotNone(
            source_graph_module._validated_reference_materiality_scope(
                document
            )
        )
        candidate["document_id"] = record["existing_document_id"]
        active = source_graph_module._production_downstream_documents(
            documents=(document,),
            facts=(),
            candidates=(candidate,),
            materiality_decisions=(
                {
                    "candidate_id": candidate["candidate_id"],
                    "decision_id": candidate["materiality_decision_id"],
                    "material_relevance": True,
                    "matched_requested_source_family": (
                        "ISSUER_NEWSROOM"
                    ),
                    "objective_ids": candidate["objective_ids"],
                },
            ),
            fetch_records=(record,),
        )
        self.assertEqual(active, (document,))

        forged_current_document = {
            **document,
            "content_text": "forged current bytes",
            "full_fetch_performed": False,
            "evidence_eligible": False,
        }
        self.assertEqual(
            source_graph_module._production_downstream_documents(
                documents=(forged_current_document,),
                facts=(),
                candidates=(candidate,),
                materiality_decisions=(
                    {
                        "candidate_id": candidate["candidate_id"],
                        "decision_id": candidate["materiality_decision_id"],
                        "material_relevance": True,
                        "matched_requested_source_family": (
                            "ISSUER_NEWSROOM"
                        ),
                        "objective_ids": candidate["objective_ids"],
                    },
                ),
                fetch_records=(record,),
            ),
            (),
        )

    def test_navigation_url_classifier_keeps_documents_and_articles(self) -> None:
        navigation_urls = (
            "https://issuer.example.com/tag/results",
            "https://issuer.example.com/category/press/",
            "https://issuer.example.com/en/page/6/?topic=HBM4",
            "https://issuer.example.com/?s=HBM4",
            "https://issuer.example.com/search?keyword=HBM4",
        )
        retained_urls = (
            "https://issuer.example.com/news/customer-allocation-update",
            "https://issuer.example.com/category/results/earnings.pdf",
            "https://englishdart.fss.or.kr/dsbh001/main.do?rcpNo=20260601000123",
            "https://issuer.example.com/news/article?page=2",
            "https://issuer.example.com/archive/2026Q1/transcript",
        )

        for url in navigation_urls:
            with self.subTest(url=url):
                self.assertTrue(
                    source_graph_module._is_navigation_only_reference_url(url)
                )
        for url in retained_urls:
            with self.subTest(url=url):
                self.assertFalse(
                    source_graph_module._is_navigation_only_reference_url(url)
                )

    def test_persisted_navigation_url_closes_without_discarding_articles(self) -> None:
        candidates = [
            {
                "candidate_id": "DIRECT-NAV-PARENT",
                "url": "https://issuer.example.com/tag/results",
                "direct_search_discovery": True,
                "ranking_status": "MATERIAL",
                "fetch_status": "FULL_DOCUMENT_FETCHED",
            },
            {
                "candidate_id": "NAV-DESCENDANT-ARTICLE",
                "url": "https://issuer.example.com/news/result-one",
                "reference_discovery_only": True,
                "graph_expansion_parent_candidate_ids": ["DIRECT-NAV-PARENT"],
                "ranking_status": "MATERIAL",
                "fetch_status": "MATERIAL_PENDING_FETCH",
            },
            {
                "candidate_id": "NAV-GRANDCHILD",
                "url": "https://issuer.example.com/news/result-two",
                "reference_discovery_only": True,
                "graph_expansion_parent_candidate_ids": [
                    "NAV-DESCENDANT-ARTICLE"
                ],
                "ranking_status": "PENDING",
                "fetch_status": "NOT_STARTED",
            },
            {
                "candidate_id": "NONNAV-PARENT",
                "url": "https://issuer.example.com/news/current-results",
                "ranking_status": "MATERIAL",
                "fetch_status": "FULL_DOCUMENT_FETCHED",
            },
            {
                "candidate_id": "NAV-URL-CHILD",
                "url": "https://issuer.example.com/category/press",
                "reference_discovery_only": True,
                "graph_expansion_parent_candidate_ids": ["NONNAV-PARENT"],
                "ranking_status": "PENDING",
                "fetch_status": "NOT_STARTED",
            },
            {
                "candidate_id": "BODY-CITED-ARTICLE",
                "url": "https://issuer.example.com/news/cited-article",
                "graph_expansion_parent_document_ids": ["DOC-ARTICLE"],
                "ranking_status": "MATERIAL",
                "fetch_status": "MATERIAL_PENDING_FETCH",
            },
            {
                "candidate_id": "BODY-CITED-PDF",
                "url": "https://issuer.example.com/category/results/report.pdf",
                "graph_expansion_parent_document_ids": ["DOC-ARTICLE"],
                "ranking_status": "MATERIAL",
                "fetch_status": "MATERIAL_PENDING_FETCH",
            },
            {
                "candidate_id": "DIRECT-SEARCH-NAV",
                "url": "https://issuer.example.com/category/press",
                "direct_search_discovery": True,
                "ranking_status": "PENDING",
                "fetch_status": "NOT_STARTED",
            },
        ]
        closed = source_graph_module._close_navigation_only_reference_routes(candidates)

        self.assertEqual(closed, 2)
        closed_by_id = {
            row["candidate_id"]: row
            for row in candidates
            if row.get("reference_navigation_disposition")
            == "TERMINAL_DISCOVERY_ONLY"
        }
        self.assertEqual(
            set(closed_by_id),
            {
                "NAV-URL-CHILD",
                "DIRECT-SEARCH-NAV",
            },
        )
        self.assertTrue(
            all(
                row["fetch_status"]
                == "REFERENCE_DISCOVERY_REJECTED_NAVIGATION_ONLY"
                and row["ranking_status"] == "NOT_MATERIAL"
                and row["score_authority"] is False
                and row["reference_navigation_policy_version"]
                == source_graph_module.NAVIGATION_ONLY_REFERENCE_POLICY_VERSION
                for row in closed_by_id.values()
            )
        )
        retained_by_id = {
            row["candidate_id"]: row for row in candidates
        }
        self.assertEqual(
            retained_by_id["NAV-DESCENDANT-ARTICLE"]["fetch_status"],
            "MATERIAL_PENDING_FETCH",
        )
        self.assertEqual(
            retained_by_id["NAV-GRANDCHILD"]["fetch_status"],
            "NOT_STARTED",
        )
        self.assertEqual(
            retained_by_id["BODY-CITED-ARTICLE"]["fetch_status"],
            "MATERIAL_PENDING_FETCH",
        )
        self.assertEqual(
            retained_by_id["BODY-CITED-PDF"]["fetch_status"],
            "MATERIAL_PENDING_FETCH",
        )
        self.assertEqual(
            retained_by_id["DIRECT-SEARCH-NAV"]["ranking_status"],
            "NOT_MATERIAL",
        )
        self.assertEqual(
            retained_by_id["DIRECT-SEARCH-NAV"]["fetch_status"],
            "REFERENCE_DISCOVERY_REJECTED_NAVIGATION_ONLY",
        )

    def test_fetched_navigation_document_is_quarantined_and_facts_retire(
        self,
    ) -> None:
        navigation_url = "https://issuer.example.com/search?keyword=HBM4"
        article_url = "https://issuer.example.com/news/hbm4-allocation"
        pdf_url = "https://issuer.example.com/category/results/hbm4.pdf"
        candidates = [
            {
                "candidate_id": "FETCHED-NAVIGATION",
                "ranking_status": "MATERIAL",
                "fetch_status": "FULL_DOCUMENT_FETCHED",
                "document_id": "SGDOC-navigation",
                "url": navigation_url,
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
            },
            {
                "candidate_id": "ARTICLE-DESCENDANT",
                "ranking_status": "MATERIAL",
                "fetch_status": "FULL_DOCUMENT_FETCHED",
                "document_id": "SGDOC-article",
                "url": article_url,
                "graph_expansion_parent_candidate_ids": [
                    "FETCHED-NAVIGATION"
                ],
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
            },
            {
                "candidate_id": "DIRECT-PDF",
                "ranking_status": "MATERIAL",
                "fetch_status": "FULL_DOCUMENT_FETCHED",
                "document_id": "SGDOC-pdf",
                "url": pdf_url,
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
            },
        ]
        documents = [
            {
                "document_id": candidate["document_id"],
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "canonical_url": candidate["url"],
                "content_hash": hashlib.sha256(
                    candidate["url"].encode("utf-8")
                ).hexdigest(),
                "content_text": f"complete content for {candidate['candidate_id']}",
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
                "evidence_eligible": True,
            }
            for candidate in candidates
        ]
        state = {
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "evidence_documents": documents,
            "search_candidates": candidates,
            "quarantined_documents": [],
            "rejected_documents": [],
        }
        facts = (
            {"fact_id": "FACT-NAV", "source_ids": ["SGDOC-navigation"]},
            {"fact_id": "FACT-ARTICLE", "source_ids": ["SGDOC-article"]},
            {"fact_id": "FACT-PDF", "source_ids": ["SGDOC-pdf"]},
        )

        reasons = source_graph_module._quarantine_navigation_only_documents(
            state
        )
        active_facts, invalidated_count = (
            source_graph_module._filter_facts_to_active_source_documents(
                facts,
                state["evidence_documents"],
            )
        )

        self.assertEqual(
            reasons,
            ("NAVIGATION_ONLY_REFERENCE_URL:FULL_DOCUMENT_DEMOTED",),
        )
        self.assertEqual(
            {row["document_id"] for row in state["evidence_documents"]},
            {"SGDOC-article", "SGDOC-pdf"},
        )
        self.assertEqual(
            {row["fact_id"] for row in active_facts},
            {"FACT-ARTICLE", "FACT-PDF"},
        )
        self.assertEqual(invalidated_count, 1)
        self.assertEqual(
            source_graph_module.validated_quarantined_document_ids(state),
            frozenset({"SGDOC-navigation"}),
        )
        navigation = candidates[0]
        self.assertEqual(navigation["ranking_status"], "NOT_MATERIAL")
        self.assertEqual(
            navigation["fetch_status"],
            "REFERENCE_DISCOVERY_REJECTED_NAVIGATION_ONLY",
        )
        self.assertEqual(
            navigation["reference_navigation_disposition"],
            "TERMINAL_DISCOVERY_ONLY",
        )
        self.assertEqual(
            navigation["quarantined_document_id"],
            "SGDOC-navigation",
        )
        self.assertNotIn("document_id", navigation)
        self.assertEqual(
            candidates[1]["fetch_status"],
            "FULL_DOCUMENT_FETCHED",
        )
        self.assertEqual(candidates[2]["fetch_status"], "FULL_DOCUMENT_FETCHED")

    def test_ready_readonly_checkpoint_advances_navigation_migration(
        self,
    ) -> None:
        ready = {
            "status": "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
            "generated_queries": [
                {"execution_status": "SEARCH_EXECUTED"}
            ],
            "search_candidates": [
                {
                    "ranking_status": "MATERIAL",
                    "fetch_status": "FULL_DOCUMENT_FETCHED",
                    "document_id": "SGDOC-navigation",
                    "url": "https://issuer.example.com/search?keyword=HBM4",
                },
                {
                    "ranking_status": "MATERIAL",
                    "fetch_status": "FULL_DOCUMENT_FETCHED",
                    "document_id": "SGDOC-article",
                    "url": "https://issuer.example.com/news/hbm4-allocation",
                },
            ],
            "evidence_documents": [
                {
                    "document_id": "SGDOC-navigation",
                    "canonical_url": (
                        "https://issuer.example.com/search?keyword=HBM4"
                    ),
                },
                {
                    "document_id": "SGDOC-article",
                    "canonical_url": (
                        "https://issuer.example.com/news/hbm4-allocation"
                    ),
                },
            ],
        }

        self.assertFalse(
            _source_checkpoint_is_ready_for_readonly_replay(ready)
        )
        ready["evidence_documents"] = ready["evidence_documents"][1:]
        self.assertTrue(
            _source_checkpoint_is_ready_for_readonly_replay(ready)
        )

    def test_navigation_checkpoint_migration_adds_no_query_fetch_or_document(
        self,
    ) -> None:
        navigation_url = "https://issuer.example.com/search?keyword=HBM4"
        article_url = "https://issuer.example.com/news/hbm4-allocation"
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state["status"] = "EPOCH_COMPLETE_REQUIRES_SUPERVISOR"
        state["generated_queries"] = [
            {
                "query_id": "QUERY-1",
                "objective_id": "OBJECTIVE-1",
                "literal_query": QUERY,
                "generator_kind": "TEST_FIXTURE_LLM",
                "execution_status": "SEARCH_EXECUTED",
            }
        ]
        state["executed_queries"] = [QUERY]
        state["search_candidates"] = [
            {
                "candidate_id": "FETCHED-NAVIGATION",
                "ranking_status": "MATERIAL",
                "fetch_status": "FULL_DOCUMENT_FETCHED",
                "document_id": "SGDOC-navigation",
                "url": navigation_url,
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
            },
            {
                "candidate_id": "ARTICLE-DESCENDANT",
                "ranking_status": "MATERIAL",
                "fetch_status": "FULL_DOCUMENT_FETCHED",
                "document_id": "SGDOC-article",
                "url": article_url,
                "graph_expansion_parent_candidate_ids": [
                    "FETCHED-NAVIGATION"
                ],
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
            },
        ]
        state["evidence_documents"] = [
            {
                "document_id": document_id,
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "canonical_url": url,
                "content_hash": hashlib.sha256(
                    url.encode("utf-8")
                ).hexdigest(),
                "content_text": f"complete source text for {document_id}",
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
                "source_family": "ISSUER_NEWSROOM",
                "evidence_eligible": True,
            }
            for document_id, url in (
                ("SGDOC-navigation", navigation_url),
                ("SGDOC-article", article_url),
            )
        ]
        checkpoint = source_graph_module._finalize_checkpoint(state)
        provider = SourceBrainProvider()
        search = RecordingSearchProvider({})
        facts = (
            {
                "fact_id": "FACT-NAV",
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "source_ids": ["SGDOC-navigation"],
                "direction": "POSITIVE",
            },
            {
                "fact_id": "FACT-ARTICLE",
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "source_ids": ["SGDOC-article"],
                "direction": "POSITIVE",
            },
        )

        migrated = self._run(
            provider=provider,
            search=search,
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=checkpoint,
            current_evidence_facts=facts,
            checkpoint_migration_only=True,
        )

        self.assertEqual(provider.calls, [])
        self.assertEqual(search.calls, [])
        self.assertEqual(len(migrated.checkpoint["generated_queries"]), 1)
        self.assertEqual(len(migrated.checkpoint["search_candidates"]), 2)
        self.assertEqual(
            {
                row["document_id"]
                for row in migrated.evidence_documents
            },
            {"SGDOC-article"},
        )
        self.assertIn(
            "STALE_PRIOR_FACT_SOURCE_INVALIDATED:1",
            migrated.checkpoint["pending_reasons"],
        )
        self.assertTrue(migrated.audit["checkpoint_migration_only"])

    def test_stale_unverified_reference_route_closes_without_llm_ranking(self) -> None:
        candidates = [
            {
                "candidate_id": "PARENT",
                "candidate_source_family_hint": "GENERAL_WEB_DISCOVERY",
                "verified_official_domain_candidate": False,
            },
            {
                "candidate_id": "STALE-NAVIGATION",
                "reference_discovery_only": True,
                "graph_expansion_parent_candidate_ids": ["PARENT"],
                "ranking_status": "PENDING",
                "fetch_status": "NOT_STARTED",
            },
            {
                "candidate_id": "DIRECT-SEARCH",
                "reference_discovery_only": True,
                "direct_search_discovery": True,
                "graph_expansion_parent_candidate_ids": ["PARENT"],
                "ranking_status": "PENDING",
                "fetch_status": "NOT_STARTED",
            },
        ]
        closed = source_graph_module._close_non_authority_candidate_reference_routes(
            candidates
        )
        self.assertEqual(closed, 1)
        self.assertEqual(candidates[1]["ranking_status"], "NOT_MATERIAL")
        self.assertEqual(
            candidates[1]["fetch_status"],
            "REFERENCE_DISCOVERY_REJECTED_UNVERIFIED_PARENT",
        )
        self.assertEqual(candidates[2]["ranking_status"], "PENDING")

    def test_official_link_budget_prioritizes_pdf_and_delegated_host(self) -> None:
        parent = {
            "candidate_id": "OFFICIAL-PARENT",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "url": "https://www.example.com/ir/events",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "objective_ids": ["OBJECTIVE-1"],
            "query_ids": ["QUERY-1"],
            "requested_source_families": ["ISSUER_PRESENTATION"],
            "discovered_referenced_urls": [
                "https://www.example.com/menu",
                "https://delegated.example.net/webcast",
                "https://www.example.com/files/earnings.pdf?download=1",
            ],
        }
        _bind_candidate_reference_scope(
            parent,
            decision_id="DECISION-OFFICIAL-BUDGET",
        )
        candidates = [parent]
        deferred = source_graph_module._enqueue_candidate_discovery_references(
            candidates,
            parent_candidate=parent,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            max_total_candidates=3,
        )
        self.assertEqual(deferred, 1)
        self.assertEqual(
            [row["url"] for row in candidates[1:]],
            [
                "https://www.example.com/files/earnings.pdf?download=1",
                "https://delegated.example.net/webcast",
            ],
        )

    def test_reference_parent_budget_prioritizes_current_period_over_append_order(
        self,
    ) -> None:
        old_parent = {
            "candidate_id": "OLD-OFFICIAL-PARENT",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "url": "https://ir.example.com/2023Q1/entry",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_PRESENTATION",
            "material_priority": 1.0,
            "objective_ids": ["OBJECTIVE-1"],
            "query_ids": ["QUERY-OLD"],
            "requested_source_families": ["ISSUER_PRESENTATION"],
            "discovered_referenced_urls": [
                "https://ir.example.com/archive/2023Q1/transcript"
            ],
        }
        _bind_candidate_reference_scope(
            old_parent,
            decision_id="DECISION-OLD-PARENT",
        )
        current_parent = {
            **old_parent,
            "candidate_id": "CURRENT-OFFICIAL-PARENT",
            "url": "https://ir.example.com/event?id=current",
            "query_ids": ["QUERY-CURRENT"],
            "discovered_referenced_urls": [
                "https://ir.example.com/current/2026Q1/transcript"
            ],
        }
        _bind_candidate_reference_scope(
            current_parent,
            decision_id="DECISION-CURRENT-PARENT",
        )
        candidates = [old_parent, current_parent]
        for parent in source_graph_module._ordered_candidate_reference_parents(
            candidates,
            as_of_date=date(2026, 7, 12),
        ):
            source_graph_module._enqueue_candidate_discovery_references(
                candidates,
                parent_candidate=parent,
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                max_total_candidates=3,
            )
        self.assertEqual(len(candidates), 3)
        self.assertEqual(
            candidates[-1]["url"],
            "https://ir.example.com/current/2026Q1/transcript",
        )

    def test_old_official_empty_html_failure_reopens_exactly_once(self) -> None:
        candidate = {
            "candidate_id": "OFFICIAL-EMPTY-HTML",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "ranking_status": "MATERIAL",
            "fetch_status": "FETCH_REJECTED",
        }
        rejected = (
            {
                "candidate_id": "OFFICIAL-EMPTY-HTML",
                "rejection_reason": (
                    "SNIPPET_ONLY_FULL_FETCH_REQUIRED:"
                    "live_fetch_unreadable_text:empty_extracted_text"
                ),
            },
        )
        first = source_graph_module._reopen_authority_link_extraction_candidates(
            [candidate],
            rejected_documents=rejected,
        )
        second = source_graph_module._reopen_authority_link_extraction_candidates(
            [candidate],
            rejected_documents=rejected,
        )
        self.assertEqual(first, 1)
        self.assertEqual(second, 0)
        self.assertEqual(candidate["fetch_status"], "MATERIAL_PENDING_FETCH")
        self.assertTrue(candidate["link_preserving_fetch_retry_attempted"])

    def test_old_date_and_pdf_semantics_failures_reopen_exactly_once(self) -> None:
        date_candidate = {
            "candidate_id": "UNKNOWN-DATE",
            "ranking_status": "MATERIAL",
            "fetch_status": "FETCH_REJECTED",
        }
        pdf_candidate = {
            "candidate_id": "UNREADABLE-PDF",
            "ranking_status": "MATERIAL",
            "fetch_status": "FETCH_REJECTED",
        }
        rejected = (
            {
                "candidate_id": "UNKNOWN-DATE",
                "rejection_reason": "UNKNOWN_PUBLISHED_DATE_AFTER_FULL_FETCH",
            },
            {
                "candidate_id": "UNREADABLE-PDF",
                "rejection_reason": (
                    "SNIPPET_ONLY_FULL_FETCH_REQUIRED:"
                    "live_pdf_text_extraction_failed:pypdf_unreadable"
                ),
            },
        )

        first = source_graph_module._reopen_fetch_semantics_candidates(
            [date_candidate, pdf_candidate],
            rejected_documents=rejected,
        )
        date_candidate["fetch_status"] = "FETCH_REJECTED"
        pdf_candidate["fetch_status"] = "FETCH_REJECTED"
        second = source_graph_module._reopen_fetch_semantics_candidates(
            [date_candidate, pdf_candidate],
            rejected_documents=rejected,
        )

        self.assertEqual(first, 2)
        self.assertEqual(second, 0)
        self.assertTrue(
            date_candidate["publication_metadata_fetch_retry_attempted"]
        )
        self.assertEqual(
            date_candidate["fetch_semantics_policy_version"],
            PUBLICATION_DATE_INFERENCE_SEMANTICS_VERSION,
        )
        self.assertTrue(pdf_candidate["pdf_fallback_fetch_retry_attempted"])

    def test_old_date_inference_retry_reopens_for_new_policy_once(self) -> None:
        candidate = {
            "candidate_id": "UNKNOWN-DATE",
            "ranking_status": "MATERIAL",
            "fetch_status": "FETCH_REJECTED",
            "publication_metadata_fetch_retry_attempted": True,
            "fetch_semantics_policy_version": (
                "e2r_publication_date_inference_v3"
            ),
        }
        rejected = (
            {
                "candidate_id": "UNKNOWN-DATE",
                "rejection_reason": (
                    "UNKNOWN_PUBLISHED_DATE_AFTER_FULL_FETCH"
                ),
            },
        )

        first = source_graph_module._reopen_fetch_semantics_candidates(
            [candidate],
            rejected_documents=rejected,
        )
        candidate["fetch_status"] = "FETCH_REJECTED"
        second = source_graph_module._reopen_fetch_semantics_candidates(
            [candidate],
            rejected_documents=rejected,
        )

        self.assertEqual(first, 1)
        self.assertEqual(second, 0)
        self.assertEqual(
            candidate["fetch_semantics_policy_version"],
            PUBLICATION_DATE_INFERENCE_SEMANTICS_VERSION,
        )

    def test_fetch_semantics_retry_closes_before_unrelated_official_backlog(
        self,
    ) -> None:
        retry = {
            "candidate_id": "CURRENT-SEMANTICS-RETRY",
            "url": "https://issuer.example.com/q1-2026-results",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "material_priority": 1.0,
            "fetch_semantics_retry_reason": (
                "PRIOR_UNKNOWN_DATE_PRECEDED_HTML_PUBLICATION_METADATA"
            ),
        }
        unrelated = {
            "candidate_id": "OLDER-OFFICIAL-BACKLOG",
            "url": "https://issuer.example.com/2019/06/30/archive-results",
            "verified_official_domain_candidate": True,
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "material_priority": 1.0,
        }

        ordered = sorted(
            (unrelated, retry),
            key=lambda row: source_graph_module._pending_material_fetch_priority(
                row,
                as_of_date=date(2026, 7, 12),
                official_first_required=True,
            ),
        )

        self.assertEqual(ordered[0]["candidate_id"], "CURRENT-SEMANTICS-RETRY")

    def test_fetch_semantics_retry_survives_prior_objective_resolution(
        self,
    ) -> None:
        candidate = {
            "candidate_id": "CURRENT-SEMANTICS-RETRY",
            "objective_ids": ["OBJECTIVE-1"],
            "ranking_status": "MATERIAL",
            "fetch_status": "MATERIAL_PENDING_FETCH",
            "fetch_semantics_retry_reason": (
                "PRIOR_UNKNOWN_DATE_PRECEDED_PUBLICATION_DATE_INFERENCE"
            ),
            "fetch_semantics_policy_version": (
                PUBLICATION_DATE_INFERENCE_SEMANTICS_VERSION
            ),
        }

        self.assertFalse(
            source_graph_module._candidate_scope_is_fully_resolved(
                candidate,
                {"OBJECTIVE-1"},
            )
        )

    def test_current_provenance_revalidation_survives_objective_resolution(
        self,
    ) -> None:
        candidate = {
            "candidate_id": "CURRENT-PROVENANCE-REVALIDATION",
            "objective_ids": ["OBJECTIVE-1"],
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
            "materiality_revalidation_reason": (
                "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
            ),
            "alternate_route_required": True,
        }

        self.assertFalse(
            source_graph_module._candidate_scope_is_fully_resolved(
                candidate,
                {"OBJECTIVE-1"},
            )
        )

    def test_resolved_scope_pending_candidate_is_explicit_and_reversible(
        self,
    ) -> None:
        candidate = {
            "candidate_id": "RESOLVED-RANKING-TAIL",
            "objective_ids": ["OBJECTIVE-1"],
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
            "materiality_decision_id": None,
            "snippet_discovery_only": True,
            "snippet_evidence_eligible": False,
        }

        source_graph_module._reconcile_resolved_scope_candidate_ranking_statuses(
            [candidate],
            resolved_objective_ids={"OBJECTIVE-1"},
            ranking_transport_candidate_ids=set(),
        )

        self.assertEqual(
            candidate["ranking_status"],
            "RESOLVED_SCOPE_NOT_RANKED",
        )
        self.assertEqual(candidate["fetch_status"], "NOT_STARTED")
        self.assertIsNone(candidate["materiality_decision_id"])
        self.assertEqual(
            candidate["objective_resolution_transport_disposition"],
            "RANKING_NOT_REQUIRED_SCOPE_RESOLVED",
        )

        source_graph_module._reconcile_resolved_scope_candidate_ranking_statuses(
            [candidate],
            resolved_objective_ids=set(),
            ranking_transport_candidate_ids=set(),
        )

        self.assertEqual(candidate["ranking_status"], "PENDING")
        self.assertNotIn(
            "objective_resolution_transport_disposition",
            candidate,
        )

    def test_resolved_scope_status_does_not_hide_current_provenance_work(
        self,
    ) -> None:
        candidate = {
            "candidate_id": "CURRENT-PROVENANCE-ROUTE",
            "objective_ids": ["OBJECTIVE-1"],
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
            "materiality_revalidation_reason": (
                "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
            ),
            "alternate_route_required": True,
        }

        source_graph_module._reconcile_resolved_scope_candidate_ranking_statuses(
            [candidate],
            resolved_objective_ids={"OBJECTIVE-1"},
            ranking_transport_candidate_ids=set(),
        )

        self.assertEqual(candidate["ranking_status"], "PENDING")

        replay_candidate = {
            "candidate_id": "PENDING-RANKING-REPLAY",
            "objective_ids": ["OBJECTIVE-1"],
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
        }
        source_graph_module._reconcile_resolved_scope_candidate_ranking_statuses(
            [replay_candidate],
            resolved_objective_ids={"OBJECTIVE-1"},
            ranking_transport_candidate_ids={"PENDING-RANKING-REPLAY"},
        )
        self.assertEqual(replay_candidate["ranking_status"], "PENDING")

        decided_candidates = [
            {
                "candidate_id": "MATERIAL-CANDIDATE",
                "objective_ids": ["OBJECTIVE-1"],
                "ranking_status": "MATERIAL",
                "fetch_status": "FULL_DOCUMENT_FETCHED",
            },
            {
                "candidate_id": "NONMATERIAL-CANDIDATE",
                "objective_ids": ["OBJECTIVE-1"],
                "ranking_status": "NOT_MATERIAL",
                "fetch_status": "DISCOVERY_ONLY_NOT_FETCHED",
            },
        ]
        source_graph_module._reconcile_resolved_scope_candidate_ranking_statuses(
            decided_candidates,
            resolved_objective_ids={"OBJECTIVE-1"},
            ranking_transport_candidate_ids=set(),
        )
        self.assertEqual(
            [row["ranking_status"] for row in decided_candidates],
            ["MATERIAL", "NOT_MATERIAL"],
        )

    def test_acquirer_persists_resolved_ranking_tail_and_reopens_it(
        self,
    ) -> None:
        url = "https://issuer.example.com/resolved-ranking-tail"
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state.update(
            status="STOPPED_ON_RESOLUTION",
            generated_queries=[
                {
                    "query_id": "QUERY-1",
                    "objective_id": "OBJECTIVE-1",
                    "literal_query": QUERY,
                    "source_families": ["ISSUER_NEWSROOM"],
                    "execution_status": "SEARCH_EXECUTED",
                }
            ],
            executed_queries=[QUERY],
            resolved_objective_ids=["OBJECTIVE-1"],
            search_candidates=[
                {
                    "candidate_id": "RESOLVED-RANKING-TAIL",
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "title": "Current Corp unresolved ranking tail",
                    "url": url,
                    "normalized_url": url,
                    "published_at": "2026-06-20",
                    "query_ids": ["QUERY-1"],
                    "materiality_query_ids": ["QUERY-1"],
                    "objective_ids": ["OBJECTIVE-1"],
                    "requested_source_families": ["ISSUER_NEWSROOM"],
                    "ranking_status": "PENDING",
                    "fetch_status": "NOT_STARTED",
                    "snippet_discovery_only": True,
                    "snippet_evidence_eligible": False,
                    "score_authority": False,
                }
            ],
        )
        checkpoint = source_graph_module._finalize_checkpoint(state)
        first_provider = SourceBrainProvider()
        expected_lineage = {
            key: list(state["search_candidates"][0][key])
            for key in (
                "query_ids",
                "materiality_query_ids",
                "objective_ids",
                "requested_source_families",
            )
        }

        closed = self._run(
            provider=first_provider,
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        closed_candidate = next(
            row
            for row in closed.checkpoint["search_candidates"]
            if row["candidate_id"] == "RESOLVED-RANKING-TAIL"
        )
        self.assertEqual(closed.status, "STOPPED_ON_RESOLUTION")
        self.assertEqual(
            closed_candidate["ranking_status"],
            "RESOLVED_SCOPE_NOT_RANKED",
        )
        self.assertEqual(closed.audit["pending_candidate_count"], 0)
        self.assertEqual(
            closed.checkpoint["candidate_materiality_decisions"],
            [],
        )
        self.assertIsNone(closed_candidate.get("materiality_decision_id"))
        self.assertEqual(
            {
                key: list(closed_candidate[key])
                for key in expected_lineage
            },
            expected_lineage,
        )
        source_graph_module.validate_source_graph_checkpoint(
            closed.checkpoint
        )
        self.assertTrue(
            _source_checkpoint_is_ready_for_readonly_replay(
                closed.checkpoint
            )
        )
        self.assertEqual(
            _source_transport_work_state(closed.checkpoint)["candidates"][
                "RESOLVED-RANKING-TAIL"
            ],
            "TERMINAL",
        )
        supervisor_projection = project_source_graph_checkpoint(
            closed.checkpoint,
            keys=("search_candidates",),
        )
        self.assertEqual(
            supervisor_projection["search_candidates"][
                "semantic_groups"
            ][0]["state"]["ranking_status"],
            "RESOLVED_SCOPE_NOT_RANKED",
        )
        self.assertFalse(
            any(
                row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
                for row in first_provider.calls
            )
        )

        reopened_provider = SourceBrainProvider(
            source_families=("ISSUER_NEWSROOM",),
        )
        reopened = self._run(
            provider=reopened_provider,
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(
                fixture_text_by_url={url: _document_text("reopened-tail")}
            ),
            checkpoint=closed.checkpoint,
            resolved_objective_ids=(),
        )

        reopened_candidate = next(
            row
            for row in reopened.checkpoint["search_candidates"]
            if row["candidate_id"] == "RESOLVED-RANKING-TAIL"
        )
        self.assertNotEqual(
            reopened_candidate["ranking_status"],
            "RESOLVED_SCOPE_NOT_RANKED",
        )
        self.assertTrue(
            any(
                row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
                for row in reopened_provider.calls
            )
        )
        ranking_call = next(
            row
            for row in reopened_provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )
        ranking_candidate = next(
            row
            for row in ranking_call["payload"]["discovery_candidates"]
            if row["candidate_id"] == "RESOLVED-RANKING-TAIL"
        )
        self.assertEqual(
            ranking_candidate["query_ids"],
            expected_lineage["materiality_query_ids"],
        )
        self.assertEqual(
            ranking_candidate["objective_ids"],
            expected_lineage["objective_ids"],
        )
        self.assertEqual(
            ranking_candidate["requested_source_families"],
            expected_lineage["requested_source_families"],
        )

    def test_alternate_route_revalidation_ranks_before_legacy_backlog(
        self,
    ) -> None:
        alternate_route = {
            "candidate_id": "CURRENT-ALTERNATE-ROUTE",
            "rank": 2,
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
            "materiality_revalidation_reason": (
                "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
            ),
            "alternate_route_required": True,
        }
        legacy_backlog = {
            "candidate_id": "LEGACY-REVALIDATION",
            "rank": 0,
            "ranking_status": "PENDING",
            "fetch_status": "NOT_STARTED",
            "materiality_revalidation_reason": (
                "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
            ),
        }

        ordered = sorted(
            (legacy_backlog, alternate_route),
            key=lambda row: (
                source_graph_module._pending_candidate_ranking_priority(
                    row,
                    supervisor_query_direction_priority=False,
                )
            ),
        )

        self.assertEqual(
            ordered[0]["candidate_id"],
            "CURRENT-ALTERNATE-ROUTE",
        )

    def test_llm_candidate_family_gap_reopens_query_edge_not_materiality(
        self,
    ) -> None:
        candidate_id = "SGCAND-0123456789abcdef01234567"
        candidate = {
            "candidate_id": candidate_id,
            "title": "Current Corp official preliminary results",
            "url": "https://issuer.example.com/current-results",
            "query_ids": ["QUERY-VALUATION"],
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["VALUATION_MULTIPLES"],
            "candidate_source_family_hint": "ISSUER_NEWSROOM",
            "verified_official_domain_candidate": True,
            "alternate_route_required": True,
            "materiality_revalidation_reason": (
                "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
            ),
        }

        class FamilyGapProvider:
            provider_name = "TEST_FAMILY_GAP_PROVIDER"

            def complete(self, *, pass_name, payload):
                self.assertEqual(pass_name, "SOURCE_CANDIDATE_RANKING")
                return {
                    "decisions": [
                        {
                            "candidate_id": candidate_id,
                            "material_relevance": False,
                            "priority": 1.0,
                            "objective_ids": ["OBJECTIVE-1"],
                            "matched_requested_source_family": "NONE",
                            "rationale": (
                                "공식 실적 경로지만 현재 query edge의 family가 다르다."
                            ),
                        }
                    ],
                    "ranking_complete": True,
                    "unresolved_notes": [
                        candidate_id
                        + "는 ISSUER_NEWSROOM query edge가 필요하다."
                    ],
                }

            def assertEqual(self, first, second):
                if first != second:
                    raise AssertionError((first, second))

        ranking = ResearcherDocumentRanker(
            provider=FamilyGapProvider()
        ).rank_candidates(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            open_objectives=({"objective_id": "OBJECTIVE-1"},),
            candidates=(candidate,),
            current_evidence_facts=(),
            target_business_model=None,
            source_coverage=(),
        )

        self.assertEqual(ranking.status, "COMPLETE")
        self.assertEqual(len(ranking.unresolved_notes), 1)
        failures = (
            source_graph_module._candidate_source_family_query_edge_failures(
                ranking=ranking,
                candidates=(candidate,),
            )
        )
        self.assertEqual(len(failures), 1)
        self.assertEqual(
            failures[0]["source_family"],
            "ISSUER_NEWSROOM",
        )
        self.assertFalse(ranking.decisions[0].material_relevance)
        self.assertEqual(
            len(
                source_graph_module._unresolved_candidate_source_family_query_edge_failures(
                    failures,
                    candidates=(candidate,),
                )
            ),
            1,
        )

        rebound = dict(candidate)
        rebound["requested_source_families"] = [
            "VALUATION_MULTIPLES",
            "ISSUER_NEWSROOM",
        ]
        self.assertEqual(
            source_graph_module._unresolved_candidate_source_family_query_edge_failures(
                failures,
                candidates=(rebound,),
            ),
            (),
        )

        current_transport_repair = dict(candidate)
        generic_note_ranking = replace(
            ranking,
            unresolved_notes=(
                "모든 후보를 검토했으며 원문 fetch와 검증이 남아 있다.",
            ),
        )
        structural_failures = (
            source_graph_module._candidate_source_family_query_edge_failures(
                ranking=generic_note_ranking,
                candidates=(current_transport_repair,),
            )
        )
        self.assertEqual(len(structural_failures), 1)
        self.assertEqual(
            structural_failures[0]["detection_basis"],
            "LLM_NONMATERIAL_DECISION_ON_CURRENT_OFFICIAL_TRANSPORT_REPAIR_FAMILY_MISMATCH",
        )

        multi_objective_candidate = {
            **candidate,
            "objective_ids": ["OBJECTIVE-1", "OBJECTIVE-2"],
        }
        live_subset_failures = (
            source_graph_module._candidate_source_family_query_edge_failures(
                ranking=ranking,
                candidates=(multi_objective_candidate,),
            )
        )
        self.assertEqual(
            [row["objective_id"] for row in live_subset_failures],
            ["OBJECTIVE-1"],
        )
        persisted_multi = {
            **multi_objective_candidate,
            "normalized_url": multi_objective_candidate["url"],
            "ranking_status": "NOT_MATERIAL",
            "matched_requested_source_family": "NONE",
            "materiality_decision_id": ranking.decisions[0].decision_id,
        }
        persisted_multi["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(
                persisted_multi
            )
        )
        resumed_subset_failures = source_graph_module._persisted_candidate_source_family_query_edge_failures(
            candidates=(persisted_multi,),
            materiality_decisions=(ranking.decisions[0].to_dict(),),
        )
        self.assertEqual(
            [row["objective_id"] for row in resumed_subset_failures],
            ["OBJECTIVE-1"],
        )

        generic_candidate_mention = replace(
            ranking,
            unresolved_notes=(
                candidate_id + "는 현재 목적과 직접 관련되지 않는다.",
            ),
        )
        non_transport_candidate = dict(candidate)
        non_transport_candidate.pop("alternate_route_required")
        non_transport_candidate.pop("materiality_revalidation_reason")
        self.assertEqual(
            source_graph_module._candidate_source_family_query_edge_failures(
                ranking=generic_candidate_mention,
                candidates=(non_transport_candidate,),
            ),
            (),
        )
        negative_family_note = replace(
            ranking,
            unresolved_notes=(
                candidate_id
                + "에는 ISSUER_NEWSROOM query edge가 필요하지 않다.",
            ),
        )
        self.assertEqual(
            source_graph_module._candidate_source_family_query_edge_failures(
                ranking=negative_family_note,
                candidates=(non_transport_candidate,),
            ),
            (),
        )

    def test_resolved_objective_processes_current_provenance_revalidation(
        self,
    ) -> None:
        url = "https://issuer.example.com/current-provenance-release"
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state.update(
            status="STOPPED_ON_RESOLUTION",
            generated_queries=[
                {
                    "query_id": "QUERY-1",
                    "objective_id": "OBJECTIVE-1",
                    "literal_query": QUERY,
                    "source_families": ["ISSUER_NEWSROOM"],
                    "execution_status": "SEARCH_EXECUTED",
                }
            ],
            executed_queries=[QUERY],
            resolved_objective_ids=["OBJECTIVE-1"],
            search_candidates=[
                {
                    "candidate_id": "CURRENT-PROVENANCE-REVALIDATION",
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "title": "Current Corp official current release",
                    "url": url,
                    "normalized_url": url,
                    "published_at": "2026-06-20",
                    "query_ids": ["QUERY-1"],
                    "objective_ids": ["OBJECTIVE-1"],
                    "requested_source_families": ["ISSUER_NEWSROOM"],
                    "ranking_status": "PENDING",
                    "fetch_status": "NOT_STARTED",
                    "materiality_revalidation_reason": (
                        "PRODUCTION_FETCH_REQUIRES_CURRENT_SOURCE_FAMILY_MATCH"
                    ),
                    "alternate_route_required": True,
                }
            ],
        )
        checkpoint = source_graph_module._finalize_checkpoint(state)
        provider = SourceBrainProvider(
            source_families=("ISSUER_NEWSROOM",),
        )

        run = self._run(
            provider=provider,
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(
                fixture_text_by_url={url: _document_text("current-provenance")}
            ),
            checkpoint=checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        candidate = next(
            row
            for row in run.checkpoint["search_candidates"]
            if row["candidate_id"] == "CURRENT-PROVENANCE-REVALIDATION"
        )
        self.assertEqual(candidate["ranking_status"], "MATERIAL")
        self.assertEqual(candidate["fetch_status"], "FULL_DOCUMENT_FETCHED")
        self.assertEqual(run.status, "STOPPED_ON_RESOLUTION")
        ranking_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )
        self.assertEqual(
            ranking_payload["open_research_objectives"][0]["objective_id"],
            "OBJECTIVE-1",
        )

    def test_resolved_objective_still_fetches_current_semantics_retry(
        self,
    ) -> None:
        url = "https://issuer.example.com/current-semantics-retry"
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state.update(
            status="STOPPED_ON_RESOLUTION",
            generated_queries=[
                {
                    "query_id": "QUERY-1",
                    "objective_id": "OBJECTIVE-1",
                    "literal_query": QUERY,
                    "execution_status": "SEARCH_EXECUTED",
                }
            ],
            executed_queries=[QUERY],
            resolved_objective_ids=["OBJECTIVE-1"],
            search_candidates=[
                {
                    "candidate_id": "CURRENT-SEMANTICS-RETRY",
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "title": "Current Corp official current release",
                    "url": url,
                    "normalized_url": url,
                    "published_at": "2026-06-20",
                    "query_ids": ["QUERY-1"],
                    "objective_ids": ["OBJECTIVE-1"],
                    "ranking_status": "MATERIAL",
                    "fetch_status": "MATERIAL_PENDING_FETCH",
                    "material_priority": 1.0,
                    "fetch_semantics_retry_reason": (
                        "PRIOR_UNKNOWN_DATE_PRECEDED_PUBLICATION_DATE_INFERENCE"
                    ),
                    "fetch_semantics_policy_version": (
                        PUBLICATION_DATE_INFERENCE_SEMANTICS_VERSION
                    ),
                }
            ],
        )
        checkpoint = source_graph_module._finalize_checkpoint(state)

        run = self._run(
            provider=SourceBrainProvider(),
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(
                fixture_text_by_url={url: _document_text("semantics-retry")}
            ),
            checkpoint=checkpoint,
            resolved_objective_ids=("OBJECTIVE-1",),
        )

        candidate = next(
            row
            for row in run.checkpoint["search_candidates"]
            if row["candidate_id"] == "CURRENT-SEMANTICS-RETRY"
        )
        self.assertEqual(candidate["fetch_status"], "FULL_DOCUMENT_FETCHED")
        self.assertEqual(candidate["full_fetch_attempt_count"], 1)
        self.assertTrue(
            any(row.get("canonical_url") == url for row in run.evidence_documents)
        )
        ordinary_pending = {
            **candidate,
            "candidate_id": "ORDINARY-RESOLVED-PENDING",
            "fetch_status": "MATERIAL_PENDING_FETCH",
            "fetch_semantics_retry_reason": None,
            "fetch_semantics_policy_version": None,
        }
        self.assertTrue(
            source_graph_module._candidate_scope_is_fully_resolved(
                ordinary_pending,
                {"OBJECTIVE-1"},
            )
        )
        stale_policy_pending = {
            **candidate,
            "fetch_status": "MATERIAL_PENDING_FETCH",
            "fetch_semantics_policy_version": (
                "e2r_publication_date_inference_v2"
            ),
        }
        self.assertTrue(
            source_graph_module._candidate_scope_is_fully_resolved(
                stale_policy_pending,
                {"OBJECTIVE-1"},
            )
        )
        candidate["fetch_status"] = "FULL_DOCUMENT_FETCHED"
        self.assertTrue(
            source_graph_module._candidate_scope_is_fully_resolved(
                candidate,
                {"OBJECTIVE-1"},
            )
        )

    def test_legacy_text_cap_document_is_quarantined_and_refetched_once(self) -> None:
        for content_length in (199_999, 200_000):
            with self.subTest(content_length=content_length):
                content = "x" * content_length
                content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
                candidate = {
                    "candidate_id": "CAPPED-CANDIDATE",
                    "ranking_status": "MATERIAL",
                    "fetch_status": "FULL_DOCUMENT_FETCHED",
                    "document_id": "SGDOC-capped",
                    "url": "https://issuer.example.com/capped.pdf",
                    "query_ids": ["QUERY-1"],
                    "objective_ids": ["OBJECTIVE-1"],
                }
                state = {
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "evidence_documents": [
                        {
                            "document_id": "SGDOC-capped",
                            "target_id": TARGET,
                            "as_of_date": AS_OF_DATE,
                            "canonical_url": candidate["url"],
                            "content_hash": content_hash,
                            "content_text": content,
                            "source_provider": "PageFetcher",
                            "query_ids": ["QUERY-1"],
                            "objective_ids": ["OBJECTIVE-1"],
                        }
                    ],
                    "search_candidates": [candidate],
                    "quarantined_documents": [],
                    "rejected_documents": [],
                    "query_failures": [],
                }

                first = source_graph_module._quarantine_unreadable_documents(state)
                second = source_graph_module._quarantine_unreadable_documents(state)

                self.assertEqual(
                    first,
                    (
                        "INCOMPLETE_FULL_DOCUMENT_TEXT:"
                        "LEGACY_PAGE_FETCH_200000_CHAR_CAP",
                    ),
                )
                self.assertEqual(second, ())
                self.assertEqual(state["evidence_documents"], [])
                self.assertEqual(
                    candidate["fetch_status"],
                    "MATERIAL_PENDING_FETCH",
                )
                self.assertTrue(candidate["parser_semantics_refetch_required"])
                self.assertEqual(
                    source_graph_module.validated_quarantined_document_ids(state),
                    frozenset({"SGDOC-capped"}),
                )

    def test_source_repair_only_refetches_capped_document_without_new_research(self) -> None:
        url = "https://issuer.example.com/capped.pdf"
        capped = ("Current Corp legacy capped evidence " * 8_000)[:199_999]
        repaired_text = (
            "Published 2026-06-20\nCurrent Corp complete filing Page 299\n"
            + "source-backed complete filing detail " * 15_000
        )
        candidate = {
            "candidate_id": "CAPPED-CANDIDATE",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "ranking_status": "MATERIAL",
            "fetch_status": "FULL_DOCUMENT_FETCHED",
            "document_id": "SGDOC-capped",
            "url": url,
            "normalized_url": url,
            "title": "Current Corp capped filing",
            "snippet": "Current Corp complete filing",
            "source_family": "NAVER_DISCOVERY",
            "query_ids": ["QUERY-1"],
            "objective_ids": ["OBJECTIVE-1"],
            "published_at": "2026-06-20",
        }
        unrelated_terminal_candidate = {
            "candidate_id": "UNRELATED-TERMINAL-CANDIDATE",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "ranking_status": "MATERIAL",
            "fetch_status": "FETCH_REJECTED",
            "url": "https://issuer.example.com/unrelated-terminal.pdf",
            "normalized_url": (
                "https://issuer.example.com/unrelated-terminal.pdf"
            ),
            "query_ids": ["QUERY-OLD"],
            "objective_ids": ["OBJECTIVE-1"],
        }
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="PRODUCTION_DAILY",
        )
        state["status"] = "EPOCH_COMPLETE_REQUIRES_SUPERVISOR"
        state["evidence_documents"] = [
            {
                "document_id": "SGDOC-capped",
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "canonical_url": url,
                "content_hash": hashlib.sha256(capped.encode()).hexdigest(),
                "content_text": capped,
                "source_provider": "PageFetcher",
                "source_family": "NAVER_DISCOVERY",
                "published_at": "2026-06-20",
                "available_at": "2026-06-20",
                "query_ids": ["QUERY-1"],
                "objective_ids": ["OBJECTIVE-1"],
                "full_fetch_performed": True,
                "evidence_eligible": True,
            }
        ]
        state["search_candidates"] = [
            candidate,
            unrelated_terminal_candidate,
        ]
        state["rejected_documents"] = [
            source_graph_module._candidate_rejection(
                unrelated_terminal_candidate,
                "UNKNOWN_PUBLISHED_DATE_AFTER_FULL_FETCH",
                retryable=False,
            )
        ]
        state["production_downstream_document_ids"] = ["SGDOC-capped"]
        checkpoint = source_graph_module._finalize_checkpoint(state)
        provider = SourceBrainProvider(queries=())
        search = RecordingSearchProvider({})

        with mock.patch.object(
            source_graph_module,
            "_validate_provider_mode",
        ):
            run = self._run(
                provider=provider,
                search=search,
                fetcher=PageFetcher(
                    fixture_text_by_url={url: repaired_text},
                    max_text_chars=(
                        source_graph_module.PRODUCTION_PAGE_FETCH_TEXT_CHAR_BOUND
                    ),
                ),
                config=SourceGraphAcquisitionConfig(
                    mode="PRODUCTION_DAILY",
                    max_queries_per_checkpoint=1,
                    max_candidates_per_checkpoint=10,
                    max_fetches_per_checkpoint=2,
                ),
                checkpoint=checkpoint,
                resolved_objective_ids=("OBJECTIVE-1",),
                checkpoint_source_repair_only=True,
            )

        self.assertEqual(provider.calls, [])
        self.assertEqual(search.calls, [])
        self.assertTrue(run.audit["checkpoint_source_repair_only"])
        self.assertNotIn(
            "SGDOC-capped",
            {row["document_id"] for row in run.evidence_documents},
        )
        self.assertEqual(
            source_graph_module.validated_quarantined_document_ids(
                run.checkpoint
            ),
            frozenset({"SGDOC-capped"}),
        )
        repaired_candidate = next(
            row
            for row in run.checkpoint["search_candidates"]
            if row["candidate_id"] == "CAPPED-CANDIDATE"
        )
        self.assertEqual(
            repaired_candidate["fetch_status"],
            "FULL_DOCUMENT_FETCHED",
        )
        self.assertNotEqual(
            repaired_candidate["document_id"],
            "SGDOC-capped",
        )
        self.assertFalse(repaired_candidate["source_repair_pending"])
        unchanged_unrelated = next(
            row
            for row in run.checkpoint["search_candidates"]
            if row["candidate_id"] == "UNRELATED-TERMINAL-CANDIDATE"
        )
        self.assertEqual(
            unchanged_unrelated["fetch_status"],
            "FETCH_REJECTED",
        )
        self.assertNotIn(
            "publication_metadata_fetch_retry_attempted",
            unchanged_unrelated,
        )
        self.assertFalse(
            any(
                row.get("fetch_status")
                in {"MATERIAL_PENDING_FETCH", "FETCH_RETRY_PENDING"}
                for row in run.checkpoint["search_candidates"]
                if row["candidate_id"] != "CAPPED-CANDIDATE"
            )
        )
        self.assertEqual(
            run.checkpoint["production_downstream_document_ids"],
            [repaired_candidate["document_id"]],
        )
        repaired_document = run.evidence_documents[0]
        self.assertEqual(
            repaired_document["source_repair_replaces_document_id"],
            "SGDOC-capped",
        )
        self.assertIn("Page 299", repaired_document["content_text"])
        self.assertGreater(len(repaired_document["content_text"]), 500_000)
        self.assertEqual(
            source_graph_module.source_graph_pending_source_repair_ids(
                run.checkpoint
            ),
            (),
        )
        self.assertFalse(
            any(
                row.get("graph_expansion_parent_candidate_ids")
                == ["CAPPED-CANDIDATE"]
                for row in run.checkpoint["search_candidates"]
                if row["candidate_id"] != "CAPPED-CANDIDATE"
            )
        )

    def test_source_repair_failure_remains_pending_across_identical_retries(
        self,
    ) -> None:
        url = "https://issuer.example.com/capped-pending.pdf"
        capped = ("Current Corp legacy capped evidence " * 8_000)[:199_999]
        for fetcher in (
            IncompleteBoundedRepairFetcher(
                max_text_chars=(
                    source_graph_module.PRODUCTION_PAGE_FETCH_TEXT_CHAR_BOUND
                )
            ),
            TimeoutRepairFetcher(
                max_text_chars=(
                    source_graph_module.PRODUCTION_PAGE_FETCH_TEXT_CHAR_BOUND
                )
            ),
        ):
            with self.subTest(fetcher=type(fetcher).__name__):
                candidate = {
                    "candidate_id": "CAPPED-PENDING-CANDIDATE",
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "ranking_status": "MATERIAL",
                    "fetch_status": "FULL_DOCUMENT_FETCHED",
                    "document_id": "SGDOC-capped-pending",
                    "url": url,
                    "normalized_url": url,
                    "title": "Current Corp capped filing",
                    "query_ids": ["QUERY-1"],
                    "objective_ids": ["OBJECTIVE-1"],
                    "published_at": "2026-06-20",
                }
                state = source_graph_module._new_acquisition_state(
                    target_id=TARGET,
                    target_name=TARGET_NAME,
                    as_of_date=AS_OF_DATE,
                    mode="PRODUCTION_DAILY",
                )
                state["status"] = "EPOCH_COMPLETE_REQUIRES_SUPERVISOR"
                state["evidence_documents"] = [
                    {
                        "document_id": "SGDOC-capped-pending",
                        "target_id": TARGET,
                        "as_of_date": AS_OF_DATE,
                        "canonical_url": url,
                        "content_hash": hashlib.sha256(
                            capped.encode()
                        ).hexdigest(),
                        "content_text": capped,
                        "source_provider": "PageFetcher",
                        "source_family": "ISSUER_NEWSROOM",
                        "published_at": "2026-06-20",
                        "query_ids": ["QUERY-1"],
                        "objective_ids": ["OBJECTIVE-1"],
                        "full_fetch_performed": True,
                        "evidence_eligible": True,
                    }
                ]
                state["search_candidates"] = [candidate]
                state["production_downstream_document_ids"] = [
                    "SGDOC-capped-pending"
                ]
                checkpoint = source_graph_module._finalize_checkpoint(state)
                provider = SourceBrainProvider(queries=())
                search = RecordingSearchProvider({})
                config = SourceGraphAcquisitionConfig(
                    mode="PRODUCTION_DAILY",
                    max_queries_per_checkpoint=1,
                    max_candidates_per_checkpoint=10,
                    max_fetches_per_checkpoint=1,
                )

                with mock.patch.object(
                    source_graph_module,
                    "_validate_provider_mode",
                ):
                    first = self._run(
                        provider=provider,
                        search=search,
                        fetcher=fetcher,
                        config=config,
                        checkpoint=checkpoint,
                        resolved_objective_ids=("OBJECTIVE-1",),
                        checkpoint_source_repair_only=True,
                    )
                    second = self._run(
                        provider=provider,
                        search=search,
                        fetcher=fetcher,
                        config=config,
                        checkpoint=first.checkpoint,
                        resolved_objective_ids=("OBJECTIVE-1",),
                        checkpoint_source_repair_only=True,
                    )

                self.assertEqual(provider.calls, [])
                self.assertEqual(search.calls, [])
                self.assertEqual(first.status, "SOURCE_PROVIDER_PENDING")
                self.assertEqual(second.status, "SOURCE_PROVIDER_PENDING")
                self.assertEqual(
                    source_graph_module.source_graph_pending_source_repair_ids(
                        second.checkpoint
                    ),
                    ("SGDOC-capped-pending",),
                )
                self.assertFalse(
                    _source_checkpoint_is_ready_for_readonly_replay(
                        second.checkpoint
                    )
                )
                pending_candidate = second.checkpoint[
                    "search_candidates"
                ][0]
                self.assertEqual(
                    pending_candidate["fetch_status"],
                    "FETCH_RETRY_PENDING",
                )
                self.assertGreaterEqual(
                    pending_candidate["same_fetch_failure_count"],
                    2,
                )
                self.assertEqual(second.evidence_documents, ())

    def test_exact_quote_failure_reopens_only_the_named_stale_pdf(self) -> None:
        document_id = "SGDOC-abcdef123456"
        context = {
            "nested": [
                "MATERIAL_FACT_PROPOSAL_REJECTED:"
                f"{document_id}:EXACT_QUOTE_NOT_IN_FULL_DOCUMENT"
            ]
        }
        self.assertEqual(
            source_graph_module._fact_parser_repair_document_ids(context),
            (document_id,),
        )
        content = "Current Corp complete PDF text " * 20
        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        candidate = {
            "candidate_id": "STALE-PDF-CANDIDATE",
            "ranking_status": "MATERIAL",
            "fetch_status": "FULL_DOCUMENT_FETCHED",
            "document_id": document_id,
            "url": "https://issuer.example.com/stale-reading-order.pdf",
            "query_ids": ["QUERY-1"],
            "objective_ids": ["OBJECTIVE-1"],
        }
        state = {
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "evidence_documents": [
                {
                    "document_id": document_id,
                    "target_id": TARGET,
                    "as_of_date": AS_OF_DATE,
                    "canonical_url": candidate["url"],
                    "content_hash": content_hash,
                    "content_text": content,
                    "source_provider": "PageFetcher",
                    "query_ids": ["QUERY-1"],
                    "objective_ids": ["OBJECTIVE-1"],
                }
            ],
            "search_candidates": [candidate],
            "quarantined_documents": [],
            "rejected_documents": [],
            "query_failures": [],
        }

        reasons = source_graph_module._quarantine_unreadable_documents(
            state,
            parser_repair_document_ids=(document_id,),
        )

        self.assertEqual(
            reasons,
            ("STALE_PDF_READING_ORDER:EXACT_QUOTE_VALIDATION_FAILED",),
        )
        self.assertEqual(state["evidence_documents"], [])
        self.assertEqual(candidate["fetch_status"], "MATERIAL_PENDING_FETCH")
        self.assertEqual(
            source_graph_module.validated_quarantined_document_ids(state),
            frozenset({document_id}),
        )

    def test_archive_like_unknown_date_retry_remains_one_time(self) -> None:
        candidate = {
            "candidate_id": "ARCHIVE-LIST",
            "ranking_status": "MATERIAL",
            "fetch_status": "FETCH_REJECTED",
            "url": "https://issuer.example.com/tag/results",
        }
        rejected = (
            {
                "candidate_id": "ARCHIVE-LIST",
                "rejection_reason": "UNKNOWN_PUBLISHED_DATE_AFTER_FULL_FETCH",
            },
        )
        self.assertEqual(
            source_graph_module._reopen_fetch_semantics_candidates(
                [candidate], rejected_documents=rejected
            ),
            1,
        )
        candidate["fetch_status"] = "FETCH_REJECTED"
        self.assertEqual(
            source_graph_module._reopen_fetch_semantics_candidates(
                [candidate], rejected_documents=rejected
            ),
            0,
        )

    def test_ranker_receives_requested_family_and_verified_official_hint(self) -> None:
        provider = SourceBrainProvider(
            source_families=("ISSUER_PRESENTATION",),
        )
        url = "https://ir.example.com/2026q1.pdf"
        self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {QUERY: (_result("Current Corp issuer presentation", url),)}
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={url: _document_text("issuer-presentation")}
            ),
            official_domains=("example.com",),
        )
        ranking_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )
        candidate = ranking_payload["discovery_candidates"][0]
        self.assertEqual(
            candidate["requested_source_families"],
            ["ISSUER_PRESENTATION"],
        )
        self.assertTrue(candidate["verified_official_domain_candidate"])
        self.assertEqual(
            candidate["candidate_source_family_hint"],
            "ISSUER_NEWSROOM",
        )

    def test_customer_official_request_does_not_fetch_third_party_retelling(
        self,
    ) -> None:
        class CustomerSourceAwareProvider(SourceBrainProvider):
            def complete(self, *, pass_name, payload):
                if pass_name != "SOURCE_CANDIDATE_RANKING":
                    return super().complete(
                        pass_name=pass_name,
                        payload=payload,
                    )
                self.calls.append(
                    {"pass_name": pass_name, "payload": payload}
                )
                return {
                    "decisions": [
                        {
                            "candidate_id": row["candidate_id"],
                            "material_relevance": (
                                "customer.example.com/platform/hbm"
                                in str(row["url"])
                            ),
                            "priority": 1.0,
                            "objective_ids": list(row["objective_ids"]),
                            "matched_requested_source_family": (
                                "CUSTOMER_OFFICIAL"
                                if "customer.example.com"
                                in str(row["url"])
                                else "NONE"
                            ),
                            "rationale": (
                                "고객 소유 도메인의 원문만 고객 공식 "
                                "source 요청을 충족한다."
                            ),
                        }
                        for row in payload["discovery_candidates"]
                    ],
                    "ranking_complete": True,
                    "unresolved_notes": [],
                }

        provider = CustomerSourceAwareProvider(
            source_families=("CUSTOMER_OFFICIAL",),
        )
        blog_url = "https://writer.example.net/hbm-retelling"
        customer_url = "https://news.customer.example.com/platform/hbm"
        wrong_subject_customer_url = (
            "https://customer.example.com/careers/accounting"
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result("Current Corp HBM 해설", blog_url),
                        _result(
                            "Current Corp HBM platform",
                            customer_url,
                            is_news=True,
                        ),
                        _result(
                            "Customer Corp accounting careers",
                            wrong_subject_customer_url,
                        ),
                    )
                }
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={
                    blog_url: _document_text("third-party-retelling"),
                    customer_url: _document_text("customer-original"),
                    wrong_subject_customer_url: _document_text(
                        "wrong-subject-customer-original"
                    ),
                }
            ),
        )

        self.assertEqual(len(run.evidence_documents), 1)
        self.assertEqual(
            run.evidence_documents[0]["canonical_url"],
            customer_url,
        )
        self.assertEqual(
            run.evidence_documents[0]["source_family"],
            "CUSTOMER_OFFICIAL",
        )
        self.assertEqual(
            run.evidence_documents[0]["source_family_observations"],
            ["TRUSTED_BUSINESS_MEDIA", "CUSTOMER_OFFICIAL"],
        )
        self.assertTrue(
            run.evidence_documents[0][
                "source_family_assigned_by_candidate_ranker"
            ]
        )
        self.assertEqual(
            run.evidence_documents[0]["source_independence_group"],
            "CUSTOMER_OFFICIAL:news.customer.example.com",
        )
        self.assertEqual(
            run.evidence_documents[0]["verified_official_discovery_urls"],
            [customer_url],
        )
        candidates = {
            row["url"]: row
            for row in run.checkpoint["search_candidates"]
        }
        self.assertEqual(
            candidates[blog_url]["fetch_status"],
            "DISCOVERY_ONLY_NOT_FETCHED",
        )
        self.assertEqual(
            candidates[blog_url]["matched_requested_source_family"],
            "NONE",
        )
        self.assertEqual(
            candidates[wrong_subject_customer_url]["fetch_status"],
            "DISCOVERY_ONLY_NOT_FETCHED",
        )
        self.assertEqual(
            candidates[wrong_subject_customer_url][
                "matched_requested_source_family"
            ],
            "CUSTOMER_OFFICIAL",
        )

    def test_customer_official_override_preserves_strong_classifiers(
        self,
    ) -> None:
        for weak_family in (
            "GENERAL_WEB_DISCOVERY",
            "TRUSTED_BUSINESS_MEDIA",
        ):
            with self.subTest(weak_family=weak_family):
                self.assertTrue(
                    source_graph_module._ranker_customer_official_provenance_applies(
                        classified_source_family=weak_family,
                        matched_requested_source_family="CUSTOMER_OFFICIAL",
                    )
                )
        for strong_family in (
            "OPENDART",
            "KIND_KRX",
            "ISSUER_NEWSROOM",
            "REUTERS",
            "PUBLIC_BROKER_PDF",
        ):
            with self.subTest(strong_family=strong_family):
                self.assertFalse(
                    source_graph_module._ranker_customer_official_provenance_applies(
                        classified_source_family=strong_family,
                        matched_requested_source_family="CUSTOMER_OFFICIAL",
                    )
                )

    def test_checkpoint_migrates_exact_customer_news_provenance_once(
        self,
    ) -> None:
        url = "https://news.customer.example.com/releases/memory"
        text = _document_text("customer-newsroom-provenance")
        candidate = {
            "candidate_id": "CUSTOMER-NEWSROOM",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "url": url,
            "normalized_url": url,
            "query_ids": ["QUERY-1"],
            "materiality_query_ids": ["QUERY-1"],
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["CUSTOMER_OFFICIAL"],
            "matched_requested_source_family": "CUSTOMER_OFFICIAL",
            "materiality_decision_id": "DECISION-CUSTOMER-NEWSROOM",
            "ranking_status": "MATERIAL",
            "fetch_status": "FULL_DOCUMENT_FETCHED",
            "document_id": "SGDOC-CUSTOMER-NEWSROOM",
            "is_news": True,
        }
        candidate["materiality_scope_hash"] = (
            source_graph_module._candidate_materiality_scope_hash(candidate)
        )
        document = {
            "schema_version": "e2r_v5_source_graph_document_v1",
            "document_id": "SGDOC-CUSTOMER-NEWSROOM",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "canonical_url": url,
            "title": "Customer official memory release",
            "source_family": "TRUSTED_BUSINESS_MEDIA",
            "source_family_observations": ["TRUSTED_BUSINESS_MEDIA"],
            "source_provider": "PageFetcher",
            "published_at": "2026-06-20",
            "available_at": "2026-06-20",
            "content_type": "text/html",
            "content_hash": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "content_text": text,
            "query_ids": ["QUERY-1"],
            "materiality_query_ids": ["QUERY-1"],
            "objective_ids": ["OBJECTIVE-1"],
            "requested_source_families": ["CUSTOMER_OFFICIAL"],
            "matched_requested_source_family": "CUSTOMER_OFFICIAL",
            "materiality_scope_hash": candidate["materiality_scope_hash"],
            "materiality_scope_url": url,
            "source_materiality_decision_id": (
                "DECISION-CUSTOMER-NEWSROOM"
            ),
            "source_family_assigned_by_candidate_ranker": False,
            "source_independence_group": (
                "TRUSTED_BUSINESS_MEDIA:news.customer.example.com"
            ),
            "verified_official_discovery_urls": [],
            "referenced_urls": [],
            "referenced_document_ids": [],
            "full_fetch_performed": True,
            "snippet_only": False,
            "snippet_used_as_document": False,
            "evidence_eligible": True,
            "production_score_authority": False,
        }
        state = source_graph_module._new_acquisition_state(
            target_id=TARGET,
            target_name=TARGET_NAME,
            as_of_date=AS_OF_DATE,
            mode="TEST",
        )
        state["search_candidates"] = [candidate]
        state["candidate_materiality_decisions"] = [
            {
                "decision_id": "DECISION-CUSTOMER-NEWSROOM",
                "candidate_id": "CUSTOMER-NEWSROOM",
                "material_relevance": True,
                "priority": 1.0,
                "objective_ids": ["OBJECTIVE-1"],
                "matched_requested_source_family": "CUSTOMER_OFFICIAL",
                "rationale": "customer-owned official newsroom source",
            }
        ]
        state["evidence_documents"] = [document]
        checkpoint = source_graph_module._finalize_checkpoint(state)
        self.assertEqual(
            source_graph_module.source_graph_ranker_customer_official_reclassification_document_ids(
                checkpoint
            ),
            frozenset({"SGDOC-CUSTOMER-NEWSROOM"}),
        )

        first = self._run(
            provider=SourceBrainProvider(),
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=checkpoint,
            checkpoint_migration_only=True,
        )

        self.assertEqual(len(first.evidence_documents), 1)
        migrated = first.evidence_documents[0]
        self.assertEqual(migrated["document_id"], document["document_id"])
        self.assertEqual(migrated["content_hash"], document["content_hash"])
        self.assertEqual(migrated["source_family"], "CUSTOMER_OFFICIAL")
        self.assertEqual(
            migrated["source_family_before_provenance_reclassification"],
            "TRUSTED_BUSINESS_MEDIA",
        )
        self.assertEqual(
            migrated["source_independence_group"],
            "CUSTOMER_OFFICIAL:news.customer.example.com",
        )
        self.assertTrue(migrated["source_family_provenance_reclassified"])
        self.assertTrue(migrated["source_family_assigned_by_candidate_ranker"])
        self.assertEqual(first.audit["source_family_provenance_reclassified_count"], 1)
        self.assertEqual(first.checkpoint["fetch_records"], [])
        self.assertEqual(
            source_graph_module.source_graph_ranker_customer_official_reclassification_document_ids(
                first.checkpoint
            ),
            frozenset(),
        )

        second = self._run(
            provider=SourceBrainProvider(),
            search=RecordingSearchProvider({}),
            fetcher=PageFetcher(fixture_text_by_url={}),
            checkpoint=first.checkpoint,
            checkpoint_migration_only=True,
        )

        self.assertEqual(
            second.audit["source_family_provenance_reclassified_count"],
            0,
        )
        self.assertEqual(len(second.evidence_documents), 1)
        self.assertEqual(second.checkpoint["fetch_records"], [])

    def test_ranker_prompt_compacts_complete_large_fact_graph(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/large-fact-ranking"
        facts = tuple(
            {
                "fact_id": f"FACT-{index:04d}",
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "subject": "현재 회사",
                "business_segment": f"사업부-{index % 4}",
                "product_family": f"제품군-{index % 9}",
                "economic_mechanism": (
                    f"서로 다른 경제 메커니즘 {index}: "
                    + "계약·현금전환·CAPA·가격 지속성 검증 " * 12
                ),
                "predicate": f"PREDICATE-{index % 37}",
                "value": index % 101,
                "unit": "KRW",
                "period": f"2026Q{index % 4 + 1}",
                "direction": "COUNTER" if index % 7 == 0 else "POSITIVE",
                "current_lifecycle": (
                    "CURRENT" if index < 1_000 else "SUPERSEDED"
                ),
                "confidence": 0.9,
                "structured_evidence_roles": ["FORWARD_GUIDANCE"],
                "allowed_component_ids": ["eps_fcf_explosion"],
            }
            for index in range(3_000)
        )
        self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {QUERY: (_result("Current Corp material", url),)}
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={url: _document_text("large-fact-ranking")}
            ),
            current_evidence_facts=facts,
        )
        ranking_payload = next(
            row["payload"]
            for row in provider.calls
            if row["pass_name"] == "SOURCE_CANDIDATE_RANKING"
        )
        projection = ranking_payload["current_evidence_fact_graph"]
        encoded = json.dumps(ranking_payload, ensure_ascii=False, sort_keys=True)
        self.assertEqual(projection["input_fact_count"], 3_000)
        self.assertEqual(projection["fact_count"], 1_000)
        self.assertEqual(projection["closed_fact_count"], 2_000)
        self.assertTrue(projection["every_input_fact_accounted"])
        self.assertTrue(projection["every_current_fact_individually_accounted"])
        self.assertFalse(projection["fact_ids_exposed_to_candidate_ranker"])
        self.assertEqual(
            projection["current_fact_profile"]["fact_count"],
            1_000,
        )
        self.assertEqual(
            projection["closed_fact_profile"]["fact_count"],
            2_000,
        )
        self.assertNotIn("FACT-0000", encoded)
        self.assertLess(len(encoded), 100_000)

    def test_http_last_modified_verifies_missing_search_result_date(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/undated-transcript.pdf"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp undated transcript",
                            url,
                            published=None,
                        ),
                    )
                }
            ),
            fetcher=LastModifiedFetcher(url=url),
        )
        document = next(
            row
            for row in run.evidence_documents
            if row.get("canonical_url") == url
        )
        self.assertEqual(document["published_at"], "2026-05-11")
        self.assertEqual(document["publication_date_source"], "HTTP_LAST_MODIFIED")
        self.assertEqual(
            document["response_last_modified_at"],
            "2026-05-11T02:39:25",
        )

    def test_fetched_publication_metadata_verifies_missing_search_date(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/current-results"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp results",
                            url,
                            published=None,
                        ),
                    )
                }
            ),
            fetcher=PublicationMetadataFetcher(
                url=url,
                published_at="2026-04-07T07:45:00+09:00",
            ),
        )
        document = next(
            row
            for row in run.evidence_documents
            if row.get("canonical_url") == url
        )
        self.assertEqual(document["published_at"], "2026-04-07")
        self.assertEqual(
            document["publication_date_source"],
            "FETCHED_PUBLICATION_METADATA",
        )
        self.assertEqual(
            document["publication_metadata_semantics_version"],
            "e2r_page_fetch_publication_metadata_v1",
        )

    def test_future_fetched_publication_metadata_is_rejected(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/future-results"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp results",
                            url,
                            published=None,
                        ),
                    )
                }
            ),
            fetcher=PublicationMetadataFetcher(
                url=url,
                published_at="2026-06-30T07:45:00+09:00",
            ),
        )
        self.assertFalse(
            any(row.get("canonical_url") == url for row in run.evidence_documents)
        )
        self.assertTrue(
            any(
                row.get("rejection_reason")
                == "FUTURE_DOCUMENT_AFTER_FULL_FETCH"
                for row in run.checkpoint["rejected_documents"]
            )
        )

    def test_future_leading_press_release_date_is_rejected(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/future-press-release"
        text = (
            "Official Newsroom\n"
            "Press Release\n"
            "Current Corp Announces Technology Partnership\n"
            "Collaboration Supports Next-Generation Systems\n"
            "July 2, 2026\n"
            "News Summary:\n"
            "Current Corp disclosed capacity, customer qualification, pricing, "
            "cash conversion, and counter evidence. "
            + "source-backed release detail " * 12
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp technology partnership",
                            url,
                            published=None,
                        ),
                    )
                }
            ),
            fetcher=PageFetcher(fixture_text_by_url={url: text}),
        )
        self.assertFalse(
            any(row.get("canonical_url") == url for row in run.evidence_documents)
        )
        self.assertTrue(
            any(
                row.get("rejection_reason")
                == "FUTURE_DOCUMENT_AFTER_FULL_FETCH"
                for row in run.checkpoint["rejected_documents"]
            )
        )

    def test_navigation_heavy_press_release_details_is_fetched_with_date(
        self,
    ) -> None:
        provider = SourceBrainProvider(
            source_families=("CUSTOMER_OFFICIAL",),
        )
        url = "https://customer.example.com/investor/press-release-details"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp customer collaboration release",
                            url,
                            published=None,
                        ),
                    )
                }
            ),
            fetcher=PageFetcher(
                fixture_text_by_url={
                    url: _navigation_heavy_press_release_details_text()
                }
            ),
        )

        document = next(
            row
            for row in run.evidence_documents
            if row.get("canonical_url") == url
        )
        self.assertEqual(document["published_at"], "2025-10-31")
        self.assertEqual(
            document["publication_date_source"],
            "DOCUMENT_CONTENT_INFERENCE",
        )
        self.assertEqual(document["publication_metadata_parts"], [])
        self.assertFalse(
            any(
                row.get("rejection_reason")
                == "UNKNOWN_PUBLISHED_DATE_AFTER_FULL_FETCH"
                for row in run.checkpoint["rejected_documents"]
            )
        )

    def test_old_http_header_cannot_mask_future_labelled_publication_date(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/future-transcript.pdf"
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp transcript",
                            url,
                            published=None,
                        ),
                    )
                }
            ),
            fetcher=LastModifiedFetcher(
                url=url,
                text=(
                    "Published 2026-07-02\nCurrent Corp disclosed current earnings, "
                    "capacity, cash conversion, customer allocation, and counter "
                    "evidence. "
                    + "source-backed detail " * 12
                ),
            ),
        )
        self.assertFalse(
            any(row.get("canonical_url") == url for row in run.evidence_documents)
        )
        self.assertTrue(
            any(
                row.get("rejection_reason")
                == "FUTURE_DOCUMENT_AFTER_FULL_FETCH"
                for row in run.checkpoint["rejected_documents"]
            )
        )

    def test_split_article_input_date_outranks_site_registration_footer(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/article-with-split-date"
        text = (
            "입력\n"
            "2025-09-24 13:34\n"
            "Current Corp disclosed HBM capacity, customer qualification, pricing, "
            "cash conversion, and counter evidence in the full article. "
            + "source-backed article detail " * 12
            + "\n인터넷신문 등록번호\n등록일자 : 2016.04.26\n"
            "발행일자 : 2016.04.01\n"
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp HBM article",
                            url,
                            published=None,
                        ),
                    )
                }
            ),
            fetcher=PageFetcher(fixture_text_by_url={url: text}),
        )
        document = next(
            row
            for row in run.evidence_documents
            if row.get("canonical_url") == url
        )
        self.assertEqual(document["published_at"], "2025-09-24")
        self.assertEqual(
            document["publication_date_source"],
            "DOCUMENT_CONTENT_INFERENCE",
        )

    def test_split_newswire_transmission_date_is_article_metadata(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/newswire-with-split-date"
        text = (
            "Current Corp HBM article\n"
            "송고\n"
            "2025-07-08 05:01\n"
            "Current Corp disclosed HBM capacity, customer qualification, pricing, "
            "cash conversion, and counter evidence in the full article. "
            + "source-backed newswire detail " * 12
            + "\n인터넷신문 등록번호\n등록일자 : 2016.04.26\n"
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp HBM newswire",
                            url,
                            published=None,
                        ),
                    )
                }
            ),
            fetcher=PageFetcher(fixture_text_by_url={url: text}),
        )
        document = next(
            row
            for row in run.evidence_documents
            if row.get("canonical_url") == url
        )
        self.assertEqual(document["published_at"], "2025-07-08")

    def test_split_future_input_date_cannot_hide_behind_old_site_footer(self) -> None:
        provider = SourceBrainProvider()
        url = "https://example.com/future-article-with-split-date"
        text = (
            "입력\n"
            "2026-07-02 09:30\n"
            "Current Corp disclosed HBM capacity, customer qualification, pricing, "
            "cash conversion, and counter evidence in the full article. "
            + "source-backed future article detail " * 12
            + "\n인터넷신문 등록번호\n등록일자 : 2016.04.26\n"
            "발행일자 : 2016.04.01\n"
        )
        run = self._run(
            provider=provider,
            search=RecordingSearchProvider(
                {
                    QUERY: (
                        _result(
                            "Current Corp future HBM article",
                            url,
                            published=None,
                        ),
                    )
                }
            ),
            fetcher=PageFetcher(fixture_text_by_url={url: text}),
        )
        self.assertFalse(
            any(row.get("canonical_url") == url for row in run.evidence_documents)
        )
        self.assertTrue(
            any(
                row.get("rejection_reason")
                == "FUTURE_DOCUMENT_AFTER_FULL_FETCH"
                for row in run.checkpoint["rejected_documents"]
            )
        )

    def _run(
        self,
        *,
        provider: SourceBrainProvider,
        search,
        fetcher: PageFetcher,
        config: SourceGraphAcquisitionConfig | None = None,
        checkpoint: Mapping[str, Any] | None = None,
        official_gaps: Mapping[str, Sequence[str]] | None = None,
        official_documents: Sequence[Mapping[str, Any]] = (),
        official_domains: Sequence[str] = (),
        current_evidence_facts: Sequence[Mapping[str, Any]] = (),
        target_business_model: Mapping[str, Any] | None = None,
        source_coverage: Sequence[str | Mapping[str, Any]] = (),
        score_gap_context: Mapping[str, Any] | None = None,
        checkpoint_migration_only: bool = False,
        checkpoint_source_repair_only: bool = False,
        resolved_objective_ids: Sequence[str] = (),
        open_objectives: Sequence[SourceResearchObjective] | None = None,
    ):
        return ResearcherSourceGraphAcquirer(
            query_provider=provider,
            search_provider=search,
            page_fetcher=fetcher,
        ).acquire(
            config=config or SourceGraphAcquisitionConfig(mode="TEST"),
            target_id=TARGET,
            target_name=TARGET_NAME,
            target_aliases=(),
            as_of_date=AS_OF_DATE,
            open_objectives=tuple(open_objectives or (_objective(),)),
            current_evidence_facts=current_evidence_facts,
            target_business_model=target_business_model,
            source_coverage=source_coverage,
            official_documents=official_documents,
            official_gap_reasons_by_objective=(
                official_gaps
                if official_gaps is not None
                else {"OBJECTIVE-1": ("official source gap recorded",)}
            ),
            score_gap_context=score_gap_context,
            resolved_objective_ids=resolved_objective_ids,
            prior_checkpoint=checkpoint,
            official_domain_allowlist=official_domains,
            checkpoint_migration_only=checkpoint_migration_only,
            checkpoint_source_repair_only=checkpoint_source_repair_only,
        )


def _objective() -> SourceResearchObjective:
    return SourceResearchObjective(
        objective_id="OBJECTIVE-1",
        component_id="eps_fcf_explosion",
        research_objective="actual earnings and capacity conversion",
        preferred_source_families=("NAVER_DISCOVERY",),
        counter_or_supersession_required=True,
    )


def _result(
    title: str,
    url: str,
    *,
    rank: int = 1,
    published: str | None = "2026-06-20",
    query: str = QUERY,
    is_news: bool | None = None,
) -> SearchResult:
    return SearchResult(
        title=title,
        url=url,
        snippet=f"{TARGET_NAME} full report discovery metadata",
        source="fixture-search",
        published_at=(datetime.fromisoformat(published) if published else None),
        query=query,
        rank=rank,
        is_news=("reuters" in url if is_news is None else is_news),
    )


def _document_text(unique: str) -> str:
    return (
        f"Published 2026-06-20\n{TARGET_NAME} disclosed current earnings, capacity, "
        f"cash conversion, customer allocation, and counter evidence. {unique} "
        + "source-backed detail " * 10
    )


def _navigation_heavy_press_release_details_text() -> str:
    before_marker = "\n".join(
        f"Header navigation item {index}" for index in range(66)
    )
    after_marker = "\n".join(
        f"Investor navigation item {index}" for index in range(30)
    )
    return (
        "Current Corp Investor Relations\n"
        + before_marker
        + "\nPress Release Details\n"
        + after_marker
        + "\nView all news\n"
        "Current Corp and Customer Build AI Factory\n"
        "October 31, 2025\n"
        "Download this Press Release\n"
        "Current Corp and its customer described HBM3E and HBM4 collaboration, "
        "capacity qualification, cash conversion, and counter evidence. "
        + "source-backed release detail " * 12
    )


def _official_document(document_id: str, family: str) -> Mapping[str, Any]:
    text = _document_text(document_id)
    return {
        "document_id": document_id,
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "canonical_url": f"https://official.example.com/{document_id}",
        "source_family": family,
        "published_at": "2026-06-19",
        "content_text": text,
        "content_hash": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "evidence_eligible": True,
    }


if __name__ == "__main__":
    unittest.main()
