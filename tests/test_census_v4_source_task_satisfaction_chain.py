import json
import tempfile
import unittest
from pathlib import Path

from e2r.census.census_runner_v4 import _source_task_satisfaction_audit
from tests.census_v4_test_helpers import census_v4_artifacts, read_json


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def write_minimal_chain(root: Path, *, source_task_claim: bool = True, anchor_present: bool = True, extra_non_representative: bool = False) -> None:
    root.mkdir(parents=True, exist_ok=True)
    accepted = [
        {
            "claim_id": "CLM-1",
            "symbol": "005930",
            "document_id": "DOC-1",
            "anchor_id": "ANCHOR-1",
            "score_eligible": True,
            "target_scope_status": "DIRECT",
            "temporal_status": "CURRENT",
        }
    ]
    documents = [{"document_id": "DOC-1", "symbol": "005930"}]
    anchors = [{"anchor_id": "ANCHOR-1", "document_id": "DOC-1", "symbol": "005930"}] if anchor_present else []
    contributions = [
        {
            "score_contribution_id": "SCON-1",
            "support_claim_ids": ["CLM-1"],
            "symbol": "005930",
        }
    ]
    traces = [
        {
            "stagecourt_trace_id": "SCT-1",
            "accepted_claim_ids": ["CLM-1"],
            "score_contribution_ids": ["SCON-1"],
            "symbol": "005930",
        }
    ]
    stage_rows = [
        {
            "symbol": "005930",
            "accepted_claim_ids": ["CLM-1"],
            "score_contribution_ids": ["SCON-1"],
            "stagecourt_trace_id": "SCT-1",
            "base_stage": "Stage1",
        }
    ]
    executions = [
        {
            "task_id": "SRC-TASK-1",
            "symbol": "005930",
            "status": "EVIDENCE_OS_ACCEPTED",
            "accepted_claim_ids": ["CLM-1"] if source_task_claim else [],
            "score_claim_ids": ["CLM-1"] if source_task_claim else [],
            "fetched_document_ids": ["DOC-1"],
        }
    ]

    if extra_non_representative:
        accepted.append(
            {
                "claim_id": "CLM-2",
                "symbol": "000660",
                "document_id": "DOC-2",
                "anchor_id": "ANCHOR-2",
                "score_eligible": True,
                "target_scope_status": "DIRECT",
                "temporal_status": "CURRENT",
            }
        )
        documents.append({"document_id": "DOC-2", "symbol": "000660"})
        anchors.append({"anchor_id": "ANCHOR-2", "document_id": "DOC-2", "symbol": "000660"})
        contributions.append({"score_contribution_id": "SCON-2", "support_claim_ids": ["CLM-2"], "symbol": "000660"})
        traces.append(
            {
                "stagecourt_trace_id": "SCT-2",
                "accepted_claim_ids": ["CLM-2"],
                "score_contribution_ids": ["SCON-2"],
                "symbol": "000660",
            }
        )
        executions.append(
            {
                "task_id": "SRC-TASK-2",
                "symbol": "000660",
                "status": "EVIDENCE_OS_ACCEPTED",
                "accepted_claim_ids": ["CLM-2"],
                "score_claim_ids": ["CLM-2"],
                "fetched_document_ids": ["DOC-2"],
            }
        )

    write_jsonl(root / "source_task_executions.jsonl", executions)
    write_jsonl(root / "accepted_claims.jsonl", accepted)
    write_jsonl(root / "evidence_documents.jsonl", documents)
    write_jsonl(root / "evidence_anchors.jsonl", anchors)
    write_jsonl(root / "score_contributions.jsonl", contributions)
    write_jsonl(root / "stagecourt_traces.jsonl", traces)
    write_jsonl(root / "census_stage_status.jsonl", stage_rows)


class CensusV4SourceTaskSatisfactionChainTests(unittest.TestCase):
    def test_current_artifact_has_closed_representative_source_task_chain(self):
        root = census_v4_artifacts()["output_root"]
        audit = read_json(root / "source_task_satisfaction_audit.json")

        self.assertEqual(audit["schema_version"], "e2r_census_v4_source_task_satisfaction_audit_v2")
        self.assertEqual(audit["verdict"], "PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION")
        self.assertEqual(audit["critical_count"], 0)
        self.assertEqual(audit["representative_score_claim_count"], 79)
        self.assertEqual(audit["source_task_chain_closed_to_representative_stage_count"], 79)
        self.assertEqual(audit["warning_counts"]["non_representative_source_task_claim_count"], 27)

    def test_representative_score_claim_without_source_task_execution_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_chain(root, source_task_claim=False)

            audit = _source_task_satisfaction_audit(root)

        self.assertEqual(audit["verdict"], "FAIL")
        self.assertEqual(audit["critical_counts"]["representative_score_claim_without_source_task_execution_count"], 1)

    def test_representative_score_claim_missing_anchor_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_chain(root, anchor_present=False)

            audit = _source_task_satisfaction_audit(root)

        self.assertEqual(audit["verdict"], "FAIL")
        self.assertEqual(audit["critical_counts"]["representative_score_claim_missing_anchor_row_count"], 1)

    def test_non_representative_source_task_claim_is_warning_not_proof(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_chain(root, extra_non_representative=True)

            audit = _source_task_satisfaction_audit(root)

        self.assertEqual(audit["verdict"], "PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION")
        self.assertEqual(audit["critical_count"], 0)
        self.assertEqual(audit["warning_counts"]["non_representative_source_task_claim_count"], 1)
        self.assertEqual(audit["source_task_chain_closed_to_stagecourt_count"], 2)
        self.assertEqual(audit["source_task_chain_closed_to_representative_stage_count"], 1)


if __name__ == "__main__":
    unittest.main()
