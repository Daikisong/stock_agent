from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from urllib.parse import urlencode

from fastapi.testclient import TestClient

from e2r.pro_first.approval import ExactlyOnceSubmitCoordinator, ProApprovalService
from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.completion_monitor import (
    BrowserCompletionMonitor,
    ProCompletionStateService,
)
from e2r.pro_first.browser.mock_chatgpt_app import MockChatGPTServer
from e2r.pro_first.browser.protocol import BrowserCaptureRequest
from e2r.pro_first.capture.atomic_capture import AtomicCaptureWriter, CaptureIdentity
from e2r.pro_first.capture.coordinator import (
    CaptureFilesystemReconciler,
    ProCaptureCoordinator,
)
from e2r.pro_first.dashboard import LocalDashboardConfig, create_pro_first_dashboard_app
from e2r.pro_first.dossier import ProDossierImporter
from e2r.pro_first.gaps.adjudicator import DeterministicGapContext
from e2r.pro_first.gaps.service import ProGapAdjudicationService
from e2r.pro_first.ids import canonical_hash, canonical_json, stable_id
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.packet import PacketBuildInput, ResearchPacketBuilder, write_packet_bundle
from e2r.pro_first.prompt_contract import ProResearchPromptContract
from e2r.pro_first.publication import ProResultPublisher
from e2r.pro_first.scoring.service import ProScoringPipelineService
from e2r.pro_first.state_machine import TransitionContext
from e2r.pro_first.verification import ProSourceVerificationService, ProSourceVerifier
from e2r.research.page_fetcher import PageFetcher
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER
from e2r.research_brain.scoring import CreditValidatedImpact
from tests.full_score_validity_fixture import passing_full_score_validity_evidence


FIXTURE_ROOT = Path(__file__).parent / "fixtures/pro_first"


_IMPACT_COMPONENT_BY_PREDICATE = {
    "actual_earnings_conversion": "eps_fcf_explosion",
    "hbm_capacity_pre_sold": "earnings_visibility",
    "memory_price_increase_mentioned": "bottleneck_pricing",
    "spread_expansion": "bottleneck_pricing",
    "opm_expansion_pctp": "eps_fcf_explosion",
    "raw_material_cost_risk": "bottleneck_pricing",
    "arr_growth_visible": "earnings_visibility",
    "retention_or_renewal": "earnings_visibility",
}


class _GoldenEvidenceOnlyJudgeProvider:
    provider_name = "GOLDEN_EVIDENCE_ONLY_NO_SEARCH"

    def __init__(self) -> None:
        self.requests: list[dict] = []

    def judge(self, request):
        self.requests.append(dict(request))
        memo = request["component_memo"]
        positives = tuple(memo.get("positive_fact_ids") or ())
        counters = tuple(memo.get("counter_fact_ids") or ())
        proposed = min(float(memo["component_max_points"]), 3.0 if positives else 0.0)
        return {
            "proposed_points": proposed,
            "allowed_range": [0.0, min(float(memo["component_max_points"]), 3.0)],
            "rationale": "검증된 source-backed fact와 counterfact만 비교했다.",
            "anchor_comparisons": ["verified evidence versus component anchor"],
            "disagreements": [],
            "support_fact_ids": list(positives),
            "counter_fact_ids": list(counters),
            "nearest_anchor_ids": list(memo.get("historical_anchor_ids") or ())[:1],
            "why_not_higher": "추가 검증 fact 없이는 상단을 넓히지 않는다.",
            "why_not_lower": "현재 검증 fact와 counterfact가 하단을 제한한다.",
        }


@dataclass(frozen=True)
class _GoldenRun:
    result: dict
    score_receipt: dict
    stagecourt_receipt: dict
    source_rows: tuple[dict, ...]
    gap_rows: tuple[dict, ...]
    job_id: str
    submit_count: int
    capture_count: int
    judge_call_count: int
    browser_submit_count: int
    full_restart_count: int


