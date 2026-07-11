from __future__ import annotations

import hashlib
import json
import unittest
from datetime import date, datetime
from pathlib import Path

from e2r.production.source_connectors.source_provider_registry import (
    SourceFetchResult,
    SourceProviderRegistry,
)
from e2r.research.page_fetcher import FetchResult, PageFetcher
from e2r.research.search_provider import SearchResult
from e2r.research_brain.runtime.live_materialization import (
    AcquisitionResultClass,
    CurrentSourceAcquisitionOrchestrator,
    SourceAcquisitionConfig,
)


class LiveSourceAcquisitionOrchestratorTest(unittest.TestCase):
    def test_live_operational_audit_records_real_full_documents(self) -> None:
        path = (
            Path(__file__).resolve().parents[1]
            / "docs"
            / "operational"
            / "e2r_live_source_acquisition_audit.json"
        )
        audit = json.loads(path.read_text(encoding="utf-8"))

        self.assertEqual(audit["status"], "PHASE_27_ACCEPTED")
        self.assertGreater(audit["actual_live_or_fresh_document_count"], 0)
        self.assertGreater(audit["unique_evidence_document_count"], 0)
        self.assertEqual(sum(audit["critical_counts"].values()), 0)
        self.assertFalse(audit["safety"]["provider_error_body_materialized"])
        self.assertFalse(audit["safety"]["search_snippet_materialized"])

    def test_same_target_provider_fetch_is_reused_as_fresh_cache(self) -> None:
        connector = _FetchedDartConnector()
        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=2,
                test_mode=True,
            ),
            source_tasks=(_daily_task("Q-1"), _daily_task("Q-2")),
            question_source_tasks=(_question_task("Q-1"), _question_task("Q-2")),
            provider_registry=SourceProviderRegistry((connector,)),
        )

        self.assertEqual(result.status, "CURRENT_SOURCE_ACQUISITION_PASS")
        self.assertEqual(connector.calls, 1)
        self.assertEqual(len(result.evidence_documents), 1)
        self.assertEqual(
            result.evidence_documents[0].source_task_ids,
            ("Q-1", "Q-2"),
        )
        self.assertEqual(
            [item.acquisition_class for item in result.provider_fetch_results],
            [
                AcquisitionResultClass.REAL_PROVIDER_FETCH.value,
                AcquisitionResultClass.FRESH_PROVIDER_CACHE.value,
            ],
        )
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_generic_portal_is_health_only_and_never_document(self) -> None:
        task = _question_task("Q-KRX", source="KRX")
        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=1,
                test_mode=True,
            ),
            source_tasks=(_daily_task("Q-KRX", source="KRX"),),
            question_source_tasks=(task,),
            provider_registry=SourceProviderRegistry((_GenericKrxConnector(),)),
        )

        self.assertFalse(result.evidence_documents)
        self.assertEqual(
            result.provider_fetch_results[0].acquisition_class,
            AcquisitionResultClass.PROVIDER_HEALTH_ONLY.value,
        )
        self.assertEqual(
            result.audit["critical_counts"]["generic_portal_counted_as_symbol_evidence"],
            0,
        )

    def test_provider_failure_is_not_masked_as_no_result(self) -> None:
        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=1,
                test_mode=True,
            ),
            source_tasks=(_daily_task("Q-FAIL"),),
            question_source_tasks=(_question_task("Q-FAIL"),),
            provider_registry=SourceProviderRegistry((_FailedDartConnector(),)),
        )

        self.assertEqual(
            result.provider_fetch_results[0].acquisition_class,
            AcquisitionResultClass.PROVIDER_FAILED.value,
        )
        self.assertEqual(
            result.audit["critical_counts"]["provider_failure_masked_no_result"],
            0,
        )

    def test_provider_error_body_is_not_materialized_as_document(self) -> None:
        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=1,
                test_mode=True,
            ),
            source_tasks=(_daily_task("Q-ERROR-BODY"),),
            question_source_tasks=(_question_task("Q-ERROR-BODY"),),
            provider_registry=SourceProviderRegistry((_ErrorBodyDartConnector(),)),
        )

        self.assertFalse(result.evidence_documents)
        self.assertEqual(
            result.provider_fetch_results[0].acquisition_class,
            AcquisitionResultClass.REJECTED_BY_POLICY.value,
        )
        self.assertEqual(
            result.provider_fetch_results[0].policy_rejection_reason,
            "fetched_document_content_too_small",
        )

    def test_allowed_web_fallback_forwards_llm_query_after_official_gap(self) -> None:
        events: list[str] = []
        first_query = "테스트회사 2026년 1분기 계약 취소 조건 원문"
        second_query = "테스트회사 2025년 사업보고서 계약 잔액 원문"
        url = "https://news.example.test/test-company-contract"
        search = _RecordingSearchProvider(
            events,
            {
                first_query: (
                    SearchResult(
                        title="테스트회사 계약 조건 보도",
                        url=url,
                        snippet="검색 snippet은 발견용일 뿐이다.",
                        source="Naver Search",
                        published_at=datetime(2026, 7, 9, 9, 0),
                        query=first_query,
                        rank=1,
                        is_news=True,
                    ),
                ),
                second_query: (),
            },
        )
        full_text = (
            "테스트회사는 2026년 1분기 고객 계약의 취소 조건과 계약 잔액을 "
            "공식 원문에서 설명했다. 검색 결과의 짧은 요약이 아니라 실제 기사 "
            "본문 전체를 PageFetcher로 수집해 대상 회사, 날짜, 계약 범위를 확인한다."
        )
        fetcher = _RecordingPageFetcher(
            events,
            PageFetcher(fixture_text_by_url={url: full_text}),
        )
        connector = _OrderedFailedDartConnector(events)

        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=1,
                test_mode=True,
            ),
            source_tasks=(
                _daily_task(
                    "Q-WEB",
                    allow_web=True,
                    queries=(first_query, second_query),
                    max_queries=2,
                ),
            ),
            question_source_tasks=(
                _question_task(
                    "Q-WEB",
                    queries=(first_query, second_query),
                    max_queries=2,
                ),
            ),
            provider_registry=SourceProviderRegistry((connector,)),
            web_search_provider=search,
            page_fetcher=fetcher,
        )

        self.assertEqual(
            events,
            ["official", f"search:{first_query}", f"fetch:{url}"],
        )
        self.assertEqual(search.queries, [first_query])
        self.assertEqual(result.web_search_tasks[0]["query"], first_query)
        self.assertTrue(result.web_search_tasks[0]["query_forwarded_verbatim"])
        self.assertTrue(result.web_search_tasks[0]["official_request_record_ids"])
        self.assertTrue(result.web_search_tasks[0]["official_gap_reasons"])
        self.assertEqual(len(result.web_fetched_documents), 1)
        self.assertEqual(len(result.evidence_documents), 1)
        self.assertEqual(result.evidence_documents[0].source_task_ids, ("Q-WEB",))
        self.assertFalse(result.evidence_documents[0].snippet_only)
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_web_fallback_is_blocked_when_task_does_not_allow_it(self) -> None:
        events: list[str] = []
        query = "테스트회사 2026년 1분기 공식 원문"
        search = _RecordingSearchProvider(events, {query: ()})

        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=1,
                test_mode=True,
            ),
            source_tasks=(_daily_task("Q-NO-WEB", queries=(query,)),),
            question_source_tasks=(_question_task("Q-NO-WEB", queries=(query,)),),
            provider_registry=SourceProviderRegistry((_OrderedFailedDartConnector(events),)),
            web_search_provider=search,
            page_fetcher=PageFetcher(),
        )

        self.assertEqual(events, ["official"])
        self.assertFalse(search.queries)
        self.assertFalse(result.web_search_tasks)
        self.assertFalse(result.web_search_results)

    def test_future_and_snippet_only_web_results_are_rejected(self) -> None:
        events: list[str] = []
        query = "테스트회사 2026년 1분기 계약 원문"
        future_url = "https://news.example.test/future"
        snippet_url = "https://news.example.test/snippet-only"
        search = _RecordingSearchProvider(
            events,
            {
                query: (
                    SearchResult(
                        title="테스트회사 미래 기사",
                        url=future_url,
                        snippet="미래 기사 snippet",
                        published_at=datetime(2026, 7, 11, 8, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                    SearchResult(
                        title="테스트회사 현재 기사",
                        url=snippet_url,
                        snippet="이 snippet만으로는 증거가 될 수 없다.",
                        published_at=datetime(2026, 7, 9, 8, 0),
                        query=query,
                        rank=2,
                        is_news=True,
                    ),
                )
            },
        )
        fetcher = _RecordingPageFetcher(events, PageFetcher())

        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=1,
                test_mode=True,
            ),
            source_tasks=(
                _daily_task("Q-SAFE-WEB", allow_web=True, queries=(query,)),
            ),
            question_source_tasks=(
                _question_task("Q-SAFE-WEB", queries=(query,)),
            ),
            provider_registry=SourceProviderRegistry((_OrderedFailedDartConnector(events),)),
            web_search_provider=search,
            page_fetcher=fetcher,
        )

        self.assertNotIn(f"fetch:{future_url}", events)
        self.assertIn(f"fetch:{snippet_url}", events)
        self.assertFalse(result.web_fetched_documents)
        self.assertFalse(result.evidence_documents)
        reasons = {item["rejection_reason"] for item in result.web_rejected_documents}
        self.assertIn("FUTURE_DOCUMENT", reasons)
        self.assertIn("SNIPPET_ONLY_FULL_FETCH_REQUIRED", reasons)
        self.assertEqual(result.audit["critical_counts"]["web_future_document_accepted"], 0)
        self.assertEqual(result.audit["critical_counts"]["snippet_document"], 0)

    def test_production_web_fallback_rejects_fixture_search_provider(self) -> None:
        events: list[str] = []
        query = "테스트회사 2026년 1분기 계약 원문"
        question = _question_task("Q-PROD-WEB", queries=(query,))
        question["production_execution_allowed"] = True
        question["query_intent"]["generator_kind"] = "REAL_LLM"

        with self.assertRaisesRegex(ValueError, "live NaverFreeSearchProvider"):
            CurrentSourceAcquisitionOrchestrator().acquire(
                SourceAcquisitionConfig(
                    as_of_date="2026-07-10",
                    max_tasks=1,
                    test_mode=False,
                ),
                source_tasks=(
                    _daily_task("Q-PROD-WEB", allow_web=True, queries=(query,)),
                ),
                question_source_tasks=(question,),
                provider_registry=SourceProviderRegistry(
                    (_OrderedFailedDartConnector(events),)
                ),
                web_search_provider=_RecordingSearchProvider(events, {query: ()}),
                page_fetcher=PageFetcher(live_enabled=True),
            )


