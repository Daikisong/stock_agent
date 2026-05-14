"""Backtest helpers that are not part of the core price-path engine."""

from e2r.backtest.layer1_recall import (
    Layer1RecallCase,
    Layer1RecallResult,
    Layer1RecallSummary,
    evaluate_layer1_recall,
    evaluate_layer1_recall_case,
    failure_reason_for_layer1_miss,
)
from e2r.backtest.historical_case_replay import (
    HistoricalCaseReplayResult,
    HistoricalCaseReplayRunner,
    HistoricalCaseReplaySummary,
    render_historical_case_replay_summary,
)

__all__ = [
    "HistoricalCaseReplayResult",
    "HistoricalCaseReplayRunner",
    "HistoricalCaseReplaySummary",
    "Layer1RecallCase",
    "Layer1RecallResult",
    "Layer1RecallSummary",
    "evaluate_layer1_recall",
    "evaluate_layer1_recall_case",
    "failure_reason_for_layer1_miss",
    "render_historical_case_replay_summary",
]
