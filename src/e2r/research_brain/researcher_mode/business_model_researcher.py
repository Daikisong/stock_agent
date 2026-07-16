"""Independent business-mechanism pass that precedes component research."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_researcher import (
    StructuredResearchProvider,
    _invalidate_provider_response_cache,
)
from .schemas import (
    BusinessModelMemo,
    EvidenceFact,
    assert_blind_research_output,
    scrub_blind_research_payload,
)
from .prompt_projection import (
    citable_fact_id_by_row_index,
    project_current_decision_citable_facts,
    project_research_source_claim_profile,
    project_research_source_document_profile,
    resolve_citable_fact_row_indices,
)


@dataclass(frozen=True)
class BusinessModelResearchResult:
    status: str
    memo: BusinessModelMemo | None
    pending_reasons: tuple[str, ...]
    provider_name: str

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown business model research status")
        if self.status == "COMPLETE" and (
            self.memo is None or not self.memo.research_complete
        ):
            raise ValueError("complete business model result requires a complete memo")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending business model result requires a reason")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "memo": self.memo.to_dict() if self.memo else None,
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
        }


class BusinessMechanismResearcher:
    researcher_role = "BusinessMechanismResearcher"

    def __init__(self, *, provider: StructuredResearchProvider) -> None:
        self.provider = provider

    def research(
        self,
        *,
        target_id: str,
        archetype_id: str,
        as_of_date: str,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        source_claims: Sequence[Mapping[str, Any]],
        source_documents: Sequence[Mapping[str, Any]],
        source_coverage: Sequence[str | Mapping[str, Any]],
    ) -> BusinessModelResearchResult:
        facts = tuple(_coerce_fact(row) for row in evidence_facts)
        _assert_rows_as_of(source_claims, as_of_date)
        _assert_rows_as_of(source_documents, as_of_date)
        if any(row.target_id != target_id for row in facts):
            raise ValueError("business model researcher received cross-target facts")
        if any(row.as_of_date != as_of_date for row in facts):
            raise ValueError("business model EvidenceFact date mismatch")
        fact_by_id = {row.fact_id: row for row in facts}
        if len(fact_by_id) != len(facts):
            raise ValueError("EvidenceFact ids must be unique")
        fact_projection = project_current_decision_citable_facts(facts)
        fact_id_by_row_index = citable_fact_id_by_row_index(fact_projection)
        payload = scrub_blind_research_payload(
            {
                "researcher_role": self.researcher_role,
                "target_id": target_id,
                "archetype_id": archetype_id,
                "as_of_date": as_of_date,
                "current_evidence_fact_graph": fact_projection["facts"],
                "current_evidence_fact_projection": {
                    key: value
                    for key, value in fact_projection.items()
                    if key not in {"facts", "fact_id_by_row_index"}
                },
                "source_claims": project_research_source_claim_profile(
                    source_claims
                ),
                "source_documents": project_research_source_document_profile(
                    source_documents
                ),
                "source_coverage": list(source_coverage),
            }
        )
        attempt_payload = payload
        validation_retry_used = False
        while True:
            try:
                response = self.provider.complete(
                    pass_name="BUSINESS_MODEL_RESEARCH",
                    payload=attempt_payload,
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
                cited_facts = resolve_citable_fact_row_indices(
                    response["fact_row_indices"],
                    fact_id_by_row_index=fact_id_by_row_index,
                    label="fact_row_indices",
                )
                cited_sources = tuple(
                    sorted(
                        {
                            source_id
                            for fact_id in cited_facts
                            for source_id in fact_by_id[fact_id].source_ids
                        }
                    )
                )
                memo = BusinessModelMemo(
                    memo_id=stable_intelligence_id(
                        "BMMEMO",
                        {
                            "target_id": target_id,
                            "archetype_id": archetype_id,
                            "as_of_date": as_of_date,
                            "response": scrub_blind_research_payload(response),
                            "resolved_fact_ids": cited_facts,
                            "resolved_source_ids": cited_sources,
                        },
                    ),
                    target_id=target_id,
                    archetype_id=archetype_id,
                    as_of_date=as_of_date,
                    business_model_summary=str(
                        response["business_model_summary"]
                    ),
                    revenue_engines=_unique_strings(
                        response["revenue_engines"], "revenue_engines"
                    ),
                    cost_and_cash_drivers=_unique_strings(
                        response["cost_and_cash_drivers"],
                        "cost_and_cash_drivers",
                    ),
                    capacity_and_supply_constraints=_unique_strings(
                        response["capacity_and_supply_constraints"],
                        "capacity_and_supply_constraints",
                    ),
                    customer_and_channel_dependencies=_unique_strings(
                        response["customer_and_channel_dependencies"],
                        "customer_and_channel_dependencies",
                    ),
                    fact_ids=cited_facts,
                    source_ids=cited_sources,
                    uncertainties=_unique_strings(
                        response["uncertainties"], "uncertainties"
                    ),
                    confidence=float(response["confidence"]),
                    research_complete=bool(response["research_complete"]),
                )
            except (KeyError, TypeError, ValueError) as exc:
                _invalidate_provider_response_cache(self.provider, exc)
                if validation_retry_used:
                    return self._pending("INVALID_PROVIDER_OUTPUT", exc)
                validation_retry_used = True
                attempt_payload = scrub_blind_research_payload(
                    {
                        **payload,
                        "business_model_validation_retry_context": {
                            "validation_error": (
                                " ".join(str(exc).split())[-500:]
                                or exc.__class__.__name__
                            ),
                            "rejected_response": response,
                            "instruction": (
                                "Rewrite the complete business-model memo from "
                                "the supplied current fact graph. If "
                                "research_complete is true, select at least one "
                                "source-backed current fact_row_index that directly "
                                "supports the stated revenue, cost, cash, capacity, "
                                "or customer mechanism. Never invent or repair a "
                                "citation. If no qualifying fact exists, set "
                                "research_complete=false and explain the uncertainty."
                            ),
                        },
                    }
                )
                continue
            break
        if not memo.research_complete:
            return BusinessModelResearchResult(
                status="PENDING",
                memo=memo,
                pending_reasons=("BUSINESS_MODEL_RESEARCH_INCOMPLETE",),
                provider_name=self._provider_name,
            )
        return BusinessModelResearchResult(
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

    def _pending(self, code: str, error: Exception) -> BusinessModelResearchResult:
        detail = " ".join(str(error).split())[-500:] or error.__class__.__name__
        return BusinessModelResearchResult(
            status="PENDING",
            memo=None,
            pending_reasons=(f"{code}:{detail}",),
            provider_name=self._provider_name,
        )


def _coerce_fact(row: EvidenceFact | Mapping[str, Any]) -> EvidenceFact:
    if isinstance(row, EvidenceFact):
        return row
    payload = {
        key: row[key]
        for key in EvidenceFact.__dataclass_fields__
        if key in row
    }
    for key in (
        "source_ids",
        "claim_ids",
        "quote_ids",
        "corroborating_independence_groups",
        "question_family_tags",
        "primitive_tags",
        "allowed_component_ids",
        "structured_evidence_roles",
    ):
        if key in payload:
            payload[key] = tuple(payload[key] or ())
    return EvidenceFact(**payload)


def _unique_strings(value: Any, label: str) -> tuple[str, ...]:
    if isinstance(value, str) or not isinstance(value, Sequence):
        raise TypeError(f"{label} must be an array")
    result = tuple(str(item).strip() for item in value)
    if any(not item for item in result) or len(result) != len(set(result)):
        raise ValueError(f"{label} must contain unique nonempty strings")
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


__all__ = ["BusinessMechanismResearcher", "BusinessModelResearchResult"]
