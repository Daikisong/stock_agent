"""Models for free cheap-scan candidate discovery."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum

from e2r.models import Market

CANDIDATE_SOURCE_PATHS = frozenset(
    {
        "official_cheap_scan",
        "report_radar",
        "runtime_fixture_spec",
        "targeted_smoke",
        "top_trading_value_probe",
    }
)


class RecommendedNextLayer(str, Enum):
    """Next action after cheap scan."""

    NONE = "none"
    EVENT_SEARCH = "event_search"
    DEEP_RESEARCH = "deep_research"


@dataclass(frozen=True)
class CheapScanCandidate:
    """One cheap-scan candidate from official/free sources."""

    symbol: str
    company_name: str
    market: Market
    as_of_date: date
    reason_codes: tuple[str, ...] = field(default_factory=tuple)
    price_event_score: float = 0.0
    disclosure_event_score: float = 0.0
    financial_event_score: float = 0.0
    risk_event_score: float = 0.0
    cheap_scan_total_score: float = 0.0
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)
    recommended_next_layer: RecommendedNextLayer = RecommendedNextLayer.NONE
    dropped_reason: str | None = None
    candidate_source_path: str = "official_cheap_scan"
    test_injected: bool = False
    production_candidate: bool = True

    def __post_init__(self) -> None:
        if not self.symbol.strip():
            raise ValueError("symbol must be non-empty")
        if not self.company_name.strip():
            raise ValueError("company_name must be non-empty")
        if type(self.as_of_date) is not date:
            raise ValueError("as_of_date must be a date")
        if not isinstance(self.market, Market):
            object.__setattr__(self, "market", Market(self.market))
        if not isinstance(self.recommended_next_layer, RecommendedNextLayer):
            object.__setattr__(self, "recommended_next_layer", RecommendedNextLayer(self.recommended_next_layer))
        if self.candidate_source_path not in CANDIDATE_SOURCE_PATHS:
            allowed = ", ".join(sorted(CANDIDATE_SOURCE_PATHS))
            raise ValueError(f"candidate_source_path must be one of: {allowed}")
        if self.test_injected and self.production_candidate:
            raise ValueError("test_injected candidates cannot be production candidates")
        object.__setattr__(self, "reason_codes", tuple(dict.fromkeys(self.reason_codes)))
        object.__setattr__(self, "evidence_ids", tuple(dict.fromkeys(self.evidence_ids)))
        for field_name in (
            "price_event_score",
            "disclosure_event_score",
            "financial_event_score",
            "risk_event_score",
            "cheap_scan_total_score",
        ):
            value = getattr(self, field_name)
            if value < 0 or value > 100:
                raise ValueError(f"{field_name} must be between 0 and 100")


__all__ = ["CANDIDATE_SOURCE_PATHS", "CheapScanCandidate", "RecommendedNextLayer"]
