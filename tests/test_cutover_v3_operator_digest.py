import unittest

from e2r.production.cutover_v3 import _operator_digest_v3
from tests.cutover_v3_test_helpers import fake_provider_matrix, fake_v3_base


class CutoverV3OperatorDigestTests(unittest.TestCase):
    def test_operator_digest_has_next_action_and_no_provider_reject(self):
        report = _operator_digest_v3(base_bundles=[fake_v3_base()], provider_matrix=fake_provider_matrix())
        self.assertEqual(report["summary"]["status"], "OPERATOR_DIGEST_PASS")
        self.assertTrue(all(row["next_action"] for row in report["rows"]))
        self.assertEqual(report["summary"]["provider_failure_final_reject_count"], 0)


if __name__ == "__main__":
    unittest.main()
