import hashlib
import csv
import unittest
from pathlib import Path

from tests.census_v4_test_helpers import census_v4_artifacts


class CensusV4ArtifactManifestTests(unittest.TestCase):
    def test_manifest_has_hash_size_and_row_count_for_every_leaf(self):
        artifacts = census_v4_artifacts()
        output_root = Path(artifacts["output_root"])
        manifest = artifacts["artifact_manifest"]
        rows = manifest["artifacts"]
        self.assertGreater(len(rows), 30)
        names = {row["name"] for row in rows}
        output_names = {path.name for path in output_root.iterdir() if path.is_file() and path.name != "artifact_manifest.json"}
        self.assertEqual(names, output_names)
        for required in (
            "census_stage_status.jsonl",
            "accepted_claims.jsonl",
            "evidence_claims.jsonl",
            "score_contributions.jsonl",
            "stagecourt_traces.jsonl",
            "claim_to_stage_trace.jsonl",
            "sample_leaf_bundle.jsonl",
            "full_thesis_smoke_tasks.jsonl",
            "full_thesis_refresh_queue.jsonl",
            "full_thesis_seed_materialization_trace.jsonl",
            "full_thesis_seed_materialization_audit.json",
            "full_thesis_refresh_queue_audit.json",
            "full_thesis_production_runner_audit.json",
            "full_thesis_production_audit.json",
            "c06_guard_replay_audit.json",
            "controlled_semantic_replay_audit.json",
            "all_archetype_replay_matrix.json",
            "goal_requirement_matrix_audit.json",
            "leaf_artifact_audit.json",
            "readiness_verdict.json",
            "audit_summary.json",
            "operator_digest.md",
            "acceptance_report.md",
            "report_generation_audit.json",
            "brain_stage_promotion_audit.json",
            "brain_web_readiness_gate_audit.json",
            "brain_claim_mapping_trace.jsonl",
            "claim_to_stage_forensic_audit.json",
            "non_representative_claim_audit.json",
            "source_task_realness_audit.json",
            "existing_ledger_reuse_audit.json",
            "last_effective_thesis_audit.json",
            "source_coverage_audit.json",
            "runtime_plausibility_audit.json",
            "research_brain_v4_bridge_audit.json",
        ):
            self.assertIn(required, names)
        self.assertNotIn("artifact_manifest.json", names)
        for row in rows:
            path = output_root / row["name"]
            content = path.read_bytes()
            self.assertEqual(row["byte_size"], len(content))
            self.assertEqual(row["sha256"], hashlib.sha256(content).hexdigest())
            if path.suffix == ".jsonl":
                self.assertEqual(row["row_count"], sum(1 for line in content.splitlines() if line.strip()))
            elif path.suffix == ".csv":
                with path.open(newline="", encoding="utf-8-sig") as handle:
                    csv_rows = list(csv.reader(handle))
                self.assertEqual(row["row_count"], max(0, len(csv_rows) - 1) if csv_rows else 0)


if __name__ == "__main__":
    unittest.main()
