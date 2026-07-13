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

from .component_researcher import StructuredResearchProvider
from .schemas import (
    BusinessModelMemo,
    EvidenceFact,
    assert_blind_research_output,
    scrub_blind_research_payload,
)
from .prompt_projection import (
    project_citable_evidence_facts,
    project_source_claims,
    project_source_document_table,
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
        source_ids = {
            source_id for row in facts for source_id in row.source_ids
        }
        for row in (*source_claims, *source_documents):
            source_id = str(
                row.get("source_id")
                or row.get("document_id")
                or row.get("evidence_id")
                or ""
            ).strip()
            if source_id:
                source_ids.add(source_id)
        fact_projection = project_citable_evidence_facts(facts)
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
                    if key != "facts"
                },
                "source_claims": project_source_claims(source_claims),
                "source_documents": project_source_document_table(
                    source_documents
                ),
                "source_coverage": list(source_coverage),
            }
        )
        try:
            response = self.provider.complete(
                pass_name="BUSINESS_MODEL_RESEARCH", payload=payload
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
            cited_facts = _unique_strings(response["fact_ids"], "fact_ids")
            cited_sources = _unique_strings(response["source_ids"], "source_ids")
            unknown_facts = set(cited_facts) - set(fact_by_id)
            unknown_sources = set(cited_sources) - source_ids
            if unknown_facts:
                raise ValueError(f"unknown fact ids: {sorted(unknown_facts)}")
            if unknown_sources:
                raise ValueError(f"unknown source ids: {sorted(unknown_sources)}")
            memo = BusinessModelMemo(
                memo_id=stable_intelligence_id(
                    "BMMEMO",
                    {
                        "target_id": target_id,
                        "archetype_id": archetype_id,
                        "as_of_date": as_of_date,
                        "response": scrub_blind_research_payload(response),
                    },
                ),
                target_id=target_id,
                archetype_id=archetype_id,
                as_of_date=as_of_date,
                business_model_summary=str(response["business_model_summary"]),
                revenue_engines=_unique_strings(
                    response["revenue_engines"], "revenue_engines"
                ),
                cost_and_cash_drivers=_unique_strings(
                    response["cost_and_cash_drivers"], "cost_and_cash_drivers"
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
            return self._pending("INVALID_PROVIDER_OUTPUT", exc)
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
