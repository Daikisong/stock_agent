import json
import unittest
from pathlib import Path

from e2r.research_reverse.research_file_scanner import scan_research_files


class ResearchReverseCaseExtractorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path("docs/operational")
        cls.inventory = json.loads((cls.root / "research_reverse_case_inventory.json").read_text(encoding="utf-8"))
        cls.coverage = json.loads((cls.root / "research_reverse_archetype_coverage_matrix.json").read_text(encoding="utf-8"))

    def test_research_case_inventory_has_documented_large_corpus(self) -> None:
        self.assertEqual(self.inventory["schema_version"], "e2r_research_reverse_case_inventory_v1")
        self.assertGreater(self.inventory["record_count"], 1000)
        self.assertGreater(self.inventory["documented_corpus_size"], 1000)
        self.assertEqual(self.inventory["archetype_count"], 36)

    def test_every_record_has_source_quality_and_never_changes_production_score(self) -> None:
        for record in self.inventory["records"][:500]:
            self.assertIn(record["source_quality"], self.inventory["source_quality_counts"])
            self.assertFalse(record["production_scoring_changed"])
            self.assertFalse(record["runtime_score_eligible"])

    def test_every_registered_archetype_has_pattern_summary_or_explicit_gap(self) -> None:
        self.assertEqual(self.coverage["schema_version"], "e2r_research_reverse_archetype_coverage_matrix_v1")
        self.assertEqual(self.coverage["archetype_count"], 36)
        self.assertEqual(len(self.coverage["rows"]), 36)
        for row in self.coverage["rows"]:
            self.assertTrue(row["has_pattern_summary"] or row["source_gap"], row["archetype_id"])

    def test_mandatory_archetypes_have_research_patterns(self) -> None:
        by_prefix = {row["archetype_id"].split("_", 1)[0]: row for row in self.coverage["rows"]}
        for prefix in ("C06", "C08", "C15", "C17", "C24", "C28"):
            row = by_prefix[prefix]
            self.assertGreater(row["record_count"], 0, prefix)
            self.assertGreater(row["url_backed_case_count"] + row["source_proxy_only_case_count"], 0, prefix)

    def test_generated_goal4_status_artifacts_are_not_reingested_as_research(self) -> None:
        files = {path.as_posix() for path in scan_research_files(Path("."))}
        self.assertNotIn("docs/operational/all_archetype_runtime_status_matrix_2026-07-05.md", files)
        self.assertNotIn("docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json", files)
        self.assertNotIn("docs/operational/all_archetype_runtime_status_matrix.json", files)
        self.assertNotIn("docs/operational/all_archetype_runtime_parity_matrix.json", files)
        self.assertNotIn("docs/operational/all_archetype_runtime_parity_summary.md", files)
        self.assertNotIn("docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.md", files)
        self.assertNotIn("docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.json", files)
        self.assertNotIn("docs/operational/all_archetype_next_runtime_attempt_plan.json", files)
        self.assertNotIn("docs/operational/all_archetype_next_runtime_source_tasks_2026-07-05.jsonl", files)
        self.assertNotIn("docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl", files)
        self.assertNotIn("docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.md", files)
        self.assertNotIn("docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.json", files)
        self.assertNotIn("docs/operational/all_archetype_runtime_execution_manifest.json", files)
        self.assertNotIn("docs/operational/source_lineage_repair_audit.json", files)
        self.assertNotIn("docs/operational/source_lineage_repair_audit_2026-07-05.json", files)
        self.assertNotIn("docs/operational/source_lineage_repair_audit_2026-07-05.md", files)
        self.assertNotIn("docs/0705/goal4_research_to_runtime_status_2026-07-05.md", files)
        self.assertNotIn("docs/0705/goal4_manifest_runtime_attempt_patched_v2_final_audit_2026-07-05.md", files)
        self.assertNotIn("docs/0705/goal4_research_memory_target_materialization_plan_2026-07-05.md", files)
        self.assertNotIn("docs/0705/goal4_source_lineage_repair_audit_2026-07-08.md", files)


if __name__ == "__main__":
    unittest.main()
