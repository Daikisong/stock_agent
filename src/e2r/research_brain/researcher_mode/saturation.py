"""Independent provider-backed semantic research saturation contract."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_researcher import ComponentResearchResult, StructuredResearchProvider
from .red_team_researcher import RedTeamResearchResult
from .research_supervisor import ResearchSupervisorReview
from .schemas import CANONICAL_COMPONENT_ORDER, assert_blind_research_output, scrub_blind_research_payload
from .source_graph_explorer import validate_source_graph_checkpoint
from .prompt_projection import (
    project_research_epoch_checkpoint,
    project_source_graph_checkpoint,
    project_structured_result,
)


SATURATION_REVIEW_ROLES = (
    "RESEARCH_SUPERVISOR_A",
    "RESEARCH_SUPERVISOR_B",
    "INDEPENDENT_COMPLETENESS_REVIEWER",
)

GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY = "NOT_RUN_POST_RUN_ONLY"


@dataclass(frozen=True)
class SaturationReview:
    review_id: str
    reviewer_role: str
    approve: bool
    seven_component_memos_complete: bool
    material_positive_routes_reviewed: bool
    counter_and_supersession_routes_checked: bool
    structured_data_complete: bool
    new_source_family_directions_reviewed: bool
    unresolved_material_questions: tuple[str, ...]
    rationale: str
    gold_evaluation_status: str = GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
    gold_critical_fact_miss_count: int | None = None
    no_reasonable_positive_route_remaining: bool = True
    checkpoint_id: str | None = None
    epoch: int | None = None
    provider_name: str = "TEST_OR_LEGACY_REVIEW"
    prompt_hash: str | None = None
    provider_backed: bool = False
    fixed_round_completion_used: bool = False
    zero_search_result_treated_as_saturation: bool = False
    transport_budget_treated_as_saturation: bool = False
    schema_version: str = "e2r_semantic_saturation_review_v3"

    def __post_init__(self) -> None:
        if self.reviewer_role not in SATURATION_REVIEW_ROLES:
            raise ValueError("unknown saturation reviewer role")
        if self.gold_evaluation_status != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY:
            raise ValueError("production saturation review cannot contain Gold outcome")
        if self.gold_critical_fact_miss_count is not None:
            raise ValueError("production saturation review cannot contain Gold miss count")
        if not self.rationale.strip():
            raise ValueError("saturation review rationale is required")
        if self.epoch is not None and self.epoch < 0:
            raise ValueError("saturation review epoch cannot be negative")
        if (
            self.fixed_round_completion_used
            or self.zero_search_result_treated_as_saturation
            or self.transport_budget_treated_as_saturation
        ):
            raise ValueError("transport or fixed-round outcomes cannot prove saturation")
        if self.provider_backed and (not self.provider_name or not self.prompt_hash):
            raise ValueError("provider-backed saturation review requires lineage")
        criteria = (
            self.seven_component_memos_complete,
            self.material_positive_routes_reviewed,
            self.counter_and_supersession_routes_checked,
            self.structured_data_complete,
            self.new_source_family_directions_reviewed,
            self.no_reasonable_positive_route_remaining,
            not self.unresolved_material_questions,
        )
        if self.approve and not all(criteria):
            raise ValueError("saturation approval requires every semantic criterion")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SaturationReviewerResult:
    reviewer_role: str
    status: str
    review: SaturationReview | None
    pending_reasons: tuple[str, ...]
    provider_name: str
    prompt_hash: str | None = None

    def __post_init__(self) -> None:
        if self.reviewer_role not in SATURATION_REVIEW_ROLES:
            raise ValueError("unknown saturation reviewer role")
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown saturation reviewer result status")
        if self.status == "COMPLETE" and self.review is None:
            raise ValueError("complete saturation result requires a review")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending saturation result requires reasons")
        if self.review is not None and self.review.reviewer_role != self.reviewer_role:
            raise ValueError("saturation result/review role mismatch")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "reviewer_role": self.reviewer_role,
            "status": self.status,
            "review": self.review.to_dict() if self.review else None,
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
            "prompt_hash": self.prompt_hash,
        }


@dataclass(frozen=True)
class SemanticSaturationCertificate:
    certificate_id: str
    status: str
    review_ids: tuple[str, ...]
    pending_reasons: tuple[str, ...]
    semantic_saturation_certified: bool
    fixed_round_completion_used: bool = False
    zero_search_result_treated_as_saturation: bool = False
    transport_budget_treated_as_saturation: bool = False
    checkpoint_id: str | None = None
    reviewer_roles: tuple[str, ...] = ()
    provider_prompt_hashes: tuple[str, ...] = ()
    provider_backed_reviews_required: bool = False
    gold_evaluation_status: str = GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
    gold_critical_fact_miss_count: int | None = None
    schema_version: str = "e2r_semantic_saturation_certificate_v3"

    def __post_init__(self) -> None:
        if self.status not in {"CERTIFIED", "PENDING"}:
            raise ValueError("unknown saturation certificate status")
        if self.gold_evaluation_status != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY:
            raise ValueError("production saturation certificate cannot contain Gold outcome")
        if self.gold_critical_fact_miss_count is not None:
            raise ValueError("production saturation certificate cannot contain Gold miss count")
        if (
            self.fixed_round_completion_used
            or self.zero_search_result_treated_as_saturation
            or self.transport_budget_treated_as_saturation
        ):
            raise ValueError("transport outcomes cannot certify semantic saturation")
        if (self.status == "CERTIFIED") != self.semantic_saturation_certified:
            raise ValueError("certificate status and semantic flag disagree")
        if self.status == "CERTIFIED" and self.pending_reasons:
            raise ValueError("certified saturation cannot have pending reasons")
        if self.semantic_saturation_certified and set(self.reviewer_roles) != set(
            SATURATION_REVIEW_ROLES
        ):
            raise ValueError("certificate requires all independent reviewer roles")
        if self.semantic_saturation_certified and (
            len(self.review_ids) != len(SATURATION_REVIEW_ROLES)
            or len(self.review_ids) != len(set(self.review_ids))
        ):
            raise ValueError("certificate requires unique review lineage")
        if self.semantic_saturation_certified and self.provider_backed_reviews_required and (
            not self.checkpoint_id
            or len(self.provider_prompt_hashes) != len(SATURATION_REVIEW_ROLES)
            or len(self.provider_prompt_hashes)
            != len(set(self.provider_prompt_hashes))
        ):
            raise ValueError("provider-backed certificate requires unique prompt lineage")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


class SemanticSaturationReviewer:
    """Run one independent semantic sufficiency review through the LLM provider."""

    def __init__(
        self,
        *,
        reviewer_role: str,
        provider: StructuredResearchProvider,
    ) -> None:
        if reviewer_role not in SATURATION_REVIEW_ROLES:
            raise ValueError("unknown saturation reviewer role")
        self.reviewer_role = reviewer_role
        self.provider = provider

    def review(
        self,
        *,
        checkpoint: Mapping[str, Any],
        supervisor_review: ResearchSupervisorReview,
        component_results: Sequence[ComponentResearchResult],
        red_team_result: RedTeamResearchResult | None,
        structured_result: Any | None,
        source_graph_checkpoint: Mapping[str, Any],
    ) -> SaturationReviewerResult:
        provider_name = str(
            getattr(self.provider, "provider_name", type(self.provider).__name__)
        )
        if not supervisor_review.ready_for_independent_saturation_review:
            return SaturationReviewerResult(
                reviewer_role=self.reviewer_role,
                status="PENDING",
                review=None,
                pending_reasons=("SUPERVISOR_NOT_READY_FOR_SATURATION_REVIEW",),
                provider_name=provider_name,
            )
        validate_source_graph_checkpoint(
            source_graph_checkpoint,
            target_id=str(checkpoint.get("target_id") or ""),
            as_of_date=str(checkpoint.get("as_of_date") or ""),
        )
        payload = scrub_blind_research_payload(
            {
                "reviewer_role": self.reviewer_role,
                "research_epoch_checkpoint": project_research_epoch_checkpoint(
                    checkpoint
                ),
                "supervisor_review": supervisor_review.to_dict(),
                "component_results": [row.to_dict() for row in component_results],
                "red_team_result": (
                    red_team_result.to_dict() if red_team_result else None
                ),
                "structured_result": (
                    project_structured_result(structured_result)
                ),
                "source_graph_checkpoint": _saturation_source_graph_payload(
                    source_graph_checkpoint
                ),
            }
        )
        try:
            response = self.provider.complete(
                pass_name="SEMANTIC_SATURATION_REVIEW", payload=payload
            )
            assert_blind_research_output(response)
            prompt_hash = _provider_prompt_hash(self.provider, payload)
            review = _review_from_response(
                response=response,
                reviewer_role=self.reviewer_role,
                checkpoint=checkpoint,
                supervisor_review=supervisor_review,
                component_results=component_results,
                red_team_result=red_team_result,
                structured_result=structured_result,
                source_graph_checkpoint=source_graph_checkpoint,
                provider_name=provider_name,
                prompt_hash=prompt_hash,
            )
            return SaturationReviewerResult(
                reviewer_role=self.reviewer_role,
                status="COMPLETE",
                review=review,
                pending_reasons=(),
                provider_name=provider_name,
                prompt_hash=prompt_hash,
            )
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
            KeyError,
            TypeError,
            ValueError,
        ) as exc:
            return SaturationReviewerResult(
                reviewer_role=self.reviewer_role,
                status="PENDING",
                review=None,
                pending_reasons=(
                    f"SATURATION_PROVIDER_OR_OUTPUT_ERROR:{type(exc).__name__}:{exc}",
                ),
                provider_name=provider_name,
                prompt_hash=_provider_prompt_hash(self.provider, payload),
            )


class SemanticSaturationCertifier:
    def certify(
        self,
        reviews: Sequence[SaturationReview],
        *,
        expected_checkpoint_id: str | None = None,
        require_provider_reviews: bool = False,
    ) -> SemanticSaturationCertificate:
        roles = [row.reviewer_role for row in reviews]
        reasons = []
        if len(roles) != len(set(roles)):
            reasons.append("DUPLICATE_SATURATION_REVIEW_ROLE")
        missing = set(SATURATION_REVIEW_ROLES) - set(roles)
        if missing:
            reasons.append("MISSING_REVIEW_ROLES:" + ",".join(sorted(missing)))
        review_ids = [row.review_id for row in reviews]
        if len(review_ids) != len(set(review_ids)):
            reasons.append("DUPLICATE_SATURATION_REVIEW_ID")
        prompt_hashes = [row.prompt_hash for row in reviews if row.prompt_hash]
        if require_provider_reviews:
            if not expected_checkpoint_id:
                reasons.append("MISSING_EXPECTED_CHECKPOINT_ID")
            if any(not row.provider_backed or not row.prompt_hash for row in reviews):
                reasons.append("NON_PROVIDER_BACKED_SATURATION_REVIEW")
            if len(prompt_hashes) != len(set(prompt_hashes)):
                reasons.append("DUPLICATE_SATURATION_PROMPT_HASH")
            epochs = {row.epoch for row in reviews}
            if len(epochs) != 1 or None in epochs:
                reasons.append("SATURATION_REVIEW_EPOCH_MISMATCH")
        if expected_checkpoint_id is not None and any(
            row.checkpoint_id != expected_checkpoint_id for row in reviews
        ):
            reasons.append("SATURATION_REVIEW_CHECKPOINT_MISMATCH")
        for row in reviews:
            if not row.approve:
                reasons.append(f"{row.reviewer_role}:NOT_APPROVED")
            if not row.no_reasonable_positive_route_remaining:
                reasons.append(
                    f"{row.reviewer_role}:REASONABLE_POSITIVE_ROUTE_REMAINS"
                )
            reasons.extend(
                f"{row.reviewer_role}:{question}"
                for question in row.unresolved_material_questions
            )
            if (
                row.gold_evaluation_status
                != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
                or row.gold_critical_fact_miss_count is not None
            ):
                reasons.append(f"{row.reviewer_role}:PRODUCTION_GOLD_OUTCOME_PRESENT")
        certified = not reasons and set(roles) == set(SATURATION_REVIEW_ROLES)
        payload = {
            "review_ids": sorted(review_ids),
            "reviewer_roles": sorted(roles),
            "checkpoint_id": expected_checkpoint_id,
            "certified": certified,
            "pending_reasons": reasons,
            "prompt_hashes": sorted(prompt_hashes),
            "gold_evaluation_status": GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
        }
        return SemanticSaturationCertificate(
            certificate_id=stable_intelligence_id("SATCERT", payload),
            status="CERTIFIED" if certified else "PENDING",
            review_ids=tuple(sorted(review_ids)),
            pending_reasons=tuple(dict.fromkeys(reasons)),
            semantic_saturation_certified=certified,
            checkpoint_id=expected_checkpoint_id,
            reviewer_roles=tuple(sorted(set(roles))),
            provider_prompt_hashes=tuple(sorted(prompt_hashes)),
            provider_backed_reviews_required=require_provider_reviews,
        )


def _review_from_response(
    *,
    response: Mapping[str, Any],
    reviewer_role: str,
    checkpoint: Mapping[str, Any],
    supervisor_review: ResearchSupervisorReview,
    component_results: Sequence[ComponentResearchResult],
    red_team_result: RedTeamResearchResult | None,
    structured_result: Any | None,
    source_graph_checkpoint: Mapping[str, Any],
    provider_name: str,
    prompt_hash: str,
) -> SaturationReview:
    if (
        checkpoint.get("gold_evaluation_status")
        != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
        or checkpoint.get("gold_critical_fact_miss_count") is not None
    ):
        raise ValueError("production checkpoint cannot expose a Gold outcome")
    unresolved = _string_tuple(response.get("unresolved_material_questions"))
    seven_complete = _required_bool(response, "seven_component_memos_complete")
    positive_reviewed = _required_bool(
        response, "material_positive_routes_reviewed"
    )
    counter_checked = _required_bool(
        response, "counter_and_supersession_routes_checked"
    )
    structured_complete = _required_bool(response, "structured_data_complete")
    source_directions_reviewed = _required_bool(
        response, "new_source_family_directions_reviewed"
    )
    reasonable_routes = _required_bool(
        response, "reasonable_positive_routes_remaining"
    )
    approve = _required_bool(response, "approve")
    actual_seven_complete = bool(
        len(component_results) == len(CANONICAL_COMPONENT_ORDER)
        and set(row.component_id for row in component_results)
        == set(CANONICAL_COMPONENT_ORDER)
        and all(row.status == "COMPLETE" for row in component_results)
    )
    actual_counter = bool(
        supervisor_review.counter_and_supersession_checked
        and red_team_result
        and red_team_result.status == "COMPLETE"
        and red_team_result.memo
        and set(red_team_result.memo.reviewed_component_ids)
        == set(CANONICAL_COMPONENT_ORDER)
        and red_team_result.memo.review_complete
    )
    actual_structured = _structured_data_complete(structured_result)
    if seven_complete != actual_seven_complete:
        raise ValueError("saturation component completeness contradicts current memos")
    if counter_checked != actual_counter:
        raise ValueError("saturation counter status lacks current proof")
    if structured_complete != actual_structured:
        raise ValueError("saturation structured-data status contradicts current records")
    if positive_reviewed and not supervisor_review.component_memos_sufficient:
        raise ValueError("positive-route review lacks sufficient component memos")
    if source_directions_reviewed and (
        supervisor_review.new_source_family_directions
        or supervisor_review.query_direction_briefs
    ):
        raise ValueError("unexecuted supervisor directions remain")
    if not _source_graph_allows_saturation(
        source_graph_checkpoint,
        research_checkpoint=checkpoint,
    ):
        raise ValueError("Source Graph is pending or supported only by zero results")
    deterministic_approve = bool(
        supervisor_review.ready_for_independent_saturation_review
        and actual_seven_complete
        and positive_reviewed
        and actual_counter
        and actual_structured
        and source_directions_reviewed
        and not reasonable_routes
        and not unresolved
    )
    if approve != deterministic_approve:
        raise ValueError("saturation approval contradicts semantic gates")
    checkpoint_id = str(checkpoint.get("checkpoint_id") or "")
    if not checkpoint_id:
        raise ValueError("saturation review requires a checkpoint id")
    epoch = int(checkpoint.get("epoch") or 0)
    identity = {
        "reviewer_role": reviewer_role,
        "checkpoint_id": checkpoint_id,
        "epoch": epoch,
        "response": dict(response),
        "prompt_hash": prompt_hash,
    }
    return SaturationReview(
        review_id=stable_intelligence_id("SATREVIEW", identity),
        reviewer_role=reviewer_role,
        approve=approve,
        seven_component_memos_complete=seven_complete,
        material_positive_routes_reviewed=positive_reviewed,
        counter_and_supersession_routes_checked=counter_checked,
        structured_data_complete=structured_complete,
        new_source_family_directions_reviewed=source_directions_reviewed,
        unresolved_material_questions=unresolved,
        rationale=str(response["rationale"]),
        no_reasonable_positive_route_remaining=not reasonable_routes,
        checkpoint_id=checkpoint_id,
        epoch=epoch,
        provider_name=provider_name,
        prompt_hash=prompt_hash,
        provider_backed=True,
    )


def _saturation_source_graph_payload(
    checkpoint: Mapping[str, Any],
) -> Mapping[str, Any]:
    return project_source_graph_checkpoint(
        checkpoint,
        keys=(
            "checkpoint_id",
            "epoch",
            "generated_queries",
            "query_failures",
            "fetch_records",
            "evidence_documents",
            "rejected_documents",
            "resolved_objective_ids",
            "transport_budget_can_complete_research",
            "semantic_saturation_certified",
        ),
    )


def _string_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, (list, tuple)):
        raise TypeError("expected an array of strings")
    rows = tuple(str(row).strip() for row in value)
    if any(not row for row in rows) or len(rows) != len(set(rows)):
        raise ValueError("string array must contain unique non-empty values")
    return rows


def _required_bool(row: Mapping[str, Any], key: str) -> bool:
    value = row[key]
    if type(value) is not bool:
        raise TypeError(f"{key} must be a boolean")
    return value


def _source_graph_allows_saturation(
    checkpoint: Mapping[str, Any],
    *,
    research_checkpoint: Mapping[str, Any],
) -> bool:
    if bool(checkpoint.get("transport_budget_can_complete_research")):
        return False
    if str(checkpoint.get("status") or "") not in {
        "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
        "STOPPED_ON_RESOLUTION",
    }:
        return False
    if str(research_checkpoint.get("source_graph_checkpoint_id") or "") != str(
        checkpoint.get("checkpoint_id") or ""
    ):
        return False
    executed = tuple(
        row
        for row in checkpoint.get("generated_queries") or ()
        if str(row.get("execution_status") or "")
        not in {"", "PENDING", "BLOCKED_OFFICIAL_FIRST"}
    )
    zero_result_only = bool(
        executed
        and not (checkpoint.get("evidence_documents") or ())
        and all(str(row.get("execution_status")) == "NO_RESULT" for row in executed)
    )
    return not zero_result_only


def _structured_data_complete(result: Any | None) -> bool:
    if result is None or getattr(result, "status", None) != "COMPLETE":
        return False
    records = getattr(result, "records", None)
    if not records:
        return False
    missing = getattr(result, "missing_roles_by_component", {}) or {}
    return not any(missing.values())


def _provider_prompt_hash(
    provider: StructuredResearchProvider, payload: Mapping[str, Any]
) -> str:
    calls = getattr(provider, "calls", None)
    if isinstance(calls, list) and calls:
        value = calls[-1].get("prompt_hash")
        if value:
            return str(value)
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


__all__ = [
    "GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY",
    "SATURATION_REVIEW_ROLES",
    "SaturationReview",
    "SaturationReviewerResult",
    "SemanticSaturationCertificate",
    "SemanticSaturationCertifier",
    "SemanticSaturationReviewer",
]
