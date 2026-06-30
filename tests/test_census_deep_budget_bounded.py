import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from tests.census_test_helpers import instrument


class CensusDeepBudgetBoundedTests(unittest.TestCase):
    def test_source_and_llm_budget_present_for_deep(self):
        inst = instrument()
        scan = BaselineScanResult(symbol=inst.symbol, as_of_date="2026-07-01", recent_disclosure_count=5, trigger_priority_score=50)
        decision = decide_depths([inst], [scan], config=CensusDepthPolicyConfig(max_deep_symbols=1, sector_sample_quota=0))[0]
        self.assertGreater(decision.source_task_budget["max_tasks"], 0)
        self.assertIsNotNone(decision.source_task_budget["max_fetches_per_task"])
        self.assertGreaterEqual(decision.llm_budget["max_calls"], 0)


if __name__ == "__main__":
    unittest.main()
