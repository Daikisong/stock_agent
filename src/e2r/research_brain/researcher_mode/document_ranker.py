"""Material-relevance document ranking without a fixed top-N completion gate."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_researcher import StructuredResearchProvider
from .prompt_projection import project_candidate_ranking_evidence_context
from .schemas import ComponentResearchPlan
from .schemas import assert_blind_research_output, scrub_blind_research_payload


@dataclass(frozen=True)
class DocumentRelevanceDecision:
    document_id: str
    material_relevance: bool
    relevance_score: float
    matched_research_questions: tuple[str, ...]
    reasons: tuple[str, ...]
    evidence_eligible: bool

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "document_id": self.document_id,
            "material_relevance": self.material_relevance,
            "relevance_score": self.relevance_score,
            "matched_research_questions": list(self.matched_research_questions),
            "reasons": list(self.reasons),
            "evidence_eligible": self.evidence_eligible,
        }


@dataclass(frozen=True)
class SourceCandidateMaterialityDecision:
    decision_id: str
    candidate_id: str
    material_relevance: bool
    priority: float
    objective_ids: tuple[str, ...]
    matched_requested_source_family: str | None
    rationale: str
    snippet_discovery_only: bool = True
    evidence_eligible: bool = False
    score_authority: bool = False

    def __post_init__(self) -> None:
        if not self.decision_id or not self.candidate_id or not self.rationale.strip():
            raise ValueError("candidate materiality decision identity is required")
        if not 0 <= float(self.priority) <= 1:
            raise ValueError("candidate materiality priority must be between 0 and 1")
        if not self.snippet_discovery_only or self.evidence_eligible or self.score_authority:
            raise ValueError("search-result metadata cannot become evidence or score")
        if self.material_relevance and not self.objective_ids:
            raise ValueError("material candidate must map to a research objective")
        if (
            self.material_relevance
            and not self.matched_requested_source_family
        ):
            raise ValueError(
                "material candidate must match one requested source family"
            )

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "decision_id": self.decision_id,
            "candidate_id": self.candidate_id,
            "material_relevance": self.material_relevance,
            "priority": self.priority,
            "objective_ids": list(self.objective_ids),
            "matched_requested_source_family": (
                self.matched_requested_source_family or "NONE"
            ),
            "rationale": self.rationale,
            "snippet_discovery_only": self.snippet_discovery_only,
            "evidence_eligible": self.evidence_eligible,
            "score_authority": self.score_authority,
        }


@dataclass(frozen=True)
class CandidateRankingResult:
    status: str
    decisions: tuple[SourceCandidateMaterialityDecision, ...]
    pending_reasons: tuple[str, ...]
    provider_name: str
    prompt_hash: str
    response_hash: str | None
    completion_flag_reconciled: bool = False

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown candidate ranking status")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending candidate ranking requires reasons")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "decisions": [row.to_dict() for row in self.decisions],
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "completion_flag_reconciled": self.completion_flag_reconciled,
        }


class ResearcherDocumentRanker:
    """LLM semantic ranker that accounts for every discovery candidate."""

    def __init__(self, *, provider: StructuredResearchProvider) -> None:
        self.provider = provider

    def rank_candidates(
        self,
        *,
        target_id: str,
        target_name: str,
        as_of_date: str,
        open_objectives: Sequence[Mapping[str, Any]],
        candidates: Sequence[Mapping[str, Any]],
        current_evidence_facts: Sequence[Mapping[str, Any]],
        target_business_model: Mapping[str, Any] | None,
        source_coverage: Sequence[str | Mapping[str, Any]],
    ) -> CandidateRankingResult:
        candidate_by_id = {
            str(row.get("candidate_id") or ""): row for row in candidates
        }
        if "" in candidate_by_id or len(candidate_by_id) != len(candidates):
            raise ValueError("candidate ids must be nonempty and unique")
        objective_ids = {
            str(row.get("objective_id") or "") for row in open_objectives
        }
        if "" in objective_ids:
            raise ValueError("source objective id is required")
        payload = scrub_blind_research_payload(
            {
                "target_id": target_id,
                "target_name": target_name,
                "as_of_date": as_of_date,
                "open_research_objectives": list(open_objectives),
                "discovery_candidates": [
                    {
                        "candidate_id": row["candidate_id"],
                        "title": row.get("title"),
                        "url": row.get("url"),
                        "snippet": row.get("snippet"),
                        "source": row.get("source"),
                        "published_at": row.get("published_at"),
                        "is_pdf": bool(row.get("is_pdf")),
                        "is_news": bool(row.get("is_news")),
                        "is_disclosure": bool(row.get("is_disclosure")),
                        "query_ids": list(
                            row.get("materiality_query_ids")
                            or row.get("query_ids")
                            or ()
                        ),
                        "objective_ids": list(row.get("objective_ids") or ()),
                        "requested_source_families": list(
                            row.get("requested_source_families") or ()
                        ),
                        "verified_official_domain_candidate": bool(
                            row.get("verified_official_domain_candidate")
                        ),
                        "candidate_source_family_hint": row.get(
                            "candidate_source_family_hint"
                        ),
                        "graph_expansion_parent_document_ids": list(
                            row.get("graph_expansion_parent_document_ids") or ()
                        ),
                        "graph_expansion_parent_candidate_ids": list(
                            row.get("graph_expansion_parent_candidate_ids") or ()
                        ),
                        "snippet_discovery_only": True,
                    }
                    for row in candidates
                ],
                "current_evidence_fact_graph": (
                    project_candidate_ranking_evidence_context(
                        current_evidence_facts
                    )
                ),
                "target_business_model": target_business_model,
                "source_coverage": list(source_coverage),
            }
        )
        partition_limit = _semantic_partition_character_limit(self.provider)
        candidate_count_limit = _candidate_partition_count_limit(
            self.provider
        )
        if (
            len(candidates) > 1
            and (
                (
                    candidate_count_limit is not None
                    and len(candidates) > candidate_count_limit
                )
                or (
                    partition_limit is not None
                    and len(
                        json.dumps(
                            payload,
                            ensure_ascii=False,
                            sort_keys=True,
                            separators=(",", ":"),
                        )
                    )
                    > partition_limit
                )
            )
        ):
            return self._rank_candidate_partitions(
                target_id=target_id,
                target_name=target_name,
                as_of_date=as_of_date,
                open_objectives=open_objectives,
                candidates=candidates,
                current_evidence_facts=current_evidence_facts,
                target_business_model=target_business_model,
                source_coverage=source_coverage,
            )
        attempt_payload = payload
        prompt_hash = stable_intelligence_id("RANKPROMPT", attempt_payload)
        response_hash = None
        decisions: tuple[SourceCandidateMaterialityDecision, ...] = ()
        ranking_complete = False
        notes: tuple[str, ...] = ()
        completion_flag_reconciled = False
        for attempt_index in range(2):
            prompt_hash = stable_intelligence_id("RANKPROMPT", attempt_payload)
            try:
                response = self.provider.complete(
                    pass_name="SOURCE_CANDIDATE_RANKING",
                    payload=attempt_payload,
                )
            except (
                StructuredProviderUnavailable,
                StructuredProviderRejected,
                TimeoutError,
                OSError,
                RuntimeError,
            ) as exc:
                return CandidateRankingResult(
                    status="PENDING",
                    decisions=(),
                    pending_reasons=(f"RANKING_PROVIDER_ERROR:{_error_text(exc)}",),
                    provider_name=_provider_name(self.provider),
                    prompt_hash=prompt_hash,
                    response_hash=None,
                )
            response_hash = stable_intelligence_id(
                "RANKRESP", scrub_blind_research_payload(response)
            )
            try:
                decisions, ranking_complete, notes = _decode_candidate_ranking(
                    response=response,
                    candidate_by_id=candidate_by_id,
                    objective_ids=objective_ids,
                )
                if not ranking_complete:
                    complete_roster = (
                        len(decisions) == len(candidate_by_id)
                        and {
                            row.candidate_id for row in decisions
                        } == set(candidate_by_id)
                    )
                    if attempt_index == 1 and complete_roster:
                        ranking_complete = True
                        completion_flag_reconciled = True
                    else:
                        raise ValueError(
                            "candidate ranking declared incomplete after candidate "
                            "accounting"
                            + (":" + " | ".join(notes) if notes else "")
                        )
            except (KeyError, TypeError, ValueError) as exc:
                _invalidate_provider_response_cache(self.provider, exc)
                if attempt_index == 0:
                    # Do not coerce, drop, or deterministically replace invalid
                    # LLM decisions.  Return the exact contract failure and the
                    # complete allowed-id roster to the LLM for a clean rewrite.
                    attempt_payload = scrub_blind_research_payload(
                        {
                            **payload,
                            "ranking_retry_context": {
                                "validation_error": _error_text(exc),
                                "required_candidate_ids": sorted(candidate_by_id),
                                "required_objective_ids": sorted(objective_ids),
                                "instruction": (
                                    "Rewrite the complete decisions array using "
                                    "each required candidate_id exactly once. "
                                    "ranking_complete means every discovery "
                                    "candidate was classified, not that every "
                                    "candidate supplies sufficient evidence. Mark "
                                    "irrelevant, future, or nonresolving candidates "
                                    "material_relevance=false with a rationale, then "
                                    "set ranking_complete=true after the full roster "
                                    "is accounted."
                                ),
                            },
                        }
                    )
                    continue
                if len(candidates) > 1:
                    return self._rank_candidate_partitions(
                        target_id=target_id,
                        target_name=target_name,
                        as_of_date=as_of_date,
                        open_objectives=open_objectives,
                        candidates=candidates,
                        current_evidence_facts=current_evidence_facts,
                        target_business_model=target_business_model,
                        source_coverage=source_coverage,
                    )
                return CandidateRankingResult(
                    status="PENDING",
                    decisions=(),
                    pending_reasons=(
                        f"INVALID_RANKING_OUTPUT:{_error_text(exc)}",
                    ),
                    provider_name=_provider_name(self.provider),
                    prompt_hash=prompt_hash,
                    response_hash=response_hash,
                )
            break
        if not ranking_complete:
            return CandidateRankingResult(
                status="PENDING",
                decisions=tuple(decisions),
                pending_reasons=(
                    "RANKING_DECLARED_INCOMPLETE",
                    *notes,
                ),
                provider_name=_provider_name(self.provider),
                prompt_hash=prompt_hash,
                response_hash=response_hash,
            )
        return CandidateRankingResult(
            status="COMPLETE",
            decisions=tuple(
                sorted(decisions, key=lambda row: (-row.priority, row.candidate_id))
            ),
            pending_reasons=(),
            provider_name=_provider_name(self.provider),
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            completion_flag_reconciled=completion_flag_reconciled,
        )

    def _rank_candidate_partitions(
        self,
        *,
        target_id: str,
        target_name: str,
        as_of_date: str,
        open_objectives: Sequence[Mapping[str, Any]],
        candidates: Sequence[Mapping[str, Any]],
        current_evidence_facts: Sequence[Mapping[str, Any]],
        target_business_model: Mapping[str, Any] | None,
        source_coverage: Sequence[str | Mapping[str, Any]],
    ) -> CandidateRankingResult:
        """Losslessly split a roster only after two invalid full rewrites.

        This is transport recovery, not top-N selection: both deterministic
        halves are evaluated, every candidate id must reappear, and all
        decisions are recombined before the caller advances the checkpoint.
        """

        candidate_count_limit = _candidate_partition_count_limit(self.provider)
        if (
            candidate_count_limit is not None
            and len(candidates) > candidate_count_limit
        ):
            partitions = tuple(
                tuple(candidates[start : start + candidate_count_limit])
                for start in range(0, len(candidates), candidate_count_limit)
            )
        else:
            midpoint = len(candidates) // 2
            partitions = (
                tuple(candidates[:midpoint]),
                tuple(candidates[midpoint:]),
            )
        results = tuple(
            self.rank_candidates(
                target_id=target_id,
                target_name=target_name,
                as_of_date=as_of_date,
                open_objectives=open_objectives,
                candidates=partition,
                current_evidence_facts=current_evidence_facts,
                target_business_model=target_business_model,
                source_coverage=source_coverage,
            )
            for partition in partitions
            if partition
        )
        decisions = tuple(
            sorted(
                (decision for result in results for decision in result.decisions),
                key=lambda row: (-row.priority, row.candidate_id),
            )
        )
        expected_ids = {
            str(candidate.get("candidate_id") or "") for candidate in candidates
        }
        received_ids = {decision.candidate_id for decision in decisions}
        roster_complete = bool(
            len(decisions) == len(received_ids)
            and received_ids == expected_ids
        )
        all_complete = bool(
            roster_complete
            and results
            and all(result.status == "COMPLETE" for result in results)
        )
        split_lineage = [
            {
                "prompt_hash": result.prompt_hash,
                "response_hash": result.response_hash,
                "status": result.status,
                "decision_count": len(result.decisions),
            }
            for result in results
        ]
        if all_complete:
            return CandidateRankingResult(
                status="COMPLETE",
                decisions=decisions,
                pending_reasons=(),
                provider_name=_provider_name(self.provider),
                prompt_hash=stable_intelligence_id(
                    "RANKPROMPT-SPLIT", split_lineage
                ),
                response_hash=stable_intelligence_id(
                    "RANKRESP-SPLIT",
                    [decision.to_dict() for decision in decisions],
                ),
                completion_flag_reconciled=any(
                    result.completion_flag_reconciled
                    for result in results
                ),
            )
        pending_reasons = ["SEMANTIC_RANKING_SPLIT_PENDING"]
        if not roster_complete:
            pending_reasons.append(
                "SEMANTIC_RANKING_SPLIT_ROSTER_MISMATCH:"
                f"expected={len(expected_ids)}:received={len(received_ids)}"
            )
        pending_reasons.extend(
            f"PARTITION_{index}:{reason}"
            for index, result in enumerate(results)
            for reason in result.pending_reasons
        )
        return CandidateRankingResult(
            status="PENDING",
            decisions=decisions,
            pending_reasons=tuple(pending_reasons),
            provider_name=_provider_name(self.provider),
            prompt_hash=stable_intelligence_id(
                "RANKPROMPT-SPLIT-PENDING", split_lineage
            ),
            response_hash=None,
            completion_flag_reconciled=any(
                result.completion_flag_reconciled
                for result in results
            ),
        )


def _decode_candidate_ranking(
    *,
    response: Mapping[str, Any],
    candidate_by_id: Mapping[str, Mapping[str, Any]],
    objective_ids: set[str],
) -> tuple[
    tuple[SourceCandidateMaterialityDecision, ...],
    bool,
    tuple[str, ...],
]:
    assert_blind_research_output(response)
    raw_decisions = response["decisions"]
    if isinstance(raw_decisions, (str, bytes)) or not isinstance(
        raw_decisions, Sequence
    ):
        raise TypeError("candidate decisions must be an array")
    decisions = []
    seen = set()
    for raw in raw_decisions:
        if not isinstance(raw, Mapping):
            raise TypeError("candidate decision must be an object")
        candidate_id = str(raw.get("candidate_id") or "")
        if candidate_id not in candidate_by_id or candidate_id in seen:
            raise ValueError("candidate ranking has unknown or duplicate id")
        seen.add(candidate_id)
        cited_objectives = _unique_strings(raw.get("objective_ids"))
        if set(cited_objectives) - objective_ids:
            raise ValueError("candidate ranking cited unknown objective")
        candidate = candidate_by_id[candidate_id]
        candidate_objective_ids = set(
            _unique_strings(candidate.get("objective_ids") or ())
        )
        if set(cited_objectives) - candidate_objective_ids:
            raise ValueError(
                "candidate ranking cited an objective outside its query edge"
            )
        requested_source_families = set(
            _unique_strings(
                candidate.get("requested_source_families") or ()
            )
        )
        raw_matched_source_family = str(
            raw.get("matched_requested_source_family") or ""
        ).strip()
        matched_source_family = (
            None
            if raw_matched_source_family == "NONE"
            else raw_matched_source_family
        )
        if (
            not raw_matched_source_family
            or (
                matched_source_family is not None
                and matched_source_family not in requested_source_families
            )
        ):
            raise ValueError(
                "candidate ranking cited an unrequested source family"
            )
        material_relevance = bool(raw["material_relevance"])
        if material_relevance and not matched_source_family:
            raise ValueError(
                "candidate materiality and requested source family mismatch"
            )
        decisions.append(
            SourceCandidateMaterialityDecision(
                decision_id=stable_intelligence_id(
                    "MATDEC",
                    {
                        "candidate_id": candidate_id,
                        "response": scrub_blind_research_payload(raw),
                    },
                ),
                candidate_id=candidate_id,
                material_relevance=material_relevance,
                priority=float(raw["priority"]),
                objective_ids=cited_objectives,
                matched_requested_source_family=matched_source_family,
                rationale=str(raw["rationale"]),
            )
        )
    ranking_complete = bool(response["ranking_complete"])
    missing = set(candidate_by_id) - seen
    if ranking_complete and missing:
        raise ValueError(
            "complete candidate ranking omitted ids: " + ",".join(sorted(missing))
        )
    return tuple(decisions), ranking_complete, _unique_strings(
        response.get("unresolved_notes")
    )


class MaterialDocumentRanker:
    """Ranks every candidate and retains every material one.

    Token overlap is a retrieval signal only.  It never creates an
    EvidenceFact, a component point, absence, or completion decision.
    """

    def rank(
        self,
        *,
        target_id: str,
        as_of_date: str,
        documents: Sequence[Mapping[str, Any]],
        research_plans: Sequence[ComponentResearchPlan],
    ) -> tuple[DocumentRelevanceDecision, ...]:
        cutoff = date.fromisoformat(as_of_date)
        questions = tuple(
            dict.fromkeys(
                question
                for plan in research_plans
                for question in plan.research_questions
            )
        )
        question_tokens = {question: _tokens(question) for question in questions}
        decisions = []
        seen = set()
        for row in documents:
            document_id = str(
                row.get("document_id") or row.get("source_id") or ""
            ).strip()
            if not document_id:
                raise ValueError("document_id is required")
            if document_id in seen:
                raise ValueError("document ids must be unique")
            seen.add(document_id)
            content = str(
                row.get("full_text")
                or row.get("content")
                or row.get("body")
                or ""
            ).strip()
            is_snippet = bool(row.get("snippet_only")) or str(
                row.get("document_kind") or ""
            ).upper() in {"SNIPPET", "SEARCH_RESULT"}
            published = _published_date(row)
            future = bool(published and published > cutoff)
            row_target = str(row.get("target_id") or "").strip()
            target_match = row_target == target_id or target_id.lower() in content.lower()
            content_tokens = _tokens(content)
            matched = tuple(
                question
                for question, tokens in question_tokens.items()
                if tokens and len(tokens & content_tokens) / len(tokens) >= 0.20
            )
            source_tier = str(row.get("source_tier") or row.get("source_family") or "")
            authoritative = source_tier.upper() in {
                "ISSUER_OFFICIAL",
                "OFFICIAL_FILING",
                "CUSTOMER_OFFICIAL",
                "STRUCTURED",
                "TRUSTED_INDEPENDENT",
            }
            evidence_eligible = bool(content) and not is_snippet and not future
            score = (
                (0.35 if target_match else 0.0)
                + (0.35 * min(1.0, len(matched) / max(1, len(questions))))
                + (0.20 if authoritative else 0.0)
                + (0.10 if evidence_eligible else 0.0)
            )
            material = evidence_eligible and target_match and (
                bool(matched) or authoritative
            )
            reasons = []
            if future:
                reasons.append("FUTURE_DOCUMENT_EXCLUDED")
            if is_snippet:
                reasons.append("SNIPPET_DISCOVERY_ONLY")
            if not content:
                reasons.append("FULL_DOCUMENT_NOT_FETCHED")
            if not target_match:
                reasons.append("TARGET_SCOPE_NOT_ESTABLISHED")
            if matched:
                reasons.append("MATERIAL_RESEARCH_QUESTION_MATCH")
            if authoritative:
                reasons.append("AUTHORITATIVE_SOURCE_FAMILY")
            decisions.append(
                DocumentRelevanceDecision(
                    document_id=document_id,
                    material_relevance=material,
                    relevance_score=round(score, 6),
                    matched_research_questions=matched,
                    reasons=tuple(reasons),
                    evidence_eligible=evidence_eligible,
                )
            )
        return tuple(
            sorted(decisions, key=lambda row: (-row.relevance_score, row.document_id))
        )

    def select_material(
        self, decisions: Sequence[DocumentRelevanceDecision]
    ) -> tuple[str, ...]:
        """Return all material ids; deliberately no top_n parameter exists."""

        return tuple(
            row.document_id for row in decisions if row.material_relevance
        )


def _published_date(row: Mapping[str, Any]) -> date | None:
    raw = str(
        row.get("published_at")
        or row.get("publication_date")
        or row.get("filed_at")
        or ""
    ).strip()
    if not raw:
        return None
    try:
        return date.fromisoformat(raw[:10])
    except ValueError:
        return None


def _tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[0-9A-Za-z가-힣_]{2,}", value.lower())
        if token
    }


def _unique_strings(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, (str, bytes)):
        values = (value,)
    elif isinstance(value, Sequence):
        values = value
    else:
        raise TypeError("expected string array")
    result = tuple(str(item).strip() for item in values)
    if any(not item for item in result) or len(result) != len(set(result)):
        raise ValueError("string array must contain unique nonempty values")
    return result


def _provider_name(provider: StructuredResearchProvider) -> str:
    return str(getattr(provider, "provider_name", provider.__class__.__name__))


def _semantic_partition_character_limit(
    provider: StructuredResearchProvider,
) -> int | None:
    value = getattr(
        provider,
        "candidate_ranking_prompt_chunk_chars",
        None,
    )
    if value is None:
        value = getattr(provider, "semantic_prompt_chunk_chars", None)
    if isinstance(value, bool) or not isinstance(value, int) or value < 10_000:
        return None
    return value


def _candidate_partition_count_limit(
    provider: StructuredResearchProvider,
) -> int | None:
    value = getattr(
        provider,
        "candidate_ranking_page_candidate_limit",
        None,
    )
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        return None
    return value


def _error_text(error: Exception) -> str:
    return " ".join(str(error).split())[-500:] or error.__class__.__name__


def _invalidate_provider_response_cache(
    provider: StructuredResearchProvider,
    error: Exception,
) -> None:
    """Evict only the candidate response rejected by semantic validation."""

    invalidate = getattr(provider, "invalidate_last_response_cache", None)
    if not callable(invalidate):
        return
    try:
        invalidate(reason=f"{error.__class__.__name__}:{_error_text(error)}")
    except (OSError, TypeError, ValueError, RuntimeError):
        return


__all__ = [
    "CandidateRankingResult",
    "DocumentRelevanceDecision",
    "MaterialDocumentRanker",
    "ResearcherDocumentRanker",
    "SourceCandidateMaterialityDecision",
]
