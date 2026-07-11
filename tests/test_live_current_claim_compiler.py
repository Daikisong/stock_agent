from __future__ import annotations

import hashlib
import json
import unittest
from datetime import date
from pathlib import Path

from e2r.agentic import (
    AgenticEvidenceProviderBundle,
    AdjudicationProposal,
    ClaimExtractionOutput,
    Directness,
    FakeClaimExtractorProvider,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingOutput,
    PrimitiveMappingProposal,
    RawAssertion,
    RelationToTarget,
    SemanticStatus,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
)
from e2r.research_brain.runtime.live_materialization import (
    CurrentClaimCompiler,
    CurrentClaimCompilerConfig,
)


class LiveCurrentClaimCompilerTest(unittest.TestCase):
    def test_live_operational_audit_rejects_unrelated_official_claims(self) -> None:
        path = (
            Path(__file__).resolve().parents[1]
            / "docs"
            / "operational"
            / "e2r_live_current_claim_audit.json"
        )
        audit = json.loads(path.read_text(encoding="utf-8"))

        self.assertEqual(audit["status"], "PHASE_28_ACCEPTED")
        self.assertGreater(audit["contract_blind_raw_assertion_count"], 0)
        self.assertGreater(audit["adjudicated_claim_count"], 0)
        self.assertEqual(audit["accepted_current_claim_count"], 0)
        self.assertEqual(sum(audit["critical_counts"].values()), 0)
        self.assertFalse(audit["safety"]["official_document_auto_accepted"])

    def test_irrelevant_full_document_keeps_original_question_open(self) -> None:
        result = CurrentClaimCompiler().compile(
            CurrentClaimCompilerConfig(
                as_of_date="2026-07-10",
                max_documents=1,
                test_mode=True,
            ),
            evidence_documents=(_document(),),
            question_source_tasks=(_task(),),
            provider_bundle=AgenticEvidenceProviderBundle(
                extractor=FakeClaimExtractorProvider(ClaimExtractionOutput()),
                adjudicator=_NeverAdjudicator(),
                mapper=_NeverMapper(),
            ),
        )

        self.assertEqual(result.status, "CURRENT_CLAIM_COMPILER_PASS")
        self.assertFalse(result.accepted_current_claims)
        self.assertFalse(result.daily_claim_provenance)
        self.assertEqual(
            result.source_task_satisfaction[0].status,
            "NO_RELEVANT_CLAIM",
        )
        self.assertTrue(result.source_task_satisfaction[0].original_gap_open)
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_document_content_hash_mismatch_is_rejected(self) -> None:
        document = _document()
        document["content_hash"] = "0" * 64

        with self.assertRaisesRegex(ValueError, "content hash mismatch"):
            CurrentClaimCompiler().compile(
                CurrentClaimCompilerConfig(
                    as_of_date="2026-07-10",
                    max_documents=1,
                    test_mode=True,
                ),
                evidence_documents=(document,),
                question_source_tasks=(_task(),),
                provider_bundle=AgenticEvidenceProviderBundle(
                    extractor=FakeClaimExtractorProvider(ClaimExtractionOutput()),
                    adjudicator=_NeverAdjudicator(),
                    mapper=_NeverMapper(),
                ),
            )

    def test_multiple_targets_do_not_inherit_last_compile_job_target(self) -> None:
        first = _document(target_id="000001", target_name="첫회사", task_id="TASK-1")
        second = _document(target_id="000002", target_name="둘회사", task_id="TASK-2")
        result = CurrentClaimCompiler().compile(
            CurrentClaimCompilerConfig(
                as_of_date="2026-07-10",
                max_documents=2,
                test_mode=True,
            ),
            evidence_documents=(first, second),
            question_source_tasks=(
                _task(target_id="000001", company_name="첫회사", task_id="TASK-1"),
                _task(target_id="000002", company_name="둘회사", task_id="TASK-2"),
            ),
            provider_bundle=AgenticEvidenceProviderBundle(
                extractor=_TargetEchoExtractor(),
                adjudicator=_TargetEchoAdjudicator(),
                mapper=_AcceptFirstPrimitiveMapper(),
            ),
        )

        self.assertEqual(
            {row["target_id"] for row in result.accepted_current_claims},
            {"000001", "000002"},
        )
        self.assertEqual(
            {row.target_id for row in result.daily_claim_provenance},
            {"000001", "000002"},
        )

    def test_dossier_optional_primitive_is_explicit_and_unknown_is_rejected(self) -> None:
        bundle = AgenticEvidenceProviderBundle(
            extractor=FakeClaimExtractorProvider(ClaimExtractionOutput()),
            adjudicator=_NeverAdjudicator(),
            mapper=_NeverMapper(),
        )
        valid = CurrentClaimCompiler().compile(
            CurrentClaimCompilerConfig(
                as_of_date="2026-07-10",
                max_documents=1,
                test_mode=True,
                additional_primitive_ids=("shipment_or_revenue_mix",),
            ),
            evidence_documents=(_document(),),
            question_source_tasks=(_task(),),
            provider_bundle=bundle,
        )
        self.assertEqual(valid.status, "CURRENT_CLAIM_COMPILER_PASS")
        with self.assertRaisesRegex(ValueError, "outside EvidenceContract"):
            CurrentClaimCompiler().compile(
                CurrentClaimCompilerConfig(
                    as_of_date="2026-07-10",
                    max_documents=1,
                    test_mode=True,
                    additional_primitive_ids=("invented_dossier_primitive",),
                ),
                evidence_documents=(_document(),),
                question_source_tasks=(_task(),),
                provider_bundle=bundle,
            )