class _FetchedDartConnector:
    provider_name = "OpenDART"
    source_class = "DART"

    def __init__(self) -> None:
        self.calls = 0

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str):
        self.calls += 1
        text = (
            f"{company_name}({symbol}) 2026년 1분기 공식 사업보고 원문. "
            "계약 기간, 계약 금액, 현금흐름, 취소 조건과 최신 정정 여부를 "
            "회사 직접 공시의 본문과 표에서 확인할 수 있다."
        )
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"REQ-{symbol}",
            request_params={"symbol": symbol},
            status="FETCHED",
            canonical_url=f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={symbol}",
            official_document_id=f"opendart:disclosure:{symbol}",
            published_at="2026-05-15",
            available_at="2026-05-15",
            fetched_at="2026-07-10T09:00:00Z",
            content_hash=hashlib.sha256(text.encode("utf-8")).hexdigest(),
            raw_text=text,
            structured_payload={"symbol": symbol, "detail_fetched": True},
            provider_request_id=f"REQ-{symbol}",
        )


class _FailedDartConnector:
    provider_name = "OpenDART"
    source_class = "DART"

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str):
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"REQ-{symbol}",
            request_params={"symbol": symbol},
            status="PROVIDER_FAILED",
            fetched_at="2026-07-10T09:00:00Z",
            provider_error="provider unavailable",
            provider_request_id=f"REQ-{symbol}",
        )


