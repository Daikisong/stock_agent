"""Depth policy for bounded Census execution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence

from e2r.production.metadata import stable_hash

from .schemas import BaselineScanResult, DepthDecision, DepthLevel, UniverseInstrument


@dataclass(frozen=True)
class CensusDepthPolicyConfig:
    high_priority_threshold: float = 35.0
    official_light_threshold: float = 10.0
    max_deep_symbols: int = 25
    sector_sample_quota: int = 1
    max_source_tasks_per_symbol: int = 3
    max_fetches_per_task: int = 3
    max_llm_calls_per_symbol: int = 1


def depth_policy_from_mapping(payload: Mapping[str, object] | None) -> CensusDepthPolicyConfig:
    payload = dict(payload or {})
    return CensusDepthPolicyConfig(
        high_priority_threshold=float(payload.get("high_priority_threshold", 35.0)),
        official_light_threshold=float(payload.get("official_light_threshold", 10.0)),
        max_deep_symbols=int(payload.get("max_deep_symbols", 25)),
        sector_sample_quota=int(payload.get("sector_sample_quota", 1)),
        max_source_tasks_per_symbol=int(payload.get("max_source_tasks_per_symbol", 3)),
        max_fetches_per_task=int(payload.get("max_fetches_per_task", 3)),
        max_llm_calls_per_symbol=int(payload.get("max_llm_calls_per_symbol", 1)),
    )


def decide_depths(
    instruments: Sequence[UniverseInstrument],
    scans: Sequence[BaselineScanResult],
    *,
    config: CensusDepthPolicyConfig,
) -> tuple[DepthDecision, ...]:
    by_symbol = {scan.symbol: scan for scan in scans}
    prioritized = sorted(
        (
            (item, by_symbol[item.symbol])
            for item in instruments
            if item.eligible_for_census and item.symbol in by_symbol
        ),
        key=lambda pair: (-pair[1].trigger_priority_score, pair[0].symbol),
    )
    deep_symbols = _bounded_deep_symbols(prioritized, config=config)
    sampled = _sector_samples(instruments, config=config)
    decisions: list[DepthDecision] = []
    for instrument in instruments:
        scan = by_symbol.get(instrument.symbol)
        if not instrument.eligible_for_census:
            decisions.append(
                DepthDecision(
                    symbol=instrument.symbol,
                    recommended_depth=DepthLevel.L0_UNIVERSE_ONLY,
                    reason=f"skipped_ineligible:{instrument.exclusion_reason}",
                    must_not_deepen_reason=instrument.exclusion_reason,
                )
            )
            continue
        if scan is None:
            decisions.append(
                DepthDecision(
                    symbol=instrument.symbol,
                    recommended_depth=DepthLevel.L0_UNIVERSE_ONLY,
                    reason="missing_baseline_scan",
                    must_not_deepen_reason="missing_baseline_scan",
                )
            )
            continue
        if scan.has_provider_failure:
            decisions.append(
                DepthDecision(
                    symbol=instrument.symbol,
                    recommended_depth=DepthLevel.L1_CHEAP_BASELINE,
                    reason="provider_failure_pending",
                    must_not_deepen_reason="provider_failure",
                )
            )
            continue
        if instrument.symbol in deep_symbols:
            decisions.append(
                _deep_decision(
                    instrument.symbol,
                    depth=DepthLevel.L3_RESEARCH_BRAIN_TRIAGE,
                    reason="priority_or_current_event_within_deep_budget",
                    config=config,
                )
            )
            continue
        if instrument.symbol in sampled:
            decisions.append(
                _deep_decision(
                    instrument.symbol,
                    depth=DepthLevel.L3_RESEARCH_BRAIN_TRIAGE,
                    reason="sector_random_audit_quota",
                    config=config,
                )
            )
            continue
        if scan.trigger_priority_score >= config.official_light_threshold or scan.has_current_event:
            decisions.append(
                DepthDecision(
                    symbol=instrument.symbol,
                    recommended_depth=DepthLevel.L2_OFFICIAL_LIGHT,
                    reason="official_light_signal",
                    source_task_budget={"max_tasks": 1, "max_fetches_per_task": 1},
                    llm_budget={"max_calls": 0},
                )
            )
            continue
        decisions.append(
            DepthDecision(
                symbol=instrument.symbol,
                recommended_depth=DepthLevel.L1_CHEAP_BASELINE,
                reason="low_signal_census_light",
                source_task_budget={"max_tasks": 0, "max_fetches_per_task": 0},
                llm_budget={"max_calls": 0},
            )
        )
    return tuple(decisions)


def _bounded_deep_symbols(
    prioritized: Sequence[tuple[UniverseInstrument, BaselineScanResult]],
    *,
    config: CensusDepthPolicyConfig,
) -> set[str]:
    result: list[str] = []
    for instrument, scan in prioritized:
        if scan.trigger_priority_score >= config.high_priority_threshold or scan.recent_risk_event_count > 0:
            result.append(instrument.symbol)
        if len(result) >= config.max_deep_symbols:
            break
    return set(result)


def _sector_samples(instruments: Iterable[UniverseInstrument], *, config: CensusDepthPolicyConfig) -> set[str]:
    if config.sector_sample_quota <= 0:
        return set()
    by_sector: dict[str, list[UniverseInstrument]] = {}
    for item in instruments:
        if not item.eligible_for_census:
            continue
        key = item.large_sector_id or "unknown"
        by_sector.setdefault(key, []).append(item)
    sampled: set[str] = set()
    for sector, rows in by_sector.items():
        sorted_rows = sorted(rows, key=lambda item: stable_hash({"sector": sector, "symbol": item.symbol}))
        for item in sorted_rows[: config.sector_sample_quota]:
            sampled.add(item.symbol)
    return sampled


def _deep_decision(
    symbol: str,
    *,
    depth: DepthLevel,
    reason: str,
    config: CensusDepthPolicyConfig,
) -> DepthDecision:
    return DepthDecision(
        symbol=symbol,
        recommended_depth=depth,
        reason=reason,
        expected_runtime_cost="MEDIUM",
        source_task_budget={
            "max_tasks": config.max_source_tasks_per_symbol,
            "max_fetches_per_task": config.max_fetches_per_task,
            "max_retries": 1,
        },
        llm_budget={"max_calls": config.max_llm_calls_per_symbol},
    )


__all__ = ["CensusDepthPolicyConfig", "decide_depths", "depth_policy_from_mapping"]
