import unittest

from e2r.production.cutover_v3 import _provider_completeness_matrix_v3


class CutoverV3ProviderCompletenessTests(unittest.TestCase):
    def test_provider_completeness_passes_with_opendart_risk_and_revision_paths(self):
        rows = []
        for provider in ("OpenDART", "KRX", "CompanyGuide"):
            rows.append(
                {
                    "provider_name": provider,
                    "status": "FETCHED",
                    "mode": "live",
                    "provider_request_id": f"REQ-{provider}",
                    "content_hash": f"HASH-{provider}",
                    "canonical_url": f"https://example.com/{provider}",
                }
            )
        for provider in ("IssuerIR", "TrustedNews"):
            rows.append(
                {
                    "provider_name": provider,
                    "status": "PROVIDER_FAILED",
                    "mode": "live",
                    "provider_request_id": f"REQ-{provider}",
                    "provider_error": "not configured",
                }
            )
        matrix = _provider_completeness_matrix_v3({"rows": rows})
        self.assertEqual(matrix["summary"]["status"], "PROVIDER_COMPLETENESS_PASS")
        self.assertEqual(matrix["summary"]["provider_blocker_count"], 0)
        self.assertEqual(matrix["summary"]["provider_accounting_gap_count"], 0)
        self.assertGreaterEqual(matrix["summary"]["risk_provider_path_exercised_count"], 1)
        self.assertGreaterEqual(matrix["summary"]["revision_report_ir_provider_path_exercised_count"], 1)

    def test_required_provider_gap_blocks_pass(self):
        matrix = _provider_completeness_matrix_v3({"rows": [{"provider_name": "OpenDART", "status": "FETCHED"}]})
        self.assertNotEqual(matrix["summary"]["status"], "PROVIDER_COMPLETENESS_PASS")
        self.assertGreater(matrix["summary"]["provider_blocker_count"], 0)

    def test_fetched_provider_without_request_id_or_content_hash_is_not_ready(self):
        rows = [
            {"provider_name": "OpenDART", "status": "FETCHED", "mode": "live", "canonical_url": "https://example.com"},
            {"provider_name": "KRX", "status": "FETCHED", "mode": "live", "canonical_url": "https://example.com"},
            {"provider_name": "CompanyGuide", "status": "FETCHED", "mode": "live", "canonical_url": "https://example.com"},
        ]
        matrix = _provider_completeness_matrix_v3({"rows": rows})
        self.assertEqual(matrix["summary"]["provider_success_missing_metadata_count"], 3)
        self.assertEqual(matrix["summary"]["status"], "PROVIDER_COMPLETENESS_NOT_READY")


if __name__ == "__main__":
    unittest.main()
