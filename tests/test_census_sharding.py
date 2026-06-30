import unittest

from e2r.census.shard_planner import select_shard
from tests.census_test_helpers import instrument


class CensusShardingTests(unittest.TestCase):
    def test_shards_partition_symbols(self):
        instruments = [instrument(f"{idx:06d}") for idx in range(1, 20)]
        shard0 = select_shard(instruments, shard_count=2, shard_index=0)
        shard1 = select_shard(instruments, shard_count=2, shard_index=1)
        self.assertEqual(len({row.symbol for row in shard0} & {row.symbol for row in shard1}), 0)
        self.assertEqual(len(shard0) + len(shard1), len(instruments))


if __name__ == "__main__":
    unittest.main()
