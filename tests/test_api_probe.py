from datetime import date
import json
import tempfile
import unittest
from unittest.mock import patch

from e2r.cli.probe_korea_apis import build_arg_parser, config_from_args
from e2r.probe import APIProbeConfig, APIProbeRunner, compare_expected_fields, profile_payload
from e2r.sources.http_client import HttpClientStats, HttpResult


AS_OF = date(2024, 5, 14)


class APIProbeTests(unittest.TestCase):
    def test_probe_runner_stores_raw_response_files(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = APIProbeRunner().run(APIProbeConfig(as_of_date=AS_OF, output_directory=output_dir))

            raw_dir = result.output_directory / "raw"
            self.assertTrue((raw_dir / "opendart_list.json").exists())
            self.assertTrue((raw_dir / "data_go_kr_stock_prices.json").exists())
            self.assertTrue(result.schema_summary_json_path.exists())
            self.assertTrue(result.schema_summary_md_path.exists())
            self.assertTrue(result.normalizer_report_json_path.exists())
            self.assertTrue(result.normalizer_report_md_path.exists())
            self.assertTrue(result.run_log_path.exists())
            self.assertEqual(result.run_log.requests_succeeded, len(result.raw_responses))

    def test_schema_profiler_extracts_top_level_keys_and_item_fields(self):
        profile = profile_payload("data_go_kr_stock_prices", STOCK_PRICE_PAYLOAD)
        field_names = {field.name for field in profile.fields}

        self.assertEqual(profile.top_level_keys, ("response",))
        self.assertEqual(profile.selected_item_path, "response.body.items.item")
        self.assertIn("basDt", field_names)
        self.assertIn("clpr", field_names)
        self.assertEqual(profile.expected_field_comparison["missing_expected_fields"], [])
        self.assertIn("unexpected_fields", profile.expected_field_comparison)

    def test_expected_field_comparison_detects_missing_fields(self):
        comparison = compare_expected_fields("data_go_kr_stock_prices", {"basDt", "srtnCd"})

        self.assertIn("clpr", comparison["missing_expected_fields"])
        self.assertIn("basDt", comparison["present_expected_fields"])

    def test_normalizer_dry_run_succeeds_for_mocked_stock_price_response(self):
        fixture_payloads = {"data_go_kr_stock_prices": STOCK_PRICE_PAYLOAD}
        with tempfile.TemporaryDirectory() as output_dir:
            result = APIProbeRunner(fixture_payloads=fixture_payloads).run(
                APIProbeConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    probe_opendart=False,
                    probe_naver=False,
                    probe_krx=False,
                )
            )

        report = _normalizer_report(result, "data_go_kr_stock_prices")
        self.assertEqual(report.rows_seen, 1)
        self.assertEqual(report.rows_normalized, 1)
        self.assertEqual(report.failures, 0)

    def test_normalizer_dry_run_reports_failures_without_crashing(self):
        fixture_payloads = {
            "data_go_kr_stock_prices": {
                "response": {"body": {"items": {"item": [{"basDt": "20240514", "srtnCd": ""}]}}}
            }
        }
        with tempfile.TemporaryDirectory() as output_dir:
            result = APIProbeRunner(fixture_payloads=fixture_payloads).run(
                APIProbeConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    probe_opendart=False,
                    probe_naver=False,
                    probe_krx=False,
                )
            )

        report = _normalizer_report(result, "data_go_kr_stock_prices")
        self.assertEqual(report.rows_seen, 1)
        self.assertEqual(report.rows_normalized, 0)
        self.assertGreaterEqual(report.failures, 1)
        self.assertTrue(result.run_log.warnings)

    def test_probe_run_log_does_not_contain_api_keys(self):
        http_client = MockHttpClient(
            {
                "opendart": {"status": "000", "message": "ok", "page_no": 1, "total_count": 0, "total_page": 1, "list": []},
                "openapi.naver.com": {"items": []},
                "apis.data.go.kr": STOCK_PRICE_PAYLOAD,
                "data-dbg.krx.co.kr": {"OutBlock_1": []},
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "KRX_OPENAPI_KEY": "KRX_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = APIProbeRunner(http_client=http_client).run(
                APIProbeConfig(as_of_date=AS_OF, output_directory=output_dir, fixture_mode=False, live_enabled=True)
            )
            run_log_text = result.run_log_path.read_text(encoding="utf-8")

        self.assertNotIn("OPENDART_SECRET", run_log_text)
        self.assertNotIn("NAVER_SECRET", run_log_text)
        self.assertNotIn("DATA_SECRET", run_log_text)
        self.assertNotIn("KRX_SECRET", run_log_text)
        self.assertEqual(result.run_log.requests_failed, 0)

    def test_missing_credentials_skip_source_instead_of_crashing(self):
        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", {}, clear=True):
            result = APIProbeRunner().run(
                APIProbeConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    env_file=None,
                )
            )

        self.assertEqual(result.run_log.requests_attempted, 0)
        self.assertIn("opendart_list", result.run_log.skipped_sources)
        self.assertIn("naver_news", result.run_log.skipped_sources)
        self.assertIn("data_go_kr_stock_prices", result.run_log.skipped_sources)
        self.assertIn("krx_stk_bydd_trd", result.run_log.skipped_sources)
        self.assertEqual(result.run_log.source_modes["opendart_list"], "fallback")
        self.assertEqual(result.run_log.fallback_reasons["opendart_list"], "missing_OPENDART_API_KEY")

    def test_probe_config_can_skip_raw_storage(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = APIProbeRunner().run(
                APIProbeConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    save_raw=False,
                    probe_opendart=False,
                    probe_naver=False,
                    probe_krx=False,
                )
            )

            self.assertFalse((result.output_directory / "raw" / "data_go_kr_stock_prices.json").exists())
            self.assertTrue(result.schema_summary_json_path.exists())
            self.assertTrue(result.normalizer_report_json_path.exists())

    def test_cli_argument_parsing_works(self):
        parser = build_arg_parser()
        args = parser.parse_args(
            [
                "--date",
                "2024-05-14",
                "--live",
                "--sample-symbol",
                "005930",
                "--sample-company",
                "삼성전자",
                "--sample-query",
                "삼성전자 수주잔고",
                "--skip-krx",
                "--max-requests-per-source",
                "2",
                "--no-save-raw",
            ]
        )
        config = config_from_args(args)

        self.assertEqual(config.as_of_date, AS_OF)
        self.assertTrue(config.live_enabled)
        self.assertFalse(config.fixture_mode)
        self.assertEqual(config.sample_company, "삼성전자")
        self.assertEqual(config.sample_query, "삼성전자 수주잔고")
        self.assertFalse(config.probe_krx)
        self.assertEqual(config.max_requests_per_source, 2)
        self.assertFalse(config.save_raw)


