from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from e2r.agentic import (
    AgenticEvidenceProviderBundle,
    ClaimExtractionOutput,
    FakeClaimExtractorProvider,
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


class _NeverAdjudicator:
    def adjudicate(self, inputs):
        raise AssertionError("empty extraction must not adjudicate")


class _NeverMapper:
    def map(self, inputs):
        raise AssertionError("empty extraction must not map")


def _document() -> dict:
    text = (
        "테스트회사는 2026년 6월 1일 자기주식 취득 결정을 공시했다. "
        "이 문서는 고객 HBM 배정, 제품 세대, 생산능력 또는 계약 기간을 설명하지 않는다. "
        "따라서 별도의 공식 문서 확인이 필요하다."
    )
    return {
        "document_id": "DOC-" + hashlib.sha256(text.encode("utf-8")).hexdigest()[:20],
        "target_id": "000001",
        "target_name": "테스트회사",
        "source_task_ids": ["QSOURCE-TEST"],
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


def _task() -> dict:
    return {
        "task_id": "QSOURCE-TEST",
        "target_id": "000001",
        "company_name": "테스트회사",
        "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        "primitive_id": "customer_preorder_or_allocation",
        "recipe_id": "ERECIPE-TEST",
    }


if __name__ == "__main__":
    unittest.main()
