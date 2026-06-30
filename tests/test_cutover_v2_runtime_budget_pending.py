import unittest

from e2r.production.cutover_v2 import _sla_report_v2


class CutoverV2RuntimeBudgetPendingTests(unittest.TestCase):
    def test_sla_budget_state_is_explicit(self):
        report = _sla_report_v2(base={"sla_report": {"summary": {"total_runtime_seconds": 1, "max_total_runtime_seconds": 10}}})
        self.assertEqual(report["summary"]["budget_state"], "COMPLETE")


if __name__ == "__main__":
    unittest.main()
