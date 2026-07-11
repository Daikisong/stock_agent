"""Semantic failure를 LLM 재조사 context로 바꾸되 query 자체는 만들지 않는다."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash


RESEARCH_REPAIR_FAILURE_CLASSES = {
    "NO_DOCUMENT_FOUND",
    "WRONG_BUSINESS_SEGMENT",
    "WRONG_PRODUCT_FAMILY",
    "WRONG_SUBJECT",
    "STALE_ONLY",
    "GENERIC_CONTEXT_ONLY",
    "SNIPPET_ONLY",
    "DOCUMENT_PARSE_FAILED",
    "REROUTED_MECHANISM",
    "CLAIM_EXTRACTION_FAILED",
    "IMPACT_MAPPING_FAILED",
    "COUNTER_ONLY",
    "PROVIDER_FAILED",
    "BUDGET_EXHAUSTED",
    "GOLD_MATERIAL_FACT_MISSED",
}

FAILURE_NEXT_ACTIONS = {
    "NO_DOCUMENT_FOUND": "CHANGE_SOURCE_ROUTE_AND_REPLAN",
    "WRONG_BUSINESS_SEGMENT": "TIGHTEN_BUSINESS_MECHANISM_SCOPE",
    "WRONG_PRODUCT_FAMILY": "TIGHTEN_PRODUCT_SCOPE",
    "WRONG_SUBJECT": "TIGHTEN_TARGET_IDENTITY_AND_DIRECTNESS",
    "STALE_ONLY": "FIND_CURRENT_OR_SUPERSEDING_SOURCE",
    "GENERIC_CONTEXT_ONLY": "PRIORITIZE_TARGET_DIRECT_QUANTIFIED_SOURCE",
    "SNIPPET_ONLY": "FETCH_ORIGINAL_FULL_DOCUMENT",
    "DOCUMENT_PARSE_FAILED": "RESELECT_SECTION_TABLE_OR_PARSER",
    "REROUTED_MECHANISM": "PRESERVE_REROUTED_IMPACT_AND_REPLAN_ORIGINAL_GAP",
    "CLAIM_EXTRACTION_FAILED": "RESELECT_ANCHOR_AND_REEXTRACT_CLAIM",
    "IMPACT_MAPPING_FAILED": "READJUDICATE_CLAIM_PRIMITIVE_EDGE",
    "COUNTER_ONLY": "PRESERVE_COUNTER_AND_SEARCH_SUPPORT_ROUTE",
    "PROVIDER_FAILED": "CHANGE_OR_RETRY_PROVIDER_WITH_FAILURE_CONTEXT",
    "BUDGET_EXHAUSTED": "KEEP_PENDING_AND_PLAN_NEW_BOUNDED_TASK",
    "GOLD_MATERIAL_FACT_MISSED": "REPLAN_WITHOUT_GOLD_SOURCE_OR_FACT",
}

_ALIASES = {
    "NO_RELEVANT_CLAIM": "GENERIC_CONTEXT_ONLY",
    "SOURCE_EXHAUSTED": "NO_DOCUMENT_FOUND",
    "REROUTED_PRIMITIVE": "REROUTED_MECHANISM",
    "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN": "REROUTED_MECHANISM",
    "IMPACT_MAPPING_REJECTED": "IMPACT_MAPPING_FAILED",
    "IMPACT_ADJUDICATION_REQUIRED": "IMPACT_MAPPING_FAILED",
    "PROVIDER_PENDING": "PROVIDER_FAILED",
    "BUDGET_PENDING": "BUDGET_EXHAUSTED",
}
_URL_RE = re.compile(r"https?://\S+", re.IGNORECASE)
_FORBIDDEN_GOLD_KEYS = {
    "gold_fact_id",
    "gold_source_url",
    "gold_query",
    "expected_component",
    "expected_score",
}


@dataclass(frozen=True)
class AdaptiveResearchRepairDirective:
    directive_id: str
    failure_class: str
    next_action: str
    question_family_id: str
    original_question: str
    score_gap_context: Mapping[str, Any]
    query_generation_owner: str
    deterministic_fallback_query_allowed: bool
    require_novel_query: bool
    preserve_rerouted_impacts: bool
    preserve_counter_evidence: bool
    original_gap_open: bool
    terminal_status_if_unresolved: str

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


def canonical_research_failure_class(status: str) -> str:
    value = str(status or "").upper()
    if not value:
        return "NO_DOCUMENT_FOUND"
    canonical = _ALIASES.get(value, value)
    if canonical not in RESEARCH_REPAIR_FAILURE_CLASSES:
        raise ValueError(f"unknown adaptive research failure class: {status}")
    return canonical


def compile_research_repair_directive(
    *,
    failure_class: str,
    question_family_id: str,
    original_question: str,
    failure_reason: str,
    missing_route_categories: Sequence[str] = (),
    rejected_document_reasons: Sequence[str] = (),
    preserved_evidence_ids: Sequence[str] = (),
    validation_feedback: Sequence[str] = (),
) -> AdaptiveResearchRepairDirective:
    canonical = canonical_research_failure_class(failure_class)
    if not question_family_id.strip() or not original_question.strip():
        raise ValueError("adaptive repair requires the original material question")
    sanitized_reason = _URL_RE.sub("[REDACTED_SOURCE]", failure_reason)
    safe_preserved_ids = (
        ()
        if canonical == "GOLD_MATERIAL_FACT_MISSED"
        else tuple(
            dict.fromkeys(
                str(value) for value in preserved_evidence_ids if str(value)
            )
        )
    )
    safe_validation_feedback = (
        ()
        if canonical == "GOLD_MATERIAL_FACT_MISSED"
        else tuple(
            _URL_RE.sub("[REDACTED_SOURCE]", str(value))
            for value in validation_feedback
            if str(value)
        )
    )
    context = {
        "failure_class": canonical,
        "failure_reason": sanitized_reason,
        "missing_route_categories": tuple(
            sorted({str(value) for value in missing_route_categories if str(value)})
        ),
        "rejected_document_reasons": tuple(
            sorted({str(value) for value in rejected_document_reasons if str(value)})
        ),
        "preserved_evidence_ids": safe_preserved_ids,
        "validation_feedback": safe_validation_feedback,
        "instruction": (
            "Use the current evidence and this failure diagnosis to propose a new, "
            "target-specific query. Do not repeat an executed query. Do not infer "
            "a score or Stage. Do not use a gold URL, gold fact, or expected output."
        ),
    }
    _assert_no_gold_payload(context)
    terminal = {
        "PROVIDER_FAILED": "PROVIDER_PENDING",
        "BUDGET_EXHAUSTED": "BUDGET_PENDING",
    }.get(canonical, "SOURCE_PENDING")
    payload = {
        "failure_class": canonical,
        "question_family_id": question_family_id,
        "original_question": original_question,
        "score_gap_context": context,
        "next_action": FAILURE_NEXT_ACTIONS[canonical],
    }
    return AdaptiveResearchRepairDirective(
        directive_id="REPAIR-" + stable_hash(payload)[:24],
        failure_class=canonical,
        next_action=FAILURE_NEXT_ACTIONS[canonical],
        question_family_id=question_family_id,
        original_question=original_question,
        score_gap_context=context,
        query_generation_owner="LLM",
        deterministic_fallback_query_allowed=False,
        require_novel_query=True,
        preserve_rerouted_impacts=canonical == "REROUTED_MECHANISM",
        preserve_counter_evidence=canonical == "COUNTER_ONLY",
        original_gap_open=True,
        terminal_status_if_unresolved=terminal,
    )


def audit_adaptive_repair_contract() -> Mapping[str, Any]:
    directives = tuple(
        compile_research_repair_directive(
            failure_class=failure_class,
            question_family_id="GENERIC_MATERIAL_QUESTION",
            original_question="What current source-backed fact resolves this material question?",
            failure_reason="controlled contract audit",
            preserved_evidence_ids=("EVIDENCE-1",),
        )
        for failure_class in sorted(RESEARCH_REPAIR_FAILURE_CLASSES)
    )
    by_failure = {row.failure_class: row for row in directives}
    critical = {
        "failure_class_without_action_count": len(
            RESEARCH_REPAIR_FAILURE_CLASSES - set(FAILURE_NEXT_ACTIONS)
        ),
        "deterministic_fallback_query_allowed_count": sum(
            row.deterministic_fallback_query_allowed for row in directives
        ),
        "non_llm_query_owner_count": sum(
            row.query_generation_owner != "LLM" for row in directives
        ),
        "rerouted_impact_not_preserved_count": int(
            not by_failure["REROUTED_MECHANISM"].preserve_rerouted_impacts
        ),
        "counter_evidence_not_preserved_count": int(
            not by_failure["COUNTER_ONLY"].preserve_counter_evidence
        ),
        "provider_failure_not_pending_count": int(
            by_failure["PROVIDER_FAILED"].terminal_status_if_unresolved
            != "PROVIDER_PENDING"
        ),
        "budget_exhaustion_not_pending_count": int(
            by_failure["BUDGET_EXHAUSTED"].terminal_status_if_unresolved
            != "BUDGET_PENDING"
        ),
        "gold_payload_exposed_count": int(
            bool(
                by_failure["GOLD_MATERIAL_FACT_MISSED"].score_gap_context[
                    "preserved_evidence_ids"
                ]
            )
        ),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_adaptive_research_repair_audit_v1",
        "status": (
            "ADAPTIVE_RESEARCH_REPAIR_PASS"
            if critical_sum == 0
            else "ADAPTIVE_RESEARCH_REPAIR_FAIL"
        ),
        "failure_class_count": len(RESEARCH_REPAIR_FAILURE_CLASSES),
        "failure_classes": sorted(RESEARCH_REPAIR_FAILURE_CLASSES),
        "directives": [row.to_dict() for row in directives],
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }


def _assert_no_gold_payload(value: Any) -> None:
    if isinstance(value, Mapping):
        forbidden = {str(key).casefold() for key in value} & _FORBIDDEN_GOLD_KEYS
        if forbidden:
            raise ValueError("gold payload cannot enter production repair context")
        for item in value.values():
            _assert_no_gold_payload(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _assert_no_gold_payload(item)


__all__ = [
    "AdaptiveResearchRepairDirective",
    "FAILURE_NEXT_ACTIONS",
    "RESEARCH_REPAIR_FAILURE_CLASSES",
    "canonical_research_failure_class",
    "compile_research_repair_directive",
    "audit_adaptive_repair_contract",
]
