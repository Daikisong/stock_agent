import unittest

from e2r.production.cutover_v3 import _operator_digest_v3
from tests.cutover_v3_test_helpers import fake_provider_matrix, fake_v3_base


class CutoverV3ProviderPendingNotFinalRejectTests(unittest.TestCase):
    def test_provider_blocker_rows_become_provider_wait_not_final_reject(self):
        report = _operator_digest_v3(
            base_bundles=[fake_v3_base()],
            provider_matrix=fake_provider_matrix(status="PROVIDER_COMPLETENESS_NOT_READY", blockers=1),
        )

        self.assertGreater(report["summary"]["pending_item_count"], 0)
        self.assertEqual(report["summary"]["provider_failure_final_reject_count"], 0)
        self.assertTrue(all(row["next_action"] == "PROVIDER_WAIT" for row in report["rows"]))


if __name__ == "__main__":
    unittest.main()
