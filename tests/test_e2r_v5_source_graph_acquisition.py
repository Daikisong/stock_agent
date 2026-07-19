from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.page_fetcher import FetchResult, PageFetcher
from e2r.research.publication_date import (
    infer_source_locator_publication_date,
)
from e2r.research.search_provider import SearchResult
import e2r.research_brain.researcher_mode.source_graph_explorer as source_graph_module
from e2r.research_brain.researcher_mode import (
    PHASE85_PASS,
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
                        "rationale": "research objective와 직접 관련된 후보",
                    }
                    for index, row in enumerate(rows)
                ],
                "ranking_complete": True,
                "unresolved_notes": [],
            }
        raise AssertionError(pass_name)


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
            all(row["ranking_status"] == "PENDING" for row in stale_candidates)
        )

    def test_production_general_web_requires_recorded_official_gap(self) -> None:
        provider = SourceBrainProvider()
        naver = NoNetworkLiveNaver()
        fetcher = PageFetcher(live_enabled=True)
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
        current_parent = {
            **old_parent,
            "candidate_id": "CURRENT-OFFICIAL-PARENT",
            "url": "https://ir.example.com/event?id=current",
            "query_ids": ["QUERY-CURRENT"],
            "discovered_referenced_urls": [
                "https://ir.example.com/current/2026Q1/transcript"
            ],
        }
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
        self.assertTrue(pdf_candidate["pdf_fallback_fetch_retry_attempted"])

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

    def test_legacy_text_cap_document_is_quarantined_and_refetched_once(self) -> None:
        content = "x" * 200_000
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
        self.assertEqual(candidate["fetch_status"], "MATERIAL_PENDING_FETCH")
        self.assertTrue(candidate["parser_semantics_refetch_required"])
        self.assertEqual(
            source_graph_module.validated_quarantined_document_ids(state),
            frozenset({"SGDOC-capped"}),
        )

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
            open_objectives=(_objective(),),
            current_evidence_facts=current_evidence_facts,
            target_business_model=None,
            source_coverage=(),
            official_documents=official_documents,
            official_gap_reasons_by_objective=(
                official_gaps
                if official_gaps is not None
                else {"OBJECTIVE-1": ("official source gap recorded",)}
            ),
            prior_checkpoint=checkpoint,
            official_domain_allowlist=official_domains,
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
) -> SearchResult:
    return SearchResult(
        title=title,
        url=url,
        snippet=f"{TARGET_NAME} full report discovery metadata",
        source="fixture-search",
        published_at=(datetime.fromisoformat(published) if published else None),
        query=query,
        rank=rank,
        is_news="reuters" in url,
    )


def _document_text(unique: str) -> str:
    return (
        f"Published 2026-06-20\n{TARGET_NAME} disclosed current earnings, capacity, "
        f"cash conversion, customer allocation, and counter evidence. {unique} "
        + "source-backed detail " * 10
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
