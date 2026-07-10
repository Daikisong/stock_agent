from __future__ import annotations

import unittest
from dataclasses import replace
from datetime import datetime
from pathlib import Path

from e2r.agentic.evidence_os import EvidenceDocument, SourceType
from e2r.research.page_fetcher import PageFetcher
from e2r.research.search_provider import FixtureSearchProvider, SearchResult
from e2r.research_brain.compiler import (
    compile_case_level_source_verification,
    compile_research_intelligence,
    load_historical_case_source_links,
    load_historical_provider_snapshots,
)
from e2r.research_brain.intelligence_schema import (
    CurrentEvidenceFact,
    PlannerSourceTaskDraft,
)
from e2r.research_brain.planning import (
    FixtureQuestionQueryProvider,
    QueryGeneratorKind,
    compile_question_task_context,
    plan_question_source_task,
)
from e2r.research_brain.recipes import compile_evidence_recipe_os
from e2r.research_brain.runtime import (
    AcquisitionMode,
    AcquisitionStatus,
    BudgetUsage,
    ConnectorBatch,
    DocumentCandidate,
    DocumentRejectionReason,
    RecipeDocumentSelector,
    SearchFetchSourceConnector,
    SourceAcquisitionEngine,
    StaticSourceConnector,
    adapt_v4_source_acquisition_result,
    audit_acquisition_results,
)
from e2r.research_brain.schemas import SourceTaskType
from e2r.research_brain.v4_schemas import SourceAcquisitionResultV4


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_FIXTURES = REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "corpus"
SOURCE_FIXTURES = (
    REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "source_verification"
)


class SourceAcquisitionDocumentSelectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mandatory = compile_research_intelligence(
            [CORPUS_FIXTURES / "golden_mandatory_cases.md"],
            repo_root=REPO_ROOT,
        )
        source_cases = compile_research_intelligence(
            [SOURCE_FIXTURES / "golden_source_cases.jsonl"],
            repo_root=REPO_ROOT,
        )
        cases = (*mandatory.cases, *source_cases.cases)
        source_result = compile_case_level_source_verification(
            cases,
            snapshots=load_historical_provider_snapshots(
                SOURCE_FIXTURES / "provider_snapshots.jsonl"
            ),
            case_source_links=load_historical_case_source_links(
                SOURCE_FIXTURES / "case_source_links.jsonl"
            ),
            repo_root=REPO_ROOT,
        )
        cls.recipes = compile_evidence_recipe_os(
            cases,
            source_verifications=source_result.verifications,
        ).recipes
        cls.recipe = next(
            recipe
            for recipe in cls.recipes
            if recipe.primitive_id == "customer_preorder_or_allocation"
        )
        cls.selector = RecipeDocumentSelector(
            {recipe.recipe_id: recipe for recipe in cls.recipes}
        )
        cls.task = cls._build_task(cls.recipe)

    @classmethod
    def _build_task(cls, recipe):
        context = compile_question_task_context(
            target_id="TARGET-000660",
            target_name="테스트기업",
            symbol="000660",
            target_aliases=("Test Company",),
            as_of_date="2025-03-31",
            current_facts=(
                CurrentEvidenceFact(
                    fact_id="FACT-1",
                    text="대상 회사는 고객 배정과 생산능력 제약을 설명했다.",
                    observed_date="2025-03-20",
                    target_relation="DIRECT",
                    current_status="CURRENT",
                ),
            ),
            missing_information=("계약 취소 조건과 구속력을 확인해야 한다.",),
        )
        draft = PlannerSourceTaskDraft(
            draft_id=f"DRAFT:{recipe.recipe_id}",
            recipe_id=recipe.recipe_id,
            question_to_answer=recipe.question_to_answer,
            why_material="현재 가설을 직접 문서와 반증 조건으로 확인해야 한다.",
            query_intent="대상 회사 공식 문서의 계약 조건을 기준일 이전 범위에서 찾는다.",
            preferred_source_families=recipe.preferred_source_families[:3],
            fallback_source_families=recipe.discovery_sources[:2],
            max_queries=3,
            max_candidates=20,
            max_fetches=5,
            stop_condition="직접 anchor와 counter check가 확인되면 중단한다.",
        )

        def query_callback(payload):
            return {
                "input_id": payload["input_id"],
                "literal_queries": [
                    "테스트기업 2025 1Q 공식 공시 IR 고객 계약 취소 조건"
                ],
                "generation_rationale": "대상과 기준 분기를 명시했다.",
                "ambiguity_reasons": [],
                "abstain": False,
                "abstention_reason": "",
            }

        result = plan_question_source_task(
            draft=draft,
            recipe=recipe,
            context=context,
            candidate_event_id="EVENT-1",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            provider=FixtureQuestionQueryProvider(callback=query_callback),
            test_mode=True,
        )
        return result.task

    def _production_contract_task(self):
        intent = replace(
            self.task.query_intent,
            generator_kind=QueryGeneratorKind.REAL_LLM.value,
            provider_name="contract-real-provider",
        )
        return replace(self.task, query_intent=intent, test_only=False)

    def _with_research_report_route(self, task=None):
        task = task or self.task
        route = replace(
            task.source_route,
            fallback_source_families=tuple(
                dict.fromkeys(
                    (*task.source_route.fallback_source_families, "ResearchReport")
                )
            ),
        )
        return replace(
            task,
            task_id=f"{task.task_id}:research-report",
            source_route=route,
        )

    def _text(self, *, target=True):
        company = "테스트기업" if target else "다른기업"
        return (
            f"{company} official filing\n"
            "customer allocation and supply agreement terms were disclosed.\n"
            "capacity and utilization remained constrained while product ASP increased.\n"
            "guidance and estimate revisions include cancellation counter checks."
        )

    def _candidate(
        self,
        *,
        task=None,
        candidate_id="CAND-1",
        source_family="DART",
        document_type="filing",
        published_at="2025-03-15",
        available_at="2025-03-15",
        full_text=None,
        content_hash="AUTO",
        full_fetch_performed=True,
        counts_as_live=False,
        is_snapshot=False,
        report_replay=False,
        fake_provider=True,
        is_repost=False,
        original_source_url="https://dart.example/document/1",
        original_source_verified=True,
        target_relation="DIRECT",
        discovery_source_family=None,
        provider_error=None,
    ):
        task = task or self.task
        text = self._text() if full_text is None else full_text
        if content_hash == "AUTO":
            import hashlib

            content_hash = hashlib.sha256(str(text).encode("utf-8")).hexdigest()
        return DocumentCandidate(
            candidate_id=candidate_id,
            task_id=task.task_id,
            recipe_id=task.recipe_id,
            provider_name="fixture-source-provider",
            source_family=source_family,
            document_type=document_type,
            title="테스트기업 공식 문서",
            canonical_url=f"https://source.example/{candidate_id}",
            original_source_url=original_source_url,
            published_at=published_at,
            available_at=available_at,
            fetched_at="2025-03-31",
            full_text=text,
            content_hash=content_hash,
            content_type="text/plain",
            discovery_source_family=discovery_source_family,
            snippet="검색 snippet은 discovery에만 쓴다.",
            full_fetch_performed=full_fetch_performed,
            counts_as_live=counts_as_live,
            is_snapshot=is_snapshot,
            report_replay=report_replay,
            fake_provider=fake_provider,
            is_repost=is_repost,
            original_source_verified=original_source_verified,
            target_relation=target_relation,
            source_lineage_id=f"fixture:{candidate_id}",
            provider_error=provider_error,
        )

    def _connector(self, candidate, *, family=None, errors=(), fake_provider=True, log=None):
        family = family or candidate.source_family

        def batch(task, _mode, _budget):
            if log is not None:
                log.append(family)
            return ConnectorBatch(
                connector_name=f"connector:{family}",
                provider_name="fixture-source-provider",
                source_family=family,
                candidates=(candidate,) if candidate is not None else (),
                provider_errors=tuple(errors),
                usage=BudgetUsage(
                    queries=1,
                    candidates=1 if candidate is not None else 0,
                    fetches=(
                        1
                        if candidate is not None and candidate.full_fetch_performed
                        else 0
                    ),
                ),
                counts_as_live=bool(candidate and candidate.counts_as_live),
                snapshot_batch=bool(candidate and candidate.is_snapshot),
                fake_provider=fake_provider,
                discovery_only=family in {"NaverSearch", "TrustedNewsSearch"},
            )

        return StaticSourceConnector(
            connector_name=f"connector:{family}",
            provider_name="fixture-source-provider",
            source_family=family,
            batch_factory=batch,
            discovery_only=family in {"NaverSearch", "TrustedNewsSearch"},
            fake_provider=fake_provider,
        )

    def _engine(self, *connectors, test_mode=True):
        return SourceAcquisitionEngine(
            connectors=tuple(connectors),
            selector=self.selector,
            test_mode=test_mode,
        )

    def _naver_connector(self):
        query = self.task.query_intent.literal_queries[0]
        unresolved = SearchResult(
            title="테스트기업 네이버 재게시",
            url="https://n.news.naver.com/article/001/123",
            snippet="customer allocation summary",
            source="NaverSearch",
            published_at=datetime(2025, 3, 10, 8, 0),
            query=query,
            rank=1,
            is_news=True,
        )
        original_url = "https://trustednews.example/article-1"
        original = SearchResult(
            title="테스트기업 계약 조건 원문",
            url=original_url,
            snippet="supply agreement cancellation",
            source="NaverSearch",
            published_at=datetime(2025, 3, 11, 8, 0),
            query=query,
            rank=2,
            is_news=True,
        )
        return SearchFetchSourceConnector(
            connector_name="naver-search-full-fetch",
            provider_name="fixture-naver-provider",
            source_family="NaverSearch",
            fetched_source_family="TrustedNews",
            document_type="full_article",
            search_provider=FixtureSearchProvider(
                results_by_query={query: (unresolved, original)}
            ),
            page_fetcher=PageFetcher(
                fixture_text_by_url={original_url: self._text()}
            ),
            counts_as_live=False,
            fake_provider=True,
        )

    def test_controlled_smoke_selects_full_hashed_recipe_sections(self) -> None:
        candidate = self._candidate()
        result = self._engine(self._connector(candidate)).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(result.status, AcquisitionStatus.SELECTED.value)
        self.assertEqual(len(result.documents), 1)
        document = result.documents[0]
        self.assertEqual(document.task_id, self.task.task_id)
        self.assertEqual(document.recipe_id, self.task.recipe_id)
        self.assertTrue(document.content_hash)
        self.assertTrue(document.selected_sections)
        self.assertTrue(
            any(section.matched_recipe_sections for section in document.selected_sections)
        )
        self.assertFalse(document.snippet_used_as_document)
        self.assertTrue(document.controlled_smoke)
        self.assertFalse(document.runtime_score_eligible)

    def test_production_rejects_test_task_before_connector(self) -> None:
        result = self._engine().acquire(
            task=self.task,
            mode=AcquisitionMode.PRODUCTION_BOUNDED,
        )
        self.assertEqual(result.status, AcquisitionStatus.REJECTED_BY_POLICY.value)
        self.assertEqual(result.usage, BudgetUsage())

    def test_production_contract_and_source_repair_have_distinct_provenance(self) -> None:
        production_task = self._production_contract_task()
        live_candidate = self._candidate(
            task=production_task,
            candidate_id="LIVE-PRODUCTION",
            counts_as_live=True,
            fake_provider=False,
        )
        production = self._engine(
            self._connector(live_candidate, fake_provider=False),
            test_mode=False,
        ).acquire(
            task=production_task,
            mode=AcquisitionMode.PRODUCTION_BOUNDED,
        )
        self.assertEqual(production.status, AcquisitionStatus.SELECTED.value)
        self.assertTrue(production.documents[0].counts_as_live)
        self.assertFalse(production.documents[0].historical_replay)
        self.assertFalse(production.documents[0].source_repair_only)
        self.assertFalse(production.production_runtime_ready)

        repair_candidate = self._candidate(candidate_id="SOURCE-REPAIR")
        repair = self._engine(self._connector(repair_candidate)).acquire(
            task=self.task,
            mode=AcquisitionMode.SOURCE_REPAIR_BACKFILL,
        )
        self.assertEqual(repair.status, AcquisitionStatus.SELECTED.value)
        self.assertTrue(repair.documents[0].source_repair_only)
        self.assertFalse(repair.documents[0].runtime_score_eligible)

    def test_snapshot_and_report_replay_never_count_as_production_fetch(self) -> None:
        production_task = self._production_contract_task()
        snapshot = self._candidate(
            task=production_task,
            counts_as_live=False,
            is_snapshot=True,
            fake_provider=False,
        )
        snapshot_result = self._engine(
            self._connector(snapshot, fake_provider=False),
            test_mode=False,
        ).acquire(
            task=production_task,
            mode=AcquisitionMode.PRODUCTION_BOUNDED,
        )
        self.assertEqual(
            snapshot_result.rejections[0].reason,
            DocumentRejectionReason.SNAPSHOT_AS_LIVE.value,
        )

        production_report_task = self._with_research_report_route(production_task)
        report = self._candidate(
            task=production_report_task,
            candidate_id="REPORT-REPLAY",
            source_family="ResearchReport",
            document_type="research_report",
            counts_as_live=False,
            is_snapshot=True,
            report_replay=True,
            fake_provider=False,
            original_source_url="https://broker.example/report.pdf",
        )
        report_result = self._engine(
            self._connector(report, family="ResearchReport", fake_provider=False),
            test_mode=False,
        ).acquire(
            task=production_report_task,
            mode=AcquisitionMode.PRODUCTION_BOUNDED,
        )
        self.assertEqual(
            report_result.rejections[0].reason,
            DocumentRejectionReason.REPORT_REPLAY_NOT_REAL_FETCH.value,
        )

    def test_historical_replay_preserves_non_live_provenance(self) -> None:
        report_task = self._with_research_report_route()
        report = self._candidate(
            task=report_task,
            candidate_id="HIST-REPORT",
            source_family="ResearchReport",
            document_type="research_report",
            published_at="2024-10-01",
            available_at="2024-10-01",
            counts_as_live=False,
            is_snapshot=True,
            report_replay=True,
            original_source_url="https://broker.example/report.pdf",
        )
        result = self._engine(
            self._connector(report, family="ResearchReport")
        ).acquire(
            task=report_task,
            mode=AcquisitionMode.HISTORICAL_REPLAY,
        )
        self.assertEqual(result.status, AcquisitionStatus.SELECTED.value)
        self.assertTrue(result.documents[0].historical_replay)
        self.assertFalse(result.documents[0].counts_as_live)
        non_snapshot = self._candidate(
            candidate_id="HIST-NON-SNAPSHOT",
            counts_as_live=False,
            is_snapshot=False,
        )
        rejected = self._engine(self._connector(non_snapshot)).acquire(
            task=self.task,
            mode=AcquisitionMode.HISTORICAL_REPLAY,
        )
        self.assertEqual(
            rejected.rejections[0].reason,
            DocumentRejectionReason.NON_SNAPSHOT_IN_HISTORICAL_REPLAY.value,
        )

    def test_unknown_future_snippet_hash_and_wrong_subject_are_rejected(self) -> None:
        cases = {
            "UNKNOWN_DATE": self._candidate(
                candidate_id="UNKNOWN",
                published_at=None,
                available_at=None,
            ),
            "FUTURE_DATE": self._candidate(
                candidate_id="FUTURE",
                published_at="2025-04-01",
                available_at="2025-04-01",
            ),
            "SNIPPET_ONLY": self._candidate(
                candidate_id="SNIPPET",
                full_text="",
                content_hash=None,
                full_fetch_performed=False,
            ),
            "NO_CONTENT_HASH": self._candidate(
                candidate_id="NOHASH",
                content_hash=None,
            ),
            "CONTENT_HASH_MISMATCH": self._candidate(
                candidate_id="BADHASH",
                content_hash="0" * 64,
            ),
            "WRONG_SUBJECT": self._candidate(
                candidate_id="WRONG",
                full_text=self._text(target=False),
                target_relation="UNKNOWN",
            ),
        }
        for expected, candidate in cases.items():
            with self.subTest(expected=expected):
                result = self._engine(self._connector(candidate)).acquire(
                    task=self.task,
                    mode=AcquisitionMode.CONTROLLED_SMOKE,
                )
                self.assertFalse(result.documents)
                self.assertEqual(result.rejections[0].reason, expected)

    def test_source_class_document_mismatch_and_stale_report_are_rejected(self) -> None:
        mismatch = self._candidate(
            candidate_id="MISMATCH",
            source_family="DART",
            document_type="full_article",
        )
        mismatch_result = self._engine(self._connector(mismatch)).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(
            mismatch_result.rejections[0].reason,
            DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH.value,
        )
        report_task = self._with_research_report_route()
        stale = self._candidate(
            task=report_task,
            candidate_id="STALE",
            source_family="ResearchReport",
            document_type="research_report",
            published_at="2020-01-01",
            available_at="2020-01-01",
            original_source_url="https://broker.example/stale.pdf",
        )
        stale_result = self._engine(
            self._connector(stale, family="ResearchReport")
        ).acquire(
            task=report_task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(
            stale_result.rejections[0].reason,
            DocumentRejectionReason.STALE_DOCUMENT.value,
        )

    def test_task_recipe_document_contract_cannot_be_bypassed(self) -> None:
        narrowed_document_route = replace(
            self.task.source_route,
            preferred_document_types=("full_article",),
        )
        narrowed_document_task = replace(
            self.task,
            task_id=f"{self.task.task_id}:full-article-only",
            source_route=narrowed_document_route,
        )
        filing = self._candidate(
            task=narrowed_document_task,
            candidate_id="TASK-DOC-MISMATCH",
        )
        document_result = self._engine(self._connector(filing)).acquire(
            task=narrowed_document_task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(
            document_result.rejections[0].reason,
            DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH.value,
        )

        narrowed_section_route = replace(
            self.task.source_route,
            preferred_sections=("unrelated task-only section",),
        )
        narrowed_section_task = replace(
            self.task,
            task_id=f"{self.task.task_id}:unlinked-section",
            source_route=narrowed_section_route,
        )
        section_candidate = self._candidate(
            task=narrowed_section_task,
            candidate_id="TASK-SECTION-MISMATCH",
        )
        section_result = self._engine(self._connector(section_candidate)).acquire(
            task=narrowed_section_task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(
            section_result.rejections[0].reason,
            DocumentRejectionReason.TASK_RECIPE_LINK_MISMATCH.value,
        )

        discovery_as_document = self._candidate(
            candidate_id="SEARCH-AS-DOCUMENT-SOURCE",
            source_family="NaverSearch",
            document_type="full_article",
            discovery_source_family="NaverSearch",
            original_source_url="https://trustednews.example/original",
        )
        discovery_result = self._engine(
            self._connector(discovery_as_document, family="NaverSearch")
        ).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(
            discovery_result.rejections[0].reason,
            DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH.value,
        )

    def test_provider_failure_is_not_masked(self) -> None:
        connector = self._connector(
            None,
            family="DART",
            errors=("official provider timeout",),
        )
        result = self._engine(connector).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(result.status, AcquisitionStatus.PROVIDER_FAILED.value)
        self.assertIn("official provider timeout", result.provider_errors)

    def test_connector_budget_violation_cannot_select_a_document(self) -> None:
        candidate = self._candidate(candidate_id="OVER-BUDGET")

        def batch(_task, _mode, remaining):
            return ConnectorBatch(
                connector_name="over-budget-connector",
                provider_name="fixture-source-provider",
                source_family="DART",
                candidates=(candidate,),
                provider_errors=(),
                usage=BudgetUsage(
                    queries=remaining.max_queries + 1,
                    candidates=1,
                    fetches=1,
                ),
                counts_as_live=False,
                snapshot_batch=False,
                fake_provider=True,
            )

        connector = StaticSourceConnector(
            connector_name="over-budget-connector",
            provider_name="fixture-source-provider",
            source_family="DART",
            batch_factory=batch,
        )
        result = self._engine(connector).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertFalse(result.documents)
        self.assertEqual(result.status, AcquisitionStatus.PROVIDER_FAILED.value)
        self.assertEqual(
            result.rejections[0].reason,
            DocumentRejectionReason.OUTSIDE_BUDGET.value,
        )
        self.assertFalse(result.budget_within_task)

    def test_naver_discovery_requires_original_full_fetch_or_rejection(self) -> None:
        result = self._engine(self._naver_connector()).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(len(result.documents), 1)
        self.assertEqual(len(result.rejections), 1)
        self.assertEqual(
            result.rejections[0].reason,
            DocumentRejectionReason.REPOST_WITHOUT_ORIGINAL.value,
        )
        self.assertEqual(
            result.documents[0].discovery_source_family,
            "NaverSearch",
        )
        self.assertEqual(
            result.documents[0].original_source_url,
            "https://trustednews.example/article-1",
        )
        self.assertFalse(result.documents[0].snippet_used_as_document)
        self.assertTrue(result.official_attempted_before_discovery)

    def test_discovery_runs_after_official_gap_but_not_after_selected_official(self) -> None:
        log = []
        no_official = self._connector(None, family="DART", log=log)
        discovery_candidate = self._candidate(
            candidate_id="DISCOVERY",
            source_family="TrustedNews",
            document_type="full_article",
            discovery_source_family="NaverSearch",
            original_source_url="https://trustednews.example/discovery",
        )
        discovery = self._connector(
            discovery_candidate,
            family="NaverSearch",
            log=log,
        )
        result = self._engine(no_official, discovery).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertLess(log.index("DART"), log.index("NaverSearch"))
        self.assertTrue(any("NO_CANDIDATES:DART" in gap for gap in result.source_gaps))

        second_log = []
        official = self._connector(
            self._candidate(candidate_id="OFFICIAL"),
            family="DART",
            log=second_log,
        )
        unused_discovery = self._connector(
            discovery_candidate,
            family="NaverSearch",
            log=second_log,
        )
        selected = self._engine(official, unused_discovery).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertTrue(selected.documents)
        self.assertNotIn("NaverSearch", second_log)

    def test_discovery_candidate_cannot_masquerade_as_direct_official(self) -> None:
        masquerading = self._candidate(
            candidate_id="DISCOVERY-AS-DART",
            source_family="TrustedNews",
            document_type="full_article",
            discovery_source_family="NaverSearch",
            original_source_url="https://trustednews.example/masquerading",
        )
        connector = self._connector(masquerading, family="DART")
        result = self._engine(connector).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertFalse(result.documents)
        self.assertEqual(
            result.rejections[0].reason,
            DocumentRejectionReason.SOURCE_CLASS_DOCUMENT_MISMATCH.value,
        )

    def test_naver_connector_misconfigured_as_main_route_is_never_run(self) -> None:
        route = replace(
            self.task.source_route,
            fallback_source_families=tuple(
                dict.fromkeys(
                    (*self.task.source_route.fallback_source_families, "NaverSearch")
                )
            ),
        )
        task = replace(
            self.task,
            task_id=f"{self.task.task_id}:misconfigured-naver",
            source_route=route,
        )
        calls = []

        def batch(_task, _mode, _budget):
            calls.append("NaverSearch")
            return ConnectorBatch(
                connector_name="misconfigured-naver-main",
                provider_name="fixture-source-provider",
                source_family="NaverSearch",
                candidates=(),
                provider_errors=(),
                usage=BudgetUsage(),
                counts_as_live=False,
                snapshot_batch=False,
                fake_provider=True,
                discovery_only=False,
            )

        connector = StaticSourceConnector(
            connector_name="misconfigured-naver-main",
            provider_name="fixture-source-provider",
            source_family="NaverSearch",
            batch_factory=batch,
            discovery_only=False,
            fake_provider=True,
        )
        result = self._engine(connector).acquire(
            task=task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(calls, [])
        self.assertTrue(
            any(
                gap == "DISCOVERY_ONLY_SOURCE_SKIPPED:NaverSearch"
                for gap in result.source_gaps
            )
        )

    def test_v4_snapshot_adapter_preserves_replay_provenance(self) -> None:
        text = self._text()
        document = EvidenceDocument.from_text(
            text=text,
            canonical_url="https://broker.example/replay.pdf",
            source_type=SourceType.RESEARCH_REPORT,
            source_name="stored report",
            published_at=datetime(2024, 10, 1, 8, 0),
            available_at=datetime(2024, 10, 1, 8, 0),
            fetched_at=datetime(2025, 3, 31, 8, 0),
            parser_version="research_brain_v4_real_source_snapshot",
            source_lineage_id="snapshot:report-1",
        )
        v4 = SourceAcquisitionResultV4(
            task_id="legacy-task",
            source_class="ResearchReport",
            provider_name="stored_real_source_snapshot_provider",
            status="PARSED",
            documents=(document,),
            document_text_by_id={document.document_id: text},
            fetched_document_ids=(document.document_id,),
            document_hashes=(document.content_hash,),
            budget_used={"queries": 1, "candidates": 1, "fetches": 1},
        )
        report_task = self._with_research_report_route()
        batch = adapt_v4_source_acquisition_result(
            result=v4,
            task=report_task,
            mode=AcquisitionMode.HISTORICAL_REPLAY,
        )
        self.assertTrue(batch.snapshot_batch)
        self.assertFalse(batch.counts_as_live)
        self.assertTrue(batch.candidates[0].report_replay)
        connector = StaticSourceConnector(
            connector_name=batch.connector_name,
            provider_name=batch.provider_name,
            source_family=batch.source_family,
            batch_factory=lambda _task, _mode, _budget: batch,
            fake_provider=False,
        )
        result = self._engine(connector).acquire(
            task=report_task,
            mode=AcquisitionMode.HISTORICAL_REPLAY,
        )
        self.assertEqual(result.status, AcquisitionStatus.SELECTED.value)
        self.assertFalse(result.documents[0].counts_as_live)

    def test_v4_as_of_date_fallback_is_restored_to_unknown_and_rejected(self) -> None:
        text = self._text()
        document = EvidenceDocument.from_text(
            text=text,
            canonical_url="https://dart.example/undated-live-document",
            source_type=SourceType.FILING,
            source_name="undated live document",
            published_at=datetime(2025, 3, 31, 8, 0),
            available_at=datetime(2025, 3, 31, 8, 0),
            fetched_at=datetime(2025, 3, 31, 8, 0),
            parser_version="research_brain_v4_live_official",
            source_lineage_id="live:undated-document",
            score_block_reasons=(
                "published_at_unknown_not_source_backed",
                "available_at_unknown_not_source_backed",
            ),
        )
        v4 = SourceAcquisitionResultV4(
            task_id="legacy-task",
            source_class="DART",
            provider_name="live_official_provider",
            status="PARSED",
            documents=(document,),
            document_text_by_id={document.document_id: text},
            fetched_document_ids=(document.document_id,),
            document_hashes=(document.content_hash,),
            budget_used={"queries": 1, "candidates": 1, "fetches": 1},
        )
        batch = adapt_v4_source_acquisition_result(
            result=v4,
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertIsNone(batch.candidates[0].published_at)
        self.assertIsNone(batch.candidates[0].available_at)
        connector = StaticSourceConnector(
            connector_name=batch.connector_name,
            provider_name=batch.provider_name,
            source_family=batch.source_family,
            batch_factory=lambda _task, _mode, _budget: batch,
            fake_provider=False,
        )
        result = self._engine(connector).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        self.assertEqual(
            result.rejections[0].reason,
            DocumentRejectionReason.UNKNOWN_DATE.value,
        )

    def test_acquisition_audit_has_zero_hard_safety_violations(self) -> None:
        controlled = self._engine(
            self._connector(self._candidate(candidate_id="AUDIT-CONTROLLED"))
        ).acquire(task=self.task, mode=AcquisitionMode.CONTROLLED_SMOKE)
        report_task = self._with_research_report_route()
        historical_candidate = self._candidate(
            task=report_task,
            candidate_id="AUDIT-HISTORICAL",
            source_family="ResearchReport",
            document_type="research_report",
            published_at="2024-10-01",
            available_at="2024-10-01",
            is_snapshot=True,
            report_replay=True,
            original_source_url="https://broker.example/audit.pdf",
        )
        historical = self._engine(
            self._connector(historical_candidate, family="ResearchReport")
        ).acquire(task=report_task, mode=AcquisitionMode.HISTORICAL_REPLAY)
        provider_failed = self._engine(
            self._connector(None, family="DART", errors=("timeout",))
        ).acquire(task=self.task, mode=AcquisitionMode.CONTROLLED_SMOKE)
        naver = self._engine(self._naver_connector()).acquire(
            task=self.task,
            mode=AcquisitionMode.CONTROLLED_SMOKE,
        )
        audit = audit_acquisition_results(
            (controlled, historical, provider_failed, naver)
        )
        self.assertEqual(audit["status"], "SOURCE_ACQUISITION_CONTRACT_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(audit["naver_terminal_candidate_count"], 2)
        self.assertEqual(
            audit["result_hash"],
            "cebcdea9ed8b1d0df34f5b30818ac6eeef2c4543ab921a59ebf3315e83d5b1bc",
        )
        self.assertFalse(audit["production_runtime_ready"])


if __name__ == "__main__":
    unittest.main()