class _ErrorBodyDartConnector:
    provider_name = "OpenDART"
    source_class = "DART"

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str):
        text = "014 파일이 존재하지 않습니다."
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"REQ-{symbol}",
            request_params={"symbol": symbol},
            status="FETCHED",
            canonical_url=f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={symbol}",
            official_document_id=f"opendart:disclosure:{symbol}",
            published_at="2026-05-15",
            available_at="2026-05-15",
            fetched_at="2026-07-10T09:00:00Z",
            content_hash=hashlib.sha256(text.encode("utf-8")).hexdigest(),
            raw_text=text,
            structured_payload={"symbol": symbol},
            provider_request_id=f"REQ-{symbol}",
        )


class _GenericKrxConnector:
    provider_name = "KRX"
    source_class = "KRX"

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str):
        text = "KRX Market Data Center generic portal"
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"REQ-{symbol}",
            request_params={"symbol": symbol},
            status="FETCHED",
            canonical_url="https://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd",
            official_document_id="krx:mdc:main",
            published_at="2026-07-10",
            available_at="2026-07-10",
            fetched_at="2026-07-10T09:00:00Z",
            content_hash=hashlib.sha256(text.encode("utf-8")).hexdigest(),
            raw_text=text,
            structured_payload={
                "score_usage": "provider_coverage_only_until_symbol_risk_endpoint_is_available"
            },
            provider_request_id=f"REQ-{symbol}",
        )