STOCK_PRICE_PAYLOAD = {
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "basDt": "20240514",
                        "srtnCd": "005930",
                        "isinCd": "KR7005930003",
                        "itmsNm": "삼성전자",
                        "mrktCtg": "KOSPI",
                        "clpr": "78000",
                        "mkp": "77000",
                        "hipr": "79000",
                        "lopr": "76000",
                        "trqu": "1000000",
                        "trPrc": "78000000000",
                        "mrktTotAmt": "465000000000000",
                    }
                ]
            },
            "totalCount": 1,
        }
    }
}


class MockHttpClient:
    def __init__(self, json_by_url_token):
        self.json_by_url_token = dict(json_by_url_token)
        self.stats = HttpClientStats()
        self.requests = []

    def get_text(self, request):
        self.requests.append(request)
        url = request.url + "?" + "&".join(f"{key}={value}" for key, value in request.params.items())
        for token, payload in self.json_by_url_token.items():
            if token in url:
                self.stats.live_requests_executed += 1
                return HttpResult(ok=True, status_code=200, text=json.dumps(payload, ensure_ascii=False))
        self.stats.live_requests_failed += 1
        return HttpResult(ok=False, error="mock_response_not_found")


def _normalizer_report(result, source_name):
    for report in result.normalizer_reports:
        if report.source_name == source_name:
            return report
    raise AssertionError(f"normalizer report not found: {source_name}")


if __name__ == "__main__":
    unittest.main()
