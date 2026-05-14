from datetime import date, datetime
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from e2r.cheap_scan import DataGoKrFSCConnector, KoreaCheapScanSources
from e2r.cli.review_korea_run import build_review_summary, render_review_summary
from e2r.models import DisclosureEvent, Stage
from e2r.pipeline.korea_live_lite import (
    KoreaLiveLiteBudget,
    KoreaLiveLiteConfig,
    KoreaLiveLiteRunner,
    build_opendart_date_range_requests,
    plan_opendart_detail_fetches,
)
from e2r.research.search_provider import EmptySearchProvider, FixtureSearchProvider, SearchResult
from e2r.sources import KINDConnector, KRXConnector, OpenDARTConnector
from e2r.sources.http_client import HttpClientStats, HttpResult


AS_OF = date(2024, 5, 21)


class KoreaLiveLiteTests(unittest.TestCase):
    def test_live_lite_config_validates_budgets(self):
        with self.assertRaises(ValueError):
            KoreaLiveLiteBudget(max_opendart_calls_per_day=-1)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, top_candidates=0)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, allow_parallel_live_requests=False, max_global_live_workers=2)

    def test_live_lite_tiny_smoke_preset_uses_safe_budget_values(self):
        config = KoreaLiveLiteConfig.smoke_preset("tiny", as_of_date=AS_OF)

        self.assertEqual(config.universe_limit, 50)
        self.assertEqual(config.budget.max_naver_search_calls_per_day, 50)
        self.assertEqual(config.budget.max_symbols_for_event_search, 5)
        self.assertEqual(config.budget.max_symbols_for_deep_research, 1)
        self.assertFalse(config.allow_parallel_live_requests)
        self.assertEqual(config.max_global_live_workers, 1)
        self.assertEqual(config.live_smoke_preset_used, "tiny")

    def test_missing_credentials_do_not_crash_and_mark_fixture_fallback(self):
        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", {}, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertTrue(result.run_log.effective_fixture_mode)
        self.assertIn("OPENDART_API_KEY", result.run_log.missing_credentials)
        self.assertIn("NAVER_CLIENT_ID", result.run_log.missing_credentials)

    def test_fixture_live_lite_run_writes_candidate_evidence_brief_and_log(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

            self.assertTrue(result.candidates_path.exists())
            self.assertTrue(result.evidence_path.exists())
            self.assertTrue(result.brief_path.exists())
            self.assertTrue(result.run_log_path.exists())
            self.assertTrue(result.calibration_json_path.exists())
            self.assertTrue(result.calibration_md_path.exists())
            self.assertIn("E2R Morning Brief", result.brief_path.read_text(encoding="utf-8"))
            candidates_json = json.loads(result.candidates_path.read_text(encoding="utf-8"))
            calibration_json = json.loads(result.calibration_json_path.read_text(encoding="utf-8"))
            run_log_json = json.loads(result.run_log_path.read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(candidates_json["candidates"]), 1)
            self.assertIn("near_miss_top_50", calibration_json)
            self.assertIn("diagnostic_reason_distribution", calibration_json)
            self.assertGreaterEqual(len(run_log_json["planned_opendart_detail_requests"]), 1)
            self.assertIn("audit_findings", run_log_json)
            self.assertIn("rate_limit_waits", run_log_json)
            self.assertIn("rate_limit_skips", run_log_json)
            self.assertIn("actual_http_requests_by_source", run_log_json)
            self.assertIn("logical_queries_by_source", run_log_json)
            self.assertIn("max_concurrency_used_by_source", run_log_json)
            self.assertEqual(run_log_json["source_modes"]["stock_issuance"], "disabled_optional")
            self.assertEqual(run_log_json["source_modes"]["krx_openapi"], "disabled_optional")
            self.assertTrue(
                any(item["source_name"] == "data_go_kr_fsc_stock_issuance" for item in run_log_json["source_license_metadata"])
            )
            self.assertTrue(any(item["source_name"] == "krx_openapi" for item in run_log_json["source_license_metadata"]))

    def test_live_lite_works_without_stock_issuance_api_and_detects_dilution_from_opendart(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    enable_stock_issuance_source=False,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        candidate = _candidate(result, "666666")
        self.assertIn("DISC_RIGHTS_OFFERING", candidate.reason_codes)
        self.assertGreater(candidate.risk_event_score, 0)
        self.assertEqual(result.run_log.source_modes["stock_issuance"], "disabled_optional")
        self.assertIn("stock issuance API is disabled_optional", " ".join(result.run_log.notes))

    def test_review_cli_summarizes_fixture_run(self):
        with tempfile.TemporaryDirectory() as output_dir:
            KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

            summary = build_review_summary(output_dir, AS_OF.isoformat())
            rendered = render_review_summary(summary)

        self.assertGreater(summary.total_candidates, 0)
        self.assertIn("opendart", summary.source_modes)
        self.assertIn("total candidates", rendered)
        self.assertIn("manual review required", rendered)

    def test_opendart_disclosure_collection_is_date_based_not_per_symbol(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertGreater(result.cheap_scan.instruments_scanned, 1)
        self.assertEqual(result.run_log.source_call_counts["opendart_disclosure_date_range"], 1)
        self.assertEqual(result.run_log.source_call_counts["opendart_symbol_disclosure_calls"], 0)

    def test_date_based_disclosure_collection_contains_multiple_symbols(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        disclosure_symbols = {item.symbol for item in result.evidence if item.source_type == "disclosure"}
        self.assertGreaterEqual(len(disclosure_symbols), 3)
        self.assertIn("111111", disclosure_symbols)
        self.assertIn("222222", disclosure_symbols)

    def test_no_disclosure_instrument_is_still_evaluated_by_price_sensor(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        candidate = _candidate(result, "444444")
        self.assertEqual(candidate.recommended_next_layer.value, "event_search")
        self.assertIn("PRICE_VOLUME_SPIKE", candidate.reason_codes)
        self.assertFalse(any(code.startswith("DISC_") for code in candidate.reason_codes))
        self.assertEqual(candidate.evidence_ids, ())

    def test_no_disclosure_instrument_can_become_event_search_via_financial_rules(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        candidate = _candidate(result, "777777")
        self.assertEqual(candidate.recommended_next_layer.value, "event_search")
        self.assertIn("FIN_OP_TURNAROUND", candidate.reason_codes)
        self.assertIn("FIN_FCF_TURNAROUND", candidate.reason_codes)
        self.assertFalse(any(code.startswith("DISC_") for code in candidate.reason_codes))

    def test_page_request_builder_emits_page_metadata(self):
        requests = build_opendart_date_range_requests(
            date(2024, 5, 20),
            date(2024, 5, 21),
            AS_OF,
            page_count=50,
            max_pages=3,
        )

        self.assertEqual([item.params["page_no"] for item in requests], [1, 2, 3])
        self.assertTrue(all(item.params["page_count"] == 50 for item in requests))
        self.assertTrue(all(item.params["bgn_de"] == "20240520" for item in requests))
        self.assertTrue(all(item.params["end_de"] == "20240521" for item in requests))

    def test_opendart_detail_fetch_requests_are_planned_only_for_watch_disclosures(self):
        watch = _disclosure("111111", "단일판매·공급계약체결", "202405210001")
        ignored = _disclosure("222222", "투자설명서", "202405210002")

        requests = plan_opendart_detail_fetches((watch, ignored), AS_OF)

        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].url, "https://opendart.fss.or.kr/api/document.xml")
        self.assertEqual(requests[0].params["rcept_no"], "202405210001")
        self.assertEqual(requests[0].params["symbol"], "111111")
        self.assertNotIn("crtfc_key", requests[0].params)

    def test_opendart_detail_fetch_executes_with_cap_and_writes_text_cache(self):
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
        http_client = MockHttpClient(
            json_by_url_token={
                "opendart": {
                    "total_page": 1,
                    "list": [
                        {
                            "stock_code": "111111",
                            "corp_name": "한전변압기",
                            "report_nm": "단일판매·공급계약체결",
                            "rcept_no": "202405210091",
                            "rcept_dt": "20240521",
                        },
                        {
                            "stock_code": "222222",
                            "corp_name": "케이전력",
                            "report_nm": "신규시설투자",
                            "rcept_no": "202405210092",
                            "rcept_dt": "20240521",
                        },
                    ],
                }
            },
            text_by_url_token={"202405210091": detail_xml, "202405210092": detail_xml},
        )
        env = {"OPENDART_API_KEY": "OPENDART_SECRET"}

        with tempfile.TemporaryDirectory() as output_dir, tempfile.TemporaryDirectory() as cache_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    cache_directory=cache_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(max_opendart_detail_fetches_per_run=1),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

            detail_cache_dir = Path(cache_dir) / "opendart_detail" / AS_OF.isoformat()
            self.assertTrue((detail_cache_dir / "202405210091.xml").exists())
            self.assertTrue((detail_cache_dir / "202405210091.txt").exists())

        self.assertEqual(len(result.run_log.executed_opendart_detail_requests), 1)
        self.assertEqual(result.run_log.source_call_counts["opendart_detail_fetches"], 1)
        detail_evidence = [item for item in result.evidence if item.source_name == "OpenDART detail"]
        self.assertEqual(len(detail_evidence), 1)
        self.assertEqual(detail_evidence[0].parsed_fields["contract_amount_to_prior_sales"], 0.45)
        self.assertGreaterEqual(detail_evidence[0].confidence, 0.7)

    def test_event_and_deep_research_symbol_budgets_are_respected(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=1,
                        max_symbols_for_deep_research=0,
                        max_naver_search_calls_per_day=1,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        skipped_reasons = {item.reason for item in result.run_log.skipped_candidates}
        self.assertIn("deep_research_symbol_budget_exhausted", skipped_reasons)
        self.assertIn("event_search_symbol_budget_exhausted", skipped_reasons)
        self.assertLessEqual(result.run_log.source_call_counts["naver_search_queries"], 1)
        self.assertTrue(result.run_log.skipped_queries)
        self.assertLessEqual(len(result.web_results), 1)

    def test_stage_3_green_requires_cross_evidence_in_live_lite(self):
        url = "https://ssl.pstatic.net/imgstock/upload/research/company/price_report.pdf"
        provider = FixtureSearchProvider(
            results_by_query={
                "가격만강세 수주잔고": (
                    SearchResult(
                        title="가격만강세 줄을 서시오",
                        url=url,
                        source="FixtureBroker",
                        published_at=datetime(2024, 5, 21, 8),
                        query="가격만강세 수주잔고",
                        rank=1,
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            }
        )
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                        max_naver_search_calls_per_day=100,
                    ),
                    browser_provider=provider,
                    free_search_provider=EmptySearchProvider(),
                    fixture_text_by_url={url: STRONG_SINGLE_REPORT_TEXT},
                )
            )

        stage_by_symbol = {item.stage.symbol: item.stage for item in result.web_results}
        self.assertEqual(stage_by_symbol["444444"].stage, Stage.STAGE_3_YELLOW)
        self.assertIn("at least two independent evidence types", " ".join(stage_by_symbol["444444"].stage_reason))

    def test_targeted_smoke_without_evidence_is_not_production_or_green(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    targeted_smoke_enabled=True,
                    targeted_smoke_symbol="009999",
                    targeted_smoke_company="스모크테스트",
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=20,
                        max_symbols_for_deep_research=20,
                        max_naver_search_calls_per_day=100,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )
            brief_text = result.brief_path.read_text(encoding="utf-8")

        self.assertFalse(any(item.candidate_source_path == "targeted_smoke" for item in result.candidates))
        self.assertTrue(result.run_log.targeted_smoke_results)
        smoke = next(item for item in result.run_log.targeted_smoke_results if item["symbol"] == "009999")
        self.assertEqual(smoke["status"], "insufficient_evidence")
        self.assertFalse(smoke["production_candidate"])
        self.assertNotEqual(smoke["stage"], Stage.STAGE_3_GREEN.value)
        self.assertNotIn("스모크테스트", brief_text)

    def test_report_radar_candidate_path_respects_budget_and_records_source_path(self):
        url = "https://ssl.pstatic.net/imgstock/upload/research/company/radar_report.pdf"
        provider = FixtureSearchProvider(
            results_by_query={
                "가격만강세 목표주가 상향 EPS 상향 PDF": (
                    SearchResult(
                        title="가격만강세 컨센서스 상회 Review PDF",
                        url=url,
                        snippet="목표주가 상향 EPS 상향 수주잔고 OPM",
                        source="FixtureBroker",
                        published_at=datetime(2024, 5, 21, 8),
                        query="가격만강세 목표주가 상향 EPS 상향 PDF",
                        rank=1,
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.8,
                    ),
                )
            }
        )
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    report_radar_enabled=True,
                    report_radar_universe_limit=1,
                    active_watchlist_symbols=("444444",),
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=20,
                        max_symbols_for_deep_research=20,
                        max_naver_search_calls_per_day=100,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=provider,
                )
            )

        self.assertTrue(result.run_log.report_radar_candidates)
        self.assertTrue(any(item.candidate_source_path == "report_radar" for item in result.candidates))
        self.assertLessEqual(result.run_log.source_call_counts["naver_search_queries"], 100)

    def test_stage_3_green_is_blocked_by_hard_parser_audit_finding(self):
        url = "https://ssl.pstatic.net/imgstock/upload/research/company/kepower_report.pdf"
        provider = FixtureSearchProvider(
            results_by_query={
                "케이전력 장기공급계약 매출액 대비": (
                    SearchResult(
                        title="케이전력 Review PDF",
                        url=url,
                        source="FixtureBroker",
                        published_at=datetime(2024, 5, 21, 8),
                        query="케이전력 장기공급계약 매출액 대비",
                        rank=1,
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            }
        )
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                        max_naver_search_calls_per_day=100,
                    ),
                    browser_provider=provider,
                    free_search_provider=EmptySearchProvider(),
                    fixture_text_by_url={url: IMPOSSIBLE_CONTRACT_REPORT_TEXT},
                )
            )

        stage_by_symbol = {item.stage.symbol: item.stage for item in result.web_results}
        self.assertEqual(stage_by_symbol["222222"].stage, Stage.STAGE_3_YELLOW)
        self.assertEqual(stage_by_symbol["222222"].grade, "parser-audit-blocked")
        self.assertTrue(any(item.code == "contract_ratio_too_high" for item in result.run_log.audit_findings))
        self.assertIn("manual_review_required", " ".join(result.run_log.notes))

    def test_hard_risk_candidate_is_not_escalated_to_green(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        hard_risk = next(candidate for candidate in result.candidates if candidate.symbol == "555555")
        self.assertEqual(hard_risk.recommended_next_layer.value, "none")
        self.assertNotIn("555555", {item.stage.symbol for item in result.web_results})

    def test_mocked_opendart_live_pagination_flows_into_disclosure_evidence(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "page_no=1": {
                    "total_page": 2,
                    "list": [
                        {
                            "stock_code": "111111",
                            "corp_name": "한전변압기",
                            "report_nm": "단일판매·공급계약체결",
                            "rcept_no": "202405210091",
                            "rcept_dt": "20240521",
                        }
                    ],
                },
                "page_no=2": {
                    "total_page": 2,
                    "list": [
                        {
                            "stock_code": "222222",
                            "corp_name": "케이전력",
                            "report_nm": "신규시설투자",
                            "rcept_no": "202405210092",
                            "rcept_dt": "20240521",
                        }
                    ],
                },
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        disclosure_symbols = {item.symbol for item in result.evidence if item.source_type == "disclosure"}
        self.assertIn("111111", disclosure_symbols)
        self.assertIn("222222", disclosure_symbols)
        self.assertEqual(result.run_log.source_modes["opendart"], "live_executed")
        self.assertGreaterEqual(result.run_log.live_requests_executed, 2)
        self.assertGreaterEqual(result.run_log.cache_writes, 2)

    def test_mocked_naver_live_search_flows_into_news_evidence(self):
        url = "https://news.example.com/live-naver-contract"
        http_client = MockHttpClient(
            json_by_url_token={
                "opendart": {"total_page": 1, "list": []},
                "openapi.naver.com": {
                    "items": [
                        {
                            "title": "가격만강세 수주잔고 공급부족",
                            "originallink": url,
                            "link": url,
                            "description": "가격만강세 수주잔고와 공급부족 뉴스",
                            "pubDate": "Tue, 21 May 2024 08:00:00 +0900",
                        }
                    ]
                },
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                        max_naver_search_calls_per_day=20,
                    ),
                    browser_provider=EmptySearchProvider(),
                    fixture_text_by_url={url: "가격만강세 수주잔고 공급부족과 판가 상승이 보도됐다."},
                )
            )

        self.assertEqual(result.run_log.source_modes["naver_search"], "live_executed")
        self.assertTrue(any(item.source_type == "news" for item in result.evidence))

    def test_request_only_sources_are_marked_when_live_credentials_exist(self):
        http_client = MockHttpClient(json_by_url_token={"opendart": {"total_page": 1, "list": []}})
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "KRX_OPENAPI_KEY": "KRX_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_modes["krx"], "request_only")
        self.assertEqual(result.run_log.source_modes["krx_openapi"], "disabled_optional")
        self.assertEqual(result.run_log.source_modes["data_go_kr"], "request_only")
        self.assertIn("krx", result.run_log.request_only_sources)
        self.assertIn("data_go_kr", result.run_log.request_only_sources)
        self.assertNotIn("krx_openapi", result.run_log.request_only_sources)

    def test_krx_openapi_request_only_when_explicitly_enabled(self):
        http_client = MockHttpClient(json_by_url_token={"opendart": {"total_page": 1, "list": []}})
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "KRX_OPENAPI_KEY": "KRX_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    enable_krx_openapi_source=True,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_modes["krx_openapi"], "request_only")
        self.assertIn("krx_openapi", result.run_log.request_only_sources)

    def test_mocked_data_go_live_listed_items_and_prices_feed_cheap_scan(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "opendart": {"total_page": 1, "list": []},
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(
                        max_data_go_kr_calls_per_day=10,
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        candidate = _candidate(result, "999999")
        self.assertEqual(candidate.company_name, "라이브전력")
        self.assertEqual(candidate.recommended_next_layer.value, "event_search")
        self.assertIn("PRICE_VOLUME_SPIKE", candidate.reason_codes)
        self.assertEqual(result.run_log.source_modes["data_go_kr"], "live_executed")
        self.assertEqual(result.run_log.source_call_counts["data_go_kr_calls"], 2)
        self.assertNotIn("data_go_kr", result.run_log.request_only_sources)

    def test_live_lite_can_run_with_data_go_v2_endpoint_config(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "opendart": {"total_page": 1, "list": []},
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }
        sources = KoreaCheapScanSources(
            krx=KRXConnector(),
            opendart=OpenDARTConnector(),
            kind=KINDConnector(),
            fsc=DataGoKrFSCConnector(
                financial_info_service_path="GetFinaStatInfoService_V2/getSummFinaStat_V2",
                disclosure_info_service_path="GetDiscInfoService_V2/getDiviDiscInfo_V2",
                corp_basic_info_service_path="GetCorpBasicInfoService_V2/getCorpOutline_V2",
            ),
        )

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    sources=sources,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(max_data_go_kr_calls_per_day=10),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_modes["data_go_kr"], "live_executed")
        self.assertEqual(result.run_log.source_modes["stock_issuance"], "disabled_optional")

    def test_data_go_live_budget_is_respected_and_falls_back_before_calls(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "opendart": {"total_page": 1, "list": []},
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(max_data_go_kr_calls_per_day=1),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_modes["data_go_kr"], "fallback")
        self.assertEqual(result.run_log.fallback_reasons["data_go_kr"], "data_go_kr_budget_too_low_for_universe_and_price")
        self.assertLessEqual(result.run_log.source_call_counts["data_go_kr_calls"], 1)
        self.assertFalse(any("GetKrxListedInfoService" in item.url for item in http_client.requests))

    def test_data_go_live_failure_falls_back_without_logging_key(self):
        http_client = MockHttpClient(json_by_url_token={"opendart": {"total_page": 1, "list": []}})
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )
            run_log_text = result.run_log_path.read_text(encoding="utf-8")

        self.assertEqual(result.run_log.source_modes["data_go_kr"], "fallback")
        self.assertEqual(result.run_log.fallback_reasons["data_go_kr"], "data_go_kr_listed_items_failed")
        self.assertGreaterEqual(result.run_log.live_requests_failed, 1)
        self.assertNotIn("DATA_SECRET", run_log_text)

    def test_api_keys_are_not_written_to_run_log(self):
        http_client = MockHttpClient(json_by_url_token={"opendart": {"total_page": 1, "list": []}})
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )
            run_log_text = result.run_log_path.read_text(encoding="utf-8")

        self.assertNotIn("OPENDART_SECRET", run_log_text)
        self.assertNotIn("NAVER_SECRET", run_log_text)
        self.assertNotIn("DATA_SECRET", run_log_text)


STRONG_SINGLE_REPORT_TEXT = """
발행일 2024.05.21
증권사: FixtureBroker
애널리스트: Fixture Analyst
제목: 가격만강세 줄을 서시오
현재가 8,100원
목표주가 18,000원
목표주가 상향 60%
상승여력 120%
FY1 매출액 3,300,000 영업이익 620,000 EPS 13,500
FY2 매출액 3,800,000 영업이익 720,000 EPS 15,800
PER 4.0배
PBR 0.8배
ROE 28%
OPM 22.0%
영업이익 YoY 300%
EPS YoY 260%
FCF 증가율 220%
EPS 상향 55%
영업이익 추정치 상향 50%
FCF 질 점수 95
수주잔고 5,000,000
신규수주 2,000,000
수주잔고/매출 220%
계약기간 72개월
계약 매출액 대비 80%
선수금 있음
해지 불가
사상 최대 수주잔고
CAPA 증가율 45%
CAPA utilization 98%
CAPA 선점 3년
CAPA 부족으로 리드타임 24개월 이상이다.
ASP YoY 25%
판가 전가 확인
구조적 공급부족이 지속된다.
멀티플 상향과 리레이팅 구간이다.
OPM 개선폭 12%
CAPEX/매출 20%
투자포인트: 수주잔고 확대|마진 개선|북미 전력망 병목
리스크: 증설 지연|원가 변동
"""

IMPOSSIBLE_CONTRACT_REPORT_TEXT = STRONG_SINGLE_REPORT_TEXT.replace("가격만강세", "케이전력").replace("계약 매출액 대비 80%", "계약 매출액 대비 600%")

DATA_GO_LISTED_ITEMS_PAYLOAD = {
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "basDt": "20240521",
                        "srtnCd": "999999",
                        "isinCd": "KR7999990000",
                        "itmsNm": "라이브전력",
                        "corpNm": "라이브전력",
                        "mrktCtg": "KOSDAQ",
                    }
                ]
            },
            "totalCount": 1,
            "numOfRows": 1000,
            "pageNo": 1,
        }
    }
}

