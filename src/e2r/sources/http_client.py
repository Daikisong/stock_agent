"""Small HTTP execution layer for controlled live-lite source calls."""

from __future__ import annotations

import json
import signal
import threading
import time
import urllib.parse
import urllib.request
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from types import FrameType
from typing import Callable, Iterator

from e2r.sources.rate_limit import RateLimiter, source_name_for_request
from e2r.sources.source_errors import SourceRequest


@dataclass
class HttpClientStats:
    """Mutable counters for live request execution."""

    live_requests_executed: int = 0
    live_requests_failed: int = 0
    cache_hits: int = 0
    cache_writes: int = 0
    rate_limit_waits: int = 0
    rate_limit_skips: int = 0
    actual_http_requests_by_source: dict[str, int] = field(default_factory=dict)
    logical_queries_by_source: dict[str, int] = field(default_factory=dict)
    max_concurrency_used_by_source: dict[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class HttpResult:
    """HTTP execution result that never raises into pipeline code."""

    ok: bool
    status_code: int | None = None
    json_data: object | None = None
    text: str | None = None
    bytes_data: bytes | None = None
    error: str | None = None
    cache_path: str | None = None


class HttpClient:
    """Minimal GET client with timeout, retry, optional sleep, and cache."""

    def __init__(
        self,
        *,
        timeout_seconds: float = 10.0,
        retries: int = 1,
        sleep_seconds: float = 0.0,
        sleep_hook: Callable[[float], None] = time.sleep,
        stats: HttpClientStats | None = None,
        rate_limiter: RateLimiter | None = None,
    ) -> None:
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        if retries < 0:
            raise ValueError("retries must be non-negative")
        if sleep_seconds < 0:
            raise ValueError("sleep_seconds must be non-negative")
        self.timeout_seconds = timeout_seconds
        self.retries = retries
        self.sleep_seconds = sleep_seconds
        self.sleep_hook = sleep_hook
        self.stats = stats or HttpClientStats()
        self.rate_limiter = rate_limiter

    def get_json(self, request: SourceRequest, *, cache_path: str | Path | None = None) -> HttpResult:
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached
        result = self.get_text(request)
        if not result.ok or result.text is None:
            return result
        try:
            payload = json.loads(result.text)
        except json.JSONDecodeError as exc:
            self.stats.live_requests_failed += 1
            return HttpResult(ok=False, status_code=result.status_code, text=result.text, error=f"json_decode_error:{exc}")
        self._write_cache(cache_path, result.text)
        return HttpResult(ok=True, status_code=result.status_code, json_data=payload, text=result.text, cache_path=str(cache_path) if cache_path else None)

    def get_text(self, request: SourceRequest, *, cache_path: str | Path | None = None) -> HttpResult:
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached
        source_name = source_name_for_request(request)
        _increment(self.stats.logical_queries_by_source, source_name)
        if self.rate_limiter is not None:
            decision = self.rate_limiter.acquire(source_name)
            self.stats.max_concurrency_used_by_source.update(self.rate_limiter.max_concurrency_used_by_source())
            if not decision.allowed:
                self.stats.rate_limit_skips += 1
                return HttpResult(ok=False, error=decision.reason or "rate_limit_exceeded")
            if decision.sleep_seconds > 0:
                self.stats.rate_limit_waits += 1
                self.sleep_hook(decision.sleep_seconds)
        last_error: str | None = None
        try:
            for attempt in range(self.retries + 1):
                if self.sleep_seconds and attempt:
                    self.sleep_hook(self.sleep_seconds)
                try:
                    _increment(self.stats.actual_http_requests_by_source, source_name)
                    http_request = urllib.request.Request(_url_with_params(request), headers=dict(request.headers), method=request.method)
                    with _hard_timeout(self.timeout_seconds):
                        with urllib.request.urlopen(http_request, timeout=self.timeout_seconds) as response:  # nosec - live mode is explicit
                            status_code = int(getattr(response, "status", 200))
                            text = response.read().decode("utf-8")
                    self.stats.live_requests_executed += 1
                    self._write_cache(cache_path, text)
                    return HttpResult(ok=True, status_code=status_code, text=text, cache_path=str(cache_path) if cache_path else None)
                except Exception as exc:  # pragma: no cover - real network path is mocked in tests
                    last_error = f"{type(exc).__name__}:{exc}"
            self.stats.live_requests_failed += 1
            return HttpResult(ok=False, error=last_error or "http_request_failed")
        finally:
            if self.rate_limiter is not None:
                self.rate_limiter.release(source_name)
                self.stats.max_concurrency_used_by_source.update(self.rate_limiter.max_concurrency_used_by_source())

    def get_bytes(self, request: SourceRequest, *, cache_path: str | Path | None = None) -> HttpResult:
        cached = self._read_bytes_cache(cache_path)
        if cached is not None:
            return cached
        source_name = source_name_for_request(request)
        _increment(self.stats.logical_queries_by_source, source_name)
        if self.rate_limiter is not None:
            decision = self.rate_limiter.acquire(source_name)
            self.stats.max_concurrency_used_by_source.update(self.rate_limiter.max_concurrency_used_by_source())
            if not decision.allowed:
                self.stats.rate_limit_skips += 1
                return HttpResult(ok=False, error=decision.reason or "rate_limit_exceeded")
            if decision.sleep_seconds > 0:
                self.stats.rate_limit_waits += 1
                self.sleep_hook(decision.sleep_seconds)
        last_error: str | None = None
        try:
            for attempt in range(self.retries + 1):
                if self.sleep_seconds and attempt:
                    self.sleep_hook(self.sleep_seconds)
                try:
                    _increment(self.stats.actual_http_requests_by_source, source_name)
                    http_request = urllib.request.Request(_url_with_params(request), headers=dict(request.headers), method=request.method)
                    with _hard_timeout(self.timeout_seconds):
                        with urllib.request.urlopen(http_request, timeout=self.timeout_seconds) as response:  # nosec - live mode is explicit
                            status_code = int(getattr(response, "status", 200))
                            payload = response.read()
                    self.stats.live_requests_executed += 1
                    self._write_bytes_cache(cache_path, payload)
                    return HttpResult(
                        ok=True,
                        status_code=status_code,
                        bytes_data=payload,
                        cache_path=str(cache_path) if cache_path else None,
                    )
                except Exception as exc:  # pragma: no cover - real network path is mocked in tests
                    last_error = f"{type(exc).__name__}:{exc}"
            self.stats.live_requests_failed += 1
            return HttpResult(ok=False, error=last_error or "http_request_failed")
        finally:
            if self.rate_limiter is not None:
                self.rate_limiter.release(source_name)
                self.stats.max_concurrency_used_by_source.update(self.rate_limiter.max_concurrency_used_by_source())

    def _read_cache(self, cache_path: str | Path | None) -> HttpResult | None:
        if cache_path is None:
            return None
        path = Path(cache_path)
        if not path.exists():
            return None
        text = path.read_text(encoding="utf-8")
        self.stats.cache_hits += 1
        try:
            return HttpResult(ok=True, status_code=200, json_data=json.loads(text), text=text, cache_path=str(path))
        except json.JSONDecodeError:
            return HttpResult(ok=True, status_code=200, text=text, cache_path=str(path))

    def _read_bytes_cache(self, cache_path: str | Path | None) -> HttpResult | None:
        if cache_path is None:
            return None
        path = Path(cache_path)
        if not path.exists():
            return None
        payload = path.read_bytes()
        self.stats.cache_hits += 1
        return HttpResult(ok=True, status_code=200, bytes_data=payload, cache_path=str(path))

    def _write_cache(self, cache_path: str | Path | None, text: str) -> None:
        if cache_path is None:
            return
        path = Path(cache_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        self.stats.cache_writes += 1

    def _write_bytes_cache(self, cache_path: str | Path | None, payload: bytes) -> None:
        if cache_path is None:
            return
        path = Path(cache_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        self.stats.cache_writes += 1


def _url_with_params(request: SourceRequest) -> str:
    params = {key: value for key, value in request.params.items() if key != "as_of_date"}
    if not params:
        return request.url
    separator = "&" if "?" in request.url else "?"
    return f"{request.url}{separator}{urllib.parse.urlencode(params)}"


def _increment(mapping: dict[str, int], key: str, amount: int = 1) -> None:
    mapping[key] = mapping.get(key, 0) + amount


@contextmanager
def _hard_timeout(timeout_seconds: float) -> Iterator[None]:
    if threading.current_thread() is not threading.main_thread() or not hasattr(signal, "SIGALRM"):
        yield
        return

    def _raise_timeout(signum: int, frame: FrameType | None) -> None:
        raise TimeoutError(f"http_hard_timeout:{timeout_seconds:g}s")

    old_handler = signal.getsignal(signal.SIGALRM)
    old_timer = signal.setitimer(signal.ITIMER_REAL, 0.0)
    signal.signal(signal.SIGALRM, _raise_timeout)
    signal.setitimer(signal.ITIMER_REAL, timeout_seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        signal.signal(signal.SIGALRM, old_handler)
        if old_timer[0] > 0:
            signal.setitimer(signal.ITIMER_REAL, old_timer[0], old_timer[1])


__all__ = ["HttpClient", "HttpClientStats", "HttpResult"]
