"""Source-level rate limiting for controlled live source calls."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Callable, Mapping

from e2r.sources.source_errors import SourceRequest


@dataclass(frozen=True)
class SourceRateLimit:
    """Rate and concurrency rules for one source."""

    source_name: str
    max_requests_per_day: int = 1_000
    max_requests_per_second: float | None = None
    min_interval_seconds: float = 0.0
    max_concurrency: int = 1

    def __post_init__(self) -> None:
        if not self.source_name.strip():
            raise ValueError("source_name must be non-empty")
        if self.max_requests_per_day < 0:
            raise ValueError("max_requests_per_day must be non-negative")
        if self.max_requests_per_second is not None and self.max_requests_per_second <= 0:
            raise ValueError("max_requests_per_second must be positive when set")
        if self.min_interval_seconds < 0:
            raise ValueError("min_interval_seconds must be non-negative")
        if self.max_concurrency <= 0:
            raise ValueError("max_concurrency must be positive")

    @property
    def effective_min_interval_seconds(self) -> float:
        if self.max_requests_per_second is None:
            return self.min_interval_seconds
        return max(self.min_interval_seconds, 1.0 / self.max_requests_per_second)


@dataclass
class RateLimitState:
    """Mutable source rate-limit state."""

    requests_today: int = 0
    last_request_at: float | None = None
    in_flight: int = 0
    max_concurrency_used: int = 0


@dataclass(frozen=True)
class RateLimitDecision:
    """Decision before an HTTP request is executed."""

    allowed: bool
    sleep_seconds: float = 0.0
    reason: str | None = None


class RateLimiter:
    """In-memory rate limiter for a single process live-lite run."""

    def __init__(
        self,
        limits: Mapping[str, SourceRateLimit] | tuple[SourceRateLimit, ...] = (),
        *,
        now_hook: Callable[[], float] = time.monotonic,
    ) -> None:
        if isinstance(limits, Mapping):
            self._limits = dict(limits)
        else:
            self._limits = {item.source_name: item for item in limits}
        self._states: dict[str, RateLimitState] = {}
        self._now_hook = now_hook

    def acquire(self, source_name: str) -> RateLimitDecision:
        limit = self._limits.get(source_name)
        if limit is None:
            return RateLimitDecision(allowed=True)
        state = self._states.setdefault(source_name, RateLimitState())
        if state.requests_today >= limit.max_requests_per_day:
            return RateLimitDecision(allowed=False, reason="rate_limit_exceeded")
        if state.in_flight >= limit.max_concurrency:
            return RateLimitDecision(allowed=False, reason="max_concurrency_exceeded")

        now = self._now_hook()
        sleep_seconds = 0.0
        if state.last_request_at is not None:
            elapsed = now - state.last_request_at
            sleep_seconds = max(0.0, limit.effective_min_interval_seconds - elapsed)

        state.in_flight += 1
        state.requests_today += 1
        state.max_concurrency_used = max(state.max_concurrency_used, state.in_flight)
        state.last_request_at = now + sleep_seconds
        return RateLimitDecision(allowed=True, sleep_seconds=round(sleep_seconds, 6))

    def release(self, source_name: str) -> None:
        state = self._states.get(source_name)
        if state is None:
            return
        state.in_flight = max(0, state.in_flight - 1)

    def state_for(self, source_name: str) -> RateLimitState:
        return self._states.setdefault(source_name, RateLimitState())

    def max_concurrency_used_by_source(self) -> dict[str, int]:
        return {source: state.max_concurrency_used for source, state in sorted(self._states.items())}


def source_name_for_request(request: SourceRequest) -> str:
    """Infer source name from request credential metadata or URL."""

    credential = (request.credential_name or "").upper()
    url = request.url.lower()
    if "OPENDART" in credential or "opendart" in url:
        return "opendart"
    if "NAVER" in credential or "openapi.naver.com" in url:
        return "naver_search"
    if "DATA_GO_KR" in credential or "apis.data.go.kr" in url:
        return "data_go_kr"
    if "KRX" in credential or "krx.co.kr" in url:
        return "krx"
    if "COMPANY_GUIDE" in credential or "comp.wisereport.co.kr" in url:
        return "company_guide"
    return "unknown"


__all__ = [
    "RateLimitDecision",
    "RateLimitState",
    "RateLimiter",
    "SourceRateLimit",
    "source_name_for_request",
]
