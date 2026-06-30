"""SLA and budget helpers for Census Mode."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class CensusSlaConfig:
    max_total_runtime_seconds: int = 1800
    max_symbol_runtime_seconds: int = 10
    max_deep_symbols: int = 25
    max_llm_calls: int = 50
    max_source_tasks_total: int = 250
    max_source_tasks_per_symbol: int = 3
    max_fetches_per_task: int = 3
    max_provider_failures_before_circuit_breaker: int = 100
    max_retry_count: int = 1
    top_results_must_not_be_none: bool = True
    retry_max_must_not_be_none: bool = True


def sla_from_mapping(payload: Mapping[str, Any] | None) -> CensusSlaConfig:
    payload = dict(payload or {})
    return CensusSlaConfig(
        max_total_runtime_seconds=int(payload.get("max_total_runtime_seconds", 1800)),
        max_symbol_runtime_seconds=int(payload.get("max_symbol_runtime_seconds", 10)),
        max_deep_symbols=int(payload.get("max_deep_symbols", 25)),
        max_llm_calls=int(payload.get("max_llm_calls", 50)),
        max_source_tasks_total=int(payload.get("max_source_tasks_total", 250)),
        max_source_tasks_per_symbol=int(payload.get("max_source_tasks_per_symbol", 3)),
        max_fetches_per_task=int(payload.get("max_fetches_per_task", 3)),
        max_provider_failures_before_circuit_breaker=int(payload.get("max_provider_failures_before_circuit_breaker", 100)),
        max_retry_count=int(payload.get("max_retry_count", 1)),
        top_results_must_not_be_none=bool(payload.get("top_results_must_not_be_none", True)),
        retry_max_must_not_be_none=bool(payload.get("retry_max_must_not_be_none", True)),
    )


def build_sla_report(
    *,
    config: CensusSlaConfig,
    total_runtime_seconds: float,
    deep_count: int,
    llm_calls: int,
    source_task_count: int,
    provider_failure_count: int,
    runtime_pending_count: int,
    unbounded_fetch_config_count: int = 0,
) -> dict[str, Any]:
    status = "COMPLETE"
    provider_circuit_open = provider_failure_count >= config.max_provider_failures_before_circuit_breaker
    if total_runtime_seconds > config.max_total_runtime_seconds or runtime_pending_count:
        status = "PARTIAL_WITH_PENDING"
    if provider_circuit_open:
        status = "PARTIAL_WITH_PENDING"
    if unbounded_fetch_config_count:
        status = "FAILED_UNBOUNDED_CONFIG"
    return {
        "schema_version": "e2r_census_sla_report_v1",
        "summary": {
            "status": status,
            "total_runtime_seconds": round(total_runtime_seconds, 4),
            "deep_count": deep_count,
            "llm_calls": llm_calls,
            "source_task_count": source_task_count,
            "provider_failure_count": provider_failure_count,
            "provider_circuit_open": provider_circuit_open,
            "runtime_pending_count": runtime_pending_count,
            "unbounded_fetch_config_count": unbounded_fetch_config_count,
        },
        "config": config.__dict__,
    }


def unbounded_config_count(configs: Sequence[Mapping[str, Any]]) -> int:
    count = 0
    for config in configs:
        if config.get("top_results") is None and "top_results" in config:
            count += 1
        if config.get("retry_max") is None and "retry_max" in config:
            count += 1
        if config.get("max_fetches") is None and "max_fetches" in config:
            count += 1
    return count


__all__ = ["CensusSlaConfig", "build_sla_report", "sla_from_mapping", "unbounded_config_count"]
