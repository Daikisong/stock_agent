"""Evidence-aware Stage 4A/4B/4C lifecycle detector."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

from e2r.models import Stage
from e2r.red_team import Soft4BStatus


@dataclass(frozen=True)
class StageLifecycleDetectionInput:
    """Point-in-time inputs for lifecycle monitoring after Stage 3."""

    symbol: str
    as_of_date: date
    previous_stage: Stage
    stage3_date: date | None = None
    return_since_stage3: float | None = None
    return_12m: float | None = None
    return_24m: float | None = None
    valuation_rerating_score: float | None = None
    revision_momentum_slowing: bool = False
    backlog_order_margin_slowdown: bool = False
    blowoff_price_pattern: bool = False
    crowding_or_universally_bullish: bool = False
    stage3_evidence_intact: bool = True
    eps_fcf_visibility_strong: bool = True
    hard_thesis_break: bool = False
    hard_break_reasons: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        object.__setattr__(self, "hard_break_reasons", tuple(self.hard_break_reasons))


@dataclass(frozen=True)
class StageLifecycleDetection:
    """Lifecycle detection output consumed by backtests and reports."""

    symbol: str
    as_of_date: date
    lifecycle_stage: Stage
    soft_4b_status: Soft4BStatus
    status: str
    score: float
    price_only_warning: bool
    reasons: tuple[str, ...]
    evidence_based: bool


class StageLifecycleDetector:
    """Detect 4A/4B/4C without fabricating missing evidence."""

    def detect(self, inputs: StageLifecycleDetectionInput) -> StageLifecycleDetection:
        if (
            not inputs.hard_thesis_break
            and not inputs.stage3_evidence_intact
            and not inputs.eps_fcf_visibility_strong
            and inputs.return_since_stage3 is None
            and inputs.return_12m is None
            and inputs.return_24m is None
            and inputs.valuation_rerating_score is None
            and not inputs.revision_momentum_slowing
            and not inputs.backlog_order_margin_slowdown
            and not inputs.blowoff_price_pattern
            and not inputs.crowding_or_universally_bullish
        ):
            return StageLifecycleDetection(
                symbol=inputs.symbol,
                as_of_date=inputs.as_of_date,
                lifecycle_stage=inputs.previous_stage,
                soft_4b_status=Soft4BStatus.NONE,
                status="unknown_insufficient_evidence",
                score=0.0,
                price_only_warning=False,
                reasons=("unknown_insufficient_evidence",),
                evidence_based=False,
            )

        if inputs.hard_thesis_break:
            reasons = inputs.hard_break_reasons or ("hard_thesis_break",)
            return StageLifecycleDetection(
                symbol=inputs.symbol,
                as_of_date=inputs.as_of_date,
                lifecycle_stage=Stage.STAGE_4C,
                soft_4b_status=Soft4BStatus.NONE,
                status="hard_4c",
                score=100.0,
                price_only_warning=False,
                reasons=tuple(reasons),
                evidence_based=True,
            )

        score, reasons, evidence_factors = _soft_4b_score(inputs)
        price_only = score >= 35.0 and evidence_factors == 0
        if price_only:
            return StageLifecycleDetection(
                symbol=inputs.symbol,
                as_of_date=inputs.as_of_date,
                lifecycle_stage=Stage.STAGE_4A,
                soft_4b_status=Soft4BStatus.WATCH,
                status="price_only_4b_watch",
                score=score,
                price_only_warning=True,
                reasons=tuple(reasons),
                evidence_based=False,
            )

        if score >= 75.0 and evidence_factors >= 2:
            status = Soft4BStatus.GRADUATED
        elif score >= 55.0 and evidence_factors >= 1:
            status = Soft4BStatus.ELEVATED
        elif score >= 35.0 and evidence_factors >= 1:
            status = Soft4BStatus.WATCH
        else:
            status = Soft4BStatus.NONE

        if status != Soft4BStatus.NONE:
            return StageLifecycleDetection(
                symbol=inputs.symbol,
                as_of_date=inputs.as_of_date,
                lifecycle_stage=Stage.STAGE_4B,
                soft_4b_status=status,
                status=status.value,
                score=score,
                price_only_warning=False,
                reasons=tuple(reasons),
                evidence_based=True,
            )

        lifecycle = Stage.STAGE_4A if inputs.stage3_evidence_intact and inputs.eps_fcf_visibility_strong else inputs.previous_stage
        return StageLifecycleDetection(
            symbol=inputs.symbol,
            as_of_date=inputs.as_of_date,
            lifecycle_stage=lifecycle,
            soft_4b_status=Soft4BStatus.NONE,
            status="4A_ongoing" if lifecycle == Stage.STAGE_4A else "insufficient_lifecycle_evidence",
            score=score,
            price_only_warning=False,
            reasons=tuple(reasons or ("stage3_evidence_intact",)),
            evidence_based=bool(reasons),
        )


def _soft_4b_score(inputs: StageLifecycleDetectionInput) -> tuple[float, list[str], int]:
    score = 0.0
    reasons: list[str] = []
    evidence_factors = 0
    if inputs.return_since_stage3 is not None and inputs.return_since_stage3 >= 2.0:
        score += 20.0
        reasons.append("stage3_return_multiple_gt_3x")
    elif inputs.return_since_stage3 is not None and inputs.return_since_stage3 >= 1.0:
        score += 12.0
        reasons.append("stage3_return_multiple_gt_2x")
    if inputs.return_12m is not None and inputs.return_12m >= 1.5:
        score += 12.0
        reasons.append("12m_return_excessive")
    if inputs.return_24m is not None and inputs.return_24m >= 2.5:
        score += 10.0
        reasons.append("24m_return_excessive")
    if inputs.valuation_rerating_score is not None and inputs.valuation_rerating_score >= 90.0:
        score += 15.0
        evidence_factors += 1
        reasons.append("valuation_rerating_score_saturated")
    if inputs.revision_momentum_slowing:
        score += 20.0
        evidence_factors += 1
        reasons.append("revision_momentum_slowing")
    if inputs.backlog_order_margin_slowdown:
        score += 20.0
        evidence_factors += 1
        reasons.append("backlog_order_margin_slowdown")
    if inputs.blowoff_price_pattern:
        score += 10.0
        reasons.append("blowoff_price_pattern")
    if inputs.crowding_or_universally_bullish:
        score += 10.0
        evidence_factors += 1
        reasons.append("crowding_or_universally_bullish")
    return min(100.0, score), reasons, evidence_factors


__all__ = [
    "StageLifecycleDetection",
    "StageLifecycleDetectionInput",
    "StageLifecycleDetector",
]
