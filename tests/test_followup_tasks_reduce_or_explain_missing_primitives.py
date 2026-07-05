import json
import unittest
from pathlib import Path


class FollowupTasksReduceOrExplainMissingPrimitivesTests(unittest.TestCase):
    def test_followup_tasks_have_success_condition_or_pending_source_fallback(self) -> None:
        audit = json.loads(Path("docs/operational/research_memory_followup_task_audit.json").read_text(encoding="utf-8"))
        for task in audit["tasks"]:
            self.assertIn("accepted current direct claim", task["success_condition"])
            self.assertIn(task["fallback_if_not_found"], {"PENDING_SOURCE", "THESIS_NOT_SUPPORTED", "SOURCE_REPAIR_REQUIRED"})
            self.assertEqual(task["expected_claim_schema"]["primitive_id"], task["missing_primitive"])


if __name__ == "__main__":
    unittest.main()
