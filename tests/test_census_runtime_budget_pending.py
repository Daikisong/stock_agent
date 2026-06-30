import unittest

from e2r.census.census_sla import CensusSlaConfig, build_sla_report


class CensusRuntimeBudgetPendingTests(unittest.TestCase):
    def test_runtime_pending_is_not_final_reject(self):
        report = build_sla_report(
            config=CensusSlaConfig(max_total_runtime_seconds=1),
            total_runtime_seconds=2,
            deep_count=0,
            llm_calls=0,
            source_task_count=0,
            provider_failure_count=0,
            runtime_pending_count=1,
        )
        self.assertEqual(report["summary"]["status"], "PARTIAL_WITH_PENDING")


if __name__ == "__main__":
    unittest.main()
