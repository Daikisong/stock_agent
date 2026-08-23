from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest
from unittest.mock import patch

from e2r.pro_first.ids import canonical_hash, canonical_json
from e2r.pro_first.gaps.service import ProGapAdjudicationService
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.post_import import (
    ProFirstPostImportCoordinator,
    ProPostImportScoringInputs,
    compile_conservative_gap_contexts,
)
from e2r.pro_first.scoring.component_bridge import ProComponentMemoCompiler
from e2r.pro_first.scoring.audit import audit_scoring_publication_gate
from e2r.pro_first.scoring.codex_judge_provider import (
    CodexEvidenceOnlyJudgeProvider,
)
from e2r.pro_first.scoring.codex_dossier_impact_provider import (
    CodexDossierImpactProvider,
)
from e2r.pro_first.scoring.impact_compiler import ProValidatedImpactCompiler
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
from tests.research_saturation_fixture import (
    passing_research_saturation_receipt,
    v2_scoring_dossier,
)
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


class _ImpactProvider:
    provider_name = "UNIT_STRUCTURED_IMPACT_PROVIDER"

    def __init__(self) -> None:
        self.calls = []

    def complete(self, *, pass_name, payload):
        self.calls.append((pass_name, dict(payload)))
        if pass_name == "IMPACT_SKEPTIC":
            return {"verdict": "APPROVE", "issues": []}
        claim = payload["accepted_claim"]
        mapping = next(
            row
            for row in claim["mapping_candidates"]
            if row["primitive_id"] == "memory_price_increase_mentioned"
        )
        question = next(
            row
            for row in payload["question_impact_contracts"]
            if row["question_family_id"] == "asp_pricing_actual"
        )
        subcriterion = next(
            row
            for row in payload["component_subcriteria"]["bottleneck_pricing"]
            if row["question_family_id"] == "asp_pricing_actual"
            and "memory_price_increase_mentioned"
            in row.get("allowed_primitive_ids", ())
        )
        return {
            "impacts": [
                {
                    "mapping_id": mapping["mapping_id"],
                    "primitive_id": mapping["primitive_id"],
                    "question_family_id": question["question_family_id"],
                    "question_contract_hash": question["contract_hash"],
                    "component_id": "bottleneck_pricing",
                    "component_subcriterion_id": subcriterion["subcriterion_id"],
                    "mechanism_scope_match": payload[
                        "mechanism_scope_validation_by_component"
                    ]["bottleneck_pricing"]["scope_match"],
                    "direction": "SUPPORT",
                    "support_type": "DIRECT_ACTUAL",
                    "strength_band": "MODERATE",
                    "completeness_band": "PARTIAL",
                    "causal_distance": "DIRECT",
                    "temporal_scope": "CURRENT",
                    "source_family": "ISSUER_OFFICIAL",
                    "evidence_family_id": "provider-cannot-own-this-id",
                    "confidence": 0.8,
                    "rationale": "검증 원문이 현재 가격 상승을 직접 확인한다.",
                    "unsupported_aspects": ["FCF 전환은 별도 증거가 필요하다."],
                    "counter_claim_ids": [],
                }
            ],
            "unsupported_aspects": ["FCF 전환은 별도 증거가 필요하다."],
            "counter_thesis": [],
            "reasoning_summary": "bounded impact only",
        }


class _TamperingImpactProvider(_ImpactProvider):
    def complete(self, *, pass_name, payload):
        result = super().complete(pass_name=pass_name, payload=payload)
        if pass_name == "IMPACT_PROPOSAL":
            result["impacts"][0]["mapping_id"] = "PROVIDER-INVENTED-MAPPING"
            result["impacts"][0]["source_family"] = "PROVIDER-INVENTED-SOURCE"
            result["impacts"][0]["direction"] = "COUNTER"
        return result


