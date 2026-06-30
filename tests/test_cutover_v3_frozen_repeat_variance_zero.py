import unittest

from e2r.production.cutover_v3 import _frozen_replay_rows_from_live


class CutoverV3FrozenRepeatVarianceZeroTests(unittest.TestCase):
    def test_repeated_frozen_signatures_have_zero_variance(self):
        rows = _frozen_replay_rows_from_live(
            [{"as_of_date": "2026-06-30", "watchlist_signature": "abc", "source_corpus_hash": "src"}],
            required_days=10,
            repeated_days=3,
        )
        repeat_rows = [row for row in rows if row["run_kind"] == "frozen_repeat_group"]
        self.assertEqual(len(repeat_rows), 3)
        self.assertEqual(sum(row["repeat_variance"] for row in repeat_rows), 0)


if __name__ == "__main__":
    unittest.main()
