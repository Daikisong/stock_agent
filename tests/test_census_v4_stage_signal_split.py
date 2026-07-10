import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tests.census_v4_test_helpers import by_symbol, census_v4_artifacts
from e2r.census.atomic_stage_decision import canonical_stage_for_display
from e2r.census.census_v4_auditor import audit_census_v4_leaf_artifacts
from e2r.census.census_runner_v4 import _with_operator_scope_aliases


class CensusV4StageSignalSplitTests(unittest.TestCase):
    def test_canonical_stage_mapping_covers_display_labels(self):
        self.assertEqual(canonical_stage_for_display("Stage0"), "0")
        self.assertEqual(canonical_stage_for_display("Stage1"), "1")
        self.assertEqual(canonical_stage_for_display("Stage2-Watch"), "2")
        self.assertEqual(canonical_stage_for_display("Stage2-Actionable"), "2")
        self.assertEqual(canonical_stage_for_display("Stage3-Yellow"), "3-Yellow")
        self.assertEqual(canonical_stage_for_display("Stage3-Green"), "3-Green")
        self.assertEqual(canonical_stage_for_display("Red"), "3-Red")
        self.assertEqual(canonical_stage_for_display("Reject"), "3-Red")

    def test_canonical_stage_is_separate_from_display_stage_label(self):
        artifacts = census_v4_artifacts()
        audit = artifacts["leaf_audit"]
        self.assertEqual(audit["critical_counts"]["canonical_stage_invalid_count"], 0)
        self.assertEqual(audit["critical_counts"]["canonical_stage_display_label_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_scope_missing_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_scope_invalid_count"], 0)
        self.assertEqual(audit["critical_counts"]["full_thesis_stage_without_full_thesis_scope_count"], 0)
        self.assertEqual(audit["metrics"]["stage_scope_distribution"]["FULL_THESIS"], 2)
        self.assertEqual(audit["metrics"]["stage_scope_distribution"]["CENSUS_EVENT_BOARD"], len(artifacts["stage_rows"]) - 2)
        allowed = {"0", "1", "2", "3-Green", "3-Yellow", "3-Red", "4A", "4B", "4C", "5"}
        for row in artifacts["stage_rows"]:
            self.assertIn(row["canonical_stage"], allowed)
            self.assertIn(row["stage_scope"], {"CENSUS_EVENT_BOARD", "FULL_THESIS"})
            if row["base_stage"] == "Stage2-Watch":
                self.assertEqual(row["canonical_stage"], "2")
            if row["base_stage"] == "Red":
                self.assertEqual(row["canonical_stage"], "3-Red")

    def test_operator_scope_aliases_make_event_board_stage_labels_explicit(self):
        artifacts = census_v4_artifacts()
        audit = artifacts["leaf_audit"]
        self.assertEqual(audit["critical_counts"]["operator_scope_alias_missing_count"], 0)
        self.assertEqual(audit["critical_counts"]["event_board_operator_alias_unscoped_count"], 0)
        self.assertEqual(audit["critical_counts"]["non_full_thesis_operator_use_overclaim_count"], 0)
        self.assertEqual(audit["critical_counts"]["non_full_e2r_operator_score_overclaim_count"], 0)
        self.assertNotIn("FULL_THESIS_STAGE", audit["metrics"]["operator_stage_use_distribution"])
        self.assertEqual(audit["metrics"]["operator_stage_use_distribution"]["SMOKE_ONLY_STAGE_NOT_PRODUCTION"], 2)
        self.assertEqual(audit["metrics"]["operator_stage_use_distribution"]["NOT_FULL_THESIS_STAGE"], len(artifacts["stage_rows"]) - 2)
        self.assertNotIn("FULL_E2R_SCORE", audit["metrics"]["operator_score_use_distribution"])
        self.assertEqual(audit["metrics"]["operator_score_use_distribution"]["SMOKE_ONLY_SCORE_NOT_PRODUCTION"], 2)
        self.assertEqual(audit["metrics"]["operator_score_use_distribution"]["NOT_FULL_E2R_SCORE"], len(artifacts["stage_rows"]) - 2)
        for row in artifacts["stage_rows"]:
            if row["stage_scope"] == "FULL_THESIS":
                self.assertEqual(row["operator_stage_use"], "SMOKE_ONLY_STAGE_NOT_PRODUCTION")
                self.assertEqual(row["operator_score_use"], "SMOKE_ONLY_SCORE_NOT_PRODUCTION")
                self.assertEqual(row["operator_scope_note"], "controlled_smoke_full_thesis_not_production")
                self.assertTrue(row["base_stage_display"].startswith("FULL_THESIS_"))
                self.assertTrue(row["stage_decision_status_display"].startswith("FULL_THESIS_"))
                self.assertFalse(row["is_full_thesis_stage"])
                self.assertFalse(row["is_full_e2r_score"])
                self.assertTrue(row["is_controlled_smoke_full_thesis_stage"])
            else:
                self.assertEqual(row["operator_stage_use"], "NOT_FULL_THESIS_STAGE")
                self.assertEqual(row["operator_score_use"], "NOT_FULL_E2R_SCORE")
                self.assertEqual(row["operator_scope_note"], "census_event_board_status_not_full_thesis")
                self.assertTrue(row["base_stage_display"].startswith("EVENT_BOARD_"))
                self.assertTrue(row["stage_decision_status_display"].startswith("EVENT_BOARD_"))
                self.assertFalse(row["is_full_thesis_stage"])
                self.assertFalse(row["is_full_e2r_score"])
                self.assertFalse(row.get("is_controlled_smoke_full_thesis_stage") is True)

    def test_pending_material_gaps_are_not_complete(self):
        audit = census_v4_artifacts()["leaf_audit"]
        self.assertEqual(audit["critical_counts"]["pending_material_marked_complete_count"], 0)
        for row in census_v4_artifacts()["stage_rows"]:
            if row["stage_decision_status"] == "PENDING_MATERIAL_GAPS":
                self.assertNotEqual(row["investigation_status"], "COMPLETE")

    def test_red_has_risk_signal(self):
        row = by_symbol(census_v4_artifacts()["stage_rows"], "030350")
        self.assertEqual(row["base_stage"], "Red")
        self.assertEqual(row["canonical_stage"], "3-Red")
        self.assertEqual(row["stage_signal"], "RISK_REVIEW")
        self.assertEqual(row["risk_stage_signal"], "CURRENT_DIRECT_RISK")

    def test_display_label_in_canonical_stage_fails_audit(self):
        with _mutated_stage_rows() as output_root:
            _mutate_stage_row(
                output_root,
                lambda row: row.update({"canonical_stage": "Stage2-Watch"}) if row.get("base_stage") == "Stage2-Watch" else None,
            )
            audit = audit_census_v4_leaf_artifacts(output_root)
        self.assertGreater(audit["critical_counts"]["canonical_stage_invalid_count"], 0)
        self.assertGreater(audit["critical_counts"]["canonical_stage_display_label_count"], 0)
        self.assertEqual(audit["verdict"], "FAIL")

    def test_canonical_stage_trace_mismatch_fails_audit(self):
        with _mutated_stage_rows() as output_root:
            _mutate_stage_row(
                output_root,
                lambda row: row.update({"canonical_stage": "1"}) if row.get("base_stage") == "Stage2-Watch" else None,
            )
            audit = audit_census_v4_leaf_artifacts(output_root)
        self.assertEqual(audit["critical_counts"]["canonical_stage_invalid_count"], 0)
        self.assertEqual(audit["critical_counts"]["canonical_stage_display_label_count"], 0)
        self.assertGreater(audit["critical_counts"]["stage_trace_canonical_stage_mismatch_count"], 0)
        self.assertEqual(audit["verdict"], "FAIL")

    def test_missing_stage_scope_fails_audit(self):
        with _mutated_stage_rows() as output_root:
            _mutate_stage_row(
                output_root,
                lambda row: row.pop("stage_scope", None) if row.get("base_stage") == "Stage2-Watch" else None,
            )
            audit = audit_census_v4_leaf_artifacts(output_root)
        self.assertGreater(audit["critical_counts"]["stage_scope_missing_count"], 0)
        self.assertEqual(audit["verdict"], "FAIL")

    def test_full_thesis_stage_without_full_thesis_scope_fails_audit(self):
        with _mutated_stage_rows() as output_root:
            _mutate_stage_row(
                output_root,
                lambda row: row.update({"full_thesis_stage": "Stage3-Green", "stage_scope": "CENSUS_EVENT_BOARD"})
                if row.get("base_stage") == "Stage1" and row.get("atomic_stage_decision_id")
                else None,
            )
            audit = audit_census_v4_leaf_artifacts(output_root)
        self.assertGreater(audit["critical_counts"]["full_thesis_stage_without_full_thesis_scope_count"], 0)
        self.assertEqual(audit["verdict"], "FAIL")

    def test_missing_operator_scope_alias_fails_audit(self):
        with _mutated_stage_rows() as output_root:
            _mutate_stage_row(
                output_root,
                lambda row: row.pop("operator_stage_use", None) if row.get("base_stage") == "Stage1" else None,
            )
            audit = audit_census_v4_leaf_artifacts(output_root)
        self.assertGreater(audit["critical_counts"]["operator_scope_alias_missing_count"], 0)
        self.assertEqual(audit["verdict"], "FAIL")

    def test_unscoped_event_board_alias_fails_audit(self):
        with _mutated_stage_rows() as output_root:
            _mutate_stage_row(
                output_root,
                lambda row: row.update({"base_stage_display": "Stage1"}) if row.get("base_stage") == "Stage1" else None,
            )
            audit = audit_census_v4_leaf_artifacts(output_root)
        self.assertGreater(audit["critical_counts"]["event_board_operator_alias_unscoped_count"], 0)
        self.assertEqual(audit["verdict"], "FAIL")

    def test_brain_official_partial_scope_is_allowed_with_aliases(self):
        with _mutated_stage_rows() as output_root:
            _mutate_stage_row(
                output_root,
                lambda row: row.update(
                    _with_operator_scope_aliases(
                        {
                            **row,
                            "stage_scope": "BRAIN_OFFICIAL_PARTIAL",
                            "score_scope": "BRAIN_OFFICIAL_CLAIM_BACKED_PARTIAL",
                        }
                    )
                )
                if row.get("base_stage") == "Stage1" and row.get("atomic_stage_decision_id")
                else None,
            )
            audit = audit_census_v4_leaf_artifacts(output_root)
        self.assertEqual(audit["critical_counts"]["stage_scope_invalid_count"], 0)
        self.assertEqual(audit["critical_counts"]["brain_official_operator_alias_unscoped_count"], 0)
        self.assertGreater(audit["critical_counts"]["stage_trace_scope_mismatch_count"], 0)

    def test_event_board_operator_full_thesis_overclaim_fails_audit(self):
        with _mutated_stage_rows() as output_root:
            _mutate_stage_row(
                output_root,
                lambda row: row.update({"operator_stage_use": "FULL_THESIS_STAGE"}) if row.get("base_stage") == "Stage1" else None,
            )
            audit = audit_census_v4_leaf_artifacts(output_root)
        self.assertGreater(audit["critical_counts"]["non_full_thesis_operator_use_overclaim_count"], 0)
        self.assertEqual(audit["verdict"], "FAIL")

class _mutated_stage_rows:
    def __enter__(self) -> Path:
        self._tmp = tempfile.TemporaryDirectory()
        src = census_v4_artifacts()["output_root"]
        self.output_root = Path(self._tmp.name) / "out"
        shutil.copytree(src, self.output_root)
        return self.output_root

    def __exit__(self, exc_type, exc, tb) -> None:
        self._tmp.cleanup()


def _mutate_stage_row(output_root: Path, mutator) -> None:
    path = output_root / "census_stage_status.jsonl"
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    changed = False
    for row in rows:
        before = dict(row)
        mutator(row)
        if row != before:
            changed = True
            break
    if not changed:
        raise AssertionError("no stage row was mutated")
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