class _WholeDossierImpactProvider:
    provider_name = "UNIT_WHOLE_DOSSIER_IMPACT_PROVIDER"

    def __init__(self, *, tamper_mapping: bool = False) -> None:
        self.calls = []
        self.tamper_mapping = tamper_mapping

    def complete_dossier(self, *, payload):
        self.calls.append(dict(payload))
        impacts = []
        for claim in payload["verified_claim_catalog"]:
            edge = dict(claim["allowed_impact_edges"][0])
            if self.tamper_mapping:
                edge["mapping_id"] = "PROVIDER-INVENTED-MAPPING"
            impacts.append(
                {
                    "claim_id": claim["claim_id"],
                    **edge,
                    "support_type": "PARTIAL_BRIDGE",
                    "strength_band": "MODERATE",
                    "completeness_band": "PARTIAL",
                    "causal_distance": "DIRECT",
                    "confidence": 0.8,
                    "rationale": "검증된 claim과 허용 edge만 연결했다.",
                    "unsupported_aspects": ["더 강한 인과 bridge는 확인되지 않았다."],
                    "counter_claim_ids": [],
                }
            )
        return {
            "impacts": impacts,
            "unsupported_aspects": ["미확인 bridge는 deterministic cap으로 남긴다."],
            "reasoning_summary": "whole dossier bounded pass",
        }


