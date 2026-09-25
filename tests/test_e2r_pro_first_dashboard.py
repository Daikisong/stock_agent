from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from fastapi.testclient import TestClient

from e2r.pro_first.approval import ProApprovalService
from e2r.pro_first.dashboard import (
    DashboardActions,
    LocalDashboardConfig,
    create_pro_first_dashboard_app,
)
from e2r.pro_first.ids import canonical_hash, canonical_json, stable_id
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.publication import ProResultPublisher
from e2r.pro_first.scoring.publication_gate import FullThesisEligibilityReceipt
from e2r.pro_first.reuse import ProSameInputReuseGate
from e2r.pro_first.state_machine import TransitionContext
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER


class ProFirstDashboardTest(unittest.TestCase):
    archetype_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name) / "runtime"
        self.now = lambda: datetime(2026, 8, 22, 3, 4, 5, tzinfo=timezone.utc)
        self.store = ProFirstJobStore(
            Path(self.temporary_directory.name) / "dashboard.sqlite3",
            now=self.now,
        )
        self.candidate = self.store.create_candidate(
            symbol="005930",
            company_name="검증기업",
            as_of_date="2026-08-22",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="dashboard-trigger",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={
                "production_candidate": True,
                "trigger_ids": ["TRIGGER-1"],
                "reason_codes": ["DEEP_RESEARCH_REQUIRED"],
            },
        )
        self.job = self.store.create_job(
            self.candidate.candidate_id,
            archetype_ids=(self.archetype_id,),
        )
        self.token = "dashboard-unit-token-0123456789"
        self.config = LocalDashboardConfig(
            runtime_root=self.root,
            port=8765,
            allowed_origins=("http://testserver",),
            local_token=self.token,
        )
        self.app = create_pro_first_dashboard_app(
            store=self.store,
            config=self.config,
            approval_service=ProApprovalService(self.store, now=self.now),
        )
        self.client = TestClient(self.app)
        self.headers = {
            "Origin": "http://testserver",
            "X-E2R-Local-Token": self.token,
        }

    def _transition(
        self,
        target: JobStatus,
        *,
        context: TransitionContext | None = None,
        updates=None,
    ) -> None:
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=self.job.state_version,
            to_status=target,
            actor="dashboard-unit-fixture",
            idempotency_key=(
                f"dashboard-unit-{self.job.state_version}-{target.value}"
            ),
            context=context,
            updates=updates,
        )

    def _prepare_approval_job(self) -> str:
        self._transition(JobStatus.PACKET_BUILDING)
        packet_hash = canonical_hash({"packet": "dashboard-unit"})
        packet_id = "PROPACKET-dashboard-unit"
        self.job = self.store.record_packet(
            self.job.job_id,
            expected_version=self.job.state_version,
            packet_id=packet_id,
            packet_hash=packet_hash,
            manifest={
                "packet_id": packet_id,
                "packet_hash": packet_hash,
                "job_id": self.job.job_id,
            },
            actor="dashboard-unit-fixture",
            idempotency_key="dashboard-unit-packet",
        )
        self._transition(JobStatus.BROWSER_PREPARING)
        prompt_hash = canonical_hash({"prompt": "dashboard-unit"})
        self.job = self.store.record_browser_prepared(
            self.job.job_id,
            expected_version=self.job.state_version,
            browser_session_id="PROBROWSER-dashboard-unit",
            conversation_id="CONVERSATION-dashboard-unit",
            adapter_name="UNIT_BROWSER",
            packet_hash=packet_hash,
            prompt_hash=prompt_hash,
            state={"ui_state": "PROMPT_READY"},
            actor="dashboard-unit-fixture",
            idempotency_key="dashboard-unit-browser-prepared",
        )
        return prompt_hash

    def _finalize_job(self) -> Path:
        for target in (
            JobStatus.PACKET_BUILDING,
            JobStatus.PACKET_READY,
            JobStatus.BROWSER_PREPARING,
            JobStatus.USER_ATTENTION_REQUIRED,
            JobStatus.IMPORTING,
        ):
            self._transition(target)
        component_ids = list(CANONICAL_COMPONENT_ORDER)
        dossier_hash = canonical_hash({"job_id": self.job.job_id, "fixture": True})
        dossier_id = "PRODOSSIER-dashboard-unit"
        self.job = self.store.record_dossier_import(
            self.job.job_id,
            expected_version=self.job.state_version,
            dossier_id=dossier_id,
            dossier_hash=dossier_hash,
            import_receipt={
                "schema_version": "e2r_pro_dossier_import_receipt_v1",
                "job_id": self.job.job_id,
                "normalized_dossier_hash": dossier_hash,
                "validation_status": "PASS",
                "score_authority": False,
                "stage_authority": False,
                "evidence_promoted_count": 0,
                "component_ids": component_ids,
            },
            actor="dashboard-unit-fixture",
            idempotency_key="dashboard-unit-dossier",
        )
        self._transition(JobStatus.VERIFYING_SOURCES)
        verification_hash = canonical_hash({"verification": "dashboard-unit"})
        self.job = self.store.record_source_verification(
            self.job.job_id,
            expected_version=self.job.state_version,
            verification_id="PROVERIFY-dashboard-unit",
            dossier_id=dossier_id,
            verification_hash=verification_hash,
            receipt={
                "schema_version": "e2r_pro_source_verification_receipt_v1",
                "status": "SOURCE_VERIFICATION_COMPLETE",
                "job_id": self.job.job_id,
                "dossier_id": dossier_id,
                "verification_hash": verification_hash,
                "candidate_fact_count": 2,
                "terminal_fact_count": 2,
                "accepted_fact_candidate_count": 1,
                "compiled_evidence_fact_count": 1,
                "source_document_count": 1,
                "query_count": 0,
                "search_count": 0,
                "pro_score_authority": False,
                "pro_stage_authority": False,
            },
            actor="dashboard-unit-fixture",
            idempotency_key="dashboard-unit-verification",
        )
        self._transition(JobStatus.COMPONENT_RESEARCH)
        self._transition(
            JobStatus.JUDGING,
            context=TransitionContext(
                component_coverage_complete=True,
                research_saturation_valid=True,
            ),
        )
        self._transition(
            JobStatus.SCORING,
            context=TransitionContext(judge_coverage_complete=True),
        )
        assessments = [
            {
                "assessment_id": f"ASSESS-{component_id}",
                "component_id": component_id,
            }
            for component_id in component_ids
        ]
        vector = {component_id: 0.0 for component_id in component_ids}
        eligibility = FullThesisEligibilityReceipt(
            job_id=self.job.job_id,
            selected_archetype_id=self.archetype_id,
            research_eligibility_hash=canonical_hash({"research": "complete"}),
            saturation_receipt_hash=canonical_hash({"saturation": "complete"}),
            verified_fact_roster_hash=canonical_hash([]),
            claim_lineage_roster_hash=canonical_hash([]),
            component_memo_hash=canonical_hash(component_ids),
            judge_decision_hash=canonical_hash({"judge_count": 21}),
            component_count=7,
            component_terminal_count=7,
            judge_count=21,
            claim_lineage_count=0,
            impact_count=0,
        ).to_dict()
        score_base = {
            "schema_version": "e2r_pro_calibrated_score_bridge_receipt_v1",
            "status": "DETERMINISTIC_SCORE_COMPLETE",
            "job_id": self.job.job_id,
            "selected_archetype_id": self.archetype_id,
            "score": {
                "component_score_vector": vector,
                "verified_supported_score": 0.0,
                "provisional_score_lower": 0.0,
                "provisional_score_upper": 0.0,
                "full_e2r_score": 0.0,
                "full_score_valid": True,
                "score_type": "FULL_E2R_SCORE",
            },
            "component_assessments": assessments,
            "validated_impacts": [],
            "pending_reasons": [],
            "impact_fact_lineage": {},
            "score_valid": True,
            "scorer_class": "ResearchCalibratedComponentScorer",
            "ignored_proposed_score_ranges_hash": canonical_hash({}),
            "ignored_proposed_stage": "5",
            "pro_score_ignored": True,
            "pro_stage_ignored": True,
            "new_score_engine_count": 0,
            "production_score_authority": True,
            "production_stage_authority": False,
            "judge_decision_count": 21,
            "accepted_claim_count": 0,
            "full_thesis_eligibility_hash": eligibility["eligibility_hash"],
            "full_thesis_eligibility": eligibility,
        }
        score_hash = canonical_hash(score_base)
        score_receipt_id = stable_id(
            "PROSCORE",
            {"job_id": self.job.job_id, "score_hash": score_hash},
        )
        score_receipt = {
            **score_base,
            "score_receipt_id": score_receipt_id,
            "score_hash": score_hash,
        }
        self.job = self.store.record_score_result(
            self.job.job_id,
            expected_version=self.job.state_version,
            score_receipt_id=score_receipt_id,
            score_hash=score_hash,
            receipt=score_receipt,
            actor="dashboard-unit-fixture",
            idempotency_key="dashboard-unit-score",
        )
        decision = {
            "component_assessment_ids": [
                row["assessment_id"] for row in assessments
            ],
            "claim_impact_ids": [],
            "full_e2r_score": 0.0,
            "full_score_valid": True,
            "canonical_stage": "1",
            "decision_status": "FINAL",
            "stage_signal": "FULL_THESIS_STAGE_1",
            "risk_overlay": {
                "hard_break_claim_ids": [],
                "current_direct_open_counter_claim_ids": [],
                "risk_state": "NO_HARD_BREAK",
            },
        }
        stage_base = {
            "schema_version": "e2r_pro_atomic_stagecourt_bridge_receipt_v1",
            "status": "ATOMIC_STAGECOURT_COMPLETE",
            "job_id": self.job.job_id,
            "score_receipt_id": score_receipt_id,
            "decision": decision,
            "stagecourt_class": "AtomicStageCourtV2",
            "ignored_proposed_stage": "5",
            "pro_stage_ignored": True,
            "new_stage_engine_count": 0,
            "production_score_authority": False,
            "production_stage_authority": True,
            "full_thesis_eligibility_hash": eligibility["eligibility_hash"],
        }
        stage_hash = canonical_hash(stage_base)
        stage_id = stable_id(
            "PROSTAGECOURT",
            {"job_id": self.job.job_id, "stagecourt_hash": stage_hash},
        )
        stage_receipt = {
            **stage_base,
            "stagecourt_receipt_id": stage_id,
            "stagecourt_hash": stage_hash,
        }
        self.job = self.store.record_stagecourt_result(
            self.job.job_id,
            expected_version=self.job.state_version,
            stagecourt_receipt_id=stage_id,
            stagecourt_hash=stage_hash,
            receipt=stage_receipt,
            actor="dashboard-unit-fixture",
            idempotency_key="dashboard-unit-stage",
        )
        job_root = self.root / "jobs" / self.job.job_id
        scoring_root = job_root / "scoring"
        verification_root = job_root / "verification"
        scoring_root.mkdir(parents=True, exist_ok=True)
        verification_root.mkdir(parents=True, exist_ok=True)
        (scoring_root / "full_thesis_eligibility_receipt.json").write_text(
            canonical_json(eligibility) + "\n",
            encoding="utf-8",
        )
        (scoring_root / "component_memos.jsonl").write_text(
            "".join(
                canonical_json({"component_id": component_id}) + "\n"
                for component_id in component_ids
            ),
            encoding="utf-8",
        )
        (scoring_root / "judge_decisions.jsonl").write_text(
            "".join(
                canonical_json(
                    {
                        "judge_id": f"JUDGE-{component_id}-{role}",
                        "component_id": component_id,
                        "role": role,
                    }
                )
                + "\n"
                for component_id in component_ids
                for role in ("ANALYST", "SKEPTIC", "CALIBRATION_JUDGE")
            ),
            encoding="utf-8",
        )
        (verification_root / "source_verifications.jsonl").write_text(
            canonical_json(
                {
                    "status": "ACCEPTED_CURRENT",
                    "source_id": "PROSOURCE-dashboard-unit",
                }
            )
            + "\n",
            encoding="utf-8",
        )
        return job_root

    def test_health(self) -> None:
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
        self.assertTrue(response.json()["loopback_only"])
        with self.assertRaisesRegex(ValueError, "loopback"):
            LocalDashboardConfig(runtime_root=self.root, host="0.0.0.0")

    def test_job_list(self) -> None:
        response = self.client.get("/api/jobs")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 1)
        self.assertEqual(response.json()["jobs"][0]["job_id"], self.job.job_id)
        self.assertNotIn("approval_nonce_hash", response.json()["jobs"][0])

    def test_job_detail(self) -> None:
        response = self.client.get(f"/api/jobs/{self.job.job_id}")
        self.assertEqual(response.status_code, 200)
        detail = response.json()
        self.assertEqual(detail["job"]["symbol"], "005930")
        self.assertIn("progress", detail)
        self.assertNotIn("approval_nonce_hash", detail["job"])

    def test_approval_endpoint(self) -> None:
        prompt_hash = self._prepare_approval_job()
        issued = self.client.post(
            f"/api/jobs/{self.job.job_id}/approve",
            headers=self.headers,
            json={"action": "issue", "prompt_hash": prompt_hash},
        )
        self.assertEqual(issued.status_code, 200)
        nonce = issued.json()["approval_nonce"]
        approved = self.client.post(
            f"/api/jobs/{self.job.job_id}/approve",
            headers=self.headers,
            json={
                "action": "consume",
                "prompt_hash": prompt_hash,
                "approval_nonce": nonce,
            },
        )
        self.assertEqual(approved.status_code, 200)
        self.assertEqual(approved.json()["status"], "APPROVED")
        reused = self.client.post(
            f"/api/jobs/{self.job.job_id}/approve",
            headers=self.headers,
            json={
                "action": "consume",
                "prompt_hash": prompt_hash,
                "approval_nonce": nonce,
            },
        )
        self.assertEqual(reused.status_code, 409)

    def test_approval_requires_local_token(self) -> None:
        prompt_hash = self._prepare_approval_job()
        url = f"/api/jobs/{self.job.job_id}/approve"
        missing = self.client.post(
            url,
            headers={"Origin": "http://testserver"},
            json={"action": "issue", "prompt_hash": prompt_hash},
        )
        wrong_origin = self.client.post(
            url,
            headers={
                "Origin": "https://attacker.example",
                "X-E2R-Local-Token": self.token,
            },
            json={"action": "issue", "prompt_hash": prompt_hash},
        )
        self.assertEqual(missing.status_code, 403)
        self.assertEqual(wrong_origin.status_code, 403)

    def test_cancel(self) -> None:
        response = self.client.post(
            f"/api/jobs/{self.job.job_id}/cancel",
            headers=self.headers,
            json={"reason": "사용자 요청"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["job"]["status"], "CANCELLED")

    def test_clarification(self) -> None:
        for target, context in (
            (JobStatus.PACKET_BUILDING, None),
            (JobStatus.PACKET_READY, None),
            (JobStatus.BROWSER_PREPARING, None),
            (JobStatus.AWAITING_USER_APPROVAL, None),
            (JobStatus.APPROVED, None),
            (
                JobStatus.SUBMITTING,
                TransitionContext(approval_nonce_consumed=True),
            ),
            (JobStatus.RESEARCH_RUNNING, None),
            (JobStatus.AWAITING_CLARIFICATION, None),
        ):
            self._transition(target, context=context)
        answers = []

        def answer(job_id: str, text: str):
            answers.append((job_id, text))
            job = self.store.get_job(job_id)
            self.job = self.store.transition(
                job_id,
                expected_version=job.state_version,
                to_status=JobStatus.RESEARCH_RUNNING,
                actor="dashboard-clarification",
                idempotency_key=f"dashboard-clarification:{job.state_version}",
                payload={"answer_hash": canonical_hash(text)},
            )
            return {"status": self.job.status}

        app = create_pro_first_dashboard_app(
            store=self.store,
            config=self.config,
            actions=DashboardActions(submit_clarification=answer),
            approval_service=ProApprovalService(self.store, now=self.now),
        )
        response = TestClient(app).post(
            f"/api/jobs/{self.job.job_id}/clarification",
            headers=self.headers,
            json={"answer": "MEMORY segment 기준으로 계속 진행"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "RESEARCH_RUNNING")
        self.assertEqual(len(answers), 1)

    def test_result_publication(self) -> None:
        job_root = self._finalize_job()
        publisher = ProResultPublisher(self.store)
        first = publisher.publish(self.job.job_id, job_root=job_root)
        second = publisher.publish(self.job.job_id, job_root=job_root)
        self.assertEqual(first.result, second.result)
        self.assertEqual(first.result["component_coverage"], "7/7")
        self.assertEqual(first.result["judge_coverage"], "21/21")
        self.assertEqual(first.result["canonical_stage"], "1")
        self.assertFalse(first.result["investment_recommendation"])
        response = self.client.get(f"/api/results/{self.job.job_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), first.result)
        self.assertIsNotNone(self.store.get_job(self.job.job_id).published_at)

    def _same_dossier_reuse(self):
        job_root = self._finalize_job()
        published = ProResultPublisher(self.store).publish(
            self.job.job_id,
            job_root=job_root,
        )
        dossier_receipt = self.store.get_dossier_import_receipt(self.job.job_id)
        self.assertIsNotNone(dossier_receipt)
        dossier_hash = str(dossier_receipt["normalized_dossier_hash"])
        before_jobs = self.store.list_jobs()

        reused = ProSameInputReuseGate(self.store).evaluate(
            prior_job_id=self.job.job_id,
            current_trigger_fingerprint=self.job.trigger_fingerprint,
            prior_source_delta_hash="SOURCE-DELTA-SAME",
            current_source_delta_hash="SOURCE-DELTA-SAME",
            expected_dossier_hash=dossier_hash,
        )

        self.assertIsNotNone(reused)
        return reused, published, before_jobs

    def test_same_snapshot_zero_pro_submit(self) -> None:
        reused, published, before_jobs = self._same_dossier_reuse()

        self.assertEqual(reused.result, published.result)
        self.assertEqual(reused.receipt["status"], "SAME_DOSSIER_NOOP")
        self.assertEqual(reused.receipt["browser_submit_count"], 0)
        self.assertEqual(reused.receipt["new_pro_research_count"], 0)
        self.assertTrue(reused.receipt["no_new_job_created"])
        self.assertEqual(self.store.list_jobs(), before_jobs)

    def test_same_snapshot_zero_gap_search(self) -> None:
        reused, published, before_jobs = self._same_dossier_reuse()

        self.assertEqual(reused.result, published.result)
        self.assertEqual(reused.receipt["supplemental_query_count"], 0)
        self.assertEqual(reused.receipt["supplemental_fetch_count"], 0)
        self.assertEqual(reused.receipt["source_fetch_count"], 0)
        self.assertEqual(reused.receipt["recomputed_component_count"], 0)
        self.assertEqual(reused.receipt["recomputed_judge_count"], 0)
        self.assertEqual(reused.receipt["score_variance"], 0.0)
        self.assertEqual(reused.receipt["stage_variance"], 0)
        self.assertTrue(reused.receipt["no_new_job_created"])
        self.assertEqual(self.store.list_jobs(), before_jobs)


if __name__ == "__main__":
    unittest.main()
