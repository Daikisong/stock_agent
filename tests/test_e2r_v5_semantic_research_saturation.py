from __future__ import annotations

import hashlib
import inspect
import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.researcher_mode import (
    CANONICAL_COMPONENT_MAX_POINTS,
    CANONICAL_COMPONENT_ORDER,
    GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
    PHASE87_PASS,
    RESEARCH_EPOCH_OUTPUT_FILES,
    RESEARCH_SUPERVISOR_SCHEMA,
    SATURATION_REVIEW_ROLES,
    SEMANTIC_SATURATION_REVIEW_SCHEMA,
    ComponentResearchMemo,
    ComponentResearchResult,
    CollaborationCodexResearcherProvider,
    CollaborationCodexSubagentTransport,
    EvidenceFact,
    RedTeamMemo,
    RedTeamResearchResult,
    ResearchEpochRunner,
    ResearchSupervisor,
    ResearchSupervisorReview,
    SaturationReview,
    SemanticSaturationCertifier,
    SemanticSaturationReviewer,
    SupervisorFailureAssessment,
    SynthesisMemo,
    SynthesisResult,
    StructuredMetricRecord,
    StructuredResearchResult,
    compile_phase87_semantic_research_saturation_audit,
    import_collaboration_response,
    load_research_epoch_checkpoint,
    validate_source_graph_checkpoint,
    validated_quarantined_document_ids,
    write_research_epoch_run,
)
from e2r.research_brain.researcher_mode.research_supervisor import (
    build_counter_and_supersession_route_proof,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.saturation import (
    _semantic_saturation_prompt_payload,
)
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    _completion_gates,
    _production_semantic_saturation_certified,
)
from e2r.research_brain.researcher_mode.research_epoch import (
    _preliminary_saturation_state,
    _research_checkpoint_hash,
    _research_checkpoint_id,
)


TARGET = "CURRENT-TARGET"
AS_OF_DATE = "2026-06-29"
ARCHETYPE = "CURRENT-ARCHETYPE"
OBJECTIVE_ID = "OBJ-CURRENT"


class Phase87SupervisorProvider:
    def __init__(self, mode: str = "READY") -> None:
        self.mode = mode
        self.provider_name = f"PHASE87_SUPERVISOR_{mode}"
        self.calls: list[Mapping[str, Any]] = []

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        self.calls.append({"pass_name": pass_name, "payload": payload})
        if self.mode == "ERROR":
            raise RuntimeError("fixture supervisor unavailable")
        if pass_name != "RESEARCH_SUPERVISOR_REVIEW":
            raise AssertionError(pass_name)
        gap_mode = self.mode == "GAP"
        parser_mode = self.mode == "PARSER"
        absence_mode = self.mode == "ABSENCE"
        force_ready = self.mode == "FORCE_READY"
        score_disagreement_components = set(
            (payload.get("required_output_rosters") or {}).get(
                "material_score_disagreement_component_ids"
            )
            or ()
        )
        structured_payload = payload.get("structured_result") or {}
        structured_complete = bool(
            structured_payload.get("status") == "COMPLETE"
            and structured_payload.get("records")
        )
        findings = []
        for index, component_id in enumerate(CANONICAL_COMPONENT_ORDER):
            sufficient = not (
                (gap_mode and index == 0)
                or component_id in score_disagreement_components
            )
            findings.append(
                {
                    "component_id": component_id,
                    "memo_sufficient": sufficient,
                    "missing_fact_needs": (
                        []
                        if sufficient or component_id in score_disagreement_components
                        else ["현금 전환의 지속성 원천 사실"]
                    ),
                    "rationale": (
                        "judge 허용구간 불일치가 남아 memo의 비교 설명을 다시 쓴다."
                        if component_id in score_disagreement_components
                        else "현재 memo의 사실·반증·구조화 지표를 검토했다."
                    ),
                }
            )
        assessments = []
        for failure in payload["prior_query_source_failures"]:
            reason = str(
                failure.get("failure_reason") or failure.get("reason") or ""
            ).upper()
            if parser_mode or "PARSER" in reason:
                classification = "PARSER_EXTRACTOR_FAILURE"
                retryable = True
                absence_allowed = False
            elif absence_mode or (force_ready and "NO_RESULT" in reason):
                classification = "SOURCE_ABSENCE_CANDIDATE"
                retryable = False
                absence_allowed = True
            elif "NO_RESULT" in reason:
                classification = "INSUFFICIENT_SEARCH"
                retryable = True
                absence_allowed = False
            else:
                classification = "IRRELEVANT_DOCUMENT"
                retryable = False
                absence_allowed = False
            assessments.append(
                {
                    "failure_id": failure["failure_id"],
                    "classification": classification,
                    "rationale": "실패 원인과 재처리 가능성을 원문 상태로 구분했다.",
                    "retryable": retryable,
                    "source_absence_claim_allowed": absence_allowed,
                }
            )
        operational_gap = bool(
            gap_mode
            or parser_mode
            or absence_mode
            or score_disagreement_components
        )
        ready = bool(
            (
                self.mode == "READY"
                and structured_complete
                and not assessments
                and not score_disagreement_components
            )
            or force_ready
        )
        missing_facts = (
            [
                {
                    "component_id": CANONICAL_COMPONENT_ORDER[0],
                    "fact_need": "현금 전환의 지속성 원천 사실",
                    "why_material": "EPS 성장과 FCF 전환의 차이를 바꾼다.",
                    "direction": "POSITIVE",
                }
            ]
            if gap_mode
            else []
        )
        source_directions = (
            [
                {
                    "objective_id": OBJECTIVE_ID,
                    "source_family": "ISSUER_PRESENTATION",
                    "direction": "미확인 현금 전환 근거를 다른 공식 원문 계열에서 확인",
                    "rationale": "기존 문서에는 현금 전환 조건이 없다.",
                    "counter_or_supersession": False,
                }
            ]
            if gap_mode
            else []
        )
        query_directions = (
            [
                {
                    "objective_id": OBJECTIVE_ID,
                    "research_need": "현금 전환의 기간과 취소 조건 확인",
                    "avoid_repeating": ["이미 실패한 일반 요약 문서 방향"],
                    "counter_or_supersession": False,
                }
            ]
            if gap_mode
            else []
        )
        unresolved = (
            ["현금 전환의 지속성 원천 사실이 확인되지 않음"]
            if gap_mode
            else ["파서 재처리가 끝나지 않음"]
            if parser_mode
            else ["source absence 판단을 독립 검토해야 함"]
            if absence_mode
            else []
        )
        if not structured_complete and not force_ready:
            unresolved.append("필수 structured data가 비어 있음")
        if score_disagreement_components:
            unresolved.append(
                "독립 judge 허용구간 불일치를 component memo 재작성으로 해소해야 함"
            )
        next_actions = (
            []
            if ready
            else [
                "실패 사유와 미해결 fact를 다음 LLM 조사 epoch에 되돌린다."
            ]
        )
        return {
            "component_findings": findings,
            "missing_material_facts": missing_facts,
            "failure_assessments": assessments,
            "new_source_family_directions": source_directions,
            "query_direction_briefs": query_directions,
            "unresolved_material_questions": unresolved,
            "next_actions": next_actions,
            "counter_and_supersession_checked": ready,
            "structured_data_complete": (
                True if force_ready else structured_complete
            ),
            "component_memos_sufficient": not (
                gap_mode or score_disagreement_components
            ),
            "reasonable_positive_routes_remaining": not ready,
            "ready_for_independent_saturation_review": ready,
            "rationale": (
                "모든 합리적 조사 방향을 검토했다."
                if ready
                else "아직 semantic research gap이 남아 있다."
            ),
        }


class Phase87CorrectingSupervisorProvider(Phase87SupervisorProvider):
    def __init__(self, invalid_kind: str) -> None:
        super().__init__("READY")
        self.invalid_kind = invalid_kind
        self.invalidations: list[str] = []

    def invalidate_last_response_cache(self, reason: str) -> None:
        self.invalidations.append(reason)

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        response = dict(super().complete(pass_name=pass_name, payload=payload))
        if len(self.calls) == 1:
            if self.invalid_kind == "UNKNOWN_OBJECTIVE":
                response["new_source_family_directions"] = [
                    {
                        "objective_id": "OBJ-INVENTED",
                        "source_family": "ISSUER_PRESENTATION",
                        "direction": "허용되지 않은 목적을 참조한 잘못된 방향",
                        "rationale": "검증 재시도 fixture",
                        "counter_or_supersession": False,
                    }
                ]
            elif self.invalid_kind == "MISSING_FAILURE_GROUP":
                response["failure_assessments"] = response[
                    "failure_assessments"
                ][:-1]
            elif self.invalid_kind == "SOURCE_ABSENCE_WITHOUT_PROOF":
                response["failure_assessments"][0].update(
                    {
                        "classification": "SOURCE_ABSENCE_CANDIDATE",
                        "retryable": False,
                        "source_absence_claim_allowed": True,
                    }
                )
            elif self.invalid_kind == "ABSENCE_PERMISSION_CLASS_MISMATCH":
                response["failure_assessments"][0].update(
                    {
                        "classification": "PARSER_EXTRACTOR_FAILURE",
                        "retryable": True,
                        "source_absence_claim_allowed": True,
                    }
                )
            return response
        context = payload["supervisor_validation_retry_context"]
        if self.invalid_kind == "COUNTER_WITHOUT_PROOF":
            response.update(
                {
                    "counter_and_supersession_checked": False,
                    "reasonable_positive_routes_remaining": True,
                    "ready_for_independent_saturation_review": False,
                    "next_actions": [
                        "counter 및 supersession 실행 근거를 추가 조사한다."
                    ],
                    "rationale": "route proof가 없어 완료 상태를 교정했다.",
                }
            )
        if not context["allowed_objective_ids"]:
            raise AssertionError("retry context lost allowed objective ids")
        return response


class Phase87SaturationProvider:
    def __init__(self, name: str, *, unresolved: bool = False) -> None:
        self.provider_name = name
        self.unresolved = unresolved
        self.calls: list[Mapping[str, Any]] = []

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        if pass_name != "SEMANTIC_SATURATION_REVIEW":
            raise AssertionError(pass_name)
        response = {
            "approve": not self.unresolved,
            "seven_component_memos_complete": True,
            "material_positive_routes_reviewed": True,
            "counter_and_supersession_routes_checked": True,
            "structured_data_complete": True,
            "new_source_family_directions_reviewed": True,
            "reasonable_positive_routes_remaining": self.unresolved,
            "unresolved_material_questions": (
                ["독립 검토에서 추가 positive route가 발견됨"]
                if self.unresolved
                else []
            ),
            "rationale": "현재 checkpoint만 보고 독립적으로 completeness를 검토했다.",
        }
        self.calls.append(
            {
                "pass_name": pass_name,
                "payload": payload,
                "prompt_hash": _stable_test_hash(payload),
                "response": response,
                "status": "COMPLETE",
            }
        )
        return response

    def validated_request_payload(
        self,
        *,
        pass_name: str,
        prompt_hash: str,
    ) -> Mapping[str, Any] | None:
        matches = [
            row["payload"]
            for row in self.calls
            if row.get("pass_name") == pass_name
            and row.get("status") == "COMPLETE"
            and _stable_test_hash(row.get("payload")) == prompt_hash
        ]
        return dict(matches[0]) if len(matches) == 1 else None

    def validated_pending_request_payload(
        self,
        *,
        pass_name: str,
        prompt_hash: str,
    ) -> Mapping[str, Any] | None:
        matches = [
            row["payload"]
            for row in self.calls
            if row.get("pass_name") == pass_name
            and _stable_test_hash(row.get("payload")) == prompt_hash
        ]
        return dict(matches[0]) if len(matches) == 1 else None


class Phase87PendingSaturationProvider(Phase87SaturationProvider):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.transport_pending = True

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        if not self.transport_pending:
            return super().complete(pass_name=pass_name, payload=payload)
        self.calls.append({"pass_name": pass_name, "payload": payload})
        prompt_hash = _stable_test_hash(payload)
        raise StructuredProviderUnavailable(
            "COLLABORATION_RESPONSE_PENDING:"
            f"COLLABREQ-{prompt_hash}"
        )


