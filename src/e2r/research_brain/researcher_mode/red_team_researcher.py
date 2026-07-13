"""Independent counter-thesis researcher for the seven component memos."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_researcher import StructuredResearchProvider
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    BusinessModelMemo,
    ComponentAnchor,
    ComponentResearchMemo,
    EvidenceFact,
    RedTeamMemo,
    assert_blind_research_output,
    scrub_blind_research_payload,
)
from .prompt_projection import (
    citable_fact_id_by_row_index,
    project_citable_evidence_facts,
    project_source_claim_profile,
    project_source_document_profile,
    resolve_citable_fact_row_indices,
)


@dataclass(frozen=True)
class RedTeamResearchResult:
    status: str
    memo: RedTeamMemo | None
    pending_reasons: tuple[str, ...]
    provider_name: str

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown red-team result status")
        if self.status == "COMPLETE" and (
            self.memo is None or not self.memo.review_complete
        ):
            raise ValueError("complete red-team result requires a complete memo")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending red-team result requires reasons")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "memo": self.memo.to_dict() if self.memo else None,
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
        }


class RedTeamResearcher:
    researcher_role = "RedTeamResearcher"

    def __init__(self, *, provider: StructuredResearchProvider) -> None:
        self.provider = provider

    def research(
        self,
        *,
        business_model: BusinessModelMemo,
        component_memos: Sequence[ComponentResearchMemo],
        evidence_facts: Sequence[EvidenceFact],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
        source_coverage: Sequence[str | Mapping[str, Any]],
        source_claims: Sequence[Mapping[str, Any]] = (),
        source_documents: Sequence[Mapping[str, Any]] = (),
    ) -> RedTeamResearchResult:
        memo_by_component = {row.component_id: row for row in component_memos}
        _assert_rows_as_of(source_claims, business_model.as_of_date)
        _assert_rows_as_of(source_documents, business_model.as_of_date)
        if len(memo_by_component) != len(component_memos):
            raise ValueError("component memos must be unique")
        if any(
            row.target_id != business_model.target_id
            or row.archetype_id != business_model.archetype_id
            for row in component_memos
        ):
            raise ValueError("red-team received cross-target component memos")
        fact_by_id = {row.fact_id: row for row in evidence_facts}
        if len(fact_by_id) != len(evidence_facts):
            raise ValueError("EvidenceFact ids must be unique")
        anchor_rows = [
            _blind_anchor(row)
            for row in historical_anchors
            if _field(row, "archetype_id") == business_model.archetype_id
        ]
        anchor_ids = {str(row["anchor_id"]) for row in anchor_rows}
        coverage_labels = _coverage_labels(source_coverage)
        fact_projection = project_citable_evidence_facts(evidence_facts)
        fact_id_by_row_index = citable_fact_id_by_row_index(fact_projection)
        payload = scrub_blind_research_payload(
            {
                "researcher_role": self.researcher_role,
                "target_id": business_model.target_id,
                "as_of_date": business_model.as_of_date,
                "archetype_id": business_model.archetype_id,
                "target_business_model": business_model.to_dict(),
                "component_research_memos": [row.to_dict() for row in component_memos],
                "current_evidence_fact_graph": fact_projection["facts"],
                "current_evidence_fact_projection": {
                    key: value
                    for key, value in fact_projection.items()
                    if key != "facts"
                },
                "historical_component_anchors": anchor_rows,
                "source_coverage": list(source_coverage),
                "source_claims": project_source_claim_profile(source_claims),
                "source_documents": project_source_document_profile(
                    source_documents
                ),
            }
        )
        try:
            response = self.provider.complete(
                pass_name="RED_TEAM_RESEARCH", payload=payload
            )
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
        ) as exc:
            return self._pending("PROVIDER_ERROR", exc)
        try:
            assert_blind_research_output(response)
            reviewed = _strings(response, "reviewed_component_ids")
            challenged = resolve_citable_fact_row_indices(
                response["challenged_fact_row_indices"],
                fact_id_by_row_index=fact_id_by_row_index,
                label="challenged_fact_row_indices",
            )
            counters = tuple(
                fact_id
                for fact_id in challenged
                if fact_by_id[fact_id].direction == "COUNTER"
                and fact_by_id[fact_id].current_lifecycle
                not in {"RESOLVED", "SUPERSEDED"}
            )
            cited_coverage = _strings(response, "source_coverage")
            if set(reviewed) - set(memo_by_component):
                raise ValueError("red team cited an unresearched component")
            if set((*challenged, *counters)) - set(fact_by_id):
                raise ValueError("red team cited an unknown EvidenceFact")
            if set(cited_coverage) - coverage_labels:
                raise ValueError("red team cited unknown source coverage")
            # The ids are intentionally included in the identity even though
            # anchor comparisons remain prose in this Phase 84 memo.
            memo = RedTeamMemo(
                memo_id=stable_intelligence_id(
                    "RTMEMO",
                    {
                        "target_id": business_model.target_id,
                        "memo_ids": sorted(row.memo_id for row in component_memos),
                        "anchor_ids": sorted(anchor_ids),
                        "response": scrub_blind_research_payload(response),
                        "resolved_challenged_fact_ids": challenged,
                        "resolved_counter_fact_ids": counters,
                    },
                ),
                target_id=business_model.target_id,
                archetype_id=business_model.archetype_id,
                reviewed_component_ids=reviewed,
                challenged_fact_ids=challenged,
                counter_fact_ids=counters,
                resolved_challenges=_strings(response, "resolved_challenges"),
                unresolved_challenges=_strings(response, "unresolved_challenges"),
                recommended_research_directions=_strings(
                    response, "recommended_research_directions"
                ),
                source_coverage=cited_coverage,
                confidence=float(response["confidence"]),
                review_complete=bool(response["review_complete"]),
            )
        except (KeyError, TypeError, ValueError) as exc:
            return self._pending("INVALID_PROVIDER_OUTPUT", exc)
        reasons = []
        if set(memo.reviewed_component_ids) != set(CANONICAL_COMPONENT_ORDER):
            reasons.append("SEVEN_COMPONENT_REVIEW_INCOMPLETE")
        if not memo.review_complete:
            reasons.append("RED_TEAM_DECLARED_INCOMPLETE")
        if reasons:
            return RedTeamResearchResult(
                status="PENDING",
                memo=memo,
                pending_reasons=tuple(reasons),
                provider_name=self._provider_name,
            )
        return RedTeamResearchResult(
            status="COMPLETE",
            memo=memo,
            pending_reasons=(),
            provider_name=self._provider_name,
        )

    @property
    def _provider_name(self) -> str:
        return str(
            getattr(self.provider, "provider_name", self.provider.__class__.__name__)
        )

    def _pending(self, code: str, error: Exception) -> RedTeamResearchResult:
        detail = " ".join(str(error).split())[-500:] or error.__class__.__name__
        return RedTeamResearchResult(
            status="PENDING",
            memo=None,
            pending_reasons=(f"{code}:{detail}",),
            provider_name=self._provider_name,
        )


def _blind_anchor(row: ComponentAnchor | Mapping[str, Any]) -> Mapping[str, Any]:
    value = row.to_dict() if isinstance(row, ComponentAnchor) else dict(row)
    if value.get("company_name_conditioned") or value.get("target_symbol_conditioned"):
        raise ValueError("target-conditioned historical anchors are forbidden")
    allowed = {
        "anchor_id",
        "archetype_id",
        "component_id",
        "economic_fact_patterns",
        "role",
        "score_band",
        "points_lower",
        "points_mid",
        "points_upper",
        "max_points",
        "confidence",
        "usable_as_exact_anchor",
        "usable_as_ordinal_anchor",
    }
    return {key: value[key] for key in allowed if key in value}


def _field(row: Any, key: str) -> Any:
    return row.get(key) if isinstance(row, Mapping) else getattr(row, key)


def _strings(response: Mapping[str, Any], key: str) -> tuple[str, ...]:
    value = response[key]
    if isinstance(value, str) or not isinstance(value, Sequence):
        raise TypeError(f"{key} must be an array")
    result = tuple(str(item).strip() for item in value)
    if any(not item for item in result) or len(result) != len(set(result)):
        raise ValueError(f"{key} must contain unique nonempty strings")
    return result


def _coverage_labels(rows: Sequence[str | Mapping[str, Any]]) -> set[str]:
    result = set()
    for row in rows:
        if isinstance(row, str):
            label = row
        else:
            label = str(
                row.get("coverage_id")
                or row.get("source_family")
                or row.get("route_id")
                or ""
            )
        if label.strip():
            result.add(label.strip())
    return result


def _assert_rows_as_of(rows: Sequence[Mapping[str, Any]], as_of_date: str) -> None:
    cutoff = date.fromisoformat(as_of_date)
    for row in rows:
        raw = next(
            (
                str(row.get(key)).strip()
                for key in (
                    "published_at",
                    "publication_date",
                    "filed_at",
                    "observed_at",
                )
                if row.get(key)
            ),
            "",
        )
        if not raw:
            continue
        try:
            observed = date.fromisoformat(raw[:10])
        except ValueError as exc:
            raise ValueError(f"invalid source date: {raw}") from exc
        if observed > cutoff:
            raise ValueError(
                f"future source exposure is forbidden: {observed.isoformat()} > {as_of_date}"
            )


__all__ = ["RedTeamResearchResult", "RedTeamResearcher"]
