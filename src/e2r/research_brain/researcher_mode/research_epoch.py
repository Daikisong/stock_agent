"""Checkpoint/resume orchestration for semantic Researcher Mode epochs."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .component_judge import SynthesisResult
from .component_researcher import ComponentResearchResult
from .red_team_researcher import RedTeamResearchResult
from .research_supervisor import (
    ResearchSupervisor,
    ResearchSupervisorReview,
    SupervisorComponentFinding,
    SupervisorFactGap,
    SupervisorFailureAssessment,
    SupervisorQueryDirection,
    SupervisorSourceDirection,
    _material_score_disagreement_component_ids,
)
from .saturation import (
    GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
    SATURATION_REVIEW_ROLES,
    SaturationReview,
    SaturationReviewerResult,
    SemanticSaturationCertificate,
    SemanticSaturationCertifier,
    SemanticSaturationReviewer,
)
from .schemas import CANONICAL_COMPONENT_ORDER, EvidenceFact
from .source_graph_explorer import validated_quarantined_document_ids


RESEARCH_EPOCH_OUTPUT_FILES: Mapping[str, str] = {
    "checkpoint": "research_epoch_checkpoint.json",
    "supervisor_review": "research_supervisor_review.json",
    "saturation_reviews": "semantic_saturation_reviews.jsonl",
    "saturation_certificate": "semantic_saturation_certificate.json",
}


@dataclass(frozen=True)
class ResearchEpochCheckpoint:
    checkpoint_id: str
    checkpoint_hash: str
    target_id: str
    as_of_date: str
    epoch: int
    status: str
    resumed_from_checkpoint_id: str | None
    source_graph_checkpoint_id: str | None
    queries: tuple[Mapping[str, Any], ...]
    documents: tuple[Mapping[str, Any], ...]
    new_facts: tuple[Mapping[str, Any], ...]
    retired_facts: tuple[Mapping[str, Any], ...]
    changed_component_memos: tuple[Mapping[str, Any], ...]
    unresolved_material_questions: tuple[str, ...]
    next_actions: tuple[str, ...]
    supervisor_review: Mapping[str, Any]
    saturation_reviews: tuple[Mapping[str, Any], ...]
    saturation_certificate: Mapping[str, Any] | None
    cumulative_query_ids: tuple[str, ...]
    cumulative_document_ids: tuple[str, ...]
    cumulative_fact_ids: tuple[str, ...]
    current_fact_ids: tuple[str, ...]
    retired_fact_ids: tuple[str, ...]
    component_memo_hashes: Mapping[str, str]
    semantic_saturation_certified: bool
    gold_evaluation_status: str = GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
    gold_critical_fact_miss_count: int | None = None
    completion_based_on_fixed_rounds: bool = False
    zero_search_result_treated_as_saturation: bool = False
    transport_budget_treated_as_completion: bool = False
    production_score_authority: bool = False
    schema_version: str = "e2r_research_epoch_checkpoint_v3"

    def __post_init__(self) -> None:
        if not self.target_id.strip():
            raise ValueError("research epoch target id is required")
        date.fromisoformat(self.as_of_date)
        if self.epoch <= 0:
            raise ValueError("research epoch must be positive")
        if self.epoch > 1 and not self.resumed_from_checkpoint_id:
            raise ValueError("resumed research epoch requires prior checkpoint lineage")
        if not self.source_graph_checkpoint_id:
            raise ValueError("research epoch requires Source Graph checkpoint lineage")
        if self.status not in {
            "NEXT_RESEARCH_REQUIRED",
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
            "SEMANTIC_SATURATION_CERTIFIED",
        }:
            raise ValueError("unknown research epoch status")
        if (
            self.completion_based_on_fixed_rounds
            or self.zero_search_result_treated_as_saturation
            or self.transport_budget_treated_as_completion
        ):
            raise ValueError("transport or fixed-round outcomes cannot complete research")
        if self.production_score_authority:
            raise ValueError("research checkpoint cannot assign production score")
        if self.gold_evaluation_status != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY:
            raise ValueError("production research epoch cannot contain Gold outcome")
        if self.schema_version == "e2r_research_epoch_checkpoint_v3":
            if self.gold_critical_fact_miss_count is not None:
                raise ValueError("production research epoch cannot contain Gold miss count")
        elif self.gold_critical_fact_miss_count is not None and (
            type(self.gold_critical_fact_miss_count) is not int
            or self.gold_critical_fact_miss_count < 0
        ):
            raise ValueError("legacy Gold field must be a nonnegative integer")
        if self.semantic_saturation_certified != (
            self.status == "SEMANTIC_SATURATION_CERTIFIED"
        ):
            raise ValueError("checkpoint saturation flag and status disagree")
        if self.semantic_saturation_certified and not self.saturation_certificate:
            raise ValueError("certified checkpoint requires a certificate")
        if self.saturation_certificate and bool(
            self.saturation_certificate.get("semantic_saturation_certified")
        ) != self.semantic_saturation_certified:
            raise ValueError("checkpoint and saturation certificate disagree")
        if self.semantic_saturation_certified:
            certificate = self.saturation_certificate or {}
            v3_gold_contract = (
                self.schema_version == "e2r_research_epoch_checkpoint_v3"
            )
            if (
                certificate.get("status") != "CERTIFIED"
                or certificate.get("checkpoint_id") != self.checkpoint_id
                or certificate.get("provider_backed_reviews_required") is not True
                or (
                    v3_gold_contract
                    and (
                        certificate.get("gold_evaluation_status")
                        != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
                        or certificate.get("gold_critical_fact_miss_count")
                        is not None
                    )
                )
            ):
                raise ValueError("certified checkpoint has invalid certificate lineage")
            results = tuple(self.saturation_reviews)
            roles = [str(row.get("reviewer_role") or "") for row in results]
            reviews = [row.get("review") for row in results]
            review_ids = [
                str(review.get("review_id") or "")
                for review in reviews
                if isinstance(review, Mapping)
            ]
            prompt_hashes = [
                str(review.get("prompt_hash") or "")
                for review in reviews
                if isinstance(review, Mapping)
            ]
            if (
                len(results) != len(SATURATION_REVIEW_ROLES)
                or set(roles) != set(SATURATION_REVIEW_ROLES)
                or any(row.get("status") != "COMPLETE" for row in results)
                or len(review_ids) != len(SATURATION_REVIEW_ROLES)
                or set(review_ids) != set(certificate.get("review_ids") or ())
                or len(prompt_hashes) != len(SATURATION_REVIEW_ROLES)
                or len(prompt_hashes) != len(set(prompt_hashes))
                or set(prompt_hashes)
                != set(certificate.get("provider_prompt_hashes") or ())
                or any(
                    not isinstance(review, Mapping)
                    or review.get("approve") is not True
                    or review.get("provider_backed") is not True
                    or review.get("checkpoint_id") != self.checkpoint_id
                    or (
                        v3_gold_contract
                        and (
                            review.get("gold_evaluation_status")
                            != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
                            or review.get("gold_critical_fact_miss_count")
                            is not None
                        )
                    )
                    or review.get("reviewer_role")
                    != results[index].get("reviewer_role")
                    for index, review in enumerate(reviews)
                )
            ):
                raise ValueError("certified checkpoint lacks three valid reviews")
        if len(self.cumulative_query_ids) != len(set(self.cumulative_query_ids)):
            raise ValueError("checkpoint query ids must be unique")
        if len(self.cumulative_document_ids) != len(set(self.cumulative_document_ids)):
            raise ValueError("checkpoint document ids must be unique")
        if len(self.cumulative_fact_ids) != len(set(self.cumulative_fact_ids)):
            raise ValueError("checkpoint fact ids must be unique")
        if len(self.current_fact_ids) != len(set(self.current_fact_ids)):
            raise ValueError("checkpoint current fact ids must be unique")
        if len(self.retired_fact_ids) != len(set(self.retired_fact_ids)):
            raise ValueError("checkpoint retired fact ids must be unique")
        if not set(self.current_fact_ids).issubset(self.cumulative_fact_ids):
            raise ValueError("current fact ids must belong to cumulative lineage")
        if not set(self.retired_fact_ids).issubset(self.cumulative_fact_ids):
            raise ValueError("retired fact ids must belong to cumulative lineage")
        if set(self.current_fact_ids) & set(self.retired_fact_ids):
            raise ValueError("current and retired fact ids must be disjoint")
        retired_delta_ids = [
            str(row.get("fact_id") or "") for row in self.retired_facts
        ]
        if (
            any(not value for value in retired_delta_ids)
            or len(retired_delta_ids) != len(set(retired_delta_ids))
            or not set(retired_delta_ids).issubset(self.retired_fact_ids)
        ):
            raise ValueError("retired fact delta requires explicit lineage")
        if self.checkpoint_hash != _research_checkpoint_hash(self.to_dict()):
            raise ValueError("research epoch checkpoint hash mismatch")
        if self.checkpoint_id != _research_checkpoint_id(self.to_dict()):
            raise ValueError("research epoch checkpoint id mismatch")

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))

    def to_score_gap_context(self) -> Mapping[str, Any]:
        return {
            "research_epoch_checkpoint_id": self.checkpoint_id,
            "epoch": self.epoch,
            "gold_evaluation_status": self.gold_evaluation_status,
            "unresolved_material_questions": list(
                self.unresolved_material_questions
            ),
            "next_actions": list(self.next_actions),
            "current_fact_ids": list(self.current_fact_ids),
            "retired_fact_ids": list(self.retired_fact_ids),
            "supervisor": dict(self.supervisor_review),
            "saturation_reviews": list(self.saturation_reviews),
            "saturation_certificate": (
                dict(self.saturation_certificate)
                if self.saturation_certificate
                else None
            ),
        }


@dataclass(frozen=True)
class ResearchEpochRun:
    checkpoint: ResearchEpochCheckpoint
    supervisor_review: ResearchSupervisorReview
    saturation_reviewer_results: tuple[SaturationReviewerResult, ...]
    saturation_certificate: SemanticSaturationCertificate | None

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "checkpoint": self.checkpoint.to_dict(),
            "supervisor_review": self.supervisor_review.to_dict(),
            "saturation_reviewer_results": [
                row.to_dict() for row in self.saturation_reviewer_results
            ],
            "saturation_certificate": (
                self.saturation_certificate.to_dict()
                if self.saturation_certificate
                else None
            ),
        }


class ResearchEpochRunner:
    """Run one resumable semantic epoch; there is deliberately no max_rounds."""

    def __init__(
        self,
        *,
        supervisor: ResearchSupervisor,
        saturation_reviewers: Sequence[SemanticSaturationReviewer] = (),
    ) -> None:
        roles = [row.reviewer_role for row in saturation_reviewers]
        if len(roles) != len(set(roles)):
            raise ValueError("saturation reviewer roles must be unique")
        if roles and set(roles) != set(SATURATION_REVIEW_ROLES):
            raise ValueError("configured saturation reviewers must contain all three roles")
        self.supervisor = supervisor
        self.saturation_reviewers = tuple(saturation_reviewers)

    def run_epoch(
        self,
        *,
        target_id: str,
        as_of_date: str,
        component_results: Sequence[ComponentResearchResult],
        red_team_result: RedTeamResearchResult | None,
        synthesis_result: SynthesisResult | None,
        structured_result: Any | None,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        source_graph_checkpoint: Mapping[str, Any],
        open_objectives: Sequence[Mapping[str, Any]],
        prior_failures: Sequence[Mapping[str, Any]],
        counter_and_supersession_route_proof: Sequence[Mapping[str, Any]],
        prior_checkpoint: ResearchEpochCheckpoint | Mapping[str, Any] | None = None,
        score_gap_context: Mapping[str, Any] | None = None,
    ) -> ResearchEpochRun:
        prior = _coerce_checkpoint(prior_checkpoint)
        if prior is not None and (
            prior.target_id != target_id or prior.as_of_date != as_of_date
        ):
            raise ValueError("research epoch resume target/as_of mismatch")
        certified_reuse = _certified_saturation_reuse_run(
            prior=prior,
            supervisor=self.supervisor,
            saturation_reviewers=self.saturation_reviewers,
            component_results=component_results,
            red_team_result=red_team_result,
            synthesis_result=synthesis_result,
            structured_result=structured_result,
            evidence_facts=evidence_facts,
            source_graph_checkpoint=source_graph_checkpoint,
            open_objectives=open_objectives,
            prior_failures=prior_failures,
            counter_and_supersession_route_proof=(
                counter_and_supersession_route_proof
            ),
            score_gap_context=score_gap_context,
        )
        if certified_reuse is not None:
            return certified_reuse
        replay = _saturation_transport_replay_context(
            prior=prior,
            saturation_reviewers=self.saturation_reviewers,
            component_results=component_results,
            red_team_result=red_team_result,
            synthesis_result=synthesis_result,
            structured_result=structured_result,
            evidence_facts=evidence_facts,
            source_graph_checkpoint=source_graph_checkpoint,
            score_gap_context=score_gap_context,
        )
        if replay is not None:
            epoch, supervisor_review, state = replay
        else:
            epoch = (prior.epoch + 1) if prior else 1
            supervisor_review = self.supervisor.review_epoch(
                epoch=epoch,
                target_id=target_id,
                as_of_date=as_of_date,
                component_results=component_results,
                red_team_result=red_team_result,
                synthesis_result=synthesis_result,
                structured_result=structured_result,
                evidence_facts=evidence_facts,
                source_graph_checkpoint=source_graph_checkpoint,
                open_objectives=open_objectives,
                prior_failures=prior_failures,
                counter_and_supersession_route_proof=counter_and_supersession_route_proof,
                prior_review=prior.supervisor_review if prior else None,
                score_gap_context=score_gap_context,
            )
            state = _research_epoch_state(
                target_id=target_id,
                as_of_date=as_of_date,
                epoch=epoch,
                prior=prior,
                evidence_facts=evidence_facts,
                component_results=component_results,
                source_graph_checkpoint=source_graph_checkpoint,
                supervisor_review=supervisor_review,
            )
            state["checkpoint_id"] = _research_checkpoint_id(state)
            state["checkpoint_hash"] = _research_checkpoint_hash(state)
        base_checkpoint_id = str(state["checkpoint_id"])
        preliminary = dict(state)

        reviewer_results: list[SaturationReviewerResult] = []
        certificate = None
        if supervisor_review.ready_for_independent_saturation_review:
            if self.saturation_reviewers:
                for reviewer in self.saturation_reviewers:
                    reviewer_results.append(
                        reviewer.review(
                            checkpoint=preliminary,
                            supervisor_review=supervisor_review,
                            component_results=component_results,
                            red_team_result=red_team_result,
                            structured_result=structured_result,
                            evidence_facts=evidence_facts,
                            source_graph_checkpoint=source_graph_checkpoint,
                        )
                    )
                completed_reviews = tuple(
                    row.review
                    for row in reviewer_results
                    if row.status == "COMPLETE" and row.review is not None
                )
                certificate = SemanticSaturationCertifier().certify(
                    completed_reviews,
                    expected_checkpoint_id=base_checkpoint_id,
                    require_provider_reviews=True,
                )
            else:
                certificate = SemanticSaturationCertifier().certify(
                    (),
                    expected_checkpoint_id=base_checkpoint_id,
                    require_provider_reviews=True,
                )
        state["saturation_reviews"] = [row.to_dict() for row in reviewer_results]
        state["saturation_certificate"] = (
            certificate.to_dict() if certificate else None
        )
        certified = bool(certificate and certificate.semantic_saturation_certified)
        state["semantic_saturation_certified"] = certified
        state["status"] = (
            "SEMANTIC_SATURATION_CERTIFIED"
            if certified
            else "READY_FOR_INDEPENDENT_SATURATION_REVIEW"
            if supervisor_review.ready_for_independent_saturation_review
            else "NEXT_RESEARCH_REQUIRED"
        )
        if certified:
            state["next_actions"] = []
        elif supervisor_review.ready_for_independent_saturation_review:
            review_actions = []
            for row in reviewer_results:
                if row.status == "PENDING":
                    review_actions.extend(
                        f"{row.reviewer_role}:{reason}"
                        for reason in row.pending_reasons
                    )
                elif row.review and not row.review.approve:
                    review_actions.append(
                        f"{row.reviewer_role}:resolve independent completeness objections"
                    )
            if not reviewer_results:
                review_actions.append(
                    "configure and run all three independent semantic saturation reviewers"
                )
            state["next_actions"] = list(
                dict.fromkeys((*state["next_actions"], *review_actions))
            )
            reviewer_questions = [
                question
                for row in reviewer_results
                if row.review is not None
                for question in row.review.unresolved_material_questions
            ]
            state["unresolved_material_questions"] = list(
                dict.fromkeys(
                    (*state["unresolved_material_questions"], *reviewer_questions)
                )
            )
        state["checkpoint_hash"] = _research_checkpoint_hash(state)
        checkpoint = _checkpoint_from_mapping(state)
        return ResearchEpochRun(
            checkpoint=checkpoint,
            supervisor_review=supervisor_review,
            saturation_reviewer_results=tuple(reviewer_results),
            saturation_certificate=certificate,
        )


_COLLABORATION_RESPONSE_PENDING_PATTERN = re.compile(
    r"(?:^|:)COLLABORATION_RESPONSE_PENDING:"
    r"COLLABREQ-[0-9a-f]{64}(?:$|:)"
)


def _certified_saturation_reuse_run(
    *,
    prior: ResearchEpochCheckpoint | None,
    supervisor: ResearchSupervisor,
    saturation_reviewers: Sequence[SemanticSaturationReviewer],
    component_results: Sequence[ComponentResearchResult],
    red_team_result: RedTeamResearchResult | None,
    synthesis_result: SynthesisResult | None,
    structured_result: Any | None,
    evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
    source_graph_checkpoint: Mapping[str, Any],
    open_objectives: Sequence[Mapping[str, Any]],
    prior_failures: Sequence[Mapping[str, Any]],
    counter_and_supersession_route_proof: Sequence[Mapping[str, Any]],
    score_gap_context: Mapping[str, Any] | None,
) -> ResearchEpochRun | None:
    """Reuse one unchanged v3 certificate without reopening provider review.

    A downstream retry, such as StageCourt transport recovery, does not create
    new research semantics.  The persisted certificate may therefore be
    replayed only after rebuilding its pre-review checkpoint and proving that
    every current provider prompt still matches the three immutable prompt
    commitments.  Status text alone is never sufficient.
    """

    if (
        prior is None
        or prior.schema_version != "e2r_research_epoch_checkpoint_v3"
        or prior.status != "SEMANTIC_SATURATION_CERTIFIED"
        or not prior.semantic_saturation_certified
        or len(saturation_reviewers) != len(SATURATION_REVIEW_ROLES)
        or set(row.reviewer_role for row in saturation_reviewers)
        != set(SATURATION_REVIEW_ROLES)
        or len(prior.saturation_reviews) != len(SATURATION_REVIEW_ROLES)
        or _material_score_disagreement_component_ids(score_gap_context)
    ):
        return None
    if str(source_graph_checkpoint.get("checkpoint_id") or "") != str(
        prior.source_graph_checkpoint_id or ""
    ):
        return None

    try:
        supervisor_review = _coerce_supervisor_review(prior.supervisor_review)
    except (KeyError, TypeError, ValueError):
        return None
    current_supervisor_provider = str(
        getattr(
            supervisor.provider,
            "provider_name",
            type(supervisor.provider).__name__,
        )
    )
    if (
        supervisor_review.epoch != prior.epoch
        or supervisor_review.reviewer_role != supervisor.reviewer_role
        or supervisor_review.provider_name != current_supervisor_provider
        or not str(supervisor_review.prompt_hash or "").strip()
        or not supervisor_review.ready_for_independent_saturation_review
        or synthesis_result is None
        or synthesis_result.status != "COMPLETE"
        or synthesis_result.memo is None
        or supervisor_review.synthesis_memo_id
        != synthesis_result.memo.memo_id
        or supervisor_review.synthesis_memo_hash
        != _stable_hash(synthesis_result.memo.to_dict())
    ):
        return None
    prior_review_prompt_projection = (
        supervisor_review.prior_review_prompt_projection
    )
    if (
        supervisor_review.schema_version
        == "e2r_research_supervisor_review_v2"
        and prior.epoch > 1
    ):
        recover_payload = getattr(
            supervisor.provider,
            "validated_request_payload",
            None,
        )
        if not callable(recover_payload):
            return None
        try:
            recovered_payload = recover_payload(
                pass_name="RESEARCH_SUPERVISOR_REVIEW",
                prompt_hash=str(supervisor_review.prompt_hash),
            )
        except (KeyError, TypeError, ValueError, RuntimeError, OSError):
            return None
        if not isinstance(recovered_payload, Mapping):
            return None
        recovered_projection = recovered_payload.get(
            "prior_supervisor_review"
        )
        if recovered_projection is not None and not isinstance(
            recovered_projection,
            Mapping,
        ):
            return None
        prior_review_prompt_projection = recovered_projection
    try:
        current_supervisor_prompt_hash = supervisor.preview_prompt_hash(
            epoch=prior.epoch,
            target_id=prior.target_id,
            as_of_date=prior.as_of_date,
            component_results=component_results,
            red_team_result=red_team_result,
            synthesis_result=synthesis_result,
            structured_result=structured_result,
            evidence_facts=evidence_facts,
            source_graph_checkpoint=source_graph_checkpoint,
            open_objectives=open_objectives,
            prior_failures=prior_failures,
            counter_and_supersession_route_proof=(
                counter_and_supersession_route_proof
            ),
            prior_review=None,
            prior_review_prompt_projection=(
                prior_review_prompt_projection
            ),
            score_gap_context=score_gap_context,
        )
    except (KeyError, TypeError, ValueError, RuntimeError, OSError):
        return None
    if current_supervisor_prompt_hash != supervisor_review.prompt_hash:
        return None

    current_component_hashes = _complete_component_memo_hashes(
        component_results
    )
    if (
        current_component_hashes is None
        or dict(prior.component_memo_hashes) != current_component_hashes
        or red_team_result is None
        or red_team_result.status != "COMPLETE"
        or red_team_result.memo is None
        or not red_team_result.memo.review_complete
        or structured_result is None
        or getattr(structured_result, "status", None) != "COMPLETE"
        or not getattr(structured_result, "records", None)
        or any(
            (getattr(structured_result, "missing_roles_by_component", {}) or {}).values()
        )
    ):
        return None
    synthesis_memo = synthesis_result.memo
    current_memo_ids = {
        row.memo.memo_id
        for row in component_results
        if row.memo is not None
    }
    if (
        set(synthesis_memo.component_memo_ids) != current_memo_ids
        or synthesis_memo.red_team_memo_id != red_team_result.memo.memo_id
        or synthesis_memo.red_team_memo_hash
        != _stable_hash(red_team_result.memo.to_dict())
    ):
        return None

    fact_ids = tuple(
        str(_fact_payload(row).get("fact_id") or "") for row in evidence_facts
    )
    if (
        any(not value for value in fact_ids)
        or len(fact_ids) != len(set(fact_ids))
        or set(fact_ids) != set(prior.current_fact_ids)
    ):
        return None

    reviewer_by_role = {
        row.reviewer_role: row for row in saturation_reviewers
    }
    persisted_results: list[SaturationReviewerResult] = []
    reviews: list[SaturationReview] = []
    result_by_role: dict[str, SaturationReviewerResult] = {}
    try:
        for raw_result in prior.saturation_reviews:
            result = _coerce_saturation_reviewer_result(raw_result)
            role = result.reviewer_role
            if role not in reviewer_by_role or role in result_by_role:
                return None
            reviewer = reviewer_by_role[role]
            provider_name = str(
                getattr(
                    reviewer.provider,
                    "provider_name",
                    type(reviewer.provider).__name__,
                )
            )
            review = result.review
            if (
                result.status != "COMPLETE"
                or result.pending_reasons
                or review is None
                or result.provider_name != provider_name
                or review.provider_name != provider_name
                or not result.prompt_hash
                or result.prompt_hash != review.prompt_hash
                or not review.provider_backed
                or not review.approve
                or review.checkpoint_id != prior.checkpoint_id
                or review.epoch != prior.epoch
                or review.gold_evaluation_status
                != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
                or review.gold_critical_fact_miss_count is not None
                or review.fixed_round_completion_used
                or review.zero_search_result_treated_as_saturation
                or review.transport_budget_treated_as_saturation
                or review.review_id != _expected_saturation_review_id(review)
            ):
                return None
            result_by_role[role] = result
            persisted_results.append(result)
            reviews.append(review)
        if len({row.prompt_hash for row in reviews}) != len(
            SATURATION_REVIEW_ROLES
        ):
            return None
        review_by_role = {
            row.reviewer_role: row for row in reviews
        }
        certificate = _coerce_saturation_certificate(
            prior.saturation_certificate
        )
        expected_certificate = SemanticSaturationCertifier().certify(
            reviews,
            expected_checkpoint_id=prior.checkpoint_id,
            require_provider_reviews=True,
        )
        if (
            not certificate.semantic_saturation_certified
            or certificate.status != "CERTIFIED"
            or certificate.to_dict() != expected_certificate.to_dict()
        ):
            return None
    except (KeyError, TypeError, ValueError):
        return None

    preliminary = _preliminary_saturation_state(
        prior=prior,
        supervisor_review=supervisor_review,
    )
    if preliminary is None:
        return None
    try:
        for role, reviewer in reviewer_by_role.items():
            if reviewer.preview_prompt_hash(
                checkpoint=preliminary,
                supervisor_review=supervisor_review,
                component_results=component_results,
                red_team_result=red_team_result,
                structured_result=structured_result,
                evidence_facts=evidence_facts,
                source_graph_checkpoint=source_graph_checkpoint,
            ) != result_by_role[role].prompt_hash:
                return None
            if reviewer.validate_persisted_response_identity(
                checkpoint=preliminary,
                supervisor_review=supervisor_review,
                component_results=component_results,
                red_team_result=red_team_result,
                structured_result=structured_result,
                evidence_facts=evidence_facts,
                source_graph_checkpoint=source_graph_checkpoint,
                review=review_by_role[role],
                persisted_identity=(
                    result_by_role[role].provider_response_identity
                ),
            ) is None:
                return None
    except (
        KeyError,
        TypeError,
        ValueError,
        RuntimeError,
        OSError,
    ):
        return None

    return ResearchEpochRun(
        checkpoint=prior,
        supervisor_review=supervisor_review,
        saturation_reviewer_results=tuple(persisted_results),
        saturation_certificate=certificate,
    )


def _complete_component_memo_hashes(
    component_results: Sequence[ComponentResearchResult],
) -> dict[str, str] | None:
    if (
        len(component_results) != len(CANONICAL_COMPONENT_ORDER)
        or set(row.component_id for row in component_results)
        != set(CANONICAL_COMPONENT_ORDER)
        or any(
            row.status != "COMPLETE"
            or row.memo is None
            or not row.memo.research_complete
            for row in component_results
        )
    ):
        return None
    return {
        row.component_id: _stable_hash(row.memo.to_dict())
        for row in component_results
        if row.memo is not None
    }


def _coerce_saturation_reviewer_result(
    value: Mapping[str, Any],
) -> SaturationReviewerResult:
    payload = dict(value)
    raw_review = payload.get("review")
    review = None
    if raw_review is not None:
        review_payload = dict(raw_review)
        review_payload["unresolved_material_questions"] = tuple(
            review_payload.get("unresolved_material_questions") or ()
        )
        review = SaturationReview(**review_payload)
    payload["review"] = review
    payload["pending_reasons"] = tuple(payload.get("pending_reasons") or ())
    if payload.get("provider_response_identity") is not None:
        payload["provider_response_identity"] = dict(
            payload["provider_response_identity"]
        )
    return SaturationReviewerResult(**payload)


def _coerce_saturation_certificate(
    value: Mapping[str, Any] | None,
) -> SemanticSaturationCertificate:
    if not isinstance(value, Mapping):
        raise TypeError("certified saturation checkpoint requires a certificate")
    payload = dict(value)
    for key in (
        "review_ids",
        "pending_reasons",
        "reviewer_roles",
        "provider_prompt_hashes",
    ):
        payload[key] = tuple(payload.get(key) or ())
    return SemanticSaturationCertificate(**payload)


def _expected_saturation_review_id(review: SaturationReview) -> str:
    response = {
        "approve": review.approve,
        "seven_component_memos_complete": (
            review.seven_component_memos_complete
        ),
        "material_positive_routes_reviewed": (
            review.material_positive_routes_reviewed
        ),
        "counter_and_supersession_routes_checked": (
            review.counter_and_supersession_routes_checked
        ),
        "structured_data_complete": review.structured_data_complete,
        "new_source_family_directions_reviewed": (
            review.new_source_family_directions_reviewed
        ),
        "reasonable_positive_routes_remaining": (
            not review.no_reasonable_positive_route_remaining
        ),
        "unresolved_material_questions": list(
            review.unresolved_material_questions
        ),
        "rationale": review.rationale,
    }
    return stable_intelligence_id(
        "SATREVIEW",
        {
            "reviewer_role": review.reviewer_role,
            "checkpoint_id": review.checkpoint_id,
            "epoch": review.epoch,
            "response": response,
            "prompt_hash": review.prompt_hash,
        },
    )


def _preliminary_saturation_state(
    *,
    prior: ResearchEpochCheckpoint,
    supervisor_review: ResearchSupervisorReview,
) -> dict[str, Any] | None:
    state = dict(prior.to_dict())
    state["saturation_reviews"] = []
    state["saturation_certificate"] = None
    state["semantic_saturation_certified"] = False
    state["status"] = "READY_FOR_INDEPENDENT_SATURATION_REVIEW"
    state["unresolved_material_questions"] = list(
        supervisor_review.unresolved_material_questions
    )
    state["next_actions"] = list(supervisor_review.next_actions)
    state["supervisor_review"] = supervisor_review.to_dict()
    state["checkpoint_hash"] = _research_checkpoint_hash(state)
    if _research_checkpoint_id(state) != prior.checkpoint_id:
        return None
    return state


def _saturation_transport_replay_context(
    *,
    prior: ResearchEpochCheckpoint | None,
    saturation_reviewers: Sequence[SemanticSaturationReviewer],
    component_results: Sequence[ComponentResearchResult],
    red_team_result: RedTeamResearchResult | None,
    synthesis_result: SynthesisResult | None,
    structured_result: Any | None,
    evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
    source_graph_checkpoint: Mapping[str, Any],
    score_gap_context: Mapping[str, Any] | None,
) -> tuple[int, ResearchSupervisorReview, dict[str, Any]] | None:
    """Replay only an unchanged READY checkpoint's exact transport wait.

    The persisted checkpoint contains reviewer-wait diagnostics that were not
    part of the original reviewer prompt.  Reconstruct that preliminary
    checkpoint, then require all three current prompts to match the persisted
    prompt commitments before reusing the epoch/checkpoint identity.
    """

    if (
        prior is None
        or prior.schema_version != "e2r_research_epoch_checkpoint_v3"
        or prior.status != "READY_FOR_INDEPENDENT_SATURATION_REVIEW"
        or prior.semantic_saturation_certified
        or len(saturation_reviewers) != len(SATURATION_REVIEW_ROLES)
        or set(row.reviewer_role for row in saturation_reviewers)
        != set(SATURATION_REVIEW_ROLES)
        or len(prior.saturation_reviews) != len(SATURATION_REVIEW_ROLES)
    ):
        return None
    if _material_score_disagreement_component_ids(score_gap_context):
        return None
    if str(source_graph_checkpoint.get("checkpoint_id") or "") != str(
        prior.source_graph_checkpoint_id or ""
    ):
        return None

    try:
        supervisor_review = _coerce_supervisor_review(prior.supervisor_review)
    except (KeyError, TypeError, ValueError):
        return None
    if (
        supervisor_review.epoch != prior.epoch
        or not supervisor_review.ready_for_independent_saturation_review
        or synthesis_result is None
        or synthesis_result.status != "COMPLETE"
        or synthesis_result.memo is None
        or supervisor_review.synthesis_memo_id
        != synthesis_result.memo.memo_id
        or supervisor_review.synthesis_memo_hash
        != _stable_hash(synthesis_result.memo.to_dict())
    ):
        return None

    reviewer_by_role = {
        row.reviewer_role: row for row in saturation_reviewers
    }
    persisted_by_role: dict[str, Mapping[str, Any]] = {}
    prompt_hashes: list[str] = []
    pending_count = 0
    for raw_result in prior.saturation_reviews:
        if not isinstance(raw_result, Mapping):
            return None
        result = dict(raw_result)
        role = str(result.get("reviewer_role") or "")
        if role not in reviewer_by_role or role in persisted_by_role:
            return None
        reviewer = reviewer_by_role[role]
        provider_name = str(
            getattr(
                reviewer.provider,
                "provider_name",
                type(reviewer.provider).__name__,
            )
        )
        prompt_hash = str(result.get("prompt_hash") or "")
        if (
            not prompt_hash
            or str(result.get("provider_name") or "") != provider_name
        ):
            return None
        prompt_hashes.append(prompt_hash)
        status = str(result.get("status") or "")
        if status == "PENDING":
            reasons = result.get("pending_reasons") or ()
            if (
                isinstance(reasons, (str, bytes))
                or not isinstance(reasons, Sequence)
                or not reasons
                or result.get("review") is not None
                or not all(
                    _COLLABORATION_RESPONSE_PENDING_PATTERN.search(str(reason))
                    for reason in reasons
                )
            ):
                return None
            pending_count += 1
        elif status == "COMPLETE":
            review = result.get("review")
            if not isinstance(review, Mapping) or (
                review.get("approve") is not True
                or review.get("provider_backed") is not True
                or str(review.get("reviewer_role") or "") != role
                or str(review.get("checkpoint_id") or "")
                != prior.checkpoint_id
                or int(review.get("epoch") or 0) != prior.epoch
                or str(review.get("provider_name") or "") != provider_name
                or str(review.get("prompt_hash") or "") != prompt_hash
                or review.get("gold_evaluation_status")
                != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
                or review.get("gold_critical_fact_miss_count") is not None
            ):
                return None
        else:
            return None
        persisted_by_role[role] = result
    if pending_count == 0 or len(prompt_hashes) != len(set(prompt_hashes)):
        return None

    certificate = prior.saturation_certificate
    if not isinstance(certificate, Mapping) or (
        certificate.get("status") != "PENDING"
        or certificate.get("semantic_saturation_certified") is not False
        or str(certificate.get("checkpoint_id") or "")
        != prior.checkpoint_id
        or certificate.get("provider_backed_reviews_required") is not True
        or certificate.get("gold_evaluation_status")
        != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
        or certificate.get("gold_critical_fact_miss_count") is not None
    ):
        return None

    state = _preliminary_saturation_state(
        prior=prior,
        supervisor_review=supervisor_review,
    )
    if state is None:
        return None

    try:
        for role, reviewer in reviewer_by_role.items():
            current_prompt_hash = reviewer.preview_prompt_hash(
                checkpoint=state,
                supervisor_review=supervisor_review,
                component_results=component_results,
                red_team_result=red_team_result,
                structured_result=structured_result,
                evidence_facts=evidence_facts,
                source_graph_checkpoint=source_graph_checkpoint,
            )
            if current_prompt_hash != str(
                persisted_by_role[role].get("prompt_hash") or ""
            ):
                return None
    except (
        KeyError,
        TypeError,
        ValueError,
        RuntimeError,
        OSError,
    ):
        return None
    return prior.epoch, supervisor_review, state


def _coerce_supervisor_review(
    value: ResearchSupervisorReview | Mapping[str, Any],
) -> ResearchSupervisorReview:
    if isinstance(value, ResearchSupervisorReview):
        return value
    payload = dict(value)
    payload["component_status"] = dict(payload.get("component_status") or {})
    for key in (
        "unresolved_material_questions",
        "source_family_gaps",
        "parser_or_extractor_failures",
        "next_actions",
    ):
        payload[key] = tuple(payload.get(key) or ())
    if payload.get("prior_review_prompt_projection") is not None:
        payload["prior_review_prompt_projection"] = dict(
            payload["prior_review_prompt_projection"]
        )
    component_findings = []
    for row in payload.get("component_findings") or ():
        values = dict(row)
        values["missing_fact_needs"] = tuple(
            values.get("missing_fact_needs") or ()
        )
        component_findings.append(SupervisorComponentFinding(**values))
    payload["component_findings"] = tuple(component_findings)
    payload["missing_material_facts"] = tuple(
        SupervisorFactGap(**dict(row))
        for row in payload.get("missing_material_facts") or ()
    )
    payload["failure_assessments"] = tuple(
        SupervisorFailureAssessment(**dict(row))
        for row in payload.get("failure_assessments") or ()
    )
    payload["new_source_family_directions"] = tuple(
        SupervisorSourceDirection(**dict(row))
        for row in payload.get("new_source_family_directions") or ()
    )
    query_directions = []
    for row in payload.get("query_direction_briefs") or ():
        values = dict(row)
        values["avoid_repeating"] = tuple(values.get("avoid_repeating") or ())
        query_directions.append(SupervisorQueryDirection(**values))
    payload["query_direction_briefs"] = tuple(query_directions)
    return ResearchSupervisorReview(**payload)


def write_research_epoch_run(
    run: ResearchEpochRun, output_directory: str | Path
) -> Mapping[str, Path]:
    root = Path(output_directory)
    paths = {
        key: root / filename for key, filename in RESEARCH_EPOCH_OUTPUT_FILES.items()
    }
    write_json(paths["checkpoint"], run.checkpoint.to_dict())
    write_json(paths["supervisor_review"], run.supervisor_review.to_dict())
    write_jsonl(
        paths["saturation_reviews"],
        (row.to_dict() for row in run.saturation_reviewer_results),
    )
    write_json(
        paths["saturation_certificate"],
        run.saturation_certificate.to_dict()
        if run.saturation_certificate
        else {
            "status": "PENDING",
            "semantic_saturation_certified": False,
            "checkpoint_id": run.checkpoint.checkpoint_id,
            "pending_reasons": list(
                run.checkpoint.unresolved_material_questions
                or ("SATURATION_REVIEW_NOT_COMPLETE",)
            ),
        },
    )
    return paths


def load_research_epoch_checkpoint(
    path: str | Path,
) -> ResearchEpochCheckpoint:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("research epoch checkpoint must be an object")
    return _checkpoint_from_mapping(payload)


def _research_epoch_state(
    *,
    target_id: str,
    as_of_date: str,
    epoch: int,
    prior: ResearchEpochCheckpoint | None,
    evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
    component_results: Sequence[ComponentResearchResult],
    source_graph_checkpoint: Mapping[str, Any],
    supervisor_review: ResearchSupervisorReview,
) -> dict[str, Any]:
    date.fromisoformat(as_of_date)
    query_rows = tuple(
        _json_safe(row)
        for row in (source_graph_checkpoint.get("generated_queries") or ())
    )
    document_rows = tuple(
        _json_safe(row)
        for row in (source_graph_checkpoint.get("evidence_documents") or ())
    )
    fact_rows = tuple(_fact_payload(row) for row in evidence_facts)
    query_by_id = {_row_id(row, "query_id", "QUERY"): row for row in query_rows}
    document_by_id = {
        _row_id(row, "document_id", "DOCUMENT"): row for row in document_rows
    }
    fact_by_id = {str(row["fact_id"]): row for row in fact_rows}
    if len(query_by_id) != len(query_rows):
        raise ValueError("research epoch query ids must be unique")
    if len(document_by_id) != len(document_rows):
        raise ValueError("research epoch document ids must be unique")
    if len(fact_by_id) != len(fact_rows):
        raise ValueError("research epoch fact ids must be unique")
    prior_query_ids = set(prior.cumulative_query_ids if prior else ())
    prior_document_ids = set(prior.cumulative_document_ids if prior else ())
    prior_fact_ids = set(prior.cumulative_fact_ids if prior else ())
    prior_current_fact_ids = set(prior.current_fact_ids if prior else ())
    prior_retired_fact_ids = set(prior.retired_fact_ids if prior else ())
    current_memo_hashes: dict[str, str] = dict(
        prior.component_memo_hashes if prior else {}
    )
    changed_memos = []
    prior_memo_hashes = dict(prior.component_memo_hashes if prior else {})
    component_ids = [row.component_id for row in component_results]
    if len(component_ids) != len(set(component_ids)):
        raise ValueError("research epoch component results must be unique")
    if prior and not prior_query_ids.issubset(query_by_id):
        raise ValueError("resumed Source Graph lost cumulative query lineage")
    quarantined_document_ids = validated_quarantined_document_ids(
        source_graph_checkpoint
    )
    if prior and not prior_document_ids.issubset(
        set(document_by_id) | set(quarantined_document_ids)
    ):
        raise ValueError("resumed Source Graph lost cumulative document lineage")
    current_fact_ids = set(fact_by_id)
    retired_this_epoch = prior_current_fact_ids - current_fact_ids
    retired_fact_ids = (
        prior_retired_fact_ids | retired_this_epoch
    ) - current_fact_ids
    for result in sorted(component_results, key=lambda row: row.component_id):
        if result.memo is None:
            continue
        memo = result.memo.to_dict()
        memo_hash = _stable_hash(memo)
        current_memo_hashes[result.component_id] = memo_hash
        if prior_memo_hashes.get(result.component_id) != memo_hash:
            changed_memos.append(memo)
    state = {
        "schema_version": "e2r_research_epoch_checkpoint_v3",
        "target_id": target_id,
        "as_of_date": as_of_date,
        "epoch": epoch,
        "status": (
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW"
            if supervisor_review.ready_for_independent_saturation_review
            else "NEXT_RESEARCH_REQUIRED"
        ),
        "resumed_from_checkpoint_id": prior.checkpoint_id if prior else None,
        "source_graph_checkpoint_id": source_graph_checkpoint.get("checkpoint_id"),
        "queries": [
            query_by_id[row_id]
            for row_id in sorted(set(query_by_id) - prior_query_ids)
        ],
        "documents": [
            document_by_id[row_id]
            for row_id in sorted(set(document_by_id) - prior_document_ids)
        ],
        "new_facts": [
            fact_by_id[row_id]
            for row_id in sorted(set(fact_by_id) - prior_fact_ids)
        ],
        "retired_facts": [
            {
                "fact_id": fact_id,
                "reason": "FACT_EXTRACTION_REVISED_OR_SUPERSEDED",
                "retired_in_epoch": epoch,
                "prior_checkpoint_id": prior.checkpoint_id if prior else None,
                "production_score_authority": False,
            }
            for fact_id in sorted(retired_this_epoch)
        ],
        "changed_component_memos": changed_memos,
        "unresolved_material_questions": list(
            supervisor_review.unresolved_material_questions
        ),
        "next_actions": list(supervisor_review.next_actions),
        "supervisor_review": supervisor_review.to_dict(),
        "saturation_reviews": [],
        "saturation_certificate": None,
        "cumulative_query_ids": sorted(set(query_by_id) | prior_query_ids),
        "cumulative_document_ids": sorted(
            set(document_by_id) | prior_document_ids
        ),
        "cumulative_fact_ids": sorted(set(fact_by_id) | prior_fact_ids),
        "current_fact_ids": sorted(current_fact_ids),
        "retired_fact_ids": sorted(retired_fact_ids),
        "component_memo_hashes": current_memo_hashes,
        "semantic_saturation_certified": False,
        "gold_evaluation_status": GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
        "gold_critical_fact_miss_count": None,
        "completion_based_on_fixed_rounds": False,
        "zero_search_result_treated_as_saturation": False,
        "transport_budget_treated_as_completion": False,
        "production_score_authority": False,
    }
    return state


def _checkpoint_from_mapping(payload: Mapping[str, Any]) -> ResearchEpochCheckpoint:
    values = dict(payload)
    _validate_v3_checkpoint_schema(values)
    if values.get("schema_version") in {
        "e2r_research_epoch_checkpoint_v1",
        "e2r_research_epoch_checkpoint_v2",
    }:
        # Legacy checkpoints overloaded 0/1 as an apparent Gold result even
        # though Phase 94 had not opened the private post-run lane.  Preserve
        # the raw field only so the original id/hash remains verifiable; the
        # explicit state makes it non-authoritative and the next epoch writes
        # the v3 nullable contract.
        values.setdefault(
            "gold_evaluation_status",
            GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
        )
    legacy_current_fact_ids_missing = "current_fact_ids" not in values
    legacy_retired_fact_ids_missing = "retired_fact_ids" not in values
    legacy_retired_facts_missing = "retired_facts" not in values
    for key in (
        "queries",
        "documents",
        "new_facts",
        "retired_facts",
        "changed_component_memos",
        "saturation_reviews",
    ):
        values[key] = tuple(_json_safe(row) for row in values.get(key) or ())
    for key in (
        "cumulative_query_ids",
        "cumulative_document_ids",
        "cumulative_fact_ids",
        "current_fact_ids",
        "retired_fact_ids",
        "unresolved_material_questions",
        "next_actions",
    ):
        values[key] = tuple(values.get(key) or ())
    values["component_memo_hashes"] = dict(
        values.get("component_memo_hashes") or {}
    )
    if legacy_current_fact_ids_missing:
        values["current_fact_ids"] = tuple(values.get("cumulative_fact_ids") or ())
    if legacy_retired_fact_ids_missing:
        values["retired_fact_ids"] = ()
    if legacy_retired_facts_missing:
        values["retired_facts"] = ()
    values["supervisor_review"] = _json_safe(
        values.get("supervisor_review") or {}
    )
    if values.get("saturation_certificate") is not None:
        values["saturation_certificate"] = _json_safe(
            values["saturation_certificate"]
        )
    return ResearchEpochCheckpoint(**values)


def _coerce_checkpoint(
    value: ResearchEpochCheckpoint | Mapping[str, Any] | None,
) -> ResearchEpochCheckpoint | None:
    if value is None:
        return value
    if isinstance(value, ResearchEpochCheckpoint):
        payload = value.to_dict()
        reconstructed = _checkpoint_from_mapping(payload)
        if reconstructed.to_dict() != payload:
            raise ValueError(
                "research epoch checkpoint object round-trip mismatch"
            )
        return reconstructed
    return _checkpoint_from_mapping(value)


def _validate_v3_checkpoint_schema(payload: Mapping[str, Any]) -> None:
    if payload.get("schema_version") != "e2r_research_epoch_checkpoint_v3":
        return
    _require_exact_mapping_keys(
        payload,
        set(ResearchEpochCheckpoint.__dataclass_fields__),
        "research epoch checkpoint v3",
    )
    supervisor = payload.get("supervisor_review")
    if not isinstance(supervisor, Mapping):
        raise ValueError("research supervisor review must be an object")
    supervisor_schema_version = supervisor.get("schema_version")
    supervisor_keys = set(ResearchSupervisorReview.__dataclass_fields__)
    if (
        supervisor_schema_version
        == "e2r_research_supervisor_review_v2"
    ):
        expected_supervisor_keys = (
            supervisor_keys - {"prior_review_prompt_projection"}
        )
    elif (
        supervisor_schema_version
        == "e2r_research_supervisor_review_v3"
    ):
        expected_supervisor_keys = supervisor_keys
    else:
        raise ValueError("unknown nested research supervisor review schema")
    _require_exact_mapping_keys(
        supervisor,
        expected_supervisor_keys,
        f"research supervisor review {supervisor_schema_version}",
    )
    _validate_supervisor_nested_schema(supervisor)
    try:
        _coerce_supervisor_review(supervisor)
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(
            "invalid nested research supervisor review"
        ) from exc

    results = payload.get("saturation_reviews")
    if not isinstance(results, (list, tuple)):
        raise ValueError("checkpoint saturation reviews must be an array")
    result_keys = set(SaturationReviewerResult.__dataclass_fields__)
    legacy_result_keys = result_keys - {"provider_response_identity"}
    for result in results:
        if not isinstance(result, Mapping) or (
            set(result) != result_keys
            and set(result) != legacy_result_keys
        ):
            raise ValueError(
                "checkpoint saturation reviewer result key mismatch"
            )
        identity = result.get("provider_response_identity")
        if identity is not None:
            _require_exact_mapping_keys(
                identity,
                {
                    "schema_version",
                    "provider_route",
                    "provider_name",
                    "pass_name",
                    "prompt_hash",
                    "response_hash",
                    "request_locator_id",
                    "response_locator_id",
                    "provenance_hash",
                },
                "validated provider response identity",
            )
            if (
                identity.get("schema_version")
                != "e2r_v5_validated_provider_response_identity_v1"
            ):
                raise ValueError(
                    "unknown validated provider response identity schema"
                )
        review = result.get("review")
        if review is not None:
            _require_exact_mapping_keys(
                review,
                set(SaturationReview.__dataclass_fields__),
                "semantic saturation review v3",
            )
            if (
                review.get("schema_version")
                != "e2r_semantic_saturation_review_v3"
            ):
                raise ValueError(
                    "unknown nested semantic saturation review schema"
                )

    certificate = payload.get("saturation_certificate")
    if certificate is not None:
        _require_exact_mapping_keys(
            certificate,
            set(SemanticSaturationCertificate.__dataclass_fields__),
            "semantic saturation certificate v3",
        )
        if (
            certificate.get("schema_version")
            != "e2r_semantic_saturation_certificate_v3"
        ):
            raise ValueError(
                "unknown nested semantic saturation certificate schema"
            )


def _validate_supervisor_nested_schema(
    supervisor: Mapping[str, Any],
) -> None:
    nested = (
        (
            "component_findings",
            set(SupervisorComponentFinding.__dataclass_fields__),
        ),
        (
            "missing_material_facts",
            set(SupervisorFactGap.__dataclass_fields__),
        ),
        (
            "failure_assessments",
            set(SupervisorFailureAssessment.__dataclass_fields__),
        ),
        (
            "new_source_family_directions",
            set(SupervisorSourceDirection.__dataclass_fields__),
        ),
        (
            "query_direction_briefs",
            set(SupervisorQueryDirection.__dataclass_fields__),
        ),
    )
    for key, expected_keys in nested:
        rows = supervisor.get(key)
        if not isinstance(rows, (list, tuple)):
            raise ValueError(f"nested supervisor {key} must be an array")
        for row in rows:
            _require_exact_mapping_keys(
                row,
                expected_keys,
                f"nested supervisor {key} row",
            )


def _require_exact_mapping_keys(
    value: Any,
    expected_keys: set[str],
    label: str,
) -> None:
    if not isinstance(value, Mapping) or set(value) != expected_keys:
        raise ValueError(f"{label} key roster mismatch")


def _research_checkpoint_id(state: Mapping[str, Any]) -> str:
    legacy_projection_fields = _legacy_checkpoint_projection_fields(state)
    identity = {
        key: value
        for key, value in state.items()
        if key
        not in {
            "checkpoint_id",
            "checkpoint_hash",
            "saturation_reviews",
            "saturation_certificate",
            "semantic_saturation_certified",
            "status",
            "unresolved_material_questions",
            "next_actions",
        }
        | legacy_projection_fields
    }
    return stable_intelligence_id("REPOCH", identity)


def _research_checkpoint_hash(payload: Mapping[str, Any]) -> str:
    legacy_projection_fields = _legacy_checkpoint_projection_fields(payload)
    values = {
        key: value
        for key, value in payload.items()
        if key != "checkpoint_hash" and key not in legacy_projection_fields
    }
    return _stable_hash(values)


def _legacy_checkpoint_projection_fields(
    payload: Mapping[str, Any],
) -> set[str]:
    schema_version = payload.get("schema_version")
    fields = (
        {"gold_evaluation_status"}
        if schema_version
        in {
            "e2r_research_epoch_checkpoint_v1",
            "e2r_research_epoch_checkpoint_v2",
        }
        else set()
    )
    if schema_version == "e2r_research_epoch_checkpoint_v1":
        fields.update({"retired_facts", "current_fact_ids", "retired_fact_ids"})
    return fields


def _row_id(row: Mapping[str, Any], key: str, prefix: str) -> str:
    value = str(row.get(key) or "").strip()
    return value or stable_intelligence_id(prefix, row)


def _fact_payload(row: EvidenceFact | Mapping[str, Any]) -> Mapping[str, Any]:
    payload = row.to_dict() if isinstance(row, EvidenceFact) else dict(row)
    if not str(payload.get("fact_id") or "").strip():
        raise ValueError("research epoch fact id is required")
    return _json_safe(payload)


def _stable_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _json_safe(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False, sort_keys=True, default=str))


__all__ = [
    "RESEARCH_EPOCH_OUTPUT_FILES",
    "ResearchEpochCheckpoint",
    "ResearchEpochRun",
    "ResearchEpochRunner",
    "load_research_epoch_checkpoint",
    "write_research_epoch_run",
]