class E2RV5SemanticResearchSaturationTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_phase87_audit_is_reproducible_and_complete(self) -> None:
        actual = compile_phase87_semantic_research_saturation_audit(self.ROOT)
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_semantic_research_saturation_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, committed)
        self.assertEqual(actual["status"], PHASE87_PASS)
        self.assertEqual(actual["critical_count_sum"], 0)
        self.assertFalse(actual["fixed_round_completion_allowed"])
        self.assertFalse(actual["zero_search_result_certifies_saturation"])

    def test_provider_schemas_are_closed_and_have_no_score_or_stage(self) -> None:
        forbidden = {"score", "total_score", "stage", "final_stage"}
        for schema in (
            RESEARCH_SUPERVISOR_SCHEMA,
            SEMANTIC_SATURATION_REVIEW_SCHEMA,
        ):
            self.assertIs(schema["additionalProperties"], False)
            self.assertFalse(forbidden & set(schema["properties"]))

    def test_epoch_runner_has_no_fixed_max_rounds_parameter(self) -> None:
        signature = inspect.signature(ResearchEpochRunner.run_epoch)
        self.assertNotIn("max_rounds", signature.parameters)

    def test_complete_epoch_needs_three_provider_backed_independent_reviews(self) -> None:
        supervisor_provider = Phase87SupervisorProvider("READY")
        reviewers = tuple(
            SemanticSaturationReviewer(
                reviewer_role=role,
                provider=Phase87SaturationProvider(f"PROVIDER-{index}"),
            )
            for index, role in enumerate(SATURATION_REVIEW_ROLES)
        )
        run = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=supervisor_provider),
            saturation_reviewers=reviewers,
        ).run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        self.assertEqual(run.checkpoint.status, "SEMANTIC_SATURATION_CERTIFIED")
        self.assertTrue(run.checkpoint.semantic_saturation_certified)
        self.assertEqual(
            run.checkpoint.gold_evaluation_status,
            GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
        )
        self.assertIsNone(run.checkpoint.gold_critical_fact_miss_count)
        self.assertIsNotNone(run.saturation_certificate)
        self.assertEqual(
            set(run.saturation_certificate.reviewer_roles),  # type: ignore[union-attr]
            set(SATURATION_REVIEW_ROLES),
        )
        self.assertEqual(len(run.saturation_reviewer_results), 3)
        self.assertTrue(
            all(row.review and row.review.provider_backed for row in run.saturation_reviewer_results)
        )
        self.assertEqual(run.checkpoint.next_actions, ())
        synthesis_memo = _synthesis().memo
        assert synthesis_memo is not None
        expected_hash = _stable_test_hash(synthesis_memo.to_dict())
        self.assertEqual(
            run.supervisor_review.synthesis_memo_id,
            synthesis_memo.memo_id,
        )
        self.assertEqual(
            run.supervisor_review.synthesis_memo_hash,
            expected_hash,
        )
        checkpoint_supervisor = run.checkpoint.supervisor_review
        self.assertEqual(
            checkpoint_supervisor["synthesis_memo_hash"],
            expected_hash,
        )
        for reviewer in reviewers:
            payload = reviewer.provider.calls[-1]["payload"]
            projected_checkpoint = payload["research_epoch_checkpoint"]
            self.assertEqual(
                projected_checkpoint["gold_evaluation_status"],
                GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
            )
            self.assertNotIn(
                "gold_critical_fact_miss_count",
                projected_checkpoint,
            )
            projected_supervisor = payload["supervisor_review"]
            self.assertEqual(
                projected_supervisor["current_review_binding"][
                    "synthesis_memo_hash"
                ],
                expected_hash,
            )
            self.assertEqual(
                projected_supervisor["current_review_binding"]["review_id"],
                run.supervisor_review.review_id,
            )
            self.assertEqual(
                payload["current_evidence_fact_graph"]["record_count"],
                len(_route_facts()),
            )
            self.assertEqual(
                payload["source_graph_checkpoint"][
                    "current_checkpoint_binding"
                ]["checkpoint_id"],
                run.checkpoint.source_graph_checkpoint_id,
            )
        self.assertEqual(
            run.saturation_certificate.checkpoint_id,  # type: ignore[union-attr]
            run.checkpoint.checkpoint_id,
        )
        self.assertEqual(
            run.saturation_certificate.gold_evaluation_status,  # type: ignore[union-attr]
            GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
        )
        self.assertIsNone(
            run.saturation_certificate.gold_critical_fact_miss_count  # type: ignore[union-attr]
        )
        self.assertTrue(_production_semantic_saturation_certified(run))

    def test_certified_checkpoint_is_reused_for_unchanged_downstream_retry(
        self,
    ) -> None:
        supervisor_provider = Phase87SupervisorProvider("READY")
        saturation_providers = tuple(
            Phase87SaturationProvider(f"CERTIFIED-REUSE-{index}")
            for index in range(len(SATURATION_REVIEW_ROLES))
        )
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=supervisor_provider),
            saturation_reviewers=tuple(
                SemanticSaturationReviewer(
                    reviewer_role=role,
                    provider=provider,
                )
                for role, provider in zip(
                    SATURATION_REVIEW_ROLES,
                    saturation_providers,
                )
            ),
        )
        source_checkpoint = _source_checkpoint()
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=source_checkpoint)
        )
        supervisor_call_count = len(supervisor_provider.calls)
        saturation_call_counts = tuple(
            len(provider.calls) for provider in saturation_providers
        )
        lineage_advanced_source = _source_checkpoint_with_updates(
            source_checkpoint,
            epoch=int(source_checkpoint["epoch"]) + 1,
            resumed_from_checkpoint_id=source_checkpoint["checkpoint_id"],
        )

        resumed = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=lineage_advanced_source,
                prior_checkpoint=first.checkpoint,
            )
        )

        self.assertEqual(
            resumed.checkpoint.to_dict(),
            first.checkpoint.to_dict(),
        )
        self.assertEqual(
            resumed.supervisor_review.to_dict(),
            first.supervisor_review.to_dict(),
        )
        self.assertEqual(
            tuple(row.to_dict() for row in resumed.saturation_reviewer_results),
            tuple(row.to_dict() for row in first.saturation_reviewer_results),
        )
        self.assertEqual(
            resumed.saturation_certificate.to_dict(),  # type: ignore[union-attr]
            first.saturation_certificate.to_dict(),  # type: ignore[union-attr]
        )
        self.assertEqual(len(supervisor_provider.calls), supervisor_call_count)
        self.assertEqual(
            tuple(len(provider.calls) for provider in saturation_providers),
            saturation_call_counts,
        )

    def test_epoch_two_certification_reuses_exact_epoch_one_gap_projection(
        self,
    ) -> None:
        supervisor_provider = Phase87SupervisorProvider("GAP")
        saturation_providers = tuple(
            Phase87SaturationProvider(f"EPOCH-TWO-REUSE-{index}")
            for index in range(len(SATURATION_REVIEW_ROLES))
        )
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=supervisor_provider),
            saturation_reviewers=tuple(
                SemanticSaturationReviewer(
                    reviewer_role=role,
                    provider=provider,
                )
                for role, provider in zip(
                    SATURATION_REVIEW_ROLES,
                    saturation_providers,
                )
            ),
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        self.assertEqual(first.checkpoint.epoch, 1)
        self.assertEqual(first.checkpoint.status, "NEXT_RESEARCH_REQUIRED")

        supervisor_provider.mode = "READY"
        second = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                prior_checkpoint=first.checkpoint,
            )
        )
        self.assertEqual(second.checkpoint.epoch, 2)
        self.assertTrue(second.checkpoint.semantic_saturation_certified)
        self.assertEqual(
            second.supervisor_review.schema_version,
            "e2r_research_supervisor_review_v3",
        )
        self.assertEqual(
            second.supervisor_review.prior_review_prompt_projection,
            supervisor_provider.calls[1]["payload"][
                "prior_supervisor_review"
            ],
        )
        supervisor_call_count = len(supervisor_provider.calls)
        saturation_call_counts = tuple(
            len(provider.calls) for provider in saturation_providers
        )

        reused = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                prior_checkpoint=second.checkpoint,
            )
        )

        self.assertEqual(reused.checkpoint.to_dict(), second.checkpoint.to_dict())
        self.assertEqual(len(supervisor_provider.calls), supervisor_call_count)
        self.assertEqual(
            tuple(len(provider.calls) for provider in saturation_providers),
            saturation_call_counts,
        )

    def test_legacy_v2_epoch_two_reuse_recovers_prior_projection_from_provider_receipt(
        self,
    ) -> None:
        class RecoveringSupervisorProvider(Phase87SupervisorProvider):
            def validated_request_payload(
                self,
                *,
                pass_name: str,
                prompt_hash: str,
            ) -> Mapping[str, Any] | None:
                if pass_name != "RESEARCH_SUPERVISOR_REVIEW":
                    return None
                matches = [
                    row["payload"]
                    for row in self.calls
                    if _stable_test_hash(row["payload"]) == prompt_hash
                ]
                return dict(matches[0]) if len(matches) == 1 else None

        class LegacyV2Supervisor(ResearchSupervisor):
            def review_epoch(self, **kwargs: Any) -> ResearchSupervisorReview:
                review = super().review_epoch(**kwargs)
                if (
                    review.epoch > 1
                    and review.ready_for_independent_saturation_review
                ):
                    return replace(
                        review,
                        prior_review_prompt_projection=None,
                        schema_version="e2r_research_supervisor_review_v2",
                    )
                return review

        supervisor_provider = RecoveringSupervisorProvider("GAP")
        saturation_providers = tuple(
            Phase87SaturationProvider(f"LEGACY-V2-REUSE-{index}")
            for index in range(len(SATURATION_REVIEW_ROLES))
        )
        runner = ResearchEpochRunner(
            supervisor=LegacyV2Supervisor(provider=supervisor_provider),
            saturation_reviewers=tuple(
                SemanticSaturationReviewer(
                    reviewer_role=role,
                    provider=provider,
                )
                for role, provider in zip(
                    SATURATION_REVIEW_ROLES,
                    saturation_providers,
                )
            ),
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        supervisor_provider.mode = "READY"
        second = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                prior_checkpoint=first.checkpoint,
            )
        )
        self.assertTrue(second.checkpoint.semantic_saturation_certified)
        self.assertEqual(
            second.supervisor_review.schema_version,
            "e2r_research_supervisor_review_v2",
        )
        self.assertNotIn(
            "prior_review_prompt_projection",
            second.checkpoint.supervisor_review,
        )
        replay_state = _preliminary_saturation_state(
            prior=second.checkpoint,
            supervisor_review=second.supervisor_review,
        )
        self.assertIsNotNone(replay_state)
        replay_inputs = _epoch_inputs(
            source_checkpoint=_source_checkpoint()
        )
        rebuilt_prompt_hashes = []
        for reviewer in runner.saturation_reviewers:
            rebuilt_prompt_hashes.append(
                reviewer.preview_prompt_hash(
                    checkpoint=replay_state,  # type: ignore[arg-type]
                    supervisor_review=second.supervisor_review,
                    component_results=replay_inputs["component_results"],
                    red_team_result=replay_inputs["red_team_result"],
                    structured_result=replay_inputs["structured_result"],
                    evidence_facts=replay_inputs["evidence_facts"],
                    source_graph_checkpoint=replay_inputs[
                        "source_graph_checkpoint"
                    ],
                )
            )
        self.assertEqual(
            tuple(rebuilt_prompt_hashes),
            tuple(
                result.prompt_hash
                for result in second.saturation_reviewer_results
            ),
        )
        for provider in saturation_providers:
            self.assertEqual(
                provider.calls[-1]["payload"]["supervisor_review"][
                    "excluded_checkpoint_lineage_fields"
                ],
                ["review_id", "epoch", "prompt_hash"],
            )
        supervisor_call_count = len(supervisor_provider.calls)
        saturation_call_counts = tuple(
            len(provider.calls) for provider in saturation_providers
        )

        reused = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                prior_checkpoint=second.checkpoint,
            )
        )

        self.assertEqual(reused.checkpoint.to_dict(), second.checkpoint.to_dict())
        self.assertEqual(len(supervisor_provider.calls), supervisor_call_count)
        self.assertEqual(
            tuple(len(provider.calls) for provider in saturation_providers),
            saturation_call_counts,
        )

    def test_legacy_v2_certified_reuse_requires_valid_supervisor_response_material(
        self,
    ) -> None:
        class ResponseBoundRecoveringSupervisorProvider(
            Phase87SupervisorProvider
        ):
            response_material_state = "VALID"

            def validated_request_payload(
                self,
                *,
                pass_name: str,
                prompt_hash: str,
            ) -> Mapping[str, Any] | None:
                if (
                    pass_name != "RESEARCH_SUPERVISOR_REVIEW"
                    or self.response_material_state != "VALID"
                ):
                    return None
                matches = [
                    row["payload"]
                    for row in self.calls
                    if _stable_test_hash(row["payload"]) == prompt_hash
                ]
                return dict(matches[0]) if len(matches) == 1 else None

            def validated_pending_request_payload(
                self,
                *,
                pass_name: str,
                prompt_hash: str,
            ) -> Mapping[str, Any] | None:
                matches = [
                    row["payload"]
                    for row in self.calls
                    if pass_name == "RESEARCH_SUPERVISOR_REVIEW"
                    and _stable_test_hash(row["payload"]) == prompt_hash
                ]
                return dict(matches[0]) if len(matches) == 1 else None

        class LegacyV2Supervisor(ResearchSupervisor):
            def review_epoch(self, **kwargs: Any) -> ResearchSupervisorReview:
                review = super().review_epoch(**kwargs)
                if (
                    review.epoch > 1
                    and review.ready_for_independent_saturation_review
                ):
                    return replace(
                        review,
                        prior_review_prompt_projection=None,
                        schema_version="e2r_research_supervisor_review_v2",
                    )
                return review

        for response_material_state in (
            "RESPONSE_DELETED",
            "RESPONSE_TAMPERED",
            "RESPONSE_QUARANTINED",
        ):
            with self.subTest(
                response_material_state=response_material_state
            ):
                supervisor_provider = (
                    ResponseBoundRecoveringSupervisorProvider("GAP")
                )
                saturation_providers = tuple(
                    Phase87SaturationProvider(
                        f"LEGACY-RESPONSE-REQUIRED-"
                        f"{response_material_state}-{index}"
                    )
                    for index in range(len(SATURATION_REVIEW_ROLES))
                )
                runner = ResearchEpochRunner(
                    supervisor=LegacyV2Supervisor(
                        provider=supervisor_provider
                    ),
                    saturation_reviewers=tuple(
                        SemanticSaturationReviewer(
                            reviewer_role=role,
                            provider=provider,
                        )
                        for role, provider in zip(
                            SATURATION_REVIEW_ROLES,
                            saturation_providers,
                        )
                    ),
                )
                first = runner.run_epoch(
                    **_epoch_inputs(source_checkpoint=_source_checkpoint())
                )
                supervisor_provider.mode = "READY"
                certified = runner.run_epoch(
                    **_epoch_inputs(
                        source_checkpoint=_source_checkpoint(),
                        prior_checkpoint=first.checkpoint,
                    )
                )
                self.assertTrue(
                    certified.checkpoint.semantic_saturation_certified
                )
                self.assertEqual(
                    certified.supervisor_review.schema_version,
                    "e2r_research_supervisor_review_v2",
                )
                supervisor_call_count = len(supervisor_provider.calls)
                saturation_call_counts = tuple(
                    len(provider.calls) for provider in saturation_providers
                )
                supervisor_provider.response_material_state = (
                    response_material_state
                )

                resumed = runner.run_epoch(
                    **_epoch_inputs(
                        source_checkpoint=_source_checkpoint(),
                        prior_checkpoint=certified.checkpoint,
                    )
                )

                self.assertNotEqual(
                    resumed.checkpoint.checkpoint_id,
                    certified.checkpoint.checkpoint_id,
                )
                self.assertEqual(
                    resumed.checkpoint.epoch,
                    certified.checkpoint.epoch + 1,
                )
                self.assertEqual(
                    len(supervisor_provider.calls),
                    supervisor_call_count + 1,
                )
                self.assertEqual(
                    tuple(
                        len(provider.calls)
                        for provider in saturation_providers
                    ),
                    tuple(count + 1 for count in saturation_call_counts),
                )

    def test_certified_checkpoint_opens_new_epoch_on_bound_input_change(
        self,
    ) -> None:
        cases = (
            "fact",
            "source",
            "component",
            "red_team",
            "synthesis",
            "structured",
            "judge",
            "open_objectives",
            "prior_failures",
            "counter_route_proof",
        )
        for label in cases:
            with self.subTest(label=label):
                supervisor_provider = Phase87SupervisorProvider("READY")
                saturation_providers = tuple(
                    Phase87SaturationProvider(
                        f"CERTIFIED-CHANGED-{label}-{index}"
                    )
                    for index in range(len(SATURATION_REVIEW_ROLES))
                )
                runner = ResearchEpochRunner(
                    supervisor=ResearchSupervisor(
                        provider=supervisor_provider
                    ),
                    saturation_reviewers=tuple(
                        SemanticSaturationReviewer(
                            reviewer_role=role,
                            provider=provider,
                        )
                        for role, provider in zip(
                            SATURATION_REVIEW_ROLES,
                            saturation_providers,
                        )
                    ),
                )
                first = runner.run_epoch(
                    **_epoch_inputs(source_checkpoint=_source_checkpoint())
                )
                resumed_inputs = dict(
                    _epoch_inputs(
                        source_checkpoint=_source_checkpoint(),
                        prior_checkpoint=first.checkpoint,
                    )
                )
                if label == "fact":
                    resumed_inputs["evidence_facts"] = (
                        replace(
                            _fact("FACT-1"),
                            economic_mechanism=(
                                "changed certified cash conversion mechanism"
                            ),
                        ),
                        *_route_facts()[1:],
                    )
                elif label == "source":
                    resumed_inputs["source_graph_checkpoint"] = (
                        _source_checkpoint(extra_epoch=True)
                    )
                elif label == "component":
                    components = _components(summary_suffix="certified-v2")
                    resumed_inputs["component_results"] = components
                    resumed_inputs["synthesis_result"] = _synthesis(components)
                elif label == "red_team":
                    red_team = _red_team()
                    assert red_team.memo is not None
                    red_team = replace(
                        red_team,
                        memo=replace(red_team.memo, confidence=0.7),
                    )
                    resumed_inputs["red_team_result"] = red_team
                    resumed_inputs["synthesis_result"] = _synthesis(
                        resumed_inputs["component_results"],
                        red_team_result=red_team,
                    )
                elif label == "synthesis":
                    resumed_inputs["synthesis_result"] = _synthesis(
                        resumed_inputs["component_results"],
                        memo_id="SYNTHESIS-MEMO-certified-v2",
                        red_team_result=resumed_inputs["red_team_result"],
                    )
                elif label == "structured":
                    structured = _structured()
                    resumed_inputs["structured_result"] = replace(
                        structured,
                        records=(
                            replace(structured.records[0], value=121.0),
                        ),
                    )
                elif label == "judge":
                    resumed_inputs["score_gap_context"] = {
                        "component_research_requests": [
                            {
                                "component_id": (
                                    CANONICAL_COMPONENT_ORDER[0]
                                ),
                                "reason_codes": [
                                    "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT"
                                ],
                            }
                        ]
                    }
                elif label == "open_objectives":
                    objective = dict(_objective())
                    objective["research_objective"] = (
                        "변경된 현재 earnings와 cash conversion 검토"
                    )
                    resumed_inputs["open_objectives"] = (objective,)
                elif label == "prior_failures":
                    resumed_inputs["prior_failures"] = (
                        {
                            "failure_id": "FAIL-CERTIFIED-REUSE-CHANGED",
                            "failure_reason": "NEW_UNREADABLE_FULL_DOCUMENT",
                        },
                    )
                elif label == "counter_route_proof":
                    proof = [dict(row) for row in _counter_proof()]
                    proof[0]["parser_extractor_verified"] = False
                    resumed_inputs[
                        "counter_and_supersession_route_proof"
                    ] = tuple(proof)

                resumed = runner.run_epoch(**resumed_inputs)

                self.assertEqual(resumed.checkpoint.epoch, 2)
                self.assertNotEqual(
                    resumed.checkpoint.checkpoint_id,
                    first.checkpoint.checkpoint_id,
                )
                self.assertEqual(
                    len(supervisor_provider.calls),
                    3 if label == "counter_route_proof" else 2,
                )

    def test_certified_checkpoint_fails_closed_on_review_provider_tamper(
        self,
    ) -> None:
        supervisor_provider = Phase87SupervisorProvider("READY")
        saturation_providers = tuple(
            Phase87SaturationProvider(f"CERTIFIED-TAMPER-{index}")
            for index in range(len(SATURATION_REVIEW_ROLES))
        )
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=supervisor_provider),
            saturation_reviewers=tuple(
                SemanticSaturationReviewer(
                    reviewer_role=role,
                    provider=provider,
                )
                for role, provider in zip(
                    SATURATION_REVIEW_ROLES,
                    saturation_providers,
                )
            ),
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        tampered = dict(first.checkpoint.to_dict())
        reviews = [dict(row) for row in tampered["saturation_reviews"]]
        reviews[0]["provider_name"] = "FORGED-SATURATION-PROVIDER"
        reviews[0]["review"] = {
            **dict(reviews[0]["review"]),
            "provider_name": "FORGED-SATURATION-PROVIDER",
        }
        tampered["saturation_reviews"] = reviews
        tampered["checkpoint_hash"] = _research_checkpoint_hash(tampered)

        resumed = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                prior_checkpoint=tampered,
            )
        )

        self.assertEqual(resumed.checkpoint.epoch, 2)
        self.assertNotEqual(
            resumed.checkpoint.checkpoint_id,
            first.checkpoint.checkpoint_id,
        )
        self.assertEqual(len(supervisor_provider.calls), 2)
        self.assertEqual(
            tuple(len(provider.calls) for provider in saturation_providers),
            (2, 2, 2),
        )

    def test_certified_checkpoint_fails_closed_on_certificate_lineage_tamper(
        self,
    ) -> None:
        cases = ("certificate_id", "review_id", "prompt_hash")
        for label in cases:
            with self.subTest(label=label):
                supervisor_provider = Phase87SupervisorProvider("READY")
                saturation_providers = tuple(
                    Phase87SaturationProvider(
                        f"CERTIFIED-LINEAGE-{label}-{index}"
                    )
                    for index in range(len(SATURATION_REVIEW_ROLES))
                )
                runner = ResearchEpochRunner(
                    supervisor=ResearchSupervisor(
                        provider=supervisor_provider
                    ),
                    saturation_reviewers=tuple(
                        SemanticSaturationReviewer(
                            reviewer_role=role,
                            provider=provider,
                        )
                        for role, provider in zip(
                            SATURATION_REVIEW_ROLES,
                            saturation_providers,
                        )
                    ),
                )
                first = runner.run_epoch(
                    **_epoch_inputs(source_checkpoint=_source_checkpoint())
                )
                tampered = dict(first.checkpoint.to_dict())
                reviews = [
                    dict(row) for row in tampered["saturation_reviews"]
                ]
                certificate = dict(tampered["saturation_certificate"])
                if label == "certificate_id":
                    certificate["certificate_id"] = "SATCERT-FORGED"
                elif label == "review_id":
                    old_review_id = str(
                        reviews[0]["review"]["review_id"]
                    )
                    forged_review_id = "SATREVIEW-FORGED"
                    reviews[0]["review"] = {
                        **dict(reviews[0]["review"]),
                        "review_id": forged_review_id,
                    }
                    certificate["review_ids"] = [
                        forged_review_id
                        if value == old_review_id
                        else value
                        for value in certificate["review_ids"]
                    ]
                elif label == "prompt_hash":
                    old_prompt_hash = str(reviews[0]["prompt_hash"])
                    forged_prompt_hash = "f" * 64
                    reviews[0]["prompt_hash"] = forged_prompt_hash
                    reviews[0]["review"] = {
                        **dict(reviews[0]["review"]),
                        "prompt_hash": forged_prompt_hash,
                    }
                    certificate["provider_prompt_hashes"] = [
                        forged_prompt_hash
                        if value == old_prompt_hash
                        else value
                        for value in certificate["provider_prompt_hashes"]
                    ]
                tampered["saturation_reviews"] = reviews
                tampered["saturation_certificate"] = certificate
                tampered["checkpoint_hash"] = _research_checkpoint_hash(
                    tampered
                )

                resumed = runner.run_epoch(
                    **_epoch_inputs(
                        source_checkpoint=_source_checkpoint(),
                        prior_checkpoint=tampered,
                    )
                )

                self.assertEqual(resumed.checkpoint.epoch, 2)
                self.assertNotEqual(
                    resumed.checkpoint.checkpoint_id,
                    first.checkpoint.checkpoint_id,
                )
                self.assertEqual(len(supervisor_provider.calls), 2)

    def test_self_consistent_forged_certificate_without_provider_receipts_is_not_reused(
        self,
    ) -> None:
        original_supervisor = Phase87SupervisorProvider("READY")
        original_saturation = tuple(
            Phase87SaturationProvider(f"FORGED-RECEIPT-{index}")
            for index in range(len(SATURATION_REVIEW_ROLES))
        )
        first = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=original_supervisor),
            saturation_reviewers=tuple(
                SemanticSaturationReviewer(
                    reviewer_role=role,
                    provider=provider,
                )
                for role, provider in zip(
                    SATURATION_REVIEW_ROLES,
                    original_saturation,
                )
            ),
        ).run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )

        forged_reviews = []
        forged_results = []
        for result in first.saturation_reviewer_results:
            assert result.review is not None
            response = {
                "approve": True,
                "seven_component_memos_complete": True,
                "material_positive_routes_reviewed": True,
                "counter_and_supersession_routes_checked": True,
                "structured_data_complete": True,
                "new_source_family_directions_reviewed": True,
                "reasonable_positive_routes_remaining": False,
                "unresolved_material_questions": [],
                "rationale": "provider 호출 없이 만든 self-consistent 승인",
            }
            review_id = stable_intelligence_id(
                "SATREVIEW",
                {
                    "reviewer_role": result.reviewer_role,
                    "checkpoint_id": first.checkpoint.checkpoint_id,
                    "epoch": first.checkpoint.epoch,
                    "response": response,
                    "prompt_hash": result.prompt_hash,
                },
            )
            review = replace(
                result.review,
                review_id=review_id,
                rationale=response["rationale"],
            )
            forged_reviews.append(review)
            forged_result = dict(result.to_dict())
            forged_result.pop("provider_response_identity", None)
            forged_result["review"] = review.to_dict()
            forged_results.append(forged_result)
        forged_certificate = SemanticSaturationCertifier().certify(
            forged_reviews,
            expected_checkpoint_id=first.checkpoint.checkpoint_id,
            require_provider_reviews=True,
        )
        forged = dict(first.checkpoint.to_dict())
        forged["saturation_reviews"] = forged_results
        forged["saturation_certificate"] = forged_certificate.to_dict()
        forged["checkpoint_hash"] = _research_checkpoint_hash(forged)

        resumed_supervisor = Phase87SupervisorProvider("READY")
        resumed_saturation = tuple(
            Phase87SaturationProvider(f"FORGED-RECEIPT-{index}")
            for index in range(len(SATURATION_REVIEW_ROLES))
        )
        self.assertEqual(len(resumed_supervisor.calls), 0)
        self.assertEqual(
            tuple(len(provider.calls) for provider in resumed_saturation),
            (0, 0, 0),
        )
        resumed = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=resumed_supervisor),
            saturation_reviewers=tuple(
                SemanticSaturationReviewer(
                    reviewer_role=role,
                    provider=provider,
                )
                for role, provider in zip(
                    SATURATION_REVIEW_ROLES,
                    resumed_saturation,
                )
            ),
        ).run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                prior_checkpoint=forged,
            )
        )

        self.assertEqual(resumed.checkpoint.epoch, 2)
        self.assertEqual(len(resumed_supervisor.calls), 1)
        self.assertEqual(
            tuple(len(provider.calls) for provider in resumed_saturation),
            (1, 1, 1),
        )

    def test_checkpoint_object_internal_mapping_mutation_is_rejected_at_resume(
        self,
    ) -> None:
        supervisor_provider = Phase87SupervisorProvider("READY")
        saturation_providers = tuple(
            Phase87SaturationProvider(f"OBJECT-MUTATION-{index}")
            for index in range(len(SATURATION_REVIEW_ROLES))
        )
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=supervisor_provider),
            saturation_reviewers=tuple(
                SemanticSaturationReviewer(
                    reviewer_role=role,
                    provider=provider,
                )
                for role, provider in zip(
                    SATURATION_REVIEW_ROLES,
                    saturation_providers,
                )
            ),
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        first.checkpoint.component_memo_hashes[
            CANONICAL_COMPONENT_ORDER[0]
        ] = "f" * 64

        with self.assertRaisesRegex(ValueError, "checkpoint hash mismatch"):
            runner.run_epoch(
                **_epoch_inputs(
                    source_checkpoint=_source_checkpoint(),
                    prior_checkpoint=first.checkpoint,
                )
            )

    def test_rehashed_checkpoint_with_forged_nested_v3_schema_is_rejected(
        self,
    ) -> None:
        cases = ("supervisor", "review", "certificate")
        for label in cases:
            with self.subTest(label=label):
                supervisor_provider = Phase87SupervisorProvider("READY")
                saturation_providers = tuple(
                    Phase87SaturationProvider(
                        f"NESTED-SCHEMA-{label}-{index}"
                    )
                    for index in range(len(SATURATION_REVIEW_ROLES))
                )
                runner = ResearchEpochRunner(
                    supervisor=ResearchSupervisor(
                        provider=supervisor_provider
                    ),
                    saturation_reviewers=tuple(
                        SemanticSaturationReviewer(
                            reviewer_role=role,
                            provider=provider,
                        )
                        for role, provider in zip(
                            SATURATION_REVIEW_ROLES,
                            saturation_providers,
                        )
                    ),
                )
                first = runner.run_epoch(
                    **_epoch_inputs(source_checkpoint=_source_checkpoint())
                )
                forged = dict(first.checkpoint.to_dict())
                if label == "supervisor":
                    forged["supervisor_review"] = {
                        **dict(forged["supervisor_review"]),
                        "forged_schema_field": True,
                    }
                elif label == "review":
                    results = [
                        dict(row) for row in forged["saturation_reviews"]
                    ]
                    results[0]["review"] = {
                        **dict(results[0]["review"]),
                        "forged_schema_field": True,
                    }
                    forged["saturation_reviews"] = results
                else:
                    forged["saturation_certificate"] = {
                        **dict(forged["saturation_certificate"]),
                        "forged_schema_field": True,
                    }
                forged["checkpoint_hash"] = _research_checkpoint_hash(
                    forged
                )

                with self.assertRaisesRegex(
                    ValueError,
                    "key roster mismatch",
                ):
                    runner.run_epoch(
                        **_epoch_inputs(
                            source_checkpoint=_source_checkpoint(),
                            prior_checkpoint=forged,
                        )
                    )

    def test_self_resealed_v3_prior_review_projection_tampering_is_rejected_on_load(
        self,
    ) -> None:
        supervisor_provider = Phase87SupervisorProvider("GAP")
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=supervisor_provider),
            saturation_reviewers=(),
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        supervisor_provider.mode = "READY"
        second = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                prior_checkpoint=first.checkpoint,
            )
        )
        projection = second.checkpoint.supervisor_review[
            "prior_review_prompt_projection"
        ]
        self.assertIsInstance(projection, Mapping)

        def reseal_projection(value: Mapping[str, Any]) -> None:
            semantic = dict(value)
            semantic.pop("prior_review_semantic_hash", None)
            for key in (
                "checkpoint_lineage_excluded_from_provider",
                "excluded_checkpoint_lineage_fields",
                "full_prior_review_persisted_outside_prompt",
                "fixed_top_n_used",
                "prompt_projection_is_research_cap",
                "score_authority",
            ):
                semantic.pop(key, None)
            value["prior_review_semantic_hash"] = _stable_test_hash(semantic)  # type: ignore[index]

        cases = (
            "top_extra",
            "top_missing",
            "failure_nested_extra",
            "parser_nested_missing",
            "semantic_hash",
            "authority",
        )
        with tempfile.TemporaryDirectory() as directory:
            for label in cases:
                with self.subTest(label=label):
                    forged = json.loads(
                        json.dumps(
                            second.checkpoint.to_dict(),
                            ensure_ascii=False,
                        )
                    )
                    forged_projection = forged["supervisor_review"][
                        "prior_review_prompt_projection"
                    ]
                    if label == "top_extra":
                        forged_projection["forged_projection_field"] = True
                        reseal_projection(forged_projection)
                    elif label == "top_missing":
                        forged_projection.pop("rationale")
                        reseal_projection(forged_projection)
                    elif label == "failure_nested_extra":
                        forged_projection["failure_assessment_projection"][
                            "forged_nested_field"
                        ] = True
                        reseal_projection(forged_projection)
                    elif label == "parser_nested_missing":
                        forged_projection[
                            "parser_or_extractor_failure_projection"
                        ].pop("failure_roster_hash")
                        reseal_projection(forged_projection)
                    elif label == "semantic_hash":
                        forged_projection[
                            "prior_review_semantic_hash"
                        ] = "0" * 64
                    else:
                        forged_projection["score_authority"] = True
                    forged["checkpoint_id"] = _research_checkpoint_id(forged)
                    forged["checkpoint_hash"] = _research_checkpoint_hash(
                        forged
                    )
                    path = Path(directory) / f"{label}.json"
                    path.write_text(
                        json.dumps(forged, ensure_ascii=False),
                        encoding="utf-8",
                    )

                    with self.assertRaisesRegex(
                        ValueError,
                        "invalid nested research supervisor review",
                    ):
                        load_research_epoch_checkpoint(path)

    def test_clean_resume_consumes_exact_pending_saturation_requests_in_same_epoch(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            supervisor_provider = Phase87SupervisorProvider("READY")
            saturation_providers = tuple(
                CollaborationCodexResearcherProvider(
                    transport=CollaborationCodexSubagentTransport()
                )
                for _ in SATURATION_REVIEW_ROLES
            )
            cache_root = Path(directory) / "research_provider_response_cache"
            for provider in saturation_providers:
                provider.configure_response_cache(cache_root)
            journal_root = (
                cache_root.parent
                / "collaboration_codex_subagent_provider"
            )
            reviewers = tuple(
                SemanticSaturationReviewer(
                    reviewer_role=role,
                    provider=provider,
                )
                for role, provider in zip(
                    SATURATION_REVIEW_ROLES,
                    saturation_providers,
                )
            )
            runner = ResearchEpochRunner(
                supervisor=ResearchSupervisor(provider=supervisor_provider),
                saturation_reviewers=reviewers,
            )
            source_checkpoint = _source_checkpoint()
            first = runner.run_epoch(
                **_epoch_inputs(source_checkpoint=source_checkpoint)
            )
            first_prompt_hashes = tuple(
                row.prompt_hash for row in first.saturation_reviewer_results
            )
            request_paths = tuple(
                (journal_root / "requests").glob("COLLABREQ-*.json")
            )
            first_request_ids = {path.stem for path in request_paths}
            self.assertEqual(
                first.checkpoint.status,
                "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
            )
            self.assertEqual(len(set(first_prompt_hashes)), 3)
            self.assertEqual(len(first_request_ids), 3)
            self.assertTrue(
                all(
                    "COLLABORATION_RESPONSE_PENDING:COLLABREQ-"
                    in row.pending_reasons[0]
                    for row in first.saturation_reviewer_results
                )
            )
            response = {
                "approve": True,
                "seven_component_memos_complete": True,
                "material_positive_routes_reviewed": True,
                "counter_and_supersession_routes_checked": True,
                "structured_data_complete": True,
                "new_source_family_directions_reviewed": True,
                "reasonable_positive_routes_remaining": False,
                "unresolved_material_questions": [],
                "rationale": (
                    "현재 checkpoint만 보고 독립적으로 completeness를 검토했다."
                ),
            }
            lineage_advanced_source = _source_checkpoint_with_updates(
                source_checkpoint,
                epoch=int(source_checkpoint["epoch"]) + 1,
                resumed_from_checkpoint_id=source_checkpoint[
                    "checkpoint_id"
                ],
            )
            still_pending = runner.run_epoch(
                **_epoch_inputs(
                    source_checkpoint=lineage_advanced_source,
                    prior_checkpoint=first.checkpoint,
                )
            )
            self.assertEqual(still_pending.checkpoint.epoch, first.checkpoint.epoch)
            self.assertEqual(
                still_pending.checkpoint.checkpoint_id,
                first.checkpoint.checkpoint_id,
            )
            self.assertEqual(
                {
                    path.stem
                    for path in (journal_root / "requests").glob(
                        "COLLABREQ-*.json"
                    )
                },
                first_request_ids,
            )
            for index, request_id in enumerate(sorted(first_request_ids)):
                import_collaboration_response(
                    journal_root=journal_root,
                    request_id=request_id,
                    response_payload=response,
                    agent_id=f"clean-resume-agent-{index}",
                    canonical_task_name=f"/root/clean_resume_{index}",
                    agent_model="codex-collaboration",
                )
            resumed = runner.run_epoch(
                **_epoch_inputs(
                    source_checkpoint=lineage_advanced_source,
                    prior_checkpoint=still_pending.checkpoint,
                )
            )

            self.assertEqual(len(supervisor_provider.calls), 1)
            self.assertEqual(resumed.checkpoint.epoch, first.checkpoint.epoch)
            self.assertEqual(
                resumed.checkpoint.checkpoint_id,
                first.checkpoint.checkpoint_id,
            )
            self.assertEqual(
                tuple(
                    row.prompt_hash
                    for row in resumed.saturation_reviewer_results
                ),
                first_prompt_hashes,
            )
            self.assertEqual(
                {
                    path.stem
                    for path in (journal_root / "requests").glob(
                        "COLLABREQ-*.json"
                    )
                },
                first_request_ids,
            )
            self.assertTrue(resumed.checkpoint.semantic_saturation_certified)
            self.assertEqual(
                resumed.saturation_certificate.checkpoint_id,  # type: ignore[union-attr]
                first.checkpoint.checkpoint_id,
            )
            self.assertFalse(
                resumed.checkpoint.completion_based_on_fixed_rounds
            )
            self.assertFalse(
                resumed.checkpoint.zero_search_result_treated_as_saturation
            )
            self.assertFalse(
                resumed.checkpoint.transport_budget_treated_as_completion
            )
            provider_call_counts = tuple(
                len(provider.calls) for provider in saturation_providers
            )
            legacy_v3 = dict(resumed.checkpoint.to_dict())
            legacy_results = [
                dict(row) for row in legacy_v3["saturation_reviews"]
            ]
            for row in legacy_results:
                row.pop("provider_response_identity", None)
            legacy_v3["saturation_reviews"] = legacy_results
            legacy_v3["checkpoint_hash"] = _research_checkpoint_hash(
                legacy_v3
            )

            reused = runner.run_epoch(
                **_epoch_inputs(
                    source_checkpoint=lineage_advanced_source,
                    prior_checkpoint=legacy_v3,
                )
            )

            self.assertEqual(reused.checkpoint.epoch, resumed.checkpoint.epoch)
            self.assertEqual(len(supervisor_provider.calls), 1)
            self.assertEqual(
                tuple(
                    len(provider.calls) for provider in saturation_providers
                ),
                provider_call_counts,
            )

    def test_clean_resume_opens_new_epoch_when_bound_semantic_input_changes(
        self,
    ) -> None:
        """Facts/source/components bind positive, failure, and counter routes."""

        cases = (
            (
                "fact",
                {
                    "facts": (
                        replace(
                            _fact("FACT-1"),
                            economic_mechanism=(
                                "changed current cash conversion mechanism"
                            ),
                        ),
                        *_route_facts()[1:],
                    ),
                },
            ),
            (
                "source_graph",
                {"source_checkpoint": _source_checkpoint(extra_epoch=True)},
            ),
            (
                "component_and_synthesis",
                {"components": _components(summary_suffix="v2")},
            ),
        )
        for label, changes in cases:
            with self.subTest(label=label):
                supervisor_provider = Phase87SupervisorProvider("READY")
                saturation_providers = tuple(
                    Phase87PendingSaturationProvider(
                        f"CHANGED-{label}-{index}"
                    )
                    for index in range(len(SATURATION_REVIEW_ROLES))
                )
                runner = ResearchEpochRunner(
                    supervisor=ResearchSupervisor(
                        provider=supervisor_provider
                    ),
                    saturation_reviewers=tuple(
                        SemanticSaturationReviewer(
                            reviewer_role=role,
                            provider=provider,
                        )
                        for role, provider in zip(
                            SATURATION_REVIEW_ROLES,
                            saturation_providers,
                        )
                    ),
                )
                first = runner.run_epoch(
                    **_epoch_inputs(source_checkpoint=_source_checkpoint())
                )
                resumed_inputs = {
                    "source_checkpoint": _source_checkpoint(),
                    "prior_checkpoint": first.checkpoint,
                    **changes,
                }
                second = runner.run_epoch(**_epoch_inputs(**resumed_inputs))

                self.assertEqual(second.checkpoint.epoch, 2)
                self.assertNotEqual(
                    second.checkpoint.checkpoint_id,
                    first.checkpoint.checkpoint_id,
                )
                self.assertEqual(len(supervisor_provider.calls), 2)
                self.assertNotEqual(
                    tuple(
                        row.prompt_hash
                        for row in second.saturation_reviewer_results
                    ),
                    tuple(
                        row.prompt_hash
                        for row in first.saturation_reviewer_results
                    ),
                )

    def test_source_lineage_replay_fails_closed_on_each_semantic_leaf(
        self,
    ) -> None:
        base = _source_checkpoint()
        query_changed = [dict(row) for row in base["generated_queries"]]
        query_changed[0]["literal_query"] = (
            "changed current target counter evidence"
        )
        document_changed = [dict(row) for row in base["evidence_documents"]]
        document_changed[0]["source_family"] = "CUSTOMER_OFFICIAL"
        cases = {
            "generated_query": {"generated_queries": query_changed},
            "evidence_document": {"evidence_documents": document_changed},
            "query_failure": {
                "query_failures": [
                    {
                        "failure_id": "SGFAIL-SEMANTIC-CHANGE",
                        "query_id": "Q-COUNTER",
                        "objective_id": OBJECTIVE_ID,
                        "failure_stage": "SEARCH",
                        "failure_reason": "CHANGED_PROVIDER_FAILURE",
                        "alternate_route_required": True,
                        "absence_eligible": False,
                        "zero_result_only": False,
                    }
                ]
            },
            "resolved_objective": {
                "resolved_objective_ids": [OBJECTIVE_ID]
            },
            "terminal_status": {"status": "STOPPED_ON_RESOLUTION"},
        }
        for label, semantic_update in cases.items():
            with self.subTest(label=label):
                supervisor_provider = Phase87SupervisorProvider("READY")
                saturation_providers = tuple(
                    Phase87PendingSaturationProvider(
                        f"SEMANTIC-LEAF-{label}-{index}"
                    )
                    for index in range(len(SATURATION_REVIEW_ROLES))
                )
                runner = ResearchEpochRunner(
                    supervisor=ResearchSupervisor(
                        provider=supervisor_provider
                    ),
                    saturation_reviewers=tuple(
                        SemanticSaturationReviewer(
                            reviewer_role=role,
                            provider=provider,
                        )
                        for role, provider in zip(
                            SATURATION_REVIEW_ROLES,
                            saturation_providers,
                        )
                    ),
                )
                first = runner.run_epoch(
                    **_epoch_inputs(source_checkpoint=base)
                )
                changed = _source_checkpoint_with_updates(
                    base,
                    epoch=int(base["epoch"]) + 1,
                    resumed_from_checkpoint_id=base["checkpoint_id"],
                    **semantic_update,
                )

                resumed = runner.run_epoch(
                    **_epoch_inputs(
                        source_checkpoint=changed,
                        prior_checkpoint=first.checkpoint,
                    )
                )

                self.assertEqual(resumed.checkpoint.epoch, 2)
                self.assertNotEqual(
                    resumed.checkpoint.checkpoint_id,
                    first.checkpoint.checkpoint_id,
                )
                self.assertEqual(len(supervisor_provider.calls), 2)

    def test_clean_resume_fails_closed_on_new_material_judge_disagreement(
        self,
    ) -> None:
        supervisor_provider = Phase87SupervisorProvider("READY")
        reviewers = tuple(
            SemanticSaturationReviewer(
                reviewer_role=role,
                provider=Phase87PendingSaturationProvider(
                    f"DISAGREEMENT-{index}"
                ),
            )
            for index, role in enumerate(SATURATION_REVIEW_ROLES)
        )
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=supervisor_provider),
            saturation_reviewers=reviewers,
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        resumed_inputs = dict(
            _epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                prior_checkpoint=first.checkpoint,
            )
        )
        resumed_inputs["score_gap_context"] = {
            "component_research_requests": [
                {
                    "component_id": CANONICAL_COMPONENT_ORDER[0],
                    "reason_codes": [
                        "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT"
                    ],
                }
            ]
        }
        second = runner.run_epoch(**resumed_inputs)

        self.assertEqual(second.checkpoint.epoch, 2)
        self.assertEqual(len(supervisor_provider.calls), 2)
        self.assertEqual(
            second.checkpoint.status,
            "NEXT_RESEARCH_REQUIRED",
        )
        self.assertEqual(second.saturation_reviewer_results, ())

    def test_large_saturation_payload_is_loss_accounted_and_under_transport_contract(
        self,
    ) -> None:
        base = ResearchEpochRunner(
            supervisor=ResearchSupervisor(
                provider=Phase87SupervisorProvider("READY")
            ),
            saturation_reviewers=(),
        ).run_epoch(**_epoch_inputs(source_checkpoint=_source_checkpoint()))
        expanded_assessments = tuple(
            SupervisorFailureAssessment(
                failure_id=f"FAILURE-{index:05d}",
                classification="IRRELEVANT_DOCUMENT",
                rationale=(
                    "동일 semantic failure group이며 current objective는 "
                    "다른 source-backed facts로 해결됐다."
                ),
                retryable=False,
                source_absence_claim_allowed=False,
            )
            for index in range(3_666)
        )
        supervisor_review = replace(
            base.supervisor_review,
            failure_assessments=expanded_assessments,
        )
        facts = (
            _fact("FACT-1"),
            *(
                _fact(f"FACT-LARGE-{index:05d}")
                for index in range(7_999)
            ),
        )
        checkpoint = dict(base.checkpoint.to_dict())
        checkpoint["current_fact_ids"] = [row.fact_id for row in facts]
        checkpoint["cumulative_fact_ids"] = [row.fact_id for row in facts]
        checkpoint["new_facts"] = [row.to_dict() for row in facts]
        checkpoint["supervisor_review"] = supervisor_review.to_dict()
        checkpoint["checkpoint_hash"] = _stable_test_hash(checkpoint)

        source_checkpoint = dict(_source_checkpoint())
        source_checkpoint.update(
            {
                "generated_queries": [
                    {
                        "query_id": f"QUERY-{index:04d}",
                        "objective_id": OBJECTIVE_ID,
                        "execution_status": "SEARCH_EXECUTED",
                        "counter_or_supersession_search": bool(index % 2),
                        "search_result_count": 1,
                        "literal_query": f"generic current research route {index}",
                    }
                    for index in range(500)
                ],
                "query_failures": [
                    {
                        "failure_id": f"QFAIL-{index:04d}",
                        "query_id": f"QUERY-{index % 500:04d}",
                        "objective_id": OBJECTIVE_ID,
                        "failure_stage": "SEARCH",
                        "failure_reason": "grouped terminal route",
                        "alternate_route_required": False,
                        "absence_eligible": False,
                        "zero_result_only": False,
                    }
                    for index in range(1_800)
                ],
                "search_candidates": [
                    {
                        "candidate_id": f"CAND-{index:05d}",
                        "ranking_status": "RANKED",
                        "fetch_status": "FETCHED",
                        "candidate_source_family_hint": "ISSUER_PRESENTATION",
                        "verified_official_domain_candidate": True,
                        "objective_ids": [OBJECTIVE_ID],
                        "requested_source_families": ["ISSUER_PRESENTATION"],
                        "rank": index + 1,
                        "url": f"https://issuer.example/{index}",
                        "title": "grouped candidate",
                        "snippet": "discovery only",
                    }
                    for index in range(4_000)
                ],
                "candidate_materiality_decisions": [
                    {
                        "decision_id": f"MAT-{index:05d}",
                        "candidate_id": f"CAND-{index:05d}",
                        "material_relevance": True,
                        "evidence_eligible": True,
                        "snippet_discovery_only": False,
                        "score_authority": False,
                        "objective_ids": [OBJECTIVE_ID],
                        "priority": 1,
                        "rationale": "material current route",
                    }
                    for index in range(4_000)
                ],
                "fetch_records": [
                    {
                        "fetch_id": f"FETCH-{index:05d}",
                        "candidate_id": f"CAND-{index:05d}",
                        "disposition": "FETCHED",
                        "full_fetch_attempted": True,
                        "snippet_used_as_document": False,
                        "score_authority": False,
                        "objective_ids": [OBJECTIVE_ID],
                    }
                    for index in range(2_500)
                ],
                "rejected_documents": [
                    {
                        "rejection_id": f"REJECT-{index:05d}",
                        "candidate_id": f"CAND-{index:05d}",
                        "retryable": False,
                        "snippet_used_as_document": False,
                        "score_authority": False,
                        "objective_ids": [OBJECTIVE_ID],
                        "accepted_claim_ids": [],
                        "rejection_reason": "duplicate or superseded document",
                    }
                    for index in range(1_900)
                ],
                "evidence_documents": [
                    {
                        "document_id": f"DOC-{index:05d}",
                        "target_id": TARGET,
                        "as_of_date": AS_OF_DATE,
                        "source_family": "ISSUER_PRESENTATION",
                        "source_provider": "ISSUER",
                        "publication_date_source": "DOCUMENT",
                        "full_fetch_performed": True,
                        "snippet_only": False,
                        "evidence_eligible": True,
                        "content_hash": f"{index:064x}",
                    }
                    for index in range(1_400)
                ],
            }
        )
        source_checkpoint["checkpoint_hash"] = _stable_test_hash(
            {
                key: value
                for key, value in source_checkpoint.items()
                if key not in {"checkpoint_hash", "checkpoint_id"}
            }
        )
        checkpoint["source_graph_checkpoint_id"] = source_checkpoint[
            "checkpoint_id"
        ]

        payloads = tuple(
            _semantic_saturation_prompt_payload(
                reviewer_role=role,
                checkpoint=checkpoint,
                supervisor_review=supervisor_review,
                component_results=_components(),
                red_team_result=_red_team(),
                structured_result=_structured(),
                evidence_facts=facts,
                source_graph_checkpoint=source_checkpoint,
            )
            for role in SATURATION_REVIEW_ROLES
        )
        encoded_sizes = tuple(
            len(
                json.dumps(
                    payload,
                    ensure_ascii=False,
                    sort_keys=True,
                    default=str,
                ).encode("utf-8")
            )
            for payload in payloads
        )
        self.assertTrue(all(size < 1_000_000 for size in encoded_sizes))
        fact_projection = payloads[0]["current_evidence_fact_graph"]
        self.assertEqual(fact_projection["record_count"], 8_000)
        self.assertTrue(
            fact_projection["every_record_accounted_by_hash_and_group_count"]
        )
        self.assertFalse(fact_projection["fixed_top_n_used"])
        corroboration_review = fact_projection[
            "independent_corroboration_review"
        ]
        self.assertEqual(
            corroboration_review["review_scope"],
            "CURRENT_INFORMATION_CONFIDENCE_MEMO_FACTS",
        )
        self.assertEqual(
            corroboration_review["review_scope_requested_fact_count"],
            1,
        )
        self.assertTrue(
            corroboration_review[
                "facts_outside_current_memo_remain_accounted_in_semantic_groups"
            ]
        )
        self.assertFalse(
            corroboration_review["review_scope_uses_fixed_top_n"]
        )
        supervisor_projection = payloads[0]["supervisor_review"]
        self.assertEqual(
            supervisor_projection["failure_assessment_projection"][
                "failure_assessment_count"
            ],
            3_666,
        )
        self.assertTrue(
            supervisor_projection["failure_assessment_projection"][
                "every_assessment_accounted_by_group_count_and_hash"
            ]
        )
        source_projection = payloads[0]["source_graph_checkpoint"]
        for key, count in (
            ("generated_queries", 500),
            ("query_failures", 1_800),
            ("search_candidates", 4_000),
            ("candidate_materiality_decisions", 4_000),
            ("fetch_records", 2_500),
            ("rejected_documents", 1_900),
            ("evidence_documents", 1_400),
        ):
            self.assertEqual(source_projection[key]["record_count"], count)
            self.assertTrue(
                source_projection[key][
                    "every_record_accounted_by_hash_and_group_count"
                ]
            )
        self.assertEqual(
            payloads[0]["component_results"][0]["memo"][
                "researcher_summary"
            ],
            _components()[0].memo.researcher_summary,
        )
        self.assertEqual(
            payloads[0]["red_team_result"]["memo"]["memo_id"],
            _red_team().memo.memo_id,
        )
        self.assertEqual(
            payloads[0]["structured_result"]["status"],
            _structured().status,
        )
        prompt_hashes = tuple(_stable_test_hash(payload) for payload in payloads)
        self.assertEqual(len(set(prompt_hashes)), len(SATURATION_REVIEW_ROLES))
        reviews = tuple(
            SaturationReview(
                review_id=f"SAT-LARGE-{index}",
                reviewer_role=role,
                approve=True,
                seven_component_memos_complete=True,
                material_positive_routes_reviewed=True,
                counter_and_supersession_routes_checked=True,
                structured_data_complete=True,
                new_source_family_directions_reviewed=True,
                unresolved_material_questions=(),
                rationale="대형 loss-accounted payload를 독립적으로 검토했다.",
                checkpoint_id=str(checkpoint["checkpoint_id"]),
                epoch=int(checkpoint["epoch"]),
                provider_name=f"PROVIDER-{index}",
                prompt_hash=prompt_hashes[index],
                provider_backed=True,
            )
            for index, role in enumerate(SATURATION_REVIEW_ROLES)
        )
        certificate = SemanticSaturationCertifier().certify(
            reviews,
            expected_checkpoint_id=str(checkpoint["checkpoint_id"]),
            require_provider_reviews=True,
        )
        self.assertTrue(certificate.semantic_saturation_certified)

        mutated_facts = list(facts)
        mutated_facts[-1] = replace(mutated_facts[-1], value=False)
        mutated_payload = _semantic_saturation_prompt_payload(
            reviewer_role=SATURATION_REVIEW_ROLES[0],
            checkpoint=checkpoint,
            supervisor_review=supervisor_review,
            component_results=_components(),
            red_team_result=_red_team(),
            structured_result=_structured(),
            evidence_facts=mutated_facts,
            source_graph_checkpoint=source_checkpoint,
        )
        self.assertNotEqual(
            fact_projection["record_roster_hash"],
            mutated_payload["current_evidence_fact_graph"][
                "record_roster_hash"
            ],
        )

    def test_saturation_rejects_missing_facts_and_stale_source_before_provider(
        self,
    ) -> None:
        base = ResearchEpochRunner(
            supervisor=ResearchSupervisor(
                provider=Phase87SupervisorProvider("READY")
            ),
            saturation_reviewers=(),
        ).run_epoch(**_epoch_inputs(source_checkpoint=_source_checkpoint()))
        provider = Phase87SaturationProvider("FAIL_CLOSED")
        reviewer = SemanticSaturationReviewer(
            reviewer_role=SATURATION_REVIEW_ROLES[0],
            provider=provider,
        )
        common = {
            "supervisor_review": base.supervisor_review,
            "component_results": _components(),
            "red_team_result": _red_team(),
            "structured_result": _structured(),
            "source_graph_checkpoint": _source_checkpoint(),
        }
        with self.assertRaisesRegex(ValueError, "exactly match"):
            reviewer.review(
                checkpoint=base.checkpoint.to_dict(),
                evidence_facts=_route_facts()[:-1],
                **common,
            )
        stale = dict(base.checkpoint.to_dict())
        stale["source_graph_checkpoint_id"] = "STALE-SOURCE-CHECKPOINT"
        with self.assertRaisesRegex(ValueError, "binding is stale"):
            reviewer.review(
                checkpoint=stale,
                evidence_facts=_route_facts(),
                **common,
            )
        self.assertEqual(provider.calls, [])

    def test_supervisor_does_not_request_without_current_complete_synthesis(
        self,
    ) -> None:
        components = _components()
        invalid_syntheses = (
            None,
            SynthesisResult(
                status="PENDING",
                memo=None,
                pending_reasons=("fixture pending",),
                provider_name="PHASE87_SYNTHESIS_FIXTURE",
            ),
            _synthesis(components, target_id="OTHER-TARGET"),
            _synthesis(components, archetype_id="OTHER-ARCHETYPE"),
            SynthesisResult(
                status="COMPLETE",
                memo=replace(
                    _synthesis(components).memo,  # type: ignore[arg-type]
                    component_memo_ids=tuple(
                        row.memo.memo_id
                        for row in components[:-1]
                        if row.memo is not None
                    ),
                ),
                pending_reasons=(),
                provider_name="PHASE87_SYNTHESIS_FIXTURE",
            ),
        )
        for synthesis in invalid_syntheses:
            with self.subTest(synthesis=synthesis):
                provider = Phase87SupervisorProvider("READY")
                inputs = dict(_supervisor_inputs(components=components))
                inputs["synthesis_result"] = synthesis
                review = ResearchSupervisor(provider=provider).review_epoch(
                    **inputs
                )
                self.assertEqual(provider.calls, [])
                self.assertEqual(review.status, "NEXT_RESEARCH_REQUIRED")
                self.assertIn(
                    "SUPERVISOR_SYNTHESIS_LINEAGE_PENDING",
                    review.rationale,
                )
                self.assertIsNone(review.synthesis_memo_id)
                self.assertIsNone(review.synthesis_memo_hash)

    def test_supervisor_prompt_identity_changes_with_synthesis_and_drops_stale_prior(
        self,
    ) -> None:
        components = _components()
        first_synthesis = _synthesis(components, memo_id="SYNTHESIS-MEMO-v1")
        second_synthesis = _synthesis(components, memo_id="SYNTHESIS-MEMO-v2")
        provider = Phase87SupervisorProvider("READY")
        supervisor = ResearchSupervisor(provider=provider)
        first = supervisor.review_epoch(
            **_supervisor_inputs(
                components=components,
                synthesis=first_synthesis,
            )
        )
        second = supervisor.review_epoch(
            **_supervisor_inputs(
                components=components,
                synthesis=second_synthesis,
            ),
            prior_review=first,
        )
        first_payload = provider.calls[-2]["payload"]
        second_payload = provider.calls[-1]["payload"]
        first_binding = first_payload["current_synthesis"]["binding"]
        second_binding = second_payload["current_synthesis"]["binding"]
        self.assertNotEqual(first_binding, second_binding)
        self.assertNotEqual(first.prompt_hash, second.prompt_hash)
        self.assertIsNone(second_payload["prior_supervisor_review"])
        self.assertEqual(
            second.synthesis_memo_id,
            second_binding["synthesis_memo_id"],
        )
        self.assertEqual(
            second.synthesis_memo_hash,
            second_binding["synthesis_memo_hash"],
        )

    def test_current_red_team_change_invalidates_synthesis_before_provider(
        self,
    ) -> None:
        components = _components()
        original_red_team = _red_team()
        synthesis = _synthesis(
            components,
            red_team_result=original_red_team,
        )
        changed_red_team = replace(
            original_red_team,
            memo=replace(
                original_red_team.memo,  # type: ignore[arg-type]
                memo_id="RED-TEAM-MEMO-v2",
            ),
        )
        provider = Phase87SupervisorProvider("READY")
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs(
                components=components,
                synthesis=synthesis,
                red_team=changed_red_team,
            )
        )
        self.assertEqual(provider.calls, [])
        self.assertEqual(review.status, "NEXT_RESEARCH_REQUIRED")
        self.assertIn(
            "CURRENT_SYNTHESIS_RED_TEAM_LINEAGE_MISMATCH",
            review.rationale,
        )

    def test_counter_completion_requires_current_synthesis_supervisor_binding(
        self,
    ) -> None:
        components = _components()
        red_team = _red_team()
        synthesis = _synthesis(components, red_team_result=red_team)
        review = ResearchSupervisor(
            provider=Phase87SupervisorProvider("READY")
        ).review_epoch(
            **_supervisor_inputs(
                components=components,
                synthesis=synthesis,
                red_team=red_team,
            )
        )
        dossier = SimpleNamespace(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            component_results=components,
            red_team_result=red_team,
            synthesis_result=synthesis,
        )
        common = {
            "source_graph": SimpleNamespace(
                status="STOPPED_ON_RESOLUTION",
                audit={"critical_count_sum": 0},
            ),
            "fact_extraction": SimpleNamespace(
                status="FACT_EXTRACTION_COMPLETE",
                audit={"critical_count_sum": 0},
            ),
            "structured": SimpleNamespace(status="COMPLETE"),
            "aggregation": SimpleNamespace(
                component_results=tuple(
                    SimpleNamespace(material_disagreement=False)
                    for _ in CANONICAL_COMPONENT_ORDER
                ),
                score_valid=True,
            ),
        }
        gates = _completion_gates(
            dossier=dossier,
            epoch=SimpleNamespace(supervisor_review=review),
            **common,
        )
        self.assertTrue(gates["counter_thesis_complete"])
        self.assertFalse(gates["production_semantic_saturation_certified"])
        missing = _completion_gates(
            dossier=SimpleNamespace(**{**dossier.__dict__, "synthesis_result": None}),
            epoch=SimpleNamespace(supervisor_review=review),
            **common,
        )
        self.assertFalse(missing["counter_thesis_complete"])
        stale = _completion_gates(
            dossier=dossier,
            epoch=SimpleNamespace(
                supervisor_review=replace(
                    review,
                    synthesis_memo_hash="0" * 64,
                )
            ),
            **common,
        )
        self.assertFalse(stale["counter_thesis_complete"])
        changed_red_team = replace(
            red_team,
            memo=replace(
                red_team.memo,  # type: ignore[arg-type]
                memo_id="RED-TEAM-MEMO-v2",
            ),
        )
        stale_red_team = _completion_gates(
            dossier=SimpleNamespace(
                **{
                    **dossier.__dict__,
                    "red_team_result": changed_red_team,
                }
            ),
            epoch=SimpleNamespace(supervisor_review=review),
            **common,
        )
        self.assertFalse(stale_red_team["counter_thesis_complete"])

    def test_zero_results_are_failure_context_not_semantic_saturation(self) -> None:
        source = _source_checkpoint(zero_results=True)
        provider = Phase87SupervisorProvider("FORCE_READY")
        run = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=provider),
            saturation_reviewers=(),
        ).run_epoch(
            **_epoch_inputs(
                source_checkpoint=source,
                counter_proof=(
                    {
                        "objective_id": OBJECTIVE_ID,
                        "route_kind": "COUNTER_AND_SUPERSESSION",
                        "query_id": "Q-ZERO",
                    },
                ),
            )
        )
        self.assertEqual(run.checkpoint.status, "NEXT_RESEARCH_REQUIRED")
        self.assertFalse(run.checkpoint.semantic_saturation_certified)
        self.assertIn(
            "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR",
            run.supervisor_review.unresolved_material_questions[0],
        )

    def test_material_score_disagreement_reaches_supervisor_and_reopens_only_its_memo(
        self,
    ) -> None:
        component_id = CANONICAL_COMPONENT_ORDER[2]
        score_gap_context = {
            "deterministic_score_aggregation_status": (
                "DETERMINISTIC_SCORE_RESEARCH_REQUIRED"
            ),
            "score_valid": False,
            "component_research_requests": [
                {
                    "component_id": component_id,
                    "reason_codes": [
                        "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT"
                    ],
                    "proposal_points": {
                        "ANALYST": 16.5,
                        "SKEPTIC": 15.5,
                        "CALIBRATION_JUDGE": 18.35,
                    },
                },
                {
                    "component_id": CANONICAL_COMPONENT_ORDER[3],
                    "reason_codes": [
                        "COMPONENT_SCORING_MEMO_NOT_READY",
                        "SKEPTIC:PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING",
                    ],
                },
            ],
            "material_disagreement_judge_reviews": [
                {
                    "component_id": component_id,
                    "judge_reviews": [
                        {
                            "role": "SKEPTIC",
                            "proposed_points": 15.5,
                            "allowed_range": [14.5, 17.0],
                            "rationale": "현재 counter를 반영한 상단이다.",
                        },
                        {
                            "role": "CALIBRATION_JUDGE",
                            "proposed_points": 18.35,
                            "allowed_range": [18.05, 18.75],
                            "rationale": "ordinal anchor의 하단이다.",
                        },
                    ],
                }
            ],
            "score_or_stage_authority": False,
        }
        provider = Phase87SupervisorProvider("READY")
        run = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=provider),
            saturation_reviewers=(),
        ).run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint()),
            score_gap_context=score_gap_context,
        )

        self.assertEqual(run.checkpoint.status, "NEXT_RESEARCH_REQUIRED")
        findings = {
            row.component_id: row
            for row in run.supervisor_review.component_findings
        }
        self.assertFalse(findings[component_id].memo_sufficient)
        self.assertTrue(
            findings[CANONICAL_COMPONENT_ORDER[3]].memo_sufficient
        )
        payload = provider.calls[0]["payload"]
        self.assertEqual(
            payload["required_output_rosters"][
                "material_score_disagreement_component_ids"
            ],
            [component_id],
        )
        reviews = payload["deterministic_score_gap_context"][
            "material_disagreement_judge_reviews"
        ][0]["judge_reviews"]
        self.assertEqual(reviews[0]["allowed_range"], [14.5, 17.0])
        self.assertEqual(reviews[1]["allowed_range"], [18.05, 18.75])

    def test_transport_pending_judge_cannot_reopen_complete_component_memo(
        self,
    ) -> None:
        component_id = CANONICAL_COMPONENT_ORDER[3]

        class ReopeningProvider(Phase87SupervisorProvider):
            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                findings = [
                    dict(row) for row in response["component_findings"]
                ]
                for row in findings:
                    if row["component_id"] == component_id:
                        row.update(
                            {
                                "memo_sufficient": False,
                                "missing_fact_needs": [],
                                "rationale": "transport 대기를 memo 결함으로 오인",
                            }
                        )
                response.update(
                    {
                        "component_findings": findings,
                        "component_memos_sufficient": False,
                        "reasonable_positive_routes_remaining": True,
                        "ready_for_independent_saturation_review": False,
                        "next_actions": ["judge transport 응답을 기다린다."],
                        "rationale": "transport 대기만 남아 있다.",
                    }
                )
                return response

        provider = ReopeningProvider("READY")
        run = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=provider),
            saturation_reviewers=(),
        ).run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint()),
            score_gap_context={
                "component_research_requests": [
                    {
                        "component_id": component_id,
                        "reason_codes": [
                            "COMPONENT_SCORING_MEMO_NOT_READY",
                            "SKEPTIC:PROVIDER_ERROR:"
                            "COLLABORATION_RESPONSE_PENDING",
                        ],
                    }
                ]
            },
        )

        self.assertEqual(run.checkpoint.status, "NEXT_RESEARCH_REQUIRED")
        self.assertEqual(run.supervisor_review.component_findings, ())
        self.assertIn(
            "transport-pending judge responses cannot reopen",
            run.supervisor_review.unresolved_material_questions[0],
        )
        self.assertEqual(len(provider.calls), 2)

    def test_supervisor_query_direction_requires_matching_concrete_fact_gap(
        self,
    ) -> None:
        class DirectionWithoutGapProvider(Phase87SupervisorProvider):
            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                response.update(
                    {
                        "query_direction_briefs": [
                            {
                                "objective_id": OBJECTIVE_ID,
                                "research_need": "근거 없는 추가 검색",
                                "avoid_repeating": [],
                                "counter_or_supersession": False,
                            }
                        ],
                        "reasonable_positive_routes_remaining": True,
                        "ready_for_independent_saturation_review": False,
                        "next_actions": ["근거 없는 검색을 시도한다."],
                        "rationale": "구체적 missing fact 없이 검색을 요청했다.",
                    }
                )
                return response

        provider = DirectionWithoutGapProvider("READY")
        run = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=provider),
            saturation_reviewers=(),
        ).run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )

        self.assertEqual(run.supervisor_review.component_findings, ())
        self.assertIn(
            "requires a concrete component fact gap",
            run.supervisor_review.unresolved_material_questions[0],
        )
        self.assertEqual(len(provider.calls), 2)

    def test_parser_failure_and_source_absence_are_distinct(self) -> None:
        parser_provider = Phase87SupervisorProvider("PARSER")
        parser_review = ResearchSupervisor(provider=parser_provider).review_epoch(
            **_supervisor_inputs(
                prior_failures=(
                    {
                        "failure_id": "FAIL-PARSER",
                        "failure_reason": "PDF_PARSER_TABLE_EXTRACTION_FAILED",
                    },
                )
            )
        )
        self.assertEqual(
            parser_review.failure_assessments[0].classification,
            "PARSER_EXTRACTOR_FAILURE",
        )
        self.assertEqual(parser_review.parser_or_extractor_failures, ("FAIL-PARSER",))
        absence_provider = Phase87SupervisorProvider("ABSENCE")
        absence_review = ResearchSupervisor(provider=absence_provider).review_epoch(
            **_supervisor_inputs(
                prior_failures=(
                    {
                        "failure_id": "FAIL-ABSENCE",
                        "failure_reason": "MULTI_SOURCE_SEMANTIC_ABSENCE_REVIEW",
                        "absence_eligible": True,
                        "zero_result_only": False,
                        "parser_extractor_verified": True,
                        "provider_transport_verified": True,
                        "attempted_source_families": [
                            "ISSUER_PRESENTATION",
                            "CUSTOMER_OFFICIAL",
                        ],
                    },
                )
            )
        )
        self.assertEqual(
            absence_review.failure_assessments[0].classification,
            "SOURCE_ABSENCE_CANDIDATE",
        )
        self.assertTrue(
            absence_review.failure_assessments[0].source_absence_claim_allowed
        )

    def test_resolved_multi_objective_generation_failures_keep_lineage_without_blocking(
        self,
    ) -> None:
        class BlockingClassificationReadyProvider(Phase87SupervisorProvider):
            def __init__(self) -> None:
                super().__init__("FORCE_READY")

            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                for assessment in response["failure_assessments"]:
                    assessment.update(
                        {
                            "classification": "PROVIDER_FAILURE",
                            "retryable": True,
                            "source_absence_claim_allowed": False,
                        }
                    )
                return response

        provider_reasons = tuple(
            f"QUERY_PROVIDER_ERROR:historical-provider-attempt-{index}"
            for index in range(24)
        )
        no_query_reason = "LLM_RETURNED_NO_NEW_VALID_QUERY"
        source = _source_checkpoint_with_updates(
            _source_checkpoint(),
            status="STOPPED_ON_RESOLUTION",
            resolved_objective_ids=[OBJECTIVE_ID],
            source_graph={
                "open_objectives": [{"objective_id": OBJECTIVE_ID}]
            },
            query_failures=[
                {
                    "query_id": "QUERY_GENERATION",
                    "objective_id": "MULTI_OBJECTIVE",
                    "failure_reason": reason,
                }
                for reason in (*provider_reasons, no_query_reason)
            ],
            query_generation_history=[
                {
                    "status": "PENDING",
                    "queries": [],
                    "rejected_suggestions": [],
                    "feedback_for_next_llm_call": [reason],
                    "provider_name": "CURRENT-QUERY-PROVIDER",
                    "prompt_hash": f"QUERYPROMPT-{index}",
                    "response_hash": None,
                    "deterministic_fallback_query_used": False,
                }
                for index, reason in enumerate(
                    (*provider_reasons, no_query_reason)
                )
            ],
        )
        provider = BlockingClassificationReadyProvider()
        review = ResearchSupervisor(provider=provider).review_epoch(
            **{
                **_supervisor_inputs(),
                "source_graph_checkpoint": source,
            }
        )

        self.assertEqual(
            review.status,
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
        )
        self.assertEqual(len(review.failure_assessments), 25)
        supplied = provider.calls[-1]["payload"][
            "prior_query_source_failures"
        ]
        by_reason = {
            row["failure_reason"]: row
            for row in supplied
        }
        provider_group = by_reason["QUERY_PROVIDER_ERROR"]
        self.assertEqual(provider_group["member_failure_count"], 24)
        self.assertIs(provider_group["resolved"], True)
        self.assertEqual(
            provider_group["resolved_by"],
            "SOURCE_GRAPH_OBJECTIVE_RESOLUTION",
        )
        self.assertEqual(
            provider_group["relation_coverage"]["objective_ids"],
            {OBJECTIVE_ID: 24},
        )
        no_query_group = by_reason[no_query_reason]
        self.assertIs(no_query_group["resolved"], True)
        self.assertEqual(
            no_query_group["relation_coverage"]["objective_ids"],
            {OBJECTIVE_ID: 1},
        )

    def test_multi_objective_label_without_raw_generation_lineage_still_blocks(
        self,
    ) -> None:
        class BlockingClassificationReadyProvider(Phase87SupervisorProvider):
            def __init__(self) -> None:
                super().__init__("FORCE_READY")

            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                for assessment in response["failure_assessments"]:
                    assessment.update(
                        {
                            "classification": "PROVIDER_FAILURE",
                            "retryable": True,
                            "source_absence_claim_allowed": False,
                        }
                    )
                return response

        source = _source_checkpoint_with_updates(
            _source_checkpoint(),
            status="STOPPED_ON_RESOLUTION",
            resolved_objective_ids=[OBJECTIVE_ID],
            source_graph={
                "open_objectives": [{"objective_id": OBJECTIVE_ID}]
            },
            query_failures=[
                {
                    "query_id": "QUERY_GENERATION",
                    "objective_id": "MULTI_OBJECTIVE",
                    "failure_reason": (
                        "QUERY_PROVIDER_ERROR:not-in-generation-history"
                    ),
                }
            ],
            query_generation_history=[],
        )
        provider = BlockingClassificationReadyProvider()
        review = ResearchSupervisor(provider=provider).review_epoch(
            **{
                **_supervisor_inputs(),
                "source_graph_checkpoint": source,
            }
        )

        self.assertEqual(review.status, "NEXT_RESEARCH_REQUIRED")
        self.assertEqual(len(provider.calls), 2)
        supplied = provider.calls[-1]["payload"][
            "prior_query_source_failures"
        ][0]
        self.assertNotIn("resolved", supplied)
        self.assertEqual(
            supplied["relation_coverage"]["objective_id"],
            {"MULTI_OBJECTIVE": 1},
        )

    def test_resolved_rejected_query_keeps_exact_objective_lineage(self) -> None:
        class BlockingClassificationReadyProvider(Phase87SupervisorProvider):
            def __init__(self) -> None:
                super().__init__("FORCE_READY")

            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                for assessment in response["failure_assessments"]:
                    assessment.update(
                        {
                            "classification": "INSUFFICIENT_SEARCH",
                            "retryable": True,
                            "source_absence_claim_allowed": False,
                        }
                    )
                return response

        rejected_feedback = "TARGET_SCOPE_MISSING:counterparty-only query"
        source = _source_checkpoint_with_updates(
            _source_checkpoint(),
            status="STOPPED_ON_RESOLUTION",
            resolved_objective_ids=[OBJECTIVE_ID],
            source_graph={
                "open_objectives": [{"objective_id": OBJECTIVE_ID}]
            },
            query_failures=[
                {
                    "query_id": "QUERY_GENERATION",
                    "objective_id": "MULTI_OBJECTIVE",
                    "failure_reason": rejected_feedback,
                }
            ],
            query_generation_history=[
                {
                    "status": "PARTIAL",
                    "queries": [],
                    "rejected_suggestions": [
                        {
                            "suggestion_index": "0",
                            "objective_id": OBJECTIVE_ID,
                            "literal_query": "counterparty-only query",
                            "reason": "TARGET_SCOPE_MISSING",
                        }
                    ],
                    "feedback_for_next_llm_call": [rejected_feedback],
                    "provider_name": "CURRENT-QUERY-PROVIDER",
                    "prompt_hash": "QUERYPROMPT-REJECTED-SCOPE",
                    "response_hash": "QUERYRESP-REJECTED-SCOPE",
                    "deterministic_fallback_query_used": False,
                }
            ],
        )
        provider = BlockingClassificationReadyProvider()
        review = ResearchSupervisor(provider=provider).review_epoch(
            **{
                **_supervisor_inputs(),
                "source_graph_checkpoint": source,
            }
        )

        self.assertEqual(
            review.status,
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
        )
        supplied = provider.calls[-1]["payload"][
            "prior_query_source_failures"
        ][0]
        self.assertIs(supplied["resolved"], True)
        self.assertEqual(
            supplied["resolved_by"],
            "SOURCE_GRAPH_OBJECTIVE_RESOLUTION",
        )
        self.assertEqual(
            supplied["relation_coverage"]["objective_ids"],
            {OBJECTIVE_ID: 1},
        )

    def test_resolved_parser_assessment_is_honest_but_not_an_open_parser_gap(
        self,
    ) -> None:
        class ResolvedParserReadyProvider(Phase87SupervisorProvider):
            def __init__(self) -> None:
                super().__init__("FORCE_READY")

            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                for assessment in response["failure_assessments"]:
                    assessment.update(
                        {
                            "classification": "PARSER_EXTRACTOR_FAILURE",
                            "retryable": True,
                            "source_absence_claim_allowed": False,
                        }
                    )
                return response

        source = _source_checkpoint_with_updates(
            _source_checkpoint(),
            status="STOPPED_ON_RESOLUTION",
            resolved_objective_ids=[OBJECTIVE_ID],
            source_graph={
                "open_objectives": [{"objective_id": OBJECTIVE_ID}]
            },
        )
        provider = ResolvedParserReadyProvider()
        review = ResearchSupervisor(provider=provider).review_epoch(
            **{
                **_supervisor_inputs(
                    prior_failures=(
                        {
                            "failure_id": "FAIL-RESOLVED-PARSER",
                            "failure_kind": "DOCUMENT_REJECTION",
                            "failure_reason": (
                                "FACT_EXTRACTOR_REPORTED_UNREADABLE_FULL_DOCUMENT"
                            ),
                            "objective_ids": [OBJECTIVE_ID],
                        },
                    )
                ),
                "source_graph_checkpoint": source,
            }
        )

        self.assertEqual(
            review.status,
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
        )
        self.assertEqual(
            review.failure_assessments[0].classification,
            "PARSER_EXTRACTOR_FAILURE",
        )
        self.assertEqual(review.parser_or_extractor_failures, ())
        supplied = provider.calls[-1]["payload"][
            "prior_query_source_failures"
        ][0]
        self.assertIs(supplied["resolved"], True)
        self.assertEqual(
            supplied["resolved_by"],
            "SOURCE_GRAPH_OBJECTIVE_RESOLUTION",
        )

    def test_equivalent_failure_group_judgment_expands_to_every_original_id(self) -> None:
        provider = Phase87SupervisorProvider("PARSER")
        failure_ids = tuple(f"FAIL-PARSER-{index}" for index in range(100))
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs(
                prior_failures=tuple(
                    {
                        "failure_id": failure_id,
                        "failure_kind": "QUERY_FAILURE",
                        "failure_stage": "PARSER",
                        "failure_reason": "PDF_PARSER_TABLE_EXTRACTION_FAILED",
                        "absence_eligible": False,
                        "zero_result_only": False,
                    }
                    for failure_id in failure_ids
                )
            )
        )
        supplied_groups = provider.calls[-1]["payload"][
            "prior_query_source_failures"
        ]
        self.assertEqual(len(supplied_groups), 1)
        self.assertEqual(supplied_groups[0]["member_failure_count"], 100)
        self.assertNotIn("member_failure_ids", supplied_groups[0])
        failure_projection = provider.calls[-1]["payload"][
            "prior_query_source_failure_projection"
        ]
        self.assertIn("failure_group_member_mapping_hash", failure_projection)
        self.assertTrue(
            failure_projection[
                "every_failure_id_preserved_by_group_roster_hash"
            ]
        )
        self.assertLess(
            len(json.dumps(provider.calls[-1]["payload"], ensure_ascii=False)),
            100_000,
        )
        self.assertEqual(
            {row.failure_id for row in review.failure_assessments},
            set(failure_ids),
        )
        self.assertEqual(
            set(review.parser_or_extractor_failures),
            set(failure_ids),
        )

    def test_prior_supervisor_expanded_failure_history_is_loss_accounted_and_bounded(
        self,
    ) -> None:
        provider = Phase87SupervisorProvider("GAP")
        failure_assessments = [
            {
                "failure_id": f"PRIOR-FAIL-{index:05d}",
                "classification": "PARSER_EXTRACTOR_FAILURE",
                "rationale": "동일 파서 실패는 대체 원문 경로가 필요하다.",
                "retryable": False,
                "source_absence_claim_allowed": False,
            }
            for index in range(5_000)
        ]
        oversized_error = (
            "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:StructuredProviderUnavailable:"
            + "replayed failure ledger " * 5_000
            + " Codex ran out of room in the model's context window"
        )
        synthesis_memo = _synthesis().memo
        assert synthesis_memo is not None
        ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs(),
            prior_review={
                "review_id": "PRIOR-REVIEW",
                "epoch": 200,
                "status": "NEXT_RESEARCH_REQUIRED",
                "component_status": {
                    component_id: "COMPLETE"
                    for component_id in CANONICAL_COMPONENT_ORDER
                },
                "unresolved_material_questions": [oversized_error],
                "source_family_gaps": [],
                "parser_or_extractor_failures": [
                    row["failure_id"] for row in failure_assessments
                ],
                "next_actions": ["provider 입력을 의미 집계로 재구성한다."],
                "failure_assessments": failure_assessments,
                "rationale": oversized_error,
                "synthesis_memo_id": synthesis_memo.memo_id,
                "synthesis_memo_hash": _stable_test_hash(
                    synthesis_memo.to_dict()
                ),
            },
        )
        payload = provider.calls[-1]["payload"]
        prior = payload["prior_supervisor_review"]
        projection = prior["failure_assessment_projection"]
        self.assertEqual(projection["failure_assessment_count"], 5_000)
        self.assertEqual(projection["semantic_group_count"], 1)
        self.assertTrue(
            projection[
                "every_assessment_accounted_by_group_count_and_hash"
            ]
        )
        self.assertEqual(
            prior["parser_or_extractor_failure_projection"]["failure_count"],
            5_000,
        )
        encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        self.assertLess(len(encoded), 150_000)
        self.assertNotIn("PRIOR-FAIL-04999", encoded)
        self.assertIn("PROVIDER_CONTEXT_WINDOW_EXCEEDED", encoded)
        self.assertTrue(prior["full_prior_review_persisted_outside_prompt"])
        self.assertFalse(prior["fixed_top_n_used"])

    def test_supervisor_prompt_ignores_epoch_and_prior_review_lineage(self) -> None:
        seed = ResearchSupervisor(
            provider=Phase87SupervisorProvider("GAP")
        ).review_epoch(**_supervisor_inputs())
        first_prior = dict(seed.to_dict())
        resumed_prior = {
            **first_prior,
            "review_id": "RESUMED-REVIEW-ID",
            "epoch": 999,
            "prompt_hash": "RESUMED-PROMPT-HASH",
        }
        provider = Phase87SupervisorProvider("GAP")
        supervisor = ResearchSupervisor(provider=provider)
        supervisor.review_epoch(
            **_supervisor_inputs(),
            prior_review=first_prior,
        )
        resumed_inputs = dict(_supervisor_inputs())
        resumed_inputs["epoch"] = 999
        supervisor.review_epoch(
            **resumed_inputs,
            prior_review=resumed_prior,
        )
        first_payload = provider.calls[-2]["payload"]
        resumed_payload = provider.calls[-1]["payload"]
        self.assertEqual(first_payload, resumed_payload)
        self.assertNotIn("epoch", first_payload)
        prior_projection = first_payload["prior_supervisor_review"]
        self.assertNotIn("review_id", prior_projection)
        self.assertNotIn("epoch", prior_projection)
        self.assertNotIn("prompt_hash", prior_projection)
        self.assertTrue(
            prior_projection["checkpoint_lineage_excluded_from_provider"]
        )

    def test_supervisor_prompt_normalizes_collaboration_wait_request_id(self) -> None:
        seed = ResearchSupervisor(
            provider=Phase87SupervisorProvider("GAP")
        ).review_epoch(**_supervisor_inputs())
        request_a = "COLLABREQ-" + ("a" * 64)
        request_b = "COLLABREQ-" + ("b" * 64)

        def prior(request_id: str) -> Mapping[str, Any]:
            wait = (
                "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                "StructuredProviderUnavailable:"
                f"COLLABORATION_RESPONSE_PENDING:{request_id}"
            )
            return {
                **seed.to_dict(),
                "unresolved_material_questions": [wait],
                "rationale": wait,
            }

        provider = Phase87SupervisorProvider("GAP")
        supervisor = ResearchSupervisor(provider=provider)
        supervisor.review_epoch(
            **_supervisor_inputs(),
            prior_review=prior(request_a),
        )
        supervisor.review_epoch(
            **_supervisor_inputs(),
            prior_review=prior(request_b),
        )

        first_payload = provider.calls[-2]["payload"]
        second_payload = provider.calls[-1]["payload"]
        self.assertEqual(first_payload, second_payload)
        encoded = json.dumps(first_payload, ensure_ascii=False, sort_keys=True)
        self.assertNotIn(request_a, encoded)
        self.assertNotIn(request_b, encoded)
        self.assertIn("COLLABREQ-<REQUEST_ID>", encoded)
        self.assertEqual(
            first_payload["prior_supervisor_review"][
                "prior_review_semantic_hash"
            ],
            second_payload["prior_supervisor_review"][
                "prior_review_semantic_hash"
            ],
        )

    def test_supervisor_resume_reuses_request_identity_after_transport_wait(
        self,
    ) -> None:
        class PendingThenReadySupervisorProvider(Phase87SupervisorProvider):
            def __init__(self) -> None:
                super().__init__("READY")
                self.transport_pending = True

            def complete(self, *, pass_name, payload):
                if self.transport_pending:
                    self.calls.append(
                        {"pass_name": pass_name, "payload": payload}
                    )
                    raise StructuredProviderUnavailable(
                        "COLLABORATION_RESPONSE_PENDING:COLLABREQ-"
                        + _stable_test_hash(payload)
                    )
                return super().complete(
                    pass_name=pass_name,
                    payload=payload,
                )

        provider = PendingThenReadySupervisorProvider()
        supervisor = ResearchSupervisor(provider=provider)
        pending = supervisor.review_epoch(**_supervisor_inputs())
        first_payload = provider.calls[-1]["payload"]

        self.assertFalse(
            pending.ready_for_independent_saturation_review
        )
        self.assertIn(
            "COLLABORATION_RESPONSE_PENDING",
            pending.rationale,
        )

        provider.transport_pending = False
        resumed_inputs = dict(_supervisor_inputs())
        resumed_inputs["epoch"] = 2
        resumed = supervisor.review_epoch(
            **resumed_inputs,
            prior_review=pending,
        )
        resumed_payload = provider.calls[-1]["payload"]

        self.assertEqual(resumed_payload, first_payload)
        self.assertTrue(
            resumed.ready_for_independent_saturation_review
        )
        self.assertIsNone(
            resumed_payload["prior_supervisor_review"]
        )

    def test_supervisor_prompt_preserves_noncanonical_provider_errors(self) -> None:
        seed = ResearchSupervisor(
            provider=Phase87SupervisorProvider("GAP")
        ).review_epoch(**_supervisor_inputs())
        request_id = "COLLABREQ-" + ("a" * 64)

        def payload_for(error: str) -> Mapping[str, Any]:
            prior = {
                **seed.to_dict(),
                "unresolved_material_questions": [error],
                "rationale": error,
            }
            provider = Phase87SupervisorProvider("GAP")
            ResearchSupervisor(provider=provider).review_epoch(
                **_supervisor_inputs(),
                prior_review=prior,
            )
            return provider.calls[-1]["payload"]

        suffixed = (
            "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
            "StructuredProviderUnavailable:"
            "COLLABORATION_RESPONSE_PENDING:"
            f"{request_id}:HTTP_503"
        )
        rejected = (
            "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
            "StructuredProviderRejected:"
            "component sufficiency contradicts current memos"
        )
        suffixed_payload = payload_for(suffixed)
        rejected_payload = payload_for(rejected)
        self.assertIn(
            request_id,
            json.dumps(suffixed_payload, ensure_ascii=False, sort_keys=True),
        )
        self.assertIn(
            "StructuredProviderRejected",
            json.dumps(rejected_payload, ensure_ascii=False, sort_keys=True),
        )
        self.assertNotEqual(
            suffixed_payload["prior_supervisor_review"][
                "prior_review_semantic_hash"
            ],
            rejected_payload["prior_supervisor_review"][
                "prior_review_semantic_hash"
            ],
        )

    def test_supervisor_provider_error_is_bounded_before_checkpoint_persistence(
        self,
    ) -> None:
        class OversizedErrorProvider(Phase87SupervisorProvider):
            def complete(self, *, pass_name, payload):
                self.calls.append({"pass_name": pass_name, "payload": payload})
                raise RuntimeError(
                    "echoed provider input " * 10_000
                    + "CONTEXT_WINDOW_EXCEEDED"
                )

        review = ResearchSupervisor(
            provider=OversizedErrorProvider("ERROR")
        ).review_epoch(**_supervisor_inputs())
        self.assertIn("SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR", review.rationale)
        self.assertIn("CONTEXT_WINDOW_EXCEEDED", review.rationale)
        self.assertLess(len(review.rationale), 700)
        self.assertEqual(
            review.unresolved_material_questions,
            (review.rationale,),
        )

    def test_zero_result_alone_cannot_be_relabelled_as_source_absence(self) -> None:
        provider = Phase87SupervisorProvider("ABSENCE")
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs(
                prior_failures=(
                    {
                        "failure_id": "FAIL-ZERO",
                        "failure_reason": "SEARCH_NO_RESULT_NOT_SATURATION",
                        "absence_eligible": True,
                        "zero_result_only": False,
                    },
                )
            )
        )
        self.assertEqual(review.status, "NEXT_RESEARCH_REQUIRED")
        self.assertIn("SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR", review.rationale)
        self.assertEqual(review.failure_assessments, ())

    def test_checkpoint_resume_records_only_deltas_and_drops_stale_prior_review(
        self,
    ) -> None:
        provider = Phase87SupervisorProvider("GAP")
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=provider),
            saturation_reviewers=(),
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        second_source = _source_checkpoint(extra_epoch=True)
        second = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=second_source,
                facts=(_fact("FACT-1"), _fact("FACT-2")),
                components=_components(summary_suffix="v2", change_only_first=True),
                prior_checkpoint=first.checkpoint,
            )
        )
        self.assertEqual(second.checkpoint.epoch, 2)
        self.assertEqual(
            second.checkpoint.resumed_from_checkpoint_id,
            first.checkpoint.checkpoint_id,
        )
        self.assertEqual([row["query_id"] for row in second.checkpoint.queries], ["Q-NEW"])
        self.assertEqual(
            [row["document_id"] for row in second.checkpoint.documents], ["DOC-2"]
        )
        self.assertEqual([row["fact_id"] for row in second.checkpoint.new_facts], ["FACT-2"])
        self.assertEqual(len(second.checkpoint.changed_component_memos), 1)
        self.assertIsNone(
            provider.calls[-1]["payload"]["prior_supervisor_review"]
        )
        self.assertNotEqual(
            first.supervisor_review.synthesis_memo_hash,
            second.supervisor_review.synthesis_memo_hash,
        )

    def test_checkpoint_reused_component_results_are_semantically_unchanged_deltas(
        self,
    ) -> None:
        provider = Phase87SupervisorProvider("GAP")
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=provider),
            saturation_reviewers=(),
        )
        original_components = _components()
        first = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                components=original_components,
            )
        )
        reused_components = tuple(
            replace(
                row,
                provider_name="CHECKPOINT_REUSED_PRIOR_COMPONENT_MEMO",
                prompt_hash=None,
            )
            for row in original_components
        )
        second = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                components=reused_components,
                prior_checkpoint=first.checkpoint,
            )
        )

        self.assertEqual(second.checkpoint.changed_component_memos, ())
        self.assertEqual(
            second.checkpoint.component_memo_hashes,
            first.checkpoint.component_memo_hashes,
        )
        self.assertIsNotNone(
            provider.calls[-1]["payload"]["prior_supervisor_review"]
        )

    def test_reextracted_fact_is_retired_with_lineage_instead_of_crashing_resume(self) -> None:
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(
                provider=Phase87SupervisorProvider("GAP")
            ),
            saturation_reviewers=(),
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        second = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(extra_epoch=True),
                facts=(_fact("FACT-2"),),
                components=_components(fact_id="FACT-2"),
                prior_checkpoint=first.checkpoint,
            )
        )
        self.assertEqual(second.checkpoint.current_fact_ids, ("FACT-2",))
        self.assertEqual(
            second.checkpoint.retired_fact_ids,
            ("FACT-1", "FACT-COUNTER", "FACT-SUPERSESSION"),
        )
        self.assertEqual(
            set(second.checkpoint.cumulative_fact_ids),
            {
                "FACT-1",
                "FACT-2",
                "FACT-COUNTER",
                "FACT-SUPERSESSION",
            },
        )
        self.assertEqual(
            second.checkpoint.retired_facts[0]["reason"],
            "FACT_EXTRACTION_REVISED_OR_SUPERSEDED",
        )

    def test_checkpoint_tampering_and_lost_cumulative_lineage_are_rejected(self) -> None:
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(
                provider=Phase87SupervisorProvider("GAP")
            )
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        tampered = dict(first.checkpoint.to_dict())
        tampered["next_actions"] = ["tampered"]
        with self.assertRaisesRegex(ValueError, "checkpoint hash mismatch"):
            runner.run_epoch(
                **_epoch_inputs(
                    source_checkpoint=_source_checkpoint(),
                    prior_checkpoint=tampered,
                )
            )
        with self.assertRaisesRegex(ValueError, "lost cumulative query lineage"):
            runner.run_epoch(
                **_epoch_inputs(
                    source_checkpoint=_source_checkpoint(with_queries=False),
                    prior_checkpoint=first.checkpoint,
                )
            )
        with self.assertRaisesRegex(ValueError, "lost cumulative document lineage"):
            runner.run_epoch(
                **_epoch_inputs(
                    source_checkpoint=_source_checkpoint(with_document=False),
                    prior_checkpoint=first.checkpoint,
                )
            )

    def test_explicit_unreadable_document_quarantine_preserves_cumulative_lineage(
        self,
    ) -> None:
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(
                provider=Phase87SupervisorProvider("GAP")
            ),
            saturation_reviewers=(),
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        source_checkpoint = _source_checkpoint(quarantine_document=True)

        self.assertEqual(
            validated_quarantined_document_ids(source_checkpoint), {"DOC-1"}
        )
        malformed_quarantine = dict(source_checkpoint)
        malformed_quarantine["rejected_documents"] = []
        with self.assertRaisesRegex(ValueError, "lacks matching rejection"):
            validated_quarantined_document_ids(malformed_quarantine)
        resumed = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=source_checkpoint,
                prior_checkpoint=first.checkpoint,
            )
        )

        self.assertEqual(resumed.checkpoint.cumulative_document_ids, ("DOC-1",))
        self.assertEqual(resumed.checkpoint.documents, ())
        supervisor_payload = runner.supervisor.provider.calls[-1]["payload"]
        supervisor_source_graph = supervisor_payload["source_graph_checkpoint"]
        self.assertEqual(
            supervisor_source_graph["quarantined_documents"]["record_count"],
            1,
        )
        self.assertEqual(
            supervisor_source_graph["quarantined_documents"][
                "document_id_roster"
            ]["count"],
            1,
        )
        self.assertTrue(
            supervisor_source_graph["quarantined_documents"][
                "every_quarantine_accounted_by_hash_and_group_count"
            ]
        )
        self.assertEqual(
            supervisor_source_graph["source_graph_prompt_projection"][
                "schema_version"
            ],
            "e2r_v5_supervisor_source_graph_projection_v4",
        )
        self.assertEqual(
            supervisor_payload["current_evidence_fact_graph"]["record_count"],
            3,
        )
        self.assertFalse(
            supervisor_payload["current_evidence_fact_graph"]["fixed_top_n_used"]
        )

    def test_prior_checkpoint_files_round_trip_and_keep_pending_reviewer_errors(self) -> None:
        reviewers = tuple(
            SemanticSaturationReviewer(
                reviewer_role=role,
                provider=Phase87SaturationProvider(
                    f"REVIEW-{index}", unresolved=index == 2
                ),
            )
            for index, role in enumerate(SATURATION_REVIEW_ROLES)
        )
        run = ResearchEpochRunner(
            supervisor=ResearchSupervisor(
                provider=Phase87SupervisorProvider("READY")
            ),
            saturation_reviewers=reviewers,
        ).run_epoch(**_epoch_inputs(source_checkpoint=_source_checkpoint()))
        self.assertFalse(run.checkpoint.semantic_saturation_certified)
        with tempfile.TemporaryDirectory() as directory:
            paths = write_research_epoch_run(run, directory)
            self.assertEqual(set(paths), set(RESEARCH_EPOCH_OUTPUT_FILES))
            restored = load_research_epoch_checkpoint(paths["checkpoint"])
            self.assertEqual(restored, run.checkpoint)
            rows = [
                json.loads(line)
                for line in paths["saturation_reviews"]
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            self.assertEqual(len(rows), 3)
            self.assertTrue(all("status" in row for row in rows))

    def test_v2_unknown_gold_sentinel_resumes_hash_safely_as_v3_not_run(self) -> None:
        runner = ResearchEpochRunner(
            supervisor=ResearchSupervisor(
                provider=Phase87SupervisorProvider("GAP")
            ),
            saturation_reviewers=(),
        )
        first = runner.run_epoch(
            **_epoch_inputs(source_checkpoint=_source_checkpoint())
        )
        legacy = dict(first.checkpoint.to_dict())
        legacy["schema_version"] = "e2r_research_epoch_checkpoint_v2"
        legacy.pop("gold_evaluation_status")
        legacy["gold_critical_fact_miss_count"] = 1
        legacy["checkpoint_id"] = _research_checkpoint_id(legacy)
        legacy["checkpoint_hash"] = _research_checkpoint_hash(legacy)

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "legacy-v2.json"
            path.write_text(
                json.dumps(legacy, ensure_ascii=False),
                encoding="utf-8",
            )
            restored = load_research_epoch_checkpoint(path)

        self.assertEqual(restored.checkpoint_id, legacy["checkpoint_id"])
        self.assertEqual(restored.checkpoint_hash, legacy["checkpoint_hash"])
        self.assertEqual(
            restored.gold_evaluation_status,
            GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
        )
        self.assertNotIn(
            "gold_critical_fact_miss_count",
            restored.to_score_gap_context(),
        )

        resumed = runner.run_epoch(
            **_epoch_inputs(
                source_checkpoint=_source_checkpoint(),
                prior_checkpoint=restored,
            )
        )
        self.assertEqual(
            resumed.checkpoint.schema_version,
            "e2r_research_epoch_checkpoint_v3",
        )
        self.assertEqual(
            resumed.checkpoint.resumed_from_checkpoint_id,
            legacy["checkpoint_id"],
        )
        self.assertEqual(
            resumed.checkpoint.gold_evaluation_status,
            GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
        )
        self.assertIsNone(resumed.checkpoint.gold_critical_fact_miss_count)

    def test_provider_outage_is_pending_and_never_builds_fallback_query(self) -> None:
        provider = Phase87SupervisorProvider("ERROR")
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs()
        )
        self.assertEqual(review.status, "NEXT_RESEARCH_REQUIRED")
        self.assertEqual(len(provider.calls), 1)
        context = review.to_score_gap_context()
        self.assertEqual(context["query_direction_briefs"], [])
        self.assertNotIn("suggested_queries", context)

    def test_supervisor_prompt_requires_llm_owned_independence_review(
        self,
    ) -> None:
        provider = Phase87SupervisorProvider("READY")
        ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs()
        )

        required = provider.calls[0]["payload"]["required_output_rosters"]
        contract = required[
            "independent_corroboration_review_contract"
        ]
        self.assertTrue(contract["llm_owns_gap_materiality"])
        self.assertEqual(
            contract["literal_query_generation_owner"],
            "SOURCE_QUERY_GENERATION_LLM",
        )
        self.assertIn("source-family direction", contract["instruction"])
        self.assertNotIn(
            "literal query",
            contract["instruction"].split("Do not")[0],
        )

    def test_supervisor_prompt_keeps_structured_report_handoff_llm_owned(
        self,
    ) -> None:
        provider = Phase87SupervisorProvider("READY")
        ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs()
        )

        required = provider.calls[0]["payload"]["required_output_rosters"]
        contract = required[
            "structured_report_source_candidate_review_contract"
        ]
        self.assertTrue(contract["llm_owns_candidate_materiality"])
        self.assertEqual(
            contract["literal_query_generation_owner"],
            "SOURCE_QUERY_GENERATION_LLM",
        )
        self.assertIn("never as evidence", contract["instruction"])
        self.assertIn("PUBLIC_BROKER_PDF", contract["instruction"])
        self.assertIn("Do not create a literal query or URL", contract["instruction"])

    def test_supervisor_semantic_error_gets_one_bounded_correction(self) -> None:
        provider = Phase87CorrectingSupervisorProvider(
            "COUNTER_WITHOUT_PROOF"
        )
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs(counter_proof=())
        )
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(len(provider.invalidations), 1)
        retry_context = provider.calls[-1]["payload"][
            "supervisor_validation_retry_context"
        ]
        self.assertIn("counter/supersession", retry_context["validation_error"])
        deterministic = retry_context["deterministic_current_state"]
        self.assertFalse(deterministic["counter_route_proof_complete"])
        self.assertFalse(deterministic["counter_completion_may_be_true"])
        self.assertFalse(review.counter_and_supersession_checked)
        self.assertEqual(review.status, "NEXT_RESEARCH_REQUIRED")

    def test_supervisor_unknown_objective_is_corrected_with_allowed_ids(self) -> None:
        provider = Phase87CorrectingSupervisorProvider("UNKNOWN_OBJECTIVE")
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs()
        )
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(len(provider.invalidations), 1)
        retry_context = provider.calls[-1]["payload"][
            "supervisor_validation_retry_context"
        ]
        self.assertEqual(retry_context["allowed_objective_ids"], [OBJECTIVE_ID])
        self.assertIn("unknown research objective", retry_context["validation_error"])
        self.assertEqual(
            review.status,
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
        )

    def test_supervisor_missing_failure_group_gets_exact_roster_feedback(
        self,
    ) -> None:
        provider = Phase87CorrectingSupervisorProvider(
            "MISSING_FAILURE_GROUP"
        )
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs(
                prior_failures=(
                    {
                        "failure_id": "FAIL-ONE",
                        "failure_reason": "FETCH_TIMEOUT",
                    },
                    {
                        "failure_id": "FAIL-TWO",
                        "failure_reason": "HTTP_404",
                    },
                )
            )
        )
        self.assertEqual(len(provider.calls), 2)
        initial_payload = provider.calls[0]["payload"]
        required = initial_payload["required_output_rosters"]
        self.assertEqual(required["failure_group_count"], 2)
        retry_context = provider.calls[1]["payload"][
            "supervisor_validation_retry_context"
        ]
        self.assertEqual(
            retry_context["required_failure_group_ids"],
            required["failure_group_ids"],
        )
        diagnostics = retry_context[
            "failure_assessment_roster_diagnostics"
        ]
        self.assertEqual(diagnostics["required_count"], 2)
        self.assertEqual(diagnostics["received_count"], 1)
        self.assertEqual(len(diagnostics["missing_failure_group_ids"]), 1)
        self.assertEqual(diagnostics["extra_failure_group_ids"], [])
        self.assertEqual(diagnostics["duplicate_failure_group_ids"], [])
        self.assertEqual(len(review.failure_assessments), 2)

    def test_supervisor_absence_proof_failure_gets_exact_group_feedback(
        self,
    ) -> None:
        provider = Phase87CorrectingSupervisorProvider(
            "SOURCE_ABSENCE_WITHOUT_PROOF"
        )
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs(
                prior_failures=(
                    {
                        "failure_id": "FAIL-NO-ABSENCE-PROOF",
                        "failure_reason": "FETCH_TIMEOUT",
                        "absence_eligible": False,
                        "zero_result_only": False,
                        "parser_extractor_verified": False,
                        "provider_transport_verified": True,
                    },
                )
            )
        )

        self.assertEqual(len(provider.calls), 2)
        diagnostics = provider.calls[1]["payload"][
            "supervisor_validation_retry_context"
        ]["failure_assessment_roster_diagnostics"]
        required_ids = provider.calls[0]["payload"][
            "required_output_rosters"
        ]["failure_group_ids"]
        self.assertEqual(
            diagnostics["source_absence_proof_invalid_group_ids"],
            required_ids,
        )
        self.assertEqual(
            diagnostics["source_absence_proof_valid_group_ids"], []
        )
        self.assertFalse(
            review.failure_assessments[0].source_absence_claim_allowed
        )
        self.assertNotEqual(
            review.failure_assessments[0].classification,
            "SOURCE_ABSENCE_CANDIDATE",
        )

    def test_supervisor_absence_permission_class_mismatch_is_identified(
        self,
    ) -> None:
        provider = Phase87CorrectingSupervisorProvider(
            "ABSENCE_PERMISSION_CLASS_MISMATCH"
        )
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs(
                prior_failures=(
                    {
                        "failure_id": "FAIL-PARSER-PERMISSION",
                        "failure_reason": "PDF_PARSER_TABLE_EXTRACTION_FAILED",
                        "absence_eligible": False,
                    },
                )
            )
        )

        diagnostics = provider.calls[1]["payload"][
            "supervisor_validation_retry_context"
        ]["failure_assessment_roster_diagnostics"]
        required_ids = provider.calls[0]["payload"][
            "required_output_rosters"
        ]["failure_group_ids"]
        self.assertEqual(
            diagnostics[
                "source_absence_permission_class_mismatch_group_ids"
            ],
            required_ids,
        )
        self.assertEqual(
            review.failure_assessments[0].classification,
            "PARSER_EXTRACTOR_FAILURE",
        )
        self.assertFalse(
            review.failure_assessments[0].source_absence_claim_allowed
        )

    def test_counter_route_requires_executed_source_graph_lineage(self) -> None:
        review = ResearchSupervisor(
            provider=Phase87SupervisorProvider("FORCE_READY")
        ).review_epoch(
            **_supervisor_inputs(
                counter_proof=(
                    {
                        "objective_id": OBJECTIVE_ID,
                        "route_kind": "COUNTER_AND_SUPERSESSION",
                        "query_id": "INVENTED-QUERY",
                    },
                )
            )
        )
        self.assertEqual(review.status, "NEXT_RESEARCH_REQUIRED")
        self.assertIn("counter/supersession", review.rationale)

    def test_counter_route_builder_requires_query_document_extractor_fact_lineage(
        self,
    ) -> None:
        source = _source_checkpoint()
        proof = build_counter_and_supersession_route_proof(
            source_graph_checkpoint=source,
            document_dispositions=(
                {
                    "document_id": "DOC-1",
                    "status": "FACTS_EXTRACTED",
                    "rationale": "fixture facts extracted",
                },
            ),
            evidence_facts=_route_facts(),
            required_objective_ids=(OBJECTIVE_ID,),
        )
        self.assertEqual(
            {(row["objective_id"], row["route_kind"]) for row in proof},
            {
                (OBJECTIVE_ID, "COUNTER"),
                (OBJECTIVE_ID, "SUPERSESSION"),
            },
        )
        ready = ResearchSupervisor(
            provider=Phase87SupervisorProvider("READY")
        ).review_epoch(
            **_supervisor_inputs(counter_proof=proof)
        )
        self.assertEqual(
            ready.status,
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
        )

        bad_disposition = build_counter_and_supersession_route_proof(
            source_graph_checkpoint=source,
            document_dispositions=(
                {
                    "document_id": "DOC-1",
                    "status": "UNREADABLE",
                    "rationale": "fixture unreadable",
                },
            ),
            evidence_facts=_route_facts(),
            required_objective_ids=(OBJECTIVE_ID,),
        )
        self.assertEqual(bad_disposition, ())
        missing_supersession = tuple(
            row for row in proof if row["route_kind"] != "SUPERSESSION"
        )
        pending = ResearchSupervisor(
            provider=Phase87SupervisorProvider("FORCE_READY")
        ).review_epoch(
            **_supervisor_inputs(counter_proof=missing_supersession)
        )
        self.assertEqual(pending.status, "NEXT_RESEARCH_REQUIRED")

    def test_completed_memo_uncertainty_and_red_team_monitoring_are_not_open_gaps(
        self,
    ) -> None:
        components = _components(
            uncertainties=("공개되지 않은 세부 수치는 점수 상단 제한 요인이다.",)
        )
        red_team = _red_team(
            unresolved_challenges=(
                "이미 점수에 반영한 공급 지속기간은 다음 실적에서 계속 감시한다.",
            )
        )
        inputs = _supervisor_inputs()
        inputs["component_results"] = components
        inputs["red_team_result"] = red_team
        inputs["synthesis_result"] = _synthesis(
            components,
            red_team_result=red_team,
        )
        ready = ResearchSupervisor(
            provider=Phase87SupervisorProvider("READY")
        ).review_epoch(**inputs)
        self.assertEqual(
            ready.status,
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
        )

        gap_inputs = dict(inputs)
        pending = ResearchSupervisor(
            provider=Phase87SupervisorProvider("GAP")
        ).review_epoch(**gap_inputs)
        self.assertEqual(pending.status, "NEXT_RESEARCH_REQUIRED")
        self.assertFalse(pending.component_memos_sufficient)

    def test_structured_complete_label_without_records_cannot_open_saturation(self) -> None:
        empty = StructuredResearchResult(
            status="COMPLETE",
            records=(),
            covered_roles_by_component={},
            missing_roles_by_component={},
            fallback_routes_required=(),
        )
        review = ResearchSupervisor(
            provider=Phase87SupervisorProvider("FORCE_READY")
        ).review_epoch(**_supervisor_inputs(structured=empty))
        self.assertEqual(review.status, "NEXT_RESEARCH_REQUIRED")
        self.assertIn("structured-data", review.rationale)

    def test_source_checkpoint_hash_and_future_date_are_validated(self) -> None:
        source = _source_checkpoint()
        self.assertEqual(validate_source_graph_checkpoint(source), source)
        tampered = dict(source)
        tampered["status"] = "STOPPED_ON_RESOLUTION"
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            validate_source_graph_checkpoint(tampered)
        future = _source_checkpoint(document_date="2026-06-30")
        with self.assertRaisesRegex(ValueError, "future document"):
            validate_source_graph_checkpoint(future)

    def test_duplicate_provider_prompt_cannot_certify_independence(self) -> None:
        reviews = tuple(
            _manual_saturation_review(
                role,
                prompt_hash="SAME-PROMPT",
            )
            for role in SATURATION_REVIEW_ROLES
        )
        certificate = SemanticSaturationCertifier().certify(
            reviews,
            expected_checkpoint_id="CHECKPOINT",
            require_provider_reviews=True,
        )
        self.assertFalse(certificate.semantic_saturation_certified)
        self.assertIn("DUPLICATE_SATURATION_PROMPT_HASH", certificate.pending_reasons)

    def test_fixed_round_zero_result_and_transport_flags_are_rejected(self) -> None:
        base = _manual_saturation_review(SATURATION_REVIEW_ROLES[0])
        for field in (
            "fixed_round_completion_used",
            "zero_search_result_treated_as_saturation",
            "transport_budget_treated_as_saturation",
        ):
            with self.assertRaisesRegex(ValueError, "cannot prove saturation"):
                replace(base, **{field: True})


