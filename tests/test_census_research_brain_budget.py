import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.depth_policy import DepthDecision, DepthLevel
from e2r.census.triage import plan_research_brain


class CensusResearchBrainBudgetTests(unittest.TestCase):
    def test_l1_depth_does_not_call_research_brain(self):
        scan = BaselineScanResult(symbol="005930", as_of_date="2026-07-01")
        decision = DepthDecision(symbol="005930", recommended_depth=DepthLevel.L1_CHEAP_BASELINE, reason="low")
        self.assertIsNone(plan_research_brain(scan=scan, depth_decision=decision))


if __name__ == "__main__":
    unittest.main()
