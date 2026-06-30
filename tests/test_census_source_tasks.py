import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.deep_dossier_scheduler import build_source_tasks
from e2r.census.depth_policy import DepthDecision, DepthLevel
from e2r.census.triage import plan_research_brain


class CensusSourceTasksTests(unittest.TestCase):
    def test_source_tasks_have_budget(self):
        scan = BaselineScanResult(symbol="005930", as_of_date="2026-07-01", recent_supply_contract_count=1)
        decision = DepthDecision(symbol="005930", recommended_depth=DepthLevel.L3_RESEARCH_BRAIN_TRIAGE, reason="test", source_task_budget={"max_tasks": 2, "max_fetches_per_task": 2, "max_retries": 1})
        plan = plan_research_brain(scan=scan, depth_decision=decision)
        tasks = build_source_tasks(plan=plan, depth_decision=decision)
        self.assertTrue(tasks)
        self.assertTrue(all(task.budget for task in tasks))
        self.assertTrue(all(not task.allows_general_web for task in tasks))


if __name__ == "__main__":
    unittest.main()
