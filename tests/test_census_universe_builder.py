import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

from e2r.census.universe import build_universe
from tests.census_test_helpers import write_universe_csv


class CensusUniverseBuilderTests(unittest.TestCase):
    def test_builds_eligible_universe_from_csv(self):
        with TemporaryDirectory() as tmp:
            path = write_universe_csv(Path(tmp) / "universe.csv", count=3)
            result = build_universe(as_of_date="2026-07-01", universe_file=path)
            self.assertEqual(result.coverage["raw_universe_count"], 3)
            self.assertEqual(result.coverage["eligible_common_stock_count"], 3)
            self.assertEqual(result.coverage["fixture_like_symbol_count"], 0)
            self.assertTrue(all(row.market in {"KOSPI", "KOSDAQ"} for row in result.instruments))


if __name__ == "__main__":
    unittest.main()
