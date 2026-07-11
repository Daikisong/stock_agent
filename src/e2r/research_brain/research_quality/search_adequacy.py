"""Question별 검색 route와 full-document 포화도를 판정한다."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash
from e2r.research_brain.scoring.question_impact_contract import (
    QuestionImpactContract,
)


SATURATION_STATUSES = {
    "EVIDENCE_FOUND",
    "ADEQUATE_ABSENCE",
    "SOURCE_PENDING",
    "PROVIDER_PENDING",
    "BUDGET_PENDING",
    "INADEQUATE_SEARCH",
}
ROUTE_CATEGORIES = {
    "OFFICIAL",
    "ISSUER_IR",
    "FINANCIAL_REVISION",
    "INDEPENDENT",
    "COUNTER",
    "SUPERSESSION",
}
PROVIDER_FAILURE_CLASSES = {
    "PROVIDER_FAILED",
    "AUTH_FAILED",
    "RATE_LIMITED",
}


@dataclass(frozen=True)
class EvidenceSearchAdequacy:
    adequacy_id: str
    target_id: str
    question_family_id: str
    official_route_attempted: bool
    issuer_ir_route_attempted: bool
    financial_revision_route_attempted: bool
    independent_source_route_attempted: bool
    counter_route_attempted: bool
    supersession_route_attempted: bool
    query_novelty_count: int
    full_document_count: int
    relevant_document_count: int
    wrong_scope_document_count: int
    provider_failures: int
    budget_exhausted: bool
    saturation_status: str
    required_route_categories: tuple[str, ...]
    attempted_route_categories: tuple[str, ...]
    unavailable_route_categories: tuple[str, ...]
    pending_route_categories: tuple[str, ...]
    missing_route_categories: tuple[str, ...]
    source_task_ids: tuple[str, ...]
    search_proof_ids: tuple[str, ...]
    relevant_document_ids: tuple[str, ...]
    positive_claim_ids: tuple[str, ...]
    supported_question: bool
    observed_question_status: str
    positive_proposal_zeroed_by_internal_validation_count: int
    gold_material_fact_miss_count: int
    adequate_absence_allowed: bool
    blocking_reasons: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.saturation_status not in SATURATION_STATUSES:
            raise ValueError("unknown evidence saturation status")

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


def compile_dossier_search_adequacy(
    *,
    question_tasks: Sequence[Mapping[str, Any]],
    executed_tasks: Sequence[Mapping[str, Any]],
    provider_requests: Sequence[Mapping[str, Any]],
    provider_fetch_results: Sequence[Mapping[str, Any]],
    web_search_tasks: Sequence[Mapping[str, Any]],
    documents: Sequence[Mapping[str, Any]],
    claims: Sequence[Mapping[str, Any]],
    primitive_mappings: Sequence[Mapping[str, Any]],
    question_closures: Sequence[Mapping[str, Any]],
    question_contracts: Mapping[str, QuestionImpactContract],
    claim_eligibility_decisions: Sequence[Mapping[str, Any]] = (),
    proposed_impacts: Sequence[Mapping[str, Any]] = (),
    validated_impacts: Sequence[Mapping[str, Any]] = (),
    material_fact_comparisons: Sequence[Mapping[str, Any]] = (),
) -> tuple[EvidenceSearchAdequacy, ...]:
    closure_by_family = {
        str(row.get("question_family_id") or ""): row
        for row in question_closures
    }
    decision_by_claim = {
        str(row.get("claim_id") or ""): row
        for row in claim_eligibility_decisions
    }
    mappings_by_claim: dict[str, list[Mapping[str, Any]]] = {}
    for row in primitive_mappings:
        if row.get("accepted_by_evidence_os") is True:
            mappings_by_claim.setdefault(
                str(row.get("claim_id") or ""), []
            ).append(row)
    validated_ids = {
        str(row.get("impact_id") or "")
        for row in validated_impacts
        if float(row.get("validated_credit_fraction") or 0) > 0
    }
    results = []
    for question in question_tasks:
        family = str(question.get("question_family_id") or "")
        target_id = str(question.get("target_id") or "")
        question_text = str(question.get("question_to_answer") or "")
        matching_tasks = tuple(
            row
            for row in executed_tasks
            if str(row.get("target_id") or "") == target_id
            and (
                str(row.get("question_family_id") or "") == family
                or str(row.get("question_to_answer") or "") == question_text
            )
        )
        task_ids = {
            str(row.get("task_id") or "")
            for row in matching_tasks
            if row.get("task_id")
        }
        requests = tuple(
            row
            for row in provider_requests
            if str(row.get("source_task_id") or "") in task_ids
        )
        fetches = tuple(
            row
            for row in provider_fetch_results
            if str(row.get("source_task_id") or "") in task_ids
        )
        web = tuple(
            row
            for row in web_search_tasks
            if str(row.get("source_task_id") or "") in task_ids
        )
        required = _required_routes(
            question=question,
            contract=question_contracts.get(family),
        )
        attempted, unavailable, pending_routes, route_proofs = _route_evidence(
            matching_tasks=matching_tasks,
            requests=requests,
            fetches=fetches,
            web=web,
        )
        queries = {
            _normalize_query(value)
            for row in matching_tasks
            for value in (row.get("query_intent") or {}).get(
                "literal_queries", ()
            )
            if _normalize_query(value)
        }
        queries.update(
            _normalize_query(row.get("query"))
            for row in web
            if _normalize_query(row.get("query"))
        )
        matching_documents = tuple(
            row
            for row in documents
            if task_ids.intersection(
                str(value) for value in row.get("source_task_ids") or ()
            )
        )
        selected, rejected = select_research_grade_documents(
            candidates=matching_documents,
            question_family_id=family,
            as_of_date=str(question.get("as_of_date") or "9999-12-31"),
            mechanism_scope=(
                question_contracts[family].mechanism_scope
                if family in question_contracts
                else ""
            ),
        )
        contract = question_contracts.get(family)
        positive_claim_ids = []
        for claim in claims:
            claim_id = str(claim.get("claim_id") or "")
            if claim.get("accepted") is not True:
                continue
            if contract is not None and not any(
                str(mapping.get("primitive_id") or "")
                in contract.allowed_primitive_ids
                for mapping in mappings_by_claim.get(claim_id, ())
            ):
                continue
            decision = decision_by_claim.get(claim_id)
            if decision is not None and decision.get(
                "component_scoring_eligibility"
            ) is not True:
                continue
            if decision is None and claim_eligibility_decisions:
                continue
            positive_claim_ids.append(claim_id)
        closure = closure_by_family.get(family, {})
        supported = str(closure.get("status") or "") in {
            "SUPPORTED",
            "PARTIALLY_SUPPORTED",
            "SUPPORTED_SCORING",
            "PARTIALLY_SUPPORTED_SCORING",
            "COUNTER_SUPPORTED",
        }
        proposed_for_question = tuple(
            row
            for row in proposed_impacts
            if str(row.get("claim_id") or "") in positive_claim_ids
            and str(row.get("direction") or "").upper()
            in {"SUPPORT", "RESOLUTION"}
        )
        zeroed_internal = sum(
            str(row.get("impact_id") or "") not in validated_ids
            or float(
                next(
                    (
                        item.get("validated_credit_fraction") or 0
                        for item in validated_impacts
                        if item.get("impact_id") == row.get("impact_id")
                    ),
                    0,
                )
            )
            <= 0
            for row in proposed_for_question
        )
        gold_misses = sum(
            str(row.get("target_id") or "") == target_id
            and str(row.get("question_family_id") or "") == family
            and row.get("materiality") == "CRITICAL"
            and not _comparison_qualified(row)
            for row in material_fact_comparisons
        )
        provider_failures = sum(
            str(row.get("acquisition_class") or "")
            in PROVIDER_FAILURE_CLASSES
            or bool(row.get("provider_error"))
            for row in fetches
        ) + sum(
            bool(row.get("search_error")) or bool(row.get("provider_errors"))
            for row in web
        )
        budget_exhausted = any(
            str(row.get("acquisition_class") or "") == "BUDGET_EXHAUSTED"
            or row.get("budget_exhausted") is True
            for row in (*fetches, *web)
        )
        missing = tuple(sorted(required - attempted - unavailable))
        proof_ids = tuple(
            dict.fromkeys(
                (
                    *route_proofs,
                    *(
                        str(row.get("web_task_id") or "")
                        for row in web
                        if row.get("web_task_id")
                    ),
                )
            )
        )
        saturation, blockers = _saturation(
            has_evidence=bool(positive_claim_ids or supported),
            provider_failures=provider_failures,
            budget_exhausted=budget_exhausted,
            missing_routes=missing,
            query_novelty_count=len(queries),
            zeroed_internal=zeroed_internal,
            gold_misses=gold_misses,
            search_proof_count=len(proof_ids),
            source_pending=bool(pending_routes),
        )
        payload = {
            "target_id": target_id,
            "question_family_id": family,
            "official_route_attempted": "OFFICIAL" in attempted,
            "issuer_ir_route_attempted": "ISSUER_IR" in attempted,
            "financial_revision_route_attempted": (
                "FINANCIAL_REVISION" in attempted
            ),
            "independent_source_route_attempted": "INDEPENDENT" in attempted,
            "counter_route_attempted": "COUNTER" in attempted,
            "supersession_route_attempted": "SUPERSESSION" in attempted,
            "query_novelty_count": len(queries),
            "full_document_count": len(selected),
            "relevant_document_count": len(selected),
            "wrong_scope_document_count": sum(
                row["reason"] == "WRONG_MECHANISM_SCOPE" for row in rejected
            ),
            "provider_failures": provider_failures,
            "budget_exhausted": budget_exhausted,
            "saturation_status": saturation,
            "required_route_categories": tuple(sorted(required)),
            "attempted_route_categories": tuple(sorted(attempted)),
            "unavailable_route_categories": tuple(sorted(unavailable)),
            "pending_route_categories": tuple(sorted(pending_routes)),
            "missing_route_categories": missing,
            "source_task_ids": tuple(sorted(task_ids)),
            "search_proof_ids": proof_ids,
            "relevant_document_ids": tuple(
                str(row.get("document_id") or "") for row in selected
            ),
            "positive_claim_ids": tuple(dict.fromkeys(positive_claim_ids)),
            "supported_question": supported,
            "observed_question_status": str(closure.get("status") or ""),
            "positive_proposal_zeroed_by_internal_validation_count": zeroed_internal,
            "gold_material_fact_miss_count": gold_misses,
            "adequate_absence_allowed": saturation == "ADEQUATE_ABSENCE",
            "blocking_reasons": blockers,
        }
        results.append(
            EvidenceSearchAdequacy(
                adequacy_id="ADEQ-" + stable_hash(payload)[:24],
                **payload,
            )
        )
    return tuple(results)


def select_research_grade_documents(
    *,
    candidates: Sequence[Mapping[str, Any]],
    question_family_id: str,
    as_of_date: str,
    mechanism_scope: str,
) -> tuple[tuple[Mapping[str, Any], ...], tuple[Mapping[str, Any], ...]]:
    """Title token이 아니라 task lineage·scope·full text로 문서를 고른다."""

    date.fromisoformat(as_of_date)
    selected = []
    rejected = []
    for row in candidates:
        reason = ""
        published = str(row.get("published_at") or row.get("published_date") or "")
        question_ids = {
            str(value) for value in row.get("question_family_ids") or ()
        }
        scopes = {
            str(value).casefold()
            for value in row.get("mechanism_scopes") or ()
        }
        if row.get("snippet_only") is True or row.get(
            "search_snippet_used_as_evidence"
        ) is True:
            reason = "SNIPPET_ONLY_DISCOVERY"
        elif not str(row.get("content_text") or "").strip():
            reason = "FULL_DOCUMENT_MISSING"
        elif published and published[:10] > as_of_date:
            reason = "FUTURE_DOCUMENT"
        elif question_ids and question_family_id not in question_ids:
            reason = "WRONG_QUESTION_PREDICATE"
        elif scopes and mechanism_scope.casefold() not in scopes:
            reason = "WRONG_MECHANISM_SCOPE"
        elif str(row.get("document_format") or "").upper() == "PDF" and not _pdf_anchor_complete(row):
            reason = "PDF_ANCHOR_INCOMPLETE"
        if reason:
            rejected.append(
                {
                    "document_id": row.get("document_id"),
                    "reason": reason,
                }
            )
        else:
            selected.append(row)
    selected.sort(
        key=lambda row: (
            _source_quality(row),
            int(bool(row.get("counter_relevance"))),
            str(row.get("published_at") or row.get("published_date") or ""),
            str(row.get("document_id") or ""),
        ),
        reverse=True,
    )
    return tuple(selected), tuple(rejected)


def audit_search_adequacy(
    rows: Sequence[EvidenceSearchAdequacy],
) -> Mapping[str, Any]:
    critical = {
        "inadequate_absence_count": sum(
            row.adequate_absence_allowed
            and (
                row.provider_failures > 0
                or row.budget_exhausted
                or bool(row.missing_route_categories)
                or bool(row.positive_claim_ids)
                or row.supported_question
                or row.positive_proposal_zeroed_by_internal_validation_count > 0
                or row.gold_material_fact_miss_count > 0
            )
            for row in rows
        ),
        "provider_failure_marked_absent_count": sum(
            row.provider_failures > 0 and row.adequate_absence_allowed
            for row in rows
        ),
        "budget_exhaustion_marked_absent_count": sum(
            row.budget_exhausted and row.adequate_absence_allowed
            for row in rows
        ),
        "positive_evidence_marked_absent_count": sum(
            bool(row.positive_claim_ids) and row.adequate_absence_allowed
            for row in rows
        ),
        "gold_miss_marked_absent_count": sum(
            row.gold_material_fact_miss_count > 0
            and row.adequate_absence_allowed
            for row in rows
        ),
        "inadequate_question_closure_absence_count": sum(
            row.observed_question_status == "EVALUATED_ABSENT"
            and not row.adequate_absence_allowed
            for row in rows
        ),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_evidence_search_adequacy_audit_v1",
        "status": (
            "EVIDENCE_SEARCH_ADEQUACY_PASS"
            if critical_sum == 0
            else "EVIDENCE_SEARCH_ADEQUACY_FAIL"
        ),
        "question_count": len(rows),
        "saturation_counts": {
            status: sum(row.saturation_status == status for row in rows)
            for status in sorted(SATURATION_STATUSES)
        },
        "rows": [row.to_dict() for row in rows],
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }


def _required_routes(
    *,
    question: Mapping[str, Any],
    contract: QuestionImpactContract | None,
) -> set[str]:
    explicit = {
        str(value).upper()
        for value in question.get("required_route_categories") or ()
    }
    if explicit:
        unknown = explicit - ROUTE_CATEGORIES
        if unknown:
            raise ValueError(f"unknown required route categories: {sorted(unknown)}")
        return explicit
    result = {"COUNTER", "SUPERSESSION"}
    if contract is None:
        return result | {"OFFICIAL", "ISSUER_IR", "INDEPENDENT"}
    for route in contract.required_source_routes:
        result.add(_contract_route_category(route))
    return result


def _route_evidence(
    *,
    matching_tasks: Sequence[Mapping[str, Any]],
    requests: Sequence[Mapping[str, Any]],
    fetches: Sequence[Mapping[str, Any]],
    web: Sequence[Mapping[str, Any]],
) -> tuple[set[str], set[str], set[str], tuple[str, ...]]:
    attempted: set[str] = set()
    unavailable: set[str] = set()
    pending: set[str] = set()
    proof_ids = []
    for row in matching_tasks:
        for attempt in row.get("adequacy_route_attempts") or ():
            category = str(attempt.get("route_category") or "").upper()
            if category not in ROUTE_CATEGORIES:
                raise ValueError("unknown explicit adequacy route")
            status = str(attempt.get("status") or "").upper()
            if status == "ATTEMPTED":
                attempted.add(category)
            elif status == "UNAVAILABLE":
                unavailable.add(category)
            elif status == "PENDING":
                pending.add(category)
            else:
                continue
            if attempt.get("proof_id"):
                proof_ids.append(str(attempt["proof_id"]))
    for row in requests:
        category = _source_class_category(str(row.get("source_class") or ""))
        if category:
            attempted.add(category)
        if row.get("provider_request_record_id"):
            proof_ids.append(str(row["provider_request_record_id"]))
    for row in fetches:
        category = _source_class_category(str(row.get("source_class") or ""))
        if category and str(row.get("acquisition_class") or "") == "SOURCE_EXHAUSTED":
            unavailable.add(category)
        if row.get("provider_fetch_result_id"):
            proof_ids.append(str(row["provider_fetch_result_id"]))
        if category and str(row.get("acquisition_class") or "") in {
            "REJECTED_BY_POLICY",
            "PROVIDER_HEALTH_ONLY",
        }:
            pending.add(category)
    for row in web:
        if row.get("search_call_executed") is True:
            attempted.add("INDEPENDENT")
    return attempted, unavailable, pending, tuple(dict.fromkeys(proof_ids))


def _saturation(
    *,
    has_evidence: bool,
    provider_failures: int,
    budget_exhausted: bool,
    missing_routes: Sequence[str],
    query_novelty_count: int,
    zeroed_internal: int,
    gold_misses: int,
    search_proof_count: int,
    source_pending: bool,
) -> tuple[str, tuple[str, ...]]:
    blockers = []
    if provider_failures:
        blockers.append("PROVIDER_FAILURE_PRESENT")
    if budget_exhausted:
        blockers.append("BUDGET_EXHAUSTED")
    if missing_routes:
        blockers.append("REQUIRED_ROUTES_INCOMPLETE")
    if query_novelty_count <= 0:
        blockers.append("NO_NOVEL_QUERY")
    if zeroed_internal:
        blockers.append("POSITIVE_PROPOSAL_ZEROED_INTERNALLY")
    if gold_misses:
        blockers.append("GOLD_MATERIAL_FACT_MISSED")
    if search_proof_count <= 0:
        blockers.append("SEARCH_PROOF_MISSING")
    if source_pending:
        blockers.append("SOURCE_ROUTE_PENDING")
    if has_evidence:
        return "EVIDENCE_FOUND", tuple(blockers)
    if provider_failures:
        return "PROVIDER_PENDING", tuple(blockers)
    if budget_exhausted:
        return "BUDGET_PENDING", tuple(blockers)
    if source_pending:
        return "SOURCE_PENDING", tuple(blockers)
    if (
        gold_misses
        or missing_routes
        or query_novelty_count <= 0
        or zeroed_internal
        or search_proof_count <= 0
    ):
        return "INADEQUATE_SEARCH", tuple(blockers)
    return "ADEQUATE_ABSENCE", ()


def _contract_route_category(route: str) -> str:
    value = route.casefold()
    if value in {"official_filing"}:
        return "OFFICIAL"
    if value in {"issuer_ir", "issuer_newsroom", "issuer_earnings", "issuer_guidance"}:
        return "ISSUER_IR"
    if value in {"financial_revision"}:
        return "FINANCIAL_REVISION"
    if value in {"customer_official", "trusted_independent"}:
        return "INDEPENDENT"
    raise ValueError(f"question contract has unknown source route: {route}")


def _source_class_category(source_class: str) -> str | None:
    if source_class in {"DART", "KIND", "KRX", "SEC", "Regulator", "Official"}:
        return "OFFICIAL"
    if source_class in {"IssuerIR", "IssuerNewsroom", "CompanyEarningsCall", "IR"}:
        return "ISSUER_IR"
    if source_class == "CompanyGuide":
        return "FINANCIAL_REVISION"
    if source_class in {"CustomerOfficial", "CustomerNewsroom", "IndustryData"}:
        return "INDEPENDENT"
    return None


def _normalize_query(value: Any) -> str:
    return " ".join(str(value or "").casefold().split())


def _comparison_qualified(row: Mapping[str, Any]) -> bool:
    return all(
        row.get(field) is True
        for field in (
            "semantic_match",
            "source_quality_match",
            "currentness_match",
            "mechanism_scope_match",
        )
    )


def _pdf_anchor_complete(row: Mapping[str, Any]) -> bool:
    anchor = row.get("evidence_anchor") or {}
    has_location = bool(
        anchor.get("page_number")
        or anchor.get("section")
        or anchor.get("table_anchor")
    )
    table = row.get("table_extraction")
    if table is None:
        return has_location
    return has_location and all(
        str(table.get(field) or "").strip()
        for field in ("value", "unit", "period")
    )


def _source_quality(row: Mapping[str, Any]) -> int:
    value = str(row.get("source_tier") or row.get("source_class") or "")
    if value in {"REGULATORY_OFFICIAL", "ISSUER_OFFICIAL", "DART", "IssuerIR"}:
        return 4
    if value in {"CUSTOMER_OFFICIAL", "CustomerOfficial"}:
        return 3
    if value in {"TRUSTED_INDEPENDENT", "IndustryData", "CompanyGuide"}:
        return 2
    return 1


__all__ = [
    "EvidenceSearchAdequacy",
    "SATURATION_STATUSES",
    "audit_search_adequacy",
    "compile_dossier_search_adequacy",
    "select_research_grade_documents",
]
