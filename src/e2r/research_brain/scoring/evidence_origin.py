from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping, Sequence


class EvidenceOrigin(str, Enum):
    ORGANIC_LIVE = "ORGANIC_LIVE"
    CONTROLLED_CLAIM_PROBE = "CONTROLLED_CLAIM_PROBE"
    TEST_FIXTURE = "TEST_FIXTURE"
    SNAPSHOT = "SNAPSHOT"
    HISTORICAL_REPLAY = "HISTORICAL_REPLAY"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class ScoringEvidencePartition:
    organic_rows: tuple[Mapping[str, Any], ...]
    excluded_rows: tuple[Mapping[str, Any], ...]
    origin_counts: Mapping[str, int]


def partition_scoring_evidence(
    rows: Sequence[Mapping[str, Any]],
    *,
    controlled_probe_claim_ids: Sequence[str] = (),
) -> ScoringEvidencePartition:
    controlled = set(str(value) for value in controlled_probe_claim_ids)
    organic: list[Mapping[str, Any]] = []
    excluded: list[Mapping[str, Any]] = []
    counts: dict[str, int] = {}
    for row in rows:
        claim_id = str(row.get("claim_id") or "")
        origin = _origin(row, controlled=controlled)
        counts[origin] = counts.get(origin, 0) + 1
        annotated = {**dict(row), "evidence_origin": origin}
        if origin == EvidenceOrigin.ORGANIC_LIVE.value:
            organic.append(annotated)
        else:
            excluded.append(annotated)
    return ScoringEvidencePartition(tuple(organic), tuple(excluded), dict(sorted(counts.items())))


def _origin(row: Mapping[str, Any], *, controlled: set[str]) -> str:
    claim_id = str(row.get("claim_id") or "")
    explicit = str(row.get("evidence_origin") or "")
    if claim_id in controlled or explicit == EvidenceOrigin.CONTROLLED_CLAIM_PROBE.value:
        return EvidenceOrigin.CONTROLLED_CLAIM_PROBE.value
    if row.get("test_only") is True or explicit == EvidenceOrigin.TEST_FIXTURE.value:
        return EvidenceOrigin.TEST_FIXTURE.value
    if row.get("historical_replay") is True or explicit == EvidenceOrigin.HISTORICAL_REPLAY.value:
        return EvidenceOrigin.HISTORICAL_REPLAY.value
    url = str(row.get("source_url") or row.get("canonical_url") or "")
    if url.startswith("snapshot://") or explicit == EvidenceOrigin.SNAPSHOT.value:
        return EvidenceOrigin.SNAPSHOT.value
    if (
        explicit == EvidenceOrigin.ORGANIC_LIVE.value
        and row.get("source_proxy_only") is False
        and row.get("fetched") is True
    ):
        return EvidenceOrigin.ORGANIC_LIVE.value
    return EvidenceOrigin.UNKNOWN.value


def audit_probe_separation(
    *,
    partition: ScoringEvidencePartition,
    scoring_decisions: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    organic_claim_ids = {str(row.get("claim_id") or "") for row in partition.organic_rows}
    decision_claim_ids = {
        str(value)
        for row in scoring_decisions
        for value in row.get("accepted_claim_ids") or ()
    }
    excluded_claim_ids = {str(row.get("claim_id") or "") for row in partition.excluded_rows}
    critical = {
        "probe_claim_counted_organic_count": sum(
            row.get("evidence_origin") == EvidenceOrigin.CONTROLLED_CLAIM_PROBE.value
            for row in partition.organic_rows
        ),
        "probe_decision_merged_into_canonical_score_count": len(
            decision_claim_ids & excluded_claim_ids
        ),
        "no_score_probe_unlocks_readiness_count": sum(
            row.get("score_type") == "NO_SCORE"
            and bool(set(str(v) for v in row.get("accepted_claim_ids") or ()) & excluded_claim_ids)
            and row.get("scoring_readiness_eligible") is True
            for row in scoring_decisions
        ),
    }
    return {
        "schema_version": "e2r_acceptance_probe_separation_audit_v1",
        "status": "CONTROLLED_CLAIM_PROBE_PASS" if sum(critical.values()) == 0 else "CONTROLLED_CLAIM_PROBE_FAIL",
        "organic_claim_count": len(organic_claim_ids),
        "excluded_claim_count": len(excluded_claim_ids),
        "origin_counts": dict(partition.origin_counts),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


__all__ = ["EvidenceOrigin", "ScoringEvidencePartition", "audit_probe_separation", "partition_scoring_evidence"]
