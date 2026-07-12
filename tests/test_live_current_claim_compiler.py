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
        with self.assertRaisesRegex(ValueError, "bounded by 48"):
            CurrentClaimCompilerConfig(
                as_of_date="2026-07-10",
                max_documents=1,
                max_raw_assertions_per_document=49,
                test_mode=True,
            )

    def test_large_filing_builds_bounded_anchors_around_llm_query_focus(self) -> None:
        document = _document()
        focused = "테스트회사의 HBM4 고객 물량 배정과 매출 비중이 확대됐다."
        text = ("정기보고서 일반 표와 주석입니다.\n" * 3_000) + focused
        document.update(
            {
                "document_id": "DOC-" + hashlib.sha256(text.encode()).hexdigest()[:20],
                "content_hash": hashlib.sha256(text.encode()).hexdigest(),
                "content_text": text,
            }
        )
        task = _task()
        task.update(
            {
                "question_to_answer": "Is HBM customer allocation and revenue mix visible?",
                "query_intent": {
                    "literal_queries": ["테스트회사 HBM4 고객 물량 배정 매출 비중 원문"]
                },
            }
        )
        extractor = FakeClaimExtractorProvider(ClaimExtractionOutput())

        CurrentClaimCompiler().compile(
            CurrentClaimCompilerConfig(
                as_of_date="2026-07-10",
                max_documents=1,
                test_mode=True,
            ),
            evidence_documents=(document,),
            question_source_tasks=(task,),
            provider_bundle=AgenticEvidenceProviderBundle(
                extractor=extractor,
                adjudicator=_NeverAdjudicator(),
                mapper=_NeverMapper(),
            ),
        )

        call = extractor.calls[0]
        self.assertIn("hbm4", call.retrieval_focus_terms)
        self.assertTrue(any(focused in anchor.exact_text for anchor in call.anchors))
        self.assertTrue(all(len(anchor.exact_text) <= 2_100 for anchor in call.anchors))

    def test_distinct_llm_question_focuses_use_bounded_multipass_extraction(self) -> None:
        document = _document(task_id="TASK-HBM")
        text = (
            "테스트회사는 HBM 수요가 견조하지만 공급은 제한적이라고 밝혔다.\n"
            + ("일반 공시 표입니다.\n" * 300)
            + "테스트회사의 잉여현금흐름 FCF는 설비투자 이후에도 개선됐다."
        )
        document.update(
            {
                "document_id": "DOC-" + hashlib.sha256(text.encode()).hexdigest()[:20],
                "content_hash": hashlib.sha256(text.encode()).hexdigest(),
                "content_text": text,
                "source_task_ids": ["TASK-HBM", "TASK-FCF"],
            }
        )
        hbm_task = _task(task_id="TASK-HBM")
        hbm_task.update(
            {
                "question_to_answer": "HBM 수요와 제한된 공급은 무엇인가?",
                "query_intent": {"literal_queries": ["테스트회사 HBM 제한된 공급"]},
            }
        )
        fcf_task = _task(task_id="TASK-FCF")
        fcf_task.update(
            {
                "question_to_answer": "FCF 개선은 무엇인가?",
                "query_intent": {"literal_queries": ["테스트회사 잉여현금흐름 FCF 개선"]},
            }
        )
        extractor = _FocusEchoExtractor()

        result = CurrentClaimCompiler().compile(
            CurrentClaimCompilerConfig(
                as_of_date="2026-07-10",
                max_documents=1,
                max_raw_assertions_per_document=4,
                max_extraction_passes_per_document=4,
                test_mode=True,
            ),
            evidence_documents=(document,),
            question_source_tasks=(hbm_task, fcf_task),
            provider_bundle=AgenticEvidenceProviderBundle(
                extractor=extractor,
                adjudicator=_TargetEchoAdjudicator(),
                mapper=_AcceptFirstPrimitiveMapper(),
            ),
        )

        self.assertEqual(len(extractor.calls), 2)
        self.assertEqual(len(result.raw_assertions), 2)
        self.assertEqual(result.audit["extraction_pass_count"], 2)
        self.assertEqual(result.audit["extracted_raw_assertion_count"], 2)
        self.assertEqual(len({row["raw_assertion_id"] for row in result.raw_assertions}), 2)
        self.assertTrue(any("hbm" in call.retrieval_focus_terms for call in extractor.calls))
        self.assertTrue(any("fcf" in call.retrieval_focus_terms for call in extractor.calls))

    def test_multipass_budget_reserves_a_candidate_for_each_llm_question(self) -> None:
        document = _document(task_id="TASK-HBM")
        text = (
            "테스트회사는 HBM 가격과 제한된 공급을 공시했다.\n"
            + ("일반 표입니다.\n" * 100)
            + "테스트회사의 FCF는 전년보다 개선됐다."
        )
        document.update(
            {
                "document_id": "DOC-" + hashlib.sha256(text.encode()).hexdigest()[:20],
                "content_hash": hashlib.sha256(text.encode()).hexdigest(),
                "content_text": text,
                "source_task_ids": ["TASK-HBM", "TASK-FCF"],
            }
        )
        hbm_task = _task(task_id="TASK-HBM")
        hbm_task["query_intent"] = {"literal_queries": ["테스트회사 HBM 가격 공급"]}
        fcf_task = _task(task_id="TASK-FCF")
        fcf_task["query_intent"] = {"literal_queries": ["테스트회사 FCF 개선"]}

        result = CurrentClaimCompiler().compile(
            CurrentClaimCompilerConfig(
                as_of_date="2026-07-10",
                max_documents=1,
                max_raw_assertions_per_document=2,
                max_extraction_passes_per_document=2,
                test_mode=True,
            ),
            evidence_documents=(document,),
            question_source_tasks=(hbm_task, fcf_task),
            provider_bundle=AgenticEvidenceProviderBundle(
                extractor=_CrowdingExtractor(),
                adjudicator=_TargetEchoAdjudicator(),
                mapper=_AcceptFirstPrimitiveMapper(),
            ),
        )

        predicates = {row["predicate"] for row in result.raw_assertions}
        self.assertEqual(len(result.raw_assertions), 2)
        self.assertIn("reported improved FCF", predicates)

    def test_limited_supply_wording_routes_to_capacity_constraint_contract(self) -> None:
        document = _document()
        text = "테스트회사는 견조한 수요 대비 제한된 공급 환경이 지속됐다고 밝혔다."
        document.update(
            {
                "document_id": "DOC-" + hashlib.sha256(text.encode()).hexdigest()[:20],
                "content_hash": hashlib.sha256(text.encode()).hexdigest(),
                "content_text": text,
            }
        )
        task = _task()
        task["primitive_id"] = "hbm_capacity_constraint"

        result = CurrentClaimCompiler().compile(
            CurrentClaimCompilerConfig(
                as_of_date="2026-07-10",
                max_documents=1,
                mapper_self_consistency_rounds=1,
                test_mode=True,
            ),
            evidence_documents=(document,),
            question_source_tasks=(task,),
            provider_bundle=AgenticEvidenceProviderBundle(
                extractor=_LimitedSupplyExtractor(),
                adjudicator=_TargetEchoAdjudicator(),
                mapper=_CapacityCandidateMapper(),
            ),
        )

        accepted = [
            row
            for row in result.primitive_mappings
            if row.get("accepted_by_evidence_os") is True
        ]
        self.assertEqual(
            [row["primitive_id"] for row in accepted],
            ["hbm_capacity_constraint"],
        )

    def test_korean_mass_production_shipment_routes_to_shipment_primitive(self) -> None:
        document = _document()
        text = "테스트회사는 세계 최초 업계 최고 성능의 HBM4 양산 출하를 완료했다."
        document.update(
            {
                "document_id": "DOC-" + hashlib.sha256(text.encode()).hexdigest()[:20],
                "content_hash": hashlib.sha256(text.encode()).hexdigest(),
                "content_text": text,
            }
        )
        task = _task()
        task["primitive_id"] = "shipment_or_revenue_mix"

        result = CurrentClaimCompiler().compile(
            CurrentClaimCompilerConfig(
                as_of_date="2026-07-10",
                max_documents=1,
                mapper_self_consistency_rounds=1,
                test_mode=True,
                additional_primitive_ids=("shipment_or_revenue_mix",),
            ),
            evidence_documents=(document,),
            question_source_tasks=(task,),
            provider_bundle=AgenticEvidenceProviderBundle(
                extractor=_MassProductionShipmentExtractor(),
                adjudicator=_TargetEchoAdjudicator(),
                mapper=_ShipmentCandidateMapper(),
            ),
        )

        accepted = [
            row
            for row in result.primitive_mappings
            if row.get("accepted_by_evidence_os") is True
        ]
        self.assertEqual(
            [row["primitive_id"] for row in accepted],
            ["shipment_or_revenue_mix"],
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


class _FocusEchoExtractor:
    def __init__(self) -> None:
        self.calls = []

    def extract(self, inputs):
        self.calls.append(inputs)
        is_hbm = "hbm" in inputs.retrieval_focus_terms
        marker = "HBM" if is_hbm else "FCF"
        anchor = next(item for item in inputs.anchors if marker in item.exact_text)
        return ClaimExtractionOutput(
            (
                RawAssertion(
                    raw_assertion_id="RA-001",
                    anchor_id=anchor.anchor_id,
                    subject_text=inputs.target_names[0],
                    predicate=(
                        "reported firm HBM demand and limited supply"
                        if is_hbm
                        else "reported improved free cash flow"
                    ),
                    object_text=marker,
                    polarity_proposal=Polarity.POSITIVE,
                    event_date_text="2026-06-01",
                    exact_quote=anchor.exact_text,
                ),
            )
        )


class _CrowdingExtractor:
    def extract(self, inputs):
        is_hbm = "hbm" in inputs.retrieval_focus_terms
        marker = "HBM" if is_hbm else "FCF"
        anchor = next(item for item in inputs.anchors if marker in item.exact_text)
        if not is_hbm:
            predicates = ("reported improved FCF",)
        else:
            predicates = tuple(f"reported HBM fact {index}" for index in range(4))
        return ClaimExtractionOutput(
            tuple(
                RawAssertion(
                    raw_assertion_id=f"RA-{index}",
                    anchor_id=anchor.anchor_id,
                    subject_text=inputs.target_names[0],
                    predicate=predicate,
                    object_text=marker,
                    polarity_proposal=Polarity.POSITIVE,
                    event_date_text="2026-06-01",
                    exact_quote=anchor.exact_text,
                )
                for index, predicate in enumerate(predicates)
            )
        )


class _LimitedSupplyExtractor:
    def extract(self, inputs):
        return ClaimExtractionOutput(
            (
                RawAssertion(
                    raw_assertion_id="RA-LIMITED-SUPPLY",
                    anchor_id=inputs.anchors[0].anchor_id,
                    subject_text=inputs.target_names[0],
                    predicate="환경이 지속됐다고 밝혔다",
                    object_text="현재 환경",
                    polarity_proposal=Polarity.NORMAL,
                    event_date_text="2026-06-01",
                    exact_quote="견조한 수요 대비 제한된 공급 환경이 지속",
                ),
            )
        )


class _MassProductionShipmentExtractor:
    def extract(self, inputs):
        return ClaimExtractionOutput(
            (
                RawAssertion(
                    raw_assertion_id="RA-HBM4-MASS-PRODUCTION-SHIPMENT",
                    anchor_id=inputs.anchors[0].anchor_id,
                    subject_text=inputs.target_names[0],
                    predicate="HBM4 양산 출하",
                    object_text="HBM4를 고객에게 양산 출하",
                    polarity_proposal=Polarity.POSITIVE,
                    event_date_text="2026-02-12",
                    exact_quote="세계 최초 업계 최고 성능의 HBM4 양산 출하",
                ),
            )
        )


class _CapacityCandidateMapper:
    def map(self, inputs):
        if "hbm_capacity_constraint" not in inputs.canonical_primitive_ids:
            return PrimitiveMappingOutput()
        return PrimitiveMappingOutput(
            (
                PrimitiveMappingProposal.build(
                    claim_id=inputs.claim.claim_id,
                    archetype_id=inputs.contract.archetype_id,
                    primitive_id="hbm_capacity_constraint",
                    support_direction=SupportDirection.SUPPORT,
                    mapping_status=MappingStatus.ACCEPTED,
                    rationale="제한된 공급 원문은 현재 공급 제약을 직접 뒷받침한다.",
                ),
            )
        )


class _ShipmentCandidateMapper:
    def map(self, inputs):
        if "shipment_or_revenue_mix" not in inputs.canonical_primitive_ids:
            return PrimitiveMappingOutput()
        return PrimitiveMappingOutput(
            (
                PrimitiveMappingProposal.build(
                    claim_id=inputs.claim.claim_id,
                    archetype_id=inputs.contract.archetype_id,
                    primitive_id="shipment_or_revenue_mix",
                    support_direction=SupportDirection.SUPPORT,
                    mapping_status=MappingStatus.ACCEPTED,
                    rationale="HBM4 양산 출하 원문은 실제 shipment를 직접 뒷받침한다.",
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