def _epoch_inputs(
    *,
    source_checkpoint: Mapping[str, Any],
    facts: Sequence[EvidenceFact] | None = None,
    components: Sequence[ComponentResearchResult] | None = None,
    counter_proof: Sequence[Mapping[str, Any]] | None = None,
    prior_checkpoint: Any | None = None,
) -> Mapping[str, Any]:
    component_results = tuple(components or _components())
    red_team_result = _red_team()
    return {
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "component_results": component_results,
        "red_team_result": red_team_result,
        "synthesis_result": _synthesis(
            component_results,
            red_team_result=red_team_result,
        ),
        "structured_result": _structured(),
        "evidence_facts": tuple(facts or _route_facts()),
        "source_graph_checkpoint": source_checkpoint,
        "open_objectives": (_objective(),),
        "prior_failures": (),
        "counter_and_supersession_route_proof": tuple(
            counter_proof if counter_proof is not None else _counter_proof()
        ),
        "prior_checkpoint": prior_checkpoint,
    }


def _supervisor_inputs(
    *,
    prior_failures: Sequence[Mapping[str, Any]] = (),
    counter_proof: Sequence[Mapping[str, Any]] | None = None,
    structured: StructuredResearchResult | None = None,
    components: Sequence[ComponentResearchResult] | None = None,
    synthesis: SynthesisResult | None = None,
    red_team: RedTeamResearchResult | None = None,
) -> Mapping[str, Any]:
    component_results = tuple(components or _components())
    red_team_result = red_team or _red_team()
    return {
        "epoch": 1,
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "component_results": component_results,
        "red_team_result": red_team_result,
        "synthesis_result": synthesis
        or _synthesis(
            component_results,
            red_team_result=red_team_result,
        ),
        "structured_result": structured or _structured(),
        "evidence_facts": _route_facts(),
        "source_graph_checkpoint": _source_checkpoint(),
        "open_objectives": (_objective(),),
        "prior_failures": tuple(prior_failures),
        "counter_and_supersession_route_proof": tuple(
            counter_proof if counter_proof is not None else _counter_proof()
        ),
    }


