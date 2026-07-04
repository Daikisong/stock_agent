import json
import shutil
import tempfile
import unittest
from pathlib import Path

from e2r.census.census_v4_auditor import audit_census_v4_leaf_artifacts
from e2r.census.census_runner_v4 import _demote_atomic_representatives_replaced_by_brain_stage
from tests.census_v4_test_helpers import census_v4_artifacts, read_json


class CensusV4NonRepresentativeClaimAuditTests(unittest.TestCase):
    def test_non_representative_claims_are_explained_and_do_not_score_leak(self):
        artifacts = census_v4_artifacts()
        audit = read_json(artifacts["output_root"] / "non_representative_claim_audit.json")
        leaf = artifacts["leaf_audit"]

        self.assertEqual(audit["verdict"], "PASS")
        self.assertEqual(audit["critical_count"], 0)
        self.assertEqual(audit["accepted_claim_count"], 106)
        self.assertGreater(audit["representative_stage_claim_count"], 0)
        self.assertGreater(audit["non_representative_claim_count"], 0)
        self.assertEqual(
            audit["representative_stage_claim_count"] + audit["non_representative_claim_count"],
            audit["accepted_claim_count"],
        )
        self.assertEqual(audit["critical_counts"]["non_representative_claim_unreasoned_count"], 0)
        self.assertEqual(audit["critical_counts"]["non_representative_claim_score_leak_count"], 0)
        self.assertGreaterEqual(audit["reason_distribution"].get("non_representative_atomic_decision", 0), 1)
        self.assertEqual(leaf["critical_counts"]["non_representative_claim_audit_failed_count"], 0)
        self.assertEqual(leaf["critical_counts"]["non_representative_claim_score_leak_count"], 0)

    def test_score_leaking_non_representative_claim_fails_leaf_audit(self):
        with _copied_output() as output_root:
            nonrep = read_json(output_root / "non_representative_claim_audit.json")
            leaking_claim = nonrep["sample_non_representative_claims"][0]["claim_id"]
            stage_path = output_root / "census_stage_status.jsonl"
            rows = _read_jsonl(stage_path)
            target = next(row for row in rows if row.get("score_contribution_ids"))
            contribution_id = target["score_contribution_ids"][0]
            contribution_path = output_root / "score_contributions.jsonl"
            contributions = _read_jsonl(contribution_path)
            for contribution in contributions:
                if contribution.get("score_contribution_id") == contribution_id or contribution.get("contribution_id") == contribution_id:
                    contribution.setdefault("support_claim_ids", []).append(leaking_claim)
                    break
            _write_jsonl(contribution_path, contributions)

            from e2r.census.census_runner_v4 import _non_representative_claim_audit

            _write_json(
                output_root / "non_representative_claim_audit.json",
                _non_representative_claim_audit(output_root=output_root, stage_rows=rows),
            )
            audit = audit_census_v4_leaf_artifacts(output_root)

        self.assertGreater(audit["critical_counts"]["non_representative_claim_score_leak_count"], 0)
        self.assertEqual(audit["verdict"], "FAIL")

    def test_brain_promoted_stage_demotes_previous_event_board_representative(self):
        atomic = [
            {
                "atomic_stage_decision_id": "ATOMIC-EVENT",
                "symbol": "001360",
                "is_representative": True,
                "accepted_claim_ids": ["CLM-EVENT"],
            },
            {
                "atomic_stage_decision_id": "ATOMIC-OTHER",
                "symbol": "003090",
                "is_representative": True,
                "accepted_claim_ids": ["CLM-OTHER"],
            },
        ]
        stage_rows = [
            {
                "symbol": "001360",
                "stage_scope": "BRAIN_WEB_PARTIAL",
                "census_stage_status_id": "CSS-BRAIN-UNIT",
                "accepted_claim_ids": ["CLM-BRAIN"],
            }
        ]

        demoted = _demote_atomic_representatives_replaced_by_brain_stage(
            atomic_rows=atomic,
            stage_rows=stage_rows,
        )

        by_id = {row["atomic_stage_decision_id"]: row for row in demoted}
        self.assertFalse(by_id["ATOMIC-EVENT"]["is_representative"])
        self.assertEqual(by_id["ATOMIC-EVENT"]["representative_replaced_by"], "BRAIN_WEB_PARTIAL")
        self.assertTrue(by_id["ATOMIC-OTHER"]["is_representative"])


class _copied_output:
    def __enter__(self) -> Path:
        self._tmp = tempfile.TemporaryDirectory()
        src = census_v4_artifacts()["output_root"]
        self.output_root = Path(self._tmp.name) / "out"
        shutil.copytree(src, self.output_root)
        return self.output_root

    def __exit__(self, exc_type, exc, tb) -> None:
        self._tmp.cleanup()


def _read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
