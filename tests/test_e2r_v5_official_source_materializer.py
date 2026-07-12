from __future__ import annotations

import hashlib
import tempfile
import unittest
from datetime import date

from e2r.production.source_connectors.source_provider_registry import (
    SourceFetchResult,
    SourceProviderRegistry,
)
from e2r.research_brain.researcher_mode import (
    CurrentOfficialSourceMaterializer,
    write_official_source_materialization,
)


class FakeOpenDART:
    provider_name = "OpenDART"
    source_class = "DART"

    def __init__(self, *, status: str = "FETCHED") -> None:
        self.status = status
        self.calls = []

    def fetch_research_document(self, **kwargs):
        self.calls.append(kwargs)
        text = (
            "<DOCUMENT><BODY>Current Corp material fact with exact source text. "
            + "A" * 5200
            + "</BODY></DOCUMENT>"
        )
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode="live",
            request_id="DART-REQUEST",
            status=self.status,
            canonical_url="https://dart.fss.or.kr/dsaf001/main.do?rcpNo=1",
            official_document_id="dart:1",
            published_at="2026-05-15",
            available_at="2026-05-15",
            fetched_at="2026-06-29T08:00:00Z",
            content_hash=hashlib.sha256(text.encode()).hexdigest(),
            raw_text=text if self.status == "FETCHED" else "",
            structured_payload={"title": "Quarterly report", "rcept_no": "1"},
            provider_error=None if self.status == "FETCHED" else "provider failed",
            provider_request_id="DART-PROVIDER-REQUEST",
        )


class FakeCompanyGuide:
    provider_name = "CompanyGuide"
    source_class = "CompanyGuide"

    def fetch(self, **kwargs):
        text = "<html><body>target consensus</body></html>"
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode="live",
            request_id="CG-REQUEST",
            status="FETCHED",
            canonical_url="https://comp.fnguide.com/?gicode=ACURRENT",
            official_document_id="companyguide:CURRENT",
            published_at="2026-06-27",
            available_at="2026-06-27",
            fetched_at="2026-06-29T08:00:00Z",
            content_hash=hashlib.sha256(text.encode()).hexdigest(),
            raw_text=text,
            structured_payload={"EPS": 123.0, "FORWARD_PER": 9.5},
            provider_request_id="CG-PROVIDER-REQUEST",
        )


class E2RV5OfficialSourceMaterializerTests(unittest.TestCase):
    def test_official_first_preserves_every_chunk_and_structured_payload(self) -> None:
        dart = FakeOpenDART()
        registry = SourceProviderRegistry((dart, FakeCompanyGuide()))
        result = CurrentOfficialSourceMaterializer(
            provider_registry=registry,
            chunk_chars=2_000,
        ).materialize(
            target_id="CURRENT",
            target_name="Current Corp",
            as_of_date="2026-06-29",
            objective_ids=("OBJECTIVE-1", "OBJECTIVE-2"),
            live_materialization_authorized=True,
        )

        self.assertEqual(result.status, "OFFICIAL_SOURCE_MATERIALIZED")
        self.assertGreater(len(result.evidence_documents), 1)
        self.assertTrue(all(row["all_chunks_preserved"] for row in result.evidence_documents))
        self.assertTrue(all(row["full_source_fetch_performed"] for row in result.evidence_documents))
        self.assertTrue(all(not row["snippet_only"] for row in result.evidence_documents))
        self.assertTrue(all(len(row["content_text"]) <= 2_000 for row in result.evidence_documents))
        self.assertEqual(
            sum(len(row["content_text"]) for row in result.evidence_documents),
            result.evidence_documents[0]["full_source_text_chars"],
        )
        self.assertEqual(len(result.structured_payloads), 2)
        self.assertEqual(dart.calls[0]["mode"], "live")
        with tempfile.TemporaryDirectory() as directory:
            paths = write_official_source_materialization(result, directory)
            self.assertTrue(all(path.is_file() for path in paths.values()))

    def test_mandatory_official_failure_is_pending_not_zero_or_absence(self) -> None:
        result = CurrentOfficialSourceMaterializer(
            provider_registry=SourceProviderRegistry((FakeOpenDART(status="PROVIDER_FAILED"),)),
            chunk_chars=2_000,
        ).materialize(
            target_id="CURRENT",
            target_name="Current Corp",
            as_of_date="2026-06-29",
            objective_ids=("OBJECTIVE-1",),
            live_materialization_authorized=True,
        )
        self.assertEqual(result.status, "OFFICIAL_SOURCE_PENDING")
        self.assertEqual(result.evidence_documents, ())
        self.assertTrue(
            any("MANDATORY_OFFICIAL_PROVIDER_PENDING" in row for row in result.pending_reasons)
        )
        self.assertFalse(result.production_score_authority)
        self.assertNotIn("score", result.to_dict())

    def test_live_execution_requires_explicit_authorization(self) -> None:
        with self.assertRaisesRegex(ValueError, "explicit authorization"):
            CurrentOfficialSourceMaterializer(
                provider_registry=SourceProviderRegistry((FakeOpenDART(),)),
                chunk_chars=2_000,
            ).materialize(
                target_id="CURRENT",
                target_name="Current Corp",
                as_of_date="2026-06-29",
                objective_ids=(),
                live_materialization_authorized=False,
            )


if __name__ == "__main__":
    unittest.main()
