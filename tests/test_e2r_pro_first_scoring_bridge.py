from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from e2r.pro_first.ids import canonical_hash, canonical_json
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.scoring.component_bridge import ProComponentMemoCompiler
from e2r.pro_first.scoring.judge_bridge import ProEvidenceOnlyJudgeBridge
from e2r.pro_first.scoring.scorer_bridge import ProCalibratedScorerBridge
from e2r.pro_first.scoring.service import ProScoringPipelineService
from e2r.pro_first.reuse import DeltaScoringReuseContext
from e2r.pro_first.scoring.stagecourt_bridge import ProAtomicStageCourtBridge
from e2r.pro_first.state_machine import TransitionContext
from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
    EvidenceFact,
)
from tests.full_score_validity_fixture import passing_full_score_validity_evidence
from tests.test_component_assessment_states import supported_impact


class _EvidenceOnlyProvider:
    provider_name = "UNIT_EVIDENCE_ONLY_PROVIDER"

    def __init__(self, *, fail_after: int | None = None) -> None:
        self.requests: list[dict] = []
        self.fail_after = fail_after

    def judge(self, request):
        self.requests.append(dict(request))
        if self.fail_after is not None and len(self.requests) > self.fail_after:
            raise RuntimeError("unit provider unavailable")
        memo = request["component_memo"]
        positive = tuple(memo.get("positive_fact_ids") or ())
        counter = tuple(memo.get("counter_fact_ids") or ())
        proposed = 3.0 if positive else 0.0
        maximum = float(memo["component_max_points"])
        anchor = tuple(memo.get("historical_anchor_ids") or ())[:1]
        return {
            "proposed_points": proposed,
            "allowed_range": [0.0, min(maximum, max(3.0, proposed))],
            "rationale": "검증된 fact와 historical anchor만 비교했다.",
            "anchor_comparisons": ["verified evidence versus nearest anchor"],
            "disagreements": [],
            "support_fact_ids": list(positive),
            "counter_fact_ids": list(counter),
            "nearest_anchor_ids": list(anchor),
            "why_not_higher": "추가 검증 fact 없이는 상단을 넓히지 않는다.",
            "why_not_lower": "현재 검증 fact가 하단을 지지한다.",
        }


