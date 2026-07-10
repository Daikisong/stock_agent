from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from e2r.production.source_connectors.source_provider_registry import SourceFetchResult
from e2r.research_brain.runtime.live_materialization import (
    ProviderDocumentRole,
    audit_live_credentials,
    build_provider_capability_matrix,
    classify_provider_result,
    counts_as_symbol_evidence,
)


class LiveProviderCapabilityMatrixTests(unittest.TestCase):
    def test_operational_capability_artifact_matches_runtime_contract(self) -> None:
        artifact = json.loads(
            (
                Path(__file__).resolve().parents[1]
                / "docs/operational/e2r_live_provider_capability_matrix.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, build_provider_capability_matrix())

    def test_required_provider_matrix_is_complete(self) -> None:
        matrix = build_provider_capability_matrix()
        self.assertEqual(matrix["provider_count"], 10)
        self.assertEqual(
            set(matrix["required_provider_names"]),
            {
                "OpenDART",
                "KRX",
                "KIND",
                "CompanyGuide",
                "IssuerIR",
                "TrustedNews",
                "NaverSearch",
                "GeneralWebFetcher",
                "ExistingLedger",
                "ResearchMemory",
            },
        )
        self.assertFalse(matrix["generic_portal_symbol_evidence_allowed"])

    def test_krx_and_kind_main_pages_are_provider_health_only(self) -> None:
        for provider, url, document_id in (
            (
                "KRX",
                "https://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd",
                "krx:mdc:main",
            ),
            ("KIND", "https://kind.krx.co.kr/main.do", "kind:main"),
        ):
            row = SourceFetchResult(
                provider_name=provider,
                source_class=provider,
                mode="live",
                request_id=f"REQ-{provider}",
                status="FETCHED",
                canonical_url=url,
                official_document_id=document_id,
                content_hash="a" * 64,
                raw_text="provider main page",
                structured_payload={"symbol": "005930"},
            )
            self.assertTrue(row.counts_as_live)
            self.assertFalse(row.counts_as_symbol_evidence)
            self.assertEqual(
                classify_provider_result(row),
                ProviderDocumentRole.PROVIDER_HEALTH_ONLY.value,
            )

    def test_generic_companyguide_page_without_symbol_is_health_only(self) -> None:
        row = {
            "provider_name": "CompanyGuide",
            "mode": "live",
            "status": "FETCHED",
            "canonical_url": "https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp",
            "official_document_id": "companyguide:generic",
            "content_hash": "b" * 64,
        }
        self.assertFalse(counts_as_symbol_evidence(row))
        self.assertEqual(
            classify_provider_result(row),
            ProviderDocumentRole.PROVIDER_HEALTH_ONLY.value,
        )

    def test_symbol_specific_official_document_can_be_evidence(self) -> None:
        row = {
            "provider_name": "OpenDART",
            "mode": "live",
            "status": "FETCHED",
            "canonical_url": "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=202607100001",
            "official_document_id": "202607100001",
            "content_hash": "c" * 64,
        }
        self.assertTrue(counts_as_symbol_evidence(row))
        self.assertEqual(
            classify_provider_result(row),
            ProviderDocumentRole.SYMBOL_EVIDENCE.value,
        )

    def test_credential_audit_loads_env_names_without_emitting_values(self) -> None:
        with tempfile.TemporaryDirectory() as tmp, patch.dict("os.environ", {}, clear=True):
            env_path = Path(tmp) / ".env"
            env_path.write_text(
                "\n".join(
                    (
                        "OPENDART_API_KEY=SECRET_DART_VALUE",
                        "KRX_OPENAPI_KEY=SECRET_KRX_VALUE",
                        "NAVER_CLIENT_ID=SECRET_NAVER_ID",
                        "NAVER_CLIENT_SECRET=SECRET_NAVER_VALUE",
                    )
                ),
                encoding="utf-8",
            )
            audit = audit_live_credentials(env_file=env_path)

        serialized = json.dumps(audit, ensure_ascii=False, sort_keys=True)
        self.assertTrue(audit["secret_values_emitted"] is False)
        self.assertNotIn("SECRET_DART_VALUE", serialized)
        self.assertNotIn("SECRET_KRX_VALUE", serialized)
        self.assertNotIn("SECRET_NAVER_VALUE", serialized)
        by_provider = {row["provider_name"]: row for row in audit["rows"]}
        self.assertEqual(by_provider["OpenDART"]["credential_state"], "PRESENT")
        self.assertEqual(by_provider["KRX"]["credential_state"], "PRESENT")
        self.assertEqual(by_provider["NaverSearch"]["credential_state"], "PRESENT")

    def test_missing_credentials_use_specific_blocker(self) -> None:
        audit = audit_live_credentials(environment={}, load_env_file=False)
        by_provider = {row["provider_name"]: row for row in audit["rows"]}
        for provider in ("OpenDART", "KRX", "NaverSearch"):
            self.assertEqual(by_provider[provider]["credential_state"], "MISSING")
            self.assertEqual(by_provider[provider]["blocker_code"], "MISSING_CREDENTIAL")

    def test_operational_credential_artifact_never_contains_secret_values(self) -> None:
        artifact_path = (
            Path(__file__).resolve().parents[1]
            / "docs/operational/e2r_live_credential_audit.json"
        )
        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertFalse(artifact["secret_values_emitted"])
        self.assertEqual(artifact["credential_state_counts"]["MISSING"], 0)
        self.assertNotIn("credential_value", artifact_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