class _OrderedFailedDartConnector(_FailedDartConnector):
    def __init__(self, events: list[str]) -> None:
        self.events = events

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str):
        self.events.append("official")
        return super().fetch(
            symbol=symbol,
            company_name=company_name,
            as_of_date=as_of_date,
            mode=mode,
        )


class _RecordingSearchProvider:
    def __init__(
        self,
        events: list[str],
        results_by_query: dict[str, tuple[SearchResult, ...]],
    ) -> None:
        self.events = events
        self.results_by_query = results_by_query
        self.queries: list[str] = []
        self.max_results: list[int] = []

    def search(self, query: str, as_of_date: date, max_results: int = 100):
        del as_of_date
        self.events.append(f"search:{query}")
        self.queries.append(query)
        self.max_results.append(max_results)
        return self.results_by_query.get(query, ())[:max_results]


class _RecordingPageFetcher:
    def __init__(self, events: list[str], base: PageFetcher) -> None:
        self.events = events
        self.base = base

    def fetch(self, url: str, *, as_of_date: date) -> FetchResult:
        self.events.append(f"fetch:{url}")
        return self.base.fetch(url, as_of_date=as_of_date)


def _question_task(
    task_id: str,
    *,
    source: str = "DART",
    queries: tuple[str, ...] = ("테스트회사 2026년 1분기 공식 공시",),
    max_queries: int = 1,
) -> dict:
    return {
        "task_id": task_id,
        "candidate_event_id": f"CAND-{task_id}",
        "target_id": "000001",
        "symbol": "000001",
        "company_name": "테스트회사",
        "as_of_date": "2026-07-10",
        "runtime_score_eligible": False,
        "production_execution_allowed": False,
        "source_route": {
            "preferred_source_families": [source],
            "fallback_source_families": ["TrustedNews"],
        },
        "budget": {"max_queries": max_queries, "max_candidates": 8, "max_fetches": 4},
        "query_intent": {
            "literal_queries": list(queries),
            "generator_kind": "TEST_FIXTURE_LLM",
            "provider_name": "fixture_question_query_provider",
            "prompt_hash": "a" * 64,
            "response_hash": "b" * 64,
        },
        "stop_condition": {"stop_on_resolution": True},
    }


def _daily_task(
    question_task_id: str,
    *,
    source: str = "DART",
    allow_web: bool = False,
    queries: tuple[str, ...] = ("테스트회사 2026년 1분기 공식 공시",),
    max_queries: int = 1,
) -> dict:
    return {
        "task_id": f"DAILY-{question_task_id}",
        "question_task_id": question_task_id,
        "target_id": "000001",
        "source_class": source,
        "max_queries": max_queries,
        "max_candidates": 8,
        "max_fetches": 4,
        "max_retries": 2,
        "literal_queries": list(queries),
        "allows_general_web": allow_web,
        "official_first_attempted": allow_web,
        "official_gap_reasons": (["official source remained unresolved"] if allow_web else []),
        "stop_condition": "stop_on_resolution",
    }


if __name__ == "__main__":
    unittest.main()
