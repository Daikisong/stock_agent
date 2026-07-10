from __future__ import annotations

import hashlib
import json
import unittest
from datetime import date
from pathlib import Path

from e2r.production.source_connectors.source_provider_registry import (
    SourceFetchResult,
    SourceProviderRegistry,
)
from e2r.research_brain.runtime.live_materialization import (
    AcquisitionResultClass,
    CurrentSourceAcquisitionOrchestrator,
    SourceAcquisitionConfig,
)


class LiveSourceAcquisitionOrchestratorTest(unittest.TestCase):
    def test_live_operational_audit_records_real_full_documents(self) -> None:
        path = (
            Path(__file__).resolve().parents[1]
            / "docs"
            / "operational"
            / "e2r_live_source_acquisition_audit.json"
        )
        audit = json.loads(path.read_text(encoding="utf-8"))

        self.assertEqual(audit["status"], "PHASE_27_ACCEPTED")
        self.assertGreater(audit["actual_live_or_fresh_document_count"], 0)
        self.assertGreater(audit["unique_evidence_document_count"], 0)
        self.assertEqual(sum(audit["critical_counts"].values()), 0)
        self.assertFalse(audit["safety"]["provider_error_body_materialized"])
        self.assertFalse(audit["safety"]["search_snippet_materialized"])

    def test_same_target_provider_fetch_is_reused_as_fresh_cache(self) -> None:
        connector = _FetchedDartConnector()
        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=2,
                test_mode=True,
            ),
            source_tasks=(_daily_task("Q-1"), _daily_task("Q-2")),
            question_source_tasks=(_question_task("Q-1"), _question_task("Q-2")),
            provider_registry=SourceProviderRegistry((connector,)),
        )

        self.assertEqual(result.status, "CURRENT_SOURCE_ACQUISITION_PASS")
        self.assertEqual(connector.calls, 1)
        self.assertEqual(len(result.evidence_documents), 1)
        self.assertEqual(
            result.evidence_documents[0].source_task_ids,
            ("Q-1", "Q-2"),
        )
        self.assertEqual(
            [item.acquisition_class for item in result.provider_fetch_results],
            [
                AcquisitionResultClass.REAL_PROVIDER_FETCH.value,
                AcquisitionResultClass.FRESH_PROVIDER_CACHE.value,
            ],
        )
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_generic_portal_is_health_only_and_never_document(self) -> None:
        task = _question_task("Q-KRX", source="KRX")
        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=1,
                test_mode=True,
            ),
            source_tasks=(_daily_task("Q-KRX", source="KRX"),),
            question_source_tasks=(task,),
            provider_registry=SourceProviderRegistry((_GenericKrxConnector(),)),
        )

        self.assertFalse(result.evidence_documents)
        self.assertEqual(
            result.provider_fetch_results[0].acquisition_class,
            AcquisitionResultClass.PROVIDER_HEALTH_ONLY.value,
        )
        self.assertEqual(
            result.audit["critical_counts"]["generic_portal_counted_as_symbol_evidence"],
            0,
        )

    def test_provider_failure_is_not_masked_as_no_result(self) -> None:
        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=1,
                test_mode=True,
            ),
            source_tasks=(_daily_task("Q-FAIL"),),
            question_source_tasks=(_question_task("Q-FAIL"),),
            provider_registry=SourceProviderRegistry((_FailedDartConnector(),)),
        )

        self.assertEqual(
            result.provider_fetch_results[0].acquisition_class,
            AcquisitionResultClass.PROVIDER_FAILED.value,
        )
        self.assertEqual(
            result.audit["critical_counts"]["provider_failure_masked_no_result"],
            0,
        )

    def test_provider_error_body_is_not_materialized_as_document(self) -> None:
        result = CurrentSourceAcquisitionOrchestrator().acquire(
            SourceAcquisitionConfig(
                as_of_date="2026-07-10",
                max_tasks=1,
                test_mode=True,
            ),
            source_tasks=(_daily_task("Q-ERROR-BODY"),),
            question_source_tasks=(_question_task("Q-ERROR-BODY"),),
            provider_registry=SourceProviderRegistry((_ErrorBodyDartConnector(),)),
        )

        self.assertFalse(result.evidence_documents)
        self.assertEqual(
            result.provider_fetch_results[0].acquisition_class,
            AcquisitionResultClass.REJECTED_BY_POLICY.value,
        )
        self.assertEqual(
            result.provider_fetch_results[0].policy_rejection_reason,
            "fetched_document_content_too_small",
        )


