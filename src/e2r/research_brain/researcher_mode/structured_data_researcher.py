"""Source-backed structured financial/consensus/valuation record boundary."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class StructuredMetricRecord:
    record_id: str
    target_id: str
    as_of_date: str
    metric_id: str
    value: float | int | str
    unit: str
    period: str
    evidence_roles: tuple[str, ...]
    source_ids: tuple[str, ...]
    source_route: str
    observed_at: str
    record_kind: str
    confidence: float
    schema_version: str = "e2r_structured_metric_record_v1"

    def __post_init__(self) -> None:
        for value, label in (
            (self.record_id, "record_id"),
            (self.target_id, "target_id"),
            (self.metric_id, "metric_id"),
            (self.unit, "unit"),
            (self.period, "period"),
            (self.source_route, "source_route"),
            (self.record_kind, "record_kind"),
        ):
            if not str(value).strip():
                raise ValueError(f"{label} is required")
        cutoff = date.fromisoformat(self.as_of_date)
        observed = date.fromisoformat(self.observed_at[:10])
        if observed > cutoff:
            raise ValueError("structured metric leaks future observations")
        if not self.source_ids:
            raise ValueError("structured metric requires source lineage")
        if len(self.source_ids) != len(set(self.source_ids)):
            raise ValueError("structured metric source ids must be unique")
        if not self.evidence_roles:
            raise ValueError("structured metric requires evidence roles")
        if not 0 <= float(self.confidence) <= 1:
            raise ValueError("structured metric confidence is invalid")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StructuredResearchResult:
    status: str
    records: tuple[StructuredMetricRecord, ...]
    covered_roles_by_component: Mapping[str, tuple[str, ...]]
    missing_roles_by_component: Mapping[str, tuple[str, ...]]
    fallback_routes_required: tuple[str, ...]
    score_authority: bool = False

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "SOURCE_PENDING"}:
            raise ValueError("unknown structured research status")
        if self.status == "COMPLETE" and any(self.missing_roles_by_component.values()):
            raise ValueError("complete structured research cannot have missing roles")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "records": [row.to_dict() for row in self.records],
            "covered_roles_by_component": {
                key: list(value)
                for key, value in self.covered_roles_by_component.items()
            },
            "missing_roles_by_component": {
                key: list(value)
                for key, value in self.missing_roles_by_component.items()
            },
            "fallback_routes_required": list(self.fallback_routes_required),
            "score_authority": self.score_authority,
        }


class StructuredDataResearcher:
    """Validates records and reports gaps; a connector gap never means 0 points."""

    def assess(
        self,
        *,
        target_id: str,
        as_of_date: str,
        records: Sequence[StructuredMetricRecord | Mapping[str, Any]],
        required_roles_by_component: Mapping[str, Sequence[str]],
        fallback_routes: Sequence[str] = (
            "COMPANYGUIDE",
            "PUBLIC_BROKER_REPORT",
            "ISSUER_GUIDANCE",
            "DART_ACTUALS_DETERMINISTIC_SCENARIO",
            "KRX_PRICE_MARKET_CAP",
        ),
    ) -> StructuredResearchResult:
        compiled = tuple(_coerce_record(row) for row in records)
        ids = [row.record_id for row in compiled]
        if len(ids) != len(set(ids)):
            raise ValueError("structured record ids must be unique")
        if any(row.target_id != target_id for row in compiled):
            raise ValueError("structured researcher received cross-target data")
        if any(row.as_of_date != as_of_date for row in compiled):
            raise ValueError("structured record as_of_date mismatch")
        covered_roles = {
            role for row in compiled for role in row.evidence_roles
        }
        covered_by_component = {}
        missing_by_component = {}
        for component_id, required in required_roles_by_component.items():
            required_set = set(required)
            covered_by_component[component_id] = tuple(
                sorted(required_set & covered_roles)
            )
            missing_by_component[component_id] = tuple(
                sorted(required_set - covered_roles)
            )
        any_missing = any(missing_by_component.values())
        return StructuredResearchResult(
            status="SOURCE_PENDING" if any_missing else "COMPLETE",
            records=compiled,
            covered_roles_by_component=covered_by_component,
            missing_roles_by_component=missing_by_component,
            fallback_routes_required=(
                tuple(dict.fromkeys(fallback_routes)) if any_missing else ()
            ),
        )


def _coerce_record(
    row: StructuredMetricRecord | Mapping[str, Any],
) -> StructuredMetricRecord:
    if isinstance(row, StructuredMetricRecord):
        return row
    payload = dict(row)
    payload["evidence_roles"] = tuple(payload.get("evidence_roles") or ())
    payload["source_ids"] = tuple(payload.get("source_ids") or ())
    return StructuredMetricRecord(**payload)


__all__ = [
    "StructuredDataResearcher",
    "StructuredMetricRecord",
    "StructuredResearchResult",
]
