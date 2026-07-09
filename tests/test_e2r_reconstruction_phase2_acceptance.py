from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.compiler import discover_historical_research_paths


REPO_ROOT = Path(__file__).resolve().parents[1]


class E2RReconstructionPhase2AcceptanceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.acceptance_path = REPO_ROOT / "e2r_reconstruction_phase2_acceptance.json"
        self.payload = json.loads(self.acceptance_path.read_text(encoding="utf-8"))

    def test_phase2_acceptance_is_scoped_and_not_runtime_ready(self) -> None:
        self.assertEqual(self.payload["phase"], 2)
        self.assertEqual(
            self.payload["status"],
            "RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS",
        )
        self.assertFalse(self.payload["production_runtime_ready"])
        self.assertNotIn("MEANINGFUL_E2R_RUNTIME_READY", self.acceptance_path.read_text())

    def test_full_registry_was_compiled(self) -> None:
        source = self.payload["source_registry"]
        self.assertEqual(source["registry_row_count"], 2260)
        self.assertEqual(source["compiled_artifact_count"], 2260)
        result = self.payload["full_corpus_result"]
        self.assertGreater(result["structured_row_count"], 100000)
        self.assertGreater(result["historical_case_count"], 10000)
        self.assertGreater(result["historical_outcome_count"], result["historical_case_count"])
        self.assertGreater(result["historical_rule_count"], 5000)
        self.assertEqual(len(discover_historical_research_paths(REPO_ROOT)), 2260)

    def test_every_phase2_hard_acceptance_is_zero_or_exact(self) -> None:
        acceptance = self.payload["hard_acceptance"]
        self.assertEqual(acceptance["valid_structured_jsonl_row_preservation_rate"], 1.0)
        self.assertIsNone(acceptance["source_text_truncation_limit"])
        for key, value in acceptance.items():
            if key in {
                "valid_structured_jsonl_row_preservation_rate",
                "source_text_truncation_limit",
            }:
                continue
            self.assertEqual(value, 0, key)

    def test_golden_corpus_covers_all_required_cases(self) -> None:
        golden = self.payload["golden_corpus"]
        self.assertEqual(golden["mandatory_case_count"], 6)
        self.assertEqual(golden["registry_sample_case_count"], 36)
        self.assertEqual(golden["canonical_archetype_coverage"], "36/36")
        self.assertEqual(len(golden["mandatory_archetypes"]), 6)

    def test_phase2_operational_report_exists(self) -> None:
        report = REPO_ROOT / "docs" / "operational" / "e2r_reconstruction_phase2_corpus_compiler.md"
        text = report.read_text(encoding="utf-8")
        self.assertIn("RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS", text)
        self.assertIn("URL_PRESENT_UNVERIFIED", text)
        self.assertIn("Phase 3", text)


if __name__ == "__main__":
    unittest.main()
