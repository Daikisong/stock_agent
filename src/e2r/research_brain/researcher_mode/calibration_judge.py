"""Blind historical-anchor calibration judge."""

from __future__ import annotations

from .component_judge import ComponentJudge
from .component_researcher import StructuredResearchProvider
from .schemas import ComponentJudgeRole


class CalibrationJudge(ComponentJudge):
    """Checks point-scale consistency without seeing historical outcomes."""

    def __init__(self, *, provider: StructuredResearchProvider) -> None:
        super().__init__(
            provider=provider,
            role=ComponentJudgeRole.CALIBRATION_JUDGE.value,
        )


__all__ = ["CalibrationJudge"]