def _components(
    *,
    summary_suffix: str = "v1",
    change_only_first: bool = False,
    fact_id: str = "FACT-1",
    uncertainties: tuple[str, ...] = (),
) -> tuple[ComponentResearchResult, ...]:
    rows = []
    for index, component_id in enumerate(CANONICAL_COMPONENT_ORDER):
        suffix = summary_suffix if not change_only_first or index == 0 else "v1"
        maximum = float(CANONICAL_COMPONENT_MAX_POINTS[component_id])
        memo = ComponentResearchMemo(
            memo_id=f"MEMO-{component_id}-{suffix}",
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            component_id=component_id,
            component_max_points=maximum,
            positive_fact_ids=(fact_id,),
            counter_fact_ids=(),
            resolution_fact_ids=(),
            structured_metrics={"fixture_metric": 1.0},
            historical_anchor_ids=(),
            researcher_summary=f"현재 사실과 구조화 지표를 종합했다 {suffix}",
            positive_case="현재 positive fact의 경제적 전달 경로가 확인된다.",
            counter_case="독립 red team에서 반증 경로를 함께 확인했다.",
            uncertainties=uncertainties,
            source_coverage=("ISSUER_PRESENTATION",),
            proposed_score_lower=maximum * 0.30,
            proposed_score_mid=maximum * 0.40,
            proposed_score_upper=maximum * 0.50,
            confidence=0.75,
            research_complete=True,
            nearest_positive_anchor_ids=(),
            nearest_counter_anchor_ids=(),
            why_not_higher="추가 독립 확인 여지를 반영했다.",
            why_not_lower="현재 source-backed fact가 존재한다.",
            researcher_role=f"TEST-{component_id}",
        )
        rows.append(
            ComponentResearchResult(
                component_id=component_id,
                researcher_role=memo.researcher_role,
                status="COMPLETE",
                memo=memo,
                pending_reasons=(),
                provider_name="PHASE87_COMPONENT_FIXTURE",
                prompt_hash=f"PROMPT-{component_id}-{suffix}",
            )
        )
    return tuple(rows)


