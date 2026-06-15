import unittest

from e2r.research.search_budget import ResearchLayer, SearchBudget, SearchBudgetTracker


class SearchBudgetTests(unittest.TestCase):
    def test_default_budget_does_not_stop_query_accounting(self):
        tracker = SearchBudgetTracker(SearchBudget())

        for _ in range(5):
            self.assertTrue(tracker.can_run("TEST", ResearchLayer.DEEP_RESEARCH).allowed)
            tracker.record_query("TEST", ResearchLayer.DEEP_RESEARCH)

        self.assertTrue(tracker.can_run("TEST", ResearchLayer.DEEP_RESEARCH).allowed)

    def test_explicit_small_budget_still_blocks(self):
        tracker = SearchBudgetTracker(SearchBudget(max_total_queries_per_day=1, max_queries_per_symbol=1))

        self.assertTrue(tracker.can_run("TEST", ResearchLayer.DEEP_RESEARCH).allowed)
        tracker.record_query("TEST", ResearchLayer.DEEP_RESEARCH)

        self.assertFalse(tracker.can_run("TEST", ResearchLayer.DEEP_RESEARCH).allowed)


if __name__ == "__main__":
    unittest.main()
