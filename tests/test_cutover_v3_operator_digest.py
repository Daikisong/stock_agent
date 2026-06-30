import unittest

from e2r.production.cutover_v3 import _operator_digest_v3
from tests.cutover_v3_test_helpers import fake_provider_matrix, fake_v3_base


class CutoverV3OperatorDigestTests(unittest.TestCase):
    def test_operator_digest_has_next_action_and_no_provider_reject(self):
        report = _operator_digest_v3(base_bundles=[fake_v3_base()], provider_matrix=fake_provider_matrix())
        self.assertEqual(report["summary"]["status"], "OPERATOR_DIGEST_PASS")
        self.assertTrue(all(row["next_action"] for row in report["rows"]))
        self.assertEqual(report["summary"]["provider_failure_final_reject_count"], 0)

    def test_provider_failure_is_source_pending_not_final_watch(self):
        base = dict(fake_v3_base())
        base["source_connector_report"] = {
            "summary": {"provider_failure_count": 1},
            "rows": [
                {
                    "provider_name": "IssuerIR",
                    "status": "PROVIDER_FAILED",
                    "provider_error": "IR page unavailable",
                    "request_params": {"symbol": "000000", "company_name": "회사0"},
                }
            ],
        }
        report = _operator_digest_v3(base_bundles=[base], provider_matrix=fake_provider_matrix())
        row = next(item for item in report["rows"] if item["symbol"] == "000000")
        self.assertEqual(row["next_action"], "RECHECK_SOURCE")
        self.assertEqual(row["score_status"], "PROVIDER_SOURCE_PENDING")
        self.assertTrue(row["provider_source_gaps"])
        self.assertEqual(report["summary"]["provider_gap_final_watch_count"], 0)


if __name__ == "__main__":
    unittest.main()
