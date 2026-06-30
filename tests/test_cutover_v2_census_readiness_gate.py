import unittest

from e2r.production.cutover_v2 import _census_readiness


class CutoverV2CensusReadinessGateTests(unittest.TestCase):
    def test_census_implementation_not_ready_when_provider_gap_material(self):
        census = _census_readiness(
            base={},
            a2={"report": {"summary": {"A2_REAL_REPLAY_VERIFIED_count": 30}}},
            provider_matrix={"summary": {"provider_blocker_count": 1}},
            stage_distribution={"summary": {"status": "MEANINGFUL_STAGE_SPLIT_PASS"}},
        )
        self.assertEqual(census["label"], "READY_FOR_CENSUS_DESIGN")
        self.assertNotIn("READY_FOR_CENSUS_IMPLEMENTATION", census["label"])


if __name__ == "__main__":
    unittest.main()
