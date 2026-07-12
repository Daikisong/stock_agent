from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.researcher_mode.audits import (
    PHASE80_ARTIFACT_PATHS,
    PHASE80_PASS,
    compile_phase80_forensics,
    write_phase80_forensics,
)


class E2RV5Phase80ForensicTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.compiled = compile_phase80_forensics(cls.ROOT)

    def test_all_required_scopes_and_six_runtime_lanes_are_audited(self) -> None:
        graph = self.compiled["call_graph"]
        self.assertEqual(graph["status"], PHASE80_PASS)
        self.assertEqual(graph["critical_count_sum"], 0)
        self.assertEqual({row["lane_id"] for row in graph["canonical_lanes"]}, set("ABCDEF"))
        self.assertTrue(all(row["exists"] for row in graph["audit_scope"]))
        self.assertGreater(graph["module_count"], 200)
        self.assertGreater(graph["import_edge_count"], 200)

    def test_parallel_score_authorities_have_file_and_line_lineage(self) -> None:
        audit = self.compiled["parallel_brains"]
        self.assertGreaterEqual(
            audit["production_reachable_parallel_score_authority_count"], 6
        )
        self.assertTrue(all(row["symbol_found"] for row in audit["authorities"]))
        self.assertTrue(all(row["source_line"] for row in audit["authorities"]))
        self.assertEqual(
            audit["canonical_future_architecture"]["canonical_namespace"],
            "e2r.research_brain.researcher_mode",
        )

    def test_score_collapse_root_causes_use_current_leaf_metrics(self) -> None:
        audit = self.compiled["score_collapse"]
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(len(audit["target_baselines"]), 2)
        by_target = {row["target_id"]: row for row in audit["target_baselines"]}
        self.assertEqual(by_target["005930"]["evidence_document_count"], 1)
        self.assertEqual(by_target["000660"]["evidence_document_count"], 2)
        self.assertEqual(by_target["005930"]["full_e2r_score"], 18.159977)
        self.assertEqual(by_target["000660"]["full_e2r_score"], 19.120509)
        self.assertIn("market_mispricing", by_target["005930"]["zero_components"])
        self.assertEqual(
            audit["question_family_budget_summary"][
                "bounded_routes_exhausted_stop_count"
            ],
            13,
        )

    def test_cli_writer_emits_all_four_phase80_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            outputs = write_phase80_forensics(
                repo_root=self.ROOT, output_root=directory
            )
            self.assertEqual(set(outputs), set(PHASE80_ARTIFACT_PATHS))
            for path in outputs.values():
                self.assertTrue(path.is_file())

    def test_committed_artifacts_capture_the_phase80_baseline(self) -> None:
        for key, relative in PHASE80_ARTIFACT_PATHS.items():
            path = self.ROOT / relative
            self.assertTrue(path.is_file(), relative)
            if key == "behavior_diff":
                text = path.read_text(encoding="utf-8")
                self.assertIn("Research vs Runtime Behavior Difference", text)
                self.assertIn("e2r.research_brain.researcher_mode", text)
            else:
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(payload["status"], PHASE80_PASS)
                self.assertEqual(payload["critical_count_sum"], 0)


if __name__ == "__main__":
    unittest.main()
