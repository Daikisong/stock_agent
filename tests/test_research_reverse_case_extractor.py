import json
import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
