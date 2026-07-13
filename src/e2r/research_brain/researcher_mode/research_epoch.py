"""Checkpoint/resume orchestration for semantic Researcher Mode epochs."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .component_researcher import ComponentResearchResult
from .red_team_researcher import RedTeamResearchResult
from .research_supervisor import ResearchSupervisor, ResearchSupervisorReview
from .saturation import (
    SATURATION_REVIEW_ROLES,
    SaturationReview,
    SaturationReviewerResult,
    SemanticSaturationCertificate,
    SemanticSaturationCertifier,
    SemanticSaturationReviewer,
)
from .schemas import EvidenceFact


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
    gold_critical_fact_miss_count: int
    completion_based_on_fixed_rounds: bool = False
    zero_search_result_treated_as_saturation: bool = False
    transport_budget_treated_as_completion: bool = False
    production_score_authority: bool = False
    schema_version: str = "e2r_research_epoch_checkpoint_v2"

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
        if self.gold_critical_fact_miss_count < 0:
            raise ValueError("gold critical fact miss count cannot be negative")
        if self.semantic_saturation_certified and self.gold_critical_fact_miss_count:
            raise ValueError("critical fact miss prevents semantic saturation")
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
            if (
                certificate.get("status") != "CERTIFIED"
                or certificate.get("checkpoint_id") != self.checkpoint_id
                or certificate.get("provider_backed_reviews_required") is not True
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
            "gold_critical_fact_miss_count": self.gold_critical_fact_miss_count,
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
        structured_result: Any | None,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        source_graph_checkpoint: Mapping[str, Any],
        open_objectives: Sequence[Mapping[str, Any]],
        prior_failures: Sequence[Mapping[str, Any]],
        counter_and_supersession_route_proof: Sequence[Mapping[str, Any]],
        prior_checkpoint: ResearchEpochCheckpoint | Mapping[str, Any] | None = None,
        gold_critical_fact_miss_count: int = 0,
    ) -> ResearchEpochRun:
        if gold_critical_fact_miss_count < 0:
            raise ValueError("gold critical fact miss count cannot be negative")
        prior = _coerce_checkpoint(prior_checkpoint)
        if prior is not None and (
            prior.target_id != target_id or prior.as_of_date != as_of_date
        ):
            raise ValueError("research epoch resume target/as_of mismatch")
        epoch = (prior.epoch + 1) if prior else 1
        supervisor_review = self.supervisor.review_epoch(
            epoch=epoch,
            target_id=target_id,
            as_of_date=as_of_date,
            component_results=component_results,
            red_team_result=red_team_result,
            structured_result=structured_result,
            evidence_facts=evidence_facts,
            source_graph_checkpoint=source_graph_checkpoint,
            open_objectives=open_objectives,
            prior_failures=prior_failures,
            counter_and_supersession_route_proof=counter_and_supersession_route_proof,
            prior_review=prior.supervisor_review if prior else None,
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
            gold_critical_fact_miss_count=gold_critical_fact_miss_count,
        )
        base_checkpoint_id = _research_checkpoint_id(state)
        state["checkpoint_id"] = base_checkpoint_id
        state["checkpoint_hash"] = _research_checkpoint_hash(state)
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
                            source_graph_checkpoint=source_graph_checkpoint,
                            gold_critical_fact_miss_count=gold_critical_fact_miss_count,
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
    gold_critical_fact_miss_count: int,
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
    if prior and not prior_document_ids.issubset(document_by_id):
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
        "schema_version": "e2r_research_epoch_checkpoint_v2",
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
        "gold_critical_fact_miss_count": gold_critical_fact_miss_count,
        "completion_based_on_fixed_rounds": False,
        "zero_search_result_treated_as_saturation": False,
        "transport_budget_treated_as_completion": False,
        "production_score_authority": False,
    }
    return state


def _checkpoint_from_mapping(payload: Mapping[str, Any]) -> ResearchEpochCheckpoint:
    values = dict(payload)
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
    if value is None or isinstance(value, ResearchEpochCheckpoint):
        return value
    return _checkpoint_from_mapping(value)


def _research_checkpoint_id(state: Mapping[str, Any]) -> str:
    legacy_projection_fields = (
        {"retired_facts", "current_fact_ids", "retired_fact_ids"}
        if state.get("schema_version") == "e2r_research_epoch_checkpoint_v1"
        else set()
    )
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
    legacy_projection_fields = (
        {"retired_facts", "current_fact_ids", "retired_fact_ids"}
        if payload.get("schema_version") == "e2r_research_epoch_checkpoint_v1"
        else set()
    )
    values = {
        key: value
        for key, value in payload.items()
        if key != "checkpoint_hash" and key not in legacy_projection_fields
    }
    return _stable_hash(values)


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
