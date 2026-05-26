"""E2R 2.0 stage classifier."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

from .calibration.scoring_profile import get_active_scoring_profile
from .models import ScoreSnapshot, Stage, StageSnapshot
from .red_team import RedTeamAssessment, RedTeamRiskLevel, Soft4BStatus


ACTIVE_RERATING_STAGES = frozenset(
    {
        Stage.STAGE_3_GREEN,
        Stage.STAGE_3_YELLOW,
        Stage.STAGE_3_RED,
        Stage.STAGE_4A,
        Stage.STAGE_4B,
    }
)
STAGE_3_GREEN_MIN_REVISION_SCORE = 50.0


def _require_date(value: date, field_name: str) -> None:
    if type(value) is not date:
        raise ValueError(f"{field_name} must be a date")


def _require_score(value: float, field_name: str) -> None:
    if value < 0 or value > 100:
        raise ValueError(f"{field_name} must be between 0 and 100")


def _score_diagnostic(score: ScoreSnapshot, key: str, default: float = 0.0) -> float:
    return float(score.diagnostic_scores.get(key, default))


def _grade_from_score(total_score: float, stage: Stage, soft_4b_status: Soft4BStatus = Soft4BStatus.NONE) -> str:
    if stage == Stage.STAGE_4C:
        return "Thesis Break"
    if stage == Stage.STAGE_4B:
        return soft_4b_status.value if soft_4b_status != Soft4BStatus.NONE else Soft4BStatus.WATCH.value
    if total_score >= 90:
        return "S"
    if total_score >= 80:
        return "A"
    if total_score >= 65:
        return "B"
    if total_score >= 45:
        return "C"
    return "Watch"


@dataclass(frozen=True)
class StageClassificationInput:
    """Inputs for deterministic stage classification.

    All fields must already be known as of `score.as_of_date`.
    """

    score: ScoreSnapshot
    red_team: RedTeamAssessment | None = None
    previous_stage: Stage | None = None
    theme_regime_score: float = 0.0
    company_event_score: float = 0.0
    high_quality_company_event: bool = False
    thesis_ongoing: bool = False
    archive_requested: bool = False
    coverage_impossible: bool = False
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        _require_score(self.theme_regime_score, "theme_regime_score")
        _require_score(self.company_event_score, "company_event_score")
        if self.red_team is not None:
            if self.red_team.symbol != self.score.symbol:
                raise ValueError("red_team symbol must match score symbol")
            if self.red_team.as_of_date > self.score.as_of_date:
                raise ValueError("red_team as_of_date cannot be after score as_of_date")
        object.__setattr__(self, "evidence_ids", tuple(self.evidence_ids))


class StageClassifier:
    """Rule-based implementation of the E2R 2.0 stage machine."""

    version = "e2r-2.0-cp2"

    def classify(self, inputs: StageClassificationInput) -> StageSnapshot:
        score = inputs.score
        red_team = inputs.red_team or RedTeamAssessment.empty(score.symbol, score.as_of_date)
        stage, reasons = self._classify_stage(inputs, red_team)
        evidence_ids = tuple(dict.fromkeys(score.evidence_ids + red_team.evidence_ids + inputs.evidence_ids))
        previous_stage = inputs.previous_stage
        return StageSnapshot(
            symbol=score.symbol,
            as_of_date=score.as_of_date,
            stage=stage,
            previous_stage=previous_stage,
            stage_changed=previous_stage is not None and previous_stage != stage,
            grade=_grade_from_score(score.total_score, stage, red_team.soft_4b_status),
            stage_reason=tuple(reasons),
            red_team_status=red_team.risk_level.value,
            evidence_ids=evidence_ids,
            classifier_version=self.version,
        )

    def _classify_stage(
        self,
        inputs: StageClassificationInput,
        red_team: RedTeamAssessment,
    ) -> tuple[Stage, list[str]]:
        score = inputs.score
        reasons: list[str] = []

        if inputs.archive_requested or inputs.coverage_impossible:
            reasons.append("archive condition was present as of the decision date")
            return Stage.STAGE_5, reasons

        if red_team.has_hard_break:
            reasons.append("Red Team hard thesis-break condition was present")
            return Stage.STAGE_4C, reasons

        profile = get_active_scoring_profile()
        if profile.guardrail_enabled("hard_4c_thesis_break_routes_to_4c") and _score_diagnostic(
            score, "hard_4c_thesis_break_score"
        ) >= 80.0:
            reasons.append("calibrated hard 4C thesis-break guard was triggered")
            return Stage.STAGE_4C, reasons
        if (
            profile.guardrail_enabled("rolling_calibration_enabled")
            and _score_diagnostic(score, "v12_scope_hard_4c_confirmation_match") > 0
            and _has_non_price_thesis_break_confirmation(score)
        ):
            reasons.append("rolling 4C confirmation guard found non-price thesis-break evidence")
            return Stage.STAGE_4C, reasons

        if inputs.previous_stage in ACTIVE_RERATING_STAGES and red_team.soft_4b_score >= 60.0:
            if not _full_4b_allowed_by_rolling_guard(score, red_team):
                reasons.append("rolling 4B guard kept price-only or early 4B evidence as watch-only")
            else:
                reasons.append(f"Soft 4B {red_team.soft_4b_status.value} score reached {red_team.soft_4b_score:.1f}")
                return Stage.STAGE_4B, reasons

        if (
            inputs.previous_stage in ACTIVE_RERATING_STAGES
            and inputs.thesis_ongoing
            and score.total_score >= 65.0
            and red_team.soft_4b_score < 60.0
            and red_team.thesis_break_score < 40.0
        ):
            reasons.append("active rerating thesis remained supported")
            return Stage.STAGE_4A, reasons

        if self._is_stage_3_red(score, red_team):
            reasons.append("Stage 3 evidence existed, but Red Team or valuation risk was high")
            return Stage.STAGE_3_RED, reasons

        if self._is_stage_3_green(score, red_team):
            reasons.append("high-confidence rerating conditions were met with low Red Team risk")
            return Stage.STAGE_3_GREEN, reasons

        if (
            score.total_score >= profile.threshold("stage3_yellow_total_min", 80.0)
            and not self._positive_stage_blocked_by_price_only(score)
        ):
            reasons.append("Stage 3 score threshold was met, but Green conditions were incomplete")
            return Stage.STAGE_3_YELLOW, reasons

        if self._is_stage_2(score, red_team):
            if self._is_stage_2_actionable(score):
                reasons.append("calibrated Stage2-Actionable tier was met inside canonical Stage 2")
            else:
                reasons.append("candidate threshold was met with required score components")
            return Stage.STAGE_2, reasons

        if inputs.company_event_score >= 60.0 or inputs.high_quality_company_event:
            reasons.append("company-level event was present, but candidate score threshold was not met")
            return Stage.STAGE_1, reasons

        if inputs.theme_regime_score >= 60.0:
            reasons.append("industry regime was present without sufficient company-level confirmation")
            return Stage.STAGE_0, reasons

        reasons.append("insufficient point-in-time evidence for a higher stage")
        return Stage.STAGE_0, reasons

    @staticmethod
    def _positive_stage_blocked_by_price_only(score: ScoreSnapshot) -> bool:
        profile = get_active_scoring_profile()
        threshold = 70.0
        if (
            profile.guardrail_enabled("rolling_calibration_enabled")
            and _score_diagnostic(score, "v12_scope_local_4b_watch_guard_match") > 0
        ):
            threshold = 60.0
        return (
            profile.guardrail_enabled("price_only_blowoff_blocks_positive_stage")
            and _score_diagnostic(score, "price_only_blowoff_score") >= threshold
        )

    @staticmethod
    def _is_stage_2(score: ScoreSnapshot, red_team: RedTeamAssessment) -> bool:
        profile = get_active_scoring_profile()
        if StageClassifier._positive_stage_blocked_by_price_only(score):
            return False
        if (
            profile.guardrail_enabled("rolling_calibration_enabled")
            and _score_diagnostic(score, "v12_scope_stage2_required_bridge_match") > 0
            and not _has_non_price_stage2_bridge(score)
        ):
            return False
        return (
            score.total_score >= profile.threshold("stage2_total_min", 65.0)
            and score.eps_fcf_explosion_score >= profile.threshold("stage2_eps_fcf_min", 10.0)
            and score.valuation_rerating_score >= profile.threshold("stage2_valuation_min", 7.0)
            and score.information_confidence_score >= profile.threshold("stage2_information_confidence_min", 3.0)
            and not red_team.has_hard_break
        )

    @staticmethod
    def _is_stage_2_actionable(score: ScoreSnapshot) -> bool:
        return (
            score.total_score >= 65.0
            and (
                _score_diagnostic(score, "calibration_stage2_actionable_evidence") > 0
                or _score_diagnostic(score, "credible_order_or_policy_evidence") > 0
            )
            and _score_diagnostic(score, "price_only_blowoff_score") < 70.0
        )

    @staticmethod
    def _is_stage_3_green(score: ScoreSnapshot, red_team: RedTeamAssessment) -> bool:
        profile = get_active_scoring_profile()
        if StageClassifier._positive_stage_blocked_by_price_only(score):
            return False
        revision_score = _score_diagnostic(score, "revision_score")
        structural_visibility_quality = _score_diagnostic(
            score,
            "structural_visibility_quality",
            _score_diagnostic(score, "contract_quality", 100.0),
        )
        contract_quality = _score_diagnostic(score, "contract_quality", 100.0)
        contract_required_for_green = _score_diagnostic(score, "contract_required_for_green", 0.0)
        one_off_shortage_risk = _score_diagnostic(score, "one_off_shortage_risk")
        return (
            score.total_score >= profile.threshold("stage3_green_total_min", 85.0)
            and score.eps_fcf_explosion_score >= profile.threshold("stage3_green_eps_fcf_min", 17.0)
            and score.earnings_visibility_score >= profile.threshold("stage3_green_visibility_min", 15.0)
            and score.bottleneck_pricing_score >= profile.threshold("stage3_green_bottleneck_min", 15.0)
            and score.market_mispricing_score >= profile.threshold("stage3_green_mispricing_min", 10.0)
            and score.valuation_rerating_score >= profile.threshold("stage3_green_valuation_min", 10.0)
            and revision_score >= profile.threshold("stage3_green_revision_min", STAGE_3_GREEN_MIN_REVISION_SCORE)
            and structural_visibility_quality >= profile.threshold("stage3_green_structural_visibility_min", 45.0)
            and (contract_required_for_green < 1.0 or contract_quality >= 45.0)
            and one_off_shortage_risk < 70.0
            and red_team.risk_level == RedTeamRiskLevel.LOW
        )

    @staticmethod
    def _is_stage_3_red(score: ScoreSnapshot, red_team: RedTeamAssessment) -> bool:
        one_off_shortage_risk = _score_diagnostic(score, "one_off_shortage_risk")
        revision_score = _score_diagnostic(score, "revision_score")
        if score.total_score < 80.0:
            return (
                one_off_shortage_risk >= 80.0
                and score.eps_fcf_explosion_score >= 17.0
                and revision_score >= STAGE_3_GREEN_MIN_REVISION_SCORE
                and score.information_confidence_score >= 2.0
            )
        return (
            red_team.risk_level in {RedTeamRiskLevel.HIGH, RedTeamRiskLevel.HARD_BREAK}
            or score.valuation_rerating_score < 7.0
            or score.earnings_visibility_score < 12.0
            or score.bottleneck_pricing_score < 12.0
            or _score_diagnostic(
                score,
                "structural_visibility_quality",
                _score_diagnostic(score, "contract_quality", 100.0),
            )
            < 25.0
            or one_off_shortage_risk >= 80.0
            or _score_diagnostic(score, "theme_overheat_score") >= 70.0
        )


def _has_non_price_stage2_bridge(score: ScoreSnapshot) -> bool:
    if _score_diagnostic(score, "calibration_stage2_actionable_evidence") > 0:
        return True
    if _score_diagnostic(score, "credible_order_or_policy_evidence") > 0:
        return True
    non_price_families = (
        "evidence_family_financial_actual",
        "evidence_family_disclosure",
        "evidence_family_research_report",
        "evidence_family_consensus",
        "evidence_family_consensus_revision",
        "evidence_family_news",
    )
    non_price_count = sum(1 for key in non_price_families if _score_diagnostic(score, key) > 0)
    return non_price_count >= 2 or _score_diagnostic(score, "cross_evidence_family_count") >= 3.0


def _has_non_price_thesis_break_confirmation(score: ScoreSnapshot) -> bool:
    if _score_diagnostic(score, "hard_4c_thesis_break_score") < 75.0:
        return False
    return any(
        _score_diagnostic(score, key) > 0
        for key in (
            "thesis_break_non_price_evidence",
            "evidence_family_disclosure",
            "evidence_family_research_report",
            "evidence_family_financial_actual",
            "evidence_family_news",
        )
    )


def _full_4b_allowed_by_rolling_guard(score: ScoreSnapshot, red_team: RedTeamAssessment) -> bool:
    profile = get_active_scoring_profile()
    if not profile.guardrail_enabled("rolling_calibration_enabled"):
        return True
    if _score_diagnostic(score, "v12_scope_local_4b_watch_guard_match") > 0 and _score_diagnostic(
        score, "price_only_blowoff_score"
    ) >= 60.0:
        return False
    if _score_diagnostic(score, "v12_scope_full_4b_overlay_match") <= 0:
        return True
    if profile.guardrail_enabled("full_4b_requires_non_price_evidence"):
        return _has_non_price_stage2_bridge(score) or red_team.thesis_break_score >= 40.0
    return True