def _fact(
    fact_id: str,
    *,
    direction: str = "POSITIVE",
    current_lifecycle: str = "CURRENT",
) -> EvidenceFact:
    return EvidenceFact(
        fact_id=fact_id,
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        subject="current target business",
        business_segment="core segment",
        product_family="core product",
        economic_mechanism="earnings convert into free cash flow",
        predicate="cash_conversion_confirmed",
        value=True,
        unit=None,
        period="2026Q2",
        direction=direction,
        source_ids=("DOC-1",),
        claim_ids=(f"CLAIM-{fact_id}",),
        quote_ids=(f"QUOTE-{fact_id}",),
        current_lifecycle=current_lifecycle,
        source_independence_group="ISSUER",
        confidence=0.85,
    )


def _route_facts() -> tuple[EvidenceFact, ...]:
    return (
        _fact("FACT-1"),
        _fact("FACT-COUNTER", direction="COUNTER"),
        _fact(
            "FACT-SUPERSESSION",
            direction="RESOLUTION",
            current_lifecycle="RESOLVED",
        ),
    )


def _red_team(
    *,
    unresolved_challenges: tuple[str, ...] = (),
) -> RedTeamResearchResult:
    memo = RedTeamMemo(
        memo_id="RED-TEAM-MEMO",
        target_id=TARGET,
        archetype_id=ARCHETYPE,
        reviewed_component_ids=tuple(CANONICAL_COMPONENT_ORDER),
        challenged_fact_ids=("FACT-1",),
        counter_fact_ids=(),
        resolved_challenges=("counter and supersession routes checked",),
        unresolved_challenges=unresolved_challenges,
        recommended_research_directions=(),
        source_coverage=("ISSUER_PRESENTATION", "CUSTOMER_OFFICIAL"),
        confidence=0.8,
        review_complete=True,
    )
    return RedTeamResearchResult(
        status="COMPLETE",
        memo=memo,
        pending_reasons=(),
        provider_name="PHASE87_RED_TEAM_FIXTURE",
    )


