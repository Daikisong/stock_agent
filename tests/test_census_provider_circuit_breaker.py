import unittest

from e2r.census.census_sla import CensusSlaConfig, build_sla_report


class CensusProviderCircuitBreakerTests(unittest.TestCase):
    def test_provider_failure_threshold_opens_circuit(self):
        report = build_sla_report(
            config=CensusSlaConfig(max_provider_failures_before_circuit_breaker=2),
            total_runtime_seconds=1,
            deep_count=0,
            llm_calls=0,
            source_task_count=0,
            provider_failure_count=2,
            runtime_pending_count=0,
        )
        self.assertEqual(report["summary"]["status"], "PARTIAL_WITH_PENDING")
        self.assertEqual(report["summary"]["provider_circuit_open"], True)


if __name__ == "__main__":
    unittest.main()
