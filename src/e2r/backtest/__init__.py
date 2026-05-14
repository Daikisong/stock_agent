"""Backtest helpers that are not part of the core price-path engine."""

from e2r.backtest.layer1_recall import (
    Layer1RecallCase,
    Layer1RecallResult,
    Layer1RecallSummary,
    evaluate_layer1_recall,
    evaluate_layer1_recall_case,
    failure_reason_for_layer1_miss,
)
from e2r.backtest.blind_discovery_replay import (
    BlindDiscoveryConfig,
    BlindDiscoveryReplay,
    BlindDiscoveryResult,
)
from e2r.backtest.asof_research_replay import (
    AsOfReplayCandidate,
    AsOfResearchReplay,
    AsOfResearchReplayConfig,
    AsOfResearchReplayResult,
    AsOfResearchReplaySnapshot,
    BenchmarkAsOfRecallRow,
    FlowTrace,
    FlowTraceStep,
    render_asof_replay_summary,
)
from e2r.backtest.benchmark_labels import BenchmarkLabel, load_benchmark_labels
from e2r.backtest.historical_official_store import HistoricalOfficialSources, HistoricalOfficialStore
from e2r.backtest.e2r_standard_replay import (
    E2RStandardReplay,
    E2RStandardReplayCandidate,
    E2RStandardReplayConfig,
    E2RStandardReplayResult,
    E2RStandardReplaySnapshot,
)
from e2r.backtest.missed_benchmark_autopsy import (
    AutopsyConfig,
    AutopsyRow,
    EvidenceAvailability,
    MissedBenchmarkAutopsy,
    MissedBenchmarkAutopsyResult,
)
from e2r.backtest.stage_lifecycle_detector import (
    StageLifecycleDetection,
    StageLifecycleDetectionInput,
    StageLifecycleDetector,
)
from e2r.backtest.monthly_replay_suite import (
    MonthlyReplaySuiteConfig,
    MonthlyReplaySuiteResult,
    MonthlyReplaySuiteRunner,
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
    "BenchmarkLabel",
    "AutopsyConfig",
    "AutopsyRow",
    "AsOfReplayCandidate",
    "AsOfResearchReplay",
    "AsOfResearchReplayConfig",
    "AsOfResearchReplayResult",
    "AsOfResearchReplaySnapshot",
    "BlindDiscoveryConfig",
    "BlindDiscoveryReplay",
    "BlindDiscoveryResult",
    "BenchmarkAsOfRecallRow",
    "E2RStandardReplay",
    "E2RStandardReplayCandidate",
    "E2RStandardReplayConfig",
    "E2RStandardReplayResult",
    "E2RStandardReplaySnapshot",
    "EvidenceAvailability",
    "FlowTrace",
    "FlowTraceStep",
    "HistoricalOfficialSources",
    "HistoricalOfficialStore",
    "MissedBenchmarkAutopsy",
    "MissedBenchmarkAutopsyResult",
    "ReplayFrequency",
    "STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE",
    "StageLifecycleBacktest",
    "StageLifecycleDetection",
    "StageLifecycleDetectionInput",
    "StageLifecycleDetector",
    "StageLifecycleInput",
    "StageLifecycleResult",
    "Layer1RecallCase",
    "Layer1RecallResult",
    "Layer1RecallSummary",
    "MonthlyReplaySuiteConfig",
    "MonthlyReplaySuiteResult",
    "MonthlyReplaySuiteRunner",
    "evaluate_layer1_recall",
    "evaluate_layer1_recall_case",
    "failure_reason_for_layer1_miss",
    "load_benchmark_labels",
    "render_asof_replay_summary",
    "render_historical_case_replay_summary",
    "render_historical_replay_summary",
]
