import unittest

from e2r.census.deep_dossier_scheduler import source_task_without_budget_count


class CensusNoUnboundedSourceTaskTests(unittest.TestCase):
    def test_missing_budget_counted(self):
        self.assertEqual(source_task_without_budget_count([{"task_id": "bad", "budget": {}}]), 1)


if __name__ == "__main__":
    unittest.main()
