"""Diagnostic view of Stage 2 and Stage 3 gate failures.

This module mirrors the classifier thresholds without changing them.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from e2r.diagnostic_values import numeric_diagnostic
from e2r.models import ScoreSnapshot, Stage
from e2r.red_team import RedTeamAssessment, RedTeamRiskLevel
from e2r.score_validity import is_score_valid, score_block_reason
from e2r.sector_profiles import profile_name_from_diagnostic
from e2r.calibration.scoring_profile import get_active_scoring_profile
from e2r.staging import STAGE_3_GREEN_MIN_REVISION_SCORE

_COMPONENT_SCORE_ATTRS = {
    "eps_fcf_explosion": "eps_fcf_explosion_score",
    "earnings_visibility": "earnings_visibility_score",
    "bottleneck_pricing": "bottleneck_pricing_score",
    "market_mispricing": "market_mispricing_score",
    "valuation_rerating": "valuation_rerating_score",
    "capital_allocation": "capital_allocation_score",
    "information_confidence": "information_confidence_score",
}
_COMPONENT_CANONICAL_MAX = {
    "eps_fcf_explosion": 20.0,
    "earnings_visibility": 20.0,
    "bottleneck_pricing": 20.0,
    "market_mispricing": 15.0,
    "valuation_rerating": 15.0,
    "capital_allocation": 5.0,
    "information_confidence": 5.0,
}


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

    if not is_score_valid(score):
        reason = score_block_reason(score) or "score_invalid"
        return StageGateDiagnostics(
            stage2_gate_passed=False,
            stage3_green_gate_passed=False,
            failed_gate_names=("failed_score_validity",),
            values_vs_thresholds={
                "failed_score_validity": {
                    "value": reason,
                    "threshold": "score_valid=true",
                    "passed": False,
                }
            },
            promotion_band="Score Pending",
        )

    revision_score = _diagnostic(score, "revision_score")
    contract_quality = _diagnostic(score, "contract_quality", 100.0)
    structural_visibility_quality = _diagnostic(score, "structural_visibility_quality", contract_quality)
    sector_visibility_score = _diagnostic(score, "sector_visibility_score")
    sector_bottleneck_score = _diagnostic(score, "sector_bottleneck_score")
    cross_evidence_family_count = _diagnostic(score, "cross_evidence_family_count", 3.0)
    report_date_confidence = _diagnostic(score, "report_date_confidence", 100.0)
    domain_specific_evidence_score = _diagnostic(score, "domain_specific_evidence_score", sector_visibility_score)
    one_off_shortage_risk = _diagnostic(score, "one_off_shortage_risk", invalid_default=70.0)
    price_only_blowoff_score = _diagnostic(score, "price_only_blowoff_score", invalid_default=70.0)
    theme_overheat_score = _diagnostic(score, "theme_overheat_score")
    snippet_only_green_block = _diagnostic(score, "snippet_only_green_block", invalid_default=1.0)
    archetype_green_restricted = _diagnostic(score, "archetype_green_restricted_by_profile", invalid_default=1.0)
    emerging_theme_active = _diagnostic(score, "emerging_theme_active", invalid_default=100.0)
    llm_deep_research_completed = _diagnostic(score, "llm_deep_research_completed")
    green_unlock_evidence_score = _diagnostic(score, "green_unlock_evidence_score")
    date_unverified_snippet_count = _diagnostic(
        score,
        "date_unverified_snippet_news_count_capped",
        invalid_default=1.0,
    )
    date_unverified_document_count = _diagnostic(
        score,
        "date_unverified_document_count_capped",
        invalid_default=1.0,
    )
    date_unverified_evidence_count = max(date_unverified_snippet_count, date_unverified_document_count)
    date_verified_evidence_available = report_date_confidence >= 1.0
    green_date_evidence_clean = date_unverified_evidence_count <= 0.0
    emerging_theme_date_verified_evidence = green_date_evidence_clean and date_verified_evidence_available
    stage2_required_bridge_match = _diagnostic(score, "v12_scope_stage2_required_bridge_match")
    sector_profile = profile_name_from_diagnostic(_diagnostic(score, "sector_profile_id", 0.0))
    contract_required_for_green = _contract_required_for_green(score, sector_profile)
    present_families = _present_evidence_families(score)
    missing_families = tuple(family for family in _EVIDENCE_FAMILIES if family not in present_families)
    profile = get_active_scoring_profile()
    stage2_total_min = profile.threshold("stage2_total_min", 65.0)
    stage3_yellow_min = profile.threshold("stage3_yellow_total_min", 80.0)
    stage3_green_min = profile.threshold("stage3_green_total_min", 85.0)
    stage3_revision_min = profile.threshold("stage3_green_revision_min", STAGE_3_GREEN_MIN_REVISION_SCORE)
    price_only_threshold = 60.0 if (
        profile.guardrail_enabled("rolling_calibration_enabled")
        and _diagnostic(score, "v12_scope_local_4b_watch_guard_match") > 0
    ) else 70.0
    price_only_blocks_positive_stage = (
        profile.guardrail_enabled("price_only_blowoff_blocks_positive_stage")
        and price_only_blowoff_score >= price_only_threshold
    )
    stage2_non_price_bridge_required = (
        profile.guardrail_enabled("rolling_calibration_enabled")
        and stage2_required_bridge_match > 0
    )

    stage2_eps = _component_gate(score, "eps_fcf_explosion", profile.threshold("stage2_eps_fcf_min", 10.0))
    stage2_valuation = _component_gate(score, "valuation_rerating", profile.threshold("stage2_valuation_min", 7.0))
    stage2_info = _component_gate(
        score,
        "information_confidence",
        profile.threshold("stage2_information_confidence_min", 3.0),
    )
    stage3_eps = _component_gate(score, "eps_fcf_explosion", profile.threshold("stage3_green_eps_fcf_min", 17.0))
    stage3_visibility = _component_gate(
        score,
        "earnings_visibility",
        profile.threshold("stage3_green_visibility_min", 15.0),
    )
    stage3_bottleneck = _component_gate(
        score,
        "bottleneck_pricing",
        profile.threshold("stage3_green_bottleneck_min", 15.0),
    )
    stage3_mispricing = _component_gate(
        score,
        "market_mispricing",
        profile.threshold("stage3_green_mispricing_min", 10.0),
    )
    stage3_valuation = _component_gate(
        score,
        "valuation_rerating",
        profile.threshold("stage3_green_valuation_min", 10.0),
    )

    checks: dict[str, tuple[float | str | bool, float | str | bool, bool]] = {
        "failed_stage2_total_score": (score.total_score, stage2_total_min, score.total_score >= stage2_total_min),
        "failed_stage2_eps_fcf": stage2_eps,
        "failed_stage2_valuation": stage2_valuation,
        "failed_stage2_information_confidence": stage2_info,
        "failed_stage3_total_score": (score.total_score, stage3_green_min, score.total_score >= stage3_green_min),
        "failed_stage3_eps_fcf": stage3_eps,
        "failed_stage3_visibility": stage3_visibility,
        "failed_stage3_bottleneck": stage3_bottleneck,
        "failed_stage3_market_mispricing": stage3_mispricing,
        "failed_stage3_valuation": stage3_valuation,
        "failed_stage3_revision": (
            revision_score,
            stage3_revision_min,
            revision_score >= stage3_revision_min,
        ),
        "failed_stage3_contract_quality": (
            contract_quality,
            45.0,
            contract_quality >= 45.0 or contract_required_for_green < 1.0,
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
        "failed_date_unverified_green_evidence": (
            (
                f"date_unverified_snippets={date_unverified_snippet_count}; "
                f"date_unverified_documents={date_unverified_document_count}"
            ),
            "no date-unverified snippets or documents",
            green_date_evidence_clean,
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
        "failed_archetype_green_policy_restriction": (
            archetype_green_restricted,
            0.0,
            archetype_green_restricted <= 0.0,
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
    if profile.guardrail_enabled("price_only_blowoff_blocks_positive_stage"):
        checks["failed_positive_stage_price_only_blowoff"] = (
            price_only_blowoff_score,
            price_only_threshold,
            not price_only_blocks_positive_stage,
        )
    if stage2_non_price_bridge_required:
        checks["failed_stage2_non_price_bridge"] = (
            _non_price_bridge_count(score),
            2.0,
            _has_non_price_stage2_bridge(score),
        )
    checks["failed_snippet_only_green_block"] = (
        snippet_only_green_block,
        0.0,
        snippet_only_green_block <= 0.0,
    )
    if emerging_theme_active > 0:
        checks["failed_emerging_theme_deep_research"] = (
            llm_deep_research_completed,
            100.0,
            llm_deep_research_completed >= 100.0,
        )
        checks["failed_emerging_theme_green_unlock_evidence"] = (
            green_unlock_evidence_score,
            60.0,
            green_unlock_evidence_score >= 60.0,
        )
        checks["failed_emerging_theme_date_verified_evidence"] = (
            (
                f"date_unverified_snippets={date_unverified_snippet_count}; "
                f"date_unverified_documents={date_unverified_document_count}; "
                f"report_date_confidence={report_date_confidence}"
            ),
            "no date-unverified snippets and report_date_confidence>=1",
            emerging_theme_date_verified_evidence,
        )
    if theme_overheat_score > 0:
        checks["failed_theme_overheat_risk"] = (
            theme_overheat_score,
            70.0,
            theme_overheat_score < 70.0,
        )

    failed = tuple(name for name, (_, _, passed) in checks.items() if not passed)
    stage2_names = {
        "failed_stage2_total_score",
        "failed_stage2_eps_fcf",
        "failed_stage2_valuation",
        "failed_stage2_information_confidence",
        "failed_stage2_red_team",
        "failed_stage2_non_price_bridge",
        "failed_positive_stage_price_only_blowoff",
    }
    stage3_names = {
        "failed_stage3_total_score",
        "failed_stage3_eps_fcf",
        "failed_stage3_visibility",
        "failed_stage3_bottleneck",
        "failed_stage3_market_mispricing",
        "failed_stage3_valuation",
        "failed_stage3_revision",
        "failed_stage3_contract_quality",
        "failed_structural_visibility_quality",
        "failed_report_date_confidence",
        "failed_date_unverified_green_evidence",
        "failed_archetype_green_policy_restriction",
        "failed_stage3_one_off_shortage_risk",
        "failed_stage3_red_team",
        "failed_positive_stage_price_only_blowoff",
        "failed_snippet_only_green_block",
        "failed_emerging_theme_deep_research",
        "failed_emerging_theme_green_unlock_evidence",
        "failed_emerging_theme_date_verified_evidence",
        "failed_theme_overheat_risk",
    }
    values = {}
    for name, (value, threshold, passed) in checks.items():
        detail: dict[str, float | str | bool] = {"value": value, "threshold": threshold, "passed": passed}
        if component_key := _COMPONENT_GATE_NAMES.get(name):
            raw_value = _raw_component_score(score, component_key)
            raw_threshold = _canonical_threshold_for_gate(name, profile)
            detail["raw_value"] = round(raw_value, 4)
            detail["raw_threshold"] = round(raw_threshold, 4)
            detail["archetype_weighted"] = _diagnostic(
                score,
                "archetype_weight_profile_applied",
                invalid_default=1.0,
            ) > 0
        values[name] = detail
    stage2_gate_passed = not any(name in failed for name in stage2_names)
    stage3_green_gate_passed = not any(name in failed for name in stage3_names)
    report_band = "Stage 3-Green" if stage3_green_gate_passed else promotion_band(score)
    return StageGateDiagnostics(
        stage2_gate_passed=stage2_gate_passed,
        stage3_green_gate_passed=stage3_green_gate_passed,
        failed_gate_names=failed,
        values_vs_thresholds=values,
        sector_profile=sector_profile,
        structural_visibility_quality=structural_visibility_quality,
        sector_visibility_score=sector_visibility_score,
        sector_bottleneck_score=sector_bottleneck_score,
        cross_evidence_families_present=present_families,
        missing_evidence_families=missing_families,
        promotion_band=report_band,
    )


def _diagnostic(
    score: ScoreSnapshot,
    key: str,
    default: float = 0.0,
    *,
    invalid_default: float = 0.0,
) -> float:
    return numeric_diagnostic(score.diagnostic_scores, key, default, invalid_default=invalid_default)


_COMPONENT_GATE_NAMES = {
    "failed_stage2_eps_fcf": "eps_fcf_explosion",
    "failed_stage2_valuation": "valuation_rerating",
    "failed_stage2_information_confidence": "information_confidence",
    "failed_stage3_eps_fcf": "eps_fcf_explosion",
    "failed_stage3_visibility": "earnings_visibility",
    "failed_stage3_bottleneck": "bottleneck_pricing",
    "failed_stage3_market_mispricing": "market_mispricing",
    "failed_stage3_valuation": "valuation_rerating",
}


def _component_gate(score: ScoreSnapshot, key: str, canonical_threshold: float) -> tuple[float, float, bool]:
    value = _effective_component_score(score, key)
    threshold = _effective_component_threshold(score, key, canonical_threshold)
    return value, threshold, value >= threshold


def _effective_component_score(score: ScoreSnapshot, key: str) -> float:
    if _diagnostic(score, "archetype_weight_profile_applied", invalid_default=1.0) > 0:
        return _diagnostic(score, f"archetype_component_{key}", _raw_component_score(score, key))
    return _raw_component_score(score, key)


def _contract_required_for_green(score: ScoreSnapshot, sector_profile: str) -> float:
    if "contract_required_for_green" in score.diagnostic_scores:
        return _diagnostic(score, "contract_required_for_green", invalid_default=1.0)
    return 1.0 if sector_profile in {"POWER_EQUIPMENT", "DEFENSE", "BATTERY_OVERHEAT"} else 0.0


def _effective_component_threshold(score: ScoreSnapshot, key: str, canonical_threshold: float) -> float:
    if _diagnostic(score, "archetype_weight_profile_applied", invalid_default=1.0) <= 0:
        return round(float(canonical_threshold), 4)
    return _weighted_component_threshold(score, key, canonical_threshold)


def _weighted_component_threshold(score: ScoreSnapshot, key: str, canonical_threshold: float) -> float:
    canonical_max = _COMPONENT_CANONICAL_MAX[key]
    weight_max = _diagnostic(
        score,
        f"archetype_weight_{key}",
        canonical_max,
        invalid_default=canonical_max,
    )
    return round(weight_max * float(canonical_threshold) / canonical_max, 4)


def _raw_component_score(score: ScoreSnapshot, key: str) -> float:
    return float(getattr(score, _COMPONENT_SCORE_ATTRS[key]))


def _canonical_threshold_for_gate(gate_name: str, profile) -> float:
    if gate_name == "failed_stage2_eps_fcf":
        return profile.threshold("stage2_eps_fcf_min", 10.0)
    if gate_name == "failed_stage2_valuation":
        return profile.threshold("stage2_valuation_min", 7.0)
    if gate_name == "failed_stage2_information_confidence":
        return profile.threshold("stage2_information_confidence_min", 3.0)
    if gate_name == "failed_stage3_eps_fcf":
        return profile.threshold("stage3_green_eps_fcf_min", 17.0)
    if gate_name == "failed_stage3_visibility":
        return profile.threshold("stage3_green_visibility_min", 15.0)
    if gate_name == "failed_stage3_bottleneck":
        return profile.threshold("stage3_green_bottleneck_min", 15.0)
    if gate_name == "failed_stage3_market_mispricing":
        return profile.threshold("stage3_green_mispricing_min", 10.0)
    if gate_name == "failed_stage3_valuation":
        return profile.threshold("stage3_green_valuation_min", 10.0)
    return 0.0


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


def _non_price_bridge_count(score: ScoreSnapshot) -> float:
    non_price_families = (
        "evidence_family_financial_actual",
        "evidence_family_disclosure",
        "evidence_family_research_report",
        "evidence_family_consensus",
        "evidence_family_consensus_revision",
        "evidence_family_news",
    )
    return float(sum(1 for key in non_price_families if _diagnostic(score, key) > 0))


def _has_non_price_stage2_bridge(score: ScoreSnapshot) -> bool:
    if _diagnostic(score, "calibration_stage2_actionable_evidence") > 0:
        return True
    if _diagnostic(score, "credible_order_or_policy_evidence") > 0:
        return True
    return _non_price_bridge_count(score) >= 2.0 or _diagnostic(score, "cross_evidence_family_count") >= 3.0


def promotion_band(score: ScoreSnapshot, deterministic_stage: Stage | None = None) -> str:
    """Return report-facing promotion band without overriding the stage."""

    if not is_score_valid(score):
        return "Score Pending"
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
    profile = get_active_scoring_profile()
    if (
        score.total_score >= 75.0
        and _component_gate(score, "eps_fcf_explosion", 14.0)[2]
        and revision_score >= 45.0
        and structural_visibility_quality >= 45.0
        and cross_evidence_family_count >= 3.0
    ):
        return "Stage 3-Watch"
    if (
        score.total_score >= 65.0
        and _component_gate(score, "eps_fcf_explosion", profile.threshold("stage2_eps_fcf_min", 10.0))[2]
        and _component_gate(score, "valuation_rerating", profile.threshold("stage2_valuation_min", 7.0))[2]
        and _component_gate(
            score,
            "information_confidence",
            profile.threshold("stage2_information_confidence_min", 3.0),
        )[2]
    ):
        return "Stage 2-High"
    if score.total_score >= 65.0:
        return "Stage 2"
    return "Stage 1"


__all__ = ["StageGateDiagnostics", "diagnose_stage_gates", "promotion_band"]
