import unittest

from e2r.production.cutover_v3 import _sla_report_v3
from tests.cutover_v3_test_helpers import fake_v3_base


class CutoverV3SlaRuntimeTests(unittest.TestCase):
    def test_sla_passes_when_average_runtime_is_under_budget_and_bounded(self):
        report = _sla_report_v3(base_bundles=[fake_v3_base(), fake_v3_base("2026-06-29")])
        self.assertEqual(report["summary"]["status"], "SLA_PASS")
        self.assertEqual(report["summary"]["unbounded_fetch_config_count"], 0)


if __name__ == "__main__":
    unittest.main()
