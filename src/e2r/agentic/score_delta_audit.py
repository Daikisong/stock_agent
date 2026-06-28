"""Audit score changes against claim deltas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .evidence_os import ScoreContributionV2


@dataclass(frozen=True)
class ScoreDeltaFinding:
    component_key: str
    criterion_id: str
    before_points: float
    after_points: float
    delta: float
    added_claim_ids: tuple[str, ...]
    removed_claim_ids: tuple[str, ...]
    added_source_evidence_ids: tuple[str, ...]
    removed_source_evidence_ids: tuple[str, ...]
    severity: str
    reason: str


def audit_unexplained_score_deltas(
    *,
    before: Sequence[ScoreContributionV2],
    after: Sequence[ScoreContributionV2],
    critical_delta: float = 5.0,
) -> tuple[ScoreDeltaFinding, ...]:
    """Find score deltas that have no corresponding claim delta."""

    before_by_key = _group_contributions(before)
    after_by_key = _group_contributions(after)
    findings: list[ScoreDeltaFinding] = []
    for key in sorted(set(before_by_key) | set(after_by_key)):
        before_points, before_claims, before_sources = before_by_key.get(key, (0.0, (), ()))
        after_points, after_claims, after_sources = after_by_key.get(key, (0.0, (), ()))
        delta = round(after_points - before_points, 10)
        if delta == 0:
            continue
        added = tuple(sorted(set(after_claims) - set(before_claims)))
        removed = tuple(sorted(set(before_claims) - set(after_claims)))
        added_sources = tuple(sorted(set(after_sources) - set(before_sources)))
        removed_sources = tuple(sorted(set(before_sources) - set(after_sources)))
        reason = "score_delta_without_claim_delta"
        if before_sources or after_sources:
            if added_sources or removed_sources:
                continue
            reason = "score_delta_without_source_evidence_delta"
        elif added or removed:
            continue
        severity = "critical" if abs(delta) >= critical_delta else "warning"
        findings.append(
            ScoreDeltaFinding(
                component_key=key[0],
                criterion_id=key[1],
                before_points=before_points,
                after_points=after_points,
                delta=delta,
                added_claim_ids=added,
                removed_claim_ids=removed,
                added_source_evidence_ids=added_sources,
                removed_source_evidence_ids=removed_sources,
                severity=severity,
                reason=reason,
            )
        )
    return tuple(findings)


def _group_contributions(
    contributions: Sequence[ScoreContributionV2],
) -> Mapping[tuple[str, str], tuple[float, tuple[str, ...], tuple[str, ...]]]:
    grouped: dict[tuple[str, str], tuple[float, tuple[str, ...], tuple[str, ...]]] = {}
    for contribution in contributions:
        key = (contribution.component_key, contribution.criterion_id)
        points, claim_ids, source_ids = grouped.get(key, (0.0, (), ()))
        all_claims = (
            *claim_ids,
            *contribution.support_claim_ids,
            *contribution.counter_claim_ids,
        )
        all_sources = (*source_ids, *contribution.source_family_ids)
        grouped[key] = (
            round(points + contribution.raw_points, 10),
            tuple(dict.fromkeys(claim for claim in all_claims if str(claim).strip())),
            tuple(dict.fromkeys(source_id for source_id in all_sources if str(source_id).strip())),
        )
    return grouped


__all__ = ["ScoreDeltaFinding", "audit_unexplained_score_deltas"]