class ProFirstBrowserGoldenE2ETest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.runtime_root = Path(self.temporary_directory.name)
        self.database_path = self.runtime_root / "pro_first.sqlite3"
        self.now = datetime(2026, 6, 30, 9, 0, 0, tzinfo=timezone.utc)
        self.server = MockChatGPTServer()
        self.server.__enter__()
        self.addCleanup(self.server.__exit__, None, None, None)

    async def asyncSetUp(self) -> None:
        from playwright.async_api import async_playwright

        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page(accept_downloads=True)

    async def asyncTearDown(self) -> None:
        await self.browser.close()
        await self.playwright.stop()

    async def test_c06_full_offline_e2e(self) -> None:
        run = await self._run_bundle("c06")
        self._assert_common_invariants(run, "c06")
        self.assertEqual(
            {row["planner_label"] for row in run.gap_rows},
            {"CORROBORATION_CAP"},
        )

    async def test_c17_full_offline_e2e(self) -> None:
        run = await self._run_bundle("c17")
        self._assert_common_invariants(run, "c17")
        self.assertEqual(
            sum(row["status"] == "ACCEPTED_COUNTER" for row in run.source_rows),
            1,
        )
        self.assertEqual(run.result["canonical_stage"], "0")
        self.assertEqual(
            run.score_receipt["pending_reasons"], ["bottleneck_pricing"]
        )

    async def test_c24_or_c28_full_offline_e2e(self) -> None:
        run = await self._run_bundle("c28")
        self._assert_common_invariants(run, "c28")
        guard = next(
            row
            for row in run.source_rows
            if row["dossier_fact_id"] == "PROFACT-C28-PROFILE-GUARD"
        )
        self.assertEqual(guard["status"], "ACCEPTED_CURRENT")
        self.assertEqual(guard["allowed_component_ids"], [])
        self.assertTrue(guard["component_rejection_reasons"])

    async def test_backend_restart_after_capture(self) -> None:
        run = await self._run_bundle("c06", restart_after_capture=True)
        self._assert_common_invariants(run, "c06")
        self.assertEqual(run.capture_count, 1)
        self.assertEqual(run.full_restart_count, 0)

    async def _run_bundle(
        self,
        bundle_name: str,
        *,
        restart_after_capture: bool = False,
    ) -> _GoldenRun:
        fixture_root = FIXTURE_ROOT / bundle_name
        packet_fixture = self._read_json(fixture_root / "research_packet.json")
        dossier_fixture = self._read_json(fixture_root / "research_dossier.json")
        invariants = self._read_json(fixture_root / "expected_invariants.json")
        report_template = (fixture_root / "pro_report.md").read_text(encoding="utf-8")
        for forbidden in (
            "expected_score",
            "expected_stage",
            "final_score",
            "final_stage",
            "canonical_stage",
            "score_value",
            "stage_decision",
        ):
            self.assertNotIn(forbidden, report_template.casefold())

        store = ProFirstJobStore(self.database_path, now=lambda: self.now)
        target = packet_fixture["target"]
        archetype_id = str(invariants["archetype_id"])
        candidate = store.create_candidate(
            symbol=str(target["symbol"]),
            company_name=str(target["company_name"]),
            as_of_date=str(packet_fixture["as_of_date"]),
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint=f"golden:{invariants['bundle_id']}",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={
                "production_candidate": True,
                "trigger_ids": [packet_fixture["trigger_summary"][0]["trigger_id"]],
                "reason_codes": ["PRO_FIRST_GOLDEN_E2E"],
            },
        )
        job = store.create_job(candidate.candidate_id, archetype_ids=(archetype_id,))
        job = store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.PACKET_BUILDING,
            actor="golden-e2e-packet",
            idempotency_key=f"golden:{bundle_name}:packet-building",
        )
        packet = ResearchPacketBuilder().build(
            PacketBuildInput(
                job_id=job.job_id,
                symbol=job.symbol,
                company_name=job.company_name,
                aliases=tuple(target.get("aliases") or ()),
                as_of_date=job.as_of_date,
                latest_trading_snapshot_date=str(
                    packet_fixture["latest_trading_snapshot_date"]
                ),
                research_mode=ResearchMode.FULL_RESEARCH,
                trigger_summary=tuple(packet_fixture["trigger_summary"]),
                candidate_archetypes=tuple(packet_fixture["candidate_archetypes"]),
                business_snapshot=dict(packet_fixture["business_snapshot"]),
                structured_financial_snapshot=dict(
                    packet_fixture["structured_financial_snapshot"]
                ),
                revision_valuation_snapshot=dict(
                    packet_fixture["revision_valuation_snapshot"]
                ),
                research_objectives=tuple(packet_fixture["research_objectives"]),
                source_preferences=tuple(packet_fixture["source_preferences"]),
                forbidden_inferences=tuple(packet_fixture["forbidden_inferences"]),
            )
        )
        job_root = self.runtime_root / "jobs" / job.job_id
        packet_bundle = write_packet_bundle(
            packet,
            job_root / "packet",
            commit_sha="golden-e2e-commit",
            config_hash=canonical_hash({"fixture": invariants["bundle_id"]}),
        )
        manifest = self._read_json(packet_bundle.packet_manifest)
        packet_id = stable_id(
            "PROPACKET", {"job_id": job.job_id, "packet_hash": packet.packet_hash}
        )
        job = store.record_packet(
            job.job_id,
            expected_version=job.state_version,
            packet_id=packet_id,
            packet_hash=packet.packet_hash,
            manifest={**manifest, "packet_id": packet_id},
            actor="golden-e2e-packet",
            idempotency_key=f"golden:{bundle_name}:packet-ready",
        )
        job = store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="golden-e2e-browser",
            idempotency_key=f"golden:{bundle_name}:browser-preparing",
        )

        run_id = str(packet.payload["run_id"])
        dossier = json.loads(json.dumps(dossier_fixture, ensure_ascii=False))
        dossier["job_id"] = job.job_id
        dossier["run_id"] = run_id
        dossier["target"] = {
            **dict(dossier["target"]),
            "target_id": job.symbol,
            "symbol": job.symbol,
            "company_name": job.company_name,
        }
        dossier["as_of_date"] = job.as_of_date
        for fact in (*dossier["material_facts"], *dossier["counterfacts"]):
            fact["target_id"] = job.symbol
            fact["subject"] = job.company_name
        report = (
            report_template.replace(str(packet_fixture["job_id"]), job.job_id)
            .replace(str(packet_fixture["run_id"]), run_id)
            .replace("{{RESEARCH_DOSSIER_JSON}}", canonical_json(dossier))
        )
        self.server.set_report_text(report)

        prompt = ProResearchPromptContract().render(
            job_id=job.job_id,
            run_id=run_id,
            symbol=job.symbol,
            as_of_date=job.as_of_date,
        )
        query = urlencode(
            {
                "job_id": job.job_id,
                "run_id": run_id,
                "target_id": job.symbol,
                "as_of_date": job.as_of_date,
                "filename": prompt.output_filename,
            }
        )
        await self.page.goto(
            f"{self.server.base_url}/c/{bundle_name}-golden?{query}",
            wait_until="domcontentloaded",
        )
        adapter = PlaywrightChatGPTWebAdapter(self.page)
        browser_session_id = stable_id(
            "PROBROWSER", {"job_id": job.job_id, "bundle": bundle_name}
        )
        prepared = await adapter.prepare_without_submit(
            browser_session_id=browser_session_id,
            packet_path=packet_bundle.research_packet_json,
            packet_hash=packet.packet_hash,
            prompt=prompt.text,
            prompt_hash=prompt.prompt_hash,
        )
        job = store.record_browser_prepared(
            job.job_id,
            expected_version=job.state_version,
            browser_session_id=prepared.browser_session_id,
            conversation_id=prepared.conversation_id,
            adapter_name="PlaywrightChatGPTWebAdapter",
            packet_hash=prepared.packet_hash,
            prompt_hash=prepared.prompt_hash,
            state={
                "state": prepared.state.value,
                "uploaded_filename": prepared.uploaded_filename,
                "send_ready": prepared.send_ready,
            },
            actor="golden-e2e-browser",
            idempotency_key=f"golden:{bundle_name}:browser-prepared",
        )
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

        local_token = "golden-dashboard-token-0123456789"
        dashboard = create_pro_first_dashboard_app(
            store=store,
            config=LocalDashboardConfig(
                runtime_root=self.runtime_root,
                allowed_origins=("http://testserver",),
                local_token=local_token,
            ),
            approval_service=ProApprovalService(store, now=lambda: self.now),
        )
        headers = {
            "Origin": "http://testserver",
            "X-E2R-Local-Token": local_token,
        }
        with TestClient(dashboard) as client:
            issued = client.post(
                f"/api/jobs/{job.job_id}/approve",
                headers=headers,
                json={"action": "issue", "prompt_hash": prompt.prompt_hash},
            )
            self.assertEqual(issued.status_code, 200, issued.text)
            approved = client.post(
                f"/api/jobs/{job.job_id}/approve",
                headers=headers,
                json={
                    "action": "consume",
                    "prompt_hash": prompt.prompt_hash,
                    "approval_nonce": issued.json()["approval_nonce"],
                },
            )
            self.assertEqual(approved.status_code, 200, approved.text)
            self.assertEqual(approved.json()["status"], "APPROVED")

        submitted = await ExactlyOnceSubmitCoordinator(store).submit(
            job.job_id, adapter, actor="golden-e2e-browser"
        )
        self.assertEqual(submitted.job.status, JobStatus.RESEARCH_RUNNING.value)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 1)
        await self.page.evaluate(
            "([state, context]) => window.__setMockState(state, context)",
            [
                "COMPLETE_WITH_MD",
                {
                    "job_id": job.job_id,
                    "run_id": run_id,
                    "target_id": job.symbol,
                    "as_of_date": job.as_of_date,
                    "filename": prompt.output_filename,
                },
            ],
        )
        completion = ProCompletionStateService(
            store,
            BrowserCompletionMonitor(
                adapter,
                required_stable_observations=3,
                poll_interval_seconds=0.01,
            ),
        )
        observed = None
        for _ in range(3):
            detected, observed = await completion.observe_job(job.job_id, run_id=run_id)
        self.assertEqual(detected.status, JobStatus.RESULT_DETECTED.value)
        self.assertIsNotNone(observed)
        self.assertTrue(observed.completion_confirmed)
        self.assertIsNotNone(observed.result)

        if restart_after_capture:
            capturing = store.transition(
                job.job_id,
                expected_version=detected.state_version,
                to_status=JobStatus.CAPTURING_ARTIFACTS,
                actor="golden-e2e-capture",
                idempotency_key=f"golden:{bundle_name}:capture-before-restart",
            )
            raw = await adapter.capture_result(
                BrowserCaptureRequest(
                    job_id=job.job_id,
                    run_id=run_id,
                    expected_filename=prompt.output_filename,
                    expected_report_hash=observed.result.report_hash,
                    staging_directory=job_root / "capture/.staging",
                )
            )
            AtomicCaptureWriter(now=lambda: self.now).finalize(
                job_root,
                identity=CaptureIdentity(
                    job_id=job.job_id,
                    run_id=run_id,
                    target_id=job.symbol,
                    as_of_date=job.as_of_date,
                    packet_hash=packet.packet_hash,
                    prompt_hash=prompt.prompt_hash,
                    conversation_id=capturing.conversation_id,
                    capture_mode="DOM_CONTRACT_MOCK_RESTART",
                ),
                raw_capture=raw,
            )
            store = ProFirstJobStore(self.database_path, now=lambda: self.now)
            recovered = await CaptureFilesystemReconciler(store).reconcile(job_root)
            self.assertIsNotNone(recovered)
        else:
            completed, _capture = await ProCaptureCoordinator(
                store, writer=AtomicCaptureWriter(now=lambda: self.now)
            ).capture(
                job.job_id,
                run_id=run_id,
                expected_filename=prompt.output_filename,
                expected_report_hash=observed.result.report_hash,
                job_root=job_root,
                adapter=adapter,
                capture_mode="DOM_CONTRACT_MOCK_GOLDEN",
            )
            self.assertEqual(completed.status, JobStatus.CAPTURE_COMPLETE.value)

        imported = ProDossierImporter(store, now=lambda: self.now).import_job(
            job.job_id, job_root=job_root
        )
        self.assertEqual(imported.job.status, JobStatus.DOSSIER_IMPORTED.value)
        source_documents = {
            str(url): fixture_root / "source_pages" / str(filename)
            for url, filename in invariants["source_documents"].items()
        }
        verification = ProSourceVerificationService(
            store,
            verifier=ProSourceVerifier(
                page_fetcher=PageFetcher(
                    fixture_text_by_url=source_documents,
                    live_enabled=False,
                    max_text_chars=None,
                )
            ),
        ).verify_job(job.job_id, job_root=job_root)
        self.assertIsNotNone(verification.result)
        self.assertEqual(
            verification.receipt["accepted_fact_candidate_count"],
            invariants["accepted_fact_count"],
        )
        source_rows = tuple(
            row.to_dict() for row in verification.result.verifications
        )

        contexts = {}
        for gap in imported.normalized_dossier["unresolved_gaps"]:
            component_id = str(gap["affected_component_ids"][0])
            contexts[str(gap["dossier_gap_id"])] = DeterministicGapContext(
                dossier_gap_id=str(gap["dossier_gap_id"]),
                component_lower_delta={component_id: 0.0},
                component_upper_delta={component_id: 2.0},
                deterministic_lower_stage="2",
                deterministic_upper_stage="2",
                executable_new_source_route_signatures=(),
                could_change_score=True,
                question_family_id=(
                    f"{archetype_id}:LEGACY_V1:{gap['stable_objective_id']}"
                ),
                mandatory_primary_source_roles=("ISSUER_OFFICIAL",),
                verified_primary_source_roles=("ISSUER_OFFICIAL",),
                missing_route_is_independent_corroboration=True,
                missing_predicate_is_new_core=False,
                public_route_fixpoint_reached=True,
                hard_break_polarity_resolved=True,
                score_stage_range_bounded=True,
                rationale="동일 deterministic Stage 범위의 독립 corroboration 공백",
            )
        gap_run = ProGapAdjudicationService(store).adjudicate_job(
            job.job_id,
            job_root=job_root,
            deterministic_contexts=contexts,
        )
        self.assertEqual(gap_run.job.status, JobStatus.COMPONENT_RESEARCH.value)
        self.assertEqual(
            gap_run.receipt["supplemental_task_count"],
            invariants["supplemental_task_count"],
        )
        self.assertEqual(gap_run.receipt["full_research_restart_count"], 0)

        facts = tuple(verification.result.fact_compilation.facts)
        impacts = self._validated_impacts(
            facts=facts,
            archetype_id=archetype_id,
            target_id=job.symbol,
        )
        impacted_components = {row.component_id for row in impacts}
        terminal_evidence = {
            component_id: {
                "status": "VERIFIED_ABSENT_AFTER_SEARCH",
                "search_exhaustion_proof": [
                    f"{invariants['bundle_id']}:SOURCE_VERIFICATION_COMPLETE"
                ],
            }
            for component_id in CANONICAL_COMPONENT_ORDER
            if component_id not in impacted_components
        }
        anchors = tuple(
            {
                "anchor_id": f"ANCHOR-{archetype_id}-{component_id}",
                "archetype_id": archetype_id,
                "component_id": component_id,
                "points_lower": 0.0,
                "points_mid": 1.0,
                "points_upper": 3.0,
            }
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        judge_provider = _GoldenEvidenceOnlyJudgeProvider()
        scoring = ProScoringPipelineService(store).run_job(
            job.job_id,
            job_root=job_root,
            selected_archetype_id=archetype_id,
            judge_provider=judge_provider,
            historical_anchors=anchors,
            validated_impacts=impacts,
            terminal_evidence=terminal_evidence,
            validity_evidence=passing_full_score_validity_evidence(
                f"{invariants['bundle_id']}:FULL_SCORE_VALIDITY"
            ),
        )
        self.assertEqual(scoring.job.status, JobStatus.FINAL.value)
        published = ProResultPublisher(store).publish(job.job_id, job_root=job_root)
        final_job = store.get_job(job.job_id)
        return _GoldenRun(
            result=dict(published.result),
            score_receipt=dict(scoring.score_receipt or {}),
            stagecourt_receipt=dict(scoring.stagecourt_receipt or {}),
            source_rows=source_rows,
            gap_rows=tuple(dict(row) for row in store.get_gap_decisions(job.job_id)),
            job_id=job.job_id,
            submit_count=final_job.submit_count,
            capture_count=final_job.capture_count,
            judge_call_count=len(judge_provider.requests),
            browser_submit_count=int(await self.page.evaluate("window.__submitCount")),
            full_restart_count=int(gap_run.receipt["full_research_restart_count"]),
        )

    def _assert_common_invariants(self, run: _GoldenRun, bundle_name: str) -> None:
        invariants = self._read_json(
            FIXTURE_ROOT / bundle_name / "expected_invariants.json"
        )
        self.assertEqual(run.submit_count, 1)
        self.assertEqual(run.browser_submit_count, 1)
        self.assertEqual(run.capture_count, 1)
        self.assertEqual(run.judge_call_count, 21)
        self.assertEqual(run.result["component_coverage"], "7/7")
        self.assertEqual(run.result["judge_coverage"], "21/21")
        self.assertIs(
            run.result["score_valid"],
            invariants["score_must_be_valid"],
            canonical_json(run.score_receipt),
        )
        if invariants["decision_must_be_final"]:
            self.assertEqual(run.result["stage_status"], "FINAL")
        else:
            self.assertTrue(str(run.result["stage_status"]).startswith("PENDING"))
        self.assertEqual(
            {row["planner_label"] for row in run.gap_rows},
            set(invariants["gap_labels"]),
        )
        vector = run.result["component_vector"]
        self.assertEqual(set(vector), set(CANONICAL_COMPONENT_ORDER))
        self.assertEqual(
            {component for component, points in vector.items() if float(points) > 0},
            set(invariants["nonzero_components"]),
        )
        self.assertEqual(run.score_receipt["judge_decision_count"], 21)
        self.assertEqual(run.score_receipt["reuse_receipt"]["scoring_query_count"], 0)
        self.assertEqual(run.score_receipt["reuse_receipt"]["scoring_fetch_count"], 0)
        self.assertEqual(run.full_restart_count, invariants["full_restart_count"])
        self.assertEqual(
            sum(row["status"].startswith("ACCEPTED_") for row in run.source_rows),
            invariants["accepted_fact_count"],
        )

    @staticmethod
    def _validated_impacts(*, facts, archetype_id: str, target_id: str):
        impacts = []
        for fact in facts:
            primitive_id = str(fact.predicate).casefold()
            component_id = _IMPACT_COMPONENT_BY_PREDICATE.get(primitive_id)
            if component_id is None or component_id not in set(fact.allowed_component_ids):
                continue
            claim_id = str(fact.claim_ids[0])
            direction = "COUNTER" if fact.direction == "COUNTER" else "SUPPORT"
            support_type = "RISK_OPEN" if direction == "COUNTER" else "DIRECT_ACTUAL"
            strength = 0.5 if direction == "COUNTER" else 0.6
            impacts.append(
                CreditValidatedImpact(
                    impact_id=stable_id(
                        "PROIMPACT",
                        {"claim_id": claim_id, "component_id": component_id},
                    ),
                    claim_id=claim_id,
                    mapping_id=stable_id("PROMAPPING", {"claim_id": claim_id}),
                    target_id=target_id,
                    archetype_id=archetype_id,
                    primitive_id=primitive_id,
                    component_id=component_id,
                    direction=direction,
                    support_type=support_type,
                    source_family="ISSUER_OFFICIAL",
                    source_independence_key=fact.source_independence_group,
                    evidence_family_id=stable_id(
                        "PROEVIDENCEFAMILY", {"primitive_id": primitive_id}
                    ),
                    question_family_id="",
                    component_subcriterion_id="",
                    raw_credit_fraction=strength,
                    validated_credit_fraction=strength,
                    support_credit_fraction=strength if direction == "SUPPORT" else 0.0,
                    counter_effect_fraction=strength if direction == "COUNTER" else 0.0,
                    resolution_effect=0.0,
                    strength_fraction=strength,
                    completeness_fraction=1.0,
                    causal_cap=1.0,
                    source_cap=1.0,
                    temporal_cap=1.0,
                    support_type_cap=1.0,
                    evidence_confidence=fact.confidence,
                    scope_validation={
                        "status": "MECHANISM_SCOPE_PASS",
                        "scope_match": True,
                        "scope": {
                            "issuer_id": target_id,
                            "business_segment": fact.business_segment,
                            "product_family": fact.product_family,
                            "economic_mechanism": fact.economic_mechanism,
                        },
                    },
                    fact_cluster_id=stable_id(
                        "PROFACTCLUSTER",
                        {"claim_id": claim_id, "period": fact.period},
                    ),
                    document_cluster_id=stable_id(
                        "PRODOCCLUSTER", {"source_ids": list(fact.source_ids)}
                    ),
                    claim_budget_scaled=False,
                    fact_budget_scaled=False,
                    document_budget_scaled=False,
                    evidence_family_budget_scaled=False,
                    correlation_scaled=False,
                    information_diversity_scaled=False,
                    corroboration_only=False,
                    duplicate_reason=None,
                    eligibility_decision_id=stable_id(
                        "PROELIGIBILITY", {"claim_id": claim_id}
                    ),
                )
            )
        if not impacts:
            raise AssertionError("source-backed facts produced no validated scoring impacts")
        return tuple(impacts)

    @staticmethod
    def _read_json(path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
