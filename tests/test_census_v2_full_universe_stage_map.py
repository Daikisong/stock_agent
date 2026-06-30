import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2FullUniverseStageMapTests(unittest.TestCase):
    def test_every_eligible_symbol_has_exactly_one_stage_row(self):
        artifacts = census_v2_artifacts()
        eligible = [row["symbol"] for row in artifacts["universe"] if row.get("eligible_for_census")]
        stage_symbols = [row["symbol"] for row in artifacts["stage_rows"]]
        self.assertEqual(len(stage_symbols), len(eligible))
        self.assertEqual(len(stage_symbols), len(set(stage_symbols)))
        self.assertEqual(set(stage_symbols), set(eligible))

    def test_full_universe_verdict_passes(self):
        self.assertEqual(census_v2_artifacts()["result"].readiness_verdict["verdict"], "FULL_UNIVERSE_STAGE_MAP_PASS")


if __name__ == "__main__":
    unittest.main()
