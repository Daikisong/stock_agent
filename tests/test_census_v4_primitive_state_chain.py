import json
import tempfile
import unittest
from pathlib import Path

from e2r.census.census_runner_v4 import _primitive_state_chain_audit
from tests.census_v4_test_helpers import census_v4_artifacts, read_json


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def write_minimal_primitive_chain(
    root: Path,
    *,
    primitive_present: bool = True,
    stage_primitive_ref: bool = True,
    mapping_present: bool = True,
    accepted_claim_primitive: str = "contract_quality",
    primitive_state_primitive: str = "contract_quality",
    brain_mapping_trace_rows: list[dict] | None = None,
) -> None:
    root.mkdir(parents=True, exist_ok=True)
    primitive_ids = ["PRIM-1"] if stage_primitive_ref else []
    write_jsonl(
        root / "accepted_claims.jsonl",
        [
            {
                "claim_id": "CLM-1",
                "symbol": "005930",
                "primitive_id": accepted_claim_primitive,
                "mapping_status": "ACCEPTED",
                "score_eligible": True,
            }
        ],
    )
    write_jsonl(
        root / "primitive_states.jsonl",
        [
            {
                "primitive_state_id": "PRIM-1",
                "symbol": "005930",
                "primitive_id": primitive_state_primitive,
                "status": "PRESENT_CURRENT",
                "support_claim_ids": ["CLM-1"],
                "counter_claim_ids": [],
            }
        ]
        if primitive_present
        else [],
    )
    write_jsonl(
        root / "primitive_mappings.jsonl",
        [
            {
                "mapping_id": "MAP-1",
                "symbol": "005930",
                "accepted_claim_ids": ["CLM-1"],
                "primitive_state_ids": ["PRIM-1"],
                "score_contribution_ids": ["SCON-1"],
                "primitive_ids": [primitive_state_primitive],
            }
        ]
        if mapping_present
        else [],
    )
    write_jsonl(
        root / "score_contributions.jsonl",
        [
            {
                "score_contribution_id": "SCON-1",
                "symbol": "005930",
                "support_claim_ids": ["CLM-1"],
                "mapping_ids": ["MAP-1"],
            }
        ],
    )
    write_jsonl(root / "brain_claim_mapping_trace.jsonl", brain_mapping_trace_rows or [])
    write_jsonl(
        root / "atomic_stage_decisions.jsonl",
        [
            {
                "atomic_stage_decision_id": "ATOMIC-1",
                "symbol": "005930",
                "accepted_claim_ids": ["CLM-1"],
                "score_contribution_ids": ["SCON-1"],
                "primitive_state_ids": primitive_ids,
            }
        ],
    )
    write_jsonl(
        root / "stagecourt_traces.jsonl",
        [
            {
                "stagecourt_trace_id": "SCT-1",
                "symbol": "005930",
                "accepted_claim_ids": ["CLM-1"],
                "score_contribution_ids": ["SCON-1"],
            }
        ],
    )
    write_jsonl(
        root / "census_stage_status.jsonl",
        [
            {
                "symbol": "005930",
                "accepted_claim_ids": ["CLM-1"],
                "score_contribution_ids": ["SCON-1"],
                "primitive_state_ids": primitive_ids,
                "atomic_stage_decision_id": "ATOMIC-1",
                "score_scale": "EVENT_WEIGHTED_PARTIAL",
            }
        ],
    )


