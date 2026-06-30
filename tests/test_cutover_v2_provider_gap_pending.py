import unittest

from e2r.production.cutover_v2 import _operator_digest_v2


class CutoverV2ProviderGapPendingTests(unittest.TestCase):
    def test_provider_gap_becomes_provider_wait(self):
        report = _operator_digest_v2(
            base={"operator_digest": {"rows": [{"symbol": "000660", "company_name": "SK하이닉스", "section": "Stage2-Watch"}]}},
            provider_matrix={"summary": {"provider_blocker_count": 2}},
        )
        self.assertEqual(report["summary"]["next_action_counts"]["PROVIDER_WAIT"], 1)


if __name__ == "__main__":
    unittest.main()
