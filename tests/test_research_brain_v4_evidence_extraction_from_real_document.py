import unittest
from datetime import date

from e2r.agentic.evidence_os import AnchorType, EvidenceAnchor, EvidenceDocument, SourceType
from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
from e2r.research_brain.v4_schemas import SourceAcquisitionResultV4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from research_brain_v4_test_helpers import c06_source_task, sample_v4_event


class _SingleDocumentRunner:
    def __init__(self, *, symbol: str, company_name: str, published_at: date, text: str, anchor_type=AnchorType.API_RECORD) -> None:
        self.symbol = symbol
        self.company_name = company_name
        self.published_at = published_at
        self.text = text
        self.anchor_type = anchor_type

    def acquire(self, *, event, task, as_of_date):
        document = EvidenceDocument.from_text(
            text=self.text,
            canonical_url=f"snapshot://unit/{self.symbol}",
            source_type=SourceType.NEWS,
            source_name="unit",
            published_at=self.published_at,
            available_at=self.published_at,
            fetched_at=as_of_date,
            parser_version="unit",
            source_proxy_only=False,
        )
        anchor = EvidenceAnchor.structured(
            document=document,
            anchor_type=self.anchor_type,
            locator="unit:1",
            exact_text=self.text,
            normalized_value={
                "symbol": self.symbol,
                "company_name": self.company_name,
                "row": {"EPS_ACTION_TYP_NM": "추정EPS 상향"},
            },
            anchor_verified=True,
        )
        return SourceAcquisitionResultV4(
            task_id=task.task_id,
            source_class="TrustedNews",
            provider_name="unit",
            status="PARSED",
            documents=(document,),
            anchors=(anchor,),
            document_text_by_id={document.document_id: self.text},
            fetched_document_ids=(document.document_id,),
            document_urls=(document.canonical_url,),
            document_hashes=(document.content_hash,),
            anchor_ids=(anchor.anchor_id,),
            budget_used={"queries": 1, "candidates": 1, "fetches": 1},
            stop_reason="unit",
        )


class ResearchBrainV4EvidenceExtractionFromRealDocumentTests(unittest.TestCase):
    def test_real_document_anchor_produces_accepted_claim(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(),
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot"),
        )
        execution = bundle.executions[0]
        self.assertEqual(execution.status, "EVIDENCE_OS_ACCEPTED")
        self.assertTrue(execution.fetched_document_ids)
        self.assertTrue(execution.evidence_anchor_ids)
        self.assertTrue(execution.accepted_claim_ids)
        for claim_id in execution.accepted_claim_ids:
            self.assertIn(claim_id, bundle.ledger.claims)

    def test_wrong_subject_document_is_rejected_not_scored(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(symbol="005930", company_name="삼성전자"),
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=_SingleDocumentRunner(
                symbol="999999",
                company_name="월덱스",
                published_at=date(2026, 6, 20),
                text="월덱스는 삼성전자를 고객으로 언급했지만 HBM 고객 수요와 추정EPS 상향은 월덱스 문서 주체의 내용이다.",
            ),
        )
        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertIn("target_scope_not_allowed:UNRELATED", execution.not_eligible_reasons)
        self.assertGreater(bundle.extraction_audit["wrong_subject_rejected_count"], 0)

    def test_old_positive_document_without_current_confirmation_is_historical_not_scored(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(),
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=_SingleDocumentRunner(
                symbol="005930",
                company_name="삼성전자",
                published_at=date(2020, 1, 10),
                text="삼성전자는 HBM 고객 수요와 추정EPS 상향 가능성을 당시 언급했다.",
            ),
        )
        execution = bundle.executions[0]
        self.assertFalse(execution.accepted_claim_ids)
        self.assertIn("temporal_not_allowed:HISTORICAL", execution.not_eligible_reasons)


if __name__ == "__main__":
    unittest.main()
