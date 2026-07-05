import json
import unittest
from pathlib import Path


class ResearchToRuntimeProxyBecomesRepairTaskTests(unittest.TestCase):
    def test_proxy_and_pending_cases_are_repair_tasks_not_score(self) -> None:
        queue = json.loads(Path("docs/operational/research_to_runtime_source_repair_queue_v1.json").read_text())
        self.assertEqual(queue["schema_version"], "e2r_research_to_runtime_source_repair_queue_v1")
        self.assertFalse(queue["source_proxy_score_allowed"])
        self.assertGreater(queue["repair_task_count"], 0)
        for task in queue["tasks"]:
            self.assertIn(task["source_case_quality"], {"SOURCE_PROXY_ONLY", "EVIDENCE_URL_PENDING"})
            self.assertFalse(task["production_score_allowed"])
            self.assertEqual(task["runtime_replay_status"], "SOURCE_REPAIR_REQUIRED")


if __name__ == "__main__":
    unittest.main()
