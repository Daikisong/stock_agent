import time
import unittest
from unittest.mock import patch

from e2r.sources.http_client import HttpClient
from e2r.sources.rate_limit import RateLimiter, SourceRateLimit
from e2r.sources.source_errors import SourceRequest


class RateLimitTests(unittest.TestCase):
    def test_rate_limiter_blocks_after_max_requests_per_day(self):
        limiter = RateLimiter((SourceRateLimit("opendart", max_requests_per_day=1),))
        request = _opendart_request()

        with patch("urllib.request.urlopen", return_value=_FakeResponse("{}")):
            client = HttpClient(rate_limiter=limiter)
            first = client.get_text(request)
            second = client.get_text(request)

        self.assertTrue(first.ok)
        self.assertFalse(second.ok)
        self.assertEqual(second.error, "rate_limit_exceeded")
        self.assertEqual(client.stats.rate_limit_skips, 1)
        self.assertEqual(client.stats.actual_http_requests_by_source["opendart"], 1)

    def test_rate_limiter_enforces_min_interval_with_sleep_hook(self):
        sleeps = []
        limiter = RateLimiter(
            (
                SourceRateLimit(
                    "opendart",
                    max_requests_per_day=5,
                    min_interval_seconds=0.5,
                    max_concurrency=1,
                ),
            ),
            now_hook=lambda: 100.0,
        )
        client = HttpClient(rate_limiter=limiter, sleep_hook=sleeps.append)

        with patch("urllib.request.urlopen", return_value=_FakeResponse("{}")):
            client.get_text(_opendart_request())
            client.get_text(_opendart_request())

        self.assertEqual(sleeps, [0.5])
        self.assertEqual(client.stats.rate_limit_waits, 1)
        self.assertEqual(client.stats.logical_queries_by_source["opendart"], 2)
        self.assertEqual(client.stats.max_concurrency_used_by_source["opendart"], 1)

    def test_source_rate_limit_defaults_to_serial_concurrency(self):
        limit = SourceRateLimit("naver_search")

        self.assertEqual(limit.max_concurrency, 1)

    def test_source_rate_limit_default_has_no_daily_cap(self):
        limiter = RateLimiter((SourceRateLimit("naver_search"),))

        self.assertTrue(limiter.acquire("naver_search").allowed)
        limiter.release("naver_search")
        self.assertTrue(limiter.acquire("naver_search").allowed)

    def test_http_client_hard_timeout_returns_failure(self):
        def slow_urlopen(*args, **kwargs):
            time.sleep(1.0)
            return _FakeResponse("{}")

        with patch("urllib.request.urlopen", side_effect=slow_urlopen):
            result = HttpClient(timeout_seconds=0.05, retries=0).get_text(_opendart_request())

        self.assertFalse(result.ok)
        self.assertTrue(result.error.startswith("TimeoutError:http_hard_timeout"))


def _opendart_request():
    return SourceRequest(
        method="GET",
        url="https://opendart.fss.or.kr/api/list.json",
        params={"bgn_de": "20240521", "end_de": "20240521"},
        fixture_mode=False,
        credential_name="OPENDART_API_KEY",
    )


class _FakeResponse:
    status = 200

    def __init__(self, text):
        self._text = text

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self):
        return self._text.encode("utf-8")


if __name__ == "__main__":
    unittest.main()
