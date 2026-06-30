import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.census_runner import CensusRunConfig, run_census_mode
from tests.census_test_helpers import write_universe_csv


class CensusFullUniverseStageMapTests(unittest.TestCase):
    def test_full_universe_map_represents_every_eligible_symbol_once(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            universe = write_universe_csv(root / "universe.csv", count=1101)
            output = root / "out"
            result = run_census_mode(
                CensusRunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output),
                    universe_file=str(universe),
                    max_symbols=0,
                    fail_on_critical_audit=True,
                    write_operational_docs=False,
                )
            )
            rows = [json.loads(line) for line in (output / "census_stage_map.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertGreater(result.universe_coverage["eligible_common_stock_count"], 1000)
            self.assertEqual(len(rows), result.universe_coverage["eligible_common_stock_count"])
            self.assertEqual(len({row["symbol"] for row in rows}), len(rows))
            self.assertEqual(result.audit_summary["summary"]["critical_count_sum"], 0)


if __name__ == "__main__":
    unittest.main()
