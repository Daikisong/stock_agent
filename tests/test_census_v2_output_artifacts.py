import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2OutputArtifactsTests(unittest.TestCase):
    def test_required_artifacts_exist(self):
        root = census_v2_artifacts()["output_root"]
        required = [
            "run_metadata.json",
            "self_repair_log.json",
            "universe.jsonl",
            "census_assessment_events.jsonl",
            "source_timelines.jsonl",
            "last_effective_thesis_states.jsonl",
            "baseline_inputs_summary.json",
            "baseline_scan_results.jsonl",
            "census_events.jsonl",
            "source_tasks.jsonl",
            "source_task_executions.jsonl",
            "evidence_documents.jsonl",
            "evidence_anchors.jsonl",
            "raw_assertions.jsonl",
            "adjudicated_claims.jsonl",
            "accepted_claims.jsonl",
            "primitive_states.jsonl",
            "score_contributions.jsonl",
            "stagecourt_traces.jsonl",
            "census_stage_status.jsonl",
            "census_stage_map.csv",
            "census_stage_summary.json",
            "audit_summary.json",
        ]
        for name in required:
            self.assertTrue((root / name).exists(), name)


if __name__ == "__main__":
    unittest.main()
