"""Production cutover gate helpers for E2R.

The production package is intentionally stricter than the Research Brain v4
shadow layer.  v4 may prove that the shape of the pipeline works; this package
checks whether the run is safe to count as a real market cutover.
"""

from .candidate_event_purity import (
    CandidateEventProductionEligibility,
    ProductionMode,
    build_candidate_purity_report,
    evaluate_candidate_event_production_eligibility,
)
from .cutover_shadow import build_production_cutover_bundle, write_production_cutover_bundle

__all__ = [
    "CandidateEventProductionEligibility",
    "ProductionMode",
    "build_candidate_purity_report",
    "build_production_cutover_bundle",
    "evaluate_candidate_event_production_eligibility",
    "write_production_cutover_bundle",
]
