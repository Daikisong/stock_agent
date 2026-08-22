from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.gaps.adjudicator import (
    DeterministicGapContext,
    ProGapAdjudicator,
)
from e2r.pro_first.gaps.service import ProGapAdjudicationService
from e2r.pro_first.gaps.supplemental_planner import (
    MaterialGapSupplementalPlanner,
)
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.ids import canonical_hash, canonical_json
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.state_machine import TransitionContext
from e2r.pro_first.dossier.validator import CANONICAL_COMPONENT_IDS
from e2r.research_brain.researcher_mode.evidence_gap import (
    EvidenceGapDisposition,
    RepeatedExhaustedGapReopenedError,
)


class ProFirstGapAdjudicationTest(unittest.TestCase):
    archetype_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.store = ProFirstJobStore(
            Path(self.temporary_directory.name) / "gap.sqlite3",
            now=lambda: datetime(2026, 8, 22, 3, 4, 5, tzinfo=timezone.utc),
        )
        candidate = self.store.create_candidate(
            symbol="123456",
            company_name="검증기업",
            as_of_date="2026-08-22",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="gap-trigger",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        self.job = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=(self.archetype_id,),
        )
        self.adjudicator = ProGapAdjudicator()
        self.planner = MaterialGapSupplementalPlanner()

    def _gap(
        self,
        *,
        gap_id: str = "PROGAP-001",
        component_id: str = "earnings_visibility",
        source_family: str = "CUSTOMER_OFFICIAL",
        proposed_gap_class: str = "CORROBORATION_CAP",
    ) -> dict:
        return {
            "dossier_gap_id": gap_id,
            "archetype_id": self.archetype_id,
            "stable_objective_id": None,
            "affected_component_ids": [component_id],
            "required_source_families": [source_family],
            "economic_mechanism_id": "CUSTOMER_COMMITMENT_VISIBILITY",
            "predicate_or_fact_need_id": "DIRECT_CONTRACT_TERMS",
            "economic_reason": "직접 계약 조건의 원문 확인이 남았다.",
            "proposed_gap_class": proposed_gap_class,
            "proposed_missing_source_role": "INDEPENDENT_CORROBORATION",
            "proposed_could_change_score": False,
            "proposed_could_change_stage": False,
            "proposed_could_change_hard_break": False,
        }

    @staticmethod
    def _dossier(gap: dict) -> dict:
        return {"unresolved_gaps": [gap]}

    def _verified_fact(self, component_id: str = "earnings_visibility") -> dict:
        return {
            "fact_id": "EFACT-current",
            "target_id": self.job.symbol,
            "as_of_date": self.job.as_of_date,
            "predicate": (
                "SOURCE_LINEAGE"
                if component_id == "information_confidence"
                else "FCF_ACTUAL"
            ),
            "structured_evidence_roles": (),
            "primitive_tags": (),
            "question_family_tags": (),
            "allowed_component_ids": [component_id],
            "current_lifecycle": "CURRENT",
        }

    @staticmethod
    def _claim_link(component_id: str = "earnings_visibility") -> dict:
        return {
            "link_id": f"CFLINK-{component_id}",
            "claim_id": f"CLAIM-{component_id}",
            "fact_id": "EFACT-current",
            "economic_fact_key": f"EKEY-{component_id}",
            "link_role": "PRIMARY_FACT_CLAIM",
            "material_claim": True,
            "claim_confidence": 0.9,
            "current_lifecycle": "CURRENT",
            "source_ids": ["PROSRC-current"],
            "source_independence_group": "PROSRCGROUP-issuer",
            "resolves_fact_ids": [],
            "supersedes_fact_ids": [],
            "production_score_authority": False,
        }

    @staticmethod
    def _context(
        *,
        gap_id: str = "PROGAP-001",
        component_id: str = "earnings_visibility",
        lower_stage: str | None = "2",
        upper_stage: str | None = "2",
        routes: tuple[str, ...] = (),
        hard_break: bool = False,
        monitoring_only: bool = False,
        provider_failure: bool = False,
    ) -> DeterministicGapContext:
        return DeterministicGapContext(
            dossier_gap_id=gap_id,
            component_lower_delta={component_id: 0.0},
            component_upper_delta={component_id: 2.0},
            deterministic_lower_stage=lower_stage,
            deterministic_upper_stage=upper_stage,
            executable_new_source_route_signatures=routes,
            provider_or_parser_failure=provider_failure,
            direct_contradiction_or_hard_break_unresolved=hard_break,
            could_change_score=not monitoring_only,
            monitoring_only=monitoring_only,
            rationale="기존 deterministic score/Stage 경계 계산 결과",
        )

    def _adjudicate(
        self,
        gap: dict,
        context: DeterministicGapContext,
        *,
        with_verified_fact: bool,
        prior_dispositions=(),
    ):
        component = gap["affected_component_ids"][0]
        facts = [self._verified_fact(component)] if with_verified_fact else []
        links = [self._claim_link(component)] if with_verified_fact else []
        return self.adjudicator.adjudicate(
            dossier=self._dossier(gap),
            job=self.job,
            verified_facts=facts,
            claim_fact_links=links,
            deterministic_contexts={gap["dossier_gap_id"]: context},
            prior_dispositions=prior_dispositions,
        )

    def test_core_gap_allows_supplement(self) -> None:
        gap = self._gap(
            source_family="CASH_FLOW",
            proposed_gap_class="MONITORING_GAP",
        )
        context = self._context(routes=("CASH_FLOW:official",))
        result = self._adjudicate(
            gap,
            context,
            with_verified_fact=False,
        )
        decision = result.decisions[0]
        self.assertEqual(decision.assessment.gap_class.value, "CORE_SCORE_BLOCKER")
        self.assertEqual(decision.planner_label, "CORE_SCORE_BLOCKER")
        self.assertTrue(decision.supplemental_allowed)
        plan = self.planner.plan(adjudication=result, job=self.job)
        self.assertEqual(len(plan.tasks), 1)
        self.assertEqual(plan.tasks[0].source_task.max_queries, 3)
        self.assertEqual(plan.tasks[0].source_task.max_candidates, 20)
        self.assertEqual(plan.tasks[0].source_task.max_fetches, 6)

    def test_stage_boundary_gap_allows_supplement(self) -> None:
        gap = self._gap(proposed_gap_class="MONITORING_GAP")
        context = self._context(
            lower_stage="2",
            upper_stage="3-Green",
            routes=("CUSTOMER_OFFICIAL:new-route",),
        )
        result = self._adjudicate(gap, context, with_verified_fact=True)
        decision = result.decisions[0]
        self.assertEqual(
            decision.assessment.gap_class.value,
            "CORROBORATION_CAP",
        )
        self.assertEqual(decision.planner_label, "STAGE_BOUNDARY_GAP")
        self.assertTrue(decision.supplemental_allowed)
        self.assertEqual(
            len(self.planner.plan(adjudication=result, job=self.job).tasks),
            1,
        )

    def test_hard_break_gap_allows_supplement(self) -> None:
        gap = self._gap(proposed_gap_class="CORROBORATION_CAP")
        context = self._context(
            routes=("CUSTOMER_OFFICIAL:counter-route",),
            hard_break=True,
        )
        result = self._adjudicate(gap, context, with_verified_fact=True)
        decision = result.decisions[0]
        self.assertEqual(decision.planner_label, "HARD_BREAK_GAP")
        self.assertEqual(decision.assessment.gap_class.value, "CORE_SCORE_BLOCKER")
        self.assertTrue(decision.supplemental_allowed)
        task = self.planner.plan(adjudication=result, job=self.job).tasks[0]
        self.assertEqual(task.source_task.task_type, "contradiction_resolution")

    def test_corroboration_gap_no_supplement(self) -> None:
        gap = self._gap(proposed_gap_class="CORE_SCORE_BLOCKER")
        result = self._adjudicate(
            gap,
            self._context(),
            with_verified_fact=True,
        )
        decision = result.decisions[0]
        self.assertEqual(decision.planner_label, "CORROBORATION_CAP")
        self.assertFalse(decision.supplemental_allowed)
        self.assertEqual(
            self.planner.plan(adjudication=result, job=self.job).tasks,
            (),
        )

    def test_monitoring_gap_no_supplement(self) -> None:
        gap = self._gap(
            component_id="information_confidence",
            proposed_gap_class="CORE_SCORE_BLOCKER",
        )
        context = self._context(
            component_id="information_confidence",
            monitoring_only=True,
        )
        result = self._adjudicate(gap, context, with_verified_fact=True)
        decision = result.decisions[0]
        self.assertEqual(decision.planner_label, "MONITORING_GAP")
        self.assertEqual(decision.assessment.gap_class.value, "MONITORING_GAP")
        self.assertFalse(decision.supplemental_allowed)
        self.assertEqual(
            self.planner.plan(adjudication=result, job=self.job).tasks,
            (),
        )

    def test_pro_gap_class_not_authoritative(self) -> None:
        gap = self._gap(
            source_family="CASH_FLOW",
            proposed_gap_class="MONITORING_GAP",
        )
        result = self._adjudicate(
            gap,
            self._context(routes=("CASH_FLOW:official",)),
            with_verified_fact=False,
        )
        row = result.decisions[0].to_dict()
        self.assertEqual(row["pro_proposed_gap_class"], "MONITORING_GAP")
        self.assertEqual(row["deterministic_evidence_class"], "CORE_SCORE_BLOCKER")
        self.assertFalse(row["pro_proposal_authoritative"])
        self.assertFalse(row["production_score_authority"])
        self.assertFalse(row["production_stage_authority"])

    def test_full_research_restart_count_zero(self) -> None:
        gap = self._gap(source_family="CASH_FLOW")
        result = self._adjudicate(
            gap,
            self._context(routes=("CASH_FLOW:official",)),
            with_verified_fact=False,
        )
        plan = self.planner.plan(adjudication=result, job=self.job)
        self.assertEqual(result.receipt_payload["full_research_restart_count"], 0)
        self.assertEqual(plan.receipt_payload["full_research_restart_count"], 0)
        self.assertEqual(plan.receipt_payload["prohibited_gap_task_count"], 0)
        self.assertEqual(plan.receipt_payload["deterministic_query_template_count"], 0)

    def test_same_gap_third_reopen_hard_fail(self) -> None:
        gap = self._gap(source_family="CASH_FLOW")
        context = self._context(routes=("CASH_FLOW:official",))
        first = self._adjudicate(
            gap,
            context,
            with_verified_fact=False,
        )
        exhausted = EvidenceGapDisposition.unresolved(
            assessment=first.decisions[0].assessment,
            attempted_route_signatures=context.executable_new_source_route_signatures,
            no_new_route_confirmation_ids=("CONFIRM-1", "CONFIRM-2"),
        )
        with self.assertRaises(RepeatedExhaustedGapReopenedError):
            self._adjudicate(
                gap,
                context,
                with_verified_fact=False,
                prior_dispositions=(exhausted,),
            )

    def test_durable_empty_gap_service_moves_directly_to_components(self) -> None:
        root = Path(self.temporary_directory.name) / "durable-job"
        dossier = {
            "job_id": self.job.job_id,
            "unresolved_gaps": [],
        }
        self._prepare_source_verified(root=root, dossier=dossier)
        service = ProGapAdjudicationService(self.store)
        first = service.adjudicate_job(
            self.job.job_id,
            job_root=root,
            deterministic_contexts={},
        )
        second = service.adjudicate_job(
            self.job.job_id,
            job_root=root,
            deterministic_contexts={},
        )
        self.assertEqual(first.job.status, JobStatus.COMPONENT_RESEARCH.value)
        self.assertIsNotNone(first.adjudication)
        self.assertEqual(first.receipt["decision_count"], 0)
        self.assertEqual(first.receipt["supplemental_task_count"], 0)
        self.assertEqual(first.receipt["full_research_restart_count"], 0)
        self.assertIsNone(second.adjudication)
        self.assertEqual(first.receipt, second.receipt)
        self.assertEqual(self.store.get_gap_decisions(self.job.job_id), ())
        matching_events = [
            event
            for event in self.store.list_events(self.job.job_id)
            if event.to_status == JobStatus.COMPONENT_RESEARCH.value
        ]
        self.assertEqual(len(matching_events), 1)

    def test_durable_material_gap_records_one_bounded_task(self) -> None:
        root = Path(self.temporary_directory.name) / "durable-material-gap"
        gap = self._gap(
            source_family="CASH_FLOW",
            proposed_gap_class="MONITORING_GAP",
        )
        dossier = {
            "job_id": self.job.job_id,
            "unresolved_gaps": [gap],
        }
        self._prepare_source_verified(root=root, dossier=dossier)
        context = self._context(routes=("CASH_FLOW:official",))
        result = ProGapAdjudicationService(self.store).adjudicate_job(
            self.job.job_id,
            job_root=root,
            deterministic_contexts={gap["dossier_gap_id"]: context},
        )
        self.assertEqual(result.job.status, JobStatus.SUPPLEMENTAL_RESEARCH.value)
        self.assertEqual(result.receipt["decision_count"], 1)
        self.assertEqual(result.receipt["supplemental_task_count"], 1)
        durable = self.store.get_gap_decisions(self.job.job_id)
        self.assertEqual(len(durable), 1)
        self.assertEqual(durable[0]["planner_label"], "CORE_SCORE_BLOCKER")
        task_lines = (root / "gaps/supplemental_tasks.jsonl").read_text(
            encoding="utf-8"
        ).splitlines()
        self.assertEqual(len(task_lines), 1)
        self.assertIn('"max_queries":3', task_lines[0])
        self.assertIn('"max_candidates":20', task_lines[0])
        self.assertIn('"max_fetches":6', task_lines[0])

    def _prepare_source_verified(
        self,
        *,
        root: Path,
        dossier: dict,
        facts: tuple[dict, ...] = (),
        links: tuple[dict, ...] = (),
    ) -> None:
        self.job = self._advance_to_importing(self.job)
        normalized_hash = canonical_hash(dossier)
        import_root = root / "import"
        import_root.mkdir(parents=True, exist_ok=True)
        (import_root / "research_dossier.normalized.json").write_text(
            canonical_json(dossier) + "\n",
            encoding="utf-8",
        )
        dossier_id = "PRODOSSIER-gap-service"
        self.job = self.store.record_dossier_import(
            self.job.job_id,
            expected_version=self.job.state_version,
            dossier_id=dossier_id,
            dossier_hash=normalized_hash,
            import_receipt={
                "schema_version": "e2r_pro_dossier_import_receipt_v1",
                "job_id": self.job.job_id,
                "normalized_dossier_hash": normalized_hash,
                "validation_status": "PASS",
                "score_authority": False,
                "stage_authority": False,
                "evidence_promoted_count": 0,
                "component_ids": list(CANONICAL_COMPONENT_IDS),
            },
            actor="test",
            idempotency_key="durable-dossier-import",
        )
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=self.job.state_version,
            to_status=JobStatus.VERIFYING_SOURCES,
            actor="test",
            idempotency_key="durable-verifying",
        )
        verification_hash = canonical_hash({"facts": facts, "links": links})
        verification_id = "PROVERIFY-gap-service"
        verification_receipt = {
            "schema_version": "e2r_pro_source_verification_receipt_v1",
            "status": "SOURCE_VERIFICATION_COMPLETE",
            "job_id": self.job.job_id,
            "dossier_id": dossier_id,
            "verification_id": verification_id,
            "verification_hash": verification_hash,
            "normalized_dossier_hash": normalized_hash,
            "candidate_fact_count": len(facts),
            "terminal_fact_count": len(facts),
            "compiled_evidence_fact_count": len(facts),
            "query_count": 0,
            "search_count": 0,
            "pro_score_authority": False,
            "pro_stage_authority": False,
        }
        verification_root = root / "verification"
        verification_root.mkdir(parents=True, exist_ok=True)
        (verification_root / "source_verification_receipt.json").write_text(
            canonical_json(verification_receipt) + "\n",
            encoding="utf-8",
        )
        (verification_root / "evidence_facts.jsonl").write_text(
            "".join(canonical_json(row) + "\n" for row in facts),
            encoding="utf-8",
        )
        (verification_root / "claim_fact_links.jsonl").write_text(
            "".join(canonical_json(row) + "\n" for row in links),
            encoding="utf-8",
        )
        self.job = self.store.record_source_verification(
            self.job.job_id,
            expected_version=self.job.state_version,
            verification_id=verification_id,
            dossier_id=dossier_id,
            verification_hash=verification_hash,
            receipt=verification_receipt,
            actor="test",
            idempotency_key="durable-source-verification",
        )

    def _advance_to_importing(self, job):
        contexts = {
            JobStatus.SUBMITTING: TransitionContext(approval_nonce_consumed=True),
            JobStatus.IMPORTING: TransitionContext(capture_receipt_verified=True),
        }
        for index, target in enumerate(
            (
                JobStatus.PACKET_BUILDING,
                JobStatus.PACKET_READY,
                JobStatus.BROWSER_PREPARING,
                JobStatus.AWAITING_USER_APPROVAL,
                JobStatus.APPROVED,
                JobStatus.SUBMITTING,
                JobStatus.RESEARCH_RUNNING,
                JobStatus.RESULT_DETECTED,
                JobStatus.CAPTURING_ARTIFACTS,
                JobStatus.CAPTURE_COMPLETE,
                JobStatus.IMPORTING,
            )
        ):
            job = self.store.transition(
                job.job_id,
                expected_version=job.state_version,
                to_status=target,
                actor="test",
                idempotency_key=f"gap-service-{index}-{target.value}",
                context=contexts.get(target),
            )
        return job


if __name__ == "__main__":
    unittest.main()