class _JudgeTransport:
    def __init__(self, payload):
        self.payload = payload
        self.calls = []

    def complete(self, **kwargs):
        self.calls.append(kwargs)

        class Response:
            pass

        response = Response()
        response.payload = self.payload
        return response


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
        source_page = verification_root / "source_pages/PROSRC-verified.txt"
        source_page.parent.mkdir(parents=True, exist_ok=True)
        source_page.write_text(
            "검증기업 MEMORY HBM 가격은 2026Q2에 10% 상승했다. " * 20,
            encoding="utf-8",
        )
        dossier_fact = {
            "dossier_fact_id": "PROFACT-verified",
            "statement": "HBM 가격이 10% 상승했다.",
            "direction": "POSITIVE",
            "subject": "검증기업",
            "target_id": self.job.symbol,
            "issuer_scoped": True,
            "business_segment": "MEMORY",
            "product_family": "HBM",
            "economic_mechanism": "PRICING_POWER",
            "predicate": "MEMORY_PRICE_INCREASE_MENTIONED",
            "value": 10,
            "unit": "%",
            "period": "2026Q2",
            "event_date": "2026-08-20",
            "current_status": "CURRENT",
            "candidate_components": ["bottleneck_pricing"],
            "source_url": "https://issuer.example/ir",
            "source_title": "검증기업 IR",
            "source_publisher": "검증기업",
            "published_at": "2026-08-20",
            "supporting_excerpt": "HBM 가격은 2026Q2에 10% 상승했다.",
            "confidence": 0.9,
        }
        dossier = v2_scoring_dossier(
            {
                **self._dossier(),
                "material_facts": [dossier_fact],
                "counterfacts": [],
                "unresolved_gaps": [],
                "source_lineages": [],
            },
            job=self.job,
            selected_archetype_ids=(self.archetype_id,),
        )
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
                    "source_url": "https://issuer.example/ir",
                    "source_id": "PROSRC-verified",
                    "content_hash": canonical_hash({"source": "verified"}),
                    "document_path": "verification/source_pages/PROSRC-verified.txt",
                },
                {
                    "dossier_fact_id": "PROFACT-unverified",
                    "status": "REJECTED_QUOTE_MISMATCH",
                    "compiled_claim_id": None,
                },
            ),
            "claim_fact_links.jsonl": (
                {
                    "claim_id": "C1",
                    "fact_id": self.fact.fact_id,
                    "link_role": "PRIMARY_FACT_CLAIM",
                    "economic_fact_key": "HBM_PRICE_2026Q2",
                },
            ),
        }
        for name, rows in artifact_rows.items():
            (verification_root / name).write_text(
                "".join(canonical_json(row) + "\n" for row in rows),
                encoding="utf-8",
            )
        dossier_id = "PRODOSSIER-" + canonical_hash(
            {"job_id": self.job.job_id, "root": str(root)}
        )[:24]
        dossier_hash = canonical_hash(dossier)
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
                "component_ids": list(CANONICAL_COMPONENT_ORDER),
                "score_authority": False,
                "stage_authority": False,
                "evidence_promoted_count": 0,
            },
            actor="scoring-integration-fixture",
            idempotency_key="scoring-integration-dossier-imported",
        )
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=self.job.state_version,
            to_status=JobStatus.VERIFYING_SOURCES,
            actor="scoring-integration-fixture",
            idempotency_key="scoring-integration-verifying",
        )
        verification_id = "PROVERIFY-" + canonical_hash(
            {"job_id": self.job.job_id, "root": str(root)}
        )[:24]
        verification_hash = canonical_hash(
            {"job_id": self.job.job_id, "fact_ids": [self.fact.fact_id]}
        )
        verification_receipt = {
            "schema_version": "e2r_pro_source_verification_receipt_v1",
            "status": "SOURCE_VERIFICATION_COMPLETE",
            "job_id": self.job.job_id,
            "dossier_id": self.job.dossier_id,
            "verification_id": verification_id,
            "verification_hash": verification_hash,
            "normalized_dossier_hash": canonical_hash(dossier),
            "candidate_fact_count": 2,
            "terminal_fact_count": 2,
            "accepted_fact_candidate_count": 1,
            "compiled_evidence_fact_count": 1,
            "full_document_fetch_count": 1,
            "document_cache_reuse_count": 0,
            "source_document_count": 1,
            "status_counts": {
                "ACCEPTED_CURRENT": 1,
                "REJECTED_QUOTE_MISMATCH": 1,
            },
            "fact_graph_ready": True,
            "query_count": 0,
            "search_count": 0,
            "pro_score_authority": False,
            "pro_stage_authority": False,
        }
        (verification_root / "source_verification_receipt.json").write_text(
            canonical_json(verification_receipt) + "\n",
            encoding="utf-8",
        )
        self.job = self.store.record_source_verification(
            self.job.job_id,
            expected_version=self.job.state_version,
            verification_id=verification_id,
            dossier_id=str(self.job.dossier_id),
            verification_hash=verification_hash,
            receipt=verification_receipt,
            actor="scoring-integration-fixture",
            idempotency_key="scoring-integration-source-verified",
        )
        self.job = ProGapAdjudicationService(self.store).adjudicate_job(
            self.job.job_id,
            job_root=root,
            deterministic_contexts={},
        ).job
        self.assertEqual(self.job.status, JobStatus.COMPONENT_RESEARCH.value)
        saturation_root = root / "saturation"
        saturation_root.mkdir(parents=True, exist_ok=True)
        saturation_root.joinpath("research_saturation_receipt.json").write_text(
            canonical_json(
                passing_research_saturation_receipt(
                    job=self.job,
                    dossier=dossier,
                    selected_archetype_ids=(self.archetype_id,),
                )
            )
            + "\n",
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

    def test_component_bridge_conservatively_normalizes_qualitative_confidence(self) -> None:
        dossier = self._dossier()
        dossier["component_research"]["eps_fcf_explosion"]["confidence"] = (
            "HIGH_ON_REPORTED_ACTUALS_MEDIUM_ON_RUN_RATE"
        )
        dossier["component_research"]["bottleneck_pricing"].update(
            {
                "proposed_score_lower": 0.0,
                "proposed_score_mid": 0.0,
                "proposed_score_upper": 0.0,
            }
        )
        result = ProComponentMemoCompiler().compile(
            dossier=dossier,
            job=self.job,
            selected_archetype_id=self.archetype_id,
            verified_facts=(self.fact,),
            source_verifications=(),
            claim_fact_links=(),
            gap_decisions=(),
            historical_anchors=self.anchors,
        )
        memo = next(
            row for row in result.memos if row.component_id == "eps_fcf_explosion"
        )
        self.assertEqual(memo.confidence, 0.60)

    def test_component_bridge_rejects_unknown_confidence_prose(self) -> None:
        dossier = self._dossier()
        dossier["component_research"]["eps_fcf_explosion"]["confidence"] = (
            "FAIRLY_CERTAIN"
        )
        dossier["component_research"]["bottleneck_pricing"].update(
            {
                "proposed_score_lower": 0.0,
                "proposed_score_mid": 0.0,
                "proposed_score_upper": 0.0,
            }
        )
        with self.assertRaisesRegex(ValueError, "HIGH/MEDIUM/LOW"):
            ProComponentMemoCompiler().compile(
                dossier=dossier,
                job=self.job,
                selected_archetype_id=self.archetype_id,
                verified_facts=(self.fact,),
                source_verifications=(),
                claim_fact_links=(),
                gap_decisions=(),
                historical_anchors=self.anchors,
            )

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

    def test_21_judge_allows_explicit_no_anchor_state(self) -> None:
        class NoAnchorProvider(_EvidenceOnlyProvider):
            def judge(self, request):
                payload = super().judge(request)
                payload["nearest_anchor_ids"] = []
                payload["anchor_comparisons"] = []
                return payload

        component = self._component_result()
        memos = tuple(
            replace(
                memo,
                historical_anchor_ids=(),
                nearest_positive_anchor_ids=(),
                nearest_counter_anchor_ids=(),
            )
            for memo in component.memos
        )
        result = ProEvidenceOnlyJudgeBridge(NoAnchorProvider()).run(
            memos=memos,
            evidence_facts=(self.fact,),
            historical_anchors=(),
            gap_decisions=(),
        )
        self.assertEqual(result.status, "JUDGING_COMPLETE")
        self.assertEqual(len(result.decisions), 21)
        self.assertTrue(
            all(not decision.nearest_anchor_ids for decision in result.decisions)
        )

    def test_21_judge_reuses_durable_response_cache(self) -> None:
        component = self._component_result()
        provider = _EvidenceOnlyProvider()
        cache_root = Path(self.temporary_directory.name) / "judge-cache"
        first = ProEvidenceOnlyJudgeBridge(provider).run(
            memos=component.memos,
            evidence_facts=(self.fact,),
            historical_anchors=self.anchors,
            gap_decisions=(),
            response_cache_root=cache_root,
        )
        second = ProEvidenceOnlyJudgeBridge(provider).run(
            memos=component.memos,
            evidence_facts=(self.fact,),
            historical_anchors=self.anchors,
            gap_decisions=(),
            response_cache_root=cache_root,
        )
        self.assertEqual(first.status, "JUDGING_COMPLETE")
        self.assertEqual(second.status, "JUDGING_COMPLETE")
        self.assertEqual(len(provider.requests), 21)
        self.assertEqual(second.receipt_payload["provider_call_count"], 0)
        self.assertEqual(
            second.receipt_payload["provider_response_reuse_count"], 21
        )

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

    def test_judge_rejects_points_above_component_contract(self) -> None:
        class OverRangeProvider(_EvidenceOnlyProvider):
            def judge(self, request):
                payload = super().judge(request)
                maximum = float(request["component_memo"]["component_max_points"])
                payload["proposed_points"] = maximum + 1.0
                payload["allowed_range"] = [0.0, maximum + 1.0]
                return payload

        component = self._component_result()
        result = ProEvidenceOnlyJudgeBridge(OverRangeProvider()).run(
            memos=component.memos,
            evidence_facts=(self.fact,),
            historical_anchors=self.anchors,
            gap_decisions=(),
        )
        self.assertEqual(result.status, "JUDGING_PROVIDER_PENDING")
        self.assertIn("JUDGE_PROVIDER_ERROR", result.pending_reasons[0])

    def test_codex_judge_provider_forwards_only_structured_request(self) -> None:
        payload = {
            "proposed_points": 1.0,
            "allowed_range": [0.0, 2.0],
            "rationale": "verified facts only",
            "support_fact_ids": [],
            "counter_fact_ids": [],
            "nearest_anchor_ids": [],
            "anchor_comparisons": [],
            "disagreements": [],
            "why_not_higher": "missing bridge",
            "why_not_lower": "bounded evidence",
        }
        transport = _JudgeTransport(payload)
        provider = CodexEvidenceOnlyJudgeProvider(transport)
        result = provider.judge(
            {
                "mode": "EVIDENCE_ONLY_NO_SEARCH",
                "role": "ANALYST",
                "component_memo": {"component_max_points": 10.0},
            }
        )
        self.assertEqual(result, payload)
        self.assertEqual(len(transport.calls), 1)
        prompt = transport.calls[0]["prompt"]
        self.assertIn("Never browse", prompt)
        self.assertNotIn("canonical_stage", prompt)
        self.assertNotIn("uniqueItems", str(transport.calls[0]["output_schema"]))

    def test_codex_whole_dossier_provider_excludes_score_and_stage_authority(self) -> None:
        transport = _JudgeTransport(
            {
                "impacts": [],
                "unsupported_aspects": ["검증 claim이 없으면 impact를 만들지 않는다."],
                "reasoning_summary": "bounded evidence only",
            }
        )
        provider = CodexDossierImpactProvider(transport)
        provider.complete_dossier(
            payload={
                "mode": "EVIDENCE_ONLY_NO_SEARCH",
                "verified_claim_catalog": [],
            }
        )
        self.assertEqual(len(transport.calls), 1)
        call = transport.calls[0]
        impact_properties = call["output_schema"]["properties"]["impacts"][
            "items"
        ]["properties"]
        self.assertNotIn("score", impact_properties)
        self.assertNotIn("stage", impact_properties)
        self.assertNotIn("direction", impact_properties)
        self.assertNotIn("source_family", impact_properties)
        self.assertNotIn("uniqueItems", str(call["output_schema"]))
        self.assertIn("Do not browse", call["prompt"])
        self.assertIn("deterministic pipeline", call["prompt"])

    def test_operational_impact_compiler_uses_one_whole_dossier_call(self) -> None:
        runtime_root = Path(self.temporary_directory.name) / "batch-impact-runtime"
        job_root = runtime_root / "jobs" / self.job.job_id
        self._prepare_durable_component_job(job_root)
        provider = _WholeDossierImpactProvider()
        dossier = {
            **self._dossier(),
            "material_facts": [
                {
                    "dossier_fact_id": "PROFACT-verified",
                    "statement": "HBM 가격이 10% 상승했다.",
                    "supporting_excerpt": "HBM 가격은 2026Q2에 10% 상승했다.",
                    "source_url": "https://issuer.example/ir",
                    "source_publisher": "검증기업",
                    "published_at": "2026-08-20",
                    "event_date": "2026-08-20",
                }
            ],
            "counterfacts": [],
        }
        result = ProValidatedImpactCompiler(
            provider,
            repo_root=Path(__file__).resolve().parents[1],
        ).compile(
            job=self.store.get_job(self.job.job_id),
            dossier=dossier,
            job_root=job_root,
            selected_archetype_id=self.archetype_id,
        )
        self.assertEqual(len(provider.calls), 1)
        self.assertEqual(result.provider_call_count, 1)
        self.assertEqual(len(result.impacts), 1)
        self.assertEqual(
            result.receipt["provider_name"],
            "UNIT_WHOLE_DOSSIER_IMPACT_PROVIDER",
        )
        request = provider.calls[0]
        self.assertEqual(request["mode"], "EVIDENCE_ONLY_NO_SEARCH")
        self.assertEqual(len(request["verified_claim_catalog"]), 1)
        self.assertNotIn("score", request["authority_boundary"])
        rerun = ProValidatedImpactCompiler(
            provider,
            repo_root=Path(__file__).resolve().parents[1],
        ).compile(
            job=self.store.get_job(self.job.job_id),
            dossier=dossier,
            job_root=job_root,
            selected_archetype_id=self.archetype_id,
        )
        self.assertEqual(len(provider.calls), 1)
        self.assertEqual(rerun.provider_call_count, 0)

    def test_whole_dossier_unknown_mapping_is_rejected_before_scoring(self) -> None:
        runtime_root = Path(self.temporary_directory.name) / "batch-tamper-runtime"
        job_root = runtime_root / "jobs" / self.job.job_id
        self._prepare_durable_component_job(job_root)
        provider = _WholeDossierImpactProvider(tamper_mapping=True)
        result = ProValidatedImpactCompiler(
            provider,
            repo_root=Path(__file__).resolve().parents[1],
        ).compile(
            job=self.store.get_job(self.job.job_id),
            dossier={
                **self._dossier(),
                "material_facts": [
                    {
                        "dossier_fact_id": "PROFACT-verified",
                        "statement": "HBM 가격이 10% 상승했다.",
                        "supporting_excerpt": "HBM 가격은 2026Q2에 10% 상승했다.",
                        "source_url": "https://issuer.example/ir",
                        "source_publisher": "검증기업",
                        "published_at": "2026-08-20",
                        "event_date": "2026-08-20",
                    }
                ],
                "counterfacts": [],
            },
            job_root=job_root,
            selected_archetype_id=self.archetype_id,
        )
        self.assertEqual(len(provider.calls), 2)
        self.assertEqual(result.provider_call_count, 2)
        self.assertEqual(result.impacts, ())
        self.assertTrue(
            any(
                reason.startswith("WHOLE_DOSSIER_IMPACT_INVALID_ROWS")
                for reason in result.pending_reasons
            )
        )

    def test_operational_impact_compiler_stays_pending_without_seven_components(self) -> None:
        runtime_root = Path(self.temporary_directory.name) / "impact-runtime"
        job_root = runtime_root / "jobs" / self.job.job_id
        self._prepare_durable_component_job(job_root)
        provider = _ImpactProvider()
        result = ProValidatedImpactCompiler(
            provider,
            repo_root=Path(__file__).resolve().parents[1],
        ).compile(
            job=self.store.get_job(self.job.job_id),
            dossier={
                **self._dossier(),
                "material_facts": [
                    {
                        "dossier_fact_id": "PROFACT-verified",
                        "statement": "HBM 가격이 10% 상승했다.",
                        "supporting_excerpt": "HBM 가격은 2026Q2에 10% 상승했다.",
                        "source_url": "https://issuer.example/ir",
                        "source_publisher": "검증기업",
                        "published_at": "2026-08-20",
                        "event_date": "2026-08-20",
                    }
                ],
                "counterfacts": [],
            },
            job_root=job_root,
            selected_archetype_id=self.archetype_id,
        )
        self.assertEqual(
            result.status, "PRO_VALIDATED_IMPACT_COMPILATION_PENDING"
        )
        self.assertEqual(len(result.impacts), 1)
        self.assertFalse(result.ready_for_judging)
        self.assertEqual([row[0] for row in provider.calls], [
            "IMPACT_PROPOSAL",
            "IMPACT_SKEPTIC",
        ])
        self.assertIn(
            "COMPONENT_IMPACT_COVERAGE_PENDING",
            result.pending_reasons[0],
        )

    def test_operational_impact_compiler_rejects_provider_owned_lineage(self) -> None:
        runtime_root = Path(self.temporary_directory.name) / "tampered-impact-runtime"
        job_root = runtime_root / "jobs" / self.job.job_id
        self._prepare_durable_component_job(job_root)
        result = ProValidatedImpactCompiler(
            _TamperingImpactProvider(),
            repo_root=Path(__file__).resolve().parents[1],
        ).compile(
            job=self.store.get_job(self.job.job_id),
            dossier={
                **self._dossier(),
                "material_facts": [
                    {
                        "dossier_fact_id": "PROFACT-verified",
                        "statement": "HBM 가격이 10% 상승했다.",
                        "supporting_excerpt": "HBM 가격은 2026Q2에 10% 상승했다.",
                        "source_url": "https://issuer.example/ir",
                        "source_publisher": "검증기업",
                        "published_at": "2026-08-20",
                        "event_date": "2026-08-20",
                    }
                ],
                "counterfacts": [],
            },
            job_root=job_root,
            selected_archetype_id=self.archetype_id,
        )
        self.assertEqual(
            result.status,
            "PRO_VALIDATED_IMPACT_COMPILATION_PENDING",
        )
        self.assertEqual(result.impacts, ())
        self.assertTrue(
            any("IMPACT_" in reason for reason in result.pending_reasons)
        )

    def test_post_import_default_waits_at_judge_provider_without_zero_score(self) -> None:
        runtime_root = Path(self.temporary_directory.name) / "runtime"
        job_root = runtime_root / "jobs" / self.job.job_id
        self._prepare_durable_component_job(job_root)

        def pending_inputs(job, _dossier, _root):
            return ProPostImportScoringInputs(
                selected_archetype_id=self.archetype_id,
                judge_provider=None,
                historical_anchors=self.anchors,
                terminal_evidence={
                    component_id: {"status": "PROVIDER_PENDING"}
                    for component_id in CANONICAL_COMPONENT_ORDER
                },
            )

        coordinator = ProFirstPostImportCoordinator(
            self.store,
            runtime_root=runtime_root,
            scoring_input_provider=pending_inputs,
        )
        advance = coordinator.advance_once(self.job.job_id)
        current = self.store.get_job(self.job.job_id)
        self.assertEqual(advance.before_status, JobStatus.COMPONENT_RESEARCH.value)
        self.assertEqual(advance.after_status, JobStatus.JUDGING.value)
        self.assertEqual(advance.wait_reason, "JUDGE_PROVIDER_UNAVAILABLE")
        self.assertEqual(current.status, JobStatus.JUDGING.value)
        self.assertIsNone(self.store.get_score_receipt(self.job.job_id))
        self.assertIsNone(self.store.get_stagecourt_receipt(self.job.job_id))

    def test_post_import_injected_validated_inputs_publish_final(self) -> None:
        runtime_root = Path(self.temporary_directory.name) / "runtime-final"
        job_root = runtime_root / "jobs" / self.job.job_id
        self._prepare_durable_component_job(job_root)
        provider = _EvidenceOnlyProvider()

        def complete_inputs(job, _dossier, _root):
            return ProPostImportScoringInputs(
                selected_archetype_id=self.archetype_id,
                judge_provider=provider,
                historical_anchors=self.anchors,
                validated_impacts=(supported_impact(),),
                terminal_evidence=self._terminal_evidence(),
                validity_evidence=passing_full_score_validity_evidence(
                    "PRO-FIRST-POST-IMPORT-FINAL"
                ),
            )

        coordinator = ProFirstPostImportCoordinator(
            self.store,
            runtime_root=runtime_root,
            scoring_input_provider=complete_inputs,
        )
        advance = coordinator.advance_once(self.job.job_id)
        current = self.store.get_job(self.job.job_id)
        publication = self.store.get_publication(self.job.job_id)
        self.assertEqual(current.status, JobStatus.FINAL.value)
        self.assertTrue(advance.published)
        self.assertEqual(advance.action, "SCORE_STAGECOURT_PUBLISH")
        self.assertIsNotNone(publication)
        self.assertEqual(len(provider.requests), 21)
        self.assertEqual(publication["result"]["component_coverage"], "7/7")
        self.assertEqual(publication["result"]["judge_coverage"], "21/21")

    def test_conservative_gap_context_ignores_proposed_authority_flags(self) -> None:
        gap = {
            "dossier_gap_id": "PROGAP-POST-IMPORT",
            "archetype_id": self.archetype_id,
            "affected_component_ids": ["earnings_visibility"],
            "required_source_families": ["CUSTOMER_OFFICIAL"],
            "proposed_gap_class": "HARD_BREAK_GAP",
            "proposed_could_change_hard_break": True,
        }
        context = compile_conservative_gap_contexts(
            self.job,
            {"unresolved_gaps": [gap]},
            Path(self.temporary_directory.name),
        )["PROGAP-POST-IMPORT"]
        self.assertFalse(context.direct_contradiction_or_hard_break_unresolved)
        self.assertIsNone(context.deterministic_lower_stage)
        self.assertIsNone(context.deterministic_upper_stage)
        self.assertEqual(context.component_lower_delta, {"earnings_visibility": 0.0})
        self.assertGreater(context.component_upper_delta["earnings_visibility"], 0.0)
        self.assertTrue(context.executable_new_source_route_signatures)

    def test_general_web_gap_does_not_claim_unproved_official_first_attempt(self) -> None:
        gap = {
            "dossier_gap_id": "PROGAP-GENERAL-WEB",
            "archetype_id": self.archetype_id,
            "affected_component_ids": ["information_confidence"],
            "required_source_families": ["GENERAL_WEB_DISCOVERY"],
        }
        context = compile_conservative_gap_contexts(
            self.job,
            {"unresolved_gaps": [gap]},
            Path(self.temporary_directory.name),
        )["PROGAP-GENERAL-WEB"]
        self.assertFalse(context.official_first_attempted)
        self.assertEqual(context.official_gap_reasons, ())

    def test_external_official_family_records_connector_gap_before_web(self) -> None:
        gap = {
            "dossier_gap_id": "PROGAP-PEER-OFFICIAL",
            "archetype_id": self.archetype_id,
            "affected_component_ids": ["earnings_visibility"],
            "required_source_families": ["PEER_CAPACITY_GUIDANCE"],
        }
        context = compile_conservative_gap_contexts(
            self.job,
            {"unresolved_gaps": [gap]},
            Path(self.temporary_directory.name),
        )["PROGAP-PEER-OFFICIAL"]
        self.assertFalse(context.official_first_attempted)
        self.assertEqual(
            context.official_gap_reasons,
            (
                "NO_DIRECT_CONNECTOR_FOR_REQUESTED_OFFICIAL_FAMILY:"
                "PEER_CAPACITY_GUIDANCE",
            ),
        )

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

    def test_partial_diagnostic_score_not_published(self) -> None:
        root = Path(self.temporary_directory.name) / "diagnostic-score-job"
        self._prepare_durable_component_job(root)
        invalid_validity = replace(
            passing_full_score_validity_evidence("P7-DIAGNOSTIC-PENDING"),
            pending_state_count=1,
        )
        run = ProScoringPipelineService(self.store).run_job(
            self.job.job_id,
            job_root=root,
            selected_archetype_id=self.archetype_id,
            judge_provider=_EvidenceOnlyProvider(),
            historical_anchors=self.anchors,
            validated_impacts=(supported_impact(),),
            terminal_evidence=self._terminal_evidence(),
            validity_evidence=invalid_validity,
        )
        diagnostic = run.research_incomplete_result or {}
        self.assertEqual(run.job.status, JobStatus.SCORING.value)
        self.assertFalse(diagnostic["score_valid"])
        self.assertIsNone(diagnostic["full_thesis_score"])
        self.assertEqual(
            diagnostic["publication_status"],
            "WITHHELD_PENDING_RESEARCH_SATURATION",
        )
        self.assertIsNone(self.store.get_score_receipt(self.job.job_id))
        self.assertIsNone(self.store.get_stagecourt_receipt(self.job.job_id))
        self.assertIsNone(self.store.get_publication(self.job.job_id))

    def test_stage0_final_not_used_for_research_incomplete(self) -> None:
        root = Path(self.temporary_directory.name) / "missing-saturation-stage-job"
        self._prepare_durable_component_job(root)
        (root / "saturation/research_saturation_receipt.json").unlink()
        run = self._run_durable_pipeline(root, _EvidenceOnlyProvider())
        diagnostic = run.research_incomplete_result or {}
        self.assertEqual(run.job.status, JobStatus.COMPONENT_RESEARCH.value)
        self.assertEqual(diagnostic["stage_status"], "RESEARCH_INCOMPLETE")
        self.assertIsNone(diagnostic["canonical_stage"])
        self.assertNotEqual(diagnostic["stage_status"], "FINAL")

    def test_full_thesis_requires_saturation(self) -> None:
        root = Path(self.temporary_directory.name) / "missing-saturation-gate-job"
        self._prepare_durable_component_job(root)
        (root / "saturation/research_saturation_receipt.json").unlink()
        run = self._run_durable_pipeline(root, _EvidenceOnlyProvider())
        self.assertFalse(run.research_eligibility.research_saturation_valid)
        self.assertIsNone(run.component_result)
        self.assertFalse((root / "scoring/component_memos.jsonl").exists())
        self.assertIsNone(run.score_receipt)
        self.assertIsNone(run.stagecourt_receipt)

    def test_pro_score_stage_fields_ignored(self) -> None:
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
        self.assertNotEqual(scoring.score.full_e2r_score, 99.0)
        self.assertNotEqual(stage.decision.canonical_stage, "5")
        self.assertTrue(scoring.receipt_payload["pro_score_ignored"])
        self.assertTrue(stage.receipt_payload["pro_stage_ignored"])

    def test_existing_component_scorer_used(self) -> None:
        receipt = self._score_result().receipt_payload
        self.assertEqual(
            receipt["scorer_class"],
            "ResearchCalibratedComponentScorer",
        )
        self.assertEqual(receipt["new_score_engine_count"], 0)

    def test_existing_atomic_stagecourt_used(self) -> None:
        stage = ProAtomicStageCourtBridge().decide(
            target_id=self.job.symbol,
            as_of_date=self.job.as_of_date,
            selected_archetype_id=self.archetype_id,
            score_result=self._score_result(),
            accepted_claim_ids=("C1",),
            evidence_facts=(self.fact,),
        )
        self.assertEqual(stage.receipt_payload["stagecourt_class"], "AtomicStageCourtV2")
        self.assertEqual(stage.receipt_payload["new_stage_engine_count"], 0)

    def test_nonzero_score_requires_claim_lineage(self) -> None:
        scoring = self._score_result()
        self.assertGreater(scoring.score.full_e2r_score, 0.0)
        self.assertEqual(scoring.impact_fact_lineage, {"C1": (self.fact.fact_id,)})
        with self.assertRaisesRegex(ValueError, "lacks fact lineage"):
            self._score_result(
                claim_fact_lineage={"C1": ("EFACT-not-in-memo",)}
            )

    def test_tracked_scoring_publication_gate_audit_matches_contract(self) -> None:
        root = Path(__file__).resolve().parents[1]
        tracked = json.loads(
            (
                root
                / "docs/operational/e2r_pro_first_v2/scoring_publication_gate_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(
            canonical_json(tracked),
            canonical_json(audit_scoring_publication_gate(root)),
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
        dossier = v2_scoring_dossier(
            self._dossier(),
            job=self.job,
            selected_archetype_ids=(self.archetype_id,),
        )
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
        (delta_root / "saturation/research_saturation_receipt.json").write_text(
            canonical_json(
                passing_research_saturation_receipt(
                    job=self.job,
                    dossier=dossier,
                    selected_archetype_ids=(self.archetype_id,),
                )
            )
            + "\n",
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
