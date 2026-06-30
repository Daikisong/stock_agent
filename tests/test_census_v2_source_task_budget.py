import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2SourceTaskBudgetTests(unittest.TestCase):
    def test_source_tasks_are_bounded(self):
        for task in census_v2_artifacts()["source_tasks"]:
            budget = task.get("budget") or {}
            self.assertIn("max_queries", budget)
            self.assertIn("max_fetches", budget)
            self.assertIsNotNone(budget["max_queries"])
            self.assertIsNotNone(budget["max_fetches"])
            self.assertFalse(task.get("allows_general_web"))


if __name__ == "__main__":
    unittest.main()
