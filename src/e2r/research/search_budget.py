"""Search budget controls for free web research."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class ResearchLayer(str, Enum):
    """Three-layer free research architecture."""

    CHEAP_SCAN = "cheap_scan"
    EVENT_SEARCH = "event_search"
    DEEP_RESEARCH = "deep_research"
    ACTIVE_MONITORING = "active_monitoring"


@dataclass(frozen=True)
class SearchBudget:
    """Search accounting for free search mode.

    ``None`` means the layer is not stopped by accounting caps. Tests may still
    pass explicit small numbers to exercise skip handling.
    """

    max_total_queries_per_day: int | None = None
    max_queries_per_symbol: int | None = None
    max_deep_research_symbols: int | None = None
    max_active_monitoring_symbols: int | None = None
    sleep_seconds_between_queries: float = 0.0
    stop_on_captcha_or_block: bool = True

    def __post_init__(self) -> None:
        for field_name in (
            "max_total_queries_per_day",
            "max_queries_per_symbol",
            "max_deep_research_symbols",
            "max_active_monitoring_symbols",
        ):
            value = getattr(self, field_name)
            if value is not None and value < 0:
                raise ValueError(f"{field_name} must be non-negative")
        if self.sleep_seconds_between_queries < 0:
            raise ValueError("sleep_seconds_between_queries must be non-negative")


@dataclass(frozen=True)
class SearchBudgetDecision:
    """Budget check result."""

    allowed: bool
    reason: str | None = None


@dataclass
class SearchBudgetTracker:
    """Mutable per-run budget state."""

    budget: SearchBudget = field(default_factory=SearchBudget)
    total_queries_used: int = 0
    queries_by_symbol: dict[str, int] = field(default_factory=dict)
    deep_research_symbols: set[str] = field(default_factory=set)
    active_monitoring_symbols: set[str] = field(default_factory=set)
    stopped_reason: str | None = None

    def can_run(self, symbol: str, layer: ResearchLayer | str) -> SearchBudgetDecision:
        layer_value = ResearchLayer(layer)
        if self.stopped_reason:
            return SearchBudgetDecision(False, self.stopped_reason)
        if self.budget.max_total_queries_per_day is not None and self.total_queries_used >= self.budget.max_total_queries_per_day:
            return SearchBudgetDecision(False, "daily_query_budget_exhausted")
        if self.budget.max_queries_per_symbol is not None and self.queries_by_symbol.get(symbol, 0) >= self.budget.max_queries_per_symbol:
            return SearchBudgetDecision(False, "symbol_query_budget_exhausted")
        if (
            layer_value == ResearchLayer.DEEP_RESEARCH
            and symbol not in self.deep_research_symbols
            and self.budget.max_deep_research_symbols is not None
            and len(self.deep_research_symbols) >= self.budget.max_deep_research_symbols
        ):
            return SearchBudgetDecision(False, "deep_research_symbol_budget_exhausted")
        if (
            layer_value == ResearchLayer.ACTIVE_MONITORING
            and symbol not in self.active_monitoring_symbols
            and self.budget.max_active_monitoring_symbols is not None
            and len(self.active_monitoring_symbols) >= self.budget.max_active_monitoring_symbols
        ):
            return SearchBudgetDecision(False, "active_monitoring_symbol_budget_exhausted")
        return SearchBudgetDecision(True)

    def record_query(self, symbol: str, layer: ResearchLayer | str) -> None:
        layer_value = ResearchLayer(layer)
        self.total_queries_used += 1
        self.queries_by_symbol[symbol] = self.queries_by_symbol.get(symbol, 0) + 1
        if layer_value == ResearchLayer.DEEP_RESEARCH:
            self.deep_research_symbols.add(symbol)
        if layer_value == ResearchLayer.ACTIVE_MONITORING:
            self.active_monitoring_symbols.add(symbol)

    def record_block(self, reason: str = "captcha_or_block_detected") -> None:
        if self.budget.stop_on_captcha_or_block:
            self.stopped_reason = reason


__all__ = [
    "ResearchLayer",
    "SearchBudget",
    "SearchBudgetDecision",
    "SearchBudgetTracker",
]
