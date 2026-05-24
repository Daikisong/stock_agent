"""Diagnostic view of Stage 2 and Stage 3 gate failures.

This module mirrors the classifier thresholds without changing them.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from e2r.models import ScoreSnapshot, Stage
from e2r.red_team import RedTeamAssessment, RedTeamRiskLevel
from e2r.sector_profiles import profile_name_from_diagnostic
from e2r.calibration.scoring_profile import get_active_scoring_profile
from e2r.staging import STAGE_3_GREEN_MIN_REVISION_SCORE


@dataclass(frozen=True)
class StageGateDiagnostics:
    """Threshold pass/fail details for score promotion autopsy."""

    stage2_gate_passed: bool
    stage3_green_gate_passed: bool
    failed_gate_names: tuple[str, ...]
    values_vs_thresholds: Mapping[str, Mapping[str, float | str | bool]]
    sector_profile: str = "GENERIC"
    structural_visibility_quality: float = 0.0
    sector_visibility_score: float = 0.0
    sector_bottleneck_score: float = 0.0
    cross_evidence_families_present: tuple[str, ...] = ()
    missing_evidence_families: tuple[str, ...] = ()
    promotion_band: str = "Stage 1"

    def failed(self, gate_name: str) -> bool:
        return gate_name in self.failed_gate_names


def diagnose_stage_gates(score: ScoreSnapshot, red_team: RedTeamAssessment) -> StageGateDiagnostics:
    """Return gate diagnostics using the current StageClassifier thresholds."""

    revision_score = _diagnostic(score, "revision_score")
    contract_quality = _diagnostic(score, "contract_quality", 100.0)
    structural_visibility_quality = _diagnostic(score, "structural_visibility_quality", contract_quality)
    sector_visibility_score = _diagnostic(score, "sector_visibility_score")
    sector_bottleneck_score = _diagnostic(score, "sector_bottleneck_score")
    cross_evidence_family_count = _diagnostic(score, "cross_evidence_family_count", 3.0)
    report_date_confidence = _diagnostic(score, "report_date_confidence", 100.0)
    domain_specific_evidence_score = _diagnostic(score, "domain_specific_evidence_score", sector_visibility_score)
    one_off_shortage_risk = _diagnostic(score, "one_off_shortage_risk")
    sector_profile = profile_name_from_diagnostic(_diagnostic(score, "sector_profile_id", 0.0))
    contract_quality_required = sector_profile in {"POWER_EQUIPMENT", "DEFENSE", "BATTERY_OVERHEAT"}
    present_families = _present_evidence_families(score)
    missing_families = tuple(family for family in _EVIDENCE_FAMILIES if family not in present_families)
    profile = get_active_scoring_profile()
    stage2_total_min = profile.threshold("stage2_total_min", 65.0)
    stage3_yellow_min = profile.threshold("stage3_yellow_total_min", 80.0)
    stage3_green_min = profile.threshold("stage3_green_total_min", 85.0)
    stage3_revision_min = profile.threshold("stage3_green_revision_min", STAGE_3_GREEN_MIN_REVISION_SCORE)

    checks: dict[str, tuple[float | str | bool, float | str | bool, bool]] = {
        "failed_stage2_total_score": (score.total_score, stage2_total_min, score.total_score >= stage2_total_min),
        "failed_stage2_eps_fcf": (score.eps_fcf_explosion_score, 10.0, score.eps_fcf_explosion_score >= 10.0),
        "failed_stage2_valuation": (score.valuation_rerating_score, 7.0, score.valuation_rerating_score >= 7.0),
        "failed_stage2_information_confidence": (
            score.information_confidence_score,
            3.0,
            score.information_confidence_score >= 3.0,
        ),
        "failed_stage3_total_score": (score.total_score, stage3_green_min, score.total_score >= stage3_green_min),
        "failed_stage3_eps_fcf": (score.eps_fcf_explosion_score, 17.0, score.eps_fcf_explosion_score >= 17.0),
        "failed_stage3_visibility": (
            score.earnings_visibility_score,
            15.0,
            score.earnings_visibility_score >= 15.0,
        ),
        "failed_stage3_bottleneck": (
            score.bottleneck_pricing_score,
            15.0,
            score.bottleneck_pricing_score >= 15.0,
        ),
        "failed_stage3_market_mispricing": (
            score.market_mispricing_score,
            10.0,
            score.market_mispricing_score >= 10.0,
        ),
        "failed_stage3_valuation": (
            score.valuation_rerating_score,
            10.0,
            score.valuation_rerating_score >= 10.0,
        ),
        "failed_stage3_revision": (
            revision_score,
            stage3_revision_min,
            revision_score >= stage3_revision_min,
        ),
        "failed_stage3_contract_quality": (
            contract_quality,
            45.0,
            contract_quality >= 45.0 or not contract_quality_required,
        ),
        "failed_structural_visibility_quality": (
            structural_visibility_quality,
            45.0,
            structural_visibility_quality >= 45.0,
        ),
        "failed_sector_visibility": (
            sector_visibility_score,
            45.0,
            sector_visibility_score >= 45.0,
        ),
        "failed_sector_bottleneck": (
            sector_bottleneck_score,
            35.0,
            sector_bottleneck_score >= 35.0,
        ),
        "failed_green_cross_evidence": (
            cross_evidence_family_count,
            3.0,
            cross_evidence_family_count >= 3.0,
        ),
        "failed_report_date_confidence": (
            report_date_confidence,
            1.0,
            report_date_confidence >= 1.0,
        ),
        "failed_domain_specific_evidence": (
            domain_specific_evidence_score,
            35.0,
            domain_specific_evidence_score >= 35.0,
        ),
        "failed_stage3_one_off_shortage_risk": (
            one_off_shortage_risk,
            70.0,
            one_off_shortage_risk < 70.0,
        ),
        "failed_stage3_red_team": (
            red_team.risk_level.value,
            RedTeamRiskLevel.LOW.value,
            red_team.risk_level == RedTeamRiskLevel.LOW,
        ),
        "failed_stage3_yellow_calibrated_total": (
            score.total_score,
            stage3_yellow_min,
            score.total_score >= stage3_yellow_min,
        ),
    }
    checks["failed_stage2_red_team"] = (red_team.has_hard_break, False, not red_team.has_hard_break)

    failed = tuple(name for name, (_, _, passed) in checks.items() if not passed)
    stage2_names = {
        "failed_stage2_total_score",
        "failed_stage2_eps_fcf",
        "failed_stage2_valuation",
        "failed_stage2_information_confidence",
        "failed_stage2_red_team",
    }
    stage3_names = {
        "failed_stage3_total_score",
        "failed_stage3_eps_fcf",
        "failed_stage3_visibility",
        "failed_stage3_bottleneck",
        "failed_stage3_market_mispricing",
        "failed_stage3_valuation",
        "failed_stage3_revision",
        "failed_structural_visibility_quality",
        "failed_report_date_confidence",
        "failed_stage3_one_off_shortage_risk",
        "failed_stage3_red_team",
    }
    values = {
        name: {"value": value, "threshold": threshold, "passed": passed}
        for name, (value, threshold, passed) in checks.items()
    }
    return StageGateDiagnostics(
        stage2_gate_passed=not any(name in failed for name in stage2_names),
        stage3_green_gate_passed=not any(name in failed for name in stage3_names),
        failed_gate_names=failed,
        values_vs_thresholds=values,
        sector_profile=sector_profile,
        structural_visibility_quality=structural_visibility_quality,
        sector_visibility_score=sector_visibility_score,
        sector_bottleneck_score=sector_bottleneck_score,
        cross_evidence_families_present=present_families,
        missing_evidence_families=missing_families,
        promotion_band=promotion_band(score),
    )


def _diagnostic(score: ScoreSnapshot, key: str, default: float = 0.0) -> float:
    value = score.diagnostic_scores.get(key, default)
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


_EVIDENCE_FAMILIES = (
    "price",
    "financial_actual",
    "disclosure",
    "research_report",
    "consensus",
    "consensus_revision",
    "news",
)


def _present_evidence_families(score: ScoreSnapshot) -> tuple[str, ...]:
    return tuple(
        family
        for family in _EVIDENCE_FAMILIES
        if _diagnostic(score, f"evidence_family_{family}", 0.0) >= 1.0
    )


def promotion_band(score: ScoreSnapshot, deterministic_stage: Stage | None = None) -> str:
    """Return report-facing promotion band without overriding the stage."""

    stage = deterministic_stage
    if stage == Stage.STAGE_3_GREEN:
        return "Stage 3-Green"
    if stage == Stage.STAGE_3_YELLOW:
        return "Stage 3-Yellow"
    if stage == Stage.STAGE_3_RED:
        return "Stage 3-Red"
    revision_score = _diagnostic(score, "revision_score")
    structural_visibility_quality = _diagnostic(
        score,
        "structural_visibility_quality",
        _diagnostic(score, "contract_quality", 0.0),
    )
    cross_evidence_family_count = _diagnostic(score, "cross_evidence_family_count")
    if (
        score.total_score >= 75.0
        and score.eps_fcf_explosion_score >= 14.0
        and revision_score >= 45.0
        and structural_visibility_quality >= 45.0
        and cross_evidence_family_count >= 3.0
    ):
        return "Stage 3-Watch"
    if (
        score.total_score >= 65.0
        and score.eps_fcf_explosion_score >= 10.0
        and score.valuation_rerating_score >= 7.0
        and score.information_confidence_score >= 3.0
    ):
        return "Stage 2-High"
    if score.total_score >= 65.0:
        return "Stage 2"
    return "Stage 1"


__all__ = ["StageGateDiagnostics", "diagnose_stage_gates", "promotion_band"]
