from datetime import date, datetime
import json
import tempfile
import unittest
from unittest.mock import patch

from e2r.models import Stage
from e2r.pipeline.korea_live_lite import (
    KoreaLiveLiteBudget,
    KoreaLiveLiteConfig,
    KoreaLiveLiteRunner,
    build_opendart_date_range_requests,
)
from e2r.research.search_provider import EmptySearchProvider, FixtureSearchProvider, SearchResult
from e2r.sources.http_client import HttpClientStats, HttpResult


AS_OF = date(2024, 5, 21)


class KoreaLiveLiteTests(unittest.TestCase):
    def test_live_lite_config_validates_budgets(self):
        with self.assertRaises(ValueError):
            KoreaLiveLiteBudget(max_opendart_calls_per_day=-1)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, top_candidates=0)

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
            self.assertIn("E2R Morning Brief", result.brief_path.read_text(encoding="utf-8"))
            candidates_json = json.loads(result.candidates_path.read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(candidates_json["candidates"]), 1)

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
        self.assertEqual(result.run_log.source_modes["data_go_kr"], "request_only")
        self.assertIn("krx", result.run_log.request_only_sources)
        self.assertIn("data_go_kr", result.run_log.request_only_sources)

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

def _candidate(result, symbol):
    for candidate in result.candidates:
        if candidate.symbol == symbol:
            return candidate
    raise AssertionError(f"candidate {symbol} not found")


class MockHttpClient:
    def __init__(self, json_by_url_token):
        self.json_by_url_token = dict(json_by_url_token)
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


if __name__ == "__main__":
    unittest.main()
