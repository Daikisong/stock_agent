"""LLM-owned literal query generation for the v5 source graph."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_researcher import StructuredResearchProvider
from .schemas import assert_blind_research_output, scrub_blind_research_payload


CANONICAL_SOURCE_FAMILIES = (
    "OPENDART",
    "KIND_KRX",
    "ISSUER_EARNINGS_RELEASE",
    "ISSUER_PRESENTATION",
    "ISSUER_NEWSROOM",
    "CUSTOMER_OFFICIAL",
    "FINANCIAL_STATEMENTS",
    "SEGMENT_DATA",
    "CASH_FLOW",
    "MARKET_CAP_PRICE",
    "CONSENSUS_REVISION",
    "VALUATION_MULTIPLES",
    "REUTERS",
    "TRUSTED_BUSINESS_MEDIA",
    "PUBLIC_BROKER_PDF",
    "INDUSTRY_REPORT",
    "NAVER_DISCOVERY",
    "GENERAL_WEB_DISCOVERY",
)


@dataclass(frozen=True)
class GeneratedSourceQuery:
    query_id: str
    objective_id: str
    literal_query: str
    source_families: tuple[str, ...]
    rationale: str
    counter_or_supersession_search: bool
    generator_kind: str
    provider_name: str
    prompt_hash: str
    response_hash: str
    production_score_authority: bool = False

    def __post_init__(self) -> None:
        if not all(
            str(value).strip()
            for value in (
                self.query_id,
                self.objective_id,
                self.literal_query,
                self.rationale,
                self.provider_name,
                self.prompt_hash,
                self.response_hash,
            )
        ):
            raise ValueError("generated source query identity is incomplete")
        if self.generator_kind not in {"REAL_LLM", "TEST_FIXTURE_LLM"}:
            raise ValueError("literal query must have LLM generator lineage")
        if self.production_score_authority:
            raise ValueError("source queries cannot score")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SourceQueryGenerationResult:
    status: str
    queries: tuple[GeneratedSourceQuery, ...]
    rejected_suggestions: tuple[Mapping[str, str], ...]
    new_source_directions: tuple[str, ...]
    unresolved_research_notes: tuple[str, ...]
    feedback_for_next_llm_call: tuple[str, ...]
    provider_name: str
    prompt_hash: str
    response_hash: str | None
    deterministic_fallback_query_used: bool = False

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PARTIAL", "PENDING"}:
            raise ValueError("unknown source query generation status")
        if self.status == "PENDING" and not self.feedback_for_next_llm_call:
            raise ValueError("pending query generation requires LLM feedback")
        if self.deterministic_fallback_query_used:
            raise ValueError("deterministic fallback queries are forbidden")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "queries": [row.to_dict() for row in self.queries],
            "rejected_suggestions": [dict(row) for row in self.rejected_suggestions],
            "new_source_directions": list(self.new_source_directions),
            "unresolved_research_notes": list(self.unresolved_research_notes),
            "feedback_for_next_llm_call": list(self.feedback_for_next_llm_call),
            "provider_name": self.provider_name,
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "deterministic_fallback_query_used": False,
        }


class ResearcherSourceQueryPlanner:
    """Asks the LLM what to search; deterministic code only validates it."""

    def __init__(self, *, provider: StructuredResearchProvider) -> None:
        self.provider = provider

    def generate(
        self,
        *,
        target_id: str,
        target_name: str,
        target_aliases: Sequence[str],
        as_of_date: str,
        open_objectives: Sequence[Mapping[str, Any]],
        current_evidence_facts: Sequence[Mapping[str, Any]],
        current_counterfacts: Sequence[Mapping[str, Any]],
        target_business_model: Mapping[str, Any] | None,
        source_coverage: Sequence[str | Mapping[str, Any]],
        prior_query_failures: Sequence[Mapping[str, Any]],
        previously_executed_queries: Sequence[str],
        theme_context: Mapping[str, Any],
        score_gap_context: Mapping[str, Any],
        generator_kind: str,
    ) -> SourceQueryGenerationResult:
        if generator_kind not in {"REAL_LLM", "TEST_FIXTURE_LLM"}:
            raise ValueError("query generator kind must be an LLM path")
        objective_by_id = {
            str(row.get("objective_id") or ""): row for row in open_objectives
        }
        if "" in objective_by_id or len(objective_by_id) != len(open_objectives):
            raise ValueError("open source objectives require unique ids")
        previous = tuple(
            dict.fromkeys(
                _normalize_query(value)
                for value in previously_executed_queries
                if str(value).strip()
            )
        )
        payload = scrub_blind_research_payload(
            {
                "target_id": target_id,
                "target_name": target_name,
                "target_aliases": list(target_aliases),
                "as_of_date": as_of_date,
                "open_research_objectives": list(open_objectives),
                "current_evidence_fact_graph": list(current_evidence_facts),
                "current_counterfacts": list(current_counterfacts),
                "target_business_model": target_business_model,
                "source_coverage": list(source_coverage),
                "prior_query_or_source_failures": list(prior_query_failures),
                "previously_executed_queries": list(previously_executed_queries),
                "theme_context": dict(theme_context),
                "score_gap_context": dict(score_gap_context),
            }
        )
        prompt_hash = stable_intelligence_id("QUERYPROMPT", payload)
        try:
            response = self.provider.complete(
                pass_name="SOURCE_QUERY_GENERATION", payload=payload
            )
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
        ) as exc:
            reason = "QUERY_PROVIDER_ERROR:" + _error_text(exc)
            return SourceQueryGenerationResult(
                status="PENDING",
                queries=(),
                rejected_suggestions=(),
                new_source_directions=(),
                unresolved_research_notes=(),
                feedback_for_next_llm_call=(reason,),
                provider_name=_provider_name(self.provider),
                prompt_hash=prompt_hash,
                response_hash=None,
            )
        response_hash = stable_intelligence_id(
            "QUERYRESP", scrub_blind_research_payload(response)
        )
        try:
            assert_blind_research_output(response)
            suggestions = response["suggested_queries"]
            if isinstance(suggestions, (str, bytes)) or not isinstance(
                suggestions, Sequence
            ):
                raise TypeError("suggested_queries must be an array")
            new_directions = _unique_strings(response["new_source_directions"])
            unresolved_notes = _unique_strings(
                response["unresolved_research_notes"]
            )
        except (KeyError, TypeError, ValueError) as exc:
            reason = "INVALID_QUERY_PROVIDER_OUTPUT:" + _error_text(exc)
            return SourceQueryGenerationResult(
                status="PENDING",
                queries=(),
                rejected_suggestions=(),
                new_source_directions=(),
                unresolved_research_notes=(),
                feedback_for_next_llm_call=(reason,),
                provider_name=_provider_name(self.provider),
                prompt_hash=prompt_hash,
                response_hash=response_hash,
            )
        accepted = []
        rejected = []
        seen = set(previous)
        target_terms = tuple(
            str(value).casefold()
            for value in dict.fromkeys((target_name, target_id, *target_aliases))
            if str(value).strip()
        )
        cutoff = date.fromisoformat(as_of_date)
        for index, raw in enumerate(suggestions):
            if not isinstance(raw, Mapping):
                rejected.append(
                    {"suggestion_index": str(index), "reason": "NOT_AN_OBJECT"}
                )
                continue
            objective_id = str(raw.get("objective_id") or "").strip()
            literal_query = " ".join(
                str(raw.get("literal_query") or "").split()
            ).strip()
            reason = _query_rejection_reason(
                objective_id=objective_id,
                literal_query=literal_query,
                source_families=raw.get("source_families"),
                objective_ids=set(objective_by_id),
                target_terms=target_terms,
                seen_queries=seen,
                cutoff=cutoff,
            )
            if reason:
                rejected.append(
                    {
                        "suggestion_index": str(index),
                        "objective_id": objective_id,
                        "literal_query": literal_query,
                        "reason": reason,
                    }
                )
                continue
            normalized = _normalize_query(literal_query)
            seen.add(normalized)
            families = _unique_strings(raw.get("source_families"))
            query = GeneratedSourceQuery(
                query_id=stable_intelligence_id(
                    "SGQUERY",
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "objective_id": objective_id,
                        "literal_query": literal_query,
                    },
                ),
                objective_id=objective_id,
                literal_query=literal_query,
                source_families=families,
                rationale=str(raw.get("rationale") or "").strip(),
                counter_or_supersession_search=bool(
                    raw.get("counter_or_supersession_search")
                ),
                generator_kind=generator_kind,
                provider_name=_provider_name(self.provider),
                prompt_hash=prompt_hash,
                response_hash=response_hash,
            )
            if not query.rationale:
                rejected.append(
                    {
                        "suggestion_index": str(index),
                        "objective_id": objective_id,
                        "literal_query": literal_query,
                        "reason": "RATIONALE_EMPTY",
                    }
                )
                seen.remove(normalized)
                continue
            accepted.append(query)
        feedback = tuple(
            f"{row.get('reason')}:{row.get('literal_query') or row.get('suggestion_index')}"
            for row in rejected
        )
        if not accepted:
            feedback = feedback or ("LLM_RETURNED_NO_NEW_VALID_QUERY",)
            status = "PENDING"
        elif rejected:
            status = "PARTIAL"
        else:
            status = "COMPLETE"
        return SourceQueryGenerationResult(
            status=status,
            queries=tuple(accepted),
            rejected_suggestions=tuple(rejected),
            new_source_directions=new_directions,
            unresolved_research_notes=unresolved_notes,
            feedback_for_next_llm_call=feedback,
            provider_name=_provider_name(self.provider),
            prompt_hash=prompt_hash,
            response_hash=response_hash,
        )


def _query_rejection_reason(
    *,
    objective_id: str,
    literal_query: str,
    source_families: Any,
    objective_ids: set[str],
    target_terms: Sequence[str],
    seen_queries: set[str],
    cutoff: date,
) -> str | None:
    if objective_id not in objective_ids:
        return "UNKNOWN_OBJECTIVE_ID"
    if not literal_query or len(literal_query) > 500:
        return "EMPTY_OR_OVERSIZED_QUERY"
    normalized = _normalize_query(literal_query)
    if normalized in seen_queries:
        return "DUPLICATE_OR_ALREADY_EXECUTED_QUERY"
    if target_terms and not any(term in literal_query.casefold() for term in target_terms):
        return "TARGET_SCOPE_MISSING"
    try:
        families = _unique_strings(source_families)
    except (TypeError, ValueError):
        return "INVALID_SOURCE_FAMILIES"
    if not families or set(families) - set(CANONICAL_SOURCE_FAMILIES):
        return "UNKNOWN_SOURCE_FAMILY"
    for raw_date in re.findall(r"\b\d{4}-\d{2}-\d{2}\b", literal_query):
        try:
            query_date = date.fromisoformat(raw_date)
        except ValueError:
            return "INVALID_QUERY_DATE"
        if query_date > cutoff:
            return "FUTURE_DATE_QUERY"
    return None


def _normalize_query(value: str) -> str:
    return " ".join(str(value).casefold().split())


def _unique_strings(value: Any) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise TypeError("expected string array")
    result = tuple(str(item).strip() for item in value)
    if any(not item for item in result) or len(result) != len(set(result)):
        raise ValueError("string array must contain unique nonempty values")
    return result


def _provider_name(provider: StructuredResearchProvider) -> str:
    return str(getattr(provider, "provider_name", provider.__class__.__name__))


def _error_text(error: Exception) -> str:
    return " ".join(str(error).split())[-500:] or error.__class__.__name__


__all__ = [
    "CANONICAL_SOURCE_FAMILIES",
    "GeneratedSourceQuery",
    "ResearcherSourceQueryPlanner",
    "SourceQueryGenerationResult",
]