class ProFirstScoringBridgeTest(unittest.TestCase):
    archetype_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.store = ProFirstJobStore(
            Path(self.temporary_directory.name) / "scoring.sqlite3",
            now=lambda: datetime(2026, 8, 22, 3, 4, 5, tzinfo=timezone.utc),
        )
        candidate = self.store.create_candidate(
            symbol="005930",
            company_name="검증기업",
            as_of_date="2026-08-22",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="scoring-trigger",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        self.job = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=(self.archetype_id,),
        )
        self.fact = EvidenceFact(
            fact_id="EFACT-verified",
            target_id=self.job.symbol,
            as_of_date=self.job.as_of_date,
            subject="검증기업",
            business_segment="MEMORY",
            product_family="HBM",
            economic_mechanism="PRICING_POWER",
            predicate="MEMORY_PRICE_INCREASE_MENTIONED",
            value=10,
            unit="%",
            period="2026Q2",
            direction="POSITIVE",
            source_ids=("PROSRC-verified",),
            claim_ids=("C1",),
            quote_ids=("PROQUOTE-verified",),
            current_lifecycle="CURRENT",
            source_independence_group="PROSRCGROUP-issuer",
            confidence=0.9,
            allowed_component_ids=("bottleneck_pricing",),
        )
        self.anchors = tuple(
            {
                "anchor_id": f"ANCHOR-{component_id}",
                "archetype_id": self.archetype_id,
                "component_id": component_id,
                "points_lower": 0.0,
                "points_mid": 1.0,
                "points_upper": 3.0,
            }
            for component_id in CANONICAL_COMPONENT_ORDER
        )

    def _dossier(self) -> dict:
        components = {}
        for component_id in CANONICAL_COMPONENT_ORDER:
            components[component_id] = {
                "positive_fact_ids": (
                    ["PROFACT-verified", "PROFACT-unverified"]
                    if component_id == "bottleneck_pricing"
                    else []
                ),
                "counter_fact_ids": [],
                "resolution_fact_ids": [],
                "structured_metrics": {},
                "historical_anchor_ids": [f"ANCHOR-{component_id}"],
                "researcher_summary": f"{component_id} evidence-only summary",
                "positive_case": "검증된 positive fact만 사용한다.",
                "counter_case": "검증된 counter fact만 사용한다.",
                "uncertainties": [],
                "proposed_score_lower": 0.0,
                "proposed_score_mid": (
                    2.0 if component_id == "bottleneck_pricing" else 0.0
                ),
                "proposed_score_upper": (
                    3.0 if component_id == "bottleneck_pricing" else 0.0
                ),
                "confidence": 0.8,
                "why_not_higher": "원문 범위를 넘지 않는다.",
                "why_not_lower": "검증 fact를 반영한다.",
            }
        return {
            "component_research": components,
            "proposed_score_ranges": {"fake_total": 99.0},
            "proposed_stage": "5",
        }

    def _component_result(self, *, gap_decisions=()):
        return ProComponentMemoCompiler().compile(
            dossier=self._dossier(),
            job=self.job,
            selected_archetype_id=self.archetype_id,
            verified_facts=(self.fact,),
            source_verifications=(
                {
                    "dossier_fact_id": "PROFACT-verified",
                    "status": "ACCEPTED_CURRENT",
                    "compiled_claim_id": "C1",
                },
                {
                    "dossier_fact_id": "PROFACT-unverified",
                    "status": "REJECTED_QUOTE_MISMATCH",
                    "compiled_claim_id": None,
                },
            ),
            claim_fact_links=(
                {"claim_id": "C1", "fact_id": self.fact.fact_id},
            ),
            gap_decisions=gap_decisions,
            historical_anchors=self.anchors,
        )

    def _judge_result(self, provider=None):
        component = self._component_result()
        provider = provider or _EvidenceOnlyProvider()
        result = ProEvidenceOnlyJudgeBridge(provider).run(
            memos=component.memos,
            evidence_facts=(self.fact,),
            historical_anchors=self.anchors,
            gap_decisions=(),
        )
        return component, provider, result

    @staticmethod
    def _terminal_evidence() -> dict:
        return {
            component_id: {
                "status": "VERIFIED_ABSENT_AFTER_SEARCH",
                "search_exhaustion_proof": ["PRO-GAP-ADJUDICATION-COMPLETE"],
            }
            for component_id in CANONICAL_COMPONENT_ORDER
            if component_id != "bottleneck_pricing"
        }

    def _score_result(self, *, impacts=None, claim_fact_lineage=None):
        component, _, judges = self._judge_result()
        return ProCalibratedScorerBridge().score(
            selected_archetype_id=self.archetype_id,
            memos=component.memos,
            judge_result=judges,
            validated_impacts=tuple(impacts or (supported_impact(),)),
            terminal_evidence=self._terminal_evidence(),
            validity_evidence=passing_full_score_validity_evidence(
                "PRO-FIRST-UNIT-VALIDITY"
            ),
            accepted_claim_ids=("C1",),
            accepted_claim_fact_ids=(
                claim_fact_lineage
                if claim_fact_lineage is not None
                else {"C1": (self.fact.fact_id,)}
            ),
            proposed_score_ranges_hash=canonical_hash(
                self._dossier()["proposed_score_ranges"]
            ),
            proposed_stage="5",
        )

    def _prepare_durable_component_job(self, root: Path) -> None:
        transition_rows = (
            (JobStatus.PACKET_BUILDING, TransitionContext(), {}),
            (JobStatus.PACKET_READY, TransitionContext(), {}),
            (JobStatus.BROWSER_PREPARING, TransitionContext(), {}),
            (JobStatus.AWAITING_USER_APPROVAL, TransitionContext(), {}),
            (JobStatus.APPROVED, TransitionContext(), {}),
            (
                JobStatus.SUBMITTING,
                TransitionContext(approval_nonce_consumed=True),
                {},
            ),
            (JobStatus.RESEARCH_RUNNING, TransitionContext(), {}),
            (JobStatus.RESULT_DETECTED, TransitionContext(), {}),
            (JobStatus.CAPTURING_ARTIFACTS, TransitionContext(), {}),
            (JobStatus.CAPTURE_COMPLETE, TransitionContext(), {}),
            (
                JobStatus.IMPORTING,
                TransitionContext(capture_receipt_verified=True),
                {},
            ),
            (
                JobStatus.DOSSIER_IMPORTED,
                TransitionContext(dossier_validated=True),
                {"dossier_id": "PRODOSSIER-scoring-unit"},
            ),
            (JobStatus.VERIFYING_SOURCES, TransitionContext(), {}),
            (
                JobStatus.GAP_ADJUDICATION,
                TransitionContext(source_verification_complete=True),
                {},
            ),
            (JobStatus.COMPONENT_RESEARCH, TransitionContext(), {}),
        )
        for index, (target, context, updates) in enumerate(transition_rows):
            self.job = self.store.transition(
                self.job.job_id,
                expected_version=self.job.state_version,
                to_status=target,
                actor="scoring-integration-fixture",
                idempotency_key=f"scoring-integration-{index}-{target.value}",
                context=context,
                updates=updates,
            )
        import_root = root / "import"
        verification_root = root / "verification"
        import_root.mkdir(parents=True, exist_ok=True)
        verification_root.mkdir(parents=True, exist_ok=True)
        dossier = {**self._dossier(), "job_id": self.job.job_id}
        (import_root / "research_dossier.normalized.json").write_text(
            canonical_json(dossier) + "\n",
            encoding="utf-8",
        )
        artifact_rows = {
            "evidence_facts.jsonl": (self.fact.to_dict(),),
            "source_verifications.jsonl": (
                {
                    "dossier_fact_id": "PROFACT-verified",
                    "status": "ACCEPTED_CURRENT",
                    "compiled_claim_id": "C1",
                },
                {
                    "dossier_fact_id": "PROFACT-unverified",
                    "status": "REJECTED_QUOTE_MISMATCH",
                    "compiled_claim_id": None,
                },
            ),
            "claim_fact_links.jsonl": (
                {"claim_id": "C1", "fact_id": self.fact.fact_id},
            ),
        }
        for name, rows in artifact_rows.items():
            (verification_root / name).write_text(
                "".join(canonical_json(row) + "\n" for row in rows),
                encoding="utf-8",
            )

    def _run_durable_pipeline(
        self,
        root: Path,
        provider,
        *,
        delta_reuse_context: DeltaScoringReuseContext | None = None,
    ):
        return ProScoringPipelineService(self.store).run_job(
            self.job.job_id,
            job_root=root,
            selected_archetype_id=self.archetype_id,
            judge_provider=provider,
            historical_anchors=self.anchors,
            validated_impacts=(supported_impact(),),
            terminal_evidence=self._terminal_evidence(),
            validity_evidence=passing_full_score_validity_evidence(
                "PRO-FIRST-DURABLE-SCORING"
            ),
            delta_reuse_context=delta_reuse_context,
        )

    def test_component_bridge_uses_verified_fact_ids(self) -> None:
        result = self._component_result()
        self.assertEqual(len(result.memos), 7)
        pricing = next(
            row for row in result.memos if row.component_id == "bottleneck_pricing"
        )
        self.assertEqual(pricing.positive_fact_ids, (self.fact.fact_id,))
        self.assertNotIn("PROFACT-unverified", pricing.positive_fact_ids)
        self.assertIn(
            "PROFACT-unverified",
            result.removed_unverified_dossier_fact_ids,
        )
        self.assertEqual(pricing.source_coverage, ("PROSRC-verified",))

    def test_corroboration_gap_is_uncertainty_not_component_blocker(self) -> None:
        result = self._component_result(
            gap_decisions=(
                {
                    "assessment": {
                        "affected_component_ids": ["bottleneck_pricing"],
                    },
                    "deterministic_evidence_class": "CORROBORATION_CAP",
                    "planner_label": "CORROBORATION_CAP",
                },
            )
        )
        pricing = next(
            row for row in result.memos if row.component_id == "bottleneck_pricing"
        )
        self.assertTrue(pricing.research_complete)
        self.assertIn("gap:CORROBORATION_CAP", pricing.uncertainties)

    def test_21_judge_no_search_mode(self) -> None:
        _, provider, result = self._judge_result()
        self.assertEqual(result.status, "JUDGING_COMPLETE")
        self.assertEqual(len(result.decisions), 21)
        self.assertEqual(len(provider.requests), 21)
        self.assertTrue(
            all(request["mode"] == "EVIDENCE_ONLY_NO_SEARCH" for request in provider.requests)
        )
        self.assertTrue(
            all("total_score" not in request for request in provider.requests)
        )
        self.assertEqual(result.receipt_payload["query_count"], 0)
        self.assertEqual(result.receipt_payload["fetch_count"], 0)
        self.assertFalse(result.receipt_payload["web_search_allowed"])

    def test_judge_provider_failure_pending(self) -> None:
        component = self._component_result()
        provider = _EvidenceOnlyProvider(fail_after=2)
        judges = ProEvidenceOnlyJudgeBridge(provider).run(
            memos=component.memos,
            evidence_facts=(self.fact,),
            historical_anchors=self.anchors,
            gap_decisions=(),
        )
        self.assertEqual(judges.status, "JUDGING_PROVIDER_PENDING")
        self.assertFalse(judges.score_valid)
        scoring = ProCalibratedScorerBridge().score(
            selected_archetype_id=self.archetype_id,
            memos=component.memos,
            judge_result=judges,
            validated_impacts=(supported_impact(),),
            terminal_evidence=self._terminal_evidence(),
            validity_evidence=passing_full_score_validity_evidence(),
            accepted_claim_ids=("C1",),
            accepted_claim_fact_ids={"C1": (self.fact.fact_id,)},
        )
        self.assertIsNone(scoring.score)
        self.assertFalse(scoring.score_valid)
        self.assertEqual(scoring.status, "JUDGING_PROVIDER_PENDING")

    def test_pro_score_ignored(self) -> None:
        scoring = self._score_result()
        self.assertTrue(scoring.score_valid)
        self.assertEqual(scoring.score.full_e2r_score, 3.0)
        self.assertNotEqual(scoring.score.full_e2r_score, 99.0)
        self.assertTrue(scoring.receipt_payload["pro_score_ignored"])

    def test_pro_stage_ignored(self) -> None:
        scoring = self._score_result()
        stage = ProAtomicStageCourtBridge().decide(
            target_id=self.job.symbol,
            as_of_date=self.job.as_of_date,
            selected_archetype_id=self.archetype_id,
            score_result=scoring,
            accepted_claim_ids=("C1",),
            evidence_facts=(self.fact,),
            ignored_proposed_stage="5",
        )
        self.assertNotEqual(stage.decision.canonical_stage, "5")
        self.assertEqual(stage.receipt_payload["ignored_proposed_stage"], "5")
        self.assertTrue(stage.receipt_payload["pro_stage_ignored"])

    def test_deterministic_component_scorer_used(self) -> None:
        scoring = self._score_result()
        receipt = scoring.receipt_payload
        self.assertEqual(
            receipt["scorer_class"],
            "ResearchCalibratedComponentScorer",
        )
        self.assertEqual(receipt["new_score_engine_count"], 0)
        self.assertEqual(len(scoring.assessments), 7)

    def test_atomic_stagecourt_v2_used(self) -> None:
        scoring = self._score_result()
        stage = ProAtomicStageCourtBridge().decide(
            target_id=self.job.symbol,
            as_of_date=self.job.as_of_date,
            selected_archetype_id=self.archetype_id,
            score_result=scoring,
            accepted_claim_ids=("C1",),
            evidence_facts=(self.fact,),
        )
        self.assertEqual(stage.receipt_payload["stagecourt_class"], "AtomicStageCourtV2")
        self.assertEqual(stage.receipt_payload["new_stage_engine_count"], 0)
        self.assertEqual(len(stage.decision.component_assessment_ids), 7)
        self.assertEqual(stage.decision.claim_impact_ids, ("I1",))

    def test_nonzero_component_requires_lineage(self) -> None:
        scoring = self._score_result()
        nonzero = [
            row
            for row in scoring.assessments
            if scoring.score.component_score_vector[row.component_id] > 0
        ]
        self.assertEqual(len(nonzero), 1)
        self.assertEqual(nonzero[0].component_id, "bottleneck_pricing")
        self.assertEqual(nonzero[0].support_impact_ids, ("I1",))
        self.assertEqual(scoring.impacts[0].claim_id, "C1")
        self.assertEqual(
            scoring.impact_fact_lineage,
            {"C1": (self.fact.fact_id,)},
        )
        with self.assertRaisesRegex(ValueError, "lacks fact lineage"):
            self._score_result(
                claim_fact_lineage={"C1": ("EFACT-not-in-memo",)}
            )

    def test_durable_pipeline_reaches_final_exactly_once(self) -> None:
        root = Path(self.temporary_directory.name) / "durable-scoring-job"
        self._prepare_durable_component_job(root)
        provider = _EvidenceOnlyProvider()
        first = self._run_durable_pipeline(root, provider)
        second = self._run_durable_pipeline(
            root,
            _EvidenceOnlyProvider(fail_after=0),
        )
        self.assertEqual(first.job.status, JobStatus.FINAL.value)
        self.assertEqual(second.job.status, JobStatus.FINAL.value)
        self.assertEqual(len(provider.requests), 21)
        self.assertEqual(first.score_receipt, second.score_receipt)
        self.assertEqual(first.stagecourt_receipt, second.stagecourt_receipt)
        self.assertEqual(
            self.store.get_score_receipt(self.job.job_id),
            first.score_receipt,
        )
        self.assertEqual(
            self.store.get_stagecourt_receipt(self.job.job_id),
            first.stagecourt_receipt,
        )
        terminal_events = [
            event
            for event in self.store.list_events(self.job.job_id)
            if event.to_status
            in {
                JobStatus.JUDGING.value,
                JobStatus.SCORING.value,
                JobStatus.STAGECOURT.value,
                JobStatus.FINAL.value,
            }
        ]
        self.assertEqual(len(terminal_events), 4)

    def test_stagecourt_resume_does_not_repeat_judges(self) -> None:
        root = Path(self.temporary_directory.name) / "resume-scoring-job"
        self._prepare_durable_component_job(root)
        provider = _EvidenceOnlyProvider()
        original = self.store.record_score_result

        def interrupt_after_commit(*args, **kwargs):
            original(*args, **kwargs)
            raise RuntimeError("simulated process exit after score commit")

        with patch.object(
            self.store,
            "record_score_result",
            side_effect=interrupt_after_commit,
        ):
            with self.assertRaisesRegex(RuntimeError, "simulated process exit"):
                self._run_durable_pipeline(root, provider)
        self.assertEqual(
            self.store.get_job(self.job.job_id).status,
            JobStatus.STAGECOURT.value,
        )
        fail_if_called = _EvidenceOnlyProvider(fail_after=0)
        resumed = self._run_durable_pipeline(root, fail_if_called)
        self.assertEqual(resumed.job.status, JobStatus.FINAL.value)
        self.assertEqual(len(provider.requests), 21)
        self.assertEqual(fail_if_called.requests, [])

    def test_delta_reopens_only_impacted_components(self) -> None:
        prior_root = Path(self.temporary_directory.name) / "prior-full-job"
        self._prepare_durable_component_job(prior_root)
        prior_run = self._run_durable_pipeline(
            prior_root,
            _EvidenceOnlyProvider(),
        )
        prior_job = prior_run.job

        candidate = self.store.create_candidate(
            symbol=prior_job.symbol,
            company_name=prior_job.company_name,
            as_of_date=prior_job.as_of_date,
            scan_window=ScanWindow.EVENING,
            trigger_fingerprint="scoring-delta-trigger",
            research_mode=ResearchMode.DELTA_RESEARCH,
            selection_receipt={"production_candidate": True, "delta": True},
        )
        self.job = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=(self.archetype_id,),
        )
        delta_root = Path(self.temporary_directory.name) / "delta-job"
        self._prepare_durable_component_job(delta_root)
        delta_fact = replace(
            self.fact,
            fact_id="EFACT-delta-pricing",
            value=12,
            source_ids=("PROSRC-delta-pricing",),
            claim_ids=("C2",),
            quote_ids=("PROQUOTE-delta-pricing",),
        )
        dossier = {**self._dossier(), "job_id": self.job.job_id}
        dossier["component_research"]["bottleneck_pricing"][
            "positive_fact_ids"
        ].append("PROFACT-delta-pricing")
        (delta_root / "import/research_dossier.normalized.json").write_text(
            canonical_json(dossier) + "\n",
            encoding="utf-8",
        )
        verification_root = delta_root / "verification"
        rows_by_name = {
            "evidence_facts.jsonl": (self.fact.to_dict(), delta_fact.to_dict()),
            "source_verifications.jsonl": (
                {
                    "dossier_fact_id": "PROFACT-verified",
                    "status": "ACCEPTED_CURRENT",
                    "compiled_claim_id": "C1",
                },
                {
                    "dossier_fact_id": "PROFACT-delta-pricing",
                    "status": "ACCEPTED_CURRENT",
                    "compiled_claim_id": "C2",
                },
            ),
            "claim_fact_links.jsonl": (
                {"claim_id": "C1", "fact_id": self.fact.fact_id},
                {"claim_id": "C2", "fact_id": delta_fact.fact_id},
            ),
        }
        for name, rows in rows_by_name.items():
            (verification_root / name).write_text(
                "".join(canonical_json(row) + "\n" for row in rows),
                encoding="utf-8",
            )
        provider = _EvidenceOnlyProvider()
        result = self._run_durable_pipeline(
            delta_root,
            provider,
            delta_reuse_context=DeltaScoringReuseContext(
                prior_job_id=prior_job.job_id,
                prior_job_root=prior_root,
                components_to_revisit=("bottleneck_pricing",),
            ),
        )

        self.assertEqual(result.job.status, JobStatus.FINAL.value)
        self.assertEqual(len(provider.requests), 3)
        self.assertEqual(
            {request["component_memo"]["component_id"] for request in provider.requests},
            {"bottleneck_pricing"},
        )
        self.assertEqual(
            result.reuse_receipt["recomputed_components"],
            ["bottleneck_pricing"],
        )
        self.assertEqual(result.reuse_receipt["recomputed_component_count"], 1)
        self.assertEqual(result.reuse_receipt["reused_component_count"], 6)
        self.assertEqual(result.reuse_receipt["recomputed_judge_count"], 3)
        self.assertEqual(result.reuse_receipt["reused_judge_count"], 18)
        self.assertEqual(result.reuse_receipt["scoring_query_count"], 0)
        self.assertEqual(result.reuse_receipt["scoring_fetch_count"], 0)
        self.assertEqual(result.reuse_receipt["full_restart_count"], 0)


if __name__ == "__main__":
    unittest.main()
