"""E2R Census Mode v1.

Census Mode builds a full-universe status map.  It does not turn baseline
events, price anomalies, or provider failures into score evidence.
"""

from .schemas import (
    AssessmentDepth,
    BaselineScanResult,
    CensusAssessmentEvent,
    CensusStageStatus,
    CensusStatus,
    DepthDecision,
    InvestigationStatus,
    ScoreValidStatus,
    SourceTask,
    SourceTaskExecution,
    UniverseInstrument,
)
from .canonical_current_adapter import (
    CANONICAL_CURRENT_ADAPTER_SCHEMA_VERSION,
    adapt_census_snapshot_to_current_input,
)

__all__ = [
    "AssessmentDepth",
    "CANONICAL_CURRENT_ADAPTER_SCHEMA_VERSION",
    "BaselineScanResult",
    "CensusAssessmentEvent",
    "CensusStageStatus",
    "CensusStatus",
    "DepthDecision",
    "InvestigationStatus",
    "ScoreValidStatus",
    "SourceTask",
    "SourceTaskExecution",
    "UniverseInstrument",
    "adapt_census_snapshot_to_current_input",
]
