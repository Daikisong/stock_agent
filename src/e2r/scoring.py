"""Deterministic E2R 2.0 scoring interface."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Mapping, Protocol

from .models import ScoreSnapshot


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
        raw_total = sum(payload.components.values()) - payload.risk_penalty
        total_score = round(max(0.0, min(100.0, raw_total)), 4)
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
            diagnostic_scores=payload.diagnostic_scores,
            evidence_ids=payload.evidence_ids,
            scoring_version=payload.scoring_version,
        )

