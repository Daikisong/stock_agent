"""Pure deterministic score-aggregation contract shared by offline receipts."""

from __future__ import annotations

from typing import Any, Mapping


AGGREGATOR_CONFIG: Mapping[str, Any] = {
    "version": "e2r_v5_component_consensus_v2",
    "required_roles": ["ANALYST", "SKEPTIC", "CALIBRATION_JUDGE"],
    "invalid_proposal_policy": "REMOVE_AND_RECORD",
    "consensus_method": "MEDIAN_WITH_ALLOWED_RANGE_INTERSECTION",
    "counter_application": "SKEPTIC_CANNOT_CREATE_SUPPORT",
    "material_disagreement_fraction": 0.20,
    "material_disagreement_absolute_floor": 2.0,
    "minimum_finalization_confidence": 0.40,
    "source_confidence_affects_points": False,
    "independent_corroboration_affects_points": False,
    "tiny_impact_cap_multiplication": False,
    "material_disagreement_policy": "RESEARCH_REQUIRED",
    "stage_authority": False,
}
