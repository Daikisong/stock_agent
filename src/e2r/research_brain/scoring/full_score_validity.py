"""Semantic consistency gate for a finalized 100-point E2R score."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash

from .component_assessment import (
    ComponentAssessment,
    TERMINAL_FULL_SCORE_STATUSES,
)


SCHEMA_VERSION = "e2r_full_score_validity_v2"
PENDING_COMPONENT_STATUSES = {
    "UNKNOWN_UNINVESTIGATED",
    "SOURCE_PENDING",
    "PROVIDER_PENDING",
    "BUDGET_PENDING",
    "HISTORICAL_ONLY",
}
PENDING_QUESTION_STATUSES = {
    "SOURCE_PENDING",
    "PROVIDER_PENDING",
    "BUDGET_PENDING",
    "SCORING_PIPELINE_ERROR",
}
ADEQUATE_ABSENCE_STATUS = "ADEQUATE_ABSENCE"


@dataclass(frozen=True)
class FullScoreValidityEvidenceV2:
    """Leaf-derived semantic checks consumed by the deterministic scorer."""

    schema_totality_status: str
    scoring_schema_critical_count: int
    silent_zero_default_count: int
    positive_impact_zeroed_by_missing_cap_count: int
    counter_impact_zeroed_by_missing_cap_count: int
    mechanism_scope_failure_count: int
    question_component_reconciliation_critical_count: int
    unresolved_contradiction_count: int
    pending_state_count: int
    absence_without_adequacy_count: int
    gold_critical_fact_miss_count: int
    cross_business_question_closure_count: int
    same_fact_duplicate_credit_count: int
    same_document_duplicate_credit_count: int
    source_audit_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        count_fields = (
            "scoring_schema_critical_count",
            "silent_zero_default_count",
            "positive_impact_zeroed_by_missing_cap_count",
            "counter_impact_zeroed_by_missing_cap_count",
            "mechanism_scope_failure_count",
            "question_component_reconciliation_critical_count",
            "unresolved_contradiction_count",
            "pending_state_count",
            "absence_without_adequacy_count",
            "gold_critical_fact_miss_count",
            "cross_business_question_closure_count",
            "same_fact_duplicate_credit_count",
            "same_document_duplicate_credit_count",
        )
        for field_name in count_fields:
            if int(getattr(self, field_name)) < 0:
                raise ValueError(f"full score validity count is negative: {field_name}")
        object.__setattr__(
            self,
            "source_audit_ids",
            tuple(
                dict.fromkeys(
                    str(value)
                    for value in self.source_audit_ids
                    if str(value).strip()
                )
            ),
        )

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


@dataclass(frozen=True)
class FullScoreValidityResultV2:
    validity_id: str
    schema_version: str
    status: str
    full_score_valid: bool
    blocking_reasons: tuple[str, ...]
    critical_counts: Mapping[str, int]
    critical_count_sum: int
    source_audit_ids: tuple[str, ...]

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


def evaluate_full_score_validity_v2(
    *,
    assessments: Sequence[ComponentAssessment],
    evidence: FullScoreValidityEvidenceV2 | None,
) -> FullScoreValidityResultV2:
    terminal_gap_count = sum(
        row.status not in TERMINAL_FULL_SCORE_STATUSES for row in assessments
    )
    if evidence is None:
        critical = {
            "validity_evidence_missing_count": 1,
            "terminal_component_gap_count": terminal_gap_count,
            "scoring_schema_not_total_count": 1,
            "silent_zero_default_count": 0,
            "positive_impact_zeroed_by_missing_cap_count": 0,
            "counter_impact_zeroed_by_missing_cap_count": 0,
            "mechanism_scope_failure_count": 0,
            "question_component_reconciliation_failure_count": 0,
            "unresolved_contradiction_count": 0,
            "pending_state_count": terminal_gap_count,
            "absence_without_adequacy_count": 0,
            "gold_critical_fact_miss_count": 0,
            "cross_business_question_closure_count": 0,
            "same_fact_duplicate_credit_count": 0,
            "same_document_duplicate_credit_count": 0,
        }
        source_audit_ids: tuple[str, ...] = ()
    else:
        critical = {
            "validity_evidence_missing_count": 0,
            "terminal_component_gap_count": terminal_gap_count,
            "scoring_schema_not_total_count": int(
                evidence.schema_totality_status
                != "SCORING_SCHEMA_TOTALITY_PASS"
                or evidence.scoring_schema_critical_count > 0
            ),
            "silent_zero_default_count": evidence.silent_zero_default_count,
            "positive_impact_zeroed_by_missing_cap_count": (
                evidence.positive_impact_zeroed_by_missing_cap_count
            ),
            "counter_impact_zeroed_by_missing_cap_count": (
                evidence.counter_impact_zeroed_by_missing_cap_count
            ),
            "mechanism_scope_failure_count": (
                evidence.mechanism_scope_failure_count
            ),
            "question_component_reconciliation_failure_count": (
                evidence.question_component_reconciliation_critical_count
            ),
            "unresolved_contradiction_count": (
                evidence.unresolved_contradiction_count
            ),
            "pending_state_count": evidence.pending_state_count,
            "absence_without_adequacy_count": (
                evidence.absence_without_adequacy_count
            ),
            "gold_critical_fact_miss_count": (
                evidence.gold_critical_fact_miss_count
            ),
            "cross_business_question_closure_count": (
                evidence.cross_business_question_closure_count
            ),
            "same_fact_duplicate_credit_count": (
                evidence.same_fact_duplicate_credit_count
            ),
            "same_document_duplicate_credit_count": (
                evidence.same_document_duplicate_credit_count
            ),
        }
        source_audit_ids = evidence.source_audit_ids
    critical_sum = sum(critical.values())
    blocking_reasons = tuple(
        key for key, value in critical.items() if value > 0
    )
    payload = {
        "schema_version": SCHEMA_VERSION,
        "assessment_ids": [row.assessment_id for row in assessments],
        "critical_counts": critical,
        "source_audit_ids": source_audit_ids,
    }
    return FullScoreValidityResultV2(
        validity_id="FSVALID-" + stable_hash(payload)[:24],
        schema_version=SCHEMA_VERSION,
        status=(
            "FULL_SCORE_VALIDITY_V2_PASS"
            if critical_sum == 0
            else "FULL_SCORE_VALIDITY_V2_FAIL"
        ),
        full_score_valid=critical_sum == 0,
        blocking_reasons=blocking_reasons,
        critical_counts=critical,
        critical_count_sum=critical_sum,
        source_audit_ids=source_audit_ids,
    )


def compile_full_score_validity_evidence_v2(
    *,
    assessments: Sequence[ComponentAssessment],
    scoring_schema_audit: Mapping[str, Any],
    impact_validation_audit: Mapping[str, Any],
    validated_impacts: Sequence[Any],
    reconciliation_audit: Mapping[str, Any],
    reconciliations: Sequence[Any],
    search_adequacy: Sequence[Mapping[str, Any]],
    material_fact_comparisons: Sequence[Mapping[str, Any]] = (),
) -> FullScoreValidityEvidenceV2:
    """Compile gate evidence from leaves, never from a report-level PASS label."""

    schema_critical = _critical(scoring_schema_audit)
    impact_critical = _critical(impact_validation_audit)
    reconciliation_critical = _critical(reconciliation_audit)
    schema_counts = scoring_schema_audit.get("critical_counts") or {}
    impact_counts = impact_validation_audit.get("critical_counts") or {}

    scope_mismatches = sum(
        (_value(row, "scope_validation") or {}).get("scope_match") is not True
        for row in validated_impacts
    )
    mechanism_scope_failure_count = max(
        int(impact_counts.get("cross_mechanism_impact_count") or 0),
        scope_mismatches,
    )
    cross_business_closure_count = sum(
        (_value(row, "scope_validation") or {}).get("scope_match") is not True
        and float(_value(row, "validated_credit_fraction") or 0.0) > 0
        for row in validated_impacts
    )
    assessment_pending = sum(
        row.status in PENDING_COMPONENT_STATUSES for row in assessments
    )
    question_pending = sum(
        str(_value(row, "reconciled_closure_status") or "")
        in PENDING_QUESTION_STATUSES
        for row in reconciliations
    )
    unresolved = max(
        sum(
            row.status == "CONTRADICTED_OPEN"
            or row.contradiction_status == "CONTRADICTED_OPEN"
            for row in assessments
        ),
        sum(
            str(_value(link, "component_state") or "")
            == "CONTRADICTED_OPEN"
            for row in reconciliations
            for link in (_value(row, "component_links") or ())
        ),
    )
    absence_without_adequacy = _absence_without_adequacy_count(
        assessments=assessments,
        reconciliations=reconciliations,
        search_adequacy=search_adequacy,
    )
    adequacy_gold_misses = sum(
        int(row.get("gold_material_fact_miss_count") or 0)
        for row in search_adequacy
    )
    comparison_gold_misses = sum(
        str(row.get("materiality") or "") == "CRITICAL"
        and not _material_fact_qualified(row)
        for row in material_fact_comparisons
    )
    source_ids = tuple(
        dict.fromkeys(
            (
                str(scoring_schema_audit.get("policy_config_hash") or ""),
                *(
                    str(_value(row, "reconciliation_id") or "")
                    for row in reconciliations
                ),
                *(
                    str(row.get("adequacy_id") or "")
                    for row in search_adequacy
                ),
            )
        )
    )
    return FullScoreValidityEvidenceV2(
        schema_totality_status=str(scoring_schema_audit.get("status") or ""),
        scoring_schema_critical_count=schema_critical,
        silent_zero_default_count=int(
            schema_counts.get("silent_zero_default_count") or 0
        ),
        positive_impact_zeroed_by_missing_cap_count=int(
            impact_counts.get("positive_impact_zeroed_by_missing_cap_count")
            or 0
        ),
        counter_impact_zeroed_by_missing_cap_count=int(
            impact_counts.get("counter_impact_zeroed_by_missing_cap_count")
            or 0
        ),
        mechanism_scope_failure_count=mechanism_scope_failure_count,
        question_component_reconciliation_critical_count=(
            reconciliation_critical
        ),
        unresolved_contradiction_count=unresolved,
        pending_state_count=max(assessment_pending, question_pending),
        absence_without_adequacy_count=absence_without_adequacy,
        gold_critical_fact_miss_count=max(
            adequacy_gold_misses, comparison_gold_misses
        ),
        cross_business_question_closure_count=(
            cross_business_closure_count
        ),
        same_fact_duplicate_credit_count=int(
            impact_counts.get("same_fact_duplicate_credit_count") or 0
        ),
        same_document_duplicate_credit_count=int(
            impact_counts.get("same_document_duplicate_credit_count") or 0
        ),
        source_audit_ids=source_ids,
    )


def _absence_without_adequacy_count(
    *,
    assessments: Sequence[ComponentAssessment],
    reconciliations: Sequence[Any],
    search_adequacy: Sequence[Mapping[str, Any]],
) -> int:
    absent_components = {
        row.component_id
        for row in assessments
        if row.status == "VERIFIED_ABSENT_AFTER_SEARCH"
    }
    if not absent_components:
        return 0
    adequacy_by_question = {
        str(row.get("question_family_id") or ""): row
        for row in search_adequacy
    }
    related_absence_rows: dict[str, list[Any]] = {
        component_id: [] for component_id in absent_components
    }
    for reconciliation in reconciliations:
        if str(_value(reconciliation, "input_closure_status") or "") != (
            "EVALUATED_ABSENT"
        ):
            continue
        states = _value(reconciliation, "component_states") or {}
        for component_id in absent_components.intersection(states):
            related_absence_rows[component_id].append(reconciliation)

    count = 0
    for component_id, rows in related_absence_rows.items():
        if not rows:
            count += 1
            continue
        if any(
            not _adequate_absence_row(
                adequacy_by_question.get(
                    str(_value(row, "question_family_id") or "")
                )
            )
            for row in rows
        ):
            count += 1
    return count


def _adequate_absence_row(row: Mapping[str, Any] | None) -> bool:
    if not row:
        return False
    return (
        row.get("adequate_absence_allowed") is True
        and str(row.get("saturation_status") or "")
        == ADEQUATE_ABSENCE_STATUS
        and int(row.get("provider_failures") or 0) == 0
        and row.get("budget_exhausted") is not True
        and not row.get("missing_route_categories")
        and int(
            row.get("positive_proposal_zeroed_by_internal_validation_count")
            or 0
        )
        == 0
        and int(row.get("gold_material_fact_miss_count") or 0) == 0
    )


def _material_fact_qualified(row: Mapping[str, Any]) -> bool:
    return all(
        row.get(field) is True
        for field in (
            "semantic_match",
            "source_quality_match",
            "currentness_match",
            "mechanism_scope_match",
        )
    )


def _critical(audit: Mapping[str, Any]) -> int:
    return int(audit.get("critical_count_sum") or 0)


def _value(row: Any, key: str) -> Any:
    if isinstance(row, Mapping):
        return row.get(key)
    return getattr(row, key, None)


__all__ = [
    "FullScoreValidityEvidenceV2",
    "FullScoreValidityResultV2",
    "SCHEMA_VERSION",
    "compile_full_score_validity_evidence_v2",
    "evaluate_full_score_validity_v2",
]
