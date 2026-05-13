"""Stage classification helper for daily scans."""

from __future__ import annotations

from dataclasses import dataclass, field

from e2r.models import ScoreSnapshot, Stage, StageSnapshot
from e2r.red_team import RedTeamAssessment
from e2r.staging import StageClassificationInput, StageClassifier


@dataclass(frozen=True)
class StageUpdateInput:
    score: ScoreSnapshot
    red_team: RedTeamAssessment | None = None
    previous_stage: Stage | None = None
    theme_regime_score: float = 0.0
    company_event_score: float = 0.0
    high_quality_company_event: bool = False
    thesis_ongoing: bool = False
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)
    mark_new_stage_changed: bool = True


class StageUpdateEngine:
    """Run the canonical classifier and mark new non-zero stages as changed."""

    def classify(self, inputs: StageUpdateInput) -> StageSnapshot:
        snapshot = StageClassifier().classify(
            StageClassificationInput(
                score=inputs.score,
                red_team=inputs.red_team,
                previous_stage=inputs.previous_stage,
                theme_regime_score=inputs.theme_regime_score,
                company_event_score=inputs.company_event_score,
                high_quality_company_event=inputs.high_quality_company_event,
                thesis_ongoing=inputs.thesis_ongoing,
                evidence_ids=inputs.evidence_ids,
            )
        )
        if (
            inputs.mark_new_stage_changed
            and inputs.previous_stage is None
            and snapshot.stage != Stage.STAGE_0
            and not snapshot.stage_changed
        ):
            return StageSnapshot(
                symbol=snapshot.symbol,
                as_of_date=snapshot.as_of_date,
                stage=snapshot.stage,
                previous_stage=snapshot.previous_stage,
                stage_changed=True,
                grade=snapshot.grade,
                stage_reason=snapshot.stage_reason,
                red_team_status=snapshot.red_team_status,
                evidence_ids=snapshot.evidence_ids,
                classifier_version=snapshot.classifier_version,
            )
        return snapshot
