import unittest

from e2r.production.cutover_v3 import _frozen_repeat_rows_from_replay_rows, _frozen_replay_row_from_bundle
from tests.cutover_v3_test_helpers import fake_v3_frozen_base


class CutoverV3FrozenRepeatVarianceZeroTests(unittest.TestCase):
    def test_repeated_frozen_signatures_have_zero_variance(self):
        rows = [
            _frozen_replay_row_from_bundle(fake_v3_frozen_base("2026-06-30", run_index=run_index))
            for run_index in (1, 2, 3)
        ]
        repeat_rows = _frozen_repeat_rows_from_replay_rows(rows)
        self.assertEqual(len(repeat_rows), 1)
        self.assertEqual(sum(row["repeat_variance"] for row in repeat_rows), 0)


if __name__ == "__main__":
    unittest.main()
