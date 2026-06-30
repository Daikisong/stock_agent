import unittest

from e2r.production.cutover_v2 import _operator_digest_v2


class CutoverV2OperatorDigestTests(unittest.TestCase):
    def test_provider_failure_item_is_provider_wait_not_reject(self):
        report = _operator_digest_v2(
            base={"operator_digest": {"rows": [{"symbol": "005930", "company_name": "삼성전자", "section": "Stage2-Watch"}]}},
            provider_matrix={"summary": {"provider_blocker_count": 1}},
        )
        self.assertEqual(report["rows"][0]["next_action"], "PROVIDER_WAIT")


if __name__ == "__main__":
    unittest.main()
