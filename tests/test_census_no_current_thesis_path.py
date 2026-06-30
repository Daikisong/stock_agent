import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.depth_policy import DepthDecision, DepthLevel
from e2r.census.triage import plan_research_brain


class CensusNoCurrentThesisPathTests(unittest.TestCase):
    def test_no_current_thesis_supported(self):
        scan = BaselineScanResult(symbol="005930", as_of_date="2026-07-01")
        decision = DepthDecision(symbol="005930", recommended_depth=DepthLevel.L3_RESEARCH_BRAIN_TRIAGE, reason="audit", source_task_budget={"max_tasks": 1, "max_fetches_per_task": 1})
        plan = plan_research_brain(scan=scan, depth_decision=decision)
        self.assertEqual(plan.status, "NO_CURRENT_THESIS")
        self.assertIn("No current E2R thesis", plan.do_not_promote_reasons[0])


if __name__ == "__main__":
    unittest.main()
