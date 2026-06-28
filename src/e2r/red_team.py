"""Red Team thesis-break and 4B crowding rules."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Mapping

from .models import RedTeamFinding


class RedTeamRiskLevel(str, Enum):
    """Aggregated Red Team risk level."""

    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    HARD_BREAK = "hard_break"


class Soft4BStatus(str, Enum):
    """Diagnostic split inside canonical Stage 4B."""

    NONE = "none"
    WATCH = "4B-watch"
    ELEVATED = "4B-elevated"
    GRADUATED = "4B-graduated"


SOFT_4B_WEIGHTS: dict[str, float] = {
    "return_since_stage3": 15.0,
    "return_12_24m": 15.0,
    "extreme_forward_valuation": 15.0,
    "revision_slowdown": 20.0,
    "backlog_contract_slowdown": 15.0,
    "market_crowding": 10.0,
    "insider_or_major_event": 5.0,
    "blowoff_price_pattern": 5.0,
}


THESIS_BREAK_WEIGHTS: dict[str, float] = {
    "eps_fcf_revision_down": 20.0,
    "backlog_or_rpo_decline": 15.0,
    "new_orders_slowdown": 10.0,
    "contract_cancelled_or_delayed": 20.0,
    "opm_decline": 10.0,
    "asp_decline": 10.0,
    "supply_glut": 10.0,
    "customer_capex_decline": 5.0,
    "accounting_or_trust_issue": 25.0,
    "cashflow_deterioration": 10.0,
    "receivables_inventory_spike": 5.0,
}


HARD_BREAK_SIGNALS = frozenset(
    {
        "contract_cancelled_or_delayed",
        "accounting_or_trust_issue",
    }
)


FINDING_DESCRIPTIONS: dict[str, str] = {
    "eps_fcf_revision_down": "medium or long-term EPS/FCF path turned down",
    "backlog_or_rpo_decline": "backlog or RPO declined",
    "new_orders_slowdown": "new order momentum slowed sharply",
    "contract_cancelled_or_delayed": "long-term contract was cancelled or delayed",
    "opm_decline": "operating margin declined",
    "asp_decline": "ASP or pricing power declined",
    "supply_glut": "supply glut risk increased",
    "customer_capex_decline": "customer capex signal weakened",
    "accounting_or_trust_issue": "accounting or trust issue appeared",
    "cashflow_deterioration": "cash flow quality deteriorated",
    "receivables_inventory_spike": "receivables or inventory increased sharply",
}


def _require_date(value: date, field_name: str) -> None:
    if type(value) is not date:
        raise ValueError(f"{field_name} must be a date")


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _validate_factor_map(values: Mapping[str, float], allowed: Mapping[str, float], field_name: str) -> dict[str, float]:
    copied = dict(values)
    unknown = set(copied) - set(allowed)
    if unknown:
        raise ValueError(f"unknown {field_name}: {sorted(unknown)}")
    for key, value in copied.items():
        if value < 0 or value > 1:
            raise ValueError(f"{field_name} {key} must be between 0 and 1")
    return copied


def _weighted_score(values: Mapping[str, float], weights: Mapping[str, float]) -> float:
    score = sum(weights[key] * values.get(key, 0.0) for key in weights)
    return round(max(0.0, min(100.0, score)), 4)


@dataclass(frozen=True)
class RedTeamSignals:
    """Point-in-time Red Team inputs.

    Signal values are normalized from 0.0 to 1.0. For example,
    `{"revision_slowdown": 1.0}` contributes the full 20 points to the
    Soft 4B score, while `0.5` contributes half.
    """

    symbol: str
    as_of_date: date
    soft_4b_factors: Mapping[str, float] = field(default_factory=dict)
    thesis_break_factors: Mapping[str, float] = field(default_factory=dict)
    evidence_ids_by_signal: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    hard_break_quorum_by_signal: Mapping[str, bool] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_date(self.as_of_date, "as_of_date")
        object.__setattr__(
            self,
            "soft_4b_factors",
            _validate_factor_map(self.soft_4b_factors, SOFT_4B_WEIGHTS, "soft_4b_factors"),
        )
        object.__setattr__(
            self,
            "thesis_break_factors",
            _validate_factor_map(self.thesis_break_factors, THESIS_BREAK_WEIGHTS, "thesis_break_factors"),
        )
        normalized_evidence: dict[str, tuple[str, ...]] = {}
        allowed_signals = set(SOFT_4B_WEIGHTS) | set(THESIS_BREAK_WEIGHTS)
        for key, evidence_ids in self.evidence_ids_by_signal.items():
            if key not in allowed_signals:
                raise ValueError(f"unknown evidence signal: {key}")
            normalized_evidence[key] = tuple(evidence_ids)
        object.__setattr__(self, "evidence_ids_by_signal", normalized_evidence)
        normalized_quorum: dict[str, bool] = {}
        for key, value in self.hard_break_quorum_by_signal.items():
            if key not in HARD_BREAK_SIGNALS:
                raise ValueError(f"unknown hard-break quorum signal: {key}")
            normalized_quorum[key] = bool(value)
        object.__setattr__(self, "hard_break_quorum_by_signal", normalized_quorum)


@dataclass(frozen=True)
class RedTeamAssessment:
    """Aggregated Red Team result consumed by stage classification."""

    symbol: str
    as_of_date: date
    soft_4b_score: float
    thesis_break_score: float
    risk_level: RedTeamRiskLevel
    has_hard_break: bool
    soft_4b_status: Soft4BStatus = Soft4BStatus.NONE
    findings: tuple[RedTeamFinding, ...] = field(default_factory=tuple)
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)
    version: str = "e2r-2.0-cp2"

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_date(self.as_of_date, "as_of_date")
        if self.soft_4b_score < 0 or self.soft_4b_score > 100:
            raise ValueError("soft_4b_score must be between 0 and 100")
        if not isinstance(self.soft_4b_status, Soft4BStatus):
            object.__setattr__(self, "soft_4b_status", Soft4BStatus(self.soft_4b_status))
        if self.thesis_break_score < 0 or self.thesis_break_score > 100:
            raise ValueError("thesis_break_score must be between 0 and 100")
        for finding in self.findings:
            if finding.symbol != self.symbol:
                raise ValueError("finding symbol must match assessment symbol")
            if finding.as_of_date > self.as_of_date:
                raise ValueError("finding as_of_date cannot be after assessment as_of_date")
        object.__setattr__(self, "findings", tuple(self.findings))
        object.__setattr__(self, "evidence_ids", tuple(self.evidence_ids))

    @classmethod
    def empty(cls, symbol: str, as_of_date: date) -> "RedTeamAssessment":
        return cls(
            symbol=symbol,
            as_of_date=as_of_date,
            soft_4b_score=0.0,
            soft_4b_status=Soft4BStatus.NONE,
            thesis_break_score=0.0,
            risk_level=RedTeamRiskLevel.LOW,
            has_hard_break=False,
        )


class RedTeamEngine:
    """Deterministic Red Team rule engine."""

    def assess(self, signals: RedTeamSignals) -> RedTeamAssessment:
        soft_4b_score = _weighted_score(signals.soft_4b_factors, SOFT_4B_WEIGHTS)
        soft_4b_status = self._soft_4b_status(soft_4b_score)
        thesis_break_score = _weighted_score(signals.thesis_break_factors, THESIS_BREAK_WEIGHTS)
        findings: list[RedTeamFinding] = []

        for risk_type, factor in signals.thesis_break_factors.items():
            if factor <= 0:
                continue
            severity = round(THESIS_BREAK_WEIGHTS[risk_type] * factor, 4)
            evidence_ids = signals.evidence_ids_by_signal.get(risk_type, ())
            source_quorum_satisfied = signals.hard_break_quorum_by_signal.get(risk_type, False)
            is_hard_break = risk_type in HARD_BREAK_SIGNALS and bool(evidence_ids) and source_quorum_satisfied
            findings.append(
                RedTeamFinding(
                    symbol=signals.symbol,
                    as_of_date=signals.as_of_date,
                    risk_type=risk_type,
                    severity=severity,
                    is_hard_break=is_hard_break,
                    description=FINDING_DESCRIPTIONS[risk_type],
                    evidence_ids=evidence_ids,
                )
            )

        has_hard_break = any(finding.is_hard_break for finding in findings)
        risk_level = self._risk_level(thesis_break_score, has_hard_break)
        evidence_ids = tuple(
            dict.fromkeys(
                tuple(
                    evidence_id
                    for signal, factor in signals.soft_4b_factors.items()
                    if factor > 0.0
                    for evidence_id in signals.evidence_ids_by_signal.get(signal, ())
                )
                + tuple(
                    evidence_id
                    for finding in findings
                    for evidence_id in finding.evidence_ids
                )
            )
        )
        return RedTeamAssessment(
            symbol=signals.symbol,
            as_of_date=signals.as_of_date,
            soft_4b_score=soft_4b_score,
            soft_4b_status=soft_4b_status,
            thesis_break_score=thesis_break_score,
            risk_level=risk_level,
            has_hard_break=has_hard_break,
            findings=tuple(findings),
            evidence_ids=evidence_ids,
        )

    @staticmethod
    def _risk_level(thesis_break_score: float, has_hard_break: bool) -> RedTeamRiskLevel:
        if has_hard_break:
            return RedTeamRiskLevel.HARD_BREAK
        if thesis_break_score >= 40.0:
            return RedTeamRiskLevel.HIGH
        if thesis_break_score >= 20.0:
            return RedTeamRiskLevel.MODERATE
        return RedTeamRiskLevel.LOW

    @staticmethod
    def _soft_4b_status(soft_4b_score: float) -> Soft4BStatus:
        if soft_4b_score >= 80.0:
            return Soft4BStatus.GRADUATED
        if soft_4b_score >= 70.0:
            return Soft4BStatus.ELEVATED
        if soft_4b_score >= 60.0:
            return Soft4BStatus.WATCH
        return Soft4BStatus.NONE