def _synthesis(
    components: Sequence[ComponentResearchResult] | None = None,
    *,
    memo_id: str = "SYNTHESIS-MEMO-v1",
    target_id: str = TARGET,
    archetype_id: str = ARCHETYPE,
    red_team_result: RedTeamResearchResult | None = None,
) -> SynthesisResult:
    component_results = tuple(components or _components())
    current_red_team_result = red_team_result or _red_team()
    assert current_red_team_result.memo is not None
    memo = SynthesisMemo(
        memo_id=memo_id,
        target_id=target_id,
        archetype_id=archetype_id,
        component_memo_ids=tuple(
            row.memo.memo_id for row in component_results if row.memo is not None
        ),
        red_team_memo_id=current_red_team_result.memo.memo_id,
        red_team_memo_hash=_stable_test_hash(
            current_red_team_result.memo.to_dict()
        ),
        cross_component_support=("7개 component의 현재 근거가 함께 수렴한다.",),
        cross_component_tensions=("현금 전환의 지속기간은 계속 검토한다.",),
        unresolved_material_questions=(),
        synthesis_summary="현재 7개 component와 red-team 결과를 종합했다.",
        confidence=0.8,
        synthesis_complete=True,
    )
    return SynthesisResult(
        status="COMPLETE",
        memo=memo,
        pending_reasons=(),
        provider_name="PHASE87_SYNTHESIS_FIXTURE",
    )


