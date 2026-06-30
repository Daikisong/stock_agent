import unittest

from e2r.census.census_sla import CensusSlaConfig, build_sla_report


class CensusSlaBudgetTests(unittest.TestCase):
    def test_complete_sla_report(self):
        report = build_sla_report(
            config=CensusSlaConfig(max_total_runtime_seconds=10),
            total_runtime_seconds=1,
            deep_count=0,
            llm_calls=0,
            source_task_count=0,
            provider_failure_count=0,
            runtime_pending_count=0,
        )
        self.assertEqual(report["summary"]["status"], "COMPLETE")


if __name__ == "__main__":
    unittest.main()
