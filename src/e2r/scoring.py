"""Deterministic E2R 2.0 scoring interface."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import date
import math
from typing import Mapping, Protocol

from .calibration.archetype_weight_profile import (
    RUNTIME_WEIGHT_PROFILE_PATH,
    WeightedComponents,
    load_archetype_weight_profile,
)
from .calibration.scoring_profile import get_active_scoring_profile
from .calibration.taxonomy import large_sector_for_archetype, normalise_canonical_archetype_id, normalise_large_sector_id
from .diagnostic_values import numeric_diagnostic
from .agentic import ScoreContributionV2
from .models import IndustrialSubScores, ScoreContribution, ScoreSnapshot


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
_SIGNED_DIAGNOSTIC_KEYS = frozenset({"calibration_total_adjustment"})


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
    score_contribution_claim_ids: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    score_contributions_v2: tuple[ScoreContributionV2, ...] = field(default_factory=tuple)
    scoring_version: str = "e2r-2.0-cp1"
    large_sector_id: str | None = None
    canonical_archetype_id: str | None = None

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
            try:
                number = float(value)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{key} must be numeric") from exc
            if not math.isfinite(number) or number < 0 or number > max_points:
                raise ValueError(f"{key} must be between 0 and {max_points}")
            component_copy[key] = number
        try:
            risk_penalty = float(self.risk_penalty)
        except (TypeError, ValueError) as exc:
            raise ValueError("risk_penalty must be numeric") from exc
        if not math.isfinite(risk_penalty) or risk_penalty < 0:
            raise ValueError("risk_penalty must be non-negative")
        diagnostic_copy: dict[str, float] = {}
        for key, value in self.diagnostic_scores.items():
            if not isinstance(key, str) or not key.strip():
                raise ValueError("diagnostic score keys must be non-empty strings")
            try:
                number = float(value)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"diagnostic score {key} must be numeric") from exc
            if not math.isfinite(number):
                raise ValueError(f"diagnostic score {key} must be finite")
            min_value = -100.0 if key in _SIGNED_DIAGNOSTIC_KEYS else 0.0
            if number < min_value or number > 100:
                raise ValueError(f"diagnostic score {key} must be between {min_value:g} and 100")
            diagnostic_copy[key] = number
        if self.industrial_sub_scores is not None and not isinstance(self.industrial_sub_scores, IndustrialSubScores):
            raise ValueError("industrial_sub_scores must be an IndustrialSubScores instance")
        contribution_claims: dict[str, tuple[str, ...]] = {}
        for key, claim_ids in self.score_contribution_claim_ids.items():
            if key not in _MAX_POINTS_BY_KEY:
                raise ValueError(f"unknown score contribution component: {key}")
            contribution_claims[key] = tuple(dict.fromkeys(str(item) for item in claim_ids if str(item).strip()))
        for item in self.score_contributions_v2:
            if not isinstance(item, ScoreContributionV2):
                raise ValueError("score_contributions_v2 must contain ScoreContributionV2 instances")
            if item.component_key not in _MAX_POINTS_BY_KEY:
                raise ValueError(f"unknown v2 score contribution component: {item.component_key}")
        if not isinstance(self.scoring_version, str) or not self.scoring_version.strip():
            raise ValueError("scoring_version must be a non-empty string")
        if self.large_sector_id is not None and (
            not isinstance(self.large_sector_id, str) or not self.large_sector_id.strip()
        ):
            raise ValueError("large_sector_id must be a non-empty string when provided")
        if self.canonical_archetype_id is not None and (
            not isinstance(self.canonical_archetype_id, str) or not self.canonical_archetype_id.strip()
        ):
            raise ValueError("canonical_archetype_id must be a non-empty string when provided")
        object.__setattr__(self, "components", component_copy)
        object.__setattr__(self, "risk_penalty", risk_penalty)
        object.__setattr__(self, "diagnostic_scores", diagnostic_copy)
        object.__setattr__(self, "evidence_ids", tuple(self.evidence_ids))
        object.__setattr__(self, "score_contribution_claim_ids", contribution_claims)
        object.__setattr__(self, "score_contributions_v2", tuple(self.score_contributions_v2))
        if self.large_sector_id is not None:
            object.__setattr__(self, "large_sector_id", normalise_large_sector_id(self.large_sector_id))
        if self.canonical_archetype_id is not None:
            object.__setattr__(self, "canonical_archetype_id", normalise_canonical_archetype_id(self.canonical_archetype_id))


class Scorer(Protocol):
    """Scoring contract used by later pipeline checkpoints."""

    def score(self, payload: ScoringPayload) -> ScoreSnapshot:
        """Return a deterministic score snapshot."""


class ArchetypeClassificationError(ValueError):
    """Raised when rolling scoring is requested without a resolved v12 taxonomy."""


def _payload_with_v2_score_components(payload: ScoringPayload) -> ScoringPayload:
    if not payload.score_contributions_v2:
        return payload
    components = _components_from_v2_contributions(payload.score_contributions_v2)
    diagnostics = dict(payload.diagnostic_scores)
    diagnostics["score_contribution_v2_component_input_used"] = 100.0
    risk_penalty = 0.0
    if payload.risk_penalty > 0.0:
        diagnostics["score_contribution_v2_legacy_risk_penalty_quarantined"] = 100.0
        diagnostics["raw_legacy_risk_penalty_before_v2_quarantine"] = round(float(payload.risk_penalty), 4)
    return replace(payload, components=components, risk_penalty=risk_penalty, diagnostic_scores=diagnostics)


def _components_from_v2_contributions(
    score_contributions_v2: tuple[ScoreContributionV2, ...],
) -> dict[str, float]:
    components = {spec.key: 0.0 for spec in CANONICAL_SCORE_COMPONENTS}
    for item in score_contributions_v2:
        max_points = _MAX_POINTS_BY_KEY[item.component_key]
        components[item.component_key] = min(
            max_points,
            components[item.component_key] + max(float(item.raw_points), 0.0),
        )
    return {key: round(value, 4) for key, value in components.items()}


class DeterministicScorer:
    """Canonical E2R 2.0 component scorer."""

    def score(self, payload: ScoringPayload) -> ScoreSnapshot:
        payload = _payload_with_v2_score_components(payload)
        profile = get_active_scoring_profile()
        diagnostic_scores = dict(payload.diagnostic_scores)
        weighted = _apply_archetype_runtime_weights(payload, profile)
        diagnostic_scores.update(weighted.diagnostics)
        calibration_bonus = 0.0
        calibration_risk_penalty = 0.0

        if numeric_diagnostic(diagnostic_scores, "calibration_stage2_actionable_evidence") > 0:
            calibration_bonus += profile.adjustment("stage2_actionable_evidence_bonus")
        if numeric_diagnostic(diagnostic_scores, "credible_order_or_policy_evidence") > 0:
            calibration_bonus += profile.adjustment("stage2_actionable_evidence_bonus")
        if numeric_diagnostic(diagnostic_scores, "high_mae_risk") > 0:
            calibration_risk_penalty += profile.adjustment("high_mae_risk_guard_penalty")
        if numeric_diagnostic(diagnostic_scores, "stage2_actionable_volatility_risk") > 0:
            calibration_risk_penalty += profile.adjustment("stage2_actionable_volatility_guard_penalty")
        if _has_stage3_cross_evidence_buffer(payload, diagnostic_scores, profile):
            calibration_bonus += profile.adjustment("stage3_cross_evidence_green_buffer")
            diagnostic_scores["stage3_cross_evidence_buffer_applied"] = 1.0
        scope_labels = _scope_labels(payload)
        if _v12_stage2_bonus_applies(payload, diagnostic_scores, profile, scope_labels):
            calibration_bonus += min(1.0, profile.adjustment("v12_stage2_archetype_bonus", 1.0))
            diagnostic_scores["v12_stage2_scope_bonus_applied"] = 1.0

        _annotate_v12_scope_matches(diagnostic_scores, profile, scope_labels)

        diagnostic_scores["active_scoring_profile"] = (
            1.0 if profile.profile_id.endswith("calibrated") or "rolling" in profile.profile_id else 0.0
        )
        diagnostic_scores["calibration_total_adjustment"] = round(calibration_bonus - calibration_risk_penalty, 4)
        diagnostic_scores.setdefault("score_valid", 100.0)
        contribution_audit = _score_contribution_claim_diagnostics(payload)
        diagnostic_scores.update(contribution_audit)
        contribution_blocked = contribution_audit.get("score_blocked_by_orphan_score_contribution", 0.0) > 0.0
        if contribution_blocked:
            diagnostic_scores["score_valid"] = 0.0
        _apply_source_backed_deep_research_unlock(diagnostic_scores)

        raw_total = sum(weighted.components.values()) + calibration_bonus - payload.risk_penalty - calibration_risk_penalty
        source_backed_floor = None if contribution_blocked else _source_backed_green_total_floor(payload, diagnostic_scores, profile, raw_total)
        if source_backed_floor is not None:
            raw_total = max(raw_total, source_backed_floor)
            diagnostic_scores["source_backed_green_total_floor_applied"] = 1.0
            diagnostic_scores["source_backed_green_total_floor"] = round(source_backed_floor, 4)
        if contribution_blocked:
            raw_total = 0.0
        total_score = round(max(0.0, min(100.0, raw_total)), 4)
        if payload.industrial_sub_scores is not None:
            diagnostic_scores.update(payload.industrial_sub_scores.as_diagnostic_scores())
        evidence_ids = payload.evidence_ids + (
            payload.industrial_sub_scores.evidence_ids if payload.industrial_sub_scores else ()
        )
        snapshot_components = dict(payload.components)
        if contribution_blocked:
            snapshot_components = {key: 0.0 for key in snapshot_components}
        return ScoreSnapshot(
            symbol=payload.symbol,
            as_of_date=payload.as_of_date,
            eps_fcf_explosion_score=snapshot_components["eps_fcf_explosion"],
            earnings_visibility_score=snapshot_components["earnings_visibility"],
            bottleneck_pricing_score=snapshot_components["bottleneck_pricing"],
            market_mispricing_score=snapshot_components["market_mispricing"],
            valuation_rerating_score=snapshot_components["valuation_rerating"],
            capital_allocation_score=snapshot_components["capital_allocation"],
            information_confidence_score=snapshot_components["information_confidence"],
            risk_penalty=0.0 if contribution_blocked else payload.risk_penalty,
            total_score=total_score,
            diagnostic_scores=diagnostic_scores,
            evidence_ids=tuple(dict.fromkeys(evidence_ids)),
            score_contribution_claim_ids=_score_contribution_claim_ids_for_snapshot(payload, snapshot_components),
            score_contribution_ledger=_score_contribution_ledger(
                snapshot_components,
                _legacy_score_contribution_claim_ids_for_components(payload.score_contribution_claim_ids, snapshot_components),
                payload.score_contributions_v2,
            ),
            scoring_version=_scoring_version(payload.scoring_version, profile.profile_id, weighted),
        )


def _apply_archetype_runtime_weights(payload: ScoringPayload, profile) -> WeightedComponents:
    if not profile.guardrail_enabled("archetype_weight_runtime_enabled"):
        return WeightedComponents(components=dict(payload.components), diagnostics={}, match=None)
    profile_path = profile.guardrail_text("archetype_weight_profile_path", str(RUNTIME_WEIGHT_PROFILE_PATH))
    runtime_profile = load_archetype_weight_profile(profile_path)
    _require_runtime_archetype_classification(payload, runtime_profile)
    weighted = runtime_profile.apply(
        payload.components,
        canonical_archetype_id=payload.canonical_archetype_id,
        large_sector_id=payload.large_sector_id,
    )
    if weighted.match is None:
        raise ArchetypeClassificationError("canonical_archetype_id did not resolve to a runtime weight profile")
    diagnostics = dict(weighted.diagnostics)
    diagnostics.update(_green_policy_diagnostics(payload, weighted))
    diagnostics["archetype_weight_support_row_count_capped"] = min(float(weighted.match.support.get("row_count", 0) or 0), 100.0)
    diagnostics["archetype_weight_support_symbol_count_capped"] = min(
        float(weighted.match.support.get("unique_symbol_count", 0) or 0),
        100.0,
    )
    return WeightedComponents(components=weighted.components, diagnostics=diagnostics, match=weighted.match)


def _score_contribution_claim_diagnostics(payload: ScoringPayload) -> dict[str, float]:
    nonzero_components = tuple(key for key, value in payload.components.items() if float(value) > 0.0)
    v2_claim_ids = _score_contribution_claim_ids_from_v2(payload.score_contributions_v2)
    require_v2 = _v2_score_contributions_required(payload.diagnostic_scores)
    claim_ids_by_component = v2_claim_ids if require_v2 else (v2_claim_ids or payload.score_contribution_claim_ids)
    claim_backed_components = tuple(
        key
        for key in nonzero_components
        if claim_ids_by_component.get(key)
    )
    orphan_components = tuple(key for key in nonzero_components if key not in claim_backed_components)
    require_claims = require_v2 or _claim_backed_score_required(payload.diagnostic_scores)
    nonzero_count = len(nonzero_components)
    claim_backed_count = len(claim_backed_components)
    orphan_count = len(orphan_components)
    ratio = claim_backed_count / nonzero_count * 100.0 if nonzero_count else 100.0
    diagnostics = {
        "score_nonzero_component_count_capped": min(float(nonzero_count), 100.0),
        "score_claim_backed_component_count_capped": min(float(claim_backed_count), 100.0),
        "orphan_score_component_count_capped": min(float(orphan_count), 100.0),
        "score_claim_backed_component_ratio": round(min(max(ratio, 0.0), 100.0), 4),
        "score_claim_backed_required": 100.0 if require_claims else 0.0,
        "score_contribution_v2_required": 100.0 if require_v2 else 0.0,
        "score_contribution_v2_input_count_capped": min(float(len(payload.score_contributions_v2)), 100.0),
        "score_contribution_v2_used": 100.0 if v2_claim_ids else 0.0,
    }
    if require_claims and orphan_count:
        diagnostics["score_blocked_by_orphan_score_contribution"] = 100.0
    return diagnostics


def _v2_score_contributions_required(diagnostics: Mapping[str, float]) -> bool:
    return any(
        numeric_diagnostic(diagnostics, key) > 0.0
        for key in (
            "require_v2_score_contributions",
            "agentic_evidence_required_for_scoring",
        )
    )


def _claim_backed_score_required(diagnostics: Mapping[str, float]) -> bool:
    return any(
        numeric_diagnostic(diagnostics, key) > 0.0
        for key in (
            "require_claim_backed_score_contributions",
            "source_backed_green_bridge_raw",
            "source_backed_deep_research_completed",
            "evidence_contract_green_gate_required_primitive_count_capped",
        )
    )


def _score_contribution_ledger(
    components: Mapping[str, float],
    claim_ids_by_component: Mapping[str, tuple[str, ...]],
    score_contributions_v2: tuple[ScoreContributionV2, ...] = (),
) -> tuple[ScoreContribution, ...]:
    v2_rows = _score_contribution_ledger_from_v2(components, score_contributions_v2)
    if v2_rows is not None:
        return v2_rows
    rows: list[ScoreContribution] = []
    for spec in CANONICAL_SCORE_COMPONENTS:
        raw_points = float(components[spec.key])
        support_claim_ids = tuple(claim_ids_by_component.get(spec.key, ()))
        if raw_points <= 0.0:
            rationale = "zero component score"
            confidence = 1.0
        elif support_claim_ids:
            rationale = "component score has claim-backed support"
            confidence = 1.0
        else:
            rationale = "component score has no support_claim_ids"
            confidence = 0.0
        rows.append(
            ScoreContribution(
                component_key=spec.key,
                criterion_id=spec.key,
                raw_points=raw_points,
                max_points=spec.max_points,
                support_claim_ids=support_claim_ids,
                rationale=rationale,
                confidence=confidence,
                cap_reason=None if support_claim_ids or raw_points <= 0.0 else "missing_support_claim_ids",
            )
        )
    return tuple(rows)


def _score_contribution_claim_ids_for_snapshot(
    payload: ScoringPayload,
    components: Mapping[str, float],
) -> Mapping[str, tuple[str, ...]]:
    return _score_contribution_claim_ids_from_v2(
        payload.score_contributions_v2,
        components=components,
    ) or _legacy_score_contribution_claim_ids_for_components(payload.score_contribution_claim_ids, components)


def _score_contribution_claim_ids_from_v2(
    score_contributions_v2: tuple[ScoreContributionV2, ...],
    *,
    components: Mapping[str, float] | None = None,
) -> dict[str, tuple[str, ...]]:
    by_component: dict[str, list[str]] = {}
    for item in score_contributions_v2:
        if item.raw_points <= 0.0:
            continue
        if components is not None and float(components.get(item.component_key, 0.0)) <= 0.0:
            continue
        by_component.setdefault(item.component_key, []).extend(item.support_claim_ids)
    return {
        component: tuple(dict.fromkeys(claim_ids))
        for component, claim_ids in by_component.items()
        if claim_ids
    }


def _legacy_score_contribution_claim_ids_for_components(
    claim_ids_by_component: Mapping[str, tuple[str, ...]],
    components: Mapping[str, float],
) -> Mapping[str, tuple[str, ...]]:
    return {
        component: tuple(dict.fromkeys(claim_ids))
        for component, claim_ids in claim_ids_by_component.items()
        if float(components.get(component, 0.0)) > 0.0 and claim_ids
    }


def _score_contribution_ledger_from_v2(
    components: Mapping[str, float],
    score_contributions_v2: tuple[ScoreContributionV2, ...],
) -> tuple[ScoreContribution, ...] | None:
    if not score_contributions_v2:
        return None
    by_component: dict[str, list[ScoreContributionV2]] = {}
    for item in score_contributions_v2:
        by_component.setdefault(item.component_key, []).append(item)
    rows: list[ScoreContribution] = []
    for spec in CANONICAL_SCORE_COMPONENTS:
        raw_points = float(components[spec.key])
        rows_for_component = by_component.get(spec.key, ())
        support_claim_ids = tuple(
            dict.fromkeys(
                claim_id
                for item in rows_for_component
                if item.raw_points > 0.0
                for claim_id in item.support_claim_ids
            )
        )
        counter_claim_ids = tuple(
            dict.fromkeys(claim_id for item in rows_for_component for claim_id in item.counter_claim_ids)
        )
        cap_reasons = tuple(dict.fromkeys(str(item.cap_reason) for item in rows_for_component if item.cap_reason))
        if raw_points <= 0.0:
            rationale = "zero component score"
            confidence = 1.0
        elif support_claim_ids:
            rationale = "component score has v2 claim-backed support"
            confidence = 1.0
        else:
            rationale = "component score has no v2 support_claim_ids"
            confidence = 0.0
        rows.append(
            ScoreContribution(
                component_key=spec.key,
                criterion_id=spec.key,
                raw_points=raw_points,
                max_points=spec.max_points,
                support_claim_ids=support_claim_ids,
                counter_claim_ids=counter_claim_ids,
                rationale=rationale,
                confidence=confidence,
                cap_reason=";".join(cap_reasons) if cap_reasons else (None if support_claim_ids or raw_points <= 0.0 else "missing_v2_support_claim_ids"),
            )
        )
    return tuple(rows)


def _apply_source_backed_deep_research_unlock(diagnostics: dict[str, float]) -> None:
    unlock_score = _source_backed_deep_research_unlock_score(diagnostics)
    if unlock_score < 60.0:
        return
    diagnostics["source_backed_deep_research_completed"] = 100.0
    diagnostics["green_unlock_evidence_score"] = round(
        max(numeric_diagnostic(diagnostics, "green_unlock_evidence_score"), unlock_score),
        4,
    )


def _source_backed_deep_research_unlock_score(diagnostics: Mapping[str, float]) -> float:
    source_bridge = numeric_diagnostic(diagnostics, "source_backed_green_bridge_raw")
    if source_bridge < 90.0:
        return 0.0
    if numeric_diagnostic(diagnostics, "score_claim_backed_component_ratio") < 100.0:
        return 0.0
    if numeric_diagnostic(diagnostics, "orphan_score_component_count_capped") > 0.0:
        return 0.0
    claim_count = numeric_diagnostic(diagnostics, "claim_backed_claim_count_capped")
    if claim_count < 20.0:
        return 0.0
    if numeric_diagnostic(diagnostics, "report_date_confidence") < 1.0:
        return 0.0
    if numeric_diagnostic(diagnostics, "date_unverified_snippet_news_count_capped") > 0.0:
        return 0.0
    if numeric_diagnostic(diagnostics, "date_unverified_document_count_capped") > 0.0:
        return 0.0

    actual_conversion = numeric_diagnostic(diagnostics, "actual_profit_conversion_score")
    medium_revision = numeric_diagnostic(diagnostics, "medium_term_revision_visibility")
    structural_visibility = numeric_diagnostic(
        diagnostics,
        "structural_visibility_quality",
        numeric_diagnostic(diagnostics, "contract_quality"),
    )
    domain_evidence = numeric_diagnostic(diagnostics, "domain_specific_evidence_score")
    bridge_count = numeric_diagnostic(diagnostics, "research_axis_bridge_present_count_capped")
    family_count = numeric_diagnostic(diagnostics, "cross_evidence_family_count")
    if family_count < 3.0 and (source_bridge < 95.0 or claim_count < 50.0 or bridge_count < 5.0):
        return 0.0
    if actual_conversion < 55.0 or medium_revision < 55.0:
        return 0.0
    if max(structural_visibility, domain_evidence) < 55.0:
        return 0.0
    if bridge_count < 5.0:
        return 0.0
    return min(100.0, source_bridge)


def _green_policy_diagnostics(payload: ScoringPayload, weighted: WeightedComponents) -> dict[str, float]:
    if weighted.match is None:
        return {}
    green_policy = weighted.match.green_policy.lower()
    absolute_block = _green_policy_is_absolute_block(green_policy)
    conditional_unlock_required = _green_policy_requires_unlock(green_policy)
    unlock_score = _green_policy_unlock_score(payload, weighted) if conditional_unlock_required else 0.0
    source_backed_policy_override = _source_backed_green_policy_override(payload, green_policy)
    restricted = (absolute_block and not source_backed_policy_override) or (
        conditional_unlock_required and unlock_score < 60.0
    )
    return {
        "archetype_green_policy_absolute_block": 1.0 if absolute_block else 0.0,
        "archetype_green_policy_unlock_required": 1.0 if conditional_unlock_required else 0.0,
        "archetype_green_policy_unlock_evidence": round(min(max(unlock_score, 0.0), 100.0), 4),
        "archetype_green_policy_source_backed_override": 1.0 if source_backed_policy_override else 0.0,
        "archetype_green_restricted_by_profile": 1.0 if restricted else 0.0,
    }


def _green_policy_is_absolute_block(green_policy: str) -> bool:
    if any(token in green_policy for token in ("redteam_guardrail", "not_green_unlock", "red_flag")):
        return True
    return green_policy in {"red_watch", "event_only_red_watch"} or green_policy.endswith("_red_watch")


def _green_policy_requires_unlock(green_policy: str) -> bool:
    if _green_policy_is_absolute_block(green_policy):
        return False
    return any(
        token in green_policy
        for token in (
            "green_restricted",
            "watch_to_green",
            "event_only_until",
            "event_premium_not_structural_green_without",
        )
    )


def _source_backed_green_policy_override(payload: ScoringPayload, green_policy: str) -> bool:
    if green_policy not in {"red_watch", "event_only_red_watch"}:
        return False
    diagnostics = payload.diagnostic_scores
    source_bridge = numeric_diagnostic(diagnostics, "source_backed_green_bridge_raw")
    guard_risk = numeric_diagnostic(diagnostics, "research_axis_bridge_guard_risk")
    guard_penalty = numeric_diagnostic(diagnostics, "research_axis_bridge_guard_risk_penalty_points")
    bridge_count = numeric_diagnostic(diagnostics, "research_axis_bridge_present_count_capped")
    if green_policy == "event_only_red_watch":
        bio_bridge = numeric_diagnostic(diagnostics, "research_axis_bridge_bio_commercialization")
        actual_conversion = numeric_diagnostic(diagnostics, "actual_profit_conversion_score")
        return (
            source_bridge >= 95.0
            and bio_bridge >= 80.0
            and actual_conversion >= 55.0
            and guard_risk <= 0.0
            and guard_penalty <= 0.0
            and bridge_count >= 5.0
        )
    return source_bridge >= 85.0 and guard_risk <= 0.0 and guard_penalty <= 0.0 and bridge_count >= 3.0


def _source_backed_green_total_floor(
    payload: ScoringPayload,
    diagnostics: Mapping[str, float],
    profile,
    raw_total: float,
) -> float | None:
    green_total_min = profile.threshold("stage3_green_total_min", 85.0)
    near_green = raw_total >= green_total_min - 2.5
    source_backed_policy_override = numeric_diagnostic(diagnostics, "archetype_green_policy_source_backed_override") > 0.0
    rich_source_backed = (
        (raw_total >= 70.0 or source_backed_policy_override)
        and numeric_diagnostic(diagnostics, "source_backed_deep_research_completed") >= 100.0
        and numeric_diagnostic(diagnostics, "score_claim_backed_component_ratio") >= 100.0
        and numeric_diagnostic(diagnostics, "orphan_score_component_count_capped") <= 0.0
        and numeric_diagnostic(diagnostics, "claim_backed_claim_count_capped") >= 20.0
    )
    if not near_green and not rich_source_backed:
        return None
    source_bridge = numeric_diagnostic(diagnostics, "source_backed_green_bridge_raw")
    guard_risk = numeric_diagnostic(diagnostics, "research_axis_bridge_guard_risk")
    guard_penalty = numeric_diagnostic(diagnostics, "research_axis_bridge_guard_risk_penalty_points")
    bridge_count = numeric_diagnostic(diagnostics, "research_axis_bridge_present_count_capped")
    actual_conversion = numeric_diagnostic(diagnostics, "actual_profit_conversion_score")
    medium_revision = numeric_diagnostic(diagnostics, "medium_term_revision_visibility")
    structural_visibility = numeric_diagnostic(diagnostics, "structural_visibility_quality")
    domain_evidence = numeric_diagnostic(diagnostics, "domain_specific_evidence_score")
    if (
        source_bridge >= 95.0
        and guard_risk <= 0.0
        and guard_penalty <= 0.0
        and bridge_count >= 5.0
        and actual_conversion >= 55.0
        and medium_revision >= 55.0
        and max(structural_visibility, domain_evidence) >= 55.0
    ):
        if source_backed_policy_override and payload.canonical_archetype_id == "C24_BIO_TRIAL_DATA_EVENT_RISK":
            floor = green_total_min
        else:
            floor = max(green_total_min, min(source_bridge, green_total_min + 5.25))
        if raw_total >= floor:
            return None
        return floor
    return None


def _green_policy_unlock_score(payload: ScoringPayload, weighted: WeightedComponents) -> float:
    diagnostics = payload.diagnostic_scores
    revision_score = numeric_diagnostic(diagnostics, "revision_score")
    structural_visibility = numeric_diagnostic(
        diagnostics,
        "structural_visibility_quality",
        numeric_diagnostic(diagnostics, "contract_quality"),
    )
    domain_evidence = numeric_diagnostic(diagnostics, "domain_specific_evidence_score")
    actual_conversion = numeric_diagnostic(diagnostics, "actual_profit_conversion_score")
    fcf_quality = numeric_diagnostic(diagnostics, "fcf_quality_score")
    bridge_count = numeric_diagnostic(diagnostics, "research_axis_bridge_present_count_capped")
    capital_return_bridge = numeric_diagnostic(diagnostics, "research_axis_bridge_capital_return")
    bio_commercialization_bridge = numeric_diagnostic(diagnostics, "research_axis_bridge_bio_commercialization")
    margin_bridge = numeric_diagnostic(diagnostics, "research_axis_bridge_margin")
    weighted_capital = weighted.components.get("capital_allocation", payload.components.get("capital_allocation", 0.0))
    capital_component_quality = min(weighted_capital / max(weighted.match.weights.get("capital_allocation", 5.0), 1.0) * 100.0, 100.0) if weighted.match else 0.0

    unlock_scores = [numeric_diagnostic(diagnostics, "green_unlock_evidence_score")]
    if actual_conversion >= 55.0 and (domain_evidence >= 35.0 or structural_visibility >= 45.0 or bridge_count >= 3.0):
        unlock_scores.append(min(actual_conversion, max(domain_evidence, structural_visibility, bridge_count / 6.0 * 100.0)))
    if fcf_quality >= 55.0 and revision_score >= 55.0 and (
        structural_visibility >= 45.0 or domain_evidence >= 35.0 or margin_bridge > 0.0
    ):
        unlock_scores.append(min(fcf_quality, revision_score))
    if capital_component_quality >= 60.0 and revision_score >= 55.0 and (
        capital_return_bridge > 0.0 or fcf_quality >= 45.0
    ):
        unlock_scores.append(min(capital_component_quality, max(capital_return_bridge, fcf_quality)))
    if bio_commercialization_bridge > 0.0 and actual_conversion >= 45.0 and domain_evidence >= 45.0:
        unlock_scores.append(min(bio_commercialization_bridge, actual_conversion, domain_evidence))
    return max(unlock_scores)


def _require_runtime_archetype_classification(payload: ScoringPayload, runtime_profile) -> None:
    if not runtime_profile.enabled or not runtime_profile.archetype_weights or not runtime_profile.large_sector_weights:
        raise ArchetypeClassificationError("runtime archetype weight profile is unavailable")
    if not payload.large_sector_id:
        raise ArchetypeClassificationError("large_sector_id is required before scoring with rolling archetype weights")
    if not payload.canonical_archetype_id:
        raise ArchetypeClassificationError(
            "canonical_archetype_id is required before scoring with rolling archetype weights"
        )
    if payload.large_sector_id not in runtime_profile.large_sector_weights:
        raise ArchetypeClassificationError(f"unknown large_sector_id for rolling scoring: {payload.large_sector_id}")
    if payload.canonical_archetype_id not in runtime_profile.archetype_weights:
        raise ArchetypeClassificationError(
            f"unknown canonical_archetype_id for rolling scoring: {payload.canonical_archetype_id}"
        )
    expected_large_sector = large_sector_for_archetype(payload.canonical_archetype_id)
    if expected_large_sector and payload.large_sector_id != expected_large_sector:
        raise ArchetypeClassificationError(
            "large_sector_id does not match canonical_archetype_id: "
            f"{payload.large_sector_id} != {expected_large_sector}"
        )


def _scoring_version(base_version: str, profile_id: str, weighted: WeightedComponents) -> str:
    if weighted.match is None:
        return f"{base_version}:{profile_id}"
    return f"{base_version}:{profile_id}:archetype_weight:{weighted.match.profile_key}"


def _has_stage3_cross_evidence_buffer(payload: ScoringPayload, diagnostics: Mapping[str, float], profile) -> bool:
    """Allow a small calibrated buffer only for non-price, Green-like evidence stacks."""

    if profile.adjustment("stage3_cross_evidence_green_buffer") <= 0:
        return False
    if numeric_diagnostic(diagnostics, "price_only_blowoff_score") >= 70.0:
        return False
    if numeric_diagnostic(diagnostics, "one_off_shortage_risk") >= 70.0:
        return False
    if numeric_diagnostic(diagnostics, "theme_overheat_score") >= 70.0:
        return False
    if numeric_diagnostic(diagnostics, "snippet_only_green_block") > 0:
        return False
    if numeric_diagnostic(diagnostics, "revision_score") < max(70.0, profile.threshold("stage3_green_revision_min", 55.0)):
        return False
    if len(payload.evidence_ids) < 2 and numeric_diagnostic(diagnostics, "cross_evidence_family_count") < 4.0:
        return False
    return (
        payload.components["eps_fcf_explosion"] >= profile.threshold("stage3_green_eps_fcf_min", 17.0)
        and payload.components["earnings_visibility"] >= profile.threshold("stage3_green_visibility_min", 15.0)
        and payload.components["bottleneck_pricing"] >= profile.threshold("stage3_green_bottleneck_min", 15.0)
        and payload.components["market_mispricing"] >= profile.threshold("stage3_green_mispricing_min", 10.0)
        and payload.components["valuation_rerating"] >= profile.threshold("stage3_green_valuation_min", 10.0)
        and payload.components["information_confidence"] >= profile.threshold("stage2_information_confidence_min", 3.0)
    )


def _scope_labels(payload: ScoringPayload) -> tuple[str, ...]:
    labels: list[str] = []
    if payload.large_sector_id:
        labels.append(f"large_sector:{payload.large_sector_id}")
    if payload.canonical_archetype_id:
        labels.append(f"canonical_archetype:{payload.canonical_archetype_id}")
    return tuple(labels)


def _has_non_price_stage2_bridge(diagnostics: Mapping[str, float]) -> bool:
    if numeric_diagnostic(diagnostics, "calibration_stage2_actionable_evidence") > 0:
        return True
    if numeric_diagnostic(diagnostics, "credible_order_or_policy_evidence") > 0:
        return True
    non_price_families = (
        "evidence_family_financial_actual",
        "evidence_family_disclosure",
        "evidence_family_research_report",
        "evidence_family_consensus",
        "evidence_family_consensus_revision",
        "evidence_family_news",
    )
    non_price_count = sum(1 for key in non_price_families if numeric_diagnostic(diagnostics, key) > 0)
    return non_price_count >= 2 or numeric_diagnostic(diagnostics, "cross_evidence_family_count") >= 3.0


def _v12_stage2_bonus_applies(payload: ScoringPayload, diagnostics: Mapping[str, float], profile, scope_labels: tuple[str, ...]) -> bool:
    if not profile.guardrail_enabled("rolling_calibration_enabled"):
        return False
    if not profile.scope_enabled("v12_stage2_bonus_scopes", scope_labels):
        return False
    if numeric_diagnostic(diagnostics, "price_only_blowoff_score", invalid_default=70.0) >= 70.0:
        return False
    if numeric_diagnostic(diagnostics, "one_off_shortage_risk", invalid_default=80.0) >= 80.0:
        return False
    if not _has_non_price_stage2_bridge(diagnostics):
        return False
    return payload.components["eps_fcf_explosion"] >= profile.threshold("stage2_eps_fcf_min", 10.0)


def _annotate_v12_scope_matches(diagnostics: dict[str, float], profile, scope_labels: tuple[str, ...]) -> None:
    if not profile.guardrail_enabled("rolling_calibration_enabled"):
        return
    scope_keys = {
        "v12_stage2_bonus_scopes": "v12_scope_stage2_bonus_match",
        "v12_stage2_required_bridge_scopes": "v12_scope_stage2_required_bridge_match",
        "v12_local_4b_watch_guard_scopes": "v12_scope_local_4b_watch_guard_match",
        "v12_full_4b_overlay_scopes": "v12_scope_full_4b_overlay_match",
        "v12_earlier_4c_watch_scopes": "v12_scope_earlier_4c_watch_match",
        "v12_hard_4c_confirmation_scopes": "v12_scope_hard_4c_confirmation_match",
    }
    for profile_key, diagnostic_key in scope_keys.items():
        if profile.scope_enabled(profile_key, scope_labels):
            diagnostics[diagnostic_key] = 1.0