def _stable_test_hash(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        default=str,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _structured() -> StructuredResearchResult:
    record = StructuredMetricRecord(
        record_id="STRUCTURED-FCF",
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        metric_id="free_cash_flow",
        value=120.0,
        unit="KRW_BN",
        period="2026Q2",
        evidence_roles=("FREE_CASH_FLOW",),
        source_ids=("DOC-1",),
        source_route="OPENDART",
        observed_at="2026-06-20",
        record_kind="ACTUAL",
        confidence=0.9,
        dataset="FINANCIAL",
        provenance="STRUCTURED_EXTRACTED",
    )
    return StructuredResearchResult(
        status="COMPLETE",
        records=(record,),
        covered_roles_by_component={"eps_fcf_explosion": ("FREE_CASH_FLOW",)},
        missing_roles_by_component={"eps_fcf_explosion": ()},
        fallback_routes_required=(),
    )


def _objective() -> Mapping[str, Any]:
    return {
        "objective_id": OBJECTIVE_ID,
        "component_id": "eps_fcf_explosion",
        "research_objective": "현재 earnings와 cash conversion의 지속성 검토",
        "preferred_source_families": [
            "ISSUER_PRESENTATION",
            "CUSTOMER_OFFICIAL",
        ],
        "counter_or_supersession_required": True,
    }


def _counter_proof() -> tuple[Mapping[str, Any], ...]:
    return (
        {
            "objective_id": OBJECTIVE_ID,
            "route_kind": "COUNTER",
            "query_id": "Q-COUNTER",
            "document_id": "DOC-1",
            "fact_id": "FACT-COUNTER",
            "parser_extractor_verified": True,
        },
        {
            "objective_id": OBJECTIVE_ID,
            "route_kind": "SUPERSESSION",
            "query_id": "Q-SUPERSESSION",
            "document_id": "DOC-1",
            "fact_id": "FACT-SUPERSESSION",
            "parser_extractor_verified": True,
        },
    )


def _source_checkpoint(
    *,
    zero_results: bool = False,
    extra_epoch: bool = False,
    with_queries: bool = True,
    with_document: bool = True,
    quarantine_document: bool = False,
    document_date: str = "2026-06-20",
) -> Mapping[str, Any]:
    if quarantine_document and not with_document:
        raise ValueError("quarantine_document already removes the active document")
    if zero_results:
        queries = [
            {
                "query_id": "Q-ZERO",
                "objective_id": OBJECTIVE_ID,
                "literal_query": "current target counter supersession evidence",
                "source_families": ["ISSUER_PRESENTATION"],
                "counter_or_supersession_search": True,
                "execution_status": "NO_RESULT",
                "search_result_count": 0,
            }
        ]
        documents: list[Mapping[str, Any]] = []
        failures = [
            {
                "query_id": "Q-ZERO",
                "objective_id": OBJECTIVE_ID,
                "failure_reason": "SEARCH_NO_RESULT_NOT_SATURATION",
            }
        ]
    else:
        queries = (
            [
                {
                    "query_id": "Q-COUNTER",
                    "objective_id": OBJECTIVE_ID,
                    "literal_query": "current target counter evidence",
                    "source_families": ["ISSUER_PRESENTATION"],
                    "counter_or_supersession_search": True,
                    "execution_status": "SEARCH_EXECUTED",
                    "search_result_count": 1,
                },
                {
                    "query_id": "Q-SUPERSESSION",
                    "objective_id": OBJECTIVE_ID,
                    "literal_query": "current target supersession evidence",
                    "source_families": ["CUSTOMER_OFFICIAL"],
                    "counter_or_supersession_search": True,
                    "execution_status": "SEARCH_EXECUTED",
                    "search_result_count": 1,
                },
            ]
            if with_queries
            else []
        )
        documents = [
            {
                "document_id": "DOC-1",
                "target_id": TARGET,
                "published_at": document_date,
                "source_family": "ISSUER_PRESENTATION",
                "query_ids": ["Q-COUNTER", "Q-SUPERSESSION"],
                "objective_ids": [OBJECTIVE_ID],
                "evidence_eligible": True,
                "full_fetch_performed": True,
                "snippet_only": False,
                "full_text": "source-backed current evidence and counter evidence",
            }
        ] if with_document and not quarantine_document else []
        failures = []
    if extra_epoch:
        queries.append(
            {
                "query_id": "Q-NEW",
                "objective_id": OBJECTIVE_ID,
                "literal_query": "current target newly directed source",
                "source_families": ["CUSTOMER_OFFICIAL"],
                "counter_or_supersession_search": False,
                "execution_status": "SEARCH_EXECUTED",
                "search_result_count": 1,
            }
        )
        documents.append(
            {
                "document_id": "DOC-2",
                "target_id": TARGET,
                "published_at": "2026-06-21",
                "source_family": "CUSTOMER_OFFICIAL",
                "full_text": "new source-backed fact",
            }
        )
    state: dict[str, Any] = {
        "schema_version": "e2r_v5_source_graph_checkpoint_v1",
        "target_id": TARGET,
        "target_name": "Current Target",
        "as_of_date": AS_OF_DATE,
        "mode": "TEST",
        "epoch": 2 if extra_epoch else 1,
        "status": "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
        "resumed_from_checkpoint_id": None,
        "generated_queries": queries,
        "executed_queries": [row["literal_query"] for row in queries],
        "query_failures": failures,
        "search_candidates": [],
        "candidate_materiality_decisions": [],
        "fetch_records": [],
        "evidence_documents": documents,
        "rejected_documents": (
            [
                {
                    "schema_version": "e2r_v5_source_graph_rejection_v1",
                    "rejection_id": "REJECT-DOC-1",
                    "candidate_id": "CAND-DOC-1",
                    "document_id": "DOC-1",
                    "url": "https://issuer.example.com/unreadable.pdf",
                    "query_ids": ["Q-COUNTER"],
                    "objective_ids": [OBJECTIVE_ID],
                    "rejection_reason": (
                        "UNREADABLE_FULL_DOCUMENT_TEXT:"
                        "excessive_control_characters:90/100"
                    ),
                    "retryable": False,
                    "content_hash": "a" * 64,
                    "evidence_eligible": False,
                    "accepted_claim_ids": [],
                    "score_authority": False,
                }
            ]
            if quarantine_document
            else []
        ),
        "quarantined_documents": (
            [
                {
                    "schema_version": "e2r_v5_source_graph_quarantine_v1",
                    "document_id": "DOC-1",
                    "candidate_id": "CAND-DOC-1",
                    "url": "https://issuer.example.com/unreadable.pdf",
                    "content_hash": "a" * 64,
                    "query_ids": ["Q-COUNTER"],
                    "objective_ids": [OBJECTIVE_ID],
                    "quarantine_reason": (
                        "UNREADABLE_FULL_DOCUMENT_TEXT:"
                        "excessive_control_characters:90/100"
                    ),
                    "evidence_eligible": False,
                    "score_authority": False,
                }
            ]
            if quarantine_document
            else []
        ),
        "resolved_objective_ids": [],
        "pending_reasons": [],
        "source_graph": {},
        "semantic_saturation_certified": False,
        "production_score_authority": False,
        "parser_field_direct_score_authority": False,
        "snippet_evidence_allowed": False,
        "transport_budget_can_complete_research": False,
    }
    encoded = json.dumps(
        state,
        ensure_ascii=False,
        sort_keys=True,
        default=str,
    ).encode("utf-8")
    checkpoint_hash = hashlib.sha256(encoded).hexdigest()
    state["checkpoint_hash"] = checkpoint_hash
    state["checkpoint_id"] = stable_intelligence_id(
        "SGCHECK",
        {
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "epoch": state["epoch"],
            "checkpoint_hash": checkpoint_hash,
        },
    )
    return state


def _source_checkpoint_with_updates(
    checkpoint: Mapping[str, Any],
    **updates: Any,
) -> Mapping[str, Any]:
    state = dict(checkpoint)
    state.update(updates)
    state.pop("checkpoint_hash", None)
    state.pop("checkpoint_id", None)
    encoded = json.dumps(
        state,
        ensure_ascii=False,
        sort_keys=True,
        default=str,
    ).encode("utf-8")
    checkpoint_hash = hashlib.sha256(encoded).hexdigest()
    state["checkpoint_hash"] = checkpoint_hash
    state["checkpoint_id"] = stable_intelligence_id(
        "SGCHECK",
        {
            "target_id": state["target_id"],
            "as_of_date": state["as_of_date"],
            "epoch": state["epoch"],
            "checkpoint_hash": checkpoint_hash,
        },
    )
    return state


def _manual_saturation_review(
    role: str,
    *,
    prompt_hash: str | None = None,
) -> SaturationReview:
    return SaturationReview(
        review_id=f"REVIEW-{role}",
        reviewer_role=role,
        approve=True,
        seven_component_memos_complete=True,
        material_positive_routes_reviewed=True,
        counter_and_supersession_routes_checked=True,
        structured_data_complete=True,
        new_source_family_directions_reviewed=True,
        unresolved_material_questions=(),
        rationale="all semantic routes independently reviewed",
        checkpoint_id="CHECKPOINT",
        epoch=1,
        provider_name=f"PROVIDER-{role}",
        prompt_hash=prompt_hash or f"PROMPT-{role}",
        provider_backed=True,
    )


if __name__ == "__main__":
    unittest.main()
