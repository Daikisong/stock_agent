import unittest

from e2r.production.cutover_v2 import _sla_report_v2


class CutoverV2ProviderCircuitBreakerTests(unittest.TestCase):
    def test_provider_circuit_count_is_explicit(self):
        report = _sla_report_v2(base={"sla_report": {"summary": {"total_runtime_seconds": 1, "max_total_runtime_seconds": 10}}})
        self.assertIn("provider_circuit_open_count", report["summary"])


if __name__ == "__main__":
    unittest.main()
