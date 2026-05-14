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
from e2r.backtest.historical_universe_replay import (
    HistoricalReplayConfig,
    HistoricalReplayMode,
    HistoricalUniverseReplay,
    HistoricalUniverseReplayResult,
    ReplayFrequency,
    render_historical_replay_summary,
)
from e2r.backtest.stage_lifecycle_backtest import (
    STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE,
    StageLifecycleBacktest,
    StageLifecycleInput,
    StageLifecycleResult,
)

__all__ = [
    "HistoricalCaseReplayResult",
    "HistoricalCaseReplayRunner",
    "HistoricalCaseReplaySummary",
    "HistoricalReplayConfig",
    "HistoricalReplayMode",
    "HistoricalUniverseReplay",
    "HistoricalUniverseReplayResult",
    "ReplayFrequency",
    "STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE",
    "StageLifecycleBacktest",
    "StageLifecycleInput",
    "StageLifecycleResult",
    "Layer1RecallCase",
    "Layer1RecallResult",
    "Layer1RecallSummary",
    "evaluate_layer1_recall",
    "evaluate_layer1_recall_case",
    "failure_reason_for_layer1_miss",
    "render_historical_case_replay_summary",
    "render_historical_replay_summary",
]
