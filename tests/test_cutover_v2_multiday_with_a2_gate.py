import unittest

from e2r.production.cutover_v2 import _multiday_validation_v2


class CutoverV2MultidayWithA2GateTests(unittest.TestCase):
    def test_multiday_requires_a2_count(self):
        report = _multiday_validation_v2(
            base={"multiday_validation": {"summary": {"status": "MULTIDAY_SHADOW_PASS"}, "rows": []}},
            a2={"report": {"summary": {"A2_REAL_REPLAY_VERIFIED_count": 0}}},
            provider_matrix={"summary": {"provider_blocker_count": 0}},
        )
        self.assertEqual(report["summary"]["status"], "MULTIDAY_SHADOW_NOT_COMPLETE")


if __name__ == "__main__":
    unittest.main()
