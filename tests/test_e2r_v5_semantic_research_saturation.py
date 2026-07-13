from __future__ import annotations

import hashlib
import inspect
import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.researcher_mode import (
    CANONICAL_COMPONENT_MAX_POINTS,
    CANONICAL_COMPONENT_ORDER,
    PHASE87_PASS,
    RESEARCH_EPOCH_OUTPUT_FILES,
    RESEARCH_SUPERVISOR_SCHEMA,
    SATURATION_REVIEW_ROLES,
    SEMANTIC_SATURATION_REVIEW_SCHEMA,
    ComponentResearchMemo,
    ComponentResearchResult,
    EvidenceFact,
    RedTeamMemo,
    RedTeamResearchResult,
    ResearchEpochRunner,
    ResearchSupervisor,
    SaturationReview,
    SemanticSaturationCertifier,
    SemanticSaturationReviewer,
    StructuredMetricRecord,
    StructuredResearchResult,
    compile_phase87_semantic_research_saturation_audit,
    load_research_epoch_checkpoint,
    validate_source_graph_checkpoint,
    validated_quarantined_document_ids,
    write_research_epoch_run,
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
        structured_payload = payload.get("structured_result") or {}
        structured_complete = bool(
            structured_payload.get("status") == "COMPLETE"
            and structured_payload.get("records")
        )
        findings = []
        for index, component_id in enumerate(CANONICAL_COMPONENT_ORDER):
            sufficient = not (gap_mode and index == 0)
            findings.append(
                {
                    "component_id": component_id,
                    "memo_sufficient": sufficient,
                    "missing_fact_needs": (
                        [] if sufficient else ["현금 전환의 지속성 원천 사실"]
                    ),
                    "rationale": "현재 memo의 사실·반증·구조화 지표를 검토했다.",
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
        operational_gap = gap_mode or parser_mode or absence_mode
        ready = bool(
            (self.mode == "READY" and structured_complete and not assessments)
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
            "component_memos_sufficient": not gap_mode,
            "reasonable_positive_routes_remaining": not ready,
            "ready_for_independent_saturation_review": ready,
            "rationale": (
                "모든 합리적 조사 방향을 검토했다."
                if ready
                else "아직 semantic research gap이 남아 있다."
            ),
        }


class Phase87SaturationProvider:
    def __init__(self, name: str, *, unresolved: bool = False) -> None:
        self.provider_name = name
        self.unresolved = unresolved
        self.calls: list[Mapping[str, Any]] = []

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        self.calls.append({"pass_name": pass_name, "payload": payload})
        if pass_name != "SEMANTIC_SATURATION_REVIEW":
            raise AssertionError(pass_name)
        return {
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

    def test_checkpoint_resume_records_only_deltas_and_returns_prior_review(self) -> None:
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
        self.assertEqual(second.checkpoint.retired_fact_ids, ("FACT-1",))
        self.assertEqual(
            set(second.checkpoint.cumulative_fact_ids), {"FACT-1", "FACT-2"}
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
            supervisor_source_graph["quarantined_documents"][0]["document_id"],
            "DOC-1",
        )
        self.assertEqual(
            supervisor_source_graph["source_graph_prompt_projection"][
                "schema_version"
            ],
            "e2r_v5_supervisor_source_graph_projection_v1",
        )
        self.assertEqual(
            supervisor_payload["current_evidence_fact_graph"]["record_count"],
            1,
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

    def test_provider_outage_is_pending_and_never_builds_fallback_query(self) -> None:
        provider = Phase87SupervisorProvider("ERROR")
        review = ResearchSupervisor(provider=provider).review_epoch(
            **_supervisor_inputs()
        )
        self.assertEqual(review.status, "NEXT_RESEARCH_REQUIRED")
        context = review.to_score_gap_context()
        self.assertEqual(context["query_direction_briefs"], [])
        self.assertNotIn("suggested_queries", context)

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
    return {
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "component_results": tuple(components or _components()),
        "red_team_result": _red_team(),
        "structured_result": _structured(),
        "evidence_facts": tuple(facts or (_fact("FACT-1"),)),
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
) -> Mapping[str, Any]:
    return {
        "epoch": 1,
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "component_results": _components(),
        "red_team_result": _red_team(),
        "structured_result": structured or _structured(),
        "evidence_facts": (_fact("FACT-1"),),
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
            uncertainties=(),
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


def _fact(fact_id: str) -> EvidenceFact:
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
        direction="POSITIVE",
        source_ids=("DOC-1",),
        claim_ids=(f"CLAIM-{fact_id}",),
        quote_ids=(f"QUOTE-{fact_id}",),
        current_lifecycle="CURRENT",
        source_independence_group="ISSUER",
        confidence=0.85,
    )


def _red_team() -> RedTeamResearchResult:
    memo = RedTeamMemo(
        memo_id="RED-TEAM-MEMO",
        target_id=TARGET,
        archetype_id=ARCHETYPE,
        reviewed_component_ids=tuple(CANONICAL_COMPONENT_ORDER),
        challenged_fact_ids=("FACT-1",),
        counter_fact_ids=(),
        resolved_challenges=("counter and supersession routes checked",),
        unresolved_challenges=(),
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
            "parser_extractor_verified": True,
        },
        {
            "objective_id": OBJECTIVE_ID,
            "route_kind": "SUPERSESSION",
            "query_id": "Q-SUPERSESSION",
            "document_id": "DOC-1",
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
        gold_critical_fact_miss_count=0,
        rationale="all semantic routes independently reviewed",
        checkpoint_id="CHECKPOINT",
        epoch=1,
        provider_name=f"PROVIDER-{role}",
        prompt_hash=prompt_hash or f"PROMPT-{role}",
        provider_backed=True,
    )


if __name__ == "__main__":
    unittest.main()
