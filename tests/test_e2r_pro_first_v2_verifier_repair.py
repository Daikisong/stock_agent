from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.multi_pass import FollowupPassPlan, ProMultiPassResearchOrchestrator
from e2r.pro_first.repair import (
    ProVerifierRepairService,
    compile_rejection_packets,
    compile_verifier_repair_contract_audit,
)
from e2r.pro_first.repair.response_delta import (
    derive_repair_delta_from_dossier_response,
)
from e2r.pro_first.saturation import ResearchSaturationAdjudicator
from e2r.pro_first.verification.source_verifier import ProSourceVerifier
from e2r.research.page_fetcher import PageFetcher
from tests.test_e2r_pro_first_v2_saturation import _complete_dossier


ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
QUESTION = "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"


class ProFirstV2VerifierRepairTest(unittest.TestCase):
    target_id = "000660"
    company_name = "검증기업"
    as_of_date = "2026-08-22"
    url = "https://issuer.example/repair-source"
    excerpt = "검증기업은 MEMORY 사업의 HBM 생산능력이 고객에게 전량 배정됐다고 밝혔다."

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name) / "job-root"
        self.store = ProFirstJobStore(
            Path(self.temporary_directory.name) / "repair.sqlite3",
            now=lambda: datetime(2026, 8, 22, 3, 4, 5, tzinfo=timezone.utc),
        )
        self.job = self._running_approved_job()
        self.orchestrator = ProMultiPassResearchOrchestrator(self.store)
        self.scope = self.orchestrator.record_completed_initial_pass(
            self.job.job_id,
            primary_archetype_ids=(ARCHETYPE,),
            response_hash="c" * 64,
        )
        self.packet = {
            "job_id": self.job.job_id,
            "run_id": "RUN-REPAIR",
            "conversation_id": self.scope.conversation_id,
            "target": {
                "symbol": self.job.symbol,
                "company_name": self.job.company_name,
            },
            "as_of_date": self.job.as_of_date,
            "candidate_archetypes": [ARCHETYPE],
            "research_mode": "FULL_RESEARCH",
        }

    def _running_approved_job(self):
        candidate = self.store.create_candidate(
            symbol=self.target_id,
            company_name=self.company_name,
            as_of_date=self.as_of_date,
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="verifier-repair-trigger",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        job = self.store.create_job(candidate.candidate_id, archetype_ids=(ARCHETYPE,))
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.PACKET_BUILDING,
            actor="test",
            idempotency_key="packet-building",
        )
        job = self.store.record_packet(
            job.job_id,
            expected_version=job.state_version,
            packet_id="PACKET-REPAIR",
            packet_hash="a" * 64,
            manifest={"packet_hash": "a" * 64},
            actor="test",
            idempotency_key="packet-ready",
        )
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="test",
            idempotency_key="browser-preparing",
        )
        job = self.store.record_browser_prepared(
            job.job_id,
            expected_version=job.state_version,
            browser_session_id="BROWSER-REPAIR",
            conversation_id="CONVERSATION-REPAIR",
            adapter_name="FakeAdapter",
            packet_hash="a" * 64,
            prompt_hash="b" * 64,
            state={"state": "AWAITING_USER_APPROVAL"},
            actor="test",
            idempotency_key="browser-prepared",
        )
        job, nonce = self.store.issue_approval_nonce(
            job.job_id,
            expected_version=job.state_version,
            actor="test",
            idempotency_key="approval-issued",
            prompt_hash="b" * 64,
            expires_at="2026-08-23T03:04:05Z",
        )
        job = self.store.consume_approval_nonce(
            job.job_id,
            nonce,
            expected_version=job.state_version,
            actor="user",
            idempotency_key="approval-consumed",
            prompt_hash="b" * 64,
        )
        job = self.store.claim_submit(
            job.job_id,
            expected_version=job.state_version,
            actor="test",
            idempotency_key="initial-submit",
        )
        return self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.RESEARCH_RUNNING,
            actor="test",
            idempotency_key="initial-running",
        )

    def _document(self, *, company: str | None = None) -> str:
        return " ".join(
            (
                "2026년 8월 1일 공식 HBM 사업 보고서.",
                company or self.company_name,
                "MEMORY 사업과 HBM 제품의 생산 및 고객 배정 현황을 설명한다.",
                self.excerpt if company is None else self.excerpt.replace(self.company_name, company),
                "이 문서는 검색 snippet이 아니라 경영진 설명과 생산 계획, 고객 배정, 사업 위험을 포함한 전체 원문이다.",
                "deterministic verifier fixture가 전체 문서 조건을 충족하도록 충분한 길이의 후속 설명을 포함한다.",
            )
        )

    def _fact(
        self,
        *,
        candidate_id: str = "PROFACT-REPAIR-001",
        question_id: str = QUESTION,
        excerpt: str | None = None,
        source_url: str | None = None,
        source_lineage_id: str = "LINEAGE-REPAIR-001",
    ) -> dict:
        return {
            "dossier_fact_id": candidate_id,
            "research_pass_id": self.scope.initial_pass_id,
            "source_lineage_id": source_lineage_id,
            "question_family_ids": [question_id],
            "repair_of_candidate_id": None,
            "statement": "HBM 생산능력이 고객에게 전량 배정됐다.",
            "direction": "POSITIVE",
            "subject": self.company_name,
            "target_id": self.target_id,
            "issuer_scoped": True,
            "business_segment": "MEMORY",
            "product_family": "HBM",
            "economic_mechanism": "CAPACITY_SCARCITY",
            "predicate": "HBM_CAPACITY_ALLOCATED",
            "value": 100,
            "unit": "%",
            "period": "2026",
            "event_date": "2026-08-01",
            "current_status": "CURRENT",
            "candidate_components": ["bottleneck_pricing"],
            "source_url": source_url or self.url,
            "source_title": "2026 HBM 생산능력 공식 업데이트",
            "source_publisher": self.company_name,
            "published_at": "2026-08-01",
            "supporting_excerpt": excerpt or self.excerpt,
            "confidence": 0.93,
            "scope_business_segment": "MEMORY",
            "scope_product_family": "HBM",
            "scope_technology_family": "HBM",
            "scope_transaction_type": "CAPACITY_INVESTMENT",
            "scope_economic_mechanism": "CAPACITY_SCARCITY",
            "scope_confidence": 1.0,
        }

    def _dossier(self, facts: list[dict]) -> dict:
        questions = []
        lineages = []
        for fact in facts:
            question_id = fact["question_family_ids"][0]
            questions.append(
                {
                    "archetype_id": ARCHETYPE,
                    "question_family_id": question_id,
                    "status": "SUPPORTED_SCORING",
                    "support_fact_ids": [fact["dossier_fact_id"]],
                    "counter_fact_ids": [],
                    "resolution_fact_ids": [],
                    "attempted_source_role_ids": ["ISSUER_OFFICIAL"],
                    "search_route_receipt_ids": [],
                    "required_source_roles_satisfied": ["ISSUER_OFFICIAL"],
                    "required_source_roles_missing": [],
                    "availability_class": "PUBLIC_SEARCHABLE",
                    "affected_component_ids": ["bottleneck_pricing"],
                    "could_change_score": True,
                    "could_change_stage": False,
                    "could_change_hard_break": False,
                    "closure_reason": "Pro candidate는 source verifier 검증 전 상태다.",
                    "adequate_search_proven": False,
                }
            )
            lineages.append(
                {
                    "source_lineage_id": fact["source_lineage_id"],
                    "source_urls": [fact["source_url"]],
                    "fact_ids": [fact["dossier_fact_id"]],
                    "independence_group_id": fact["source_lineage_id"],
                    "status": "ACTIVE",
                }
            )
        return {
            "schema_version": "e2r_pro_research_dossier_v2",
            "job_id": self.job.job_id,
            "run_id": "RUN-REPAIR",
            "conversation_id": self.scope.conversation_id,
            "research_pass_id": self.scope.initial_pass_id,
            "parent_pass_id": None,
            "target": {
                "target_id": self.target_id,
                "symbol": self.target_id,
                "company_name": self.company_name,
                "aliases": ["검증 기업"],
            },
            "as_of_date": self.as_of_date,
            "candidate_archetypes": [ARCHETYPE],
            "selected_archetypes": [ARCHETYPE],
            "research_status": "NEEDS_PUBLIC_GAP_CLOSURE",
            "business_model": {"summary": "HBM repair fixture"},
            "material_facts": facts,
            "counterfacts": [],
            "resolution_facts": [],
            "question_family_results": questions,
            "component_research": {},
            "structured_metrics": {},
            "unresolved_gaps": [],
            "source_lineages": lineages,
            "search_route_receipts": [],
            "research_passes": [
                {
                    "pass_id": self.scope.initial_pass_id,
                    "pass_name": "PRIMARY_OFFICIAL_RESEARCH",
                    "parent_pass_id": None,
                    "status": "COMPLETE",
                    "prompt_hash": "b" * 64,
                    "response_hash": "c" * 64,
                }
            ],
            "research_saturation": {},
            "verification_repair_register": [],
            "proposed_score_ranges": [],
            "score_authority": False,
            "stage_authority": False,
        }

    def _verifier(self, documents: dict[str, str] | None = None) -> ProSourceVerifier:
        return ProSourceVerifier(
            page_fetcher=PageFetcher(
                fixture_text_by_url=documents or {self.url: self._document()},
                live_enabled=False,
                max_text_chars=None,
            )
        )

    def _verify_and_plan(
        self,
        dossier: dict,
        verifier: ProSourceVerifier,
        *,
        maximum_prompt_payload_chars: int = 210_000,
    ):
        verification = verifier.verify(
            dossier=dossier,
            job=self.job,
            job_root=self.root,
        )
        rows = tuple(row.to_dict() for row in verification.verifications)
        service = ProVerifierRepairService(self.orchestrator, verifier=verifier)
        plan = service.plan_repair(
            job_id=self.job.job_id,
            job_root=self.root,
            packet=self.packet,
            dossier=dossier,
            verification_rows=rows,
            primary_archetype_ids=(ARCHETYPE,),
            maximum_prompt_payload_chars=maximum_prompt_payload_chars,
        )
        return verification, rows, service, plan

    def _complete_repair_pass(self, plan) -> str:
        self.assertIsInstance(plan.followup, FollowupPassPlan)
        pass_id = plan.followup.research_pass.pass_id
        self.orchestrator.ledger.mark_prepared(pass_id)
        self.orchestrator.ledger.claim_submit(pass_id)
        self.orchestrator.ledger.mark_running(pass_id)
        response_hash = "d" * 64
        self.orchestrator.ledger.complete_pass(
            pass_id,
            response_hash=response_hash,
        )
        return response_hash

    def _delta(self, plan, response_hash: str, actions: list[dict]) -> dict:
        return {
            "schema_version": "e2r_pro_verifier_repair_delta_v1",
            "job_id": self.job.job_id,
            "conversation_id": self.scope.conversation_id,
            "research_pass_id": plan.followup.research_pass.pass_id,
            "parent_pass_id": plan.followup.research_pass.parent_pass_id,
            "response_hash": response_hash,
            "actions": actions,
            "score_authority": False,
            "stage_authority": False,
        }

    def _corrected_fact(
        self,
        original: dict,
        plan,
        *,
        candidate_id: str = "PROFACT-REPAIRED-001",
        supporting_excerpt: str | None = None,
        source_url: str | None = None,
        source_lineage_id: str | None = None,
    ) -> dict:
        corrected = deepcopy(original)
        corrected.update(
            {
                "dossier_fact_id": candidate_id,
                "repair_of_candidate_id": original["dossier_fact_id"],
                "research_pass_id": plan.followup.research_pass.pass_id,
                "supporting_excerpt": supporting_excerpt or self.excerpt,
            }
        )
        if source_url is not None:
            corrected["source_url"] = source_url
        if source_lineage_id is not None:
            corrected["source_lineage_id"] = source_lineage_id
        return corrected

    def test_quote_mismatch_opens_repair(self) -> None:
        fact = self._fact(excerpt="원문에 없는 과장된 HBM 계약 문장")
        dossier = self._dossier([fact])
        verification, _rows, _service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        self.assertEqual(
            verification.verifications[0].status,
            "REJECTED_QUOTE_MISMATCH",
        )
        self.assertEqual(len(plan.rejection_packets), 1)
        packet = plan.rejection_packets[0]
        self.assertEqual(packet.rejection_category, "QUOTE_MISMATCH")
        self.assertIn(self.excerpt, packet.fetched_source_excerpt)
        self.assertIsInstance(plan.followup, FollowupPassPlan)
        self.assertEqual(plan.followup.research_pass.pass_name, "VERIFIER_REPAIR")
        self.assertEqual(
            plan.followup.research_pass.conversation_id,
            self.scope.conversation_id,
        )
        self.assertIn("QUOTE_MISMATCH", plan.followup.prompt_text)

    def test_repair_delta_requires_completed_same_conversation_pass(self) -> None:
        fact = self._fact(excerpt="원문에 없는 과장된 HBM 계약 문장")
        dossier = self._dossier([fact])
        _verification, rows, service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        packet = plan.rejection_packets[0]
        with self.assertRaisesRegex(ValueError, "completed same-conversation pass"):
            service.apply_and_reverify(
                job=self.job,
                job_root=self.root,
                dossier=dossier,
                plan=plan,
                repair_delta=self._delta(
                    plan,
                    "d" * 64,
                    [
                        {
                            "packet_id": packet.packet_id,
                            "candidate_id": fact["dossier_fact_id"],
                            "question_family_ids": [QUESTION],
                            "action": "WITHDRAWN",
                            "corrected_fact": None,
                        }
                    ],
                ),
                prior_verification_rows=rows,
            )

    def test_wrong_subject_opens_repair(self) -> None:
        competitor = "비교기업"
        competitor_excerpt = self.excerpt.replace(self.company_name, competitor)
        fact = self._fact(excerpt=competitor_excerpt)
        dossier = self._dossier([fact])
        verifier = self._verifier({self.url: self._document(company=competitor)})
        verification, _rows, _service, plan = self._verify_and_plan(
            dossier, verifier
        )
        self.assertEqual(
            verification.verifications[0].status,
            "REJECTED_WRONG_SUBJECT",
        )
        self.assertEqual(
            plan.rejection_packets[0].rejection_category,
            "WRONG_SUBJECT",
        )
        self.assertEqual(plan.receipt["question_family_ids"], [QUESTION])

    def test_rejected_auxiliary_fact_without_question_binding_is_diagnostic_only(self) -> None:
        linked = self._fact()
        dossier = self._dossier([linked])
        orphan_url = "https://issuer.example/auxiliary"
        orphan = self._fact(
            candidate_id="PROFACT-AUXILIARY",
            excerpt="원문에 존재하지 않는 보조 문장",
            source_url=orphan_url,
            source_lineage_id="LINEAGE-AUXILIARY",
        )
        orphan["question_family_ids"] = []
        dossier["material_facts"].append(orphan)
        dossier["source_lineages"].append(
            {
                "source_lineage_id": "LINEAGE-AUXILIARY",
                "source_urls": [orphan_url],
                "fact_ids": [orphan["dossier_fact_id"]],
                "independence_group_id": "LINEAGE-AUXILIARY",
                "status": "ACTIVE",
            }
        )
        verifier = self._verifier(
            {
                self.url: self._document(),
                orphan_url: self._document(),
            }
        )
        verification = verifier.verify(
            dossier=dossier,
            job=self.job,
            job_root=self.root,
        )
        rows = tuple(row.to_dict() for row in verification.verifications)
        self.assertEqual(rows[1]["status"], "REJECTED_QUOTE_MISMATCH")
        packets = compile_rejection_packets(
            dossier=dossier,
            verification_rows=rows,
            job_root=self.root,
            conversation_id=self.scope.conversation_id,
        )
        self.assertEqual(packets, ())

    def test_duplicate_lineage_compiler_rejection_opens_repair(self) -> None:
        fact = self._fact()
        dossier = self._dossier([fact])
        verifier = self._verifier()
        verification = verifier.verify(
            dossier=dossier,
            job=self.job,
            job_root=self.root,
        )
        rows = tuple(row.to_dict() for row in verification.verifications)
        claim_id = str(rows[0]["compiled_claim_id"])
        service = ProVerifierRepairService(self.orchestrator, verifier=verifier)
        plan = service.plan_repair(
            job_id=self.job.job_id,
            job_root=self.root,
            packet=self.packet,
            dossier=dossier,
            verification_rows=rows,
            fact_compilation_rejection_rows=(
                {
                    "claim_id": claim_id,
                    "reason": "CYCLIC_FACT_LINEAGE",
                    "accepted_claim": True,
                    "material_claim": True,
                },
            ),
            primary_archetype_ids=(ARCHETYPE,),
        )
        self.assertEqual(len(plan.rejection_packets), 1)
        self.assertEqual(
            plan.rejection_packets[0].rejection_category,
            "DUPLICATE_LINEAGE",
        )
        self.assertIn("CYCLIC_FACT_LINEAGE", plan.followup.prompt_text)

    def test_repair_can_withdraw_fact(self) -> None:
        fact = self._fact(excerpt="원문에 없는 과장된 HBM 계약 문장")
        dossier = self._dossier([fact])
        _verification, rows, service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        response_hash = self._complete_repair_pass(plan)
        packet = plan.rejection_packets[0]
        delta = self._delta(
            plan,
            response_hash,
            [
                {
                    "packet_id": packet.packet_id,
                    "candidate_id": fact["dossier_fact_id"],
                    "question_family_ids": [QUESTION],
                    "action": "WITHDRAWN",
                    "corrected_fact": None,
                }
            ],
        )
        run = service.apply_and_reverify(
            job=self.job,
            job_root=self.root,
            dossier=dossier,
            plan=plan,
            repair_delta=delta,
            prior_verification_rows=rows,
        )
        self.assertEqual(run.receipt.material_rejection_unresolved_count, 0)
        self.assertEqual(run.receipt.resolutions[0].status, "WITHDRAWN")
        self.assertFalse(run.effective_dossier["material_facts"])
        self.assertEqual(
            run.effective_dossier["question_family_results"][0]["status"],
            "PUBLIC_SEARCHABLE",
        )

    def test_partial_repair_keeps_unhandled_packet_pending(self) -> None:
        first = self._fact(excerpt="원문에 없는 첫 번째 문장")
        second = self._fact(
            candidate_id="PROFACT-REPAIR-002",
            question_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q02",
            excerpt="원문에 없는 두 번째 문장",
            source_lineage_id="LINEAGE-REPAIR-002",
        )
        dossier = self._dossier([first, second])
        _verification, rows, service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        response_hash = self._complete_repair_pass(plan)
        first_packet = next(
            row
            for row in plan.rejection_packets
            if row.candidate_id == first["dossier_fact_id"]
        )
        run = service.apply_and_reverify(
            job=self.job,
            job_root=self.root,
            dossier=dossier,
            plan=plan,
            repair_delta=self._delta(
                plan,
                response_hash,
                [
                    {
                        "packet_id": first_packet.packet_id,
                        "candidate_id": first["dossier_fact_id"],
                        "question_family_ids": [QUESTION],
                        "action": "WITHDRAWN",
                        "corrected_fact": None,
                    }
                ],
            ),
            prior_verification_rows=rows,
        )
        self.assertEqual(run.receipt.material_rejection_unresolved_count, 1)
        self.assertEqual(
            run.effective_dossier["research_status"],
            "NEEDS_VERIFIER_REPAIR",
        )
        second_question = next(
            row
            for row in run.effective_dossier["question_family_results"]
            if row["question_family_id"]
            == "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q02"
        )
        self.assertEqual(second_question["status"], "VERIFIER_REPAIR_REQUIRED")

    def test_large_repair_set_is_batched_without_dropping_deferred_packets(self) -> None:
        first = self._fact(excerpt="원문에 없는 첫 번째 문장")
        second = self._fact(
            candidate_id="PROFACT-REPAIR-002",
            question_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q02",
            excerpt="원문에 없는 두 번째 문장",
            source_lineage_id="LINEAGE-REPAIR-002",
        )
        dossier = self._dossier([first, second])
        _verification, _rows, _service, plan = self._verify_and_plan(
            dossier,
            self._verifier(),
            maximum_prompt_payload_chars=1,
        )
        self.assertEqual(len(plan.rejection_packets), 1)
        self.assertEqual(plan.receipt["pending_rejection_packet_count"], 2)
        self.assertEqual(plan.receipt["deferred_rejection_packet_count"], 1)
        self.assertTrue(plan.receipt["transport_batching_only"])
        selected_lines = (
            self.root / "repair/rejection_packets.jsonl"
        ).read_text(encoding="utf-8").splitlines()
        pending_lines = (
            self.root / "repair/pending_rejection_packets.jsonl"
        ).read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(selected_lines), 1)
        self.assertEqual(len(pending_lines), 2)

    def test_repair_cannot_invent_url_or_quote(self) -> None:
        fact = self._fact(excerpt="원문에 없는 과장된 HBM 계약 문장")
        dossier = self._dossier([fact])
        _verification, rows, service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        response_hash = self._complete_repair_pass(plan)
        packet = plan.rejection_packets[0]
        invented_url = "https://invented.example/nonexistent-source"
        corrected = self._corrected_fact(
            fact,
            plan,
            supporting_excerpt="발행되지 않은 가짜 인용문",
            source_url=invented_url,
            source_lineage_id="LINEAGE-INVENTED",
        )
        delta = self._delta(
            plan,
            response_hash,
            [
                {
                    "packet_id": packet.packet_id,
                    "candidate_id": fact["dossier_fact_id"],
                    "question_family_ids": [QUESTION],
                    "action": "REPLACED",
                    "corrected_fact": corrected,
                    "new_source_lineage": {
                        "source_lineage_id": "LINEAGE-INVENTED",
                        "source_urls": [invented_url],
                        "fact_ids": [corrected["dossier_fact_id"]],
                        "independence_group_id": "INVENTED",
                        "status": "ACTIVE",
                    },
                }
            ],
        )
        run = service.apply_and_reverify(
            job=self.job,
            job_root=self.root,
            dossier=dossier,
            plan=plan,
            repair_delta=delta,
            prior_verification_rows=rows,
        )
        resolution = run.receipt.resolutions[0]
        self.assertEqual(resolution.status, "REVERIFIED_REJECTED")
        self.assertEqual(resolution.verifier_status, "REJECTED_SOURCE_UNAVAILABLE")
        self.assertEqual(run.receipt.material_rejection_unresolved_count, 1)
        self.assertFalse(run.receipt.score_valid)

    def test_repair_cannot_invent_quote_on_real_url(self) -> None:
        fact = self._fact(excerpt="원문에 없는 최초 문장")
        dossier = self._dossier([fact])
        _verification, rows, service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        response_hash = self._complete_repair_pass(plan)
        packet = plan.rejection_packets[0]
        corrected = self._corrected_fact(
            fact,
            plan,
            supporting_excerpt="여전히 원문에 없는 새로운 가짜 인용문",
        )
        run = service.apply_and_reverify(
            job=self.job,
            job_root=self.root,
            dossier=dossier,
            plan=plan,
            repair_delta=self._delta(
                plan,
                response_hash,
                [
                    {
                        "packet_id": packet.packet_id,
                        "candidate_id": fact["dossier_fact_id"],
                        "question_family_ids": [QUESTION],
                        "action": "CORRECTED",
                        "corrected_fact": corrected,
                    }
                ],
            ),
            prior_verification_rows=rows,
        )
        self.assertEqual(
            run.receipt.resolutions[0].verifier_status,
            "REJECTED_QUOTE_MISMATCH",
        )
        self.assertEqual(run.receipt.material_rejection_unresolved_count, 1)

    def test_unrepaired_material_fact_blocks_full_thesis(self) -> None:
        dossier, verified = _complete_dossier()
        receipt = ResearchSaturationAdjudicator().adjudicate(
            dossier=dossier,
            verified_fact_ids=verified,
            verifier_repair_pending_ids=("PROREPAIRPACKET-PENDING",),
        )
        self.assertFalse(receipt.research_saturation_valid)
        self.assertFalse(receipt.component_entry_allowed)
        self.assertEqual(receipt.deterministic_research_status, "NEEDS_VERIFIER_REPAIR")

    def test_repaired_fact_is_reverified(self) -> None:
        fact = self._fact(excerpt="원문에 없는 과장된 HBM 계약 문장")
        dossier = self._dossier([fact])
        _verification, rows, service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        response_hash = self._complete_repair_pass(plan)
        packet = plan.rejection_packets[0]
        corrected = self._corrected_fact(fact, plan)
        run = service.apply_and_reverify(
            job=self.job,
            job_root=self.root,
            dossier=dossier,
            plan=plan,
            repair_delta=self._delta(
                plan,
                response_hash,
                [
                    {
                        "packet_id": packet.packet_id,
                        "candidate_id": fact["dossier_fact_id"],
                        "question_family_ids": [QUESTION],
                        "action": "NARROWED",
                        "corrected_fact": corrected,
                    }
                ],
            ),
            prior_verification_rows=rows,
        )
        resolution = run.receipt.resolutions[0]
        self.assertEqual(resolution.status, "REVERIFIED_ACCEPTED")
        self.assertEqual(resolution.verifier_status, "ACCEPTED_CURRENT")
        self.assertEqual(run.receipt.material_rejection_unresolved_count, 0)
        self.assertEqual(run.receipt.to_dict()["status"], "VERIFIER_REPAIR_COMPLETE")
        self.assertTrue(
            (run.repair_root / "verifier_repair_receipt.json").is_file()
        )

    def test_repair_can_replace_with_verified_source_url(self) -> None:
        unavailable_url = "https://unavailable.example/original"
        corrected_url = "https://issuer.example/corrected-source"
        fact = self._fact(source_url=unavailable_url)
        dossier = self._dossier([fact])
        verifier = self._verifier({corrected_url: self._document()})
        verification, rows, service, plan = self._verify_and_plan(
            dossier, verifier
        )
        self.assertEqual(
            verification.verifications[0].status,
            "REJECTED_SOURCE_UNAVAILABLE",
        )
        response_hash = self._complete_repair_pass(plan)
        packet = plan.rejection_packets[0]
        corrected = self._corrected_fact(
            fact,
            plan,
            source_url=corrected_url,
            source_lineage_id="LINEAGE-CORRECTED-SOURCE",
        )
        run = service.apply_and_reverify(
            job=self.job,
            job_root=self.root,
            dossier=dossier,
            plan=plan,
            repair_delta=self._delta(
                plan,
                response_hash,
                [
                    {
                        "packet_id": packet.packet_id,
                        "candidate_id": fact["dossier_fact_id"],
                        "question_family_ids": [QUESTION],
                        "action": "REPLACED",
                        "corrected_fact": corrected,
                        "new_source_lineage": {
                            "source_lineage_id": "LINEAGE-CORRECTED-SOURCE",
                            "source_urls": [corrected_url],
                            "fact_ids": [corrected["dossier_fact_id"]],
                            "independence_group_id": "ISSUER-CORRECTED",
                            "status": "ACTIVE",
                        },
                    }
                ],
            ),
            prior_verification_rows=rows,
        )
        self.assertEqual(
            run.receipt.resolutions[0].status,
            "REVERIFIED_ACCEPTED",
        )
        self.assertEqual(run.receipt.material_rejection_unresolved_count, 0)

    def test_captured_full_dossier_response_derives_repair_delta(self) -> None:
        fact = self._fact(excerpt="원문에 없는 과장된 HBM 계약 문장")
        dossier = self._dossier([fact])
        _verification, rows, service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        response_hash = self._complete_repair_pass(plan)
        packet = plan.rejection_packets[0]
        corrected = self._corrected_fact(fact, plan)
        response_dossier = deepcopy(dossier)
        response_dossier["research_pass_id"] = plan.followup.research_pass.pass_id
        response_dossier["parent_pass_id"] = (
            plan.followup.research_pass.parent_pass_id
        )
        response_dossier["research_status"] = "NEEDS_VERIFIER_REPAIR"
        response_dossier["material_facts"].append(corrected)
        response_dossier["source_lineages"][0]["fact_ids"].append(
            corrected["dossier_fact_id"]
        )
        response_dossier["question_family_results"][0].update(
            {
                "status": "VERIFIER_REPAIR_REQUIRED",
                "support_fact_ids": [corrected["dossier_fact_id"]],
                "search_route_receipt_ids": ["ROUTE-REPAIR-CAPTURED-001"],
                "closure_reason": "수정 candidate의 deterministic 재검증이 남았다.",
            }
        )
        response_dossier["search_route_receipts"].append(
            {
                "route_receipt_id": "ROUTE-REPAIR-CAPTURED-001",
                "pass_id": plan.followup.research_pass.pass_id,
                "archetype_id": ARCHETYPE,
                "question_family_id": QUESTION,
                "gap_id": "GAP-REPAIR-CAPTURED-001",
                "source_role_id": "ISSUER_OFFICIAL",
                "query_or_navigation_objective": "수정 원문 exact quote 재확인",
                "query_text": "검증기업 HBM 공식 보고서 exact quote",
                "result_count_seen": 1,
                "opened_source_urls": [corrected["source_url"]],
                "accepted_fact_ids": [corrected["dossier_fact_id"]],
                "rejected_candidate_ids": [],
                "provider_status": "SUCCESS",
                "no_new_route_reason": None,
                "performed_at": "2026-08-22T04:00:00Z",
            }
        )
        response_dossier["research_passes"].append(
            {
                "pass_id": plan.followup.research_pass.pass_id,
                "parent_pass_id": plan.followup.research_pass.parent_pass_id,
                "pass_name": "VERIFIER_REPAIR",
                "status": "COMPLETE",
                "prompt_hash": plan.followup.prompt_hash,
                "response_hash": response_hash,
            }
        )
        response_dossier["verification_repair_register"] = [
            {
                "candidate_id": fact["dossier_fact_id"],
                "question_family_id": QUESTION,
                "rejection_category": packet.rejection_category,
                "status": "NARROWED",
                "replacement_candidate_id": corrected["dossier_fact_id"],
            }
        ]
        run = service.apply_response_dossier_and_reverify(
            job=self.job,
            job_root=self.root,
            original_dossier=dossier,
            response_dossier=response_dossier,
            response_hash=response_hash,
            plan=plan,
            prior_verification_rows=rows,
        )
        self.assertEqual(
            run.receipt.resolutions[0].status,
            "REVERIFIED_ACCEPTED",
        )
        self.assertEqual(run.application.actions[0].action, "NARROWED")
        self.assertIn(
            "ROUTE-REPAIR-CAPTURED-001",
            run.effective_dossier["question_family_results"][0][
                "search_route_receipt_ids"
            ],
        )

    def test_candidate_level_repair_restores_packet_scope_only_for_reverification(
        self,
    ) -> None:
        second_question = "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q02"
        fact = self._fact(excerpt="원문에 없는 과장된 HBM 계약 문장")
        fact["question_family_ids"] = [QUESTION, second_question]
        dossier = self._dossier([fact])
        second_result = deepcopy(dossier["question_family_results"][0])
        second_result["question_family_id"] = second_question
        dossier["question_family_results"].append(second_result)
        _verification, _rows, _service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        response_hash = self._complete_repair_pass(plan)
        packet = plan.rejection_packets[0]
        self.assertEqual(set(packet.question_family_ids), {QUESTION, second_question})
        corrected = self._corrected_fact(fact, plan)
        # The Pro register and replacement fact may each name a different
        # representative question, but neither may escape the packet roster.
        corrected["question_family_ids"] = [second_question]
        response = deepcopy(dossier)
        response.update(
            {
                "research_pass_id": plan.followup.research_pass.pass_id,
                "parent_pass_id": plan.followup.research_pass.parent_pass_id,
            }
        )
        response["material_facts"].append(corrected)
        response["search_route_receipts"].append(
            {
                "route_receipt_id": "ROUTE-MULTI-QUESTION-REPAIR",
                "pass_id": plan.followup.research_pass.pass_id,
                "question_family_id": QUESTION,
                "accepted_fact_ids": [corrected["dossier_fact_id"]],
            }
        )
        response["verification_repair_register"] = [
            {
                "candidate_id": fact["dossier_fact_id"],
                "question_family_id": QUESTION,
                "rejection_category": packet.rejection_category,
                "status": "NARROWED",
                "replacement_candidate_id": corrected["dossier_fact_id"],
            }
        ]

        delta = derive_repair_delta_from_dossier_response(
            original_dossier=dossier,
            response_dossier=response,
            rejection_packets=plan.rejection_packets,
            response_hash=response_hash,
        )

        action = delta["actions"][0]
        self.assertEqual(
            set(action["question_family_ids"]),
            {QUESTION, second_question},
        )
        self.assertEqual(action["pro_declared_question_family_ids"], [QUESTION])
        self.assertEqual(
            action["question_scope_binding"],
            "PACKET_SCOPE_RESTORED_FOR_DETERMINISTIC_REVERIFICATION",
        )
        self.assertEqual(
            set(action["corrected_fact"]["question_family_ids"]),
            {QUESTION, second_question},
        )
        self.assertEqual(corrected["question_family_ids"], [second_question])

        escaped = deepcopy(response)
        escaped["verification_repair_register"][0]["question_family_id"] = (
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q03"
        )
        with self.assertRaisesRegex(ValueError, "escapes the rejection packet"):
            derive_repair_delta_from_dossier_response(
                original_dossier=dossier,
                response_dossier=escaped,
                rejection_packets=plan.rejection_packets,
                response_hash=response_hash,
            )

    def test_existing_accepted_fact_cannot_be_targeted_or_deleted(self) -> None:
        accepted = self._fact(candidate_id="PROFACT-ACCEPTED")
        rejected = self._fact(
            candidate_id="PROFACT-REJECTED",
            question_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q02",
            excerpt="원문에 없는 문장",
            source_lineage_id="LINEAGE-REJECTED",
        )
        dossier = self._dossier([accepted, rejected])
        _verification, _rows, _service, plan = self._verify_and_plan(
            dossier, self._verifier()
        )
        response_hash = self._complete_repair_pass(plan)
        packet = plan.rejection_packets[0]
        with self.assertRaisesRegex(ValueError, "escapes its rejection packet"):
            _service.apply_and_reverify(
                job=self.job,
                job_root=self.root,
                dossier=dossier,
                plan=plan,
                repair_delta=self._delta(
                    plan,
                    response_hash,
                    [
                        {
                            "packet_id": packet.packet_id,
                            "candidate_id": accepted["dossier_fact_id"],
                            "question_family_ids": [QUESTION],
                            "action": "WITHDRAWN",
                            "corrected_fact": None,
                        }
                    ],
                ),
                prior_verification_rows=_rows,
            )

    def test_tracked_verifier_repair_audit_matches_contract(self) -> None:
        path = (
            Path(__file__).resolve().parents[1]
            / "docs/operational/e2r_pro_first_v2/verifier_repair_audit.json"
        )
        self.assertEqual(
            json.loads(path.read_text(encoding="utf-8")),
            compile_verifier_repair_contract_audit(),
        )


if __name__ == "__main__":
    unittest.main()
