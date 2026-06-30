import unittest

from e2r.census.shard_planner import duplicate_symbol_count, merge_stage_maps


class CensusShardMergeTests(unittest.TestCase):
    def test_merge_dedupes_deterministically(self):
        rows = [{"symbol": "000002"}, {"symbol": "000001"}, {"symbol": "000001"}]
        merged = merge_stage_maps(rows)
        self.assertEqual([row["symbol"] for row in merged], ["000001", "000002"])
        self.assertEqual(duplicate_symbol_count(rows), 1)


if __name__ == "__main__":
    unittest.main()
