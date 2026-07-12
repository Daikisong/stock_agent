from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.page_fetcher import PageFetcher
from e2r.research.search_provider import SearchResult
from e2r.research_brain.researcher_mode import (
    PHASE85_PASS,
    ComponentResearchPlan,
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


class SourceBrainProvider:
    provider_name = "TEST_FIXTURE_SOURCE_BRAIN"

    def __init__(
        self,
        *,
        queries: Sequence[str] = (QUERY,),
        material_titles: Sequence[str] = (),
        omit_last_ranking: bool = False,
    ) -> None:
        self.queries = tuple(queries)
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
                        "source_families": ["NAVER_DISCOVERY"],
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


class E2RV5SourceGraphAcquisitionTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

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
        self.assertTrue(query_payload["prior_query_or_source_failures"])
        self.assertIn(
            "LLM_RETURNED_NO_NEW_VALID_QUERY",
            query_payload["prior_query_or_source_failures"][0]["failure_reason"],
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
        self.assertTrue(
            any(reason.startswith("SNIPPET_ONLY_FULL_FETCH_REQUIRED") for reason in reasons)
        )
        self.assertEqual(run.audit["critical_counts"]["snippet_evidence_document_count"], 0)

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
            current_evidence_facts=(),
            target_business_model=None,
            source_coverage=(),
            official_documents=official_documents,
            official_gap_reasons_by_objective=(
                official_gaps
                if official_gaps is not None
                else {"OBJECTIVE-1": ("official source gap recorded",)}
            ),
            prior_checkpoint=checkpoint,
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
    published: str = "2026-06-20",
    query: str = QUERY,
) -> SearchResult:
    return SearchResult(
        title=title,
        url=url,
        snippet=f"{TARGET_NAME} full report discovery metadata",
        source="fixture-search",
        published_at=datetime.fromisoformat(published),
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
