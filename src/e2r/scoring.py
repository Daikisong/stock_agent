"""Deterministic E2R 2.0 scoring interface."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Mapping, Protocol

from .calibration.scoring_profile import get_active_scoring_profile
from .models import IndustrialSubScores, ScoreSnapshot


@dataclass(frozen=True)
class ScoreComponentSpec:
    """Canonical score component and its maximum points."""

    key: str
    max_points: float
    label: str


CANONICAL_SCORE_COMPONENTS: tuple[ScoreComponentSpec, ...] = (
    ScoreComponentSpec("eps_fcf_explosion", 20.0, "EPS/FCF Explosion"),
    ScoreComponentSpec("earnings_visibility", 20.0, "Earnings Visibility and Quality"),
    ScoreComponentSpec("bottleneck_pricing", 20.0, "Bottleneck and Pricing Power"),
    ScoreComponentSpec("market_mispricing", 15.0, "Market Mispricing"),
    ScoreComponentSpec("valuation_rerating", 15.0, "Valuation Rerating Runway"),
    ScoreComponentSpec("capital_allocation", 5.0, "Capital Allocation"),
    ScoreComponentSpec("information_confidence", 5.0, "Information Confidence"),
)

_MAX_POINTS_BY_KEY = {component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS}


@dataclass(frozen=True)
class ScoringPayload:
    """Input payload for deterministic scoring.

    The payload is intentionally component-based. Feature engineering can evolve
    in later checkpoints while this interface remains stable.
    """

    symbol: str
    as_of_date: date
    components: Mapping[str, float]
    risk_penalty: float = 0.0
    diagnostic_scores: Mapping[str, float] = field(default_factory=dict)
    industrial_sub_scores: IndustrialSubScores | None = None
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)
    scoring_version: str = "e2r-2.0-cp1"

    def __post_init__(self) -> None:
        if not isinstance(self.symbol, str) or not self.symbol.strip():
            raise ValueError("symbol must be a non-empty string")
        if type(self.as_of_date) is not date:
            raise ValueError("as_of_date must be a date")
        component_copy = dict(self.components)
        expected_keys = set(_MAX_POINTS_BY_KEY)
        actual_keys = set(component_copy)
        missing = expected_keys - actual_keys
        unknown = actual_keys - expected_keys
        if missing:
            raise ValueError(f"missing score components: {sorted(missing)}")
        if unknown:
            raise ValueError(f"unknown score components: {sorted(unknown)}")
        for key, value in component_copy.items():
            max_points = _MAX_POINTS_BY_KEY[key]
            if value < 0 or value > max_points:
                raise ValueError(f"{key} must be between 0 and {max_points}")
        if self.risk_penalty < 0:
            raise ValueError("risk_penalty must be non-negative")
        diagnostic_copy = dict(self.diagnostic_scores)
        for key, value in diagnostic_copy.items():
            if not isinstance(key, str) or not key.strip():
                raise ValueError("diagnostic score keys must be non-empty strings")
            if value < 0 or value > 100:
                raise ValueError(f"diagnostic score {key} must be between 0 and 100")
        if self.industrial_sub_scores is not None and not isinstance(self.industrial_sub_scores, IndustrialSubScores):
            raise ValueError("industrial_sub_scores must be an IndustrialSubScores instance")
        if not isinstance(self.scoring_version, str) or not self.scoring_version.strip():
            raise ValueError("scoring_version must be a non-empty string")
        object.__setattr__(self, "components", component_copy)
        object.__setattr__(self, "diagnostic_scores", diagnostic_copy)
        object.__setattr__(self, "evidence_ids", tuple(self.evidence_ids))


class Scorer(Protocol):
    """Scoring contract used by later pipeline checkpoints."""

    def score(self, payload: ScoringPayload) -> ScoreSnapshot:
        """Return a deterministic score snapshot."""


class DeterministicScorer:
    """Canonical E2R 2.0 component scorer."""

    def score(self, payload: ScoringPayload) -> ScoreSnapshot:
        profile = get_active_scoring_profile()
        diagnostic_scores = dict(payload.diagnostic_scores)
        calibration_bonus = 0.0
        calibration_risk_penalty = 0.0

        if diagnostic_scores.get("calibration_stage2_actionable_evidence", 0.0) > 0:
            calibration_bonus += profile.adjustment("stage2_actionable_evidence_bonus")
        if diagnostic_scores.get("credible_order_or_policy_evidence", 0.0) > 0:
            calibration_bonus += profile.adjustment("stage2_actionable_evidence_bonus")
        if diagnostic_scores.get("high_mae_risk", 0.0) > 0:
            calibration_risk_penalty += profile.adjustment("high_mae_risk_guard_penalty")
        if diagnostic_scores.get("stage2_actionable_volatility_risk", 0.0) > 0:
            calibration_risk_penalty += profile.adjustment("stage2_actionable_volatility_guard_penalty")
        if _has_stage3_cross_evidence_buffer(payload, diagnostic_scores, profile):
            calibration_bonus += profile.adjustment("stage3_cross_evidence_green_buffer")
            diagnostic_scores["stage3_cross_evidence_buffer_applied"] = 1.0

        diagnostic_scores["active_scoring_profile"] = 1.0 if profile.profile_id.endswith("calibrated") else 0.0
        diagnostic_scores["calibration_total_adjustment"] = round(calibration_bonus - calibration_risk_penalty, 4)

        raw_total = sum(payload.components.values()) + calibration_bonus - payload.risk_penalty - calibration_risk_penalty
        total_score = round(max(0.0, min(100.0, raw_total)), 4)
        if payload.industrial_sub_scores is not None:
            diagnostic_scores.update(payload.industrial_sub_scores.as_diagnostic_scores())
        evidence_ids = payload.evidence_ids + (
            payload.industrial_sub_scores.evidence_ids if payload.industrial_sub_scores else ()
        )
        return ScoreSnapshot(
            symbol=payload.symbol,
            as_of_date=payload.as_of_date,
            eps_fcf_explosion_score=payload.components["eps_fcf_explosion"],
            earnings_visibility_score=payload.components["earnings_visibility"],
            bottleneck_pricing_score=payload.components["bottleneck_pricing"],
            market_mispricing_score=payload.components["market_mispricing"],
            valuation_rerating_score=payload.components["valuation_rerating"],
            capital_allocation_score=payload.components["capital_allocation"],
            information_confidence_score=payload.components["information_confidence"],
            risk_penalty=payload.risk_penalty,
            total_score=total_score,
            diagnostic_scores=diagnostic_scores,
            evidence_ids=tuple(dict.fromkeys(evidence_ids)),
            scoring_version=f"{payload.scoring_version}:{profile.profile_id}",
        )


def _has_stage3_cross_evidence_buffer(payload: ScoringPayload, diagnostics: Mapping[str, float], profile) -> bool:
    """Allow a small calibrated buffer only for non-price, Green-like evidence stacks."""

    if profile.adjustment("stage3_cross_evidence_green_buffer") <= 0:
        return False
    if diagnostics.get("price_only_blowoff_score", 0.0) >= 70.0:
        return False
    if diagnostics.get("one_off_shortage_risk", 0.0) >= 70.0:
        return False
    if diagnostics.get("theme_overheat_score", 0.0) >= 70.0:
        return False
    if diagnostics.get("revision_score", 0.0) < max(70.0, profile.threshold("stage3_green_revision_min", 55.0)):
        return False
    if len(payload.evidence_ids) < 2 and diagnostics.get("cross_evidence_family_count", 0.0) < 4.0:
        return False
    return (
        payload.components["eps_fcf_explosion"] >= profile.threshold("stage3_green_eps_fcf_min", 17.0)
        and payload.components["earnings_visibility"] >= profile.threshold("stage3_green_visibility_min", 15.0)
        and payload.components["bottleneck_pricing"] >= profile.threshold("stage3_green_bottleneck_min", 15.0)
        and payload.components["market_mispricing"] >= profile.threshold("stage3_green_mispricing_min", 10.0)
        and payload.components["valuation_rerating"] >= profile.threshold("stage3_green_valuation_min", 10.0)
        and payload.components["information_confidence"] >= profile.threshold("stage2_information_confidence_min", 3.0)
    )