DATA_GO_STOCK_PRICE_PAYLOAD = {
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "basDt": "20240301",
                        "srtnCd": "999999",
                        "itmsNm": "라이브전력",
                        "mkp": "10000",
                        "hipr": "11000",
                        "lopr": "9000",
                        "clpr": "10000",
                        "trqu": "10000",
                        "trPrc": "100000000",
                        "mrktTotAmt": "100000000000",
                    },
                    {
                        "basDt": "20240521",
                        "srtnCd": "999999",
                        "itmsNm": "라이브전력",
                        "mkp": "15000",
                        "hipr": "16200",
                        "lopr": "14900",
                        "clpr": "16000",
                        "trqu": "60000",
                        "trPrc": "900000000",
                        "mrktTotAmt": "160000000000",
                    },
                ]
            },
            "totalCount": 2,
            "numOfRows": 1000,
            "pageNo": 1,
        }
    }
}

def _candidate(result, symbol):
    for candidate in result.candidates:
        if candidate.symbol == symbol:
            return candidate
    raise AssertionError(f"candidate {symbol} not found")


def _disclosure(symbol, title, rcept_no):
    timestamp = datetime(2024, 5, 21, 9)
    return DisclosureEvent(
        symbol=symbol,
        source="OpenDART",
        report_type=title,
        title=title,
        published_at=timestamp,
        observed_at=timestamp,
        available_at=timestamp,
        as_of_date=AS_OF,
        rcept_no=rcept_no,
        raw_text=title,
        parsed_fields={},
    )


