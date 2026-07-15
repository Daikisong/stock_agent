from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    CANARY_MASTER_LEAF_FILES,
    canary_output_tree_hash,
    materialize_canary_checkpoint_leaves,
    refresh_canary_target_manifest_hash,
    write_canary_post_run_gold_comparison,
)


class E2RV5CanaryLeafContractTests(unittest.TestCase):
    TARGET_ID = "CURRENT-TARGET"
    AS_OF_DATE = "2026-06-29"

    def test_exact_master_leaf_roster_is_canonical(self) -> None:
        self.assertEqual(
            tuple(CANARY_MASTER_LEAF_FILES.values()),
            (
                "research_epochs.jsonl",
                "query_ledger.jsonl",
                "source_graph.jsonl",
                "documents.jsonl",
                "evidence_facts.jsonl",
                "counterfacts.jsonl",
                "component_research_memos.jsonl",
                "component_judge_decisions.jsonl",
                "historical_anchor_comparisons.jsonl",
                "final_component_decisions.jsonl",
                "score_vector.json",
                "atomic_stage_decision.json",
                "stagecourt_trace.json",
                "gold_fact_comparison.jsonl",
            ),
        )

    def test_pending_checkpoint_materializes_exact_leaves_without_score_invention(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_pending_sources(root)
            write_json(
                root / "target_run_manifest.json",
                {
                    "target_id": self.TARGET_ID,
                    "as_of_date": self.AS_OF_DATE,
                    "status": "RESEARCH_CHECKPOINT_PENDING",
                    "production_research_complete": False,
                    "output_tree_hash": "STALE",
                },
            )
            audit = materialize_canary_checkpoint_leaves(
                root,
                target_id=self.TARGET_ID,
                as_of_date=self.AS_OF_DATE,
                production_research_complete=False,
                refresh_target_manifest=True,
            )

            self.assertEqual(audit["critical_count_sum"], 0)
            self.assertEqual(audit["status"], "CANARY_LEAF_CONTRACT_PASS")
            for key, filename in CANARY_MASTER_LEAF_FILES.items():
                if key == "gold_fact_comparison":
                    self.assertFalse((root / filename).exists())
                else:
                    self.assertTrue((root / filename).is_file(), filename)
            score = json.loads((root / "score_vector.json").read_text(encoding="utf-8"))
            self.assertFalse(score["score_valid"])
            self.assertIsNone(score["component_score_vector"])
            self.assertIsNone(score["total_points"])
            self.assertFalse(score["production_stage_authority"])
            manifest = json.loads(
                (root / "target_run_manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(manifest["output_tree_hash"], canary_output_tree_hash(root))
            self.assertEqual(
                manifest["canary_leaf_contract"]["status"],
                "CANARY_LEAF_CONTRACT_PASS",
            )

    def test_post_run_gold_is_target_scoped_and_never_premature(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_pending_sources(root)
            materialize_canary_checkpoint_leaves(
                root,
                target_id=self.TARGET_ID,
                as_of_date=self.AS_OF_DATE,
                production_research_complete=False,
            )
            self.assertFalse((root / "gold_fact_comparison.jsonl").exists())

            rows = (
                {
                    "target_id": self.TARGET_ID,
                    "gold_fact_id": "G-1",
                    "production_fact_id": "P-1",
                    "semantic_match": True,
                },
            )
            audit = write_canary_post_run_gold_comparison(
                root,
                target_id=self.TARGET_ID,
                as_of_date=self.AS_OF_DATE,
                comparison_rows=rows,
                refresh_target_manifest=False,
            )
            self.assertEqual(audit["critical_count_sum"], 0)
            self.assertEqual(self._jsonl(root / "gold_fact_comparison.jsonl"), rows)

            with self.assertRaises(ValueError):
                write_canary_post_run_gold_comparison(
                    root,
                    target_id=self.TARGET_ID,
                    as_of_date=self.AS_OF_DATE,
                    comparison_rows=({"target_id": "OTHER", "gold_fact_id": "G-X"},),
                    refresh_target_manifest=False,
                )

            premature = materialize_canary_checkpoint_leaves(
                root,
                target_id=self.TARGET_ID,
                as_of_date=self.AS_OF_DATE,
                production_research_complete=False,
            )
            self.assertEqual(
                premature["critical_counts"]["premature_gold_comparison_count"],
                1,
            )

    def test_runner_progress_leaf_rebinds_manifest_tree_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_pending_sources(root)
            write_json(
                root / "target_run_manifest.json",
                {
                    "target_id": self.TARGET_ID,
                    "output_tree_hash": "BEFORE_PROGRESS",
                },
            )
            write_json(
                root / "until_pass_progress.json",
                {
                    "target_id": self.TARGET_ID,
                    "status": "RESEARCH_CHECKPOINT_PENDING",
                },
            )

            self.assertTrue(refresh_canary_target_manifest_hash(root))
            manifest = json.loads(
                (root / "target_run_manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                manifest["output_tree_hash"], canary_output_tree_hash(root)
            )

    def test_missing_atomic_stage_leaf_keeps_contract_pending(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_pending_sources(root)
            (root / "stagecourt_trace.json").unlink()
            audit = materialize_canary_checkpoint_leaves(
                root,
                target_id=self.TARGET_ID,
                as_of_date=self.AS_OF_DATE,
                production_research_complete=False,
            )
            self.assertEqual(audit["status"], "CANARY_LEAF_CONTRACT_PENDING")
            self.assertEqual(
                audit["critical_counts"]["checkpoint_leaf_missing_count"],
                1,
            )

    def _write_pending_sources(self, root: Path) -> None:
        write_json(
            root / "research_epoch_checkpoint.json",
            {
                "checkpoint_id": "EPOCH-1",
                "target_id": self.TARGET_ID,
                "as_of_date": self.AS_OF_DATE,
                "epoch": 1,
                "status": "NEXT_RESEARCH_REQUIRED",
            },
        )
        write_json(
            root / "source_graph.json",
            {
                "checkpoint_required": True,
                "covered_source_families": ["ISSUER_IR"],
                "open_objectives": ["OBJ-1"],
                "score_authority": False,
                "nodes": [{"node_id": "NODE-1", "node_type": "DOCUMENT"}],
                "edges": [
                    {
                        "edge_id": "EDGE-1",
                        "from_node_id": "NODE-1",
                        "to_node_id": "NODE-1",
                        "relationship": "SELF_TEST",
                    }
                ],
            },
        )
        write_json(
            root / "deterministic_total_score.json",
            {
                "schema_version": "e2r_total_aggregation_result_v2",
                "status": "RESEARCH_REQUIRED",
                "score": None,
                "pending_reasons": ["SEVEN_COMPONENT_RESEARCH_PENDING"],
                "production_stage_authority": False,
            },
        )
        mirrors = {
            "generated_queries.jsonl": (
                {"query_id": "Q-1", "literal_query": "provider generated query"},
            ),
            "source_graph_evidence_documents.jsonl": (
                {
                    "document_id": "DOC-1",
                    "target_id": self.TARGET_ID,
                    "as_of_date": self.AS_OF_DATE,
                },
            ),
            "judge_decisions.jsonl": (),
            "anchor_comparisons.jsonl": (),
            "component_decisions.jsonl": (
                {"component_id": "earnings_visibility", "status": "PENDING"},
            ),
        }
        for filename, rows in mirrors.items():
            write_jsonl(root / filename, rows)
        for filename in (
            "evidence_facts.jsonl",
            "counterfacts.jsonl",
            "component_research_memos.jsonl",
        ):
            write_jsonl(root / filename, ())
        write_json(
            root / "atomic_stage_decision.json",
            {
                "target_id": self.TARGET_ID,
                "as_of_date": self.AS_OF_DATE,
                "status": "RESEARCH_IN_PROGRESS",
                "score_valid": False,
                "canonical_stage": None,
            },
        )
        write_json(
            root / "stagecourt_trace.json",
            {
                "target_id": self.TARGET_ID,
                "as_of_date": self.AS_OF_DATE,
                "status": "RESEARCH_IN_PROGRESS",
                "score_valid": False,
            },
        )

    @staticmethod
    def _jsonl(path: Path) -> tuple[dict, ...]:
        return tuple(
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )


if __name__ == "__main__":
    unittest.main()
