from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from e2r.pro_first.fresh_session.efficiency_audit import (
    DEFAULT_COMPARISON_PATH,
    EXPECTED_FRESH_RECEIPTS,
    EXPECTED_OLD_FREEZE_PATH,
    EXPECTED_OLD_TAXONOMY_PATH,
    REQUIRED_ZERO_COUNTER_KEYS,
    audit_fresh_session_comparison,
    compile_fresh_session_efficiency_audit,
)


ROOT = Path(__file__).resolve().parents[1]


class FreshEfficiencyAuditTest(unittest.TestCase):
    def _comparison(self) -> dict[str, object]:
        return json.loads((ROOT / DEFAULT_COMPARISON_PATH).read_text(encoding="utf-8"))

    def _copy_audit_receipts(self, destination: Path) -> None:
        paths = [
            DEFAULT_COMPARISON_PATH,
            EXPECTED_OLD_FREEZE_PATH,
            EXPECTED_OLD_TAXONOMY_PATH,
            *EXPECTED_FRESH_RECEIPTS.values(),
        ]
        for relative in paths:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, target)

    def test_tracked_p9_comparison_recomputes_to_pass(self) -> None:
        audit = compile_fresh_session_efficiency_audit(ROOT)

        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["critical_count"], 0)
        self.assertEqual(audit["fresh_archetype_count"], 3)
        self.assertEqual(audit["fresh_aggregates"]["accepted_material_count"], 34)
        self.assertEqual(audit["fresh_aggregates"]["initial_material_candidate_count"], 36)
        self.assertEqual(audit["fresh_aggregates"]["accepted_fact_candidate_count"], 56)
        self.assertEqual(tuple(audit["required_zero_counters"]), REQUIRED_ZERO_COUNTER_KEYS)
        self.assertTrue(all(value == 0 for value in audit["required_zero_counters"].values()))

    def test_self_asserted_comparison_total_is_rejected(self) -> None:
        comparison = deepcopy(self._comparison())
        comparison["fresh_aggregates"]["accepted_material_count"] = 36

        audit = audit_fresh_session_comparison(ROOT, comparison)

        self.assertEqual(audit["status"], "FAIL")
        self.assertIn("fresh_aggregate_mismatch", audit["issues"])

    def test_nonzero_source_receipt_counter_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._copy_audit_receipts(root)
            c28_path = root / EXPECTED_FRESH_RECEIPTS[
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"
            ]
            c28 = json.loads(c28_path.read_text(encoding="utf-8"))
            c28["partial_score_published_count"] = 1
            c28_path.write_text(json.dumps(c28), encoding="utf-8")

            audit = compile_fresh_session_efficiency_audit(root)

        self.assertEqual(audit["status"], "FAIL")
        self.assertIn(
            "nonzero_efficiency_counter:partial_score_published_count:1",
            audit["issues"],
        )

    def test_old_run_submit_after_freeze_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._copy_audit_receipts(root)
            freeze_path = root / EXPECTED_OLD_FREEZE_PATH
            freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
            freeze["new_submit_count_after_freeze"] = 1
            freeze_path.write_text(json.dumps(freeze), encoding="utf-8")

            audit = compile_fresh_session_efficiency_audit(root)

        self.assertEqual(audit["status"], "FAIL")
        self.assertIn("old_run_received_submit_after_freeze", audit["issues"])

    def test_missing_source_metric_fails_closed_instead_of_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._copy_audit_receipts(root)
            c28_path = root / EXPECTED_FRESH_RECEIPTS[
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"
            ]
            c28 = json.loads(c28_path.read_text(encoding="utf-8"))
            del c28["source_fetch_count"]
            c28_path.write_text(json.dumps(c28), encoding="utf-8")

            audit = compile_fresh_session_efficiency_audit(root)

        self.assertEqual(audit["status"], "FAIL")
        self.assertIn("fresh_aggregate_source_metric_invalid", audit["issues"])


if __name__ == "__main__":
    unittest.main()