class MockHttpClient:
    def __init__(self, json_by_url_token, text_by_url_token=None):
        self.json_by_url_token = dict(json_by_url_token)
        self.text_by_url_token = dict(text_by_url_token or {})
        self.stats = HttpClientStats()
        self.requests = []

    def get_json(self, request, *, cache_path=None):
        self.requests.append(request)
        url = request.url + "?" + "&".join(f"{key}={value}" for key, value in request.params.items())
        for token, payload in self.json_by_url_token.items():
            if token in url:
                self.stats.live_requests_executed += 1
                if cache_path is not None:
                    self.stats.cache_writes += 1
                return HttpResult(ok=True, status_code=200, json_data=payload, text=json.dumps(payload), cache_path=str(cache_path) if cache_path else None)
        self.stats.live_requests_failed += 1
        return HttpResult(ok=False, error="mock_response_not_found")

    def get_text(self, request, *, cache_path=None):
        self.requests.append(request)
        url = request.url + "?" + "&".join(f"{key}={value}" for key, value in request.params.items())
        for token, text in self.text_by_url_token.items():
            if token in url:
                self.stats.live_requests_executed += 1
                if cache_path is not None:
                    path = Path(cache_path)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(text, encoding="utf-8")
                    self.stats.cache_writes += 1
                return HttpResult(ok=True, status_code=200, text=text, cache_path=str(cache_path) if cache_path else None)
        self.stats.live_requests_failed += 1
        return HttpResult(ok=False, error="mock_text_response_not_found")


if __name__ == "__main__":
    unittest.main()
