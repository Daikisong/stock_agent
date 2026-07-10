from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class LiveOperationalPackagerTest(unittest.TestCase):
    def test_phase32_audit_records_executed_but_pending_live_operation(self) -> None:
        audit = json.loads(
            (REPO_ROOT / "docs/operational/e2r_live_current_operation_audit.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(audit["official_cli_exit_code"], 0)
        self.assertGreater(audit["full_universe_count"], 1000)
        self.assertGreater(audit["actual_live_source_count"], 0)
        self.assertEqual(audit["evaluator_critical_count_sum"], 0)
        self.assertFalse(audit["production_runtime_ready"])
        self.assertTrue(audit["safety"]["actual_live_execution_performed"])
        self.assertFalse(audit["safety"]["claimless_nonzero_score"])


if __name__ == "__main__":
    unittest.main()