class CensusV4PrimitiveStateChainTests(unittest.TestCase):
    def test_current_artifact_has_closed_representative_primitive_chain(self):
        root = census_v4_artifacts()["output_root"]
        audit = read_json(root / "primitive_state_chain_audit.json")

        self.assertEqual(audit["schema_version"], "e2r_census_v4_primitive_state_chain_audit_v1")
        self.assertEqual(audit["verdict"], "PASS")
        self.assertEqual(audit["critical_count"], 0)
        self.assertEqual(audit["representative_score_claim_count"], 79)
        self.assertEqual(audit["representative_score_claim_with_primitive_state_count"], 79)
        self.assertEqual(audit["primitive_mapping_count"], 106)
        self.assertTrue(audit["mapping_leaf_resolution_supported"])

    def test_representative_score_claim_without_primitive_state_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_primitive_chain(root, primitive_present=False, stage_primitive_ref=False)

            audit = _primitive_state_chain_audit(root)

        self.assertEqual(audit["verdict"], "FAIL")
        self.assertEqual(audit["critical_counts"]["representative_score_claim_without_primitive_state_count"], 1)
        self.assertEqual(audit["critical_counts"]["representative_stage_row_missing_primitive_state_ids_count"], 1)

    def test_stage_primitive_ref_must_match_atomic_decision(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_primitive_chain(root, primitive_present=True, stage_primitive_ref=False)

            audit = _primitive_state_chain_audit(root)

        self.assertEqual(audit["verdict"], "FAIL")
        self.assertEqual(audit["critical_counts"]["representative_stage_row_missing_primitive_state_ids_count"], 1)
        self.assertEqual(audit["critical_counts"]["atomic_decision_primitive_set_mismatch_count"], 0)

    def test_score_mapping_id_without_mapping_leaf_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_primitive_chain(root, mapping_present=False)

            audit = _primitive_state_chain_audit(root)

        self.assertEqual(audit["verdict"], "FAIL")
        self.assertEqual(audit["critical_counts"]["representative_score_mapping_id_not_found_count"], 1)

    def test_multi_mapping_claim_can_support_each_accepted_primitive_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_primitive_chain(
                root,
                accepted_claim_primitive="delivery_schedule",
                primitive_state_primitive="contract_duration_months",
                brain_mapping_trace_rows=[
                    {
                        "claim_id": "CLM-1",
                        "symbol": "005930",
                        "accepted": True,
                        "mapping_status": "ACCEPTED",
                        "primitive_id": "contract_duration_months",
                        "primitive_state_ids": ["PRIM-1"],
                    }
                ],
            )

            audit = _primitive_state_chain_audit(root)

        self.assertEqual(audit["verdict"], "PASS")
        self.assertEqual(audit["critical_counts"]["primitive_state_claim_primitive_mismatch_count"], 0)
        self.assertEqual(audit["claim_with_multi_accepted_primitive_count"], 1)

    def test_accepted_primitive_summary_does_not_prove_state_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_primitive_chain(
                root,
                accepted_claim_primitive="delivery_schedule",
                primitive_state_primitive="contract_duration_months",
                brain_mapping_trace_rows=[
                    {
                        "claim_id": "CLM-1",
                        "symbol": "005930",
                        "accepted": True,
                        "mapping_status": "ACCEPTED",
                        "primitive_id": "delivery_schedule",
                        "accepted_primitive_ids": ["contract_duration_months"],
                        "primitive_state_ids": ["PRIM-1"],
                    }
                ],
            )

            audit = _primitive_state_chain_audit(root)

        self.assertEqual(audit["verdict"], "FAIL")
        self.assertEqual(audit["critical_counts"]["primitive_state_claim_primitive_mismatch_count"], 1)

    def test_brain_mapping_trace_must_reference_same_primitive_state_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_primitive_chain(
                root,
                accepted_claim_primitive="delivery_schedule",
                primitive_state_primitive="contract_duration_months",
                brain_mapping_trace_rows=[
                    {
                        "claim_id": "CLM-1",
                        "symbol": "005930",
                        "accepted": True,
                        "mapping_status": "ACCEPTED",
                        "primitive_id": "contract_duration_months",
                        "primitive_state_ids": ["PRIM-OTHER"],
                    }
                ],
            )

            audit = _primitive_state_chain_audit(root)

        self.assertEqual(audit["verdict"], "FAIL")
        self.assertEqual(audit["critical_counts"]["primitive_state_claim_primitive_mismatch_count"], 1)

    def test_brain_mapping_trace_symbol_must_match_state_symbol(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_primitive_chain(
                root,
                accepted_claim_primitive="delivery_schedule",
                primitive_state_primitive="contract_duration_months",
                brain_mapping_trace_rows=[
                    {
                        "claim_id": "CLM-1",
                        "symbol": "000660",
                        "accepted": True,
                        "mapping_status": "ACCEPTED",
                        "primitive_id": "contract_duration_months",
                        "primitive_state_ids": ["PRIM-1"],
                    }
                ],
            )

            audit = _primitive_state_chain_audit(root)

        self.assertEqual(audit["verdict"], "FAIL")
        self.assertEqual(audit["critical_counts"]["primitive_state_claim_primitive_mismatch_count"], 1)

    def test_state_primitive_without_accepted_mapping_still_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_primitive_chain(
                root,
                accepted_claim_primitive="delivery_schedule",
                primitive_state_primitive="contract_duration_months",
            )

            audit = _primitive_state_chain_audit(root)

        self.assertEqual(audit["verdict"], "FAIL")
        self.assertEqual(audit["critical_counts"]["primitive_state_claim_primitive_mismatch_count"], 1)


if __name__ == "__main__":
    unittest.main()
