import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.depth_policy import DepthDecision, DepthLevel
from e2r.census.triage import plan_research_brain, research_brain_output_forbidden_key_count


class CensusResearchBrainTriageTests(unittest.TestCase):
    def test_research_brain_plan_has_no_score_stage_keys(self):
        scan = BaselineScanResult(symbol="005930", as_of_date="2026-07-01", recent_supply_contract_count=1)
        decision = DepthDecision(symbol="005930", recommended_depth=DepthLevel.L3_RESEARCH_BRAIN_TRIAGE, reason="test", source_task_budget={"max_tasks": 1, "max_fetches_per_task": 1})
        plan = plan_research_brain(scan=scan, depth_decision=decision)
        self.assertIsNotNone(plan)
        self.assertEqual(research_brain_output_forbidden_key_count(plan), 0)
        self.assertIn("contract_quality_bridge", plan.must_verify_primitives)


if __name__ == "__main__":
    unittest.main()