class _NeverAdjudicator:
    def adjudicate(self, inputs):
        raise AssertionError("empty extraction must not adjudicate")


class _NeverMapper:
    def map(self, inputs):
        raise AssertionError("empty extraction must not map")


class _TargetEchoExtractor:
    def extract(self, inputs):
        return ClaimExtractionOutput(
            (
                RawAssertion(
                    raw_assertion_id=f"RA-{inputs.target_entity_id}",
                    anchor_id=inputs.anchors[0].anchor_id,
                    subject_text=inputs.target_names[0],
                    predicate="reported HBM customer allocation",
                    object_text="current committed volume",
                    polarity_proposal=Polarity.POSITIVE,
                    event_date_text="2026-06-01",
                    exact_quote=inputs.anchors[0].exact_text,
                ),
            )
        )


class _TargetEchoAdjudicator:
    def adjudicate(self, inputs):
        return AdjudicationProposal(
            subject_entity_id=inputs.target_entity_id,
            relation_to_target=RelationToTarget.SELF,
            directness=Directness.DIRECT,
            target_scope_status=TargetScopeStatus.DIRECT,
            polarity=Polarity.POSITIVE,
            temporal_status=TemporalStatus.CURRENT,
            semantic_status=SemanticStatus.PASS_,
            investigation_status=InvestigationStatus.COMPLETE,
            event_date=date(2026, 6, 1),
        )


class _AcceptFirstPrimitiveMapper:
    def map(self, inputs):
        return PrimitiveMappingOutput(
            (
                PrimitiveMappingProposal.build(
                    claim_id=inputs.claim.claim_id,
                    archetype_id=inputs.contract.archetype_id,
                    primitive_id=inputs.canonical_primitive_ids[0],
                    support_direction=SupportDirection.SUPPORT,
                    mapping_status=MappingStatus.ACCEPTED,
                    rationale="Direct current target claim supports the primitive.",
                ),
            )
        )


def _document(
    *,
    target_id: str = "000001",
    target_name: str = "테스트회사",
    task_id: str = "QSOURCE-TEST",
) -> dict:
    text = (
        f"{target_name}({target_id})는 2026년 6월 1일 자기주식 취득 결정을 공시했다. "
        "이 문서는 고객 HBM 배정, 제품 세대, 생산능력 또는 계약 기간을 설명하지 않는다. "
        "따라서 별도의 공식 문서 확인이 필요하다."
    )
    return {
        "document_id": "DOC-" + hashlib.sha256(text.encode("utf-8")).hexdigest()[:20],
        "target_id": target_id,
        "target_name": target_name,
        "source_task_ids": [task_id],
        "source_class": "DART",
        "provider_name": "OpenDART",
        "canonical_url": "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=1",
        "official_document_id": "opendart:disclosure:1",
        "published_at": "2026-06-01",
        "available_at": "2026-06-01",
        "fetched_at": "2026-07-10T09:00:00Z",
        "content_hash": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "content_text": text,
        "structured_payload": {},
        "source_lineage_id": "REQ-TEST",
    }


def _task(
    *,
    target_id: str = "000001",
    company_name: str = "테스트회사",
    task_id: str = "QSOURCE-TEST",
) -> dict:
    return {
        "task_id": task_id,
        "target_id": target_id,
        "company_name": company_name,
        "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        "primitive_id": "customer_preorder_or_allocation",
        "recipe_id": "ERECIPE-TEST",
    }


if __name__ == "__main__":
    unittest.main()