class _FetchedDartConnector:
    provider_name = "OpenDART"
    source_class = "DART"

    def __init__(self) -> None:
        self.calls = 0

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str):
        self.calls += 1
        text = (
            f"{company_name}({symbol}) 2026년 1분기 공식 사업보고 원문. "
            "계약 기간, 계약 금액, 현금흐름, 취소 조건과 최신 정정 여부를 "
            "회사 직접 공시의 본문과 표에서 확인할 수 있다."
        )
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"REQ-{symbol}",
            request_params={"symbol": symbol},
            status="FETCHED",
            canonical_url=f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={symbol}",
            official_document_id=f"opendart:disclosure:{symbol}",
            published_at="2026-05-15",
            available_at="2026-05-15",
            fetched_at="2026-07-10T09:00:00Z",
            content_hash=hashlib.sha256(text.encode("utf-8")).hexdigest(),
            raw_text=text,
            structured_payload={"symbol": symbol, "detail_fetched": True},
            provider_request_id=f"REQ-{symbol}",
        )


class _FailedDartConnector:
    provider_name = "OpenDART"
    source_class = "DART"

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str):
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"REQ-{symbol}",
            request_params={"symbol": symbol},
            status="PROVIDER_FAILED",
            fetched_at="2026-07-10T09:00:00Z",
            provider_error="provider unavailable",
            provider_request_id=f"REQ-{symbol}",
        )


class _ErrorBodyDartConnector:
    provider_name = "OpenDART"
    source_class = "DART"

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str):
        text = "014 파일이 존재하지 않습니다."
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"REQ-{symbol}",
            request_params={"symbol": symbol},
            status="FETCHED",
            canonical_url=f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={symbol}",
            official_document_id=f"opendart:disclosure:{symbol}",
            published_at="2026-05-15",
            available_at="2026-05-15",
            fetched_at="2026-07-10T09:00:00Z",
            content_hash=hashlib.sha256(text.encode("utf-8")).hexdigest(),
            raw_text=text,
            structured_payload={"symbol": symbol},
            provider_request_id=f"REQ-{symbol}",
        )


class _GenericKrxConnector:
    provider_name = "KRX"
    source_class = "KRX"

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str):
        text = "KRX Market Data Center generic portal"
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=f"REQ-{symbol}",
            request_params={"symbol": symbol},
            status="FETCHED",
            canonical_url="https://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd",
            official_document_id="krx:mdc:main",
            published_at="2026-07-10",
            available_at="2026-07-10",
            fetched_at="2026-07-10T09:00:00Z",
            content_hash=hashlib.sha256(text.encode("utf-8")).hexdigest(),
            raw_text=text,
            structured_payload={
                "score_usage": "provider_coverage_only_until_symbol_risk_endpoint_is_available"
            },
            provider_request_id=f"REQ-{symbol}",
        )


def _question_task(task_id: str, *, source: str = "DART") -> dict:
    return {
        "task_id": task_id,
        "target_id": "000001",
        "company_name": "테스트회사",
        "as_of_date": "2026-07-10",
        "runtime_score_eligible": False,
        "production_execution_allowed": False,
        "source_route": {
            "preferred_source_families": [source],
            "fallback_source_families": ["TrustedNews"],
        },
        "budget": {"max_queries": 1, "max_candidates": 8, "max_fetches": 4},
        "query_intent": {"literal_queries": ["테스트회사 2026년 1분기 공식 공시"]},
    }


def _daily_task(question_task_id: str, *, source: str = "DART") -> dict:
    return {
        "task_id": f"DAILY-{question_task_id}",
        "question_task_id": question_task_id,
        "target_id": "000001",
        "source_class": source,
        "max_queries": 1,
        "max_candidates": 8,
        "max_fetches": 4,
        "max_retries": 2,
    }


if __name__ == "__main__":
    unittest.main()
