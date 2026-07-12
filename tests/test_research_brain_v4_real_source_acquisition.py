import unittest
import io
import hashlib
import json
import zipfile
from dataclasses import replace
from datetime import date, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from e2r.production.source_connectors.companyguide_live_connector import CompanyGuideLiveConnector
from e2r.production.source_connectors.opendart_live_connector import OpenDARTLiveConnector
from e2r.production.source_connectors.source_provider_registry import SourceFetchResult, SourceProviderRegistry
from e2r.research.page_fetcher import PageFetcher
from e2r.research.search_provider import FixtureSearchProvider, SearchResult, normalize_search_result
from e2r.research_brain.v4_production_orchestrator import build_source_acquisition_report_v4
from e2r.research_brain.v4_schemas import SourceTaskExecutionV4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from tests.research_brain_v4_test_helpers import c06_source_task, research_brain_v4_fixture_root, sample_v4_event


class ResearchBrainV4RealSourceAcquisitionTests(unittest.TestCase):
    def test_companyguide_snapshot_fetches_real_document_and_anchor(self):
        result = SourceAcquisitionRunnerV4(
            mode="frozen_real_source_snapshot",
            repo_root=research_brain_v4_fixture_root(),
        ).acquire(
            event=sample_v4_event(),
            task=c06_source_task(),
            as_of_date=date(2026, 6, 29),
        )
        self.assertEqual(result.status, "PARSED")
        self.assertGreaterEqual(len(result.fetched_document_ids), 1)
        self.assertEqual(len(result.fetched_document_ids), len(result.anchor_ids))
        self.assertTrue(all(url.startswith("snapshot://company_guide/") for url in result.document_urls))
        self.assertNotIn(sample_v4_event().event_summary, result.document_text_by_id.values())

    def test_live_official_mode_uses_connector_document_not_snapshot_fallback(self):
        event = sample_v4_event()
        task = c06_source_task()
        registry = SourceProviderRegistry(
            connectors=(
                _LiveOfficialFixtureConnector(),
            )
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_official_only",
            source_provider_registry=registry,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(len(result.fetched_document_ids), 1)
        self.assertEqual(result.document_urls, ("https://example.com/companyguide/A005930",))
        self.assertFalse(any(url.startswith("snapshot://") for url in result.document_urls))
        self.assertIn("목표주가 상향", next(iter(result.document_text_by_id.values())))

    def test_live_official_respects_task_source_order_before_registry_order(self):
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        calls: list[str] = []
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            preferred_source_classes=("IssuerIR", "CompanyGuide"),
            fallback_source_classes=("DART",),
            max_queries=3,
            max_candidates=3,
            max_fetches=1,
        )
        registry = SourceProviderRegistry(
            connectors=(
                _RecordingLiveConnector(
                    provider_name="OpenDART",
                    source_class="DART",
                    url="https://dart.fss.or.kr/dsaf001/main.do?rcpNo=NOISE",
                    raw_text="SK하이닉스(000660) 유상증자 결정",
                    calls=calls,
                ),
                _RecordingLiveConnector(
                    provider_name="CompanyGuide",
                    source_class="CompanyGuide",
                    url="https://wcomp.fnguide.com/company/000660",
                    raw_text="SK하이닉스(000660) HBM 매출 전망과 EPS 상향",
                    calls=calls,
                ),
                _RecordingLiveConnector(
                    provider_name="IssuerIR",
                    source_class="IR",
                    url="https://www.skhynix.com/ir",
                    raw_text="",
                    calls=calls,
                    status="PROVIDER_FAILED",
                    provider_error="issuer_ir_not_found",
                ),
            )
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_official_only",
            source_provider_registry=registry,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(calls, ["IssuerIR", "CompanyGuide"])
        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.document_urls, ("https://wcomp.fnguide.com/company/000660",))
        self.assertEqual(result.source_class, "CompanyGuide")
        self.assertNotIn("OpenDART", calls)
        self.assertEqual(result.budget_used["queries"], 2)

    def test_live_official_respects_task_query_budget_before_connector_count(self):
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        calls: list[str] = []
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            preferred_source_classes=("DART",),
            fallback_source_classes=(),
            max_queries=2,
            max_candidates=5,
            max_fetches=1,
        )
        registry = SourceProviderRegistry(
            connectors=(
                _RecordingLiveConnector(
                    provider_name="OpenDART-A",
                    source_class="DART",
                    url="https://dart.fss.or.kr/dsaf001/main.do?rcpNo=NOISEA",
                    raw_text="",
                    calls=calls,
                    status="PROVIDER_FAILED",
                    provider_error="dart_a_not_found",
                ),
                _RecordingLiveConnector(
                    provider_name="OpenDART-B",
                    source_class="DART",
                    url="https://dart.fss.or.kr/dsaf001/main.do?rcpNo=NOISEB",
                    raw_text="",
                    calls=calls,
                    status="PROVIDER_FAILED",
                    provider_error="dart_b_not_found",
                ),
                _RecordingLiveConnector(
                    provider_name="OpenDART-C",
                    source_class="DART",
                    url="https://dart.fss.or.kr/dsaf001/main.do?rcpNo=SHOULD_NOT_CALL",
                    raw_text="SK하이닉스(000660) HBM 매출 전망과 EPS 상향",
                    calls=calls,
                ),
            )
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_official_only",
            source_provider_registry=registry,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(calls, ["OpenDART-A", "OpenDART-B"])
        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.budget_used["queries"], 2)
        self.assertLessEqual(result.budget_used["queries"], task.max_queries)
        self.assertEqual(result.fetched_document_ids, ())

    def test_live_official_document_counts_as_real_non_snapshot_document(self):
        event = sample_v4_event()
        task = c06_source_task()
        registry = SourceProviderRegistry(connectors=(_LiveOfficialFixtureConnector(),))
        result = SourceAcquisitionRunnerV4(
            mode="live_official_only",
            source_provider_registry=registry,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))
        execution = SourceTaskExecutionV4(
            task_id=task.task_id,
            source_task=task.to_dict(),
            status="NO_EVIDENCE_FOUND",
            fetched_document_ids=tuple(result.fetched_document_ids),
            document_urls=tuple(result.document_urls),
            document_hashes=tuple(result.document_hashes),
            evidence_anchor_ids=tuple(result.anchor_ids),
            budget_used=dict(result.budget_used),
            stop_reason=result.stop_reason,
        )

        report = build_source_acquisition_report_v4((execution,))
        summary = report["summary"]
        self.assertEqual(summary["fetched_document_count"], 1)
        self.assertEqual(summary["snapshot_document_fetched_count"], 0)
        self.assertEqual(summary["real_document_fetched_count"], 1)
        self.assertEqual(summary["unique_real_document_fetched_count"], 1)
        self.assertEqual(summary["real_document_count_semantics"], "live_non_snapshot_document_only")

    def test_live_official_score_usage_becomes_document_score_block_reason(self):
        event = sample_v4_event()
        task = c06_source_task()
        registry = SourceProviderRegistry(connectors=(_ScoreBlockedLiveConnector(),))

        result = SourceAcquisitionRunnerV4(
            mode="live_official_only",
            source_provider_registry=registry,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(len(result.documents), 1)
        self.assertEqual(
            result.documents[0].score_block_reasons,
            ("provider_coverage_only_until_numeric_revision_parser_accepts_claims",),
        )

    def test_companyguide_live_connector_extracts_consensus_numeric_anchor(self):
        html = _companyguide_consensus_html()

        with patch(
            "e2r.production.source_connectors.companyguide_live_connector._fetch_companyguide_main",
            return_value=(html, hashlib.sha256(html.encode("utf-8")).hexdigest(), "https://wcomp.fnguide.com"),
        ):
            result = CompanyGuideLiveConnector(repo_root=".").fetch(
                symbol="000660",
                company_name="SK하이닉스",
                as_of_date=date(2026, 7, 1),
                mode="live",
            )

        self.assertEqual(result.status, "FETCHED")
        self.assertEqual(result.published_at, "2026-07-01")
        self.assertNotIn("score_usage", result.structured_payload)
        self.assertEqual(result.structured_payload["CONSENSUS_AS_OF_DATE"], "2026/07/01")
        self.assertEqual(result.structured_payload["TARGET_PRC"], 501458)
        self.assertEqual(result.structured_payload["EPS"], 45534)
        self.assertEqual(result.structured_payload["CONSENSUS_PROVIDER_COUNT"], 24)
        self.assertIn("투자의견 컨센서스", result.structured_payload["score_anchor_text"])

    def test_companyguide_future_consensus_is_score_blocked(self):
        html = _companyguide_consensus_html(date_text="2026/07/02")

        with patch(
            "e2r.production.source_connectors.companyguide_live_connector._fetch_companyguide_main",
            return_value=(html, hashlib.sha256(html.encode("utf-8")).hexdigest(), "https://wcomp.fnguide.com"),
        ):
            result = CompanyGuideLiveConnector(repo_root=".").fetch(
                symbol="000660",
                company_name="SK하이닉스",
                as_of_date=date(2026, 7, 1),
                mode="live",
            )

        self.assertEqual(result.published_at, "2026-07-02")
        self.assertEqual(result.structured_payload["score_usage"], "companyguide_consensus_after_as_of_date_not_score_evidence")

    def test_live_full_bounded_uses_target_scoped_llm_query_for_web_fetch(self):
        event = sample_v4_event()
        query = "삼성전자 HBM 고객 배정 qualification"
        url = "https://news.example.com/samsung-hbm"
        task = replace(
            c06_source_task("named_customer_or_customer_quality"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="삼성전자 HBM 고객 배정 확인",
                        url=url,
                        snippet="삼성전자 HBM 고객 배정 관련 기사",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "삼성전자(005930)는 HBM 고객 배정과 qualification 진행 상황을 설명했다. 원문 전문이다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.document_urls, (url,))
        self.assertEqual(len(result.web_search_tasks), 1)
        self.assertEqual(len(result.web_search_results), 1)
        self.assertEqual(len(result.web_fetched_documents), 1)
        self.assertEqual(result.web_search_tasks[0]["status"], "SEARCH_EXECUTED")
        self.assertTrue(result.web_search_tasks[0]["search_call_executed"])
        self.assertEqual(result.web_search_results[0]["selection_status"], "SELECTED_FOR_FETCH")
        self.assertEqual(result.web_fetched_documents[0]["document_id"], result.fetched_document_ids[0])
        self.assertFalse(any(url.startswith("snapshot://") for url in result.document_urls))

    def test_live_full_bounded_external_preferred_preserves_single_query_budget_for_web(self):
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        query = "SK하이닉스 000660 HBM customer allocation report"
        url = "https://securities.example.com/research/sk-hynix-000660"
        calls: list[str] = []
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("IssuerIR", "CompanyGuide"),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="SK Hynix 000660 - HBM customer allocation report",
                        url=url,
                        snippet="SK Hynix HBM customer allocation and demand visibility report",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_report_domain=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "SK Hynix 000660 described HBM customer allocation and demand visibility in this report."
            }
        )
        registry = SourceProviderRegistry(
            connectors=(
                _RecordingLiveConnector(
                    provider_name="CompanyGuide",
                    source_class="CompanyGuide",
                    url="https://wcomp.fnguide.com/company/000660",
                    raw_text="SK하이닉스(000660) 공식 fallback 문서",
                    calls=calls,
                ),
            )
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=registry,
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(calls, [])
        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.document_urls, (url,))
        self.assertEqual(result.source_class, "BrokerReportPublicPDF")
        self.assertEqual(len(result.web_search_tasks), 1)
        self.assertEqual(len(result.web_fetched_documents), 1)
        self.assertEqual(result.budget_used["queries"], 1)
        self.assertEqual(result.budget_used["fetches"], 1)

    def test_live_full_bounded_marks_company_homepage_subdomain_as_verified_newsroom_original(self):
        with TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            snapshot_dir = repo_root / "data/cache/company_guide/2026-06-28"
            snapshot_dir.mkdir(parents=True)
            (snapshot_dir / "000660_snapshot.html").write_text(
                '<html><body><a title="새창열기:[홈페이지] http://www.skhynix.com" '
                'href="http://www.skhynix.com">홈페이지</a></body></html>',
                encoding="utf-8",
            )
            event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
            query = "SK하이닉스 000660 HBM 고객 배정 공식 뉴스룸 2026"
            url = "https://news.skhynix.com/gtc-2026-exhibition-booth/"
            task = replace(
                c06_source_task("customer_preorder_or_allocation"),
                preferred_source_classes=("CompanyNewsroom",),
                fallback_source_classes=("NaverSearch",),
                query_intents=(query,),
                max_queries=1,
                max_candidates=5,
                max_fetches=1,
            )
            search_provider = FixtureSearchProvider(
                results_by_query={
                    query: (
                        SearchResult(
                            title="SK하이닉스, GTC 2026서 엔비디아와 파트너십 재확인 - SK hynix Newsroom",
                            url=url,
                            snippet="SK하이닉스 000660 AI 메모리 제품 포트폴리오 공식 뉴스룸",
                            source="https://openapi.naver.com/v1/search/webkr.json",
                            published_at=datetime(2026, 6, 30, 9, 0),
                            query=query,
                            rank=1,
                            is_news=True,
                        ),
                    )
                }
            )
            fetcher = PageFetcher(
                fixture_text_by_url={
                    url: "SK하이닉스(000660)는 GTC 2026에서 AI 메모리 제품 포트폴리오를 공개했다."
                }
            )

            result = SourceAcquisitionRunnerV4(
                mode="live_full_bounded",
                repo_root=repo_root,
                source_provider_registry=SourceProviderRegistry(connectors=()),
                web_search_provider=search_provider,
                web_page_fetcher=fetcher,
            ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.source_class, "CompanyNewsroom")
        self.assertEqual(result.documents[0].source_name, "IssuerOfficialDomain")
        self.assertIn("verified_issuer_original:", result.documents[0].source_lineage_id)
        self.assertEqual(result.web_fetched_documents[0]["verified_issuer_original"], True)
        self.assertEqual(result.web_fetched_documents[0]["verified_issuer_original_source_class"], "CompanyNewsroom")
        self.assertEqual(result.web_fetched_documents[0]["verified_issuer_homepage_host"], "skhynix.com")
        self.assertEqual(result.web_fetched_documents[0]["verified_issuer_result_host"], "news.skhynix.com")

    def test_live_full_bounded_does_not_mark_independent_news_as_verified_issuer_original(self):
        with TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            snapshot_dir = repo_root / "data/cache/company_guide/2026-06-28"
            snapshot_dir.mkdir(parents=True)
            (snapshot_dir / "000660_snapshot.html").write_text(
                '<html><body><a title="새창열기:[홈페이지] http://www.skhynix.com" '
                'href="http://www.skhynix.com">홈페이지</a></body></html>',
                encoding="utf-8",
            )
            event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
            query = "SK하이닉스 000660 HBM 고객 배정 공식 뉴스룸 2026"
            url = "https://www.dailian.co.kr/news/view/1594665"
            task = replace(
                c06_source_task("customer_preorder_or_allocation"),
                preferred_source_classes=("CompanyNewsroom",),
                fallback_source_classes=("NaverSearch",),
                query_intents=(query,),
                max_queries=1,
                max_candidates=5,
                max_fetches=1,
            )
            search_provider = FixtureSearchProvider(
                results_by_query={
                    query: (
                        SearchResult(
                            title="SK하이닉스, AI 메모리 전시",
                            url=url,
                            snippet="SK하이닉스 000660 관련 기사",
                            source="https://openapi.naver.com/v1/search/webkr.json",
                            published_at=datetime(2026, 6, 30, 9, 0),
                            query=query,
                            rank=1,
                            is_news=True,
                        ),
                    )
                }
            )
            fetcher = PageFetcher(
                fixture_text_by_url={
                    url: "SK하이닉스(000660)는 AI 메모리 제품 포트폴리오를 전시했다."
                }
            )

            result = SourceAcquisitionRunnerV4(
                mode="live_full_bounded",
                repo_root=repo_root,
                source_provider_registry=SourceProviderRegistry(connectors=()),
                web_search_provider=search_provider,
                web_page_fetcher=fetcher,
            ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertNotIn("verified_issuer_original:", result.documents[0].source_lineage_id)
        self.assertEqual(result.web_fetched_documents[0]["verified_issuer_original"], False)
        self.assertIsNone(result.web_fetched_documents[0]["verified_issuer_original_source_class"])

    def test_live_full_bounded_does_not_mark_issuer_domain_spoof_hosts_as_verified_original(self):
        with TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            snapshot_dir = repo_root / "data/cache/company_guide/2026-06-28"
            snapshot_dir.mkdir(parents=True)
            (snapshot_dir / "000660_snapshot.html").write_text(
                '<html><body><a title="새창열기:[홈페이지] http://www.skhynix.com" '
                'href="http://www.skhynix.com">홈페이지</a></body></html>',
                encoding="utf-8",
            )
            event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
            query = "SK하이닉스 000660 HBM 고객 배정 공식 뉴스룸 2026"
            urls = (
                "https://news.skhynix.co.kr/official-looking",
                "https://news-skhynix.co.kr/official-looking",
                "https://skhynix-investor.co.kr/news",
                "https://skhynix.example.com/news",
                "https://skhynix.com.fake-domain.com/news",
            )
            task = replace(
                c06_source_task("customer_preorder_or_allocation"),
                preferred_source_classes=("CompanyNewsroom",),
                fallback_source_classes=("NaverSearch",),
                query_intents=(query,),
                max_queries=1,
                max_candidates=len(urls),
                max_fetches=len(urls),
            )
            search_provider = FixtureSearchProvider(
                results_by_query={
                    query: tuple(
                        SearchResult(
                            title=f"SK하이닉스 000660 공식 뉴스룸처럼 보이는 도메인 {index}",
                            url=url,
                            snippet="SK하이닉스 000660 AI 메모리 관련 글",
                            source="https://openapi.naver.com/v1/search/webkr.json",
                            published_at=datetime(2026, 6, 30, 9, 0),
                            query=query,
                            rank=index,
                            is_news=True,
                        )
                        for index, url in enumerate(urls, start=1)
                    )
                }
            )
            fetcher = PageFetcher(
                fixture_text_by_url={
                    url: "SK하이닉스(000660)는 AI 메모리 제품 포트폴리오를 전시했다."
                    for url in urls
                }
            )

            result = SourceAcquisitionRunnerV4(
                mode="live_full_bounded",
                repo_root=repo_root,
                source_provider_registry=SourceProviderRegistry(connectors=()),
                web_search_provider=search_provider,
                web_page_fetcher=fetcher,
            ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(len(result.web_fetched_documents), len(urls))
        self.assertTrue(all(row["verified_issuer_original"] is False for row in result.web_fetched_documents))
        self.assertTrue(all("verified_issuer_original:" not in document.source_lineage_id for document in result.documents))

    def test_live_full_bounded_marks_registry_backed_alternate_official_domain(self):
        with TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            snapshot_dir = repo_root / "data/cache/company_guide/2026-06-28"
            snapshot_dir.mkdir(parents=True)
            (snapshot_dir / "000660_snapshot.html").write_text(
                '<html><body><a title="새창열기:[홈페이지] http://www.skhynix.com" '
                'href="http://www.skhynix.com">홈페이지</a></body></html>',
                encoding="utf-8",
            )
            config_dir = repo_root / "configs"
            config_dir.mkdir(parents=True)
            (config_dir / "e2r_issuer_official_domains_v1.json").write_text(
                json.dumps(
                    {
                        "schema_version": "e2r_issuer_official_domains_v1",
                        "entries": [
                            {
                                "entry_id": "issuer-domain-000660-newsroom-ko-fixture",
                                "symbol": "000660",
                                "company_name": "SK하이닉스",
                                "host": "news.skhynix.co.kr",
                                "source_class": "CompanyNewsroom",
                                "source_url": "https://news.skhynix.com/",
                                "source_anchor_text": "KOR",
                                "valid_from": "2026-06-28",
                                "verified_as_of": "2026-06-28",
                                "status": "ACTIVE",
                            }
                        ],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
            query = "SK하이닉스 000660 HBM 고객 배정 공식 뉴스룸 2026"
            url = "https://news.skhynix.co.kr/official-looking"
            task = replace(
                c06_source_task("customer_preorder_or_allocation"),
                preferred_source_classes=("CompanyNewsroom",),
                fallback_source_classes=("NaverSearch",),
                query_intents=(query,),
                max_queries=1,
                max_candidates=5,
                max_fetches=1,
            )
            search_provider = FixtureSearchProvider(
                results_by_query={
                    query: (
                        SearchResult(
                            title="SK하이닉스 000660 공식 뉴스룸 HBM 고객 물량 배정",
                            url=url,
                            snippet="SK하이닉스 000660 공식 뉴스룸 KOR",
                            source="https://openapi.naver.com/v1/search/webkr.json",
                            published_at=datetime(2026, 6, 30, 9, 0),
                            query=query,
                            rank=1,
                            is_news=True,
                        ),
                    )
                }
            )
            fetcher = PageFetcher(
                fixture_text_by_url={
                    url: "SK하이닉스(000660)는 HBM 고객 물량 배정 관련 내용을 공식 뉴스룸에 게시했다."
                }
            )

            result = SourceAcquisitionRunnerV4(
                mode="live_full_bounded",
                repo_root=repo_root,
                source_provider_registry=SourceProviderRegistry(connectors=()),
                web_search_provider=search_provider,
                web_page_fetcher=fetcher,
            ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.source_class, "CompanyNewsroom")
        self.assertEqual(result.documents[0].source_name, "IssuerOfficialDomain")
        self.assertIn(
            "verified_issuer_original:issuer_official_domain:news.skhynix.co.kr:news.skhynix.co.kr",
            result.documents[0].source_lineage_id,
        )
        row = result.web_fetched_documents[0]
        self.assertEqual(row["verified_issuer_original"], True)
        self.assertEqual(row["verified_issuer_homepage_host"], "news.skhynix.co.kr")
        self.assertEqual(row["verified_issuer_result_host"], "news.skhynix.co.kr")
        self.assertEqual(row["verified_issuer_authority_source_kind"], "issuer_official_domain_registry")
        self.assertEqual(row["verified_issuer_authority_source_url"], "https://news.skhynix.com/")
        self.assertEqual(row["verified_issuer_authority_source_anchor_text"], "KOR")

    def test_live_full_bounded_ignores_future_registry_official_domain(self):
        with TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            snapshot_dir = repo_root / "data/cache/company_guide/2026-06-28"
            snapshot_dir.mkdir(parents=True)
            (snapshot_dir / "000660_snapshot.html").write_text(
                '<html><body><a title="새창열기:[홈페이지] http://www.skhynix.com" '
                'href="http://www.skhynix.com">홈페이지</a></body></html>',
                encoding="utf-8",
            )
            config_dir = repo_root / "configs"
            config_dir.mkdir(parents=True)
            (config_dir / "e2r_issuer_official_domains_v1.json").write_text(
                json.dumps(
                    {
                        "schema_version": "e2r_issuer_official_domains_v1",
                        "entries": [
                            {
                                "entry_id": "issuer-domain-000660-newsroom-ko-future-fixture",
                                "symbol": "000660",
                                "company_name": "SK하이닉스",
                                "host": "news.skhynix.co.kr",
                                "source_class": "CompanyNewsroom",
                                "source_url": "https://news.skhynix.com/",
                                "source_anchor_text": "KOR",
                                "valid_from": "2026-07-03",
                                "verified_as_of": "2026-07-03",
                                "status": "ACTIVE",
                            }
                        ],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
            query = "SK하이닉스 000660 HBM 고객 배정 공식 뉴스룸 2026"
            url = "https://news.skhynix.co.kr/official-looking"
            task = replace(
                c06_source_task("customer_preorder_or_allocation"),
                preferred_source_classes=("CompanyNewsroom",),
                fallback_source_classes=("NaverSearch",),
                query_intents=(query,),
                max_queries=1,
                max_candidates=5,
                max_fetches=1,
            )
            search_provider = FixtureSearchProvider(
                results_by_query={
                    query: (
                        SearchResult(
                            title="SK하이닉스 000660 공식 뉴스룸 HBM 고객 물량 배정",
                            url=url,
                            snippet="SK하이닉스 000660 공식 뉴스룸 KOR",
                            source="https://openapi.naver.com/v1/search/webkr.json",
                            published_at=datetime(2026, 6, 30, 9, 0),
                            query=query,
                            rank=1,
                            is_news=True,
                        ),
                    )
                }
            )
            fetcher = PageFetcher(
                fixture_text_by_url={
                    url: "SK하이닉스(000660)는 HBM 고객 물량 배정 관련 내용을 공식 뉴스룸에 게시했다."
                }
            )

            result = SourceAcquisitionRunnerV4(
                mode="live_full_bounded",
                repo_root=repo_root,
                source_provider_registry=SourceProviderRegistry(connectors=()),
                web_search_provider=search_provider,
                web_page_fetcher=fetcher,
            ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertNotIn("verified_issuer_original:", result.documents[0].source_lineage_id)
        self.assertEqual(result.web_fetched_documents[0]["verified_issuer_original"], False)
        self.assertIsNone(result.web_fetched_documents[0]["verified_issuer_authority_source_kind"])

    def test_live_full_bounded_rejects_fetched_web_document_without_target_entity(self):
        event = sample_v4_event(symbol="069620", company_name="대웅제약")
        query = "대웅제약 069620 신규시설투자 생산능력"
        url = "https://news.example.com/market-summary"
        task = replace(
            c06_source_task("volume_growth_visible"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="대웅제약 신규시설투자 후속 점검",
                        url=url,
                        snippet="대웅제약 신규시설투자 관련 검색 스니펫",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "한국카본, 테스, 셀트리온, 에이프로젠 주요공시를 정리한 기사 본문이다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertNotIn("no_live_connector_for_requested_source_class", result.provider_errors)
        self.assertEqual(len(result.web_search_results), 1)
        self.assertEqual(result.web_search_results[0]["selection_status"], "REJECTED_TARGET_RELEVANCE_AFTER_FETCH")
        self.assertEqual(len(result.web_rejected_documents), 1)
        self.assertEqual(result.web_rejected_documents[0]["rejection_reason"], "web_fetch_target_not_found_in_full_text")

    def test_live_full_bounded_rejects_search_metadata_target_when_fetched_body_lacks_target(self):
        event = sample_v4_event(symbol="005930", company_name="삼성전자")
        query = "삼성전자 HBM 고객 배정 qualification"
        url = "https://news.example.com/supplier-audit"
        task = replace(
            c06_source_task("named_customer_or_customer_quality"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="삼성전자 공급망 관련 기사",
                        url=url,
                        snippet="삼성전자 고객사 언급이 있는 검색 스니펫",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "월덱스는 감사의견 적정을 받았고 반도체 부품 공급망 전망을 설명했다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertEqual(len(result.web_search_results), 1)
        self.assertEqual(result.web_search_results[0]["selection_status"], "REJECTED_TARGET_RELEVANCE_AFTER_FETCH")
        self.assertEqual(len(result.web_rejected_documents), 1)
        self.assertEqual(result.web_rejected_documents[0]["rejection_reason"], "web_fetch_target_not_found_in_full_text")

    def test_live_full_bounded_rejects_stock_quote_profile_page_even_with_target(self):
        event = sample_v4_event(symbol="003090", company_name="대웅")
        query = "대웅 신규시설투자 생산능력"
        url = "https://finance.naver.com/item/main.naver?code=003090"
        task = replace(
            c06_source_task("volume_growth_visible"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="대웅 : Npay 증권",
                        url=url,
                        snippet="대웅 종목 시세 정보",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_news=False,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: (
                    "대웅 : Npay 증권\n종목명 대웅\n종목코드 003090\n"
                    "종목 시세 정보\n현재가 17,380 전일대비 상승 480 거래량 50,650 시가 17,300 고가 17,580 저가 17,030"
                )
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertEqual(len(result.web_search_results), 1)
        self.assertEqual(result.web_search_results[0]["selection_status"], "REJECTED_NON_EVIDENCE_RESULT_METADATA")
        self.assertEqual(len(result.web_rejected_documents), 1)
        self.assertEqual(
            result.web_rejected_documents[0]["rejection_reason"],
            "web_result_stock_quote_or_profile_page_not_source_document",
        )

    def test_naver_webkr_provider_url_does_not_make_result_news(self):
        result = normalize_search_result(
            {
                "title": "대웅 신규시설투자 검색 결과",
                "url": "https://timeli.tistory.com/1800",
                "snippet": "대웅 관련 검색 스니펫",
                "source": "https://openapi.naver.com/v1/search/webkr.json",
                "rank": 1,
            },
            fallback_query="대웅 신규시설투자",
        )

        self.assertFalse(result.is_news)

    def test_live_full_bounded_rejects_stock_list_result_before_fetch(self):
        event = sample_v4_event(symbol="003090", company_name="대웅")
        query = "대웅 신규시설투자 생산능력"
        url = "https://timeli.tistory.com/1800"
        task = replace(
            c06_source_task("volume_growth_visible"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="2025년 7월 9일 오늘의 상승률 TOP30 이슈정리",
                        url=url,
                        snippet="대웅 003090 상승률과 최근공시를 함께 나열한 목록 페이지",
                        source="https://openapi.naver.com/v1/search/webkr.json",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_news=False,
                    ),
                )
            }
        )
        fetcher = PageFetcher(fixture_text_by_url={url: "이 텍스트는 fetch되면 안 된다."})

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertEqual(len(result.web_search_results), 1)
        self.assertEqual(result.web_search_results[0]["selection_status"], "REJECTED_NON_EVIDENCE_RESULT_METADATA")
        self.assertEqual(result.web_rejected_documents[0]["rejection_reason"], "web_result_stock_list_or_channel_page_not_source_document")

    def test_live_full_bounded_rejects_low_quality_blog_before_fetch(self):
        event = sample_v4_event(symbol="005930", company_name="삼성전자")
        query = "삼성전자 HBM 고객 배정 qualification"
        url = "https://some-personal-blog.tistory.com/1234"
        task = replace(
            c06_source_task("named_customer_or_customer_quality"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="삼성전자 HBM 고객 배정 개인 블로그 정리",
                        url=url,
                        snippet="삼성전자 HBM 고객 배정을 개인 투자 관점에서 정리한 글",
                        source="https://openapi.naver.com/v1/search/webkr.json",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_news=False,
                    ),
                )
            }
        )
        fetcher = PageFetcher(fixture_text_by_url={url: "이 블로그는 fetch되면 안 된다."})

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertEqual(result.web_search_results[0]["selection_status"], "REJECTED_NON_EVIDENCE_RESULT_METADATA")
        self.assertEqual(
            result.web_rejected_documents[0]["rejection_reason"],
            "web_result_low_quality_blog_or_social_not_score_source",
        )
        self.assertEqual(result.budget_used["fetch_attempts"], 0)

    def test_live_full_bounded_rejects_low_quality_blog_content_after_fetch(self):
        event = sample_v4_event(symbol="005930", company_name="삼성전자")
        query = "삼성전자 HBM 고객 배정 qualification"
        url = "https://news.example.com/samsung-hbm-commentary"
        task = replace(
            c06_source_task("named_customer_or_customer_quality"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="삼성전자 HBM 고객 배정 해설",
                        url=url,
                        snippet="삼성전자 HBM 고객 배정 관련 글",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_news=False,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "삼성전자 HBM 고객 배정 관련 개인블로그 투자아이디어 글이다. 원문 공시나 IR 인용은 없다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertEqual(result.web_search_results[0]["selection_status"], "REJECTED_NON_EVIDENCE_CONTENT_AFTER_FETCH")
        self.assertEqual(
            result.web_rejected_documents[0]["rejection_reason"],
            "web_fetch_low_quality_blog_or_social_not_score_source",
        )
        self.assertEqual(result.budget_used["fetch_attempts"], 1)

    def test_live_full_bounded_prefers_target_source_over_market_digest(self):
        event = sample_v4_event(symbol="003090", company_name="대웅제약")
        query = "대웅제약 신규시설투자 생산능력"
        digest_url = "https://news.example.com/daily-disclosure-roundup"
        source_url = "https://news.example.com/daewoong-facility-investment"
        task = replace(
            c06_source_task("volume_growth_visible"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="장 마감 후 주요공시 모음",
                        url=digest_url,
                        snippet="대웅제약 등 여러 상장사 공시를 요약",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                    SearchResult(
                        title="대웅제약 신규시설투자 생산능력 정정 원문 해설",
                        url=source_url,
                        snippet="대웅제약 신규시설투자 정정 공시와 생산능력 관련 기사",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 10, 0),
                        query=query,
                        rank=2,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                digest_url: "장 마감 후 주요공시 모음: 대웅제약, 다른회사A, 다른회사B 공시를 한 줄씩 나열했다.",
                source_url: "대웅제약(069620)은 신규시설투자 정정과 생산능력 확보 일정을 설명했다. 원문 전문이다.",
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.document_urls, (source_url,))
        self.assertEqual(result.web_search_results[0]["url"], source_url)
        self.assertEqual(result.web_search_results[0]["selection_status"], "SELECTED_FOR_FETCH")
        self.assertTrue(
            any(
                row["url"] == digest_url
                and row["rejection_reason"] == "web_result_market_digest_or_disclosure_roundup_not_source_document"
                for row in result.web_rejected_documents
            )
        )

    def test_live_full_bounded_rejects_investing_market_digest_before_fetching_target_article(self):
        event = sample_v4_event(symbol="001360", company_name="삼성제약")
        query = "삼성제약 001360 회사 뉴스룸 계약 생산 매출 수익성 2026"
        digest_url = "https://kr.investing.com/news/stock-market-news/article-1791774"
        source_url = "https://news.example.com/samsung-pharm-contract-margin"
        task = replace(
            c06_source_task("margin_bridge_visible"),
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            preferred_source_classes=("TrustedNews",),
            fallback_source_classes=("NaverSearch",),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="[0121개장체크] 美 증시, FOMC 관망 심리 속 하락",
                        url=digest_url,
                        snippet="국채금리 상승 부담과 3대 지수 흐름을 정리한 시장 기사",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                    SearchResult(
                        title="삼성제약 001360 계약 생산 매출 수익성 점검",
                        url=source_url,
                        snippet="삼성제약 계약 생산 매출 수익성 관련 원문 기사",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 10, 0),
                        query=query,
                        rank=2,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                digest_url: "이 시장 요약 페이지는 fetch되면 안 된다.",
                source_url: "삼성제약(001360)은 계약 생산 매출과 수익성 개선 계획을 설명했다. 원문 전문이다.",
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.document_urls, (source_url,))
        self.assertEqual(result.budget_used["fetch_attempts"], 1)
        rejected = {row["url"]: row["rejection_reason"] for row in result.web_rejected_documents}
        self.assertEqual(rejected[digest_url], "web_result_market_or_stock_profile_page_not_source_document")

    def test_live_full_bounded_web_relevance_uses_title_symbol_english_alias(self):
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        query = "SK하이닉스 000660 HBM customer allocation report"
        url = "https://securities.example.com/research/sk-hynix-000660"
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("ReportPDF",),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="SK Hynix 000660 - Research Report | Broker",
                        url=url,
                        snippet="SK Hynix HBM customer allocation and demand report",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_report_domain=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "SK Hynix described HBM customer allocation and demand visibility. Full report text."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.document_urls, (url,))
        self.assertEqual(result.web_search_results[0]["selection_status"], "SELECTED_FOR_FETCH")
        self.assertFalse(result.web_rejected_documents)

    def test_live_full_bounded_marks_recognized_broker_report_domain_as_verified_original(self):
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        query = "SK하이닉스 000660 HBM customer allocation report PDF"
        url = "https://stock.pstatic.net/stock-research/company/17/20250630_company_000660.pdf"
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("ReportPDF",),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="SK Hynix 000660 - Research Report | Broker",
                        url=url,
                        snippet="SK Hynix HBM customer allocation and demand report",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_pdf=True,
                        is_report_domain=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "SK Hynix described HBM customer allocation and demand visibility. Full report text."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.source_class, "BrokerReportPublicPDF")
        self.assertEqual(result.documents[0].source_name, "BrokerReportDomain")
        self.assertIn(
            "verified_report_original:broker_report_domain:stock.pstatic.net",
            result.documents[0].source_lineage_id,
        )
        fetched = result.web_fetched_documents[0]
        self.assertEqual(fetched["verified_report_original"], True)
        self.assertEqual(fetched["verified_report_original_source_class"], "BrokerReportPublicPDF")
        self.assertEqual(fetched["verified_report_original_resolver"], "recognized_broker_report_domain")
        self.assertEqual(fetched["verified_report_result_host"], "stock.pstatic.net")

    def test_live_full_bounded_marks_broker_research_routes_from_goal4_artifacts_as_verified_original(self):
        event = sample_v4_event(symbol="012510", company_name="더존비즈온")
        cases = (
            (
                "https://www.eugenefn.com/common/files/amail/20250609_B45_sophie.yim_79.pdf",
                "eugenefn.com",
                True,
                "2H25 OUTLOOK 반도체 소부장",
            ),
            (
                "https://bbn.kiwoom.com/rfCR10848",
                "bbn.kiwoom.com",
                False,
                "더존비즈온 (012510) AI 시대를 앞당길 주역",
            ),
            (
                "https://securities.miraeasset.com/bbs/board/message/view.do?categoryId=1521&messageId=2332084",
                "securities.miraeasset.com",
                False,
                "더존비즈온 (012510/매수) 이익 먼저 잡고, 성장은 곧 따라올 것",
            ),
        )
        for url, host, is_pdf, title in cases:
            with self.subTest(url=url):
                query = f"{event.company_name} {event.symbol} 리포트 ARR 성장 원문"
                task = replace(
                    c06_source_task("medium_term_revision_visibility"),
                    candidate_event_id=event.candidate_event_id,
                    symbol=event.symbol,
                    company_name=event.company_name,
                    preferred_source_classes=("BrokerReportPublicPDF",),
                    fallback_source_classes=("ReportPDF",),
                    query_intents=(query,),
                    max_queries=1,
                    max_candidates=5,
                    max_fetches=1,
                )
                search_provider = FixtureSearchProvider(
                    results_by_query={
                        query: (
                            SearchResult(
                                title=title,
                                url=url,
                                snippet=f"{event.company_name} {event.symbol} recurring revenue report",
                                source="NaverSearch",
                                published_at=datetime(2026, 6, 30, 9, 0),
                                query=query,
                                rank=1,
                                is_pdf=is_pdf,
                                is_report_domain=True,
                            ),
                        )
                    }
                )
                fetcher = PageFetcher(
                    fixture_text_by_url={
                        url: f"{event.company_name} recurring revenue and ARR growth are discussed in this broker report."
                    }
                )

                result = SourceAcquisitionRunnerV4(
                    mode="live_full_bounded",
                    source_provider_registry=SourceProviderRegistry(connectors=()),
                    web_search_provider=search_provider,
                    web_page_fetcher=fetcher,
                ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

                self.assertEqual(result.status, "PARSED")
                self.assertEqual(result.source_class, "BrokerReportPublicPDF")
                self.assertEqual(result.documents[0].source_name, "BrokerReportDomain")
                self.assertIn(
                    f"verified_report_original:broker_report_domain:{host}",
                    result.documents[0].source_lineage_id,
                )
                fetched = result.web_fetched_documents[0]
                self.assertEqual(fetched["verified_report_original"], True)
                self.assertEqual(fetched["verified_report_result_host"], host)

    def test_live_full_bounded_does_not_mark_broker_domain_non_report_pdf_as_verified_original(self):
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        query = "SK하이닉스 000660 HBM customer allocation report PDF"
        url = "https://www.samsungpop.com/customer/event_terms.pdf"
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=("ReportPDF",),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="SK Hynix 000660 event terms PDF | SamsungPop",
                        url=url,
                        snippet="SK Hynix HBM customer allocation and demand text appears in a non-report PDF.",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_pdf=True,
                        is_report_domain=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "SK Hynix HBM customer allocation and demand visibility text inside non-report terms PDF."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.source_class, "BrokerReportPublicPDF")
        self.assertNotEqual(result.documents[0].source_name, "BrokerReportDomain")
        self.assertNotIn("verified_report_original:broker_report_domain:", result.documents[0].source_lineage_id)
        fetched = result.web_fetched_documents[0]
        self.assertEqual(fetched["verified_report_original"], False)
        self.assertIsNone(fetched["verified_report_original_source_class"])
        self.assertIsNone(fetched["verified_report_original_resolver"])

    def test_live_full_bounded_does_not_mark_same_host_query_spoof_as_verified_original(self):
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        query = "SK하이닉스 000660 HBM customer allocation report PDF"
        spoof_urls = (
            (
                "https://www.samsungpop.com/support/download?"
                "saveKey=research.pdf&fileName=fake.pdf&contentType=application/pdf"
            ),
            "https://www.samsungpop.com/common.do?next=research.pdf&contentType=application/pdf",
            "https://www.samsungpop.com/media/pdfs/fake.pdf",
        )
        for url in spoof_urls:
            with self.subTest(url=url):
                task = replace(
                    c06_source_task("customer_preorder_or_allocation"),
                    candidate_event_id=event.candidate_event_id,
                    symbol=event.symbol,
                    company_name=event.company_name,
                    preferred_source_classes=("BrokerReportPublicPDF",),
                    fallback_source_classes=("ReportPDF",),
                    query_intents=(query,),
                    max_queries=1,
                    max_candidates=5,
                    max_fetches=1,
                )
                search_provider = FixtureSearchProvider(
                    results_by_query={
                        query: (
                            SearchResult(
                                title="SK Hynix 000660 fake research PDF | SamsungPop",
                                url=url,
                                snippet="SK Hynix HBM customer allocation and demand text appears in a support download.",
                                source="NaverSearch",
                                published_at=datetime(2026, 6, 30, 9, 0),
                                query=query,
                                rank=1,
                                is_pdf=True,
                                is_report_domain=True,
                            ),
                        )
                    }
                )
                fetcher = PageFetcher(
                    fixture_text_by_url={
                        url: "SK Hynix HBM customer allocation and demand visibility text inside support download."
                    }
                )

                result = SourceAcquisitionRunnerV4(
                    mode="live_full_bounded",
                    source_provider_registry=SourceProviderRegistry(connectors=()),
                    web_search_provider=search_provider,
                    web_page_fetcher=fetcher,
                ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

                self.assertEqual(result.status, "PARSED")
                self.assertEqual(result.source_class, "BrokerReportPublicPDF")
                self.assertNotEqual(result.documents[0].source_name, "BrokerReportDomain")
                self.assertNotIn("verified_report_original:broker_report_domain:", result.documents[0].source_lineage_id)
                fetched = result.web_fetched_documents[0]
                self.assertEqual(fetched["verified_report_original"], False)
                self.assertIsNone(fetched["verified_report_original_source_class"])
                self.assertIsNone(fetched["verified_report_original_resolver"])

    def test_stored_broker_report_snapshot_requires_verified_report_original_url(self):
        event = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        task = replace(
            c06_source_task("customer_preorder_or_allocation"),
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=(),
            max_fetches=1,
        )
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            snapshot_root = root / "data/report_snapshots"
            snapshot_root.mkdir(parents=True)
            (snapshot_root / "spoofed_report.txt").write_text(
                "SK하이닉스 000660 target price revision and HBM demand visibility.",
                encoding="utf-8",
            )
            (snapshot_root / "report_snapshots.jsonl").write_text(
                "\n".join(
                    json.dumps(row)
                    for row in (
                        {
                            "url": "https://evil.example/samsungpop.com/research/fake-report.pdf",
                            "title": "SK Hynix fake broker report",
                            "symbol": "000660",
                            "company_name": "SK하이닉스",
                            "as_of_date": "2026-06-30",
                            "source_type": "broker_report",
                            "extracted_text_path": "spoofed_report.txt",
                        },
                        {
                            "url": (
                                "https://www.samsungpop.com/support/download?"
                                "saveKey=research.pdf&fileName=fake.pdf&contentType=application/pdf"
                            ),
                            "title": "SK Hynix same-host fake broker report",
                            "symbol": "000660",
                            "company_name": "SK하이닉스",
                            "as_of_date": "2026-06-30",
                            "source_type": "broker_report",
                            "extracted_text_path": "spoofed_report.txt",
                        },
                        {
                            "url": "https://www.samsungpop.com/common.do?next=research.pdf&contentType=application/pdf",
                            "title": "SK Hynix common.do fake broker report",
                            "symbol": "000660",
                            "company_name": "SK하이닉스",
                            "as_of_date": "2026-06-30",
                            "source_type": "broker_report",
                            "extracted_text_path": "spoofed_report.txt",
                        },
                        {
                            "url": "https://www.samsungpop.com/media/pdfs/fake.pdf",
                            "title": "SK Hynix media pdf fake broker report",
                            "symbol": "000660",
                            "company_name": "SK하이닉스",
                            "as_of_date": "2026-06-30",
                            "source_type": "broker_report",
                            "extracted_text_path": "spoofed_report.txt",
                        },
                    )
                )
                + "\n",
                encoding="utf-8",
            )

            result = SourceAcquisitionRunnerV4(
                mode="frozen_real_source_snapshot",
                repo_root=root,
            ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "NO_EVIDENCE_FOUND")
        self.assertFalse(result.documents)
        self.assertEqual(result.stop_reason, "no_matching_real_source_snapshot")

    def test_live_full_bounded_rejects_generic_major_disclosure_roundup_before_fetch(self):
        event = sample_v4_event(symbol="003090", company_name="대웅제약")
        query = "대웅제약 신규시설투자 생산능력"
        roundup_url = "https://www.kdpress.co.kr/news/articleView.html?idxno=205554"
        task = replace(
            c06_source_task("volume_growth_visible"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="[주요공시] 한국카본, 테스, 셀트리온, 에이프로젠, 삼부토건 외",
                        url=roundup_url,
                        snippet="대웅제약 신규시설투자 정정 공시도 포함된 주요공시 라운드업",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(fixture_text_by_url={roundup_url: "이 라운드업은 fetch되면 안 된다."})

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertEqual(result.web_search_results[0]["selection_status"], "REJECTED_NON_EVIDENCE_RESULT_METADATA")
        self.assertEqual(
            result.web_rejected_documents[0]["rejection_reason"],
            "web_result_market_digest_or_disclosure_roundup_not_source_document",
        )

    def test_live_full_bounded_rejects_site_archive_before_fetch(self):
        event = sample_v4_event(symbol="003090", company_name="대웅제약")
        query = "대웅제약 신규시설투자 생산능력"
        archive_url = "https://biz.heraldcorp.com/sitemap/archive/2020/20200423"
        task = replace(
            c06_source_task("volume_growth_visible"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="23일 - 헤럴드경제",
                        url=archive_url,
                        snippet="대웅제약을 포함한 날짜별 기사 목록",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(fixture_text_by_url={archive_url: "이 아카이브는 fetch되면 안 된다."})

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertEqual(result.web_search_results[0]["selection_status"], "REJECTED_NON_EVIDENCE_RESULT_METADATA")
        self.assertEqual(
            result.web_rejected_documents[0]["rejection_reason"],
            "web_result_site_archive_or_sitemap_not_source_document",
        )

    def test_live_full_bounded_dedupes_repeated_web_result_url_before_refetch(self):
        event = sample_v4_event(symbol="003090", company_name="대웅제약")
        query = "대웅제약 신규시설투자 생산능력"
        duplicate_url = "https://plumsec.com/ko/report/detail?rcept_no=20260630801612"
        unique_url = "https://news.example.com/daewoong-followup"
        task = replace(
            c06_source_task("volume_growth_visible"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=2,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="대웅제약 신규시설투자 정정 원문",
                        url=duplicate_url,
                        snippet="대웅제약 신규시설투자 정정 공시",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                    SearchResult(
                        title="대웅제약 신규시설투자 정정 원문 재배포",
                        url=duplicate_url,
                        snippet="같은 URL 재검색 결과",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 5),
                        query=query,
                        rank=2,
                        is_news=True,
                    ),
                    SearchResult(
                        title="대웅제약 신규시설투자 생산능력 후속 기사",
                        url=unique_url,
                        snippet="대웅제약 신규시설투자 후속 기사",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 10, 0),
                        query=query,
                        rank=3,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                duplicate_url: "대웅제약(069620)은 신규시설투자 정정 공시를 설명했다.",
                unique_url: "대웅제약(069620)은 신규시설투자 생산능력 후속 계획을 설명했다.",
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.document_urls, (duplicate_url, unique_url))
        self.assertEqual([row["selection_status"] for row in result.web_search_results], [
            "SELECTED_FOR_FETCH",
            "REJECTED_DUPLICATE_WEB_RESULT",
            "SELECTED_FOR_FETCH",
        ])
        self.assertTrue(
            any(row["rejection_reason"] == "duplicate_web_result_url_not_refetched" for row in result.web_rejected_documents)
        )

    def test_live_full_bounded_keeps_official_first_and_web_fallback_leafs(self):
        event = sample_v4_event()
        query = "삼성전자 HBM 고객 배정 qualification"
        url = "https://news.example.com/samsung-hbm-followup"
        task = replace(
            c06_source_task("named_customer_or_customer_quality"),
            preferred_source_classes=("CompanyGuide",),
            fallback_source_classes=("NaverSearch",),
            query_intents=(query,),
            max_queries=2,
            max_candidates=5,
            max_fetches=2,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="삼성전자 HBM 고객 배정 확인",
                        url=url,
                        snippet="삼성전자 HBM 고객 배정 관련 기사",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 20, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "삼성전자(005930)는 HBM 고객 배정과 qualification 진행 상황을 설명했다. 원문 전문이다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=(_LiveOfficialFixtureConnector(),)),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(len(result.fetched_document_ids), 2)
        self.assertEqual(result.document_urls[0], "https://example.com/companyguide/A005930")
        self.assertEqual(result.document_urls[1], url)
        self.assertEqual(len(result.web_search_tasks), 1)
        self.assertEqual(len(result.web_fetched_documents), 1)
        self.assertEqual(result.web_search_tasks[0]["status"], "SEARCH_EXECUTED")
        self.assertLessEqual(result.budget_used["queries"], task.max_queries)
        self.assertLessEqual(result.budget_used["fetches"], task.max_fetches)

    def test_live_full_bounded_rejects_unscoped_llm_query_without_search(self):
        event = sample_v4_event()
        task = replace(
            c06_source_task("named_customer_or_customer_quality"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=("HBM 고객 배정 qualification",),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=FixtureSearchProvider(),
            web_page_fetcher=PageFetcher(fixture_text_by_url={}),
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "REJECTED_BY_POLICY")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertEqual(len(result.web_search_tasks), 1)
        self.assertEqual(result.web_search_tasks[0]["status"], "REJECTED_BY_POLICY")
        self.assertEqual(result.web_rejected_documents[0]["rejection_reason"], "web_query_not_target_scoped")
        self.assertIn("missing_target_scoped_llm_query_intent", result.provider_errors)

    def test_official_solvable_gap_is_not_sent_to_web_fallback(self):
        event = sample_v4_event()
        task = replace(
            c06_source_task("medium_term_revision_visibility"),
            preferred_source_classes=("NaverSearch",),
            fallback_source_classes=(),
            query_intents=("삼성전자 EPS revision",),
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=FixtureSearchProvider(),
        ).acquire(event=event, task=task, as_of_date=date(2026, 6, 29))

        self.assertEqual(result.status, "REJECTED_BY_POLICY")
        self.assertIn("official_solvable_gap_sent_to_general_web", result.provider_errors)

    def test_cash_or_revision_gap_allows_bounded_report_fallback_after_official_first(self):
        event = sample_v4_event(symbol="034020", company_name="두산에너빌리티")
        query = "두산에너빌리티 034020 2026 영업이익 추정 상향 리포트 PDF"
        url = "https://research.example.com/doosan-energy-revision.pdf"
        task = replace(
            c06_source_task("cash_or_revision_conversion"),
            preferred_source_classes=("ReportPDF", "BrokerReportPublicPDF"),
            fallback_source_classes=("CompanyNewsroom",),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="두산에너빌리티 실적 추정 상향 리포트",
                        url=url,
                        snippet="두산에너빌리티 034020 영업이익 추정 상향 리포트 원문",
                        source="BrokerReportPublicPDF",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_news=False,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "두산에너빌리티(034020)의 2026년 영업이익 추정치가 상향 조정됐다는 리포트 원문."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertNotEqual(result.status, "REJECTED_BY_POLICY")
        self.assertNotIn("official_solvable_gap_sent_to_general_web", result.provider_errors)
        self.assertEqual(len(result.web_search_tasks), 1)
        self.assertEqual(result.web_search_tasks[0]["status"], "SEARCH_EXECUTED")

    def test_contract_visibility_gap_is_not_sent_to_web_fallback(self):
        event = sample_v4_event(symbol="114450", company_name="그린생명과학")
        query = "그린생명과학 114450 단일판매 공급계약 정정 배경"
        url = "https://news.example.com/green-contract-context"
        task = replace(
            c06_source_task("contract_visibility"),
            preferred_source_classes=("CompanyNewsroom",),
            fallback_source_classes=("TrustedNews",),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="그린생명과학 공급계약 정정 배경",
                        url=url,
                        snippet="그린생명과학 114450 단일판매 공급계약 정정 배경 설명",
                        source="TrustedNews",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "그린생명과학(114450)은 단일판매 공급계약 정정 배경과 계약 가시성을 설명했다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "REJECTED_BY_POLICY")
        self.assertIn("official_solvable_gap_sent_to_general_web", result.provider_errors)
        self.assertEqual(result.web_search_tasks, ())
        self.assertEqual(result.fetched_document_ids, ())
        self.assertEqual(result.document_urls, ())

    def test_news_fallback_uses_news_source_class_when_report_pdf_is_first_preference(self):
        event = sample_v4_event(symbol="114450", company_name="그린생명과학")
        query = "그린생명과학 114450 2026 공급계약 수익성 개선"
        url = "https://news.example.com/green-margin-bridge"
        task = replace(
            c06_source_task("margin_bridge_visible"),
            preferred_source_classes=("BrokerReportPublicPDF", "ReportPDF", "TrustedNews", "CompanyNewsroom"),
            fallback_source_classes=("IndustryMedia",),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="그린생명과학 공급계약 수익성 개선 기대",
                        url=url,
                        snippet="그린생명과학 114450 공급계약 수익성 개선 관련 기사",
                        source="TrustedNews",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_news=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "그린생명과학(114450)은 AI반도체 소재 공급계약으로 수익성 개선 가능성을 설명했다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.source_class, "IndustryMedia")
        self.assertEqual(result.document_urls, (url,))
        self.assertEqual(result.documents[0].source_type.value, "NEWS")

    def test_web_discovered_kind_document_keeps_official_kind_source_class(self):
        event = sample_v4_event(symbol="003090", company_name="대웅")
        query = "대웅 003090 신규시설투자 정정 공시"
        url = "https://kind.krx.co.kr/common/disclsviewer.do?method=search&acptno=20260630001612"
        task = replace(
            c06_source_task("mix_improvement"),
            preferred_source_classes=("TrustedNews", "BrokerReportPublicPDF", "CompanyNewsroom"),
            fallback_source_classes=("IndustryMedia", "ReportPDF", "NaverSearch"),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="[대웅] [정정]신규시설투자등",
                        url=url,
                        snippet="대웅 003090 신규시설투자 정정 공시",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_disclosure=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "대웅(003090)은 신규시설투자 정정 공시에서 투자기간과 투자목적을 설명했다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.source_class, "KIND")
        self.assertEqual(result.documents[0].source_name, "KIND")
        self.assertEqual(result.documents[0].source_type.value, "FILING")
        self.assertEqual(result.web_search_results[0]["official_detail_resolution_required"], True)
        self.assertEqual(result.web_search_results[0]["official_source_class"], "KIND")
        self.assertEqual(result.web_search_results[0]["official_detail_resolver"], "kind_disclsviewer_acptno")
        self.assertEqual(result.web_search_results[0]["official_document_id"], "kind:disclosure:20260630001612")
        self.assertEqual(result.web_search_results[0]["official_detail_resolution_status"], "RESOLVED")
        self.assertEqual(result.web_fetched_documents[0]["official_detail_resolution_status"], "RESOLVED")
        self.assertEqual(result.web_fetched_documents[0]["official_document_id"], "kind:disclosure:20260630001612")

    def test_web_discovered_dart_document_keeps_official_dart_resolution_metadata(self):
        event = sample_v4_event(symbol="003090", company_name="대웅")
        query = "대웅 003090 신규시설투자 정정 DART"
        url = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801612"
        task = replace(
            c06_source_task("mix_improvement"),
            preferred_source_classes=("TrustedNews", "BrokerReportPublicPDF", "CompanyNewsroom"),
            fallback_source_classes=("IndustryMedia", "ReportPDF", "NaverSearch"),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="[대웅] [정정]신규시설투자등",
                        url=url,
                        snippet="대웅 003090 신규시설투자 정정 DART 공시",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_disclosure=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "대웅(003090)은 신규시설투자 정정 공시에서 투자기간과 투자목적을 설명했다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertEqual(result.source_class, "DART")
        self.assertEqual(result.documents[0].source_name, "DART")
        self.assertEqual(result.documents[0].source_type.value, "FILING")
        self.assertEqual(result.web_search_results[0]["official_detail_resolution_required"], True)
        self.assertEqual(result.web_search_results[0]["official_source_class"], "DART")
        self.assertEqual(result.web_search_results[0]["official_detail_resolver"], "dart_viewer_rcpno")
        self.assertEqual(result.web_search_results[0]["official_document_id"], "opendart:disclosure:20260630801612")
        self.assertEqual(result.web_search_results[0]["official_detail_resolution_status"], "RESOLVED")
        self.assertEqual(result.web_fetched_documents[0]["official_detail_resolution_status"], "RESOLVED")

    def test_web_discovered_official_detail_fetch_failure_is_a_resolver_failure(self):
        event = sample_v4_event(symbol="003090", company_name="대웅")
        query = "대웅 003090 신규시설투자 정정 공시"
        url = "https://kind.krx.co.kr/common/disclsviewer.do?method=search&acptno=20260630001612"
        task = replace(
            c06_source_task("mix_improvement"),
            preferred_source_classes=("TrustedNews",),
            fallback_source_classes=("NaverSearch",),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="[대웅] [정정]신규시설투자등",
                        url=url,
                        snippet="대웅 003090 신규시설투자 정정 공시",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_disclosure=True,
                    ),
                )
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=PageFetcher(fixture_text_by_url={}),
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertEqual(result.fetched_document_ids, ())
        self.assertIn("official_detail_resolve_failed", result.provider_errors)
        self.assertEqual(result.web_search_results[0]["official_detail_resolution_required"], True)
        self.assertEqual(result.web_search_results[0]["official_detail_resolution_status"], "FAILED")
        self.assertEqual(result.web_rejected_documents[0]["official_detail_resolution_status"], "FAILED")
        self.assertTrue(result.web_rejected_documents[0]["rejection_reason"].startswith("official_detail_resolve_failed:"))

    def test_web_discovered_fake_kind_path_does_not_become_official_kind_source_class(self):
        event = sample_v4_event(symbol="003090", company_name="대웅")
        query = "대웅 003090 신규시설투자 정정 공시"
        url = "https://example.com/archive/kind.krx.co.kr/fake-disclosure"
        task = replace(
            c06_source_task("mix_improvement"),
            preferred_source_classes=("TrustedNews", "KIND", "BrokerReportPublicPDF"),
            fallback_source_classes=("IndustryMedia", "NaverSearch"),
            query_intents=(query,),
            max_queries=1,
            max_candidates=5,
            max_fetches=1,
        )
        search_provider = FixtureSearchProvider(
            results_by_query={
                query: (
                    SearchResult(
                        title="[대웅] [정정]신규시설투자등",
                        url=url,
                        snippet="대웅 003090 신규시설투자 정정 공시를 인용한 비공식 페이지",
                        source="NaverSearch",
                        published_at=datetime(2026, 6, 30, 9, 0),
                        query=query,
                        rank=1,
                        is_disclosure=True,
                    ),
                )
            }
        )
        fetcher = PageFetcher(
            fixture_text_by_url={
                url: "대웅(003090)은 신규시설투자 정정 공시에서 투자기간과 투자목적을 설명했다."
            }
        )

        result = SourceAcquisitionRunnerV4(
            mode="live_full_bounded",
            source_provider_registry=SourceProviderRegistry(connectors=()),
            web_search_provider=search_provider,
            web_page_fetcher=fetcher,
        ).acquire(event=event, task=task, as_of_date=date(2026, 7, 1))

        self.assertEqual(result.status, "PARSED")
        self.assertNotEqual(result.source_class, "KIND")

    def test_opendart_live_connector_prefers_detail_disclosure_over_company_profile(self):
        detail_xml = """
        <DOCUMENT>
          <SECTION-1>
            계약금액: 4,000억원
            최근매출액 대비: 45%
            계약기간: 2024.05.21 ~ 2027.05.20
            계약상대방: 북미 유틸리티
            계약내용: 초고압변압기
          </SECTION-1>
        </DOCUMENT>
        """
        calls: list[str] = []

        def fake_get(url, params=None, timeout=None):
            calls.append(url)
            if url.endswith("/list.json"):
                return _FakeResponse(
                    json_payload={
                        "status": "000",
                        "list": [
                            {
                                "stock_code": "111111",
                                "corp_name": "한전변압기",
                                "report_nm": "단일판매·공급계약체결",
                                "rcept_no": "202405210091",
                                "rcept_dt": "20240521",
                            }
                        ],
                    }
                )
            if url.endswith("/document.xml"):
                return _FakeResponse(text_payload=detail_xml)
            raise AssertionError(f"unexpected OpenDART URL: {url}")

        with patch.dict("os.environ", {"OPENDART_API_KEY": "unit-secret"}, clear=True), patch(
            "e2r.production.source_connectors.opendart_live_connector._corp_row_for_symbol",
            return_value={"symbol": "111111", "company_name": "한전변압기", "corp_code": "00199999"},
        ), patch("e2r.production.source_connectors.opendart_live_connector.requests.get", side_effect=fake_get):
            result = OpenDARTLiveConnector(repo_root=".").fetch(
                symbol="111111",
                company_name="한전변압기",
                as_of_date=date(2026, 6, 29),
                mode="live",
            )

        self.assertEqual(result.status, "FETCHED")
        self.assertEqual(result.mode, "live")
        self.assertEqual(result.canonical_url, "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=202405210091")
        self.assertEqual(result.official_document_id, "opendart:disclosure:202405210091")
        self.assertIn("list.json", " ".join(calls))
        self.assertIn("document.xml", " ".join(calls))
        self.assertNotIn("company.json", " ".join(calls))
        self.assertEqual(result.structured_payload["row_source"], "opendart_detail")
        self.assertEqual(result.structured_payload["contract_amount_to_prior_sales"], 0.45)
        self.assertEqual(result.structured_payload["counterparty"], "북미 유틸리티")
        self.assertTrue(result.structured_payload["detail_fetched"])
        self.assertNotIn("score_usage", result.structured_payload)

    def test_opendart_live_connector_decodes_document_xml_zip_payload(self):
        detail_xml = """
        <DOCUMENT>
          <SECTION-1>
            계약금액: 4,000억원
            최근매출액 대비: 45%
            계약상대방: 북미 유틸리티
          </SECTION-1>
        </DOCUMENT>
        """
        archive = io.BytesIO()
        with zipfile.ZipFile(archive, "w") as zf:
            zf.writestr("202405210091.xml", detail_xml)

        def fake_get(url, params=None, timeout=None):
            if url.endswith("/list.json"):
                return _FakeResponse(
                    json_payload={
                        "status": "000",
                        "list": [
                            {
                                "stock_code": "111111",
                                "corp_name": "한전변압기",
                                "report_nm": "단일판매·공급계약체결",
                                "rcept_no": "202405210091",
                                "rcept_dt": "20240521",
                            }
                        ],
                    }
                )
            if url.endswith("/document.xml"):
                return _FakeResponse(content_payload=archive.getvalue())
            raise AssertionError(f"unexpected OpenDART URL: {url}")

        with patch.dict("os.environ", {"OPENDART_API_KEY": "unit-secret"}, clear=True), patch(
            "e2r.production.source_connectors.opendart_live_connector._corp_row_for_symbol",
            return_value={"symbol": "111111", "company_name": "한전변압기", "corp_code": "00199999"},
        ), patch("e2r.production.source_connectors.opendart_live_connector.requests.get", side_effect=fake_get):
            result = OpenDARTLiveConnector(repo_root=".").fetch(
                symbol="111111",
                company_name="한전변압기",
                as_of_date=date(2026, 6, 29),
                mode="live",
            )

        self.assertEqual(result.status, "FETCHED")
        self.assertNotIn("PK", result.raw_text[:20])
        self.assertIn("계약금액", result.raw_text)
        self.assertEqual(result.structured_payload["contract_amount_to_prior_sales"], 0.45)

    def test_opendart_full_thesis_fetch_prefers_periodic_report_without_changing_daily_fetch(self):
        detail_by_receipt = {
            "202607100001": "<DOCUMENT>유상증자 시설자금 확정 공시와 발행 조건을 설명하는 충분한 길이의 공식 문서 본문입니다. 기준일 현재 발행 절차가 진행 중입니다.</DOCUMENT>",
            "202605150001": (
                "<DOCUMENT>분기보고서 공식 문서 본문입니다."
                + ("정기보고서 본문 " * 3000)
                + "20,000자 뒤의 HBM 매출과 영업이익 현황도 보존되어야 합니다.</DOCUMENT>"
            ),
        }

        def fake_get(url, params=None, timeout=None):
            if url.endswith("/list.json"):
                return _FakeResponse(
                    json_payload={
                        "status": "000",
                        "list": [
                            {
                                "stock_code": "000660",
                                "corp_name": "SK하이닉스",
                                "report_nm": "주요사항보고서(유상증자결정)",
                                "rcept_no": "202607100001",
                                "rcept_dt": "20260710",
                            },
                            {
                                "stock_code": "000660",
                                "corp_name": "SK하이닉스",
                                "report_nm": "분기보고서 (2026.03)",
                                "rcept_no": "202605150001",
                                "rcept_dt": "20260515",
                            },
                        ],
                    }
                )
            if url.endswith("/document.xml"):
                return _FakeResponse(text_payload=detail_by_receipt[str(params["rcept_no"])])
            raise AssertionError(f"unexpected OpenDART URL: {url}")

        environment = {"OPENDART_API_KEY": "unit-secret"}
        corp = {"symbol": "000660", "company_name": "SK하이닉스", "corp_code": "00164779"}
        with patch.dict("os.environ", environment, clear=True), patch(
            "e2r.production.source_connectors.opendart_live_connector._corp_row_for_symbol",
            return_value=corp,
        ), patch(
            "e2r.production.source_connectors.opendart_live_connector.requests.get",
            side_effect=fake_get,
        ):
            connector = OpenDARTLiveConnector(repo_root=".")
            daily = connector.fetch(
                symbol="000660",
                company_name="SK하이닉스",
                as_of_date=date(2026, 7, 11),
                mode="live",
            )
            research = connector.fetch_research_document(
                symbol="000660",
                company_name="SK하이닉스",
                as_of_date=date(2026, 7, 11),
                mode="live",
            )

        self.assertEqual(daily.request_params["rcept_no"], "202607100001")
        self.assertEqual(research.request_params["rcept_no"], "202605150001")
        self.assertIn("HBM 매출", research.raw_text)
        self.assertGreater(len(research.raw_text), 20_000)
        self.assertTrue(research.structured_payload["research_document_preserved"])

    def test_opendart_live_connector_blocks_list_only_disclosure_when_detail_fails(self):
        def fake_get(url, params=None, timeout=None):
            if url.endswith("/list.json"):
                return _FakeResponse(
                    json_payload={
                        "status": "000",
                        "list": [
                            {
                                "stock_code": "111111",
                                "corp_name": "한전변압기",
                                "report_nm": "단일판매·공급계약체결",
                                "rcept_no": "202405210091",
                                "rcept_dt": "20240521",
                            }
                        ],
                    }
                )
            if url.endswith("/document.xml"):
                raise RuntimeError("document endpoint unavailable")
            raise AssertionError(f"unexpected OpenDART URL: {url}")

        with patch.dict("os.environ", {"OPENDART_API_KEY": "unit-secret"}, clear=True), patch(
            "e2r.production.source_connectors.opendart_live_connector._corp_row_for_symbol",
            return_value={"symbol": "111111", "company_name": "한전변압기", "corp_code": "00199999"},
        ), patch("e2r.production.source_connectors.opendart_live_connector.requests.get", side_effect=fake_get):
            result = OpenDARTLiveConnector(repo_root=".").fetch(
                symbol="111111",
                company_name="한전변압기",
                as_of_date=date(2026, 6, 29),
                mode="live",
            )

        self.assertEqual(result.status, "FETCHED")
        self.assertEqual(result.structured_payload["row_source"], "opendart_list")
        self.assertEqual(result.structured_payload["score_usage"], "opendart_list_only_detail_not_fetched")
        self.assertNotIn("contract_amount_to_prior_sales", result.structured_payload)


class _LiveOfficialFixtureConnector:
    provider_name = "CompanyGuide"
    source_class = "CompanyGuide"

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        raw_text = f"{company_name}({symbol}) 목표주가 상향 EPS_ACTION_TYP_NM=상향"
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"SRCREQ-UNIT-{symbol}",
            request_params={"symbol": symbol, "company_name": company_name},
            status="FETCHED",
            canonical_url=f"https://example.com/companyguide/A{symbol}",
            official_document_id=f"companyguide:{symbol}",
            published_at=as_of_date.isoformat(),
            available_at=as_of_date.isoformat(),
            fetched_at=as_of_date.isoformat(),
            content_hash="unit-content-hash",
            raw_text=raw_text,
            structured_payload={
                "symbol": symbol,
                "company_name": company_name,
                "EPS_ACTION_TYP_NM": "상향",
            },
            provider_request_id=f"SRCREQ-UNIT-{symbol}",
        )


class _ScoreBlockedLiveConnector:
    provider_name = "CompanyGuide"
    source_class = "CompanyGuide"

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        raw_text = f"{company_name}({symbol}) OpenDART company profile"
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"SRCREQ-BLOCKED-{symbol}",
            request_params={"symbol": symbol, "company_name": company_name},
            status="FETCHED",
            canonical_url=f"https://wcomp.fnguide.com/company/{symbol}",
            official_document_id=f"companyguide:coverage:{symbol}",
            published_at=as_of_date.isoformat(),
            available_at=as_of_date.isoformat(),
            fetched_at=as_of_date.isoformat(),
            content_hash="unit-score-blocked-content-hash",
            raw_text=raw_text,
            structured_payload={
                "symbol": symbol,
                "company_name": company_name,
                "provider": self.provider_name,
                "score_usage": "provider_coverage_only_until_numeric_revision_parser_accepts_claims",
            },
            provider_request_id=f"SRCREQ-BLOCKED-{symbol}",
        )


def _companyguide_consensus_html(*, date_text: str = "2026/07/01") -> str:
    return f"""
    <html><body>
      <h2>투자의견 컨센서스</h2>
      <span class="date">[{date_text}]</span>
      <table>
        <thead>
          <tr>
            <th>투자의견</th>
            <th>목표주가</th>
            <th>EPS</th>
            <th>PER</th>
            <th>추정기관수</th>
          </tr>
        </thead>
        <tbody>
          <tr class="rwc_g tr_h68">
            <td class="clf c">4.0</td>
            <td class="c">501,458</td>
            <td class="c">45,534</td>
            <td class="c">6.9</td>
            <td class="cle c">24</td>
          </tr>
        </tbody>
      </table>
    </body></html>
    """


class _RecordingLiveConnector:
    def __init__(
        self,
        *,
        provider_name: str,
        source_class: str,
        url: str,
        raw_text: str,
        calls: list[str],
        status: str = "FETCHED",
        provider_error: str | None = None,
    ) -> None:
        self.provider_name = provider_name
        self.source_class = source_class
        self._url = url
        self._raw_text = raw_text
        self._calls = calls
        self._status = status
        self._provider_error = provider_error

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        self._calls.append(self.provider_name)
        request_id = f"SRCREQ-{self.provider_name}-{symbol}"
        if self._status != "FETCHED":
            return SourceFetchResult(
                provider_name=self.provider_name,
                source_class=self.source_class,
                mode=mode,
                request_id=request_id,
                request_params={"symbol": symbol, "company_name": company_name},
                status=self._status,
                fetched_at=as_of_date.isoformat(),
                provider_error=self._provider_error,
                provider_request_id=request_id,
            )
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=request_id,
            request_params={"symbol": symbol, "company_name": company_name},
            status="FETCHED",
            canonical_url=self._url,
            official_document_id=f"{self.provider_name}:{symbol}",
            published_at=as_of_date.isoformat(),
            available_at=as_of_date.isoformat(),
            fetched_at=as_of_date.isoformat(),
            content_hash=f"unit-{self.provider_name}-{symbol}",
            raw_text=self._raw_text,
            structured_payload={
                "symbol": symbol,
                "company_name": company_name,
                "provider": self.provider_name,
            },
            provider_request_id=request_id,
        )


class _FakeResponse:
    def __init__(self, *, json_payload=None, text_payload="", content_payload=None) -> None:
        self._json_payload = json_payload
        self.text = text_payload
        self.content = content_payload if content_payload is not None else text_payload.encode("utf-8")

    def raise_for_status(self) -> None:
        return None

    def json(self):
        if self._json_payload is None:
            raise ValueError("no json payload")
        return self._json_payload


if __name__ == "__main__":
    unittest.main()
