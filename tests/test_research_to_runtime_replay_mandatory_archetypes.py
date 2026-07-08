import json
import unittest
from pathlib import Path


class ResearchToRuntimeReplayMandatoryArchetypesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.matrix = json.loads(Path("docs/operational/research_to_runtime_replay_matrix_v1.json").read_text())
        cls.by_prefix = {row["archetype_id"].split("_", 1)[0]: row for row in cls.matrix["rows"]}

    def test_mandatory_archetype_replay_matrix_exists(self) -> None:
        self.assertEqual(self.matrix["schema_version"], "e2r_research_to_runtime_replay_matrix_v1")
        self.assertEqual(self.matrix["mandatory_archetype_count"], 6)
        self.assertEqual(set(self.by_prefix), {"C06", "C08", "C15", "C17", "C24", "C28"})
        self.assertEqual(self.matrix["production_score_leak_count"], 0)
        self.assertTrue(self.matrix["all_source_proxy_cases_planning_only"])

    def test_each_mandatory_archetype_has_positive_guard_proxy_and_lifecycle_status(self) -> None:
        for prefix, row in self.by_prefix.items():
            self.assertEqual(row["positive_runtime_replay_status"], "ACCEPTED_CLAIM_CREATED", prefix)
            self.assertEqual(row["guard_runtime_replay_status"], "ACCEPTED_CLAIM_CREATED", prefix)
            self.assertTrue(row["source_proxy_repair_required"], prefix)
            self.assertGreater(len(row["source_proxy_repair_task_ids"]), 0, prefix)
            self.assertIn(
                row["current_lifecycle_validation_status"],
                {
                    "CURRENT_PRODUCTION_FULL_THESIS_AVAILABLE",
                    "CURRENT_PRODUCTION_CANDIDATE_BLOCKED",
                    "LIFECYCLE_NOT_CURRENT",
                },
                prefix,
            )
            self.assertFalse(row["production_score_evidence_allowed"], prefix)
            if prefix in {"C17"}:
                self.assertEqual(row["runtime_full_thesis_row_count"], 1, prefix)
            else:
                self.assertEqual(row["runtime_full_thesis_row_count"], 0, prefix)

    def test_c06_is_replay_and_blocked_production_not_smoke_substitution(self) -> None:
        c06 = self.by_prefix["C06"]
        self.assertEqual(c06["positive_runtime_replay_status"], "ACCEPTED_CLAIM_CREATED")
        self.assertEqual(c06["current_lifecycle_validation_status"], "CURRENT_PRODUCTION_CANDIDATE_BLOCKED")
        self.assertEqual(c06["runtime_parity_status"], "FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP")
        self.assertFalse(c06["production_score_evidence_allowed"])
        self.assertEqual(c06["runtime_full_thesis_row_count"], 0)


if __name__ == "__main__":
    unittest.main()
